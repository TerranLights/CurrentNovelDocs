# ⏩ MOVED 2026-10-23: this library now lives in the novel repo's worldbuilding folder

**New home:** `/home/kuroskalacs/Documents/Doll-Fi/media/Literature/books/CurrentNovelDocs/worldbuilding/Object_Oriented_Location_Synthesis/`. Moved from the Inner Tepenia GDD repo (`Worldspace/Locations-and-Levels/Object_Oriented_Location_Synthesis/`) at the developer's direction: all non-city worldbuilding is done in `worldbuilding/`, and the GDD repo is for the 35+ cities' ULM, CST and RWBEM. The files are byte-identical to the GDD copy at the time of the move (96 files). Absolute paths inside the scripts and the research brief were updated to the new location; dated entries below that mention the old GDD path are history. The GDD git history keeps the earlier versions. Plan: `worldbuilding/PLAN_OF_ACTION/00_MASTER_PLAN_DRAFT.md`.

---

# RESUME HERE: OOLSD library

# ✅ 2026-10-12: CANON COMPARISON DONE (all six checkpoint steps). Files in `research/`: `_canon_comparison_CHECKPOINT.md` (all boxes ticked), `_canon_extract_interplanetary.md` (K-1 to K-29), `canon_vs_physics_comparison.md` (32 rows: 12 consistent, 9 with conditions, 2 tension, 0 conflict, 7 no basis, 2 canon-internal; audit pasted at the end), `canon_adjustment_proposals.md` (AP-1 to AP-9, proposals only, nothing applied to canon). Headline: no canon claim in the research set is forbidden by physics; no date needs to move (canon's spans are 2.6-10x longer than the physics chain). Gaps: where orbital mass came from (propose Moon + near-Earth asteroids), dose standard (RL-1 open item), Tower export tonnage, Venus 'mines' meaning, Mars water source. **Awaiting the developer's decisions on AP-1, AP-2, AP-4, AP-6 (and smaller AP-3, AP-5, AP-9).** Next small research item suggested: polar-orbit consequences of a South Pole Tower. Mirny ULM Step 5 still waits for 05:00.

# ✅ 2026-10-12 ~00:40: TRANCHE 8 IS DONE AND SYNTHESIZED. All 11 files complete (planet_deconstruction 353 lines, Mercury inventory 392, Venus inventory 395, power and heat 650, orbital dynamics 420, oxygen/hydrogen for Mars water 432, Mars water budget 415, benefits Mercury 454, Venus 416, Sun 440, value and markets 507); `research/planetary_harvesting_and_benefits_synthesis.md` written (canon-free). Bookkeeping DONE and verified: `04_Handwave_Register.md` C-96 to C-167 (proposals) and `DEFERRED_RESEARCH.md` Batches 16 to 26 (118 rows); 15 earlier register rows got a "See also" sentence appended (C-12, 14, 29, 48, 51, 57, 59, 75, 77, 80, 81, 87, 90, 92, 95). Next handwave number: C-168. Headline: oxygen from Mercury/Venus to Mars and hydrogen from the Sun both fail on cost (Mars has 16-22 m of polar water and 43 wt% oxygen soil); taking Mercury apart is limited by planet-side heat (840-4,600 K surface), not machines; removing most of Venus would sweep Mercury through a chaos resonance; every real Sun benefit is light and gravity, not matter. **Still pending (needs the developer's go): compare all the syntheses with the existing interplanetary timeline and propose adjustments.**

# 🔄 UPDATE 2026-10-11 23:45: the usage window ran out at ~21:50 and all 11 tranche-8 agents died with only their file headings written; the window reset at 23:40 and **all 11 were re-dispatched at ~23:45** (new IDs are in `research/_calc/tranche8_status.py`).

# 🆕 READ FIRST, 2026-10-11 ~21:45: TRANCHE 8 DISPATCHED (11 opus agents). The developer asked for (a) research on all aspects of harvesting Mercury and Venus *the planets themselves*, and (b) full research on every benefit of mining Mercury, Venus and "mining" the Sun, with one agent on whether oxygen can be harvested from Mercury/Venus and hydrogen from the Sun and trucked to Mars to make water. Files in `research/` (agent IDs in `_calc/tranche8_status.py`): `planet_deconstruction_literature_and_engineering` · `mercury_whole_planet_inventory_and_extraction` · `venus_whole_planet_inventory_and_stripping` · `planetary_scale_power_and_heat` · `orbital_dynamics_of_planetary_harvesting` · `oxygen_and_hydrogen_supply_for_mars_water` · `mars_water_budget_and_retention` · `benefits_of_mining_mercury` · `benefits_of_mining_venus` · `benefits_of_mining_the_sun` · `value_and_markets_of_inner_system_materials`. Exact prompts: `research/_dispatch_prompts_tranche8.md`. **If the usage window cut them off:** `python3 -I research/_calc/tranche8_status.py`, then re-dispatch each INCOMPLETE or MISSING file with the one-line prompt at the top of the prompts file (each continues from its own SEARCH LOG). **When all report:** review each against the nine sections; enter candidate handwaves in `04_Handwave_Register.md` (next number C-96) and open threads in `DEFERRED_RESEARCH.md` (Batches 16 to 26; a bookkeeping agent did this for earlier tranches, prompt pattern in the session history: insert after the last table, never rewrite, `sed -i "Nr"`); write `research/planetary_harvesting_and_benefits_synthesis.md` (canon-free; answer the oxygen/hydrogen-to-Mars question directly, state where the premise holds and where not); then answer the developer. Still pending from before (needs the developer's go): compare the syntheses with the existing interplanetary timeline.

