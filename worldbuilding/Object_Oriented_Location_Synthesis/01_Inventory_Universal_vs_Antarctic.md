# Inventory: what in the ULM, CST and RWBEM is universal, and what is Antarctic-specific

**Created 2026-10-06. Status: first pass, mechanical.** Package 1 (`README.md`) starts from this.

**How this was made, and its limit.** Line counts and keyword counts were run on each file. The ULM runbook
(`00_RUNBOOK.md`) was read in full this session. `01`, `02`, `04` and `05` were read at their headings and at the
passages cited below. The rest were **not re-read**. A keyword count says a file *mentions* a term. It does not say
the file *depends* on it. Rows marked **unverified** need a read before anyone acts on them.

Keywords counted, per file: `Antarctic`, `Concordia`, `Zhongshan`, `Shirayuki`, `Sinheung`, `Davis`, `Mirny`, `Census`,
`robot`, `Tepen`, `Cancer`, `district`.

## 1. The ULM's own layering, which the handoff builds on

The ULM already splits itself, by developer instruction (2026-09-03, "the LAYERING LAW"):

| Layer | Files | May name a location? |
|---|---|:--:|
| **Universal** | `01`, `02`, `03`, `04`, `05`, `README` | no |
| **Project** | `00_RUNBOOK.md`, `Pre-Contamination_Reviews/`, `06_Worked_Example_Provenance.md`, `Test_Runs/` | yes |

So the universal layer **is already largely written**. The handoff job is to verify the layering holds, then separate
what is left. It is not a rewrite.

## 2. File-by-file

Handoff action key: **AS-IS** copy unchanged at handoff · **POINTER** keep as a pointer now, decide at handoff ·
**STRIP** move the project instance out and keep the rule · **REWRITE** the universal form does not exist yet ·
**EXCLUDE** not part of the package.

| File | Lines | Verified findings | Layer | Handoff action |
|---|--:|---|---|---|
| `01_Frame_Typology_and_Inheritance.md` | 588 | `Antarctic` 0, `Tepen` 0, `Concordia` 0, `Census` 1, `Second Interwar` 1. Types include **Vessel**, **Structure**, **Corridor**, **Network locus**, **Interstitial**. Modifiers include **Orbital / extraplanetary**, **Enclosed**, **Mobile**. §5.1's inheritance classes (Determined / Inflected / Originated / Aggregated) and §5.2's provisional-inheritance protocol are the OO model's skeleton. | universal | **AS-IS.** One check: §4 (Frame) needs a non-Antarctic era example. Population bands were calibrated on cities; check they hold for a Mars-scale polity. |
| `02_Generators_Capability_and_Symbols.md` | 804 | `Antarctic` 0, `Tepen` 0, `Concordia` 1, `robot` 3, `Census` 4. §6.4 says the symbol REGISTER "is project-specific and lives in the runbook". | universal | **AS-IS**, with a check of the `Concordia`, `Census` and `robot` hits. G1's register is project data (runbook §C.7). |
| `03_The_Phase_Spine.md` | 1,195 | `Tepen` 55, `Falkland` 2, `robot` 18. The hits are the per-phase `MUST OPEN` blocks added 2026-09-07 (`M-169`) with absolute project addresses. | **mixed** | **STRIP.** The phase questions and mechanics are universal. The `MUST OPEN` blocks are the project address layer. Either move them to a per-project addendum, or leave them as a replaceable block. |
| `04_QA_Gates_and_Differentiation.md` | 926 | `Zhongshan` 11, `Davis` 2, `Sinheung` 1. These are the Parts V and V.2 measurement records, baseline tables and `Zhongshan_Opus`-keyed "DO NOT retrofit" notes. They are **run records inside a "universal" file**. | **mixed** | **STRIP.** The gates (0–11, C, F, I, P, G) are universal. The T-instrument baselines and run names are project data. The layering law's own check (`grep -c -F -f locnames.txt`) would have flagged these. |
| `05_The_Input_Contract.md` | 821 | `Antarctic` 0, `Tepen` 2, `Census` 5. The PROVIDED / RESERVED / PRODUCED / REQUESTED categories and §6's provenance rules are the "slot" vocabulary. | universal | **AS-IS.** Check the two `Tepen` hits. |
| `Run_Modes_Warm_and_Cold.md` | 178 | `Zhongshan` 1, `Concordia` 1, `Census` 4. | mostly universal | **AS-IS**, after moving the one `Zhongshan` hit. Note: the library's runs will be **warm** by default; cold runs need the quarantine apparatus, which is project-heavy. |
| `README.md` | 241 | not counted | universal | **unverified** |
| `Disciplines/00b`, `00d`, `00f` | 261 / 222 / 834 | `district` 14 / 26 / 56. Each carries a few project hits (`Concordia` 1, `Sinheung` 1). | universal in intent, **district vocabulary in practice** | **STRIP.** "District" is the worked-instance vocabulary of the method's origin. Generalize "district" to "sub-location of a parent". |
| `Cultural_Synthesis_Techniques.md` (CST) | 1,194 | `Concordia` 18, `Cancer` 19, `Sinheung` 10, `district` 52, `Tepen` 7, `robot` 8 | **mixed**, heavy in worked instances | **STRIP.** Sixteen techniques plus an extension. Each technique's worked instance comes from a Concordia district or Sinheung. The techniques are general. The instances must move out as pointers, the way `04` and the layering law already prescribe. |
| `Real-World_Basis_Extrapolation_Method.md` (RWBEM) | 417 | `Concordia` 5, `Cancer` 11, `district` 18, `Shirayuki` 1 | mixed | **STRIP**, as CST. Six steps. |
| `00_RUNBOOK.md` | 3,160 | read in full this session. See §3. | **project** | **POINTER**, and carve out a universal procedure (§3). |
| `Tools/` (5 scripts) | n/a | `triple_read_verify.py` takes a list of paths and ranges (generic by design). The other four (`quotation_audit.py`, `handoff_audit.py`, `phase_discipline_check.py`, `check_founders_against_register.py`) plus `rename_sweep_held_files.py` were **not inspected**. | unknown | **unverified.** At minimum `check_founders_against_register.py` and `rename_sweep_held_files.py` are Antarctic-specific by name. |
| `PRE-TRIP_INSPECTION_RECIPE_TRIAL.md` (T1–T8) | n/a | `T8` (three-reader read consensus) is a general instrument. The §6a/§6b address books are project data. | mixed | **STRIP** the address books. T8 is the reusable part. |
| `Stepwise_Execution/` | n/a | "Extracts, not authority" per the runbook. | derived | **EXCLUDE.** Regenerate from the packaged method. |
| `Pre-Contamination_Reviews/`, `Test_Runs/`, `Datasheets/` | n/a | Cold-run, test-run and per-city extraction records. | project | **EXCLUDE.** The library does not run cold. |

