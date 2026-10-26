#!/usr/bin/env bash
# Prints the two checkpoint lines of every expected output file.
# Usage: bash _dispatch/check_status.sh   (from anywhere)
cd "$(dirname "$0")/.." || exit 1
files=(
 "A|SB Tablet I - The Coming of Enkidu.md"
 "A|SB Tablet II - The Taming of Enkidu.md"
 "B|SB Tablet III - Preparations for the Expedition.md"
 "B|SB Tablet IV - The Journey to the Forest of Cedar.md"
 "B|SB Tablet V - The Combat with Humbaba.md"
 "C|SB Tablet VI - Ishtar and the Bull of Heaven.md"
 "C|SB Tablet VII - The Death of Enkidu.md"
 "C|SB Tablet VIII - The Funeral of Enkidu.md"
 "D|SB Tablet IX - The Wanderings of Gilgamesh.md"
 "D|SB Tablet X - At the Edge of the World.md"
 "D|SB Tablet XI - Immortality Denied.md"
 "E1|Sumerian 1 - Gilgamesh and Akka.md"
 "E1|Sumerian 2 - Gilgamesh and Huwawa.md"
 "E1|Sumerian 3 - Gilgamesh and the Bull of Heaven.md"
 "E2|Sumerian 4 - Gilgamesh and the Netherworld (and Tablet XII).md"
 "E2|Sumerian 5 - The Death of Gilgamesh.md"
 "F|Old Babylonian fragments (chapter 3).md"
 "F|Other early fragments - Ugarit, Hattusa, Emar, Megiddo, Sealand (chapter 4).md"
)
done_n=0; total=${#files[@]}
for row in "${files[@]}"; do
  agent=${row%%|*}; f=${row#*|}
  if [[ ! -f "$f" ]]; then printf "%-3s %-72s MISSING\n" "$agent" "$f"; continue; fi
  s=$(sed -n 1p "$f"); l=$(sed -n 2p "$f" | grep -o "LINE REFS:.*" || echo "LINE REFS: (no line)")
  r=$(sed -n 3p "$f" | grep -o "REWRITE:.*" || echo "REWRITE: (no line)")
  [[ "$s" == "STATUS: COMPLETE"* && "$l" == "LINE REFS: CHECKED"* && ( "$r" == "REWRITE: DONE"* || "$r" == "REWRITE: NOT NEEDED"* ) ]] && done_n=$((done_n+1))
  printf "%-3s %-60.60s %-34.34s | %-20.20s | %s\n" "$agent" "$f" "$s" "$l" "$r"
done
src="_source_text (local only, not in git)"
[[ -d "$src" ]] || echo "NOTE: $src is missing; recreate it (see _dispatch/brief.md)."
echo "Fully done (STATUS COMPLETE + LINE REFS CHECKED + REWRITE DONE or NOT NEEDED): $done_n of $total"
