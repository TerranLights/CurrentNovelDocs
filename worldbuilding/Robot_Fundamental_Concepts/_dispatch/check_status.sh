#!/usr/bin/env bash
# Show the STATUS line of every notes file in this pass.
cd "$(dirname "$0")/.." || exit 1
find . -name "Notes - *GDD zodiac documentation*.md" -o -name "00 - Cross-cutting notes (GDD zodiac documentation).md" | sort | while read -r f; do
  printf '%-95s %s\n' "$f" "$(grep -m1 '^STATUS:' "$f")"
done
echo "Expected: 12 sign files + 1 cross-cutting + 1 Ophiuchus/Hub = 14"
