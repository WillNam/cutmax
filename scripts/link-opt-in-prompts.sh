#!/usr/bin/env bash
# Deprecated alias — platforms are first-class now.
echo "note: link-opt-in-prompts.sh is an alias of link-platforms.sh"
exec "$(cd "$(dirname "$0")" && pwd)/link-platforms.sh" "$@"
