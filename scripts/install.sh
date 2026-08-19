#!/usr/bin/env bash
# One-shot install: link cutmax + all sub-skills + platforms.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TARGET="${1:-$HOME/.codex/skills}"

echo "cutmax install"
echo "  root=$ROOT"
echo "  target=$TARGET"

# Link cutmax root skill if not already present
dest="$TARGET/cutmax"
if [ ! -e "$dest" ] && [ ! -L "$dest" ]; then
  ln -s "$ROOT" "$dest"
  echo "linked cutmax -> $dest"
else
  echo "cutmax already at $dest"
fi

# Link all local sub-skills
for d in "$ROOT"/skills/*; do
  [ -d "$d" ] || continue
  name="$(basename "$d")"
  subdest="$TARGET/$name"
  if [ -e "$subdest" ] || [ -L "$subdest" ]; then
    echo "skip existing $subdest"
    continue
  fi
  ln -s "$d" "$subdest"
  echo "linked $name -> $subdest"
done

# Link platform skills
for d in "$ROOT"/platforms/*/; do
  [ -d "$d" ] || continue
  name="$(basename "$d")"
  # skip seedance-and-prompts (prompt pack, not a single skill dir)
  case "$name" in
    seedance-and-prompts)
      for sub in "$d"*/; do
        [ -d "$sub" ] || continue
        subname="$(basename "$sub")"
        subdest="$TARGET/$subname"
        if [ -e "$subdest" ] || [ -L "$subdest" ]; then
          echo "skip existing $subdest"
          continue
        fi
        ln -s "$sub" "$subdest"
        echo "linked $subname -> $subdest"
      done
      ;;
    *)
      subdest="$TARGET/$name"
      if [ -e "$subdest" ] || [ -L "$subdest" ]; then
        echo "skip existing $subdest"
        continue
      fi
      ln -s "$d" "$subdest"
      echo "linked $name -> $subdest"
      ;;
  esac
done

echo ""
echo "done. trigger with /cutmax or mention 'cutmax' in agent chat."
echo "sub-skills linked to $TARGET"
