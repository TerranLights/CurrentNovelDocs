# Character Development Methodology — Stage 3: Character Data

**Pipeline position:** turning the processed information from Stage 2 (`02_Information_Processing.md`) into
actual usable character data — the structured fields a finished Doll psychological profile should contain.
Distinct from the existing `Character_Spec_Fill-In_Sheet_Template.md`, which is surface/mechanical data, not
this deep layer.

**Status:** complete (2026-08-09) — vocabulary consolidation, the per-Doll fill-in worksheet (tier determination,
fill-in order, Stage 2 cross-references), and the Front-Gate/Character Hierarchy resolution are all in place.
No open items remaining.

---

## Step Zero: The Front-Gate Question — does this character need the full node set?

Before filling in anything below, decide how much of Stage 3 a given character actually warrants. This isn't a
node itself — it's a calibration step that governs how much of the rest of this stage to actually do.

- **Drift vs. Drive** (Swain) — most characters, including most background District NPCs and Under-Questline
  figures, don't have Drive; they have Drift (path-of-least-resistance, passively made decisions). A Drift
  character works fine in a bit part but is fatally weak as a protagonist or major companion.
- **Card's Character Hierarchy** (walk-on / minor / major — filed under Stage 4, cross-referenced here) is the
  structural-weight counterpart: Drift/Drive tells you how much internal engine a character needs; the
  Hierarchy tells you how much narrative weight she's carrying. Read them together.
- **Practical rule:** a walk-on/Drift-type character may only need the Ghost and Want nodes filled in, not the
  full set below. Full-companion and major-NPC status is what earns the complete node set.

---

## Consolidated Core Nodes

The DRAFT file contained six different named systems all describing the same underlying Want/Need/Ghost/Lie
territory (Weiland's Lie/Want/Need/Ghost/Truth; Boutros's Goal/Desire/Lesson; St. John's GMC and External/
Internal Goal/Greatest Fear; Alderson's Strength/Longing/Fear; Swain's Purpose/Motive and Direction/Goal/Drive/
Attitude; plus Truby's original Desire/Need split). Below is the reconciled set — one canonical node per real
concept, with every source vocabulary that maps onto it named explicitly so nothing gets silently lost.

### NODE: Want (External Goal)
**Merges:** Weiland's Want · Truby's Desire (*external* sense — see the terminology collision flagged under
Desire/Motive, below) · Boutros's Goal · St. John's GMC-Goal / External Goal · Swain's Purpose/Goal.

The concrete, external, plot-level thing she's pursuing. Keep Swain's two-level split as a built-in refinement
rather than flattening this to one field:
- **General Goal** — the whole-arc throughline (survive the threat, restore the status quo).
- **Immediate Goals** — the scene-by-scene sub-goals in service of the General Goal.

### NODE: Need / Truth (Internal)
**Merges:** Weiland's Need/Truth · Boutros's Lesson.

The corrective belief that cures the Lie. Boutros's "the Lesson doesn't have to be learned, and doesn't have to
be positive" is the same claim as Weiland's Negative Arc taxonomy (Disillusionment/Fall/Corruption) stated in
different words — not additional content, just confirmation from a second source.

### NODE: Lie / Flaw
**Merges:** Weiland's Lie · Boutros's Flaw.

On inspection these are identical: a wound-rooted false belief that actively blocks the Want. Boutros's
Flaw-vs-Personality-Trait test survives as a useful diagnostic *question* (see Standalone Fields, below), but
Flaw itself is not a separate field from Lie — it's the same node under a different name.
- **Romance sub-case:** St. John's "I can't love him because ___" one-line prompt is a quick-fill variant of
  this exact node, scoped specifically to what blocks the internal conflict for a romanceable companion. Use it
  as a fast draft-starter for the Lie/Flaw node when the character in question is a romance option, not as a
  separate field.

### NODE: Ghost (Backstory Wound)
**Merges:** Weiland's Ghost · Corbett's Ghost (already flagged in the DRAFT file as directly convergent) ·
St. John's Prime Motivating Incident / GMC-Motivation (backstory factors).

The past wound that explains *why* she believes the Lie. **The Five Fundamental Types of Death** (Social /
Spiritual / Psychological / Professional / Physical — already project-canonical) stays attached here as a
checklist applied *to* this node, not a separate field: when building a Ghost, name which of the five types of
death is actually in play.
- **Proportionality rule** (Weiland): the bigger the Ghost, the bigger the Lie, the bigger the arc — calibrate
  the wound to the scale of transformation the questline is actually meant to deliver.
- **Reveal-timing is a separate decision**, not part of the node's content: gradual reveal, origin-prologue (the
  Ghost dramatized as its own opening sequence), or never revealed at all are all legitimate — decide
  deliberately per companion rather than defaulting to one.

