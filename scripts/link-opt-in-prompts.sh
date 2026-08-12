#!/usr/bin/env bash
# Explicitly link opt-in prompt-for-paid-models skills.
# These target third-party paid video products; not part of free default.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$ROOT/opt-in/prompt-for-paid-models"
TARGET="${1:-$HOME/.codex/skills}"
mkdir -p "$TARGET"
echo "Linking opt-in paid-model prompt skills into: $TARGET"
echo "(These do not call APIs; rendering on Seedance/Kling/etc. may cost credits.)"
for d in "$SRC"/*; do
  [ -d "$d" ] || continue
  name="$(basename "$d")"
  [ "$name" = "README.md" ] && continue
  dest="$TARGET/$name"
  if [ -e "$dest" ] || [ -L "$dest" ]; then
    echo "skip existing $dest"
    continue
  fi
  ln -s "$d" "$dest"
  echo "linked $name"
done
echo done
