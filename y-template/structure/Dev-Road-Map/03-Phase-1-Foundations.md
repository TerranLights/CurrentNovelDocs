# Phase 1 — Foundations

**Prerequisite:** All Blocking Decisions resolved.

**What this phase does:** Fixes the tentative facts everything else depends on — where and when this story takes place, what it's called, how it's told. Nothing in Phase 2 onward should require guessing at any of these.

---

## 1.1 — Setting & Timeline Placement

Confirm where this novel sits in the shared universe:
- What year/era is this story set in? Cross-check against the shared timeline (`reference/story-structure-definitions.md` for the beat framework; the shared universe-timeline reference for actual in-world dates/history).
- What does that placement *rule out*? (E.g., Streetside Harmonies is set in 2149 — over 150 years before robots gain legal personhood in this universe's 2318 Jeju-do ruling — which is why its robot protagonist has no legal rights. Any fact established elsewhere in the shared timeline that would contradict this story's premise needs to be caught here, not discovered mid-draft.)
- Any local/regional facts specific to this story's setting that need to be nailed down before character or plot work begins.

## 1.2 — Naming Conventions

- Character naming conventions (is there a pattern tied to culture/region/era, per the shared universe's own conventions?)
- Place naming conventions

**Important: settling the *convention* here is not the same as assigning actual proper names to specific characters.** A character does not need a proper name to have a personality, a role, or a full arc — see `04-Phase-2-Characters.md`. It's entirely normal for character and even plot work to proceed under placeholder/shorthand identifiers (a role, a description, a working nickname) with real names assigned later, whenever it's actually convenient. Don't treat an unnamed character as blocked or incomplete.

## 1.3 — Structural Conventions

- Verse or prose? If verse, what's the stanza/table convention (see `structure/main story/stanza scene and chapter breakdowns/outline-template.md`)?
- Point of view and tense
- Any scene-break or section-break notation convention

## 1.4 — Title

- Working title vs. final title, if different

## 1.5 — Untrack the Final-Text Folder

**Before any real prose gets written into this novel's `text/` folder, add it to the repo's root `.gitignore`.** `text/` is where the actual conclusive, copyrightable manuscript prose lives — as opposed to the outline/planning tables elsewhere in `structure/`, which are fine to keep tracked. Once a novel is far enough along to file for copyright, its draft text shouldn't be sitting exposed in a public repo (or in that repo's git *history* — untracking alone doesn't remove anything already committed). Follow the existing pattern already in `.gitignore` for the other novels in this repo, e.g.:

```
[This Novel's Folder Name]/text/
```

If this novel is a series with per-book subfolders (`Book - X/`, `Book N/`, etc.), each book's own `text/` folder needs its own line, the same way The Four-Realm Musician and The Saga of Maggie Aarden are handled.

---

## Phase 1 Output Checklist

- [ ] Setting/era confirmed and cross-checked against shared-universe timeline
- [ ] Naming *conventions* settled (proper names for specific characters can still be pending — that's tracked per-character in Phase 2, not here)
- [ ] Structural conventions (verse/prose, POV, tense, scene-break notation) settled
- [ ] Title settled (or explicitly deferred, with reasoning)
- [ ] This novel's `text/` folder(s) added to root `.gitignore` before any real prose is written into them

**When all items are checked: Phase 2 and Phase 6 can begin.**