### NODE: Desire / Motive (the emotional connector)
**Merges:** Boutros's Desire · Swain's Motive · St. John's Internal Goal · Alderson's Longing.

**Terminology collision, worth stating plainly so it's never silently misapplied: Boutros's "Desire" is
internal; Truby's "Desire" (captured earlier in the DRAFT file) is external and equals the Want node above.**
Same word, opposite referent, two unrelated sources. Once disambiguated, this node is genuinely additive — none
of Weiland's four core terms separately name "the emotional charge that makes the Want matter this much,
usually traceable back to the Ghost." Use the **Why Chain** (Boutros — keep asking "why does she want this"
past the first, obvious answer until it becomes primal) as the construction technique for this node; it's
listed under Stage 2 as a processing tool, but its *output* is what fills this field.

### NODE: Greatest Fear
**Merges:** St. John's Greatest Fear · Alderson's Fear.

What she is most afraid will happen or be revealed. Feeds directly into Black Moment construction in Stage 5 —
St. John's own rule: a companion's low point should be engineered to match this specific, already-established
fear precisely, not just be "something bad."

### NODE: Background Taxonomy (Body / Environment / Experience / Ideas)
**Merges:** Swain's four-part "Bent Twigs" · Corbett's Egri-derived Physical/Psychological/Sociological
three-way split.

Swain's four-category version is strictly more granular and is the recommended canonical form — Egri's three
categories map onto three of Swain's four (Physical→Body, Sociological→Environment, Psychological→roughly
Experience), but Egri's has no slot for Swain's fourth category, **Ideas** (exposure to a specific belief
system, philosophy, book, speech, or person's worldview as its own independent shaping force, distinct from
lived experience or trauma) — given this project's unusually rich religious/philosophical landscape
(Polydimensional Animism and the other robot religions, competing national ideologies), Ideas is worth keeping
as its own explicit slot rather than folding it into Experience by default.
- **Experience carries its own sharp caution, worth keeping attached to this node**: it is not the objective
  event that creates the psychological effect, it's the character's individual interpretation of and reaction
  to it (Swain) — two companions sharing a structurally similar backstory template (war orphan, exile, diaspora
  refugee) should be built to react to it in genuinely different ways, not just relocated to different
  Districts.

---

## Fields That Stay Standalone

Genuinely distinct information, not redundant with any node above:

- **Strength** (Alderson) — a positive, competence-based trait shown independent of her wound or her goal. No
  other source names an explicit "what is she good at, apart from what hurts her" field.
- **Reasons She Can't Quit** (External / Internal — the output of Swain's Drive formula) — a commitment/stakes
  mechanism, distinct from goal-content: External (a literal constraint forces continued engagement) and
  Internal (named psychological compulsions — Pride, Shame, Duty, Gratitude, Loyalty).
- **Dominant Attitude + Contradictory Exception** (Swain) — a habitual, not-necessarily-rational disposition
  toward a topic, plus exactly one narrow, genuine exception to it that only surfaces under a specific,
  plantable circumstance. A controlled inconsistency, not a random one.
- **Character Trait vs. Personality Trait** (Boutros) — a second, unrelated axis from Lie/Flaw: character traits
  (honesty, loyalty) come from morals/values/upbringing and are often hidden until tested; personality traits
  (bubbly, dour) are outward, often deliberately performed projection. A Doll can perform a personality trait
  that actively conceals a contradictory character trait.
