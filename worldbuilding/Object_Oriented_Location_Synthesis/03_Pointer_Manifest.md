# Pointer manifest

**Created 2026-10-06.** Pointers now, copies at handoff (developer, 2026-10-06). Every address is absolute. Each row
was tested for existence on 2026-10-06 (`OK` = exists; line counts are as of that day). **Existence is not
admissibility or reliability.** A tier column will be added when the data pack is built (`00_RUNBOOK.md` §C.6).

**Repo roots used below:**
- `GDD` = `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD`
- `UNIV` = `/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline`

## A. The method (Package 1)

| Item | Address | State |
|---|---|---|
| ULM runbook | `GDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md` | OK, 3,160 lines. Project layer. |
| ULM `01`–`05`, `Run_Modes_Warm_and_Cold.md`, `README.md` | same folder | OK. Universal layer, with the fixes in `01_Inventory…` §4. |
| ULM disciplines `00b`, `00d`, `00f` | `…/Universal_Location_Methodology/Disciplines/` | OK. District vocabulary to generalize. |
| CST (original) | `GDD/Worldspace/Locations-and-Levels/Cultural_Synthesis_Techniques.md` | OK, 1,194 lines. `WITHHELD` from cold runs. |
| RWBEM (original) | `GDD/Worldspace/Locations-and-Levels/Real-World_Basis_Extrapolation_Method.md` | OK, 417 lines. `WITHHELD` from cold runs. |
| CST, RWBEM (the ULM's copies) | `…/Universal_Location_Methodology/Disciplines/` | OK. Which copy goes in is open (`01_Inventory…` §5). |
| T8 reading-consensus instrument | `…/Universal_Location_Methodology/PRE-TRIP_INSPECTION_RECIPE_TRIAL.md` §N, and `Tools/triple_read_verify.py` | OK. Generic by design. |
| Developer rulings log | `…/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md` | OK. **Project-wide rulings; which of them carry to orbit is open.** |
| Status and counts | `…/Universal_Location_Methodology/MASTER_Process_Tracker.md` | OK. The source for any honest status banner. |

## B. What exists on orbit and the later bodies

| Item | Address | State |
|---|---|---|
| Orbital Infrastructure scaffold | `GDD/Worldspace/Locations-and-Levels/Outside-World/Orbital-Infrastructure/README.md` | OK, 40 lines. **The only file in that folder.** The three build stages, the open items, the three downstream consumers. |
| Build order and rationale | `GDD/TODO.md`, the entry "Orbital infrastructure — logistics, mathematics, and dimensions" (line 1338 on 2026-10-06) | OK. Not copied. |
| Engineering math | `GDD/Theoretical-Calculations/` — `Orbital_Infrastructure_Mass_Budget.md`, `Von_Braun_Wheel_Mass_Budget.md`, `Design_Efficiency_Comparison.md`, `Amundsen_Tower_Space_Fountain_Design.md` | OK. **At the repo root, not under `Worldspace/`.** Note this when copying. |
| Orbital population (Census II) | `GDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Official_Population_Census.md` ("Orbital Population (Census II)") | OK, 796 lines. |
| Reserved home for orbital culture | `GDD/Neo-Races-and-Cultures/Orbital_Cryptograph_Helix_Era/` | OK. **Empty** (a `.gitkeep` and a 7,041-byte `README.md`). The `README.md` reads "extend the same method to the orbital infrastructure population". |
| The neo-culture method | `GDD/Neo-Races-and-Cultures/_Method/` | OK. Not read this session. |
| Solar Colonization era | `UNIV/Timeline Eras/3 The Solar Colonization/README.md` | OK. **0 lines. Empty.** |
| Post-Solar eras | `UNIV/Timeline Eras/4 Post-Solar eras/README.md` | OK. Not read this session. |
| Planetary symbols (neutral layer) | `GDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Symbolic_Substrate/Planetary_Symbols.md` | OK, 203 lines. **Subject to the symbol deferral (`DR-8`, `00_RUNBOOK.md` §C.7).** |
| Subnet symbolic associations | `GDD/Storyline/DLC-Questlines/Subnet_Symbolic_Associations.md` | OK, 484 lines. Subnet scale; the runbook says do not cross-apply it to city scale. |
| `Upper-Earth/` | `GDD/Worldspace/Locations-and-Levels/Outside-World/Upper-Earth/` | OK. `Timeline.md` is a **7-line redirect stub** to the universe repo. `Geography.md` is empty. |

**Where the timeline detail actually lives.** Memory, not a file I could confirm in this repo: Cryptograph Helix's
dating, the Outer Tepenia gap (roughly 1,000 years after the novel series ends), and the Jovian / Saturnian /
Centaurian mapping. The Outer Tepenia 1 README is the one verified-in-memory source for the gap. **To resolve:** locate
the file that states the Cryptograph Helix timeline and the Greater Tepenia outline, and add it here. This is the
largest gap in the manifest.

## C. The origin data pack (Package 2: pointers, since the corpus is unfinished)

| Item | Address | State |
|---|---|---|
| The city passes (the 38-city ULM) | `GDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/` | OK. **Four cities complete; Mirny in progress** (Steps −1 to 3 and Phases 2–8 done). The package is copied only after the corpus completes. |
| Founding Register | `GDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Founding_Register.md` | OK, 93 lines. Founders live only here. |
| Subnet regional personalities | see the memory entry "Subnet regional-personality guide". **Path not looked up this session.** | to locate |
| Acts, divergence operator, no-stereotypes law | `UNIV/Reference/No_National_Stereotypes.md` | OK, 174 lines. |
| Census I and II, composition | `…/Cities/Official_Population_Census.md` | OK. |
| Robot canon | `GDD/Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md` (438 lines); `UNIV/Reference/Robot_Universals/`; `UNIV/Reference/Laws_of_Robotics.md` (54 lines) | OK. Binds the whole universe. |
| Universe authority law | `UNIV/Reference/Repo_Scope.md` | OK, 30 lines. |
| World history | `UNIV/Reference/World_History_Reference.md` | OK, 351 lines. |

## D. The receiving repos

| Repo | Address | Role | State |
|---|---|---|---|
| CurrentNovelDocs | `/home/kuroskalacs/Documents/Doll-Fi/media/Literature/books/CurrentNovelDocs/` | **first**: low Earth orbit | OK |
| The Cryptograph Helix | `/home/kuroskalacs/Documents/Doll-Fi/media/Literature/books/The Cryptograph Helix series/` (`TheCryptographHelixDD/` inside) | **second**: Mars, its orbit, Venus, the Belt, early Jupiter | OK |
| Outer Tepenia series | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Outer Tepenia series/` (`Outer Tepenia 1`, `Outer Tepenia 2`, `Outer Tepenia New Centauri`) | **later**: noted at the developer's direction, 2026-10-06 | OK |

## E. What is not in this manifest, and why

- **Per-class physical data.** Not gathered. It needs real research under `LAW 0-R`.
- **A tier for each row.** Added with the data pack.
- **The locnames list** the layering-law check needs (`01_Inventory…` §4.1). It contains every location name, so a
  session that is not running a cold derivation should build it.

## F. Handoff copy list (filled at Package 1 and Package 2)

At handoff, the cited rows above are copied into the receiving repo. Rows to copy at Package 1: all of §A, after the
fixes in `01_Inventory…` §4, and the build-order and orbital rows of §B. Rows to copy at Package 2: all of §C.
**Stubs and redirects are not copied.** The `Upper-Earth/Timeline.md` stub is the reason: copying a pointer file would
carry a dead address into a repo that cannot reach it.

## G. Inputs the developer is supplying

| Input | Where it goes | State |
|---|---|---|
| Isaac Arthur video subtitle files, on the topics this library needs | `research/_inputs/` in this folder | **pending**: the developer is downloading them (2026-10-06). **Secondary source**: use for scope and leads, and check every number against a primary source before it enters a class (`02_Design_Brief.md` §8). |
