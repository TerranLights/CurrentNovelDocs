# Plan of Action: 2026-10-29 to roughly March 2027 (DRAFT)

**Opened 2026-10-23** by the Inner Tepenia GDD session, at the developer's request, in the shared worldbuilding folder so every repo can point to it. **Status: DRAFT, being worked out with the developer between 2026-10-23 and 2026-10-29.** Nothing here is a ruling until it appears under "Decisions" with a date. Items marked **(to inventory)** are placeholders that this week's inventory must replace with fact.

> **Not for the timeline repo.** The `TepenianUniverseTimeline` repo takes only finished, error-free canon. This plan and all drafting live here.

---

## 1 · What this plan is for

From **2026-10-29** the developer moves from Max 5x to **Max 20x** and intends to "power bulldoze" through as much of the universe's material as possible over about **four to six months**. The plan exists to (a) keep that effort on track and focused, (b) use every working hour and every allotment efficiently, and (c) let any repo's session find out in one read what is being done, in what order, and why.

## 2 · Decisions so far

| Date | Decision | Source |
|---|---|---|
| 2026-10-21 | The full ULM / CST / RWBEM, with vignette rounds, is expected to take **at least four or five months**; Fable is planned for CST, RWBEM and vignettes, Opus for ULM readers. The same processes later cover off-world settings. | developer |
| 2026-10-21 | **November run:** every city except Concordia (district method), Relung Panen and Amundsen Station. **Three Opus readers on every unit**; no trimming for cost ("if it runs over, I'll pay for another month"). **Casey first**, in a fresh session, not before 10-29. | developer |
| 2026-10-21 | CST and RWBEM run **strictly after** the ULM wave and its vignette round. No overlap. | developer |
| 2026-10-23 | **Sequencing:** the GDD city run goes first; every other project fills the gaps the run can't use. | developer |
| 2026-10-23 | **Hours law applies only to ULM / CST / RWBEM** (05:00 to 14:59; wrap-up 13:59), as written. Every other project's worldbuilding and drafting may run at any hour. | developer |
| 2026-10-23 | **Budget is planned in work units now** (a city pass, a vignette round, a chapter pass); the Casey run measures real cost, then units convert to weeks. | developer |
| 2026-10-23 | **First wave: the Inner Tepenia GDD and the Interwar worldbuilding.** | developer |
| 2026-10-23 | **Cryptograph Helix and the Outer Tepenia trilogy start with research on raw infrastructure** (what is possible and realistic). **Only after the full Second Interwar Period documentation is finished and complete** does work begin on deriving the societies that live in those settings and overcome their problems, hardships and struggles. | developer |
| 2026-10-23 | **No external deadline for any project.** The material is finished whenever it is done. The plan is therefore ordered by sequence and dependency, not by date; the month markers in section 3 are estimates for pacing, not targets, and nothing is cut or rushed to meet them. | developer |
| 2026-10-24 | **Post-war conditions are a later phase, added to the plan.** After the ULM, CST and RWBEM are all complete for every city, work out what the 38+ cities and societies were like after the Long Night War: how they changed, what they looked like, how they functioned (and how they collapsed). **It starts only after all three processes are complete and finished**, because a collapse can only be derived from a full model of the city when it was fully functioning. It builds on the Second Interwar picture of each city. Worked in the GDD repo (it is city work). | developer |
| 2026-10-24 | **Phases E and F can run at the same time.** Neither waits for the other: societies for Cryptograph Helix and the Outer Tepenia trilogy (E) and post-war conditions of the cities (F) may run in parallel. | developer |
| 2026-10-24 | **Mirny's loose ends and the three cities outside the November run (Concordia, Relung Panen, Amundsen Station) are scheduled in the plan** (section 4b). **Background research for all three may start this week.** | developer |
| 2026-10-24 | **Relung Panen's ULM may run this week, before the November run, provided the city is developed to the extent the ULM requires.** This is a conditional exception to "no city's ULM before 10-29"; Casey still runs first in the November run proper. The condition list is in section 4b. | developer |
| 2026-10-25 | **Volcanism and geothermal survey added** (developer): establish which cities have proximal access to geothermal heating and energy. Scope: all 38 cities; one flat row per city (nearest volcanic or geothermal feature, distance, type, activity status), no ranking and no cross-city comparison (comparison is the terminal check); no distance cutoff, so each row reports the nearest feature and its distance. Lives in the GDD at `Reference/Real-World/Volcanism_and_Geothermal/`. Real-world research only. Starts after the Relung Panen port round, to pace the allotment. | developer |
| 2026-10-25 | **Standard of living added as a phase (Phase G).** After the ULM is done and the cities are all developed, determine each city's overall standard of living. Placed after Phase D in the plan (see open question 9 for the exact trigger and era). | developer |
| 2026-10-25 | **Phase G confirmed:** it starts after Phase D (ULM, CST and RWBEM all complete); it measures the **Second Interwar**, when the cities were functioning (not the post-war era); it **feeds Phase F**; and it is determined for each city **on its own terms**, with no ranking or comparison between cities (that stays with the terminal check). | developer |
| 2026-10-23 | **The off-world library (OOLSD) moves to `worldbuilding/Object_Oriented_Location_Synthesis/`.** Done the same day: 96 files copied byte-identical and verified, old-path references updated, the GDD copy removed (history stays in the GDD git log), and a pointer left at the old location. The Concordia district work and the weapon, faction and religion catalogs stay in the GDD, as they derive from the cities. | developer (move and the stay-in-GDD reading, confirmed 2026-10-23) |
| 2026-10-23 | **Where the work happens.** The 35+ cities' ULM, CST and RWBEM are done in the **Inner Tepenia GDD repo**. **Everything else** (Interwar worldbuilding, Cryptograph Helix, the Outer Tepenia trilogy, off-world settings, novels, short films, and so on) is researched, compiled, experimented with and shaped in **`Literature/books/CurrentNovelDocs/worldbuilding/`** and its existing and yet-to-be-created subfolders. Only finished, error-free canon goes on to the timeline repo. | developer |

