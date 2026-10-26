# Seventh research tranche (mining the inner Solar System: Mercury, Venus, and the logistics network): the exact dispatch prompts

**Saved 2026-10-11 ~19:25.** Triggered by the developer's question after the starlifting synthesis: *"it sounds as though it would be better to stage a full-scale mining operation on Mercury (and maybe possibly Venus, maybe). What would be the logistics of mining the inner Solar System?"*
Each agent is told to read ONLY its own numbered section below, so the saved text and the dispatched text are the same.
**To re-dispatch a lost agent:** Agent tool, type general-purpose, model opus, background, with the one-line prompt: *"Your task is section N of /home/kuroskalacs/Documents/Doll-Fi/media/Literature/books/CurrentNovelDocs/worldbuilding/Object_Oriented_Location_Synthesis/research/_dispatch_prompts_tranche7.md . Read the common rules at the top and section N only, and follow them exactly. Your file may already exist: open it first, read its SEARCH LOG, and continue from where it ends; do not restart and do not duplicate sections."*
(`SendMessage` resumes a live agent only.)

**Developer rulings that govern all three:** research the physics on its own terms; do NOT force results into any story, timeline or canon; the briefs contain none. Anything surprising for the developer's premise (for example, what Mercury's surface actually holds) is reported plainly with its numbers.

## COMMON RULES (apply to every section)

You are a research agent for the OOLSD library. Your shared brief is at /home/kuroskalacs/Documents/Doll-Fi/media/Literature/books/CurrentNovelDocs/worldbuilding/Object_Oriented_Location_Synthesis/research/_BRIEF.md . Read it first and follow it exactly (it is final; nothing in it changes), including the nine output sections, the search-log discipline, "no figure from memory", and the 120-word final reply.
- Research physics and engineering only. Assume no story, timeline or setting. If a concept is infeasible, uneconomic or only a thought experiment, say so plainly and give the numbers that decide it.
- **Create your file FIRST** (heading plus `## SEARCH LOG`) and append as you go, so an interruption leaves something usable. If your file already exists, open it, read its SEARCH LOG, and continue from where it ends.
- **Scratch folder:** put any temporary file ONLY in /tmp/claude-1000/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/3ccdb441-c6c0-49c3-a71c-ab4a4fdd3c1e/scratchpad/ in a subfolder named after your file. **Never delete, move or overwrite any file in the research folder other than your own output file.** Other agents are writing there at the same time.
- Where an arithmetic result matters, run it (Python is available) and show the formula and inputs; inputs must be sourced constants.
- Work breadth-first across the checklist, then go back and query each quantity from a second angle (LAW 0-R). A quantity found once is one source.
- Do not read or edit anything else in the repository other than the sibling files named in your section (read-only).

---

## 1. `research/mercury_as_industrial_site.md`

Output path: /home/kuroskalacs/Documents/Doll-Fi/media/Literature/books/CurrentNovelDocs/worldbuilding/Object_Oriented_Location_Synthesis/research/mercury_as_industrial_site.md

