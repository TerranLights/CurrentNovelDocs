# Character Development Methodology — 00a: Initial Input

**Purpose:** a minimal-field intake layer sitting in front of Stage 1 (`01_Input_Information.md`), built
2026-08-09 specifically to make this methodology usable at the scale the developer actually needs — currently
1,185 Dolls either already made or ready to be made into Tepenian Universe characters, realistically approaching
or passing 2,000 once Outer Tepenia and Cryptograph Helix are underway. Manually filling in Stage 1's full field
set (Section A's 12 categories plus Section B's 13) by hand, per Doll, at that scale isn't viable for one human
developer. This file is the compression layer: the smallest set of fields the developer actually has to provide,
paired with a **Derivation Protocol** describing exactly how the rest of Stage 1 — both necessary and optional
fields — gets reconstructed from them.

**`00b_Clarification_Protocol.md`** now exists alongside this file — it's the repeatable algorithm for resolving
whatever this Derivation Protocol leaves genuinely ambiguous for a specific Doll, without falling back into a
full manual review pass per Doll.

---

## Why the Full Stage 1 Field Set Doesn't Actually Need 25 Separate Answers Per Doll

Three things make aggressive compression possible, found by re-checking every one of Stage 1's 25 categories
against what's actually irreducible:

1. **Existing doll-folder materials already answer most of Section A1, A4, A5, A9, and A10** for any Doll who
   already has a folder — Reference Images, any existing notes, any existing mechanical data. These don't need
   to be retyped into a form; they need a **pointer**, and this methodology (or the assistant applying it) reads
   them directly.
2. **A8 (the writer's own priming answers for the Mirror Interview) is a one-time setup cost, not a per-Doll
   field.** The self-pass — happiest memory, saddest memory, a time of shame, a belief that creates conflict, a
   time of being hurt — is the *same* baseline used to prime every character's Memory Mining pass (Stage 2). It
   should be gathered once, ever, not re-asked 1,185 times. Not requested below; flagged as a one-time exercise
   to do separately, whenever convenient, outside this per-Doll intake.
3. **Several Section A categories are genuinely not needed at initial registration.** A9 (introduction-scene
   context), A10's full relationship web (beyond what a folder already shows), and A11 (existing questline/
   ending concepts) are Stage 4/5-territory that only matter once a *specific* Doll's full questline is actually
   being built — not while bulk-registering 1,185 characters. These stay deliberately deferred (marked TBD) at
   this stage, filled in properly later, per-Doll, when her actual development turn comes.

What's left, after removing all of the above, is a genuinely small irreducible core: facts that can only come
from the developer's own head, because no amount of reading existing files or applying project canon could
produce them.

---

## The Minimal Seed Fields

**Fields 1-3 are the ones that actually matter. Fields 4-6 have an explicit "you decide" escape hatch — the
developer is not required to answer them if there's no strong existing preference.**

1. **Name (or doll-folder identifier).** If she already has a named folder, this is just confirming which one.
2. **Doll-folder path or pointer to existing materials, if any exist.** This single field is doing the most
   compression work in the whole intake — if a folder exists, its Reference Images, any existing notes, any
   partially-filled `Character_Spec_Fill-In_Sheet_Template.md`, and any prior design fragments all become
   directly readable, covering large parts of Section A1, A4, A5, A9, and A10 without the developer restating
   any of it.
3. **A vision statement — whatever's already in your head about her, in whatever form it's already in.** One
   line, one paragraph, a mood, a single defining trait, a "she's basically X but Y" comparison — doesn't need
   to be complete, organized, or even fully coherent. **This is the single highest-leverage field in this entire
   intake.** A short, rough description reliably implies a great deal of downstream material (a personality
   shape, a plausible Enneagram-type cluster, a likely relationship to the Long Night War, a likely emotional
   register) that the Derivation Protocol below expands outward from, the same way Boutros's Why Chain expands
   a stated Want into its underlying Desire. Give as much or as little as actually exists — "she's a bitter
   ex-soldier who never talks about her old unit" is already enough to seed several Stage 1 categories at once.
4. **Robot or human, if not already obvious from the folder.** Skippable if field 2 already makes this clear.
5. **Enneagram type, if already decided.** Explicit permission to say "you decide" — if so, one gets proposed
   from field 3 and the reference images, flagged clearly as a proposal, not asserted as settled.
6. **Location of origin, if already decided.** Deliberately worded broader than any one fixed geography — this
   intake isn't scoped to Inner Tepenia alone. It covers the full Dolliverse: the First Interwar Period
   (spanning Upper Earth), the colonization era, and the Post-Solar Era (Mars, Jupiter, and other Outer Tepenia
   locations), each with its own geography and its own placement logic. Same explicit permission to say "you
   decide" or "TBD." If left open, a placement gets proposed using whichever placement logic actually applies
   to her era/setting — faction/plot-thread association first, not simple headcount-balancing across a fixed
   set of locations, since most books don't have one; for a book set within Inner Tepenia's own city, the
   district-level version of that logic still applies. Always flagged as a proposal, never asserted as settled.

**In the absolute minimal case — an existing folder with images but no prior notes — fields 1 through 3 alone
are enough to start.** Everything else either gets read from the folder or derived per the protocol below.

---

## The Derivation Protocol

How each of Stage 1's 25 categories gets populated from the six seed fields above, existing project canon, and
reasonable inference — mapped one by one so nothing is derived by unstated magic.

### Section A — Necessary Fields

