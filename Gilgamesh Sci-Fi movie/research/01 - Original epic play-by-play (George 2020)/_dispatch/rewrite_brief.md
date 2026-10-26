# Brief: the rewrite pass (copyright), 2026-10-25

## Why
**What the law protects.** The events of the 4,000-year-old epic are free for anyone to use; Andrew George's 2020 wording is copyrighted. The play-by-play files must record the original's content in **our own words**.

**What went wrong.** Many files reuse long runs of George's wording: `python3 _dispatch/verbatim_check.py` finds 40-67% of George's text for some sections reappearing in them. Tablets I and VI-VIII show the target level: they were written in the agents' own words and score about 17-25%, partly from names and short formulas.

**Targets:** the verbatim check shows **SOURCE 20% or less** and **FILE 10% or less** for each of your files.

## Keep everything
Keep every scene, beat, specific, line and page reference, gap note, repetition note, comparison line, Differences-table row, Elements-list item, open question and lead. Keep the scene numbering and the checkpoint lines. **Never cut content to hit the target. Rephrase it.** The facts were right; only the wording changes.

## How
1. **Beats:** describe what happens. Don't retell it in the poem's phrasing or rhythm.
2. **Speeches:** use indirect summary, e.g., "Ninsun tells Shamash that…".
3. **Specifics:** write them as terse facts and numbers ("axes of three talents each; a six-rod cedar door"), not copied phrases.
4. **Quotations:** about one per scene at most, and only where the exact wording matters, such as a repeated formula or a famous line. Take the wording from a public-domain translation wherever one has the passage. The files are in `../02 - Public-domain and open sources/`:
   - **Standard version (Tablets I-XII):** R. Campbell Thompson, 1928, files `Thompson 1928 - The Epic of Gilgamish (public domain)/Tablet NN.txt`. Cite as (Thompson 1928, Tablet N, p. X), with the page from the "p. N" markers. Thompson numbers his lines by column and often reads differently from George. Quote him only where his line matches the same moment. If his reading differs in substance, add a short note: "Thompson 1928 reads …".
   - **Old Babylonian Pennsylvania (P) and Yale (Y) tablets:** Jastrow and Clay, 1920, in `Jastrow and Clay 1920 - ... (Project Gutenberg 11000).txt`. Cite as (Jastrow and Clay 1920, Pennsylvania tablet, l. N) or Yale tablet.
   - **Sumerian poems and other fragments:** there is no public-domain translation on hand, so paraphrase. Where the exact wording truly matters, quote at most a few words of George.
   - **George's own wording:** only where no public-domain wording exists (for example, fragments found after 1928). Keep each quotation to one line at most, cited with his line number.
5. **Wikipedia cross-check.** Read the matching section of `../02 .../Wikipedia - Epic of Gilgamesh synopsis (rev 1377304124, CC BY-SA 4.0).txt`. It has sections for each standard-version tablet, the Old Babylonian tablets and the Sumerian poems.
   - **It mentions something your file lacks:** check George, and add it if George has it.
   - **It reads something differently from George 2020:** add a line under Open questions: "Wikipedia's synopsis (revision 1377304124) says …; George 2020 has …".
   - **Paraphrase only.** Don't copy Wikipedia's text: its license would then apply to our files.
6. **Measure:** run `python3 _dispatch/verbatim_check.py "<your file>"` from the research folder after each file. Keep going until both targets are met.

## Checkpoint (third line of each file)
Insert or update **line 3** of the file. Leave lines 1-2 (STATUS, LINE REFS) as they are, and keep them accurate.
- `REWRITE: NOT STARTED`
- `REWRITE: IN PROGRESS (done through scene X.N)`: update after every scene.
- `REWRITE: DONE (SOURCE x%, FILE y%)`: once the targets are met.

**If you are resumed or are a replacement agent:** read line 3, continue from the next scene, and never redo finished scenes.

## Rules
- Edit only your assigned files, and run no git commands that change anything.
- American English, plain language.
- **When done, reply with:**
  - each file's SOURCE and FILE scores before and after;
  - how many Thompson or Jastrow-and-Clay quotations you used, and how many George quotations remain;
  - what the Wikipedia cross-check added or flagged.

## Assignments
| Agent | Files |
|---|---|
| B | SB Tablets III, IV, V |
| D | SB Tablets IX, X, XI |
| E1 | Sumerian 1, 2, 3 |
| E2 | Sumerian 4, 5 |
| F | Old Babylonian fragments (chapter 3); the chapter 4 file only if its own score misses the targets |

**Not needed** (already at target or close): SB Tablets I, II, VI, VII, VIII. Their line 3 reads `REWRITE: NOT NEEDED`.