TOPIC: Mercury as a site for large-scale mining, processing and launch of material: what is actually there (the surface that can be mined, not just the planet's bulk), the environment a mining operation must survive, the power available, and what the literature says about using it. Report plainly anything that cuts against the premise that Mercury is a rich iron source.

Checklist (cover each, or list the gap under Open threads with the reason):
1. Surface and near-surface composition from MESSENGER (X-ray, gamma-ray and neutron spectrometer results): weight percent of Mg, Al, Si, S, Ca, Fe, Na, K, Cl, C, Th, U, Ti, and the regional variation (northern smooth plains, high-magnesium region, volcanic terrains, low-reflectance material and its carbon). Whether any measurement shows free iron-nickel metal or iron-bearing minerals at the surface, and how much. Sulfur content and what it implies for processing.
2. Bulk structure: core radius and mass fraction, solid inner core, mantle and crust thickness, bulk density; how much of Mercury's metal is reachable from the surface, if any published study addresses that. Give the ranges and the disagreements between interpretations.
3. Regolith and surface properties: depth, grain size, bulk density, thermal inertia, strength; micrometeoroid flux at Mercury compared with the Moon; surface charging and dust.
4. Thermal environment: equatorial day maximum and night minimum; temperatures at 85 degrees and at the poles; permanently shadowed craters; the 3:2 spin-orbit resonance and the 176-day solar day; the subsurface depth where temperature becomes steady; how long a site stays sunlit or dark at the equator and near the poles, and the "peaks of eternal light" findings.
5. Volatiles: polar water-ice inventory (radar, neutron spectrometer, laser altimeter and reflectance results), the dark insulating layer over it, ice thickness and mass estimates with their uncertainty, other volatiles (sulfur, sodium, potassium, exosphere species). State the disputes.
6. Solar power: flux at perihelion, mean and aphelion; photovoltaic efficiency and degradation versus temperature (primary data, including BepiColombo and any high-temperature or high-intensity cell work); concentrator and reflector options; power per square meter of array; night storage over a roughly 88-day equatorial night versus polar siting; published surface power concepts for Mercury landers.
7. Radiation and plasma: solar energetic particle flux at 0.31 to 0.47 AU, galactic cosmic rays, the magnetosphere's shielding at the surface, micrometeoroid and impact-ejecta environment.
8. Landing, surface launch and orbit: surface gravity and escape speed; low-orbit stability and lifetime; the feasibility and scale of a surface electromagnetic launcher (mass driver or railgun), launch loop or rotating tether on an airless body with Mercury's gravity, using published designs for the Moon as the nearest anchor and stating any scaling you derive; the choice of launch direction relative to Mercury's orbital velocity.
9. Published concepts for using Mercury's material: disassembly or mining concepts (Armstrong and Sandberg and others), Mercury propellant from polar ice, any Mercury mass-driver or Mercury-industrialization paper, and the "Mercury as a solar-power or Dyson-swarm base" literature. For each: stated masses, rates, power, timescales and evidence level (demonstrated, engineering-studied, speculative).
10. Processing: given the composition in item 1, which products a Mercury operation can make (silicates, magnesium, aluminum, calcium, sulfur, carbon, any iron), and the energy per kilogram for solar-furnace and electrolysis routes from primary sources; achievable furnace temperatures and concentration ratios at Mercury's flux; consequences of high sulfur, sodium and potassium.
11. Hot-environment engineering: electronics temperature limits and demonstrated high-temperature electronics (silicon carbide and others), radiator sink temperatures at the equator versus the poles, shadow as a heat sink, and the general constraint on a human-shaped machine's heat rejection there.
12. Operations: light-time and solar-conjunction blackout for Mercury links, relay needs, what MESSENGER and BepiColombo have demonstrated (orbital lifetimes, thermal survival), and the fact that no lander has operated on Mercury (state what landing studies exist and what they assumed).

You may read, read-only: space_processing_and_fabrication.md, space_trucking_and_transport_infrastructure.md, starlifting_physics_and_minimum_infrastructure.md, moon_lagrange_and_comparables.md (to avoid repeating what they hold; cite them instead of re-deriving). Final chat reply at most 120 words.

---

## 2. `research/venus_as_extraction_site.md`

Output path: /home/kuroskalacs/Documents/Doll-Fi/media/Literature/books/CurrentNovelDocs/worldbuilding/Object_Oriented_Location_Synthesis/research/venus_as_extraction_site.md

TOPIC: Venus as a source of material for the rest of the inner Solar System: what its atmosphere and surface hold, how it could be extracted from floating platforms or the surface, and, the hard part, how any of it gets off the planet. The environment of cloud-level habitation is already in the sibling files; this file is about extraction and export, so cite the siblings for environment and add only what is new.

Checklist (cover each, or list the gap under Open threads with the reason):
1. Atmospheric inventory: total mass and the mass of each element (carbon, nitrogen, oxygen, sulfur, hydrogen, noble gases) from the composition tables; trace species and their altitude profiles; the mass and composition of the cloud and haze droplets; water content by altitude. Show the arithmetic.
2. What is scarce in the inner Solar System and what Venus uniquely holds: sourced inventories of carbon, nitrogen, hydrogen and sulfur on the Moon, Mars, Mercury, carbonaceous asteroids and Earth-crossing bodies, compared with Venus (derive the ratios from sourced numbers).
3. Extraction from the atmosphere: published processing concepts and the demonstrated hardware nearest to them (MOXIE on Mars: kg per hour and kWh per kg; solid-oxide electrolysis of carbon dioxide; nitrogen separation; sulfuric acid collection), with energy per kilogram, hardware mass and status (demonstrated, studied, speculative).
4. Floating platforms and aerostats: HAVOC, Landis, VAMP and other published concepts with masses, payloads, altitude, power, lifetime; lifting-gas options (hydrogen is scarce on Venus; breathable air or other gases in carbon dioxide); materials that survive concentrated sulfuric acid, with demonstrated exposure data; platform failure modes, including descent into hotter layers.
5. Power at cloud level: solar irradiance versus altitude (measured by probes and balloons), photovoltaic options, wind speed and the superrotation, turbulence; platform energy budgets.
6. The surface: composition from Venera and Vega X-ray fluorescence (weight percent by oxide), rock types, regolith; temperature, pressure and heat flux; what has operated there and for how long (Venera 13 and others); demonstrated high-temperature electronics and mechanisms (silicon carbide and the NASA Glenn Venus-chamber work, the LLISSE sensor); thermodynamic cost of rejecting heat into a 735 K environment (derive the ideal work per watt from sourced temperatures); published concepts for surface sampling or mining from aerostats or tethers.
7. Getting out of the well: the cloud-top ascent (Venus Ascent Vehicle, Landis and Oleson); orbital and escape speeds; published alternatives for bulk export: balloon-launched rockets, electromagnetic launch from a high platform, rotating tethers or skyhooks, a Venus space elevator (derive the synchronous orbit radius from Venus's 243-day rotation and compare it with the planet's Hill sphere radius, with sourced inputs), laser-thermal or beamed propulsion. Give each one's stated feasibility and numbers; mark SPECULATIVE where it is.
8. Venus orbital infrastructure: aerobraking and aerocapture at Venus (Magellan and others), useful orbits, Lagrange points, solar conjunction communication blackouts, the delta-v and transfer times between Venus and Earth, Mars and Mercury (cite the trucking file for the tables; add only what is new).
9. Published architecture and economics: Landis 2003 "Colonization of Venus", Venus ISRU and resource studies, with their stated platform masses, processing rates, imports and populations supported.
10. Atmosphere-removal and terraforming literature, only for its energy and mass scale (for example the energy to remove a stated mass of carbon dioxide), as a measure of how large the inventory is relative to any plausible extraction rate.
11. Hazards to equipment and to a human-shaped machine at cloud level: sulfuric acid, lightning (state the evidence level), cosmic-ray dose at cloud altitude (cite the sibling file), temperature at each altitude.

You may read, read-only: mars_venus_and_transfer.md, gap_retry_mars_venus_jupiter.md, space_trucking_and_transport_infrastructure.md, space_processing_and_fabrication.md, life_support_lowg_power_structures.md. Final chat reply at most 120 words.

---

## 3. `research/inner_system_logistics_network.md`

Output path: /home/kuroskalacs/Documents/Doll-Fi/media/Literature/books/CurrentNovelDocs/worldbuilding/Object_Oriented_Location_Synthesis/research/inner_system_logistics_network.md

TOPIC: the network-level logistics of mining and moving material among Mercury, Venus, Earth, the Moon, Mars, near-Earth asteroids and the main belt: routes, windows, propulsion near the Sun, launch from airless bodies, capture at the destination, fleet sizes for stated flows, communications, and propellant supply. The trucking file already holds delta-v tables, tug scaling and xenon limits: cite it, do not repeat it. This file adds what it lacked: Mercury and Venus as origins, gravity-assist routing, and the network as a whole.

Checklist (cover each, or list the gap under Open threads with the reason):
1. Orbital data and a synodic-period and window table for Mercury, Venus, Earth, Mars and Ceres (JPL constants, shown arithmetic); transfer times; how window spacing bunches cargo for each pair.
2. Gravity-assist routing among the inner bodies: Mercury to Venus to Earth and the reverse (BepiColombo, MESSENGER and the trajectory papers by Langevin, Yen and others); published studies of Mercury sample return or cargo return with delta-v and trip times; Venus as a hub (Venus-flyby cyclers, Earth-Venus cyclers); cost in delta-v and time with flybys versus direct. Primary sources only for numbers.
3. Propulsion performance versus distance from the Sun: solar-electric thrust and power scaling (from flown data, including BepiColombo's electric propulsion module at 0.3 to 0.5 AU), solar sails near the Sun ("sundiver" and perihelion-dive studies) with published acceleration numbers and lightness numbers, and what a tug or sail convoy from Mercury orbit to Earth or Venus orbit would take, by sourced rates.
4. Launch from airless, low-gravity bodies: a mass driver or other launcher on Mercury aimed to reach Venus, Earth or Mars transfer orbits: derive the needed hyperbolic excess speed and the best launch direction relative to Mercury's orbital velocity from sourced constants; the published lunar mass-driver and rotating-tether designs as anchors; what scales and what does not at Mercury's gravity.
5. Capture and delivery at the destination: aerocapture at Venus (dense atmosphere) versus Earth versus Mars, orbit capture energy, catchers and tether catchers for mass-driver cargo (cite SP-413 and the trucking file), the destination processing node.
6. Fleet and infrastructure sizes for stated flows: 1 kt, 100 kt and 1 Mt per year of cargo from Mercury orbit to Earth orbit, by (a) solar-electric tugs (note that sunlight at Mercury is 6.7 times Earth's), (b) a mass driver plus catcher, (c) sail convoys: tugs or sails needed, power, propellant or reaction mass, and number of round trips. Use sourced rates and show the arithmetic. Do the same for Venus-cloud cargo to Earth or Mars orbit if the Venus ascent figures in the trucking file allow.
7. Communications and navigation across the inner system: Deep Space Network capacity and constraints, solar-conjunction outage durations for each planet pair (derive from orbital data or take from mission pages), light-time table, relay constellations, the autonomy needed.
8. Wireless power transfer as part of the network: demonstrated efficiency, distance and aperture of laser and microwave power beaming; derive the aperture sizes diffraction requires at 0.3 to 1 AU; published concepts for space solar power exported from Mercury or other inner sites.
9. Propellant and consumables supply for the network: where water, carbon-dioxide-derived propellant or hydrogen exists at each node (Mercury polar ice, Venus atmosphere, lunar ice, near-Earth and carbonaceous asteroids, Mars) with sourced inventories, and the propellant budget implied by item 6's flows.
10. Space weather along the network: solar energetic particle warning times and doses at 0.3 to 1 AU, and what they imply for crewed or machine-tended traffic.
11. Reference-class evidence for how fast an operation of this kind could scale or fail: cite industrial_ramp_timelines.md rather than repeating; add only a point about supply-chain length or propellant logistics if you find a primary source.

You may read, read-only: space_trucking_and_transport_infrastructure.md, cyclers_and_large_slow_vehicles.md, industrial_ramp_timelines.md, starlifting_synthesis.md, belt_jupiter_saturn_and_deep_transit.md, mars_venus_and_transfer.md, moon_lagrange_and_comparables.md. Final chat reply at most 120 words.
