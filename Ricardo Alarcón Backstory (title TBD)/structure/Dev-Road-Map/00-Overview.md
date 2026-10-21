# [[Novel/Series Title]] — Development Roadmap

## What This Is

A structured development roadmap for this novel (or series), adapted from a game-design-document roadmap format. It orders and prioritizes the design thinking, decisions, and outline work that remain before the manuscript is ready to draft in full — not the prose itself, but everything the prose depends on: character, setting, plot structure, and open decisions.

This roadmap covers **planning and outline work only**. It is not a drafting schedule or a word-count tracker. Every item here is a decision, a piece of structural design, or a completion status — not prose.

---

## How to Read This

**The roadmap is split into seven phases**, each in its own file:

| File | Phase | What It Covers |
|------|-------|----------------|
| `02-Blocking-Decisions.md` | Pre-Phase | Open either/or decisions that must be made before downstream work can proceed |
| `03-Phase-1-Foundations.md` | Phase 1 | Settle tentative setting/timeline facts, naming conventions, structural conventions (verse/prose, POV) |
| `04-Phase-2-Characters.md` | Phase 2 | Full character-arc completion — protagonist(s) and every named secondary character |
| `05-Phase-3-Supporting-Cast.md` | Phase 3 | Organizations/groups relevant to the plot |
| `06-Phase-4-Story-and-Chapters.md` | Phase 4 | Beat-by-beat plot structure, chapter/stanza breakdowns, subplot completion |
| `07-Phase-5-Theme.md` | Phase 5 | The thematic throughline — deliberately *not* a blocking decision; see below |
| `08-Phase-6-World-Depth.md` | Phase 6 | Setting detail beyond what's strictly needed for plot — texture, secondary locations, history |
| `09-Phase-7-Long-Term.md` | Phase 7 | Sequel/series planning, deferred world-building, revision passes |

The **Craft Reference** (`10-Craft-Reference.md`) is a standing reference document, not a phase. Consult it when working on any character arc or plot beat.

The **Completion Matrix** (`01-Completion-Matrix.md`) is the single-source status table. Update it as work is completed.

---

## Current State

*Fill in after the first full read-through of this novel's existing material (hand-written outline, prior drafts, notes).*

**Overall completion: [[—]]%** of outline/planning content settled to final or near-final quality.

What is solid:
- [[—]]

What is incomplete, in priority order:
1. [[—]]

---

## Guiding Principles for This Roadmap

### Order follows dependency

The real-world writing order runs: **who are these people, and what is this place? → what do they do? → what does it all mean?** In roadmap terms: **Character (and Setting) creates Plot; Plot creates Theme.** Concretely:

1. Setting (Phase 1) and character identity/personality/arc (Phase 2) come first — a character does not need a proper name to have a personality, a role, or a full arc. Naming can and often should be deferred; see `03-Phase-1-Foundations.md` and `04-Phase-2-Characters.md`.
2. Supporting cast/groups (Phase 3) — what do they want, and what do they need that only their opposition (or the protagonist) can provide? Decided at the same time as character work, not as a separate later step.
3. Plot (Phase 4) — what do these people, with these wants, actually do?
4. Theme (Phase 5) — what does it all mean? This is discovered, not designed upfront. **Theme is deliberately not a blocking decision.** It's normal, even expected, for theme to only become fully apparent once plot, character, and structure are fully or partially built — see `07-Phase-5-Theme.md`.

Nothing in a later phase should be designed before the things it depends on — but "depends on" here means *needs to exist first*, not *needs to be final first*. A character's full arc doesn't need a settled proper name; a plot doesn't need a fully-articulated theme before it can be built.

### The universal north star

Every novel in this shared universe answers some version of the same two governing questions: **what is the Robot Experience (the counterpart to the Human Experience), and how do the Robot Experience and the Human Experience interact and relate?** This pair is fixed across the whole line — it is not something to redesign per book.

**What changes per book is the specific, concrete question that particular story asks as its own derivation of that pair.** For example, the Benson Trio novel's own north star is *"what does it mean to have a home?"* — a specific instance of the universal question, not a replacement for it.

**This novel's own north star:** [[—]]

*(Fill in once it becomes clear — per the Theme section above, this doesn't need to be settled before Phase 2 or Phase 4 begin, though having a rough sense of it early tends to help character work; it just isn't a hard prerequisite.)*

### Systems before content
A character arc that references a plot beat that isn't settled is an arc that will need rewriting. A chapter that references a setting fact that isn't confirmed is a chapter built on sand. Settle the foundations before writing the content that depends on them.

### Consult the shared framework, don't reinvent it
This novel's beat structure and character-arc format are not designed from scratch per-book — see `10-Craft-Reference.md` and `reference/story-structure-definitions.md` (shared across all novels in this line). Use them as-is unless this specific story has a genuine reason to deviate.

---

## Dependencies Map

```
Blocking Decisions
    └── Phase 1 (Foundations)
            ├── Phase 2 (Characters)
            │       └── Phase 3 (Supporting Cast) ← decided alongside Phase 2, not strictly after it
            │               └── Phase 4 (Story + Chapters) ← depends on Phase 2 + 3
            │                       └── Phase 5 (Theme) ← discovered from Phase 4, not a gate on it
            └── Phase 6 (World Depth) ← can run parallel to Phases 2–5
Phase 7 (Long-Term) ← depends on Phase 4, 5, and 6
```

Phase 6 can be worked on concurrently with Phases 2–5. Phase 7 is strictly last.
