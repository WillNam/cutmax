#!/usr/bin/env python3
"""Photo → process still → blank → sketch (pencil hand) → color (brush hand) → art.

Free/local only. Avoids washed-art-as-blank (the 'one image looping' bug).
"""

from __future__ import annotations

import argparse
import math
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageOps

FPS = 30
W, H = 1080, 1440

PHOTO_SEC = 2.4
FADE_SEC = 0.3
HOLD_SEC = 0.55
TO_BLANK_SEC = 0.25
SKETCH_SEC = 3.2
COLOR_SEC = 2.8
ART_HOLD_SEC = 2.0

EDGE_Y0, EDGE_Y1 = 500, 1000
STROKE_AMP = 55
STROKE_N = 6.5
HAND_SCALE = 0.50

SKILL_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SPRITES = SKILL_ROOT / "assets" / "hand-sprites"


def sec(n: float) -> int:
    return max(1, round(n * FPS))


def smooth(t: float) -> float:
    t = max(0.0, min(1.0, t))
    return t * t * (3.0 - 2.0 * t)


def load_rgb(path: Path) -> Image.Image:
    return Image.open(path).convert("RGB").resize((W, H), Image.Resampling.LANCZOS)


def to_sketch(art: Image.Image) -> Image.Image:
    g = ImageOps.autocontrast(art.convert("L"))
    g = ImageEnhance.Contrast(g).enhance(1.8)
    edges = g.filter(ImageFilter.FIND_EDGES)
    edges = ImageEnhance.Brightness(edges).enhance(1.4)
    return Image.blend(g.convert("RGB"), ImageOps.invert(edges).convert("RGB"), 0.18)


def blank_page() -> Image.Image:
    page = Image.new("RGB", (W, H), (248, 246, 242))
    d = ImageDraw.Draw(page)
    d.rectangle((72, 48, W - 72, H - 48), outline=(230, 226, 220), width=2)
    return page


def ken(img: Image.Image, p: float, strength: float = 0.04) -> Image.Image:
    s = 1.0 + strength * smooth(p)
    nw, nh = int(W * s), int(H * s)
    r = img.resize((nw, nh), Image.Resampling.LANCZOS)
    x = (nw - W) // 2
    y = int((nh - H) * 0.42)
    return r.crop((x, y, x + W, y + H))


def blend(a: Image.Image, b: Image.Image, t: float) -> Image.Image:
    return Image.blend(a, b, max(0.0, min(1.0, t)))


def reveal(base: Image.Image, overlay: Image.Image, p: float) -> tuple[Image.Image, float]:
    cut = int(W * max(0.0, min(1.0, p)))
    out = base.copy()
    if cut > 0:
        out.paste(overlay.crop((0, 0, cut, H)), (0, 0))
    return out, float(cut)


def load_hand(sprites: Path, name: str, scale: float) -> tuple[Image.Image, tuple[int, int]]:
    tip_file = sprites / f"{name}.tip.txt"
    img_file = sprites / f"{name}.png"
    if not img_file.exists() or not tip_file.exists():
        raise FileNotFoundError(
            f"Missing hand sprite {img_file} or {tip_file}. "
            "Copy hand-pencil.png / hand-brush.png + .tip.txt into skill assets/hand-sprites/"
        )
    tip = [int(x) for x in tip_file.read_text().strip().split(",")]
    im = Image.open(img_file).convert("RGBA")
    nw, nh = int(im.width * scale), int(im.height * scale)
    im = im.resize((nw, nh), Image.Resampling.LANCZOS)
    return im, (int(tip[0] * scale), int(tip[1] * scale))


def paste_hand(
    base: Image.Image,
    hand: Image.Image,
    tip: tuple[int, int],
    xy: tuple[float, float],
    op: float = 1.0,
) -> Image.Image:
    out = base.convert("RGBA")
    layer = hand
    if op < 0.999:
        a = layer.split()[3].point(lambda v: int(v * op))
        layer = layer.copy()
        layer.putalpha(a)
    out.alpha_composite(layer, (int(xy[0] - tip[0]), int(xy[1] - tip[1])))
    return out.convert("RGB")


def tip_path(p: float, cut: float) -> tuple[float, float]:
    y = (
        EDGE_Y0
        + (EDGE_Y1 - EDGE_Y0) * p
        + math.sin(p * STROKE_N * 2 * math.pi) * STROKE_AMP
        + math.sin(p * 21) * 5
    )
    return max(16.0, cut - 6.0), y


def fade_op(i: int, n: int, inn: int = 4, out: int = 8) -> float:
    if i < inn:
        return (i + 1) / inn
    if i > n - out:
        return max(0.0, (n - i) / out)
    return 1.0