# (earlier) ✅ 2026-10-11 ~20:30: TRANCHE 7 IS DONE AND SYNTHESIZED. All three files complete (Mercury 582 lines, Venus 437, network 849); handwaves entered as `04_Handwave_Register.md` C-75 to C-95; open threads as `DEFERRED_RESEARCH.md` Batches 13 to 15; `research/inner_system_mining_synthesis.md` written (arithmetic `_calc/inner_mining_synthesis_calc.py`, authoritative output `..._output_run2.txt`). Headline: Mercury's surface holds only 1-2 wt% iron (core is 420-470 km down), so it is not the obvious iron mine; Mercury's strengths are sunlight, polar ice, Mg/Si/Al/Ca/O/S/C; leaving it (windows, fleets, arrival speed) is the hard part; Venus cannot export in bulk (about 180-670 kt lifted per kt delivered); Moon/asteroids suit Earth, the belt suits Mars. **Still pending (needs the developer's go): compare both syntheses with the existing interplanetary timeline and propose adjustments.** The banner below is the dispatch record.

# (dispatch record) 2026-10-11 ~19:25: TRANCHE 7 DISPATCHED (mining the inner Solar System). The developer asked: *"it sounds as though it would be better to stage a full-scale mining operation on Mercury (and maybe possibly Venus, maybe). What would be the logistics of mining the inner Solar System?"* Three opus agents, one file each, in `research/`: `mercury_as_industrial_site.md` (agent `a543e6c0bf845d3e0`) · `venus_as_extraction_site.md` (`a4ba0930d3021fc25`) · `inner_system_logistics_network.md` (`ab11524550f3db59b`). Exact prompts: `research/_dispatch_prompts_tranche7.md`. Status check: `python3 -I research/_calc/tranche7_status.py`. **If the usage window cut them off:** run the status script, re-dispatch each INCOMPLETE or MISSING file with the one-line prompt at the top of the prompts file (each continues from its own SEARCH LOG). **When all three report:** review each against the nine sections; enter their candidate handwaves in `04_Handwave_Register.md` (next number C-75) and open threads in `DEFERRED_RESEARCH.md` (Batches 13 to 15); write `research/inner_system_mining_synthesis.md` (Mercury and Venus as sources, what each actually holds, routes, fleet sizes for stated flows, ranges derived by shown arithmetic; canon-free); then answer the developer. **Already known before the agents report (from the tranche-6 files; correct the premise gently):** Mercury's *surface* is low in iron (about 73 percent of its mass is the core, only the outer 16 to 19 percent of the radius is mantle and crust); its sunlight is 6.67 times Earth's; escape is only 4.25 km/s, but leaving its orbit costs 7.55 km/s to reach Earth; no study of a Mercury mass driver or cargo fleet was found; Venus's cloud tops are as hard to leave as Earth's surface (about 9 km/s, a 1,800 kg vehicle for a 10 kg payload in a NIAC study), so Venus exports are the open problem.

# 🔄 UPDATE 2026-10-11 18:45: the usage window did run out; all five starlifting agents were cut off (each had only created its file). The window reset at 18:40 and **all five were re-dispatched at ~18:45** from `research/_dispatch_prompts_tranche6.md`, each told to continue from its existing file. New agent IDs: starlifting `a1d4ea1441f7ff500` · trucking `af5a8eca755bf6577` · processing and fabrication `a9ceeec8e6135c5f1` · ramp timelines `a4876aafedcc75812` · cyclers `a1aa064b7b80b81bf`. (The IDs in the tranche table below are the dead first-run IDs.) If cut off again, use the steps in the banner that follows.

# ✅ 2026-10-11 ~19:00: `cyclers_and_large_slow_vehicles.md` is COMPLETE (308 lines, 83 log rows, nine sections; agent `a1aa064b7b80b81bf`). Not yet reviewed by the orchestrator. Headline (agent's derived figures): no engineering study sizes an O'Neill- or torus-scale habitat as a vehicle; the physics allows it (thrust load is about 10^-5 of the spin load; a short cylinder is passively spin-stable), but 10^6 t needs about 10 GW of electric power and 0.1 to 0.8 years of thrusting per 1 to 6.4 km/s, with a 40,000 to 80,000 t power plant; 10^9 t-class structures are effectively immobile (128 years per km/s at 10 GW). Cycler orbits (Aldrin, S1L1, VISIT) are real, well studied, and need only small maintenance delta-v, but everyone boards by taxi at 3 to 12 km/s. Six candidate handwaves are listed in its section 7 (not yet entered in the register).

