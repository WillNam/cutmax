#!/usr/bin/env bash
# Link official platform skills (Seedance, ChatCut, Pireel, prompt packs).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TARGET="${1:-$HOME/.codex/skills}"
mkdir -p "$TARGET"

link_one() {
  local src="$1"
  local name
  name="$(basename "$src")"
  local dest="$TARGET/$name"
  if [ -e "$dest" ] || [ -L "$dest" ]; then
    echo "skip existing $dest"
    return
  fi
  ln -s "$src" "$dest"
  echo "linked $name"
}

echo "Linking platforms into: $TARGET"
echo "(Official tools may use credits — confirm before paid generation.)"

# Top-level platform skills
for d in "$ROOT"/platforms/*; do
  [ -d "$d" ] || continue
  name="$(basename "$d")"
  case "$name" in
    seedance-and-prompts) continue ;;
    *) link_one "$d" ;;
  esac
done

# Prompt packs inside seedance-and-prompts
PROMPT_ROOT="$ROOT/platforms/seedance-and-prompts"
if [ -d "$PROMPT_ROOT" ]; then
  for d in "$PROMPT_ROOT"/*; do
    [ -d "$d" ] || continue
    link_one "$d"
  done
fi

echo done