- **Coping / Defense Mechanism (tiered)** — Corbett's four-tier hierarchy (Psychotic / Immature / Neurotic /
  Mature), independently converging with St. John's own separately-named "coping mechanisms" category. Elevated
  to first-class given the cross-source convergence already flagged in the DRAFT file. Note: core desire and
  secondary desires can call on genuinely different tiers — a companion can be Mature-tier in one domain and
  Immature-tier specifically where her core wound is implicated, and that asymmetry is itself real
  characterization, not an inconsistency to smooth over.
- **Speech-Pattern Correlation Table** (St. John) — a diagnostic *output* field: once the Ghost and self-esteem
  level are fixed, dialogue patterns across every scene should be checkable against St. John's correlation table
  (hesitant/evasive for past failure, bitter/talking-down for someone burned before, etc.) rather than invented
  fresh for a "good line" each time.
- **Enneagram (type / wing / instinct)** — stays the mandatory, primary motivational axis. Already load-bearing
  project-wide infrastructure (`Enneagram_Dynamics.md`, the Enneagram Character Index, the planned deep-dive
  folder) — not optional, not one option among equals.
- **Direction — the Five Wishes** (Swain: Adventure / Security / Recognition / Response / Power) — an optional
  *secondary* motivational lens. Deliberately not merged into Enneagram: Enneagram asks about core fear/desire
  structure and coping style; Direction asks what *style of life-fulfillment* she's chasing. Different question.
  Use when Enneagram alone doesn't fully explain a specific goal-orientation pull, not as a mandatory field.

## Diagnostic Tests (not fields — questions to run against the nodes above)

- **Flaw vs. Personality Trait test** (Boutros): does this behavior come from an unhealed belief that costs her
  something structurally important (→ belongs in Lie/Flaw), or is it just color (→ belongs in the Character
  Trait / Personality Trait fields)? A trait can graduate into a flaw if it turns out to be load-bearing; most
  never do, and that's fine.

## Coverage Checklists (three sources — reduced to two by function, not merged into one)

Three different "have I covered everything" checklists exist in the source material. They don't all do the same
job, so they aren't fully consolidated — but one is a strict subset of another and is downgraded accordingly:

- **The 12-Category Character Notebook** (Maisel) — the broadest of the three; recommended as the **master
  content checklist**. Categories: Basic Headline, Basic History, Archetypal/Category/Stereotypical Resonance,
  Actions and Reactions, Moral Valence, Dreams and Ambitions, Inner Life, Shadow Sides and Difficulties in
  Living, Consequences of Upbringing, Power/Sexual Potency/"Alpha-ness," Cultural Component, Meaning Web.
- **Backstory's Five Slots** (St. John: Belief System, Values, Family and Friends, Fears and Phobias, Prime
  Motivating Incident) — **demoted to an explicitly-named fast-pass subset of the 12-Category Notebook**, not
  kept as an independent tool. Use it when a quick first pass is needed and the full notebook is overkill.
- **The Ten Ways We Come to Know a Character** (Card: Action, Motive, the Past, Reputation, Stereotypes,
  Network, Habits and Patterns, Talents and Abilities, Tastes and Preferences, Body) — **kept fully standalone**.
  This answers a different question from the other two: not *what content exists* about her, but *how will the
  player actually learn it on-screen*. Run this checklist after the notebook is filled, as a delivery-channel
  audit, not a content-generation pass.

## Content Library, Not a Vocabulary — Flagged So It Isn't Mistaken For One

- **The Six Life Arc archetype assignment** (Weiland, *Archetypal Character Arcs* — Maiden/Hero/Queen/King/
  Crone/Mage) is **pre-built content that plugs directly into the already-consolidated Want / Need-Truth /
  Lie-Flaw nodes above** — each arc comes with its own ready-made thematic Lie/Truth pair. It is not a seventh
  competing triad. When a Doll's existing material already gestures toward one of the six life-stages, use its
  pre-built Lie/Truth pair to seed the Lie/Flaw and Need/Truth nodes rather than inventing from scratch — and
  check whether her existing material instead points toward one of the twelve Shadow Archetypes for a
  compromised/negative-arc Doll.

---

