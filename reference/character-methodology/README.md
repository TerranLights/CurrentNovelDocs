# Character Development Methodology (ported from InnerTepeniaGDD)

**Ported 2026-09-17, as a one-time deliberate fork, not a live sync.** The source (InnerTepeniaGDD's
`Worldspace/Characters/Dolls/Methodology/`) is still actively evolving for the video game. This copy is meant to
diverge from it — the video-game-specific parts (stat-check gating, branching questline mechanics, the
Ending-Shape/companion-perk machinery) need to be reworked into formats that fit prose fiction instead. Do not
assume this folder stays in sync with the source repo; treat it as its own thing going forward.

## What's here

- **`methodology/`** — the 5-stage character-development pipeline plus its `00a`/`00b`/`00c` intake-compression
  layer (the "simple input data → full character detail" mechanism): seed a handful of fields (name, vision,
  Enneagram if known, robot/human, origin) and a Derivation Protocol expands them into the full field set,
  surfacing a clarification question only when a field can't be confidently inferred. Stat/perk/dialogue-check
  game mechanics (MACHINE stats, Perks, Mastery Dividend, Natural/Adjusted 10, Romance Gate checks) and all
  named-character/district-specific InnerTepenia worked examples and roster data have been stripped out and
  relocated (see `relocated-innertepenia-specific-material/`). What remains is setting-agnostic and applies to
  any book, any location, any time period.
- **`book-extractions/`** — distilled, transformative notes mined from the source books (not raw book text):
  `Character_Development_Methodology_-_DRAFT_Ideas.md` (17 craft books, character psychology), the
  Villains/Antiheroes companion file (4 books), the *King, Warrior, Magician, Lover* extraction, and the
  `Book_Extraction_Index.md` that maps which books are extracted where and how deep. Safe to keep tracked in git
  — these are original notes/synthesis, not copies of copyrighted text.
- **`source-books/`** — the actual book files (Enneagram materials + long-term_reference craft books) that feed
  the methodology and the extractions above. **Gitignored** (`reference/character-methodology/source-books/`)
  — full copyrighted texts, several unauthorized scans, kept here locally for convenience only, never committed.
- **`relocated-innertepenia-specific-material/`** — everything InnerTepenia-specific that was pulled out of
  `methodology/` during the 2026-09-17 adaptation pass, preserved rather than deleted: the Calethina/Ayako/
  Favi/Vosora worked examples and illustrations, and the two roster-data seed files (`00d`, `00e`) that turned
  out to be actual working InnerTepenia character data rather than generic templates. Not authoritative here —
  see that folder's own README.

## Time/Length/Span-Based Structure (added 2026-09-17)

Games are non-linear (branching, replayable, no fixed length), so InnerTepeniaGDD's source methodology
deliberately avoids percentage-of-runtime beat placement — every beat is defined by functional role only. Books
are the opposite case: linear, single reading order, knowable total length. Stage 5
(`05_Beats_Paths_Results.md`) now has a "Reversal for Prose" section making percentage/page-based placement the
default, pointing at `reference/story-structure-definitions.md` (this repo, one level up — the fused
Snyder/Bell/Truby/Campbell beat structure with actual placement percentages, previously only linked from
elsewhere in this repo, not from this methodology) as the authoritative skeleton. Also folded in a 1/3-then-2/3
escalating-reveal placement rule mined from the same craft-book extractions, usable now that fixed length is
available. The Overall Process Scaffold and Stage 1 files were updated to point at this instead of the old
"never fixed percentage" framing.

## Still to do

- Decide whether the 00a/00b intake layer's field set needs trimming or renaming for novel characters (no
  per-Doll questline concept, etc.).
- Some incidental Doll/companion-questline terminology may still remain in Stages 2-3 (not yet swept as
  thoroughly as 00a/01/04/05) — worth a pass if it turns up while actually using the methodology.

**Keep the human-character material — don't strip it as part of the "remove video-game-specific bits" pass.**
The user's novels have human characters throughout, and most of this methodology (Enneagram, Want/Need/Lie/Ghost,
the book-extractions) is about psychology generally, not robot/Doll-specific. The "robot/human" seed field in
00a and any robot-specific derivation branches in 00b are the only genuinely Doll-specific content here; the
human-applicable branches of those same files, and virtually everything in Stages 1-3, stay.