# ✅ 2026-10-11 ~19:00: `starlifting_physics_and_minimum_infrastructure.md` is COMPLETE (580 lines, 88 log rows, nine sections; agent `a1d4ea1441f7ff500`). Not yet reviewed. Headline: all starlifting literature is SPECULATIVE (no design study, nothing flown); the ideal energy to lift a kg off the photosphere is GM/R = 1.908 x 10^11 J/kg; lifting a tonne of iron from the Sun costs about 10^7 times the energy of lifting it off Mercury; the photosphere is about 0.119 percent iron by mass (841 t processed per t of iron); the Sun's natural wind loses 1.32 x 10^9 kg/s; the only flown solar-matter collection (Genesis) gathered 0.46 mg of hydrogen in 853 days; a sun-facing plate reaches a refractory-metal limit at about 1.9 solar radii. The agent found two arithmetic errors in Harry 2026 and one in Scoggins and Kipping 2023 (its Conflicts section). Still running when written: trucking (file shows nine sections, awaiting its report), processing and fabrication, ramp timelines.

# ✅ 2026-10-11 ~19:05: `industrial_ramp_timelines.md` is COMPLETE (480 lines, 157 log rows, 63 searches, 17 dead ends; agent `a4876aafedcc75812`). Not yet reviewed. It reports sourced rates and precedents only (no timeline of its own). Gaps it lists: the Lackner-Wendt 1995 paper, the NREL transformer report, the Chirikjian NIAC report, the full OIG ML-2 PDF, the Tiangong primary source, and any primary robot learning rate.

# ✅ 2026-10-11 ~19:06: `space_processing_and_fabrication.md` is COMPLETE (491 lines, 124 log rows, 52 searches, 13 dead ends, 16 worked calculations; agent `a9ceeec8e6135c5f1`). Not yet reviewed. Headline: integrated circuits, rare-earth magnets and lithium are the bottleneck; one robot's magnets need about 1,000 metric tons of asteroid material (the agent's derived figure); no whole-robot parts list was found.
**⚠ INCIDENT to check at review:** the processing agent reports that another agent's helper script in the shared scratchpad wrote three copies of ITS file into `space_trucking_and_transport_infrastructure.md`, and that it removed them (keeping all 116 of the trucking file's log rows; backup in the scratchpad). That edit was outside its brief. At 19:06 the trucking file had one set of nine headings and 137 table rows, but the trucking agent had not yet reported. **Before relying on the trucking file, confirm with its report and compare its log-row count and section contents; the scratchpad backup is `$TMPDIR`-style session scratch and may be gone.** Lesson for the next tranche: give each agent its own scratch subfolder or forbid shared helper scripts.

# ✅ 2026-10-11 ~19:20: STARLIFTING SYNTHESIS WRITTEN. `research/starlifting_synthesis.md` is done (arithmetic: `_calc/starlifting_synthesis_calc.py`, authoritative output `..._output_run2.txt`). Handwaves entered as `04_Handwave_Register.md` C-48 to C-74 (proposals, none accepted); open threads entered as `DEFERRED_RESEARCH.md` Batches 8 to 12 (80 rows). **NEXT (needs the developer's go): compare the synthesis with the existing interplanetary timeline and propose adjustments; nothing has been read back from canon yet.** Headline: starlifting from the Sun does not compete as a material source (1.2 x 10^7 times Mercury's lift cost per tonne of iron); first Mt-class habitat about 33 to 56 years from commitment in the fast-growth reading; a first Mars presence needs no space industry; Mars industrial independence has no sourced date; cylinders are a late, built-in-place stage, not an early trucking vehicle.

# (earlier) 2026-10-11 ~19:10: ALL FIVE starlifting-tranche files are COMPLETE. `space_trucking_and_transport_infrastructure.md` (565 lines, 137 log rows, 18 dead ends; agent `af5a8eca755bf6577`): the agent's report matches the file, so the cross-file INCIDENT noted below left it intact. Headline (agent's figures): leaving a 0.1 AU orbit costs about 33 km/s; about 1,000 t/yr of electric-propulsion trucking would need about 2.8 times the world's current xenon output; single-pass aerocapture has never flown; depots and mass catchers exist only on paper. **NEXT: review (enter handwaves and open threads), then write `research/starlifting_synthesis.md`** (see "When all five report" in the tranche section).

# ⏭️ READ THIS FIRST ON RESUME (written 2026-10-11 ~15:45; the 5-hour window was at 92 percent, replenishing at 18:40)

**Five research agents were running when this was written** (the starlifting tranche; table in the section "Sixth research tranche" below). If the window ran out, they are gone or paused and a new session cannot resume them by agent ID. Do this, in order:

1. `cd` to `research/` and run `python3 -I _calc/tranche6_status.py`. It lists each of the five files with its line count, how many of the brief's nine sections it has and its last write time. A file with all nine sections and a closing line is **done**. A file with fewer is **incomplete**; a **MISSING** file was never started.
2. For each incomplete or missing file: **re-dispatch it** with the exact prompt in `research/_dispatch_prompts_tranche6.md` (Agent tool, general-purpose, model opus, background), adding its one-sentence addendum so the agent opens its existing file and continues instead of restarting. (If the original agent is still alive in the same session, `SendMessage` to its ID with the standard resume text instead.) The files are written incrementally, so partial work is never lost.
3. Do not amend `_BRIEF.md`. Do not put canon or the interplanetary timeline into any prompt: **the developer ruled that the physics is researched on its own terms and the timeline is adjusted afterward** (2026-10-11).
4. When all five are done: follow "When all five report" in the tranche section (review against the nine sections, enter handwaves and open threads, write `research/starlifting_synthesis.md`, only then compare with the existing timeline and propose adjustments).
5. The developer's design note (early space trucking may involve O'Neill cylinders, as slower, larger environments) is a **design idea, not a finding**; file 5 tests it against the physics.

**The other thread (ULM, Mirny) is separate:** Step 5 (Reconciliation) is at Round 3; resume from `…/Mirny_Subnet/Mirny/.t8_Step5_CHECKPOINT.md` and the tracker's RESUME HERE, **only between 05:00 and 14:59**.

---



**Written 2026-10-06 ~14:10, because the weekly allotment was at 99 % and the 5-hour window at 92 %. An interruption of
days is possible.** Read this file first. Update the status lines in place.

## Two threads are open. Do not mix them.

### Thread 1: the OOLSD library (this folder)
Developer-confirmed model: Classes, Instances, Late Binding. Read `README.md`, then `02_Design_Brief.md`.

| Done | File |
|---|---|
| ✅ | `README.md`, `01_Inventory_Universal_vs_Antarctic.md`, `02_Design_Brief.md`, `03_Pointer_Manifest.md`, `04_Handwave_Register.md` |
| ✅ | `research/_BRIEF.md` (the shared research brief; **final, never amended**) |
| ✅ | Three research files, written by background agents. **All three complete 2026-10-06.** Orchestrator review is the next step. See below. |
| ⏸️ | The developer is downloading Isaac Arthur subtitle files into `research/_inputs/` (empty at 14:09). |
| ⏸️ | **`research/SHOPPING_LIST.md`** (2026-10-06): 33 items the developer may try to obtain, plus 14 public documents the orchestrator can retry (Part B). On resume, check `research/_inputs/` for anything new and read it with the checking rule: secondary sources are leads only. |

**Research agents (dispatched ~13:55 on 2026-10-06, same brief, one file each).** Each wrote its file first and appends
as it goes, so a stopped agent leaves usable material. At 14:09 the files held 99, 308 and 107 lines.

| File | Topic | Agent ID |
|---|---|---|
| `research/leo_and_orbital_habitats.md` | LEO, rotating habitats, microgravity, electronics and machines in vacuum | `a1df57f8b7829bfe9`: **✅ COMPLETE 2026-10-06 ~14:25** (452 lines, 51 searches, 10 dead ends). **Review first:** the 1974 O'Neill article's text (2-minute period at 3,200 m radius, 0.895 g) contradicts its own Table 1 (114 s, 0.99 g). Not opened: Pearson 1975, the Lofstrom paper, the 1952 von Braun article, the Lackner/DiZio review, six SP-413 appendices. Gaps: current nanotube-fiber strength; humanoid thermal data. Not yet reviewed by the orchestrator. |
| `research/mars_venus_and_transfer.md` | Mars, Venus, Earth–Mars and Earth–Venus transfer | `a5936119cee82df3e`: **✅ COMPLETE 2026-10-06 ~14:15** (456 lines, 111 logged rows, 19 dead ends, 22 conflicts). Its gaps: Venera 13 survival time (no primary), Mars temperature by latitude, and the Venus terraforming figures (known only through a preprint). Not yet reviewed by the orchestrator. |
| `research/belt_jupiter_saturn_and_deep_transit.md` | Belt, Jupiter, Saturn, propulsion, power | `aefab0ec44b5074a5`: **✅ COMPLETE 2026-10-06 ~14:30** (553 lines, 110 logged rows, 14 dead ends). **Weakest figures:** the Europa 5.4 Sv/day and Callisto 0.01 rem/day doses rest on secondary summaries only. **Source errors the agent found:** a fact-sheet summary gave Enceladus gravity as 0.027 m/s² (correct is about 0.11); published belt-spacing figures do not reproduce from their own counts. Unopened: Wiley/Springer papers (Paranicas 2007 and 2009, Becker 2017, Bagenal and Dols 2020), the Europa Lander report, the Daedalus report, the NTRS HOPE PDF (read via a mirror). Not yet reviewed by the orchestrator. |

**Second research tranche (dispatched 2026-10-10 ~23:35, same `_BRIEF.md`).** Developer: do the logged gaps (group 1) and
the uncovered topics (group 2) now. The Cryptograph Helix timeline file (group 3) comes **later**. Same resume rules as below.
Each prompt also let the agent read, read-only, the relevant sections of the first-tranche files.