## 3 · The shape of the whole effort

```
10-23 ─ 10-29   PLANNING WEEK        inventory, rulings, Casey preflight, this plan finalized
10-29 ─ ~mid Dec  Phase A            ULM wave (GDD, 30 cities in scope), Casey first; Interwar worldbuilding fills gaps;
                                     CH / Outer Tepenia raw-infrastructure research fills gaps
        then      Phase B            vignette round after ULM (~60 per city)
        then      Phase C            CST wave (Fable), then its vignette round (~70-80 per city)
        then      Phase D            RWBEM wave (Fable), then its vignette round (~90 per city)
        gate      GATE               "Second Interwar Period documentation finished and complete"
        then      Phase E            societies for Cryptograph Helix and the Outer Tepenia trilogy
                                     (and the off-world settings via the OOLSD library)
        then      Phase G            STANDARD OF LIVING: each city's overall standard of living (after the ULM is done and the
                                     cities are all developed; after D; Second Interwar; feeds F; confirmed)
        then      Phase F            (runs in parallel with E) POST-WAR CONDITIONS (after the Long Night War): how each of the 38+ cities changed, looked and
                                     functioned, and how it collapsed. Starts only when A to D are complete for every city.
        after     Rebuild items      megasheets rewritten after all three processes; factions created after;
                                     weapon/gear catalog (gated until the 38-city corpus is done)
```

*(The month markers are guesses for pacing, not deadlines (there is none); they get replaced with measured figures after Casey. Phases A to D are strictly sequential for the GDD; the other tracks run beside them.)*

## 4 · Projects

**Where each track is worked** (ruled 2026-10-23): the GDD's 35+ cities run in the GDD repo; every other track runs in this `worldbuilding/` folder. The "What exists" column below can still point at material that lives in other repos today; that material is read in place until the developer decides whether to move it (see section 8, question 7).

| Track | What exists (to inventory) | Phase it lives in | Notes |
|---|---|---|---|
| **Inner Tepenia GDD** (`games/Inner Tepenia/InnerTepeniaGDD`) | 38 cities; ULM/CST/RWBEM methods built; Mirny ULM nearly done; 30 cities' Pre-Trip sheets and datasheets verified 2026-10-23; renames swept 2026-10-23 | A, B, C, D, F | The main daily block. Hard gates: no ULM before 10-29; 05:00 to 14:59 only. |
| **Interwar worldbuilding** (this folder: `nations/`, `history/`, `extractions/`; map project in `y-files/Map Files/`) | Post-war nations per region: several regions complete; Europe at Stage 1 (research notes); Africa unfinished; Russia Stage 1 | A (fills gaps), and the gate | The **Second Interwar docs complete** is the gate for societies in other tracks. The First Interwar sits upstream of it. |
| **Cryptograph Helix** (`Literature/books/The Cryptograph Helix series`) | (to inventory) | A: raw-infrastructure research. E: societies. | Solar Colonization era (Mars colonized; light Jupiter orbit; rudimentary Saturn exploration). |
| **Outer Tepenia 1 (Jovian), 2 (Saturnian), New Centauri** (`games/Outer Tepenia series`) | (to inventory) | A: raw-infrastructure research. E: societies. | Meta-civilization around Jupiter, Saturn and the Centauri binary. Uses the OOLSD library. |
| **Novels, including the Saga of Maggie Aarden** (`Literature/books/CurrentNovelDocs` and others) | (to inventory) | (to decide) | Ask the developer where each stands and what blocks it. |
| **Short stories, short films, TV** (`Literature/short stories`, `TV/*`) | (to inventory) | (to decide) | Southern Lights is the Second Interwar series. |
| **Audiocasts, other games** (`Audiocasts`, `games/*`) | (to inventory) | (to decide) | |
| **Shared tools and methods** (ULM tools, OOLSD library, Datasheet Methodology) | Built for the 38 cities | all | Built to be reusable for off-world locations; keep them reusable. |

