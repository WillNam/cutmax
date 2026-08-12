#!/usr/bin/env bash
# Symlink every cutmax skill into a target skills directory.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TARGET="${1:-$HOME/.codex/skills}"
mkdir -p "$TARGET"
for d in "$ROOT"/skills/*; do
  [ -d "$d" ] || continue
  name="$(basename "$d")"
  dest="$TARGET/$name"
  if [ -e "$dest" ] || [ -L "$dest" ]; then
    echo "skip existing $dest"
    continue
  fi
  ln -s "$d" "$dest"
  echo "linked $name -> $dest"
done
echo "done. target=$TARGET"
