#!/usr/bin/env python3
"""How much of George's copyrighted wording each play-by-play file reproduces.

Run from the research folder:  python3 _dispatch/verbatim_check.py [file.md ...]
(no arguments = every output file)

Two measures, both counting only runs of 6+ words copied verbatim:
  SOURCE  share of George's text for that section that reappears in the file
  FILE    share of the file's own words that sit inside copied runs
Target for the rewrite pass (2026-10-25): SOURCE 20% or less, FILE 10% or less.
Names and short repeated formulas make up part of any score, so the files that
were written in the agents' own words from the start (Tablets I, VI-VIII) score
about 17-25% SOURCE.
"""
import glob, os, re, sys

S = "_source_text (local only, not in git)/"
PAIRS = {
    "SB Tablet I - The Coming of Enkidu.md": ["SB_01_Tablet_I"],
    "SB Tablet II - The Taming of Enkidu.md": ["SB_02_Tablet_II"],
    "SB Tablet III - Preparations for the Expedition.md": ["SB_03_Tablet_III"],
    "SB Tablet IV - The Journey to the Forest of Cedar.md": ["SB_04_Tablet_IV"],
    "SB Tablet V - The Combat with Humbaba.md": ["SB_05_Tablet_V"],
    "SB Tablet VI - Ishtar and the Bull of Heaven.md": ["SB_06_Tablet_VI"],
    "SB Tablet VII - The Death of Enkidu.md": ["SB_07_Tablet_VII"],
    "SB Tablet VIII - The Funeral of Enkidu.md": ["SB_08_Tablet_VIII"],
    "SB Tablet IX - The Wanderings of Gilgamesh.md": ["SB_09_Tablet_IX"],
    "SB Tablet X - At the Edge of the World.md": ["SB_10_Tablet_X"],
    "SB Tablet XI - Immortality Denied.md": ["SB_11_Tablet_XI", "SB_12_Tablet_XII"],
    "Sumerian 1 - Gilgamesh and Akka.md": ["SUM_1_Gilgamesh_and_Akka"],
    "Sumerian 2 - Gilgamesh and Huwawa.md": ["SUM_2_Gilgamesh_and_Huwawa"],
    "Sumerian 3 - Gilgamesh and the Bull of Heaven.md": ["SUM_3_Gilgamesh_and_the_Bull_of_Heaven"],
    "Sumerian 4 - Gilgamesh and the Netherworld (and Tablet XII).md": ["SUM_4_Gilgamesh_and_the_Netherworld"],
    "Sumerian 5 - The Death of Gilgamesh.md": ["SUM_5_The_Death_of_Gilgamesh"],
    "Old Babylonian fragments (chapter 3).md": ["OB_all_fragments"],
    "Other early fragments - Ugarit, Hattusa, Emar, Megiddo, Sealand (chapter 4).md": ["MISC_all_fragments"],
}
N = 6
norm = lambda t: re.findall(r"[a-z0-9’']+", re.sub(r"\{[^}]*\}|_|\[|\]", " ", t.lower()))
grams = lambda w: {tuple(w[i:i + N]) for i in range(len(w) - N + 1)}

def covered(words, other):
    hit = [False] * len(words)
    for i in range(len(words) - N + 1):
        if tuple(words[i:i + N]) in other:
            for j in range(i, i + N):
                hit[j] = True
    return 100 * sum(hit) / max(len(words), 1)

files = sys.argv[1:] or [f for f in PAIRS if os.path.exists(f)]
for f in files:
    f = os.path.basename(f)
    if f not in PAIRS:
        print("(no source mapping)  %s" % f); continue
    src = norm(" ".join(open(S + s + ".txt", encoding="utf-8").read() for s in PAIRS[f]))
    out = norm(open(f, encoding="utf-8").read())
    print("SOURCE %5.1f%%  FILE %5.1f%%  %s" % (covered(src, grams(out)), covered(out, grams(src)), f))
