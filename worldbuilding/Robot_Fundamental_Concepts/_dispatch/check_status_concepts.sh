#!/usr/bin/env bash
# Show the STATUS line and concept count of every low-level concepts file.
cd "$(dirname "$0")/.." || exit 1
find . -name "Low-level concepts (2026-10-30).md" | sort | while read -r f; do
  n=$(grep -c '^| [a-z]' "$f")
  printf '%-60s %-45s rows=%s\n' "$(echo "$f" | cut -d/ -f3)" "$(grep -m1 '^STATUS:' "$f")" "$n"
done
echo "Expected: 12 files"