- **A1 (Foundational Identity Facts).** Name from seed 1. Robot/human from seed 4 or the folder (seed 2).
  Gen/Mark, age, and current residence: inferred from her assigned location of origin (seed 6) and whatever
  demographic patterns are established for that location/era — Inner Tepenia's own patterns for a Doll placed
  there, or the equivalent for the First Interwar Period, colonization era, or Post-Solar Era once she's placed
  in one of those instead — or defaulted to a plausible unremarkable value if nothing in seed 3 suggests
  otherwise, flagged as inferred, not asserted as confirmed. Physical appearance and Reference Images: read
  directly from the folder (seed 2) if one exists; if not, deferred until concept art exists. Occupation/social
  role: pulled from seed 3 if stated there, otherwise inferred from her assigned location's established economy
  and culture.
- **A2 (Enneagram Assignment).** From seed 5 directly if given. If "you decide": proposed from seed 3's vision
  statement plus the Reference Images, cross-checked against `Enneagram_Dynamics.md`, presented as a proposal
  for approval — never silently asserted as locked.
- **A3 (Intended Story Role and Scope).** Defaults to "a major recurring character, appearing throughout" unless
  seed 2 or seed 3 indicates otherwise (a romanceable-but-peripheral fixture, a notable local figure, a walk-on).
  Book/series placement and recurrence: TBD unless seed 2 or 3 already implies it.
- **A4 (Existing Biographical and Historical Material).** The primary expansion target of seed 3. A vision
  statement's implications get traced outward using the same Why Chain logic already established for Stage 2:
  a stated trait or circumstance gets asked "why" repeatedly against her assigned location's own established
  history and timeline position — Historical Pressures for an Inner Tepenia placement, the equivalent
  established history for the First Interwar Period, colonization era, or Post-Solar Era otherwise — until a
  plausible, specific Ghost-adjacent history emerges. Proposed, not asserted, and always checked against
  anything already in the folder (seed 2) first so nothing invented contradicts something already established.
- **A5 (Existing Surface Data).** Read directly from the folder (seed 2) if a character spec/fact sheet already
  exists there. If not: deferred, marked not-yet-assigned — this methodology does not invent surface details,
  only remains consistent with them once they exist.
- **A6 (World-Context Reference Access).** Not a per-Doll field at all — handled automatically once A1's
  location of origin is known; whichever reference canon actually applies (Inner Tepenia's Megasheets,
  Historical Pressures, and Community Infrastructure documents; or the equivalent established material for the
  First Interwar Period, colonization era, or Post-Solar Era) gets consulted as needed, without requiring the
  developer to name it.
- **A7 (Standing Design-Law Constraints).** Not per-Doll — already known and applied automatically to every
  Doll processed through this methodology.
- **A8 (The Writer's Own Priming Answers).** **Not requested per-Doll, per the one-time-cost finding above.**
  Gathered once, separately, whenever convenient — flagged here as an outstanding one-time task, not part of
  this intake.
- **A9 (Existing Narrative Introduction Context).** **Deferred (TBD) by default at initial registration.** Only
  built out when this specific Doll's actual questline development begins, not during bulk intake — unless seed
  2's folder already has something on record, in which case it's read directly.
- **A10 (Existing Supporting Cast and Relationship Web).** Read directly from the folder (seed 2) if it exists.
  Otherwise, whatever seed 3's vision statement implies (a mentioned mentor, a mentioned rival) gets captured;
  the full web is **deferred (TBD)** beyond that until her actual questline development begins.
- **A11 (Existing Questline and Ending Concepts).** **Deferred (TBD) by default** — Stage 5 territory, not
  needed until her actual arc is being built, unless seed 2's folder already has drafted concepts on record.
- **A12 (Existing Memory and Prior Design Notes).** Not a developer-provided field — checked automatically
  against project memory before any processing begins.

### Section B — Optional, Enriching Fields

None of these are requested directly in this intake. All are either pulled from the folder (seed 2) if present,
inferred from seed 3 and project canon where a reasonable inference exists, or left genuinely blank — since by
definition nothing downstream requires them, an unfilled optional field never blocks anything.

- **B1 (Soft-Detail Delivery Material), B2 (Speech/Dialect Notes), B6 (Food/Music Preferences), B7 ("Tribe"):**
  inferred from her assigned location's established culture (A6) plus anything seed 3 already implies
  about her personality, proposed lightly rather than invented in detail — these are meant to be filled in
  properly later, closer to when she's actually being written, not exhaustively front-loaded now.
- **B3 (Reputation/Rumor Material), B4 (Basic Headline), B5 (Extended Family Tree), B8 (Existing Humor/Lines),
  B9 (Concept Art Beyond Reference Images), B10 (Secondary Foils), B11 (Cross-Media Appearances), B12 (Prior
  Playtesting):** left blank unless the folder (seed 2) already has something on record. None of these are
  ever inferred from nothing.
- **B13 (The Developer's Own Unformalized Instincts).** This is functionally the same field as seed 3 — the
  vision statement *is* this category, just asked earlier and given more weight. Nothing separate to gather.

---

## What Happens After the Six Seeds Are Given

The methodology (or whoever is applying it) produces a full derived Stage 1 sheet from the above, with every
inferred (as opposed to directly-sourced-from-the-folder) field clearly marked as a proposal. This is not meant
to be a silent, one-shot output trusted blindly at 1,185-Doll scale — the review burden this creates, and how
it's kept small rather than becoming a second full manual pass, is handled by
**`00b_Clarification_Protocol.md`**: a confidence-tagging and minimal-question-surfacing algorithm that resolves
only whatever this Derivation Protocol left genuinely ambiguous for a given Doll, not a blanket re-review of
everything derived here.
