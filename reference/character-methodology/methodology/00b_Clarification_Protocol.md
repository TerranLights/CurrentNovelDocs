# Character Development Methodology — 00b: Clarification Protocol

**Purpose:** built 2026-08-09, the companion piece `00a_Initial_Input.md` flagged as coming later. Even with a
complete doll-folder pointer and a good vision statement, the Derivation Protocol won't always produce a
confident answer for every one of Stage 1's necessary fields — and *which* fields turn out ambiguous is
different for every Doll, unpredictable in advance. This file is not a fixed list of follow-up questions. It's
a repeatable **algorithm** for finding the smallest possible set of genuinely necessary clarifying questions for
any given Doll, so that resolving ambiguity stays as cheap as the initial intake was designed to be — not a
second full review pass that quietly reintroduces the 1,185-Doll workload 00a exists to avoid.

---

## The Problem, Stated Precisely

The Derivation Protocol (00a) produces a full draft Stage 1 sheet by combining the six seed fields with existing
folder materials, project canon, and inference. Some of that sheet will be solid. Some of it will be a genuine
guess. **The failure mode this file exists to prevent is treating both the same way** — either dumping the
entire derived sheet back to the developer for review (defeating the compression 00a was built for), or silently
asserting every inferred field as settled fact (risking real downstream damage when a wrong guess propagates
through Stages 2-5). Neither is acceptable at this project's actual scale.

---

## Step 1: Confidence-Tag Every Derived Field

Before anything gets surfaced to the developer, every field in the draft Stage 1 sheet gets one of four tags —
this tagging is the whole mechanism the rest of this protocol runs on.

- **SOURCED** — read directly from the doll folder, a prior note, or existing project canon. Not a guess at
  all. Never surfaced for clarification.
- **STRONG INFERENCE** — confidently derived from the vision statement (seed 3) plus project canon, with little
  real ambiguity. Example: a vision statement reading "she's a bitter ex-soldier who never talks about her old
  unit" makes "her Ghost involves losing people under her command" a strong inference even without a stated
  cause. Reported in the final sheet with its reasoning shown, but not surfaced as a question — the developer
  can correct it later if it's ever wrong, but it doesn't block anything now.
- **WEAK INFERENCE** — multiple plausible answers exist and nothing in the seed material points clearly to one,
  *or* the field is load-bearing enough (see Step 3) that guessing wrong would cause real downstream damage.
  Continuing the example above: *why* she lost them (combat failure, internal betrayal, her own choice to
  abandon them) is genuinely underdetermined by "never talks about her old unit" alone, and this specific fact
  is exactly what Stage 3's Lie/Flaw node gets built from — a wrong guess here doesn't just mis-color one field,
  it mis-shapes everything downstream of Ghost. This tier is the primary candidate for actual clarification.
- **BLOCKED** — a necessary field with no signal at all to infer from, not even weakly. Also a candidate for
  clarification, unless a safe default applies (Step 2).

Section B (optional) fields never get this treatment at all — per 00a's own rule, they're either read from the
folder, lightly inferred, or left blank, and blank is always an acceptable terminal state for an optional field.

---

## Step 2: The Three-Part Surfacing Test

A field only gets raised as an actual clarification question if **all three** of the following are true:

1. **It's a Section A (necessary) field**, not Section B. Optional fields never generate a question, regardless
   of confidence tag — an unfilled optional field blocks nothing, by definition.
2. **Its confidence tag is WEAK INFERENCE or BLOCKED.** SOURCED and STRONG INFERENCE fields are never surfaced.
3. **No safe default exists.** Several Section A fields already have an established fallback that makes
   clarification unnecessary even when genuinely uncertain — A3 (Intended Story Role) defaults to "recruitable,
   full companion, base game" per 00a's own protocol; A6, A7, A12 aren't per-Doll developer decisions at all;
   A9, A10's full web, and A11 are deliberately deferred (TBD) at this stage regardless of confidence, since
   they're Stage 4/5 territory not needed until her actual questline development begins. None of these ever
   generate a clarification question, no matter how uncertain the underlying inference is — they get the
   default or the TBD tag and move on.

What survives this filter is usually a short list: typically A1's Gen/Mark or robot/human status if the folder
didn't make it obvious, A2 (Enneagram) if the vision statement didn't strongly imply a type, A4 (Ghost-adjacent
history) if the vision statement was thin, and occasionally A6's location-of-origin proposal if two genuinely
different placements both fit equally well.