| File | Topic | Agent ID | State |
|---|---|---|---|
| `research/gap_retry_leo_human_machines_power.md` | retry: ISS data, radiation, debris, electronics, human health, launch cost, propulsion/power refs, Folta/Bailey | `aea64c079eb917f12` | **✅ COMPLETE** (418 lines, ~45 searches, ~14 dead routes). Still open: ISS reboost propellant and monthly decay from a NASA/ESA primary; ISS eclipses per year; dose at 600 km; ORDEM 3.0 numeric fluxes and ballistic-limit tables; lifetime of very large structures. NASA's own crew-dose figures are 40–90 mSv and 72 mSv per six months, so the "80/160 mSv" claim stays unverified. Not yet reviewed. |
| `research/gap_retry_mars_venus_jupiter.md` | retry: Mars climate/lava tubes/perchlorate/ice/windows/dose; Venus tables, Venera 13, cloud radiation; Jovian, Saturnian dose primaries | `a41a46fa84ff25729` | **✅ COMPLETE** (516 lines, 101 log rows). Six candidate handwaves C-27…C-32 entered as proposals. **It corrects errors in the first-tranche files: see "Corrections to apply at review" below.** Open threads in `research/DEFERRED_RESEARCH.md` Batch 5. |
| `research/robot_body_in_space.md` | new: humanoid machine thermal, radiation, vacuum tribology, power, cold, reliability | `a29fe6df604e01b3f` | **✅ COMPLETE** (751 lines, 109 log rows, 17 dead or partly dead). Eight candidate handwaves C-1…C-8 are entered in `04_Handwave_Register.md` as proposals; **they await developer rulings**. Open threads are in `research/DEFERRED_RESEARCH.md` Batch 2. Not yet reviewed. |
| `research/life_support_lowg_power_structures.md` | new: closed-loop life support, low-g biology, power and thermal at scale, structures, debris shielding, regolith | `af602675dcc830250` | **✅ COMPLETE** (591 lines, 45 searches). Eleven candidate handwaves C-16…C-26 entered in the register as proposals. Open threads in `research/DEFERRED_RESEARCH.md` Batch 4. Not yet reviewed. |
| `research/moon_lagrange_and_comparables.md` | new: the Moon, mass drivers, Lagrange points, cislunar orbits; `[RW]` mechanism-only habitat comparables | `a81561c911f1e71b7` | **✅ COMPLETE** (443 lines, ~64 searches, 10 dead ends). Seven candidate handwaves C-9…C-15 entered in the register as proposals. Flagged conflict: the OIG ISS crew-time share (13% maintenance) is a planning share, not a measured fraction. Open threads are in `research/DEFERRED_RESEARCH.md` Batch 3. Not yet reviewed. |

**Still deferred:** group 3, the Cryptograph Helix timeline file (`03_Pointer_Manifest.md` §B).

## Third research dispatch

