# Canon extract: interplanetary and orbital claims (for the physics comparison)

*Written 2026-10-12 as step 1 and 2 of `_canon_comparison_CHECKPOINT.md`. Read-only extraction: nothing in any canon file was edited. IDs are `K-n`
(K for canon, so they do not collide with the handwave register's C-numbers). "Status" is what the source file itself says about the claim; no canon-tier
number is assigned here. Quotes are short and verbatim; numbers are copied, not paraphrased.*

## A. Sources read

| Tag | Path (from the GDD root unless absolute) | Notes |
|---|---|---|
| OIR | `Worldspace/Locations-and-Levels/Outside-World/Orbital-Infrastructure/README.md` | 40 lines; "scaffolding only, established 2026-07-05" |
| OCH | `Neo-Races-and-Cultures/Orbital_Cryptograph_Helix_Era/README.md` | 121 lines; rescoped 2026-08-29; boundary and handoff to the Cryptograph Helix repo |
| OMB | `Theoretical-Calculations/Orbital_Infrastructure_Mass_Budget.md` | 111 lines; "AI-assisted back-of-envelope... plausibility bounds, not literal hard numbers" |
| VBW | `Theoretical-Calculations/Von_Braun_Wheel_Mass_Budget.md` | 146 lines; same caveat |
| DEC | `Theoretical-Calculations/Design_Efficiency_Comparison.md` | 82 lines |
| ATD | `Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md` | 1,155 lines; read TL;DR, Primary Purpose, At a Glance, The Numbers, Throughput, Tertiary Functions |
| WHR | `/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/World_History_Reference.md` | sections "The Space Elevator", "The Off-World Evacuees" |
| T1 | `.../TepenianUniverseTimeline/Timeline Eras/1 The First Interwar Period/Timeline.md` | lines 262-286 |
| T2 | `.../TepenianUniverseTimeline/Timeline Eras/2 The Second Interwar Period/Timeline.md` | lines 555-600 |
| UTL | `.../TepenianUniverseTimeline/to-be-integrated/universe-timeline.md` | 46 lines; the copy in `TheCryptographHelixDD/series-overview/` differs and was **not** read (it is the Helix repo's, and the file says it still carries older dates) |
| HJ | `Worldspace/Characters/Dolls/Past_History_-_Known_to_Tepenians/Hana Jinn/README.md` and `Personal_Background/PreWar_History.md` | |
| MEM | project memory entries `project_orbital_infrastructure_stages`, `project_tepenia_multimedia_expansion`, `project_outer_tepenia_series` | summaries of earlier developer rulings; cited as memory, not as file text |

**Not read this pass (record, do not assume empty):** `TODO.md` (the orbital-infrastructure and "spaceborne robots" entries), `Official_Population_Census.md`
(the orbital section; its figures are taken from OIR), `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Symbolic_Substrate/Planetary_Symbols.md`
(Mars "Neutral" line), the Cryptograph Helix repo itself, the Mallory Dufay files, and `Robot_Biology_and_Culture/` (cited by OIR as holding the 3-stage order).
The sibling repo's `Timeline Eras/3 The Solar Colonization/README.md` and `4 Post-Solar eras/README.md` exist and are **empty (0 bytes)**: there is no
dated Solar-Colonization-era canon in the timeline repo yet.

**Scope boundary (OCH):** this repo "does not develop orbital society"; orbital-era questions belong to the Cryptograph Helix repo. Proposals that touch orbital society
must be addressed to that repo, not applied here.

## B. Claims

### B1. Orbital infrastructure stages and dates

| ID | Claim (verbatim or exact figure) | Source | Status in source |
|---|---|---|---|
| K-1 | Stage 1 is "Robot-only staging stations": small, light, low-tech, "needs no oxygen/breathable atmosphere, no food production, no sanitation — only energy harvesting (solar, for recharging) and radiation shielding"; "First orbital structure, predates the Falkland Treaty (built ~mid-2300s per Hana Jinn/Mallory Dufay character anchors, ~200+ years before the 2564 Treaty)" | MEM (stages); T1 L262-275 | Established 2026-07-02/04 |
| K-2 | Hana Jinn "was requested by name to relocate to ... A.R.U.Ta.G. ... to research metamaterials in order to build mass drivers to launch reusable rockets into low-earth orbit to begin building the early skeleton of orbital infrastructure"; dated "shortly after the Jeju-do ruling (early-to-mid 2300s)" (Jeju-do ruling 2318-04-27) | HJ README L40; PreWar_History L8; T1 L269 | Character canon; date range is a span, not a year |
| K-3 | Mallory Dufay "oversaw the actual first orbital launches and construction, placed closer to the mid-2300s" | T1 L272-274 | Same |
| K-4 | Stage 2: O'Neill Cylinders: "the first structure humans actually occupied alongside robots. Slow-moving, but huge and floor-space-efficient"; the "primary long-term residence structure for the rest of orbital history" | MEM (stages) | Developer-established 2026-07-02/04 |
| K-5 | Stage 3: Von Braun Wheels: "light and easy to move, trading away floor-space for mobility"; built "to transport robots and humans together over long distances specifically to build further orbital infrastructure"; Cylinders stay the real housing | MEM (stages) | Same |
| K-6 | "Orbital infrastructure exists, from early in the Second Interwar Period. Not a late development. It is in place well before the war." (Second Interwar = 2564 to 2812) | OCH s1 | Foundational for Inner Tepenia |
| K-7 | The cylinder-vs-wheel mass budget: cylinder "working estimate ~1-10 million metric tons for a functional 5,000-10,000 human+robot cylinder at 1G (for scale, the ISS is ~450 tonnes)"; Kalpana One "~7 million tonnes total (mostly shielding)" for ~3,000 people; wheel at R = 16-32 km "~10-25 million tonnes" for the same population; cylinder wins by "~5.4x" | OMB s2; VBW s7; DEC | "plausibility bounds, not locked canon"; AI-assisted, order-of-magnitude |
| K-8 | Debris-built case: total human-made mass in Earth orbit "~9,000-16,200+ metric tonnes"; a station built from 100% of it houses "roughly 200-800 humans" (cylinder, 100 m radius) | OMB s1, s3, s6 | Same caveat |
| K-9 | "Scaling beyond ~1,000-2,000 people at this mass budget requires importing material from the Moon or asteroids; debris alone cannot support more"; the Orbital Composition task "should stay within the plausibility bounds... scaling up only if canon separately establishes lunar/asteroid material imports" | OMB (Design Sensitivity; Relevance) | Guidance, not canon |
| K-10 | Orbit (Earth orbit) as the first and main site; the staging, Cylinders and Wheels are described in "low Earth orbit, primarily" | OIR Purpose | Scaffolding |

### B2. Amundsen Tower

| ID | Claim | Source | Status |
|---|---|---|---|
| K-11 | Tower completion "~2688, roughly the Second Interwar Period's own Midpoint, with genuine flexibility of 'plus-or-minus a couple of decades'"; destroyed 2812; operating window "roughly 120 years" (central estimate ~124); supersedes the older ~2629-2639 | WHR (Space Elevator); T2 L555-600; UTL | Developer-confirmed 2026-08-05 |
| K-12 | Design: 150 km space fountain; guide tube 225,000 t; pellet stream "~270 tonnes/s circulating, launched at 4 km/s"; "Net power draw ~324 GW (gross ~2.16 TW before regenerative recovery)"; base accelerator track ~1.63 km; "delivers ~3.62 km/s vertically vs. ~7.82 km/s orbital velocity needed... a final rocket stage still has to do real work"; base facility mass 3 million tonnes | ATD At a Glance; The Numbers | Working design |
| K-13 | Build: "~65-75 year" window; "construction material... ~3.225 million tonnes... delivered... in ~4 years"; "~8.8 tonnes/day average over 70 years" for the tube | ATD TL;DR item 7; At a Glance | Working design |
| K-14 | Primary purposes: "(a) continent-scale energy storage/regulation... (b) bulk mass-driving of material, not passengers": "bulk material export to orbit (feeding orbital manufacturing, including eventually robot fabrication)" and "the reverse (orbital goods shipped back down)"; passengers a side-application at "~194 people/hour" design capacity | ATD Primary Purpose; Tertiary Functions | Reframed 2026-07-05; developer-approved directions |
| K-15 | The Tower throughput of bulk **material** is **not quantified**: the pellet stream (~270 t/s) is a closed circulating loop "not consumed", not the payload rate | ATD The Numbers | Gap in canon (not a claim) |
| K-16 | Passenger arithmetic: to move the whole 10,104,964 orbital population needs "~9.30 people/hour" over ~124 years (older sections say "~6.48 people/hour" over "~178yr window"); the file's At-a-Glance table and the later section disagree on the window | ATD At a Glance vs Throughput | **Internal inconsistency in canon** (old window 178 yr, new 124 yr); flagged for the developer, not a physics matter |
| K-17 | "~200+ years of already-established off-world industrial capacity via the Hana Jinn/Mallory Dufay lineage predating the Treaty" | ATD Throughput | Stated as background |

### B3. Population

| ID | Claim | Source | Status |
|---|---|---|---|
| K-18 | Census II orbital population "10,104,964 combined (5,136,822 human / 4,968,142 robot, ~50.8% human / 49.2% robot) — about 31.6% of Tepenia's total population at the time the Long Night War began" | OIR | Corrected 2026-07-05; tied to `Official_Population_Census.md` |
| K-19 | "The ~12 million who left during the later portion of the Second Interwar Period, plus however many escaped during the Long Night War itself" form the founding population of the Cryptograph Helix series; reconciliation with K-18 is "an open item" | OIR; MEM (multimedia) | Open |
| K-20 | Orbital population composition is "unstarted" and gated | OCH | Open |

### B4. Beyond Earth orbit: Mars, Venus, Belt, giants

| ID | Claim | Source | Status |
|---|---|---|---|
| K-21 | Game present (≈2822-2827): the off-world evacuees' "Current infrastructure": "Orbital installations around Earth"; "Infrastructure inside and around the moons of Mars (Phobos and Deimos)"; "Active plans to colonize Mars itself; some robots already living on Mars"; "Presence further into the inner solar system, moving toward Venus"; "Data infrastructure in the space between Venus and Earth"; "The evacuee civilization has outgrown Tepenia in every material sense" | WHR (Off-World Evacuees); UTL row ≈2822-2827 | "Confirmed alive and established" |
| K-22 | Mars/Phobos/Deimos colonization "began during Inner Tepenia's own Second Interwar Period (2564-~2812)", per the Helix repo's own `universe-timeline.md`; and "Off-world evacuees were already 'moving toward Venus' by the end of the Second Interwar Period" | MEM (multimedia) | Citing a sibling repo; note it sits beside K-21's "active plans to colonize Mars itself" (see comparison) |
| K-23 | Cryptograph Helix opens "roughly 2-3 centuries after the Long Night War" ≈ "~3012-3112" ("deliberately fluid"), spans "a couple hundred years", **opens with Mars already fully colonized**; "At the series' opening, only Mars, its moons, and limited inner solar system regions are colonized"; "Jupiter colonization happens during Cryptograph Helix events"; Saturn: "very rudimentary" exploration by the end (Book 5 of 7 uses Saturn) | MEM (multimedia); UTL Lore Constraints | Developer-confirmed 2026-08-04 |
| K-24 | Venus in Helix: "floating prison gulags/mines"; "The ~300-500 year gap accounts for Venus becoming colonized and then exploited"; the Asteroid Belt is a real setting (Books 3-4); "Silicon Valley tech giants control Mars" at the series' opening | MEM (multimedia); UTL | Drafted prose exists in the Helix repo |
| K-25 | Outer Tepenia 1 opens "roughly 1,000 years after the ending events of The Cryptograph Helix" in a fully developed Jovian metacivilization; OT2 Saturnian; New Centauri Centaurian | MEM (Outer Tepenia) | Developer-confirmed; out of scope for this comparison (interstellar and giant-planet maturity) |
| K-26 | Mercury, the Sun, Moon and Earth-Moon points: **no canon claim found** in the files read | n/a | Gap |

### B5. Robots in space

| ID | Claim | Source | Status |
|---|---|---|---|
| K-27 | "Spaceborne" vs "Earthborne" robots: "Once orbital robot-manufacturing draws on space-harvested (not Earth-shuttled) raw materials, a subset of the robot population becomes genuinely spaceborne — never touched Earth"; a rich, undeveloped identity question; "first fully spaceborne generation" beat in the novels | MEM (multimedia) | Flagged design note, undecided |
| K-28 | Robots "have no need of oxygen/food/sanitation"; robot body is a human-shaped machine with a nanotech gel brain (consciousness is the only waved item per the research brief) | MEM (stages); `_BRIEF.md` | Established |
| K-29 | Orbit "originates knowledge the surface physically cannot produce"; orbital contact with the surface: early Second Interwar → 2812 "rich", datadrives physically carried up where bandwidth is insufficient; after 2812 degraded | OCH s2, s5 | Foundational |

## C. What is **not** in canon (gaps the physics comparison must not paper over)

- No dated Solar-Colonization-era timeline (the sibling folder is empty).
- No stated source of the **mass** of orbital structures beyond the debris-budget plausibility notes (K-8, K-9): the file itself says imports from the Moon or asteroids are
  required for anything beyond about 1,000 to 2,000 people, and "unless canon separately establishes" them, which has not been done.
- No stated tonnage for the Tower's bulk material export (K-15).
- Nothing on Mercury, the Sun, the Moon or Earth-Moon points; nothing on mining; nothing on where orbital chips, magnets or lithium come from.
- No stated population of Mars or Venus at any date.