---

## Step 3: Prioritize by Downstream Leverage, Then Cap

If more than a small handful of fields survive Step 2's filter for one Doll, rank them by how many downstream
nodes and tools actually depend on getting that field right, and lead with the highest-leverage ones:

- **Enneagram (A2)** ranks highest — the Enneagram-Rooted-Contradiction principle means Stage 2's entire
  diagnostic pass is run *against* this assignment; a wrong type doesn't just mis-color her, it mis-directs
  every technique applied afterward.
- **Ghost (A4)** ranks second — directly feeds Lie/Flaw, Desire/Motive, Greatest Fear, and the Coping/Defense
  Mechanism tier (all Stage 3 nodes), and is the specific input St. John's Black Moment rule (Stage 5) needs to
  land correctly.
- **Robot/human status (A1)** ranks third — gates whether the entire Robot-Universal Friction Bank applies at
  all.
- Everything else that survives Step 2 ranks below these three in practice, since most other necessary fields
  either have partial safe defaults or feed a narrower slice of downstream work.

**If the ranked list is still long for a particular Doll, ask about the top 2-3 and let the rest default to
"propose a value and flag it clearly as a proposal"** rather than asking about everything that's merely
uncertain. A flagged proposal that turns out wrong later is cheap to fix; a blocked pipeline waiting on five
answered questions per Doll, 1,185 times, is not.

---

## Step 4: Phrase the Surviving Questions Efficiently

- **Prefer closed-form questions over open-ended ones.** A multiple-choice question with 3-4 concrete options
  takes seconds to answer; an open "tell me more about her backstory" prompt re-introduces exactly the writing
  burden this whole 00a/00b system exists to eliminate.
- **Always include a "you decide" / "propose one for me" option**, consistent with 00a's own established
  precedent for Enneagram and location of origin. This should be the easy, low-effort default answer available
  on every question this protocol generates.
- **Batch every surviving question for one Doll into a single pass.** Never resolve them one at a time across
  multiple interruptions — gather the full surviving list from Steps 2-3, present all of it together, and let
  the developer clear a given Doll's ambiguity in one sitting.

**Worked contrast, using the ex-soldier example from Step 1:**
- *Bad*: "Can you tell me more about her military backstory?" — open-ended, no bound on effort required, exactly
  what this protocol exists to avoid.
- *Good*: "Her Ghost — what actually happened to her unit: (a) lost them in a failure she blames herself for,
  (b) lost them to a betrayal from within her own ranks, (c) survived by abandoning them, and that's the wound,
  (d) something else, brief description, (e) you decide, I'll propose one." Bounded, fast to answer, and the
  "you decide" option means even this doesn't strictly require engagement if the developer would rather move on.

---

## Step 5: Record, Re-Tag, and Finalize

Once the surviving questions are answered (or deferred to "you decide" and proposed), every resolved field gets
re-tagged SOURCED (directly from the developer's answer) or, for a "you decide" resolution, STRONG INFERENCE
(now anchored by explicit developer permission to propose, rather than an unprompted guess). The deliberately
deferred fields (A9, A10's full web, A11) stay marked TBD, unchanged — they were never part of this
clarification pass and don't need to be.

**Once this step completes, Stage 1 is considered locked for this Doll** — the full sheet, with every field
either sourced, strongly inferred, or explicitly deferred, is ready to feed Stage 2's diagnostic toolkit. No
field should still be carrying a WEAK INFERENCE or BLOCKED tag at this point; if one is, it means Steps 2-3's
filter missed something load-bearing, and that's worth fixing in this protocol itself, not just for the one
Doll in front of it.

---

## Step 6: Track Recurring Gap Patterns (lightweight, closes the loop back to 00a)

If the same *kind* of gap keeps surfacing across many different Dolls — for example, if Gen/Mark keeps landing
as BLOCKED because vision statements rarely happen to mention it — that's a signal worth keeping visible, since
it suggests 00a's own seed-field design (specifically, what the vision-statement prompt nudges toward
mentioning) could be tuned to close that gap at the source, rather than this protocol having to keep resolving
the same category of ambiguity one Doll at a time. Not something to act on after a single occurrence — but worth
noting when a pattern becomes clear, as a candidate revision to `00a_Initial_Input.md` itself.
