# Canon-vs-physics comparison: CHECKPOINT (resume file)

**Task (developer, 2026-10-12):** compare the OOLSD research syntheses with the existing interplanetary canon/timeline, and propose adjustments.
Rulings that govern it (2026-10-11): research the physics first, then adjust the timeline to what is scientifically realistic; adjustments are
**proposals for the developer, never applied**; do not edit any canon file in this task. Canon tiers: only Tier-1 hard canon outranks a finding;
flag everything else as "canon claim, not tested".

**If you are resuming after the 5-hour window reset:** read this file top to bottom, find the first unticked box, do that step, tick the box,
update the `LAST TOUCHED` line, continue. Do not redo ticked steps. Every step writes its output to a file named below, so nothing lives only in
context. The final answer to the developer is step 6.

## Inputs (physics syntheses, all in `research/`)
`starlifting_synthesis.md` (SYN) · `inner_system_mining_synthesis.md` (IMS) · `planetary_harvesting_and_benefits_synthesis.md` (PHB). Their
source files are listed in each. Handwave register: `../04_Handwave_Register.md` (C-1 to C-167).

## Steps
- [x] **1. Locate canon sources.** *(done 2026-10-12; paths in `_canon_extract_interplanetary.md` section A)* List every file that states interplanetary or orbital canon (orbital infrastructure stages, O'Neill Cylinders,
  Von Braun Wheels, staging stations, Amundsen Tower, Mars/Phobos/Deimos colonization, Venus, Belt, Jupiter/Saturn, Cryptograph Helix and Outer
  Tepenia timing, 12 million emigrants, space-harvested robot materials, robot "spaceborne" generation). Search by filename and `grep -il` only,
  then read. Record paths in `research/_canon_extract_interplanetary.md` section A. Candidate locations: `Worldspace/Locations-and-Levels/Outside-World/Orbital-Infrastructure/`,
  `TODO.md` (orbital entry), `Theoretical-Calculations/`, `Official_Population_Census.md`, sibling repos (`TepenianUniverseTimeline` at
  `/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/`; `TheCryptographHelixDD`; `OuterTepenia1_GDD`), memory entries
  `project_orbital_infrastructure_stages`, `project_tepenia_multimedia_expansion`, `project_outer_tepenia_series`.
- [x] **2. Extract canon claims.** *(done 2026-10-12; K-1 to K-29 in section B; gaps in section C)* In `_canon_extract_interplanetary.md` section B: one numbered row per claim (claim text, file path and line, canon
  tier, date or duration it implies). Quote sparingly; no paraphrase of numbers. Include every date and duration, every stated mass, population,
  material source and travel claim.
- [x] **3. Build the comparison.** *(done 2026-10-12: `canon_vs_physics_comparison.md`, 32 rows; 12 consistent, 9 with conditions, 2 tension, 0 conflict, 7 no basis, 2 canon-internal)* In `research/canon_vs_physics_comparison.md`: one row per canon claim, columns: Canon claim (with ID from step 2) ·
  Physics finding (with the synthesis and section) · Verdict (CONSISTENT / CONSISTENT-WITH-CONDITIONS / TENSION / CONFLICT / NO PHYSICS BASIS) ·
  Why. Work through the claims in order; tick sub-boxes below as groups finish.
  - [x] 3a. Orbital infrastructure stages and dates (staging stations ~mid-2300s, Cylinders, Wheels; Tower ~2630-2640 vs ~2688)
  - [x] 3b. Materials: where orbital structures' mass comes from; Amundsen Tower export of raw material; "space-harvested" robot materials
  - [x] 3c. Robots: what can be made in space (chips, magnets, lithium), "spaceborne" robots
  - [x] 3d. Mars: colonization dates (Second Interwar start; fully colonized by ~3012-3112), water, population
  - [x] 3e. Venus (floating gulags/mines), Belt, Jupiter, Saturn, Mercury/Sun if any canon exists
  - [x] 3f. Population: 12 million emigrants, orbital census ~10.1 million
  - [x] 3g. Durations between stages (use [SYN] section 5 ranges, [IMS], [PHB] section 3.4)
- [x] **4. Proposals.** *(done 2026-10-12: `canon_adjustment_proposals.md`, AP-1 to AP-9)* In `research/canon_adjustment_proposals.md`: for each TENSION/CONFLICT, a proposed adjustment with options, the physics
  basis, what it would change downstream, and what is NOT being proposed. Number them AP-1, AP-2... Keep the "both-are-true" test: where canon can
  stand with a stated condition, say so first. Never apply anything.
- [x] **5. Audit.** *(done 2026-10-12: section 6 of the comparison; one canon wording slip added to AP-5)* Re-open `canon_vs_physics_comparison.md`; check every physics cell against its source file line (grep the number); check every
  canon cell against its source line; fix and note corrections at the bottom. Paste any raw check output, do not summarize it.
- [x] **6. Report.** *(done 2026-10-12)* Tell the developer: verdict counts, the proposals in order of consequence, and what needs their decision. Update
  `RESUME_HERE.md` (top banner) and the memory entry `project_oolsd_starlifting_tranche.md`.

## Files this task creates
`research/_canon_comparison_CHECKPOINT.md` (this) · `research/_canon_extract_interplanetary.md` · `research/canon_vs_physics_comparison.md` ·
`research/canon_adjustment_proposals.md`.

## Notes and snags (append as they happen)
- Canon not read this pass (listed in extract section A): TODO.md orbital entries, Official_Population_Census orbital section, Planetary_Symbols Mars line, Helix repo, Mallory Dufay files, Robot_Biology_and_Culture. Read them in step 3 only if a row needs them.
- Sibling timeline repo folder `3 The Solar Colonization` is EMPTY (0-byte README): no dated Solar-Colonization canon exists.
- Canon-internal inconsistency found (not a physics matter): Tower design file's At-a-Glance says a ~178-yr window / ~6.48 people/h; its Throughput section says ~124 yr / ~9.30 people/h (K-16). Report to the developer; do not fix.
- Orbital-society questions belong to the Cryptograph Helix repo (OCH); proposals that touch them are addressed there, not applied here.

**LAST TOUCHED:** 2026-10-12, ALL STEPS DONE. Waiting on the developer's decisions on the proposals; nothing was applied to canon.
