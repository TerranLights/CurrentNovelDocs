# Character Development Methodology — Overall Process Scaffold

**What this is:** a broad-scale architecture map of the whole methodology pipeline. **Refreshed 2026-08-09** —
the original version of this file was written as a pre-consolidation map, pointing at roughly 3,459 lines of raw
material in `Character_Development_Methodology_-_DRAFT_Ideas.md` and flagging what each stage would eventually
need to reconcile. All of that reconciliation is now done; every stage file is complete. This refresh replaces
the old "here's what needs sorting" framing with an accurate summary of what's actually in each finished file,
plus the intake layer (`00a`/`00b`) that didn't exist when this scaffold was first written. This file is still
the map, not the territory — full detail lives in each stage's own file.

**Why five stages, and what each one actually does:**

1. **Input Information** — everything that has to already exist, or be gathered, before any generative work
   starts on a given Doll.
2. **Information Processing** — the diagnostic toolkit: techniques for interrogating raw inputs to surface a
   genuine, specific psychology, rather than starting from a blank page or a generic trait list.
3. **Character Data** — the actual structured output of Stage 2, written down as reusable fields on a Doll's
   psychological profile (as distinct from the existing `Character_Spec_Fill-In_Sheet_Template.md`, which is
   surface/mechanical data, not this deep layer).
4. **Story Material** — converting a finished Character Data profile into actual story scaffolding: her role,
   her supporting cast, her thematic shape, what kind of story she's even in.
5. **Beats, Paths & Results** — the full beat-by-beat structural machinery, branching into every possible arc
   type, path, and ending a given Doll's story material can resolve into.

Downstream stages consume upstream ones. Stage 5 can't be built without Stage 4's story material; Stage 4 can't
be built without Stage 3's character data; and so on.

---

## The Intake Layer — `00a` and `00b`, Added After This Scaffold Was First Written

Not one of the five numbered stages — a compression layer sitting in front of Stage 1, built specifically for
scale: the developer's actual Doll count (1,185 and climbing toward the Outer Tepenia trilogy and Cryptograph
Helix) makes manually filling in Stage 1's full field set per Doll unworkable.

- **`00a_Initial_Input.md`** — the minimal seed-field intake (name, a doll-folder pointer if one exists, a rough
  vision statement, robot/human, Enneagram if known, location of origin if known — the last two with an explicit
  "you decide" escape hatch) plus the full Derivation Protocol mapping those six seeds onto every one of Stage
  1's 25 categories, deferring what genuinely doesn't need to exist yet (introduction-scene context, the full
  relationship web, exact ending concepts) rather than front-loading everything.
- **`00b_Clarification_Protocol.md`** — the repeatable algorithm for resolving whatever 00a's derivation leaves
  genuinely ambiguous, per Doll. Confidence-tags every derived field (Sourced / Strong Inference / Weak
  Inference / Blocked), only ever surfaces a question for a Section A field at Weak-Inference-or-worse with no
  safe default, ranks surviving gaps by downstream leverage (Enneagram highest, then Ghost, then robot/human
  status), and phrases whatever survives as closed-form multiple-choice with a "you decide" option.

---

## Cross-Cutting Constraints — apply at every stage, owned by none

- **Unlike its game-side source, this ported version is for a linear medium with a fixed length** — every beat
  can and should be defined both by functional role *and* by percentage-of-manuscript placement, using
  `reference/story-structure-definitions.md`'s Summary Table as the actual placement reference. See Stage 5's
  "Reversal for Prose" section for the full reasoning.
- **No Good Endings / Ending Distribution law** — negative endings are a minority, bittersweet is the largest
  category, positive endings are real but never costless. Stage 5's Ending-Shape Cross-Mapping Table builds
  toward this distribution.
- **No National Stereotypes** — applies most directly to the Background Taxonomy (Stage 3) and to any
  in-fiction regional-reputation shorthand (flagged explicitly where the villain/anti-hero sheet's Mordred/
  Cornwall example shows the failure mode to avoid).