def render_cycle(
    photo: Path,
    draw: Path,
    art: Path,
    frames: Path,
    pencil: Image.Image,
    tip_p: tuple[int, int],
    brush: Image.Image,
    tip_b: tuple[int, int],
) -> int:
    photo_i, draw_i, art_i = load_rgb(photo), load_rgb(draw), load_rgb(art)
    sketch = to_sketch(art_i)
    blank = blank_page()
    frames.mkdir(parents=True, exist_ok=True)
    for f in frames.glob("frame_*.jpg"):
        f.unlink()
    idx = 0

    for i in range(sec(PHOTO_SEC)):
        ken(photo_i, i / max(1, sec(PHOTO_SEC) - 1), 0.05).save(
            frames / f"frame_{idx:05d}.jpg", quality=93
        )
        idx += 1

    last = ken(photo_i, 1.0, 0.05)
    for i in range(sec(FADE_SEC)):
        blend(last, draw_i, smooth((i + 1) / sec(FADE_SEC))).save(
            frames / f"frame_{idx:05d}.jpg", quality=93
        )
        idx += 1

    for _ in range(sec(HOLD_SEC)):
        draw_i.save(frames / f"frame_{idx:05d}.jpg", quality=93)
        idx += 1

    for i in range(sec(TO_BLANK_SEC)):
        blend(draw_i, blank, smooth((i + 1) / sec(TO_BLANK_SEC))).save(
            frames / f"frame_{idx:05d}.jpg", quality=93
        )
        idx += 1

    n = sec(SKETCH_SEC)
    for i in range(n):
        p = (i + 1) / n
        composed, cut = reveal(blank, sketch, p)
        frame = paste_hand(composed, pencil, tip_p, tip_path(p, cut), fade_op(i, n))
        frame.save(frames / f"frame_{idx:05d}.jpg", quality=93)
        idx += 1

    sketch_full, _ = reveal(blank, sketch, 1.0)
    n = sec(COLOR_SEC)
    for i in range(n):
        p = (i + 1) / n
        composed, cut = reveal(sketch_full, art_i, p)
        frame = paste_hand(composed, brush, tip_b, tip_path(p, cut), fade_op(i, n, 3, 6))
        frame.save(frames / f"frame_{idx:05d}.jpg", quality=93)
        idx += 1

    for i in range(sec(ART_HOLD_SEC)):
        ken(art_i, i / max(1, sec(ART_HOLD_SEC) - 1), 0.03).save(
            frames / f"frame_{idx:05d}.jpg", quality=93
        )
        idx += 1
    return idx


def encode(frames: Path, out: Path) -> None:
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-framerate",
            str(FPS),
            "-i",
            str(frames / "frame_%05d.jpg"),
            "-c:v",
            "libx264",
            "-crf",
            "18",
            "-pix_fmt",
            "yuv420p",
            "-an",
            str(out),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def concat(files: list[Path], out: Path) -> None:
    lst = out.parent / "concat-list.txt"
    lst.write_text("\n".join(f"file '{p}'" for p in files) + "\n", encoding="utf-8")
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(lst),
            "-c:v",
            "libx264",
            "-crf",
            "18",
            "-pix_fmt",
            "yuv420p",
            "-an",
            str(out),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def parse_cycles(args: argparse.Namespace) -> list[tuple[Path, Path, Path]]:
    cycles: list[tuple[Path, Path, Path]] = []
    if args.cycle:
        for group in args.cycle:
            if len(group) != 3:
                raise SystemExit("--cycle needs exactly 3 paths: photo draw art")
            cycles.append((Path(group[0]), Path(group[1]), Path(group[2])))
    return cycles


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--work-dir", type=Path, required=True)
    ap.add_argument(
        "--cycle",
        nargs=3,
        action="append",
        metavar=("PHOTO", "DRAW", "ART"),
        help="Repeatable trio of photo / draw-process / finished art",
    )
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument(
        "--sprites",
        type=Path,
        default=None,
        help="Directory with hand-pencil.png, hand-brush.png and .tip.txt files",
    )
    args = ap.parse_args()
    cycles = parse_cycles(args)
    if not cycles:
        raise SystemExit("Provide at least one --cycle PHOTO DRAW ART")

    sprites = args.sprites
    if sprites is None:
        # Prefer skill assets, then proven trial sprites
        candidates = [
            DEFAULT_SPRITES,
            Path(
                "/Users/minnan/Projects/conan-digital-human/outputs/"
                "skill-trials-2026-08-06/handdrawn/draw-alive-work/hand-sprites"
            ),
        ]
        sprites = next((c for c in candidates if (c / "hand-pencil.png").exists()), None)
        if sprites is None:
            raise SystemExit("No hand sprites found. Pass --sprites DIR")

    pencil, tip_p = load_hand(sprites, "hand-pencil", HAND_SCALE)
    brush, tip_b = load_hand(sprites, "hand-brush", HAND_SCALE * 0.95)

    work = args.work_dir
    work.mkdir(parents=True, exist_ok=True)
    cycle_mp4s: list[Path] = []
    for i, (photo, draw, art) in enumerate(cycles, 1):
        tag = f"cycle-{i:02d}"
        print(f"== {tag} ==")
        frames = work / tag / "frames"
        n = render_cycle(photo, draw, art, frames, pencil, tip_p, brush, tip_b)
        print(f"  frames {n} ({n / FPS:.1f}s)")
        mp4 = work / tag / "cycle.mp4"
        encode(frames, mp4)
        cycle_mp4s.append(mp4)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    if len(cycle_mp4s) == 1:
        subprocess.run(["cp", "-f", str(cycle_mp4s[0]), str(args.out)], check=True)
    else:
        concat(cycle_mp4s, args.out)
    print(f"DONE {args.out}")


if __name__ == "__main__":
    main()