## 3. The runbook, carved

`00_RUNBOOK.md` is the **project layer**. Read in full this session, it carves up as follows. The *kinds* below are
reliable. The line ranges are not given.

| Section | Kind | Handoff |
|---|---|---|
| Law 0, the Law of No Forced Fit, the Law of One Location, the unit is one location, the typicality declaration | **universal laws** | **AS-IS** into the library. No Forced Fit and One Location are written for any location. |
| The Canon Registry §A (authority hierarchy), §B–§D, §C.1, §C.6–§C.8, §C.9 (research register), §C.10 | **project data** (Tepenian addresses, Antarctic frame data) | **POINTER.** The *form* (a registry with an absolute address and a tier for every row) is universal. The rows are not. |
| §C.2 Reader/Deriver isolation, §C.3–§C.5 | **universal technique, tooling-specific implementation** | **AS-IS.** The runbook states this itself: "The PRINCIPLE is universal… the IMPLEMENTATION is tooling-specific". |
| §C.9b–§C.9e (sequencing; Acts; divergence operator) | **project law that carries a universal operator** | **STRIP.** The **divergence operator** (separation · environment · struggles · goals · habits; never reason from elapsed time) is general. The Act-1 / Act-2 timeline is Tepenian. |
| Steps −1 to 10 (the procedure) | universal | **AS-IS**, with registry pointers. |
| Operating-hours law, memory blackout, graphify exception | **developer-workflow rules** | **EXCLUDE.** Not part of the method. |

## 4. What the handoff package will need that does not exist yet

1. **A locnames check on the universal layer.** `04`'s run records are the visible miss. Run the layering law's own
   mechanical check, with a proper location-name list, on `01`–`05`, CST, RWBEM and the Disciplines. The name list
   must be built **from the project's own registry**, and the check run by a session that is allowed to hold it.
2. **A generalized sub-location vocabulary** in `00b`, `00d`, `00f`, CST and RWBEM (they say "district" 56 times in
   `00f` alone).
3. **A per-project addendum slot** in `03` for the `MUST OPEN` blocks, so a receiving repo supplies its own.
4. **A tool audit.** Read the four `Tools/` scripts not inspected, and list their hard-coded paths.
5. **An honest status banner.** The ULM is stamped **PARTIALLY VALIDATED**. 4 of 38 cities are complete and Mirny is in
   progress. CST and RWBEM have **not run on any city** (`DR-14`: both are deferred until the ULM corpus completes).
   Whatever is handed over carries those dates and counts, and does not claim more validation than exists.

## 5. Questions this inventory cannot answer

- **Which copy of CST and RWBEM goes in?** The originals (at `Worldspace/Locations-and-Levels/`) are authoritative and
  `WITHHELD` from cold runs. The `Disciplines/` copies are "the ULM's own". They are the same text at the time of
  copying, but may drift.
- **Does the Interstitial type cover a *transit corridor* (an Earth–Mars transfer route), or does that need a class
  of its own?** `01` §1.1 lists Corridor and Interstitial separately.
- **Do `01`'s population bands hold at Mars scale?** Band 6 is 50M+. A Mars polity may be larger than any city and
  smaller than the Tepenian Federation.