**Waste-heat utilization** (developer, 2026-10-11: "see if there's anything that can be done by reusing heat exhaust"). Same `_BRIEF.md`.
Agent `a9433a90b61d16123` → `research/waste_heat_utilization.md`. **✅ COMPLETE** (441 lines, 52 searches, 11 dead ends). Nine claims C-33…C-41 entered in the register; open threads are Batch 6 in the deferred list. Not yet reviewed. When complete, enter its open threads in
`research/DEFERRED_RESEARCH.md` as the next batch, enter its candidate handwaves in the register, and check it against the radiator
findings that C-1 and C-25 rest on. (Origin: the developer's Grok question, whose paste I could not find; see the deferred list, P1.)

## Evening of 2026-10-11: L4/L5 and heat batteries (worked)

- **Calculations done (orchestrator, with scripts in `research/_calc/` and raw outputs):** `research/lagrange_eclipse_calculation.md` (P3: eclipse and Sun-angle statistics at Earth-Moon and Sun-Earth L4/L5; radiator, heat-pump and storage sizing) and `research/body_orbit_eclipse_calculation.md` (P2: Moon, Mars, Jupiter, Saturn circular orbits, sunlight, heliocentric case). Both are **unreviewed by the developer**; their stated limits are in section 4 of each.
- **Fifth research dispatch (sourced search), agent `af44bf5a24fe831bb`: ✅ COMPLETE** (292 lines, 46 searches, 61 page opens, 13 dead ends; `research/lagrange_thermal_environment.md`). Flown L-point missions' thermal control (JWST, SOHO, Gaia, Herschel, Planck, DSCOVR, ARTEMIS, LRO's 151-minute eclipse, Lucy), Earth-Moon L4/L5 stability and dust, Sun-Earth L4/L5 and Earth trojans, heat-storage heritage, batteries, coatings, solar constant. **Not yet reviewed by the orchestrator beyond the cross-check in `lagrange_eclipse_calculation.md` §5.9.** Its open threads are entered in `DEFERRED_RESEARCH.md` as Batch 7, and six candidate handwaves (C-42…C-47: the agent's four plus two from the calculations) are in `04_Handwave_Register.md` as proposals awaiting your rulings.
- **Headline results (calculated; cross-checked, §5.9-5.10 of the L4/L5 file):**
  - **The point itself is unstable.** The Sun-forced orbit that replaces Earth-Moon L4/L5 is small (under 6,700 km from the equilateral point) and its error grows 9.7 percent per month (e-folding 318 days). The stable motion is on **large one-month orbits about 100,000 km (mean) from the point, 153,000 to 159,000 km at most**, in the size class the literature reports for 60,000 to 90,000 mile orbits. A "grav-locked" station is on such an orbit.
  - **Eclipses along those orbits:** about 1 to 1.5 whole-Sun-hidden events a year (longest 182 min) and 2.4 to 3.2 dimming events a year (longest about 352 min); one orbit family also has a total solar eclipse by the Moon about once in eight years (up to 16 min). Sun-Earth L4/L5: none.
  - Heat battery: no cycle to carry the station through at either point. Heat pump: saves 0 to 1.1 m2 of radiator per kW, costs 0.7 to 5.2 m2 of extra array. A flown lithium-ion battery unit (76 Wh/kg at unit level, ISS) carries 1 kW through a 2.8-hour eclipse at 36 kg against 202 kg for system-level paraffin PCM. LRO crossed a 151-minute eclipse by pre-heating its own structure.
  - Low orbits around the Moon, Mars, Jupiter and Saturn are in shadow 17 to 39 percent of every orbit; Jupiter and Saturn get 27 and 92 times less sunlight than 1 AU.
  - One conflict is open: Richichi et al. 2024 say a total solar eclipse from an L4 orbit occurs "once or very few times per month"; no orbit calculated here reproduces that.
- **The class it feeds:** "Orbital habitat at a Lagrange point" does not exist yet. Its parameters are in section 5 of the L4/L5 file.

## Sixth research tranche: starlifting and the industrial chain (dispatched 2026-10-11 ~15:30, same `_BRIEF.md`)

**Developer, 2026-10-11:** research "starlifting" (harvesting raw materials from the Sun): the minimum early infrastructure to begin; the infrastructure for "space trucking" of the materials back to Earth and Mars; the infrastructure to process and fabricate them into building materials and robots; and realistic timelines between stages. **Purpose:** to learn the general setting the characters live in, and the rough timespan from first setup to a civilization on Mars. **Ruling (developer, same session): do NOT force the data into the existing interplanetary timeline. Do the research, then adjust the timeline to what is scientifically realistic.** So the agent briefs carry no canon and no timeline; the synthesis is the orchestrator's job after all four report.

| File | Topic | Agent ID | State |
|---|---|---|---|
| `research/starlifting_physics_and_minimum_infrastructure.md` | what starlifting is in the literature, the Sun's composition, energy and mass-flow scales, near-Sun engineering (Parker Solar Probe), the minimum infrastructure, alternatives (Mercury, asteroids, Moon, Venus, gas giants) | `a018afb0c3905cd6e` | running |
| `research/space_trucking_and_transport_infrastructure.md` | delta-v legs, propulsion, throughput arithmetic, depots/tugs/catchers, launch-cost data, cargo packaging, minimum fleet | `a3087c9acfbd6473d` | running |
| `research/space_processing_and_fabrication.md` | ore-to-material chains, structures, robot fabrication and its bottleneck parts, self-replication closure studies, power and mass budgets, first-structure tonnage | `acd0b43fb3bcffbf0` | running |
| `research/industrial_ramp_timelines.md` | historical build-out rates, learning rates, space-station and Mars-settlement study timelines, bootstrapping doubling times, dependency lags (sourced rates only, no speculative timeline) | `a721724ab45263369` | running |

| `research/cyclers_and_large_slow_vehicles.md` | **added ~15:45 on the developer's point that the early stages of space trucking can involve O'Neill Cylinders (slower, larger environments):** Earth-Mars cycler orbits, the ferry problem, moving and steering large rotating habitats, cargo on slow carriers, tethers, end-point infrastructure | `a6141bb61a43c43a8` | running |

*(Developer note, same session, recorded as a design idea, not a finding: the existing canon makes Cylinders the long-term residence and Wheels the transport structure; the developer now suggests Cylinders may carry the early trucking. Do not change canon yet; the research decides whether the physics supports it, then the roles are adjusted.)*

**When all five report:** (1) check each file against the brief's nine sections; resume an incomplete one by `SendMessage` to its agent ID (*"Resume: continue exactly the task in the brief from where your file ends. Nothing in the brief has changed."*); (2) enter their candidate handwaves as proposals and their open threads in `DEFERRED_RESEARCH.md` as Batches 8 to 11; (3) write the synthesis, `research/starlifting_synthesis.md`: for each stage (first collection; trucking; processing and fabrication; robots; Mars presence), the minimum infrastructure, the sourced rates, a stage-to-stage duration range derived by shown arithmetic from the sourced rates, and what each range depends on; state plainly if starlifting from the Sun itself does not compete with the alternatives; (4) only then compare with the existing interplanetary timeline and propose adjustments to the developer. **Nothing in the synthesis may be read back from the canon timeline.**

## Plan for 2026-10-11 (developer; first written as 2026-10-12 after midnight on 2026-10-10 — corrected)

- **Morning: continue the ULM on Mirny.** Say *"Continue the city run."* Phase 9 (Populations) is next; ULM is restricted to 05:00–14:59.
- **Evening: more OOLSD research.** The L4/L5 and heat-battery work below. The OOLSD folder is logistics, so the hours law does not bind it.
- **Pending your rulings** (none blocks either): the 47 candidate handwaves (C-1…C-47; C-42…C-47 added 2026-10-11 evening) in `04_Handwave_Register.md`; class 01's open
  confirmations (type Installation + Settlement, what the station stages, orbit, robot count, dose budget); the Mirny Phase 8 axis choice.

## For the next day (2026-10-11), per the developer

**L4/L5 and heat batteries.** `research/waste_heat_utilization.md` §10.2–10.3 frame the work. `DEFERRED_RESEARCH.md` P2 and P3 list it. Start
with the **calculation** (eclipse and Sun-angle statistics at Earth-Moon and Sun-Earth L4/L5, arithmetic shown), then size a radiator and
heat-pump case, then compare heat-battery options at the cycle length found.

## Corrections to apply at review (found by the second tranche)

The retry agents read primary sources the first tranche could not, and they found these errors. **The first-tranche files
still carry the old values. Fix them at review, and cite the retry file.**

| # | Where the error stands | Correction | From |
|--:|---|---|---|
| 1 | `belt_jupiter_saturn…` and `mars_venus…`: Io **heat flow** attributed to Park et al. 2024 | Park et al. 2024 measures the tidal **Love number**, not heat flow. The heat flow (about 106 TW; about 2.5 W/m² derived) comes from Veeder et al. Values agree. | `gap_retry_mars_venus_jupiter` Conflict 13 |
| 2 | `mars_venus…`: Bullock and Grinspoon's Venus end state "**43 bar, 400 K**" | **Not in the paper** (it has a "3 bar regime"). Rejected. | Conflict 14 |
| 3 | `belt_jupiter…`: Europa "**5.4 Sv/day**" and "6–7 rad/s" | Appear in nothing opened. The SDT report's own numbers are mission-integrated: about 1.7 Mrad(Si) behind 100 mil Al. Both stay flagged. | Conflict 11 |
| 4 | `mars_venus…`: Venus **1-bar altitude** (about 50 km vs Landis's "slightly over 54 km") | Radio occultation and HAVOC put 1 bar near 50–51 km (about 343 K). Landis's 54 km is the outlier. | Conflict 8 |
| 5 | `mars_venus…`: Mars **global dust storm frequency** (one in three Mars years, Zurek and Martin 1993) | The post-2001 record gives about **0.2 per Mars year**. Trust that. | Conflict 3 |
| 6 | Mars **surface GCR dose** (design-study 0.22–0.38 mSv/day vs older 119 mSv/yr) | Trust the **RAD-anchored 0.64 mSv/day at solar maximum** and **232 mSv/yr**. | Conflicts 1–2 |
| 7 | Mars top-of-atmosphere irradiance (590 vs 586.2 W/m²) | **586.2**; scale the 1990 tables by 0.9936. | Conflict 4 |
| 8 | Venera 13 survival (157 vs 127 min) | Trust **127 minutes** (NASA Glenn papers). Still no Soviet primary. | Conflict 7 |
| 9 | GCR dose at Venus 62 km (Dartnell 9.5e-4 vs Herbst 2.49e-3 mGy/h) | Use the **Herbst (higher)** value for design. | Conflict 9 |
| 10 | Enceladus plume rate (200 vs 300 kg/s); ocean thickness (26–31 km vs about 45 km) | Use **200–300 kg/s**; ocean 26–48 km depending on the core model. | Conflicts 12, 15 |
| 11 | Perchlorate "9.8 mg of dust per day" | An **ingestion** yardstick (EPA gave no inhalation value), not an inhalation limit. | Conflict 16 |
| 12 | First-tranche (already known) | Enceladus gravity is about 0.11 m/s², not 0.027; the Belt spacing figures do not reproduce from their own counts; "80 / 160 mSv" per six months is unverified (NASA's own: 40–90 and 72 mSv); the 1974 O'Neill text and Table 1 disagree (0.895 g vs 0.99 g). | earlier notes |

**Deferred research (developer, 2026-10-11):** `research/DEFERRED_RESEARCH.md` lists the searches to run again later, with "search next" leads. Batch 1 (the LEO gap-retry file) is entered. **When each of the other four agents reports, append its open threads there as the next batch.**

**On resume, for each file:**
1. Count what it holds against the brief's nine sections (Scope · SEARCH LOG · Findings · Conflicts · Derived · Constraints ·
   Candidate handwaves · Open threads · Rejected sources). A file with all nine and a closing line is **complete**.
2. **Incomplete, agent alive:** `SendMessage` to its agent ID: *"Resume: continue exactly the task in the brief from where
   your file ends. Nothing in the brief has changed."* That is a resume, not an amendment (`00_RUNBOOK.md` §C.2).
3. **Incomplete, agent gone:** re-dispatch that topic alone, with `_BRIEF.md` and the same checklist. Its own file tells it
   what is already covered. The topic checklists are in the dispatch prompts, summarized here:
   - **LEO file:** LEO environment and radiation; machines and electronics in vacuum; microgravity health; spin-gravity
     physics and the O'Neill cylinder, Stanford torus and Von Braun wheel concepts; delta-v and transport; space elevators
     and fountains.
   - **Mars/Venus file:** Mars surface, orbit and resources; Earth–Mars transfer; Venus surface and cloud layer; Earth–Venus
     transfer; terraforming figures (flag speculative).
   - **Belt/Jupiter/Saturn file:** Belt; Jupiter's radiation and moons; Saturn, Titan, Enceladus; deep transit and
     propulsion; power scaling; a short interstellar-precursor note.
4. **After all three are complete,** the orchestrator (not the agents) does the review:
   - read each file's *Candidate handwaves*, and propose each to the developer. Do **not** add any to `04_Handwave_Register.md`
     without a ruling;
   - read each file's *Conflicts* and *Open threads*;
   - **spot-check** a sample of the high-confidence figures by opening the cited source;
   - then, and only then, start filling class **invariants** in `02_Design_Brief.md` §1 (fields 4–7). **No figure enters a
     class that is not in a reviewed research file.**

## Class drafting

- **`classes/01_Robot-Only_Staging_Station.md`**: drafted 2026-10-11 as the first class (the developer chose it over the O'Neill Cylinder). **Figures are
  carried from the research files and unreviewed.** It records the developer ruling **RL-1** (robots are radiation-vulnerable equivalently to
  humans; a robot EVA suit is for radiation; stations are shielded to a human requirement) in `04_Handwave_Register.md`. §12 lists what it
  taught about the template: add a "parameters" row for slots such as orbit, and `01`'s "Enclosed" does not fit an unpressurized shielded volume.
- **Next class suggestions:** O'Neill Cylinder (stage 2), Von Braun Wheel (stage 3), Orbital transit route (Interstitial by era).

## What to do next, in order, once research is complete

1. Review the three research files (above).
2. Add `research/_inputs/` material, if present: use it for scope and leads, and check every number against a primary
   source. Isaac Arthur is a secondary source.
3. Draft **one** class declaration end to end, to prove the template: suggested first = **O'Neill Cylinder** (canon stage 2,
   most research, and the least dependent on the neo-cultures). Show it to the developer before drafting more.
4. Work the `01_Inventory…` §4 list (the locnames check, STRIP of `03`'s address blocks, the "district" vocabulary, the
   four uninspected tools). These are mechanical and can be done at any hour.
5. Locate the file stating the Cryptograph Helix timeline and the Greater Tepenia outline (`03_Pointer_Manifest.md` §B, the
   largest gap).

## Open decisions (none blocks the above)

- **Type by era:** is a type change (Interstitial → Corridor) the same instance in a new frame, or a new instance?
- **Class granularity:** one class with the body as a slot, or a subclass per body? *Deliberately undecided; decide as we go.*
- **The Federation above orbit:** does any national layer sit above Mars instances in canon?
- **The inherited open items** in `02_Design_Brief.md` §5 (12 million versus 10,104,964; the human-heavy tilt).

## Standing rules (so a new session does not need to ask)

- **Pointers now, copies at handoff.** Consumer order: CurrentNovelDocs (LEO), Cryptograph Helix, later Outer Tepenia.
- **No physical figure from recall.** No named Mars nations, no demonyms, no stereotypes. Stock names come from Inner Tepenia's
  cities and subnets, never from present-day nations.
- **Physics fidelity:** only the enumerated handwaves are exempt (`04_Handwave_Register.md`). Nanotech gel-brain consciousness
  is the only one. A robot's body obeys physics.
- **Exodus phrasing:** a proportion of the population leaves, and *among those who leave*, most left in peacetime. It is not that
  most of the country left.
- **No level-scaling.** American English.
- **This folder is logistics, so it is any-hour work.** Deriving a *specific* location is not. That is the ULM, and it keeps its
  05:00–14:59 hours law.

## The other thread: Mirny, Step 4

**Phase 8 is done. Phase 9 (Populations) is next.** Its authority is `Universal_Location_Methodology/MASTER_Process_Tracker.md`,
`📍 RESUME HERE`. Say *"Continue the city run."* The Phase 8 checkpoint
(`…/Mirny_Subnet/Mirny/.t8_Phase8_CHECKPOINT.md`) is fully ticked. Phase 9 is **restricted-hours** work (05:00–14:59, wrap-up
13:59) and needs a fresh window.
**One pending item for the developer** from Phase 8: the axis was decided against the vote count, as "Prepared, not
predicted" (`04_Phase_08_Making.md`, Merge provenance and Snag 12). Their call if they prefer "Native at the door".
**Uncommitted:** everything written this session is in the working tree. Nothing is committed.