## 4b · Scheduled items outside the main November run

### Mirny: the loose ends (GDD repo; ULM-hours work)
Mirny is not yet complete. These come at the start of Phase A, **after Casey** (Casey runs first, in a fresh session):

| # | Item | Notes |
|---|---|---|
| 1 | **Wind rewrite** of the Mirny files, per the developer's rulings on the wind register (`DR-56`, `DR-57`) | the first Mirny block, after Casey |
| 2 | **Cap-starved research** | the second Mirny block |
| 3 | **The "lived middle"** | still to be worked |
| 4 | **Open ledger answers:** the Planet symbol, Q-74 (held), Q-78 and Q-79 (no answer; left open) | leave blank where nothing naturally appears |
| 5 | **Developer declares Mirny complete** | the only thing that makes it complete |
| 6 | **Sweep the six held Mirny input files for the renames** | only after item 5 |

### The three cities outside the November run
All three keep their own prerequisites; none is run as a full ULM pass in November unless the developer says so. **Exception ruled 2026-10-24: Relung Panen's ULM may run this week, if it is ready.** If it runs: the hours law applies (ULM only 05:00 to 14:59, wrap-up 13:59), it uses three readers per unit like every other pass, and the usage window is Max 5x until 10-29.

| City | What it still needs | Method | Background research |
|---|---|---|---|
| **Relung Panen** | **Conditional go (2026-10-24): its ULM may run this week if it is ready.** Readiness, as checked 2026-10-24: sheets complete (verifier 0 fail after the completion pass); four ULM input gaps remain: (1) inspiration picks, drafted then approved; (2) its own Division-of-Industry row (a ruling on inclusion); (3) the census narrative entry; (4) the census composition tier table (items 3 and 4 wait on the held-file rename sweep, which waits for Mirny to finish; to be decided whether they can be written now under the new name). Also open: the port and the founding story (rulings). Then its culture, robot-culture, Enneagram and catalog (five stub files) and its Planet and Element symbols (last) | the Universal Location Methodology (ULM) | may start this week |
| **Amundsen Station** (real-world basis: Amundsen–Scott) | The developer wants it expanded first: a much larger population and a far more complex, intricate, engaging location for the DLC; its concept-art folder is empty; its Pre-Trip sheet, ledger and datasheets already exist (built 2026-10-21) | the ULM, after the expansion | may start this week |
| **Concordia** (the hub city) | Its 13 districts use the **district methodology**, a separate runbook; the hub city's own work is to be scoped | the district methodology | may start this week |

**Background research** here means gathering and organizing inputs before the pass (the "pre-staging" the plan already uses for all cities): it writes no culture conclusions. It is paced by the allotment, so it starts after the weekly reset (about 23:00 on 2026-10-24). A first step each is a short scoping note: what the city already has, what the research questions are, and which sources to look at.

## 5 · Dependencies that shape the order

- **Everything in the GDD derives from the 38 cities:** weapons, factions, religions, districts, music. None starts before the city corpus is done.
- **Founders come from the GDD's Founding Register**, which in turn depends on the post-war nations built in this worldbuilding folder. Europe's Italy split and the CIN are the current live case (`worldbuilding/nations/Europe - GDD hand-over intake…`).
- **Societies in later settings wait for the Second Interwar documentation** (developer, 2026-10-23).
- **Post-war conditions wait for the complete model of every city** (ULM, CST and RWBEM all finished). You cannot work out how a place collapsed until you know what it was like when it worked. Until then, the post-war spec fields (`Status`, `Connection to Concordia`, `Current Status`, `Legacy`) stay marked as not an input to any pass, exactly as the ULM already treats them.
- **Vignettes follow each wave**, and each wave follows the previous one strictly.
- **Megasheets are rewritten only after all three processes**; do not edit them meanwhile.
- **Operating hours:** ULM/CST/RWBEM only 05:00 to 14:59. Everything else is any-hour work and is where the gaps get filled.

