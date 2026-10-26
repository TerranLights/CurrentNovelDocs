# The original epic, play by play (George 2020): README and progress

**What this is:** a scene-by-scene record of the Epic of Gilgamesh as Andrew George translates it (Penguin Classics, 2nd ed., 2020). It is the base the author chose on 2026-10-25. The author's approach: the film's full plot is worked out only after this play-by-play exists, balancing faithfulness to the original against the needs of science fiction and the Tepenian universe (`../../Author Statements (2026-10-25).md`).

**What it is not:** adaptation. These files record the original only. Matching original elements to the film comes later, in the 05:00-14:59 window, with the author.

## Layout
- **`SB Tablet ...` files:** the standard Babylonian version, Tablets I-XI. Tablet XII is not part of the epic; George gives it in chapter 2, after "Gilgamesh and the Netherworld."
- **`Sumerian ...` files:** the five older Sumerian poems.
- **`Old Babylonian ...` and `Other early fragments ...` files:** the early versions.
- **The variant files** each end with a table of how they differ from the standard version.
- **`_dispatch/`:** the brief, the assignments and the extraction script. The extracted text itself stays outside the repo because it is the copyrighted translation.

## Status
**The live status is in the files themselves.** Run `bash _dispatch/check_status.sh` to print every output file's two checkpoint lines; this table is only a summary. A file is finished when it reads `STATUS: COMPLETE` and `LINE REFS: CHECKED`.

| Agent | Files | Status |
|---|---|---|
| A | SB Tablets I-II | complete (16 + 16 scenes) |
| B | SB Tablets III-V | complete (11 + 11 + 20 scenes) |
| C | SB Tablets VI-VIII | complete (15 + 14 + 11 scenes) |
| D | SB Tablets IX-XI (and the Tablet XII note) | complete (8 + 12 + 17 scenes) |
| E1 | Sumerian poems 1-3 | complete (8 + 25 + 15 scenes) |
| E2 | Sumerian poems 4-5 (and the Akkadian Tablet XII) | complete (24 + 16 scenes) |
| F | Old Babylonian and other early fragments | running |

## The rewrite pass (copyright), 2026-10-25, about 18:45 to 22:30: COMPLETE
**Why.** Many files reproduced long runs of George's wording. `python3 _dispatch/verbatim_check.py` measured 40-67% of George's text for some sections.

**What the author asked for.** Free sources folded into the notes. The free sources found are in `../02 - Public-domain and open sources/`; its README covers them and the copyrighted outlines that were ruled out:
- Thompson's 1928 public-domain translation;
- Jastrow and Clay's 1920 Old Babylonian tablets;
- Wikipedia's tablet-by-tablet synopsis (CC BY-SA).

**What the pass does** (instructions in `_dispatch/rewrite_brief.md`):
- rewrites twelve files (Tablets III-V and IX-XI, Sumerian 1-5, the Old Babylonian file) in the agents' own words, keeping every fact;
- quotes the public-domain translations in place of George wherever they have the passage;
- cross-checks each file against Wikipedia's synopsis.

**Target:** SOURCE 20% or less, FILE 10% or less. Line 3 of every file tracks it: `REWRITE: NOT NEEDED / NOT STARTED / IN PROGRESS (done through …) / DONE (scores)`.

**Result.**
- **All 18 files** read `STATUS: COMPLETE`, `LINE REFS: CHECKED`, and `REWRITE: DONE` or `NOT NEEDED`.
- **Scenes:** 295 in all, every one kept through the rewrite.
- **Copied wording:**
  - SOURCE scores are now 0-10% for the rewritten files.
  - Tablets I, II, VI-VIII stay at 17-25%; these were not rewritten.
  - Run `python3 _dispatch/verbatim_check.py` for current figures.
- **Quotations:**
  - Thompson 1928 and Jastrow and Clay 1920 replace George's wording wherever they have the passage.
  - The George quotations that remain are short, a few words each, used only where no public-domain text exists (fragments found after 1928, the Sumerian poems).
  - Where Thompson's 1928 reading differs in substance from George's, the file says "Thompson 1928 reads …".
- **Wikipedia cross-check (revision 1377304124):** it added nothing George lacks. It flagged several dozen differences of reading, logged under each file's Open questions; a few are wrong against George 2020, e.g. 300 men in the pits.
- **Interruption:** a usage cutoff stopped all five rewrite agents at about 21:00. They resumed from their checkpoint lines at 21:41, and nothing was lost.

## How the work survives a usage cutoff
- **Every output file starts with three checkpoint lines**, updated after each scene (format in `_dispatch/brief.md` and `_dispatch/rewrite_brief.md`). The third line, `REWRITE`, tracks the copyright rewrite pass.
- The first two lines:
  - `STATUS` names the next scene and the source line where it begins.
  - `LINE REFS` says whether the file's line references have been checked against the margin numbers. The first extraction lost those numbers; the script was fixed 2026-10-25 at about 17:50.
- **The source text sits in a durable local folder:** `_source_text (local only, not in git)/` here. It is git-ignored, because it is the copyrighted translation. If it is gone, `_dispatch/extract_epub.py` recreates it; the command is in the brief.
- **Briefs, assignments, the extraction script, the status check, the verbatim check and the resume prompts** are all in `_dispatch/`.
- **The extraction script was fixed twice on 2026-10-25.** It first lost the margin numbers, then dropped primed numbers such as `Nc 4´` and the indentation. All 1,085 margin numbers now come through; re-extract if the source folder is older.

## Resume procedure (after a usage cutoff)
1. Run `bash _dispatch/check_status.sh`.
2. For each agent whose files aren't finished:
   - **Same session:** resume the agent by message, using the first prompt in `_dispatch/resume_prompt.md`.
   - **New session or unreachable agent:** start a replacement agent with the second prompt there.
3. Nothing is restarted from scratch. Agents continue from the checkpoint lines.

## Next steps (PROPOSED)
1. **Done, 2026-10-25:** `../03 - Every beat of the epic, in order.md` lists every beat of Tablets I-XI in order (151 scenes, 867 beats). It adds Tablet XII as an appendix and a list of the episodes found only in older versions. Still to do: one cross-version table merging the variant files' Differences tables.
2. The Tepenian requirements list: the fixed facts the film must fit, drawn from canon and the author's rulings.
3. In the 05:00-14:59 window, with the author: the change ledger. Each original element gets one label (kept as is, given a sci-fi equivalent, changed for Tepenian canon, or cut), with a reason.