## The Per-Doll Fill-In Worksheet

Built 2026-08-09. This is what actually turns the reconciled vocabulary above into a usable, ordered process —
resolving the Front-Gate's binary Drift/Drive split against Card's three-tier Character Hierarchy (Stage 4),
since a real worksheet needs to know what a *minor* character gets, not just walk-on-vs-major.

### Tier determination

| Tier | Mandatory fields |
|---|---|
| **Walk-on** (Drift) | Ghost + Want only |
| **Minor** | Ghost + Want + Lie/Flaw + Need/Truth + Desire/Motive + Greatest Fear — the complete core wound-and-belief cluster, nothing supplementary |
| **Major** (Drive) | Everything — core cluster + all standalone fields + full coverage checklists + Six Life Arc content-library check + Speech-Pattern Correlation Table |

### Fill-in order for the core cluster

Based on the causal relationships already established when these nodes were built — Ghost causes Lie, Desire/
Motive connects Ghost/Lie to Want, Need/Truth is defined as the corrective opposite of whatever Lie turns out to
be:

1. **Ghost** first — the root; everything else is either caused by it or defined in contrast to it.
   *Stage 2 cross-reference: Self-to-Character Memory Mining, mode (a) — Boutros's fixed question set.*
2. **Greatest Fear** next, while the Ghost is fresh — tightly coupled to the wound (what she's afraid will
   happen again).
3. **Lie/Flaw** — the false belief the Ghost produced.
4. **Desire/Motive** — the emotional connector *from* the Ghost/Lie *to* the Want; has to come after Ghost/Lie
   and before Want for exactly that reason.
   *Stage 2 cross-reference: The Why Chain — its output is literally what fills this field.*
5. **Want** — now groundable in something, rather than picked arbitrarily.
6. **Need/Truth** last — defined as the corrective *opposite* of whatever Lie/Flaw turned out to be, so it can't
   really be filled in first.
   *Cross-reference: check the Six Life Arc content library first — a pre-built Lie/Truth pair may already fit
   and can be seeded here instead of built from scratch.*

### Major-tier supplementary fields

No strict order required; filled in after the core cluster:
- **Background Taxonomy** (Body/Environment/Experience/Ideas) — mostly assembly, not diagnostic.
- **Strength.** *Stage 2 cross-reference: the Scenario Diagnostic Template, run on a competence-testing
  situation.*
- **Coping/Defense Mechanism tier.** *Stage 2 cross-reference: Self-to-Character Memory Mining, mode (b) —
  Corbett's single-charged-moment version.*
- **Reasons She Can't Quit, Dominant Attitude + Exception, Character Trait vs. Personality Trait.** *Stage 2
  cross-reference: Compare-and-Contrast Self-Image, or the In-Voice Character Interview for the harder-to-access
  ones.*
- **Direction** — only if Enneagram alone doesn't explain a specific goal-orientation pull.

### Closing passes, major tier only

1. Run the **Flaw vs. Personality Trait test** against everything gathered.
2. Run the **12-Category Notebook** as a completeness check, then the **Ten Ways** checklist as a
   delivery-channel audit.
3. Build the **Speech-Pattern Correlation Table** last — a diagnostic *output*, derivable only once the Ghost
   and self-esteem level are actually fixed.

---

## Open, Undecided

**Resolved 2026-08-09:** the fill-in worksheet above closes the item that was open here. No remaining open items
for this stage.

**Resolved 2026-08-09, now that Stage 4 is built out:** the Front-Gate/Character Hierarchy question is settled —
keep the cross-reference, don't merge. Stage 4 now has its own fully-sequenced Front-Gate trio (MICE Quotient →
Character Hierarchy → Story Problem vs. Character Problem), each step there doing a distinct job specific to
*narrative role and story investment*. Pulling Character Hierarchy into this file would break that sequence for
no gain — this stage's Drift-vs-Drive front-gate serves a genuinely different, narrower question (how much
*psychological engine*, i.e. how much of the node set above, a given character needs), not how much narrative
weight she carries. The two front-gates are related and worth reading together, but they belong to their
respective stages and should stay cross-referenced rather than consolidated.