## 6 · Daily and weekly rhythm (skeleton; to settle this week)

- **05:00 to 14:59:** the GDD city run (Casey first). Three Opus readers per unit.
- **After 15:00:** mechanics and any-hour work: Interwar worldbuilding, raw-infrastructure research for CH and Outer Tepenia, tooling, pre-staging the next city's inputs.
- **Weekly:** a short review: units finished, allotment used, what moved the plan. The ledger (section 9) is updated every day work happens.
- **Allotment awareness:** record the share used per task type from Casey on, so the plan can convert units to weeks.

## 7 · This week's agenda (10-23 to 10-29)

**Expectation (developer, 2026-10-23): the six days to 10-29 are mostly planning.** Some small things will get done along the way, but the week's main product is this plan, and nothing in it is rushed. The developer's allotment is at ~98% until about **23:00 on 2026-10-24**, so the first two days are for decisions and cheap reads, not research.

| # | Item | When | Status |
|---|---|---|---|
| 1 | Inventory each project: what exists, what blocks it, a rough work-unit estimate (status files only, no deep reads) | 10-24 to 10-27 | ☐ |
| 2 | Resolve the GDD's open rulings that block Casey's sheets (Casey Phase 7 conclusion rows, Casey Phase 3 ruin row, Denison war-word lines) | 10-24 | ☐ |
| 3 | Decide the order of the GDD's pending items (Santa Luce revisit, Relung Panen rulings, climate leftovers, Mirny wind rewrite and loose ends, Dumont d'Urville and Zukelli names) | 10-25 to 10-26 | ☐ |
| 3b | **Start background research** for Relung Panen, Amundsen Station and Concordia (scoping note first, then research; after the allotment reset) | from ~23:00 on 10-24 | ☐ |
| 4 | Casey preflight: fresh session, hours, readers, measurement plan | 10-27 | ☐ |
| 5 | Settle the Interwar worldbuilding order (which regions finish first; Europe's open items) | 10-26 | ☐ |
| 6 | Define "Second Interwar documentation finished and complete" as a checkable gate | 10-27 | ☐ |
| 7 | Finalize this plan; record it as decided | 10-28 | ☐ |
| 8 | Commit and push every repo's pending work | 10-28 | ☐ |
| 9 | **Begin** | 10-29, 05:00 | ☐ |

## 8 · Open questions for the developer

1. For each non-GDD project, what is the one thing that should be finished first, and what is "finished"?
2. What exactly counts as "the full docs for the Second Interwar Period finished and complete"? (A list of required documents, a coverage checklist, or the developer's own judgment call?)
3. For Cryptograph Helix and Outer Tepenia raw-infrastructure research: which questions are already known (orbital infrastructure, Mars, the Belt, Jupiter, Saturn, Centauri), and which of those has the OOLSD library started (starlifting was researched 2026-10-11)?
4. How many hours per day does the developer expect to be at the keyboard, and does anything fixed (job, family, travel) fall between now and March?
5. ~~Is there a hard external date (a release, a pitch, a deadline) for any project?~~ **Answered 2026-10-23: no. There is no external deadline; the material is finished whenever it is done.**
6. Should the plan hold a standing "ideas parking lot" so new ideas don't derail the track in progress?

7. ~~Should the off-world library move to `worldbuilding/`?~~ **Answered and done 2026-10-23: yes, moved.** **Confirmed 2026-10-23: the Concordia district work and the weapon, faction and religion catalogs stay in the GDD.**

8. ~~Phase F's order relative to Phase E~~ **Answered 2026-10-24: E and F may run at the same time.** *Still open:* does the post-war work reach the ruined state of the Antarctic cities only, or Upper Earth's post-war condition as well?

9. ~~Phase G (standard of living): trigger, era, link to Phase F, own terms~~ **All four confirmed 2026-10-25** (after Phase D; the Second Interwar; feeds Phase F; each city on its own terms).

## 9 · Progress ledger (one line per working day, newest last)

| Date | Track | Done | Allotment note |
|---|---|---|---|
| 2026-10-23 | GDD | Renamed-city sweep (live files, 14 folders, tool keys); Relung Panen stub files; Santa Luce founders ruled and revisit tracker written; hand-over to the worldbuilding session; this plan opened | at ~98% |
