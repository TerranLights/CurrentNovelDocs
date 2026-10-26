# Brief: play-by-play of the Epic of Gilgamesh (George 2020), 2026-10-25

## The project
The author is planning a film that retells the Epic of Gilgamesh. They want to stay as true as possible to the original story, so the plot will be worked out only after there is an exact, complete play-by-play of the original. **This pass is research only:** what happens in the text, in order, and where it is in the book.
- **No adaptation.** Do not suggest adaptations, modern or science-fiction equivalents, themes, your own interpretations, or anything about the film.
- **Nothing from the author's fictional universe.** It is irrelevant here.

## The source
Andrew George, translator, *The Epic of Gilgamesh: The Babylonian Epic Poem and Other Texts in Akkadian and Sumerian*, 2nd ed., Penguin Classics, 2020.

**Extracted text:** `_source_text (local only, not in git)/`, next to `_dispatch/` in this research folder, with one `.txt` file per section.
- **It is git-ignored.** It is the full copyrighted translation, so it never goes into a commit.
- **An earlier copy exists in the session scratchpad.** It is `/tmp/claude-1000/-home-kuroskalacs-Documents-Doll-Fi-media-Literature-books-CurrentNovelDocs/3d728365-b74f-46ea-8b81-16f2bbd67a4d/scratchpad/gilgamesh_epub/text/`, and it is identical. It may vanish after a reboot; the repo copy is the one to rely on.
- **If the folder is missing, recreate it:** `python3 "<this research folder>/_dispatch/extract_epub.py" "/home/kuroskalacs/Documents/ebooks/The Epic of Gilgamesh The Babylonian Epic Poem - Andrew George (2nd ed.) [2020].epub" "<this research folder>/_source_text (local only, not in git)"`.

**Markings in the extracted text:**
- `[square brackets]`: George's restorations of broken text.
- `_underscores_`: italics in the book. Read `00_note_on_translation.txt` for what George says italics mean, and use his meaning.
- `……`: text that is lost and not restored.
- `{p.N}`: printed page N begins here.
- `{l.I 5}`: George's margin line number (tablet I, line 5). It is printed every five lines, and some carry a manuscript siglum or a prime (e.g., `{l.Nc 4´}`, `{l.OB Ni20´}`).
- **Two leading spaces:** a verse line George prints indented. In the Akkadian epic this is usually the second line of a couplet. Read George's note on the translation for how indented lines relate to the line count.

**Read first:** `00_note_on_translation.txt` and `00_dramatis_personae.txt`. You may consult `00_introduction.txt`, `GLOSSARY_proper_nouns.txt` and `APP_from_tablet_to_translation.txt` for George's explanations; cite the page.

## What to write
**Header:**
```
STATUS: IN PROGRESS (next: scene I.4, from {l.I 95})
LINE REFS: CHECKED
# Tablet I. The Coming of Enkidu: play-by-play
Research notes, 2026-10-25. Source: George 2020, chapter 1. A record of the original only; nothing here is adaptation or decision.
```

**The two checkpoint lines must stay the first two lines of the file.** A resumed or replacement agent reads only these to know where to start.
- **Line 1, `STATUS`.** Update it after every scene. It names the next scene and the source marker where that scene begins, so a fresh agent can find its place in the text. Write `STATUS: COMPLETE` when the file is done.
- **Line 2, `LINE REFS`.** Write `LINE REFS: CHECKED` once every line reference in the file comes from the `{l.…}` markers. The first extraction (before 2026-10-25, about 17:50) lost those markers, so a file begun before then starts as `LINE REFS: NOT YET CHECKED` until its references are checked and corrected against the markers. While a correction pass is underway, write `LINE REFS: CHECKING (done through scene I.6)`, so that a cutoff mid-pass can resume as well.
- **A file is finished only when it reads `STATUS: COMPLETE` and `LINE REFS: CHECKED`.**

**Then, in order:**
1. **George's synopsis.** Paraphrase the italic summary at the head of the tablet or poem.
2. **Scenes**, numbered I.1, I.2, and so on. Start a new scene when the place, the people present or the time changes, or when a new speech begins with a new purpose. For each scene give:
   - **Title, lines and pages.** Take the lines from the margin numbers and give a range, saying "about" where a marker is missing.
   - **Where and when:** the time of day, how long after the previous scene, and any durations as stated.
   - **Who:** who is present, and who speaks.
   - **Play-by-play:** numbered beats, in order, in your own words. Include every action and every speech, written as speaker → listener: the gist. Include what is only dreamed, retold, prophesied or prayed, and mark it as such.
   - **Specifics, exactly as the text gives them:** objects, materials, numbers, measurements, durations, colors, animals, places, titles and epithets.
   - **Short quotations:** only where the exact wording matters, such as a famous line, a repeated formula or a key statement. Use a line or two at most each, cited (e.g., I 8). Keep the total small: the repo is on GitHub and the translation is under copyright.
   - **Gaps:** lines that are lost or broken. Separate what George restores in brackets from what is plain text, and give his notes on what the lost part probably contained (cited).
   - **Repetitions:** formulaic repeats (dreams retold, messages repeated word for word). Say that the passage repeats, and where.
3. **Elements list** for the whole tablet or poem, each item with its scene refs:
   - characters (with their epithets as given)
   - places
   - objects and materials
   - creatures
   - gods and what they do
   - numbers and time
   - dreams and omens
   - customs and rituals
4. **Open questions and uncertainties:** where the text is unclear or damaged, or where George flags doubt.
5. **Leads (labeled as leads, optional):** observations about the text's own structure only (for example, "the dream pattern repeats"). No adaptation ideas.

**Extra, for the variant files only (Sumerian poems, Old Babylonian and other early fragments):**
- **A comparison line for every scene.** Under "Compared with the standard version," give the standard-version tablet and lines it parallels; check this against the `SB_*.txt` files. Then say what differs:
  - events added or missing;
  - names (e.g., Bilgames, Huwawa, Inanna, Enki, Utu);
  - numbers;
  - who speaks;
  - outcomes.

  Write "no counterpart in the standard version" where there is none.
- **End the file with a Differences table** with three columns: Passage | Parallels in the standard version | What differs.

## Rules
- Write **only your assigned files**, in `Gilgamesh Sci-Fi movie/research/01 - Original epic play-by-play (George 2020)/`. Edit nothing else, and run no git commands that change anything.
- No web research is needed; the book is the source.
- American English, plain language. Mark uncertainty with ⚠️.
- **Resumable:** create the file early (header and synopsis), then add to it scene by scene, updating the checkpoint lines each time, so a cutoff loses at most one scene.
- **If you are resumed or are a replacement agent:**
  1. Read your files' first two lines.
  2. Read the last scene written, to match its style and numbering.
  3. Continue from the STATUS line, then finish any LINE REFS check.
  4. Never restart a file from scratch, and never rewrite finished scenes except to correct line references.
- **When done, reply with:** your file path(s), the scene count per file, and the five most easily missed details in your section (as facts, not suggestions).