- **No Level-Scaling** — not a character-psychology concern directly, but a standing law all downstream content
  design still has to respect.

---

## Stage 1 — Input Information: complete

**File status:** Section A (12 necessary-field categories, each citing the specific downstream node or tool
that needs it) and Section B (13 optional-but-enriching categories) are both fully built. No open items.

**What it actually contains:** foundational identity facts; the mandatory Enneagram assignment; intended story
role/scope; existing biographical and historical material (the single most input-hungry category, feeding
Stage 3's Ghost node directly); existing mechanical/surface data; world-context reference access (Robot
Universals' Friction Bank chapters, relevant District Megasheets, faction/religious canon); the project's
standing design-law constraints; the writer's one-time Mirror Interview priming answers (not a per-Doll cost);
existing narrative introduction context; existing supporting cast; existing questline/ending concepts; and a
memory/prior-notes check. Section B covers soft-detail delivery material, speech/dialect notes, reputation,
a pre-existing Basic Headline if one exists, extended relationships, food/music preferences, "Tribe," existing
voice specimens, concept art, secondary foils, cross-media appearances, prior playtesting, and the developer's
own unformalized instincts.

---

## Stage 2 — Information Processing: complete

**File status:** Governing Principles, two consolidated technique-nodes, four standalone tools, and a
troubleshooting checklist are all built. The original scaffold's "three overlapping motivational-axis systems"
question is resolved: Enneagram stays the mandatory primary axis, Direction (Swain's five wishes) is an optional
secondary lens (moved to Stage 3 as a data field), and Compelling Need (Maslow) stays in Stage 2 specifically
because it's situational — what's driving her *right now* — not a fixed trait.

**What it actually contains:** four Governing Principles (Backstory Proportionality, the Consistency Caution,
the developer-refined Mystery Caution — full resolution stays in private design notes, delivered in media only
through soft ambient detail — and the "Character Is Not You" caution); two consolidated nodes (the Why Chain/
Interrogation Technique, merging Card and Boutros; Self-to-Character Memory Mining, merging Boutros's Mirror
Interview and Corbett's defense-mechanism excavation); and four standalone tools (the In-Voice Character
Interview, Obstacle Brainstorm-and-Triage, the Scenario Diagnostic Template — still the single most fully-built
tool in the whole methodology — and Compare-and-Contrast Self-Image, plus Compelling Need and the Public/Private
Values Gap).

---

## Stage 3 — Character Data: complete

**File status:** the vocabulary reconciliation flagged as "real, undone work" in the original scaffold is fully
resolved. Six previously-competing Want/Need-style triads are consolidated into seven canonical nodes, with
every source vocabulary named explicitly so nothing was silently lost. A full per-Doll fill-in worksheet
(tier determination, construction order, Stage 2 cross-references) exists on top of the vocabulary. No open
items.

**What it actually contains:** a front-gate tier system (walk-on/minor/major, bridging Stage 3's Drift-vs-Drive
question with Stage 4's Character Hierarchy); seven consolidated nodes (Want, Need/Truth, Lie/Flaw, Ghost,
Desire/Motive — including the flagged Boutros/Truby "Desire" terminology collision — Greatest Fear, and the
Background Taxonomy); eight standalone fields; a diagnostic test; a two-tier coverage-checklist system (the
12-Category Notebook as master checklist, the Ten Ways as a separate delivery-channel audit); and the Six Life
Arc archetype assignment, explicitly flagged as pre-built content for the existing nodes, not a seventh
competing vocabulary.

---

## Stage 4 — Story Material: complete

**File status:** the consolidation pass and the Player-Necessity Rule (synthesized from this project's own
already-mature in-production methodology, not book-mined) are both in place. No open items.

**What it actually contains:** a three-step Front-Gate/Sequencing Trio (MICE Quotient → Character Hierarchy →
Story Problem vs. Character Problem); one genuine merge (Contagonist, absorbing Corbett's Counterweight); Impact
Character and Revenant kept deliberately separate after a near-merge turned out to lose real information, with
the non-Truth-aligned Revenant case routed to the villain/anti-hero sheet; standalone tools (the Normal World,
the Characteristic Moment, Antagonist vs. Antagonistic Force, the Twelve Archetypal Antagonists, Four-Corner
Opposition, the Four Elements of Relationship Sizzle, Corbett's remaining functional-role catalog);
composability notes between orthogonal systems; two staging/sympathy techniques surfaced late (Card's general
sympathy-lever catalog, Boutros's cat-save/delay-the-worst-act); and the Player-Necessity Rule and its four
supporting constraints (the categorical-block sanity check, the compounding-reasons technique, the no-escort-
quest constraint, retrofit discipline).

---

## Stage 5 — Beats, Paths & Results: complete

**File status:** the Midpoint Menu, the full canonical beat sequence, the Branching Investigation-Route
Structure, the Act 3 micro-sequence, arc-type beat implications, chiastic mirroring, and the Ending-Shape
Cross-Mapping Table are all in place. No open items.

**What it actually contains:**
- **The Midpoint Menu** — twelve interchangeable Midpoint mechanics (not one canonical beat), spanning fully-
  sourced entries (Bell's two-type Mirror Moment, Weiland's Moment of Truth, the Negative Arc's Refused
  Redemption), Snyder's False Victory/False Defeat, and broader craft-convention entries, plus three
  supplementary cross-references. Two naming collisions were caught and resolved during construction ("Point of
  No Return" and "False Victory," each independently colliding across two different mined sources).
- **The full beat sequence** — Weiland's 11-beat skeleton as the canonical spine, with every other source's name
  for the same beats folded in as a glossary rather than treated as competing, plus the generalized
  Trigger-Type Design Pattern for Inciting Event construction (one thematically-matched trigger type per
  character, 7-16 concrete instances, a small setting-independent subset).
- **The Branching Investigation-Route Structure** — a minimum of 5 deterministic approaches to the same
  protagonist-unique task, alternative circumstantial approaches at a floor of 3 (target 7-12), a route-validity
  QA check, a menu of recommended route archetypes (standing-antagonism, extreme-reputation with a six-flavor
  taxonomy, long-vigil), and a multi-character non-overlap principle. Distinct from the Trigger-Type Design
  Pattern: that one gates arc *entry*, this one gates the *middle*.
- The Act 3 micro-sequence, the Three Arc Types' beat-level implications, chiastic mirroring, the Ending-Shape
  Cross-Mapping Table (with its own flagged Disillusionment "straddle" case and a named blind spot for
  reactive/Flat-Arc-adjacent characters), series-spanning arc models, common ending failure modes, and QA tools.

---

## Cross-Stage Notes

- **The vocabulary reconciliation the original scaffold flagged as undone is now fully resolved** — see Stage 3
  above. Nothing carries forward from the old "at least five different Want/Need-style triads" note.
- **Two genuinely different source types now feed this methodology, worth keeping distinct.** Stages 1-3 and
  most of 4-5 come from book-mining (the craft-theory DRAFT file). The Player-Necessity Rule and the Branching
  Investigation-Route Structure come from a different source entirely: this project's own already-mature,
  in-production companion-arc methodology. Both are legitimate, but they carry different evidentiary weight and
  different revision paths — the book-mined material can be re-checked against its source books; the
  in-production material should be kept
  in sync with `Companion_System.md` and `Universal_Rules.md` directly, since those files, not this methodology,
  are the actual source of truth for anything now codified as project-wide canon.
- **The villain/anti-hero supplement sheet remains a parallel, not subordinate, resource** — feeds Stage 4
  (antagonist/villain story material) and Stage 3 (irredeemability thresholds), kept deliberately separate.

---

## What This File Is Not

Not the finished methodology in full — that's the seven files it maps (`00a`, `00b`, `01` through `05`). This
file is the navigational summary, refreshed to stay accurate as of 2026-08-09; if any stage file changes
substantially again, this scaffold should get another pass rather than being left to drift stale a second time.
