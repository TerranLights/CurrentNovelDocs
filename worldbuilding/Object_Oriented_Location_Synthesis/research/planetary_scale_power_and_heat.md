# Planetary-scale power and heat: collecting the energy and rejecting the waste heat for harvesting a whole planet

*Research file, OOLSD library, eighth tranche, section 4. Started 2026-10-11 (one run interrupted after row 4; resumed
the same night from the log). Physics and engineering only; no story, timeline or setting assumed.*

## 1. Scope

The power that taking apart Mercury, stripping Venus's atmosphere, or taking apart solid Venus would require, and the
heat it would make: solar collectors and mirrors near 0.3 to 0.73 AU, the conversion chain from sunlight to launched mass,
radiators, planet-scale thermal limits (swarm and planet temperatures, waste-heat literature), power transmission and
night storage, the 31-, 100- and 1,000-year scale table, and whether Mercury or Venus can supply the collectors.

**Evidence marks used below:** DEMONSTRATED (flown or built), ENGINEERING-STUDIED (a quantitative design or test-article
study), SPECULATIVE (thought experiment or concept without a design), DERIVED (my arithmetic from sourced inputs, shown in
section 5). Sibling keys: **[ME]** `mercury_as_industrial_site.md`, **[NW]** `inner_system_logistics_network.md`, **[PR]**
`space_processing_and_fabrication.md`, **[LG]** `lagrange_thermal_environment.md`, **[WH]** `waste_heat_utilization.md`,
**[SYN]** `starlifting_synthesis.md`, **[IMS]** `inner_system_mining_synthesis.md`.

## 2. SEARCH LOG

*(Dates 2026-10-11, the resumed run running past midnight into 2026-10-12. Marks: useful / thin / dead; dead ends say whether
they died at the query or at the sources.)*

| # | Search string (verbatim) or page opened | Result | Notes |
|---|---|---|---|
| 0a | Opened sibling files (read-only, allowed): `starlifting_synthesis.md`, `inner_system_mining_synthesis.md`, `mercury_as_industrial_site.md` (F2-F12), `inner_system_logistics_network.md` (F3, F4, F8), `space_processing_and_fabrication.md` (3-6), `lagrange_thermal_environment.md` (3D-3G, 5), `waste_heat_utilization.md` (3A-3C) | useful | Cited, not re-derived |
| 1 | Opened https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html | useful | L = 382.8 x 10^24 J/s; T_eff 5,772 K; R 695,700 km; updated 9 May 2024 |
| 2 | Opened https://nssdc.gsfc.nasa.gov/planetary/factsheet/venusfact.html | useful | M 4.8673e24 kg, R 6,051.8 km, v_esc 10.36 km/s, a 108.210e6 km, 2,601.3 W/m^2, Bond albedo 0.77, atm ~4.8e20 kg; updated 11 Jan 2024 |
| 3 | Opened https://nssdc.gsfc.nasa.gov/planetary/factsheet/mercuryfact.html | useful | M 0.33010e24 kg, R 2,439.7 km, a 57.909e6 km, 9,082.7 W/m^2, Bond albedo 0.068; updated 11 Jan 2024 |
| 4 | (prior run, not logged at the time) downloaded to scratch `dl/sla.pdf`: Woods, Kalla, Gonzalez, Ribelin (ITN Energy Systems), "Wide-bandgap CIAS thin-film photovoltaics with transparent back contacts ..." (URL not recorded by the interrupted run) | thin | Lead only: thin-film arrays may exceed 1 kW/kg at PV+substrate level; CIS best 19.2% AM1.5 on glass. Not used for a number (URL and date unrecorded) |
| 5 | Resumed 2026-10-11 ~23:40. Search: `thin-film solar array specific power W/kg areal density kg/m2 space flexible ROSA IMM` | useful (leads) | NTRS 20030000595, DSS ROSA (>500 W/kg BOL with IMM claimed), 0.25-1.0 kg/m^2 ultralight arrays. Snippets only; numbers to be confirmed in primaries |
| 6 | Search: `NASA State of the Art small spacecraft power chapter solar array specific power W/kg table 2024` | thin | "up to 165 W/kg" (aggregator summary of SoA 2024); LISA-T >250 W/kg. Leads |
| 7 | Search: `Armstrong Sandberg "Eternity in six hours" Dyson swarm collector mass per square meter thickness efficiency` | useful (lead) | Pointed to 3.92 kg/m^2 swarm figure; confirmed in the paper (row 8) |
| 8 | Download: fhi.ox.ac.uk `intergalactic-spreading.pdf` (direct) | dead at the source | HTTP 000 (no response) |
| 9 | Download: Internet Archive copy of the same (web.archive.org/web/2014/.../intergalactic-spreading.pdf), preprint dated 12 Mar 2013 | useful | Sec. 4.1-4.3: swarm at Mercury's semimajor axis, area 4.21e22 m^2; 50% of Mercury to reflectors = 3.92 kg/m^2 (0.5 mm of iron), "most likely" a 0.001 mm film on struts; captor efficiency 1/3 "by the time the solar energy is concentrated, transformed and beamed back"; 1/10 of energy to launch; 1 km^2 seed; 5-yr lag; 31 yr 85 d; launch system efficiency "at least 50%"; notes "worries as to how the core could be cooled". **No radiator, waste-heat or thermal analysis in the model** |
| 10 | Search: `liquid droplet radiator specific mass kg/kW compared heat pipe radiator NASA study` | useful (leads) | NTRS 19820007493, 19850015934, 19870010920 opened as PDFs (rows 13-15) |
| 11 | Search: `high temperature space radiator carbon-carbon 1000 K areal mass kg/m2 nuclear electric propulsion Prometheus` | useful | NTRS 20130001608 opened (row 12); snippet "C-C heat pipe radiator 1.45 kg/m^2" not found in an opened page, not used |
| 12 | Opened PDF: Hyers, Tomboulian (UMass), Craven, Rogers (NASA MSFC), "Lightweight, High-Temperature Radiator for Space Propulsion", NTRS 20130001608 (2012 presentation, doc no. 12-055) | useful | Radiator "40% or more of the power system mass" for high-power NEP; NASA areal-density goal for NEP **2-4 kg/m^2**; aim to reject at "up to 1000 K and higher"; only raising temperature improves rejection per area since coatings are near-ideal |
| 13 | Opened PDF: Diem-Kirsop (NASA Lewis), "Advanced Radiator Concepts", SWE National Convention, 27-30 Jun 1985, NTRS 19850015934 | useful | Radiator 30-50% of power-system mass at Space Station scale; liquid belt radiator for 37.5 kWe Brayton was 40% of fin-and-tube mass; system studies 300-650 K: **LBR 0.6 to 1.3 kg/m^2, 20-50% of heat-pipe radiators** |
| 14 | Opened PDF: Astro Research Corp. (K. Knapp), "Lightweight moving radiators for heat rejection in space", final report dated 10 Nov (year OCR-garbled; NTRS accession N81-), NTRS 19820007493 | useful | **Boeing SPS thermal-engine radiator "slightly less than 5 kg/m^2" of radiating surface**, "probably the lightest mass achievable for a very large system using this type of technology"; belt 2.5 kg/m^2; particle radiator <1.5 kg/m^2 (preliminary); droplet streams an order of magnitude lighter if parameters hold; small orifices make pumping power **nearly 10% of the heat rejected**, "not acceptable" |
| 15 | Opened PDF: K. A. White III (NASA Lewis), "Liquid Droplet Radiator Development Status", NASA TM-89852 (1987), NTRS 19870010920 | useful | Uses heat-pipe technology at **5 kg/m^2 and emissivity 0.85** as the comparison baseline; evaporation and droplet-loss issues (OCR poor; qualitative use only) |
| 16 | Search: `Wright Mullan Sigurdsson Povich 2014 Ĝ infrared search extraterrestrial civilizations large energy supplies waste heat framework` | useful | arXiv 1408.1134 opened (row 17) |
| 17 | Opened PDF: Wright, Griffith, Sigurdsson, Povich, Mullan, "The Ĝ infrared search for extraterrestrial civilizations with large energy supplies. II. Framework, strategy, and first result", ApJ (accepted 23 Jun 2014), arXiv 1408.1134v1 | useful | AGENT energy balance alpha+epsilon = gamma+nu; Carnot ceiling eta = 1 - T_waste/T (Slysh 1985); 1 AU classical sphere T_waste ~250 K; Eq. 11 L alpha = gamma sigma T^4 A; going 290 K -> 29 K raises area 10^4; "reasonable" T_waste 150-600 K (factor 250 in area); humanity 1.7e7 MW (Kleidon 2010) |
| 18 | Search: `Badescu "On the radius of Dyson's sphere" Acta Astronautica optimum radius temperature` | thin | Badescu 1995 (Acta Astronautica 36:135) identified as a citation in other papers; the paper itself was not found open-access (dead at the sources for the original); led to arXiv 2006.16734, 2309.06564, 2110.13887 |
| 19 | Search: `Dyson 1960 Science "Search for Artificial Stellar Sources of Infrared Radiation" 300 K shell mass 2x10^27 g thickness` | thin | Popular pages only (Scientific American blog, magazines); figures quoted there (shell 2-3 m thick, 200 g/cm^2 from Jupiter's mass at 1 AU) **not used**: Dyson 1960 itself not opened (paywalled at Science); dead at the sources for the primary |
| 20 | Search: `Chaisson 2008 Eos "Long-term global heating from energy usage" waste heat growth rate 3 degrees` | useful | Harvard DASH copy opened (row 24); arXiv 2409.06737 opened (row 23) |
| 21 | Opened PDF: J. T. Wright, "Application of the Thermodynamics of Radiation to Dyson Spheres as Work Extractors and Computational Engines, and their Observational Consequences", accepted to AAS Journals, arXiv 2309.06564 (2023) | useful | Landsberg limit reduces to Carnot (eta = 1 - T/T*); Petela radiation-limit formula; swarm optical depth tau = A/(4 pi R^2), captured fraction (1 - e^-tau); "very little gain per gram ... once ~10% of the starlight is being used"; optimal placement of limited mass is as close to the star as possible; complete swarms have optical depths of a few; Landauer cost kT ln 2 per bit |
| 22 | Opened PDF: Huston and Wright, "Evolutionary and Observational Consequences of Dyson Sphere Feedback", arXiv 2110.13887v1 (26 Oct 2021) | useful | Light returned to the star (reflection, re-emission) makes stars expand and cool; for Sun-like stars with radiative interiors effect small; significant only for very hot spheres (much above ~300 K) or high specular reflectivity; monolithic shell "could not be built stably" (Maddox 1960); swarm is the preferred model (Dyson 1966) |
| 23 | Opened PDF: Balbi and Lingam, "Waste Heat and Habitability: Constraints from Technological Energy Consumption", arXiv 2409.06737v2 (24 Jan 2025) | useful | With ~1% per year growth in energy use, waste heat makes an Earth-like planet uninhabitable on timescales of order <= 1,000 years from the start of exponential growth; world use 1.8 x 10^5 TWh in 2022 |
| 24 | Opened PDF: E. J. Chaisson, "Long-Term Global Heating from Energy Usage", Eos Trans. AGU 89(28):253 (2008), doi 10.1029/2008EO280001, Harvard DASH | useful | Absorbed insolation ~120,000 TW; civilization ~18 TW; surface rises ~3 C when about 4% more than the Sun's dose (4,800 TW) is produced on Earth; at 2%/yr growth that is ~8 doublings, ~280 years. A planet-scale waste-heat limit by simple radiative balance |
| 25 | Opened PDF: J. T. Wright, "Dyson Spheres", Serbian Astronomical Journal (2020), arXiv 2006.16734v3 (7 Oct 2020) | useful | Eq. 64: A = 4 pi R*^2 (1 - eta)^-3; nominal 1 au sphere T_e = 160 K, eta_max 97%; each extra "nine" of efficiency needs 10^3 more radiating material; a 16 K sphere would need ~1 solar mass or be millimeters thick; rigid shells unstable, swarms preferred; Dyson (1966): planets "can (in principle) be deconstructed"; mechanics of deconstruction left to Criswell 1986 |
| 26 | Search: `NASA OTPS Space-Based Solar Power 2024 report RD1 RD2 mass metric tons 2 GW innovative heliostat swarm` | useful | OTPS report PDF opened (row 27) |
| 27 | Opened PDF: NASA Office of Technology, Policy, and Strategy, "Space-Based Solar Power" (Rodgers et al.), report dated 8 Jan 2024 (nasa.gov/wp-content/uploads/2024/01/otps-sbsp-report-final-tagged-approved-1-8-24-tagged-v2.pdf) | useful | RD1 (heliostat swarm, 2-3 suns on PV) 11.473 km^2 of panel, 5,852,000 kg in space, 1,463,000 modules of 4.00 kg; RD2 (planar) 19 km^2, 10,000,000 kg, 2,000,000 modules of 5.00 kg; cells 35%; 2.03 / 2.02 GW delivered to grid; capacity factor 0.997 / 0.6; thermal subsystem 0.40-0.50 kg per module; hardware life 10 yr. **Internal conflict:** text on p. ~30 says "1000 metric tons (MT) versus 585 MT" against the table's 5.9 Mkg and 10 Mkg (see Conflicts) |
| 28 | Search: `Parker Solar Probe solar array cooling system water radiator area temperature perihelion power watts` | thin | Trade press only (Electronic Specifier etc.): 6,000 W cooling capacity, ~5 L water, four Ti/Al radiators, arrays <= 160 C. Leads only |
| 29 | Search: `Solar Orbiter solar array 0.28 AU temperature tilt high temperature solar cells design power` | thin | ESA pages: six 2.1 x 1.2 m panels, rotated for temperature, inherited from BepiColombo MPO; up to 13 solar constants on the shield, ~500 C at the shield front. No cell temperature or power figure; not used beyond the tilt practice |
| 30 | Search: `Parker Solar Probe solar array thermal design cooling system paper IEEE PVSC "solar array" platen water perihelion 9.86 solar radii` | thin | Leads to IEEE Spectrum (row 33) and SSL Berkeley page |
| 31 | WebFetch: https://www.ssl.berkeley.edu/parker-solar-probe-cool-power/ | dead at the source | HTTP 404 |
| 32 | Search: `Mehoke Parker Solar Probe solar array cooling system design radiator 6 kW APL paper` | thin | ICES paper "Parker Solar Probe Solar Array Cooling System In-Orbit Performance Review" (TTU repository) found; ~5,500 W heat load (snippet) |
| 33 | WebFetch and curl: TTU repository item f3feca10-... (ICES PSP SACS in-orbit review) | dead at the source | HTTP 403 both ways |
| 34 | WebFetch: IEEE Spectrum, Driesman, Ercol, Gaddy, Gerger (JHU APL engineers), "How the Parker Solar Probe Survives Close Encounters With the Sun", 25 Apr 2019 | useful | Arrays: "as many as 13 watts of heating in the panels for every watt of electrical power generated"; ~5,900 W heat at closest approach; four radiators "about one meter square"; cells held to 120 C max; flux ~650 kW/m^2 ("almost 500 times" Earth's) on the shield. Written by the mission's engineers in a magazine: treated as secondary with an expert byline |
| 35 | WebFetch: https://ntrs.nasa.gov/citations/20230002489 | thin | Landis (NASA GRC), "Space Photovoltaics for Extreme High-Temperature Missions", book chapter, 19 Jan 2023; abstract has no numbers; full text not opened |
| 36 | Search: `concentrator multijunction cell efficiency record suns NREL 47.1% 143 suns temperature coefficient high irradiance` | useful (lead) | Geisz et al., Nature Energy (2020): six-junction 47.1% at 143 suns, 39.2% at one sun (trade press summaries) |
| 37 | WebFetch: nrel.gov press release on the six-junction record | dead at the source | DNS failure (ENOTFOUND) |
| 38 | Search: `space solar cell efficiency versus temperature and intensity multijunction "high intensity high temperature" HIHT BepiColombo cells qualification 10 suns` | thin | INTA record opened (row 39) |
| 39 | WebFetch: INTA repository, Martinez de Olcoz et al., "Electrical performance results of multi-junction space solar cells under high temperature high intensity environmental conditions", ESPC 2023 (2 Oct 2023) | thin | Abstract only (PDF restricted): EnVision cells expected at 2 suns and 130-140 C; temperature coefficients measured 25-100 C. No coefficient values available |
| 40 | Search: `nasa.gov smallsat-institute sst-soa power 2024 pdf "solar arrays" "W/kg" table flexible` | thin | NTRS 20170009097 (LISA-T) opened (row 44); SoA 2024 power chapter PDF itself not surfaced (dead at the query) |
| 41 | Search: `iROSA ISS roll-out solar array mass kW specific power Redwire 20 kW` | thin | Press releases: iROSA wing 28 kW BOL, XTJ cells, eight wings >160 kW; **no mass published** in what surfaced (dead at the sources for mass) |
| 42 | Search: `SPS-ALPHA Mankins mass specific power kg/kW system mass 2 GW thin film reflectors areal density` (search tool ran four sub-queries) | useful | NSS copy of the NIAC Phase 1 report opened (row 43); other returns popular |
| 43 | Opened PDF: J. C. Mankins, "SPS-ALPHA: The First Practical Solar Power Satellite via Arbitrarily Large Phased Array", NASA NIAC Phase 1 Final Report, 15 Sep 2012 (nss.org copy) | useful | DRM_5 (2 GW to Earth, GEO): **34,813,882 kg** platform hardware; primary array 32,590,615 kg; **solar reflector assembly only 770,595 kg (2.2%)**; DRM_4 (500 MW): 11,795,271 kg; reflectors "aluminum on Kapton"; raising concentration 3:1 -> 5:1 "would reduce the SPS-ALPHA platform mass by almost 15,000 tons" if devices tolerate the higher temperature; 1979 reference SPS "50,000 mT-100,000 mT" |
| 44 | Download: Aerospace Corp. Space Power Workshop 2023 LaPointe ROSA presentation (spw.aerospace.org) | dead at the source | HTTP 404 (an HTML error page came back; not used) |
| 45 | Opened PDF: NTRS 20170009097 (LISA-T, NASA MSFC) | thin | Small-satellite array table: LISA-T >250 W/kg pointed, >125 W/kg omnidirectional (CubeSat class; not used as a large-array figure) |
| 46 | Search: `MegaFlex ROSA 30-50 kW solar array specific power W/kg NASA solar electric propulsion technology demonstration mission results` | useful (lead) | NTRS 20140000360 opened (row 49); Mega-ROSA ">200 to 400 W/kg BOL at the wing level" (snippet, DSS claim, not used as a number) |
| 47 | Search: `IKAROS thin-film solar cells sail mass per area 7.5 micron polyimide g/m2 measured power` | useful (lead) | JAXA press kit opened (row 48); Wikipedia's "about 10 g/m^2" and "360 W" not used |
| 48 | Opened PDF: JAXA, IKAROS press kit (global.jaxa.jp/countdown/f17/pdf/presskit_ikaros_e.pdf, 2010) | useful | Membrane 7.5 µm polyimide with deposited aluminum, 14 m square (196 m^2); membrane mass 15 kg including 2 kg of tip masses; thin-film cells are amorphous silicon, 25 µm thick; launch mass 310 kg (DEMONSTRATED, 2010) |
| 49 | Opened PDF: Pappa, Rose, Mann, Warren (NASA LaRC), Mikulas (NIA), Kerslake, Kraft (NASA GRC), "Solar Array Structures for 300 kW-Class Spacecraft", Space Power Workshop, 24 Apr 2013, NTRS 20140000360 | useful | 300 kW-class goals: 450 kW BOL / 300 kW EOL "assuming 33% worst-case degradation"; **>120 W/kg BOL (>100 W/kg EOL) including drive**; blanket <1 kg/m^2; ~1,500 m^2 for 300 kW; MegaFlex and Mega-ROSA 30-50 kW designs (ENGINEERING-STUDIED; ground-tested wings) |
| 50 | Search: `MESSENGER solar array degradation in Mercury orbit power loss percent per year cells temperature` | thin | No degradation rate surfaced (dead at the sources for a rate); Holtzman et al. opened (row 51) |
| 51 | Opened PDF: Holtzman, Calloway, Jaskulek, Gallagher, "MESSENGER Operational Influences and Environment", Johns Hopkins APL Technical Digest 34(1), 2017 | useful | Arrays 2:1 OSR-to-cell ratio; off-pointed by an amount that rose with solar heating; **planetary IR heating near Mercury on both sides of the arrays**; pre-cooled by extra off-pointing ~1 h before orbital peak heating; front phased-array antenna reached 168 C. No degradation rate given |
| 52 | Search: `mass driver pulsed power supply efficiency capacitor energy storage coilgun overall efficiency electrical to kinetic measured` | thin | Hobbyist and student coilgun pages (0.2-5% efficiency) **not used** (not representative of engineered launchers); DTIC ADA192102 and ADA143778 surfaced, not opened (Open threads) |
| 53 | Search: `NASA SP-428 mass driver III-3 efficiency 96.4% power conditioning losses heat rejection radiators lunar mass driver` | useful | NSS transcription of SP-428 III-3 opened (rows 54, 55); summary claim "1,000 t driver, 600,000 t/yr, 92%" appeared only in a search summary (not used) |
| 54 | WebFetch: NSS transcription of NASA SP-428 (1979), Part III-3, "Mass Drivers III: Engineering" (Arnold, Bowen, Cohen, Kaplan, Fine, M. Kolm, H. Kolm, Newman, O'Neill, Snow), nss.org/settlement/nasa/spaceres/III-3.html | useful | Lunar launcher: 2,400 m/s, 10,000 m/s^2, 10.5 kg payload, 4 Hz, 488 m; **efficiency 96.4%; total power 1.25 x 10^8 W; waste power 4.46 x 10^6 W**; electric mass 2.09 x 10^6 kg, total 3.13 x 10^6 kg; raising system temperature 300 -> 400 K cuts "power plant and radiator mass ... by 31.8 percent", limited by SCR surge rating |
| 55 | WebFetch (second pass, same page): what the 96.4% includes | useful | **The 96.4% counts only i^2R losses in feeders and drive windings**; it excludes the power plant, power conditioning and switching; radiator specific mass assumed **0.020 kg/W (20 kg per kW rejected) at 300 K**, scaling with 1/T^4 |
| 56 | Search: `space power transmission cable mass per kW per km high voltage DC in space aluminum conductor long distance spacecraft power distribution study` | useful (leads) | NTRS 19870012570 and 19840012571 opened (rows 57, 58); UCSB 3 km line (5.3 kg/km) and terrestrial 150 kV line (4 t/km) appeared only in summaries, not used |
| 57 | Opened PDF: Switzer and Bents (NASA Lewis), "Coaxial Tube Array Space Transmission Line Characterization", NASA TM-89864 (1987), NTRS 19870012570 | useful | 300 kWe, **1.5% power loss**, reactor-to-platform 1-10 km, vacuum-insulated 20 kV/cm or SF6 50 kV/cm; Table I: 10 km line **12,783 kg (20 kV/cm, 8.4 kV)** or **6,530 kg (50 kV/cm, 13.3 kV)**; "Longer lines are heavier per unit length"; meteoroid bumper included (ENGINEERING-STUDIED) |
| 58 | Opened PDF: Jefferies and Renz (NASA Lewis), "Parametric Analysis of Hollow Conductor Parallel and Coaxial Transmission Lines for High Frequency Space Power Distribution", NASA TM-83601 (Mar 1984), NTRS 19840012571 | thin | Up to 1,000 V, 10-30 kHz; spacecraft-scale distribution; not used for numbers (wrong scale) |
| 59 | WebFetch: NIST CODATA, Stefan-Boltzmann constant, physics.nist.gov/cgi-bin/cuu/Value?sigma | useful | 5.670 374 419 x 10^-8 W m^-2 K^-4, exact (CODATA 2022) |
| 60 | Search: `electrical resistivity of aluminum 20 C 2.65e-8 ohm m NIST or handbook table pure metals resistivity temperature` | useful (lead) | HyperPhysics opened (row 61); BYU cleanroom 2.82e-8 noted as a conflict (row 61 notes) |
| 61 | WebFetch: HyperPhysics (Georgia State Univ.), "Resistivity and Temperature Coefficient at 20 C" (citing Giancoli, Physics, 4th ed., 1995) | useful | Al 2.65 x 10^-8 ohm m, Cu 1.68 x 10^-8 ohm m (textbook-grade; secondary) |
| 62 | Search: `thin film silicon solar cells from lunar regolith vacuum deposition Ignatiev Freundlich "Lunar Ark" solar cell paving robot mass per watt` | useful | NTRS 19980003482 opened (row 63); a ~200 kg crawler, 5-10% cells, "1 MW in several years" in an IAC-05 abstract summary (not opened; Open threads) |
| 63 | Opened PDF: Freundlich and Ignatiev (Univ. Houston), "Solar Cells for Lunar Application", Final Technical Report, NASA Grant NAG 9-806, Sep 1997, NTRS 19980003482 | useful | Silicon extracted from lunar regolith simulant evaporated in vacuum (10^-7 torr) onto glass, crystal and 25 µm Al foil; films ~1.1 eV bandgap, unintentionally p-type; cells need ">10 microns" of Si; growth rates "exceeding 5-10 microns per hour"; evaporating dopants such as As was a limitation (DEMONSTRATED at lab-film scale; no cell made from lunar Si reported) |
| 64 | Search: `density of aluminum 2.70 g/cm3 silicon 2.33 g/cm3 iron 7.87 g/cm3 table elements density handbook NIST` | useful (lead) | KnowledgeDoor pages opened (rows 65, 66) |
| 65 | WebFetch: KnowledgeDoor Elements Handbook, density (Ac-Ho) | useful | Al solid 25 C: 2.700 g/cm^3 |
| 66 | WebFetch: KnowledgeDoor Elements Handbook, density part 2 | useful | Fe solid 25 C: 7.870 g/cm^3 (Armstrong and Sandberg use 7,874 kg/m^3); silicon not on either page |
| 67 | WebFetch: Ioffe Institute semiconductor database, Si basic parameters (https; then http via curl) | useful | https failed (certificate); http copy gave Si density 2.329 g/cm^3 |
| 68 | (calc) Ran prior-run script `calc1.py` and new `as_reimpl.py` in the scratch folder | useful | Outputs pasted under Derived figures D1, D9 |
| 69 | Search: `specific heat capacity of basalt or lunar regolith J/kg K as function of temperature measured Hemingway Robie lunar samples` | useful | USGS record opened (row 70); the Hemingway 1973 fit appeared only in a preprint summary (not used) |
| 70 | WebFetch: USGS Publications Warehouse 70010431: Robie, Hemingway, Wilson, "Specific heats of lunar surface materials from 90 to 350 degrees Kelvin", Science (1970) | useful | Apollo 11 basalt and soil: about 0.06 cal/g/K at 90 K to **about 0.2 cal/g/K at 350 K** (0.84 kJ/kg/K with 4.184 J/cal) |
| 71 | Search: `high temperature superconducting power transmission in space cable cryogenic shade radiator passive cooling 77 K study` | useful (lead) | Glasgow eprint opened (row 72); patents not used |
| 72 | WebFetch: Univ. Glasgow eprint 324980: Sadeghi, Morandi, Yazdani-Asrami, "Feasibility of high temperature superconducting cables for energy harvesting in large space-based solar power satellite applications", Energy Reports 11:4523-4536 (2024) | useful (abstract) | 2 MW bipolar DC HTS cable studied at 20-77 K; cable plus cooling efficiency **99.70% (20 K) to 99.97% (77 K)**; cost and weight rise with operating temperature (ENGINEERING-STUDIED; full text not read: Open threads) |
| 73 | Search: `Helios probe solar cells 0.29 AU solar array temperature degradation power output 1974 1976 NASA` | useful (leads) | Wikipedia's "50% mirrors, below 165 C, 240 W minimum" not used; NTRS 19760063081 and the Neubauer talk opened (rows 76, 77); arXiv 2608.11113 surfaced (title on high-temperature PV for solar Oberth maneuvers), not opened (Open threads) |
| 74 | Search: `Venus Express solar array design optical solar reflectors cell temperature 0.72 AU power` | useful (lead) | ESA engineering page opened (row 75); snippet figures (-167 to +158 C qualification, 821/1,468 W, 3.5 suns equivalent) not found on the opened page, not used |
| 75 | WebFetch: ESA, Venus Express "Engineering" page, sci.esa.int/web/venus-express/-/33877-engineering (last updated 1 Sep 2019) | useful | Two wings, 5.7 m^2 total, triple-junction GaAs cells; OSR between cells on the front and on the rear; sized for >= 800 W near Earth and >= 1,100 W in Venus orbit (DEMONSTRATED, 2005-2014) |
| 76 | WebFetch: NTRS 19760063081: Ousley (GSFC), Kutzer, Panitz (DFVLR), "The Helios program and the sun", 1 Oct 1976 | thin | Abstract only: Helios A and B reached 0.31 and 0.29 AU; no array numbers |
| 77 | Opened PDF: F. M. Neubauer, "The Helios Mission", Helios Mini-Workshop, Cologne, Jun 2016 (helios-data.ssl.berkeley.edu) | useful | Cylinder-and-cone body covered with cells; insolation controlled by second-surface mirrors; **insulation deteriorated so maximum temperatures rose from perihelion to perihelion; cell deterioration reduced power over time** (heaters switched off, -80 C at aphelion) (DEMONSTRATED, qualitative) |
| 78 | Search (extended mode): `electromagnetic launcher pulsed power system wall-plug efficiency rotating machine compulsator capacitor bank charging efficiency percent study` | dead at the sources | Compulsator and EM-gun papers (UT-CEM, IEEE via ResearchGate) surfaced with no efficiency numbers in what was returned; no sourced wall-plug efficiency for a launcher's pulsed-power chain (Open threads) |
| 79 | Search: `megawatt class nuclear electric propulsion radiator specific mass kg/m2 temperature 2020s NASA study Brayton heat rejection area` | useful | NTRS 20220002034 opened (row 80); "3.53 vs 6.43 kg/kWe" Brayton vs Rankine appeared only in a summary (INL item not opened; not used) |
| 80 | Opened PDF: Machemer, Duchek, Harnack, Grella, Nikitaev, Smith (Analytical Mechanics Associates), "Mass Modeling of NEP Power Conversion Concepts for Human Mars Exploration", NETS 2022 (file dated 25 Mar 2022), NTRS 20220002034 | useful | Assumed **PMAD radiator 400 K at 7 kg/m^2; parasitic-load radiator 850 K at 10 kg/m^2**; radiator truss 4,000 kg for 2,500 m^2 = 1.6 kg/m^2 (ENGINEERING-STUDIED, model) |
| 81 | (calc) `calc2.py`, `calc3.py` run; outputs saved as `calc2_out.txt`, `calc3_out.txt` in the scratch folder | useful | Pasted under section 5 |

## 3. Findings

**The answer in brief (each line is traced in the tables and in section 5).**

1. **Collecting the power is not the hard part.** Taking Mercury apart in 31 years needs, on average, 1.8 x 10^21 W of
   kinetic power at the launchers (4.8 x 10^-6 of the Sun's output); with every sourced loss in the chain the sunlight needed is
   1.6 x 10^-5 to 2.8 x 10^-4 of the Sun's output, and the collectors weigh 10^17 to 5 x 10^19 kg, 10^-6 to 10^-4 of Mercury's mass
   (DERIVED, D5). On mass and area alone, a 31-year Mercury is not ruled out.
2. **Rejecting the heat at the planet is the binding constraint at every timescale studied, 31, 100 and 1,000 years.** Even
   with the best sourced launcher figure (96.4%, which counts only coil losses), the launchers' waste heat spread over all of
   Mercury's surface is 9.1 x 10^5 W/m^2 (31 yr), 2.8 x 10^5 (100 yr) and 2.8 x 10^4 W/m^2 (1,000 yr), against 9,083 W/m^2 of
   sunlight. To radiate it the whole planetary surface would have to sit at about 2,000, 1,500 and 840 K. If the power arrives
   by microwave beam, the receivers alone add about 30% of the delivered power as heat, giving 3,800, 2,800 and 1,600 K. Radiators
   to carry that heat at 500 K would need 9 to 3,900 times Mercury's surface area (DERIVED, D8, calc 3). **No source found
   addresses this.**
3. **The literature's 31-year figure (Armstrong and Sandberg 2013) contains no heat analysis.** Its own assumptions put about
   10^23 to 10^24 W of delivered power near Mercury in the final years, nine-tenths of it spent there "breaking chemical bonds,
   reprocessing material, or just lost to inefficiency". Radiated from Mercury's surface that would be an 18,000 to 21,000 K
   surface (DERIVED, D9). The model therefore works only if processing and its heat are moved off the planet into the swarm,
   which the paper does not state.
4. **Venus's atmosphere is a smaller job on power** (2.6 x 10^19 W for 31 years, 8.2 x 10^17 W for 1,000), and its heat load
   per square meter of planet is about 430 times lower than Mercury's for the same timescale and chain (a 69 times smaller
   energy spread over 6.2 times more surface). **Solid Venus is about 88 times Mercury's binding energy** and needs
   4 x 10^-5 to 2.5 x 10^-2 of the Sun's output; its surface heat flux at 31 years is 1.3 x 10^7 to 3.5 x 10^8 W/m^2 (D5, D8).
5. **Processing costs more energy than lifting.** If every kilogram is turned into product at the sourced plant energies
   (58 to 536 MJ/kg), processing Mercury takes 11 to 99 times its binding energy (calc 3). Only throwing raw material keeps the
   energy near the binding energy.
6. **Near-Sun collectors are limited by their own temperature, not by sunlight.** A black panel two-sided at Mercury's mean
   distance sits at 541 K; flown arrays near Mercury cover two-thirds of their area with mirrors, tilt off the Sun, and still
   degrade (DEMONSTRATED). Mirrors are cheap in mass (SPS-ALPHA: reflectors 2.2% of the platform); conversion hardware is where
   the mass goes.
7. **Mercury can supply silicon, aluminum, magnesium, oxygen and carbon for collectors, but not the iron the literature
   assumes** (the iron is 420 to 470 km down), not the hydrogen and nitrogen for polymer films, and not the chips (cite [ME],
   [PR]).

### F1. Collector technology: areal mass, specific power, behavior near the Sun (checklist 1)

| Quantity | Value and units | Source (publisher, title, URL, date) | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Large flexible array goals, 300 kW class | >120 W/kg BOL (>100 W/kg EOL) including the array drive; blanket <1 kg/m^2; ~1,500 m^2 for 300 kW; 450 kW BOL / 300 kW EOL "assuming 33% worst-case degradation" (ENGINEERING-STUDIED; 30-50 kW wings ground-tested) | Pappa, Rose, Mann, Warren, Mikulas, Kerslake, Kraft (NASA LaRC/GRC, NIA), "Solar Array Structures for 300 kW-Class Spacecraft", Space Power Workshop, 24 Apr 2013, NTRS 20140000360 | Primary | Search summaries: Mega-ROSA ">200 to 400 W/kg" (DSS claim, not used); ROSA ">500 W/kg BOL with IMM" (claim, not used) | Medium-high (goals and designs, not flight data) |
| Space solar power study modules (OTPS 2024) | RD1 heliostat swarm: 11.473 km^2 of panel, 5,852,000 kg, i.e. **0.51 kg/m^2**; 938 W/kg of DC at the cells (35%, 2-3 suns), 347 W/kg delivered to the grid. RD2 planar: 19 km^2, 10,000,000 kg, **0.53 kg/m^2**, 909 W/kg DC, 202 W/kg delivered (calc 4). Module masses 4.00 and 5.00 kg, of which thermal 0.40 and 0.50 kg; hardware life 10 yr (ENGINEERING-STUDIED) | NASA OTPS (Rodgers et al.), "Space-Based Solar Power", 8 Jan 2024, nasa.gov/wp-content/uploads/2024/01/otps-sbsp-report-final-tagged-approved-1-8-24-tagged-v2.pdf, Tables in App. B | Primary | Internal conflict on total mass (Conflicts K1) | Medium (assumed module masses, "inferred from Mankins, Sasaki, Pellegrino") |
| SPS-ALPHA platform masses | DRM_5 (2 GW delivered, GEO): **34,813,882 kg**, 57 W/kg delivered; primary array 32,590,615 kg; **solar reflector assembly 770,595 kg (2.2% of the platform)**, reflectors "aluminum on Kapton". DRM_4 (500 MW): 11,795,271 kg, 42 W/kg. Concentration 3:1 -> 5:1 "would reduce the SPS-ALPHA platform mass by almost 15,000 tons" if devices tolerate the hotter array (ENGINEERING-STUDIED) | J. C. Mankins, "SPS-ALPHA: The First Practical Solar Power Satellite via Arbitrarily Large Phased Array", NASA NIAC Phase 1 Final Report, 15 Sep 2012 (nss.org copy), Tables 7-6, 7-7, Sec. 7.3.4 | Primary | 1978 DOE/NASA reference SPS 5 GW: 34-51 million kg ([PR] 6), i.e. 98-147 W/kg delivered (calc 4) | Medium (conceptual) |
| Thin film membrane with cells, flown | IKAROS: 7.5 µm polyimide with deposited aluminum, 14 m square (196 m^2); membrane 15 kg including 2 kg of tip masses, i.e. **66 g/m^2 including thin-film cells and devices** (calc 4); cells amorphous silicon 25 µm thick (DEMONSTRATED, 2010) | JAXA, IKAROS press kit (global.jaxa.jp/countdown/f17/pdf/presskit_ikaros_e.pdf), 2010 | Primary | Sail-only loading 5.9 g/m^2 for a studied Mercury sail; polyimide upper limit about 520 K ([NW] F3) | High |
| Reflectors in the planet-disassembly literature | Swarm at Mercury's semimajor axis, area 4.21 x 10^22 m^2; half of Mercury's mass as reflectors gives **3.92 kg/m^2** (0.5 mm of iron at 7,874 kg/m^3); "the most likely structure is a very thin film (of order 0.001 mm) supported by a network of more rigid struts"; captors overall 1/3 efficient "by the time the solar energy is concentrated, transformed and beamed back to Mercury" (SPECULATIVE) | Armstrong and Sandberg, "Eternity in six hours", preprint 12 Mar 2013 for Acta Astronautica 89 (2013) 1-13, Sec. 4.1-4.2 (Internet Archive copy of fhi.ox.ac.uk/wp-content/uploads/intergalactic-spreading.pdf) | Primary (peer-reviewed thought experiment) | [ME] F9 same figures via a sibling | High that the paper says it; low as engineering |
| Flown arrays inside 0.5 AU | MESSENGER: 2:1 optical-solar-reflector to cell ratio; arrays off-pointed more as heating rose; **planetary infrared heated the arrays near Mercury, on both sides**; pre-cooled by extra off-pointing ~1 h before peak (DEMONSTRATED) | Holtzman, Calloway, Jaskulek, Gallagher, "MESSENGER Operational Influences and Environment", Johns Hopkins APL Tech. Digest 34(1), 2017 | Primary | [ME] F6: 150 C set point, qualified to 275 C; BepiColombo about 230 C maximum, 20% power loss in one simulated month | High |
| Parker Solar Probe arrays | "As many as 13 watts of heating in the panels for every watt of electrical power generated"; ~5,900 W of heat at closest approach; four radiators "about one meter square"; cells held to 120 C maximum; water coolant (DEMONSTRATED, flight from 2018) | Driesman, Ercol, Gaddy, Gerger (JHU APL), "How the Parker Solar Probe Survives Close Encounters With the Sun", IEEE Spectrum, 25 Apr 2019 | Secondary (magazine article by the mission's engineers) | Trade press: 6,000 W cooling capacity, ~5 L water, array limit 150-160 C (Conflicts K3) | Medium |
| Venus-distance arrays | Venus Express: 5.7 m^2 of triple-junction GaAs with optical solar reflectors between cells and on the rear; sized for >= 1,100 W at Venus, i.e. 193 W per m^2 of array, 7.4% of the incident 2,601 W/m^2 (calc 4) (DEMONSTRATED 2005-2014) | ESA, Venus Express "Engineering", sci.esa.int/web/venus-express/-/33877-engineering (updated 1 Sep 2019) | Primary | EnVision cells expected at 2 suns and 130-140 C (Martinez de Olcoz et al., ESPC 2023, abstract) | High (figure is a sizing minimum) |
| Helios at 0.29-0.31 AU | Cells on cone mantles with second-surface mirrors; **insulation deteriorated so maximum temperatures rose perihelion to perihelion; cell deterioration lowered power over time** (DEMONSTRATED, 1974-1976 launches; qualitative) | F. M. Neubauer, "The Helios Mission", Helios Mini-Workshop, Cologne, Jun 2016 (helios-data.ssl.berkeley.edu) | Primary (mission scientist's talk) | Ousley, Kutzer, Panitz, NTRS 19760063081 (1976): 0.31 and 0.29 AU | Medium (no rate) |
| Cell physics at high temperature | Optimum bandgap rises with temperature; ~20% near 600 K, ~13% near 800 K (theory read from a plot); SiC cells with contacts for 600 C | [ME] F6 (Landis 2004) | Primary via sibling | Landis 2023 chapter "Space Photovoltaics for Extreme High-Temperature Missions" (NTRS 20230002489), abstract only | Low-medium |
| Concentration record (terrestrial lab) | Six-junction III-V cell 47.1% at 143 suns; 39.2% at one sun (Geisz et al., Nature Energy, 2020) | Trade press summaries of the NREL release (NREL page unreachable) | Secondary | none opened | Low (lead only; not a space or hot-cell figure) |
| Equilibrium temperature of collectors and mirrors | Mercury mean distance (9,083 W/m^2), two radiating faces: black panel 541 K; black panel exporting 30% as electricity 492 K; bare aluminum mirror (0.12/0.04) 700 K; aluminum front with a high-emittance (0.80) back 389 K; quartz OSR 284 K. Perihelion: black 607 K, bare aluminum 785 K. Venus distance: black 396 K, bare aluminum 512 K (DERIVED, D2) | D2 from NSSDC, [ME] F6 and [LG] 3F coating values | Derived | [ME] F11: black plate 710 K perihelion (insulated back) matches D2's 721 K within the coating difference | High (physics); coatings are BOL values |

### F2. Conversion chain: sunlight to the kinetic energy of launched mass (checklist 2)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Launcher "efficiency" in the lunar point design | **96.4%**; total power 1.25 x 10^8 W, waste 4.46 x 10^6 W (3.6%); counts only i^2R losses in feeders and drive windings, **not the power plant, conditioning or switching** (ENGINEERING-STUDIED, never built) | NASA SP-428 (1979), III-3 "Mass Drivers III: Engineering" (Arnold, Bowen, Cohen, Kaplan, Fine, M. Kolm, H. Kolm, Newman, O'Neill, Snow), NSS transcription nss.org/settlement/nasa/spaceres/III-3.html | Primary | [TR] F2 / [NW] F4 quote the same design | High that it is defined this way |
| Launch-system efficiency assumed in the disassembly paper | "at least 50%"; overall captor chain 1/3; 1/10 of delivered power to launching, the rest to processing and losses (SPECULATIVE) | Armstrong and Sandberg 2013, Sec. 4.2-4.3 | Primary (thought experiment) | none | Low as engineering |
| Space solar power chain (microwave) | Cells 0.35, DC-DC 0.90, DC-RF 0.70, antenna 0.90, atmosphere 0.98, beam collection 0.95, rectenna 0.78, ground DC-DC 0.90 | OTPS 2024, App. B | Primary | [NW] F8: product from space DC to ground DC 0.37, from sunlight 0.13 | Medium (assumed factors) |
| Laser chain components | Fiber laser ~38% wall-plug (">50%" demonstrated elsewhere); matched PV receiver ~50%; 800 W over 8.6 km demonstrated in air | [NW] F8 (Landis et al. 2025; DARPA 2025) | Primary via sibling | none | Medium-high |
| Cable transmission in space (study) | 300 kWe over 1-10 km at **1.5% power loss**; 10 km line 12,783 kg at 20 kV/cm (8.4 kV) or 6,530 kg at 50 kV/cm (13.3 kV), meteoroid bumper included; "Longer lines are heavier per unit length" (ENGINEERING-STUDIED) | Switzer and Bents (NASA Lewis), "Coaxial Tube Array Space Transmission Line Characterization", NASA TM-89864, 1987, NTRS 19870012570, Table I | Primary | D7: bare conductor for the same case 3,236 kg | Medium-high |
| Superconducting DC cable for space solar power | 2 MW bipolar cable; cable plus cooling **99.70% (20 K) to 99.97% (77 K)** efficient; mass and cost rise with operating temperature (ENGINEERING-STUDIED) | Sadeghi, Morandi, Yazdani-Asrami, Energy Reports 11:4523-4536 (2024), eprints.gla.ac.uk/324980 (abstract) | Primary (abstract only) | none | Medium |
| Pulsed-power conditioning between bus and coils | **No sourced efficiency found** (row 78) | — | — | — | Gap |
| End-to-end, sunlight to launched kinetic energy | **0.017 to 0.30** across hot cells (0.20) to 0.35 cells, cable or microwave or laser transmission, and 0.50 or 0.964 launch efficiency; 0.24 for MESSENGER-class cells, cable and 96.4% windings; Armstrong and Sandberg's overall assumption is 1/30 = 0.033 (DERIVED, D4) | D4 | Derived | none | Medium (the 0.964 omits conditioning, so the top of the range is optimistic) |

### F3. Waste heat and radiators (checklist 3)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Radiator share of power-system mass | 30-50% at Space Station power levels; "40% or more" for high-power nuclear-electric craft | Diem-Kirsop (NASA Lewis), "Advanced Radiator Concepts", SWE convention, Jun 1985, NTRS 19850015934; Hyers, Tomboulian, Craven, Rogers, "Lightweight, High-Temperature Radiator for Space Propulsion", 2012, NTRS 20130001608 | Primary | each other | Medium-high |
| Heat-pipe and pumped radiators, flown and designed | ISS 14.2 kg/m^2 of planform, ~96 kg/kW (flown) ([WH] 3B); reactor designs 5.24-12.76 kg/m^2, NASA target <= 3 ([LG] 3F); Boeing SPS thermal-engine radiator "slightly less than 5 kg/m^2", "probably the lightest mass achievable for a very large system using this type of technology"; heat-pipe baseline 5 kg/m^2 at emittance 0.85; NEP model 7 kg/m^2 at 400 K and 10 kg/m^2 at 850 K plus 1.6 kg/m^2 of truss; SP-413 aluminum refinery 613 t for 127.2 MW through 102,400 m^2 (6.0 kg/m^2, 4.8 kg/kW, calc 4) | [WH]; [LG]; Knapp (Astro Research), "Lightweight moving radiators for heat rejection in space", NTRS 19820007493; White, NASA TM-89852 (1987); Machemer et al., NETS 2022, NTRS 20220002034; [PR] 5 | Primary | each other | Medium-high |
| Lighter radiator concepts (studied, not flown) | Liquid belt radiator 0.6-1.3 kg/m^2 over 300-650 K, 20-50% of heat-pipe mass; droplet streams an order of magnitude lighter "if the parameters chosen here prove to be realistic"; small orifices make pumping power **nearly 10% of the heat rejected**, "not acceptable"; NASA NEP areal goal 2-4 kg/m^2 | Diem-Kirsop 1985; Knapp; Hyers et al. 2012 | Primary | none flown | Medium (studies) |
| Radiator mass assumed in the lunar launcher study | 0.020 kg per W rejected at 300 K, scaling with 1/T^4; raising the system from 300 to 400 K cuts power plant plus radiator mass by 31.8%, limited by thyristor (SCR) surge ratings | SP-428 III-3 | Primary | none | Medium |
| Rejection per m^2, one face, emittance 0.85 | 390 W/m^2 at 300 K; 3,012 at 500 K; 48,198 at 1,000 K (DERIVED, D3) | NIST sigma; White 1987 emittance | Derived | [WH] 3A: 459 W/m^2 at 300 K for emittance 1 | High |
| Area and mass for 10^15 / 10^18 / 10^21 W | 300 K: 2.6 x 10^12 / 2.6 x 10^15 / 2.6 x 10^18 m^2; 500 K: 3.3 x 10^11 / 3.3 x 10^14 / 3.3 x 10^17 m^2; 1,000 K: 2.1 x 10^10 / 2.1 x 10^13 / 2.1 x 10^16 m^2. At 5 kg/m^2 the heaviest case (10^21 W at 300 K) is 1.3 x 10^19 kg, 3.9 x 10^-5 of Mercury's mass; but **10^21 W at 300 K needs 34,000 times Mercury's surface area** (DERIVED, D3) | D3 | Derived | SP-428's 20 kg/kW gives 2 x 10^19 kg for 10^21 W at 300 K | High (physics) |
| Sink problem at Mercury's surface | A vertical radiator by day sees a ~580 K sink; ground infrared ~12.7 kW/m^2; night and polar shadow sinks ~83-90 K | [ME] F11 | Derived via sibling | — | High |
| Heat that leaves with the product | Kinetic energy given to launched mass is not heat: thrown to escape it leaves as gravitational energy. Waste heat is everything else: the coil, conditioning, transmission and receiver losses, and all processing energy. Export of stored energy is the only way other than radiating ([WH] 3A) | [WH] 3A; physics | Derived | none | High |

### F4. Planet-scale thermal limits (checklist 4)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Energy balance of a star-scale civilization | alpha + epsilon = gamma + nu (collected plus generated = waste heat plus non-thermal output); maximum efficiency Carnot, eta = 1 - T_waste/T* (Slysh 1985); radiator area must grow as (1/T_waste)^4: 290 K -> 29 K raises area 10^4; "reasonable" T_waste 150 to 600 K (a factor of 250 in area); a 1 AU sphere ~250 K | Wright, Griffith, Sigurdsson, Povich, Mullan, "The Ĝ infrared search ... II", ApJ (accepted 23 Jun 2014), arXiv 1408.1134 | Primary | Wright 2020 below | High (framework) |
| Mass versus efficiency of a full sphere | A = 4 pi R*^2 (1 - eta)^-3: each added "nine" of efficiency needs 10^3 times the radiating material; nominal 1 au sphere 160 K, eta_max 97%; rigid shells unstable, swarms preferred | J. T. Wright, "Dyson Spheres", Serbian Astron. J. (2020), arXiv 2006.16734v3 (7 Oct 2020) | Primary | Ĝ II gives ~250 K for the same 1 au case (Conflicts K2) | High |
| Optimal use of limited mass | "Unless one has enough mass to capture most of a star's luminosity, the optimal placement of mass is as close to the star as possible"; "very little gain per gram ... once ~10% of the starlight is being used"; swarms that capture most light have optical depths of a few; Landsberg limit reduces to Carnot; computation costs kT ln 2 per bit (Landauer) and nested "Matrioshka" shells give no benefit for computation at that limit | J. T. Wright, "Application of the Thermodynamics of Radiation to Dyson Spheres as Work Extractors and Computational Engines ...", accepted to AAS Journals (2023), arXiv 2309.06564 | Primary | none | High (theory) |
| Feedback onto the star | Light returned by a sphere makes stars expand and cool; observable only for spheres much hotter than ~300 K or highly specular; Sun-like stars with radiative interiors little affected | Huston and Wright, arXiv 2110.13887v1 (26 Oct 2021) | Primary (preprint) | none | Medium |
| Planetary waste-heat limit by radiative balance | Earth's surface rises ~3 C when ~4% of absorbed sunlight (4,800 TW of 120,000 TW) is added as waste heat; at 2%/yr growth ~280 years | E. J. Chaisson, Eos 89(28):253 (2008), doi 10.1029/2008EO280001 | Primary | Balbi and Lingam (arXiv 2409.06737v2, Jan 2025): at ~1%/yr growth an Earth-like planet loses habitability on timescales <= ~1,000 years | High (simple balance) |
| Fraction of the Sun's output the jobs need | Mercury: 2.7 x 10^-6 (1,000 yr) to 2.8 x 10^-4 (31 yr); Venus atmosphere: 7 x 10^-9 to 4 x 10^-6; Venus solid: 4 x 10^-5 to 2.5 x 10^-2. As a swarm at Mercury's orbit these are also the optical depths: **far from a full swarm, so no star-scale thermal effect** (DERIVED, D5, D10) | D5, D10 | Derived | Armstrong and Sandberg's endpoint is a complete swarm (whole shell area) | Medium-high |
| Swarm and planet temperatures | Closed black shell at Mercury's orbit: outer face 633 K; isolated black element 532 K; Mercury inside such a shell would sit near the shell temperature or above (today's rapid-rotator mean is 440 K). Venus outside a complete shell at Mercury's orbit would receive the same flux as infrared; if it absorbs infrared fully its effective temperature rises from 227 K to 327 K (its 0.77 Bond albedo is for sunlight) (DERIVED, D10; infrared absorptivity of Venus's clouds not sourced) | D10 | Derived | none | Low-medium |

### F5. Energy storage and transmission (checklist 5)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Beaming apertures over interplanetary range | Microwave 5.8 GHz: 67 km each at 0.3 AU for 90% collection; laser 1.07 µm: 305 m; demonstrated links 1.54 km (microwave, ground) and 8.6 km (laser, air) | [NW] F8, D12 | Derived/primary via sibling | — | High (diffraction) |
| Night storage on Mercury's surface | 2,100 kWh per kW of continuous load at the equator; 760 kWh per kW at the best-lit polar point (82% lit) ([ME] F6). With batteries at 142 Wh/kg (cell) or 76 Wh/kg (ISS unit) ([LG] 3E): **14.8 to 27.6 t per kW at the equator, 5.4 to 10 t per kW at the pole, 640 to 3,300 times the mass of a 120 W/kg array per kW**; latent-heat storage (47-83 kJ/kg system level, [LG] 3D) needs 91-161 t per kW for heat (DERIVED, D6, calc 4) | D6 | Derived | none | High (arithmetic) |
| Conductor mass at fixed loss | Two-wire DC: m = 4 rho_m rho_e P L^2 / (f V^2): mass grows with the **square of distance**. Aluminum (2,700 kg/m^3, 2.65 x 10^-8 ohm m), 1.5% loss: 1 GW over 1,000 km at 1 MV, 1.9 x 10^7 kg; 10^18 W over 10,000 km at 10 MV, 1.9 x 10^16 kg (DERIVED, D7) | D7; KnowledgeDoor (Al density); HyperPhysics (resistivity) | Derived | TM-89864: 300 kW, 10 km, 13.3 kV gives 3,236 kg of conductor against a 6,530 kg assembly | Medium-high |
| Ring of collectors round Mercury instead of storage | Half of Mercury's circumference is 7.7 x 10^6 m; feeding the night side from the day side means lines of that length (D7 scaling applies); no study found | D7 | Derived | none | Low (no design) |

### F6. Scale relationships for the three jobs (checklist 6)

All from D5, D8 and calc 3. "Collector mass" spans 0.51 kg/m^2 (OTPS) at the best chain to 3.92 kg/m^2 (Armstrong and Sandberg)
at the worst chain; radiators are for the planet-side losses only (launcher, plus receiver if beamed), at emittance 0.85.

| Job and time | Launch kinetic power | Sunlight needed (fraction of L) | Collector area (m^2) | Collector mass (kg) | Planet-side heat (W) and as W/m^2 of the planet | Radiator area at 500 K, multiples of the planet's surface | Binding constraint |
|---|---|---|---|---|---|---|---|
| Mercury, 31 yr | 1.8 x 10^21 W | 1.6 x 10^-5 to 2.8 x 10^-4 | 6.7 x 10^17 to 1.2 x 10^19 | 3 x 10^17 to 5 x 10^19 | 6.8 x 10^19 (coils) to 8.7 x 10^20 (with microwave receivers); 9.1 x 10^5 to 1.2 x 10^7 W/m^2 | 303 to 3,879 | **Heat at the planet**; then power delivery to the surface (2.5 x 10^7 W/m^2 of kinetic power through the surface) |
| Mercury, 100 yr | 5.7 x 10^20 W | 5 x 10^-6 to 8.7 x 10^-5 | 2.1 x 10^17 to 3.7 x 10^18 | 10^17 to 1.4 x 10^19 | 2.1 x 10^19 to 2.7 x 10^20; 2.8 x 10^5 to 3.6 x 10^6 W/m^2 | 94 to 1,203 | Heat at the planet |
| Mercury, 1,000 yr | 5.7 x 10^19 W | 5 x 10^-7 to 8.7 x 10^-6 | 2.1 x 10^16 to 3.7 x 10^17 | 10^16 to 1.4 x 10^18 | 2.1 x 10^18 to 2.7 x 10^19; 2.8 x 10^4 to 3.6 x 10^5 W/m^2 | 9 to 120 | Heat at the planet (still 3 to 40 times the sunlight it already receives) |
| Venus atmosphere, 31 yr | 2.6 x 10^19 W | 2.3 x 10^-7 to 4 x 10^-6 | 9.7 x 10^15 to 1.7 x 10^17 (at Mercury's distance) | 5 x 10^15 to 7 x 10^17 | 9.8 x 10^17 to 1.3 x 10^19; 2.1 x 10^3 to 2.7 x 10^4 W/m^2 | 1 to 9 | Heat (and launching through a 92-bar atmosphere, outside this file) |
| Venus atmosphere, 100 yr | 8.2 x 10^18 W | 7 x 10^-8 to 1.2 x 10^-6 | 3 x 10^15 to 5 x 10^16 | 1.5 x 10^15 to 2 x 10^17 | 3 x 10^17 to 3.9 x 10^18; 660 to 8,500 W/m^2 | <1 to 3 | Heat marginal; launch method |
| Venus atmosphere, 1,000 yr | 8.2 x 10^17 W | 7 x 10^-9 to 1.2 x 10^-7 | 3 x 10^14 to 5 x 10^15 | 1.5 x 10^14 to 2 x 10^16 | 3 x 10^16 to 3.9 x 10^17; 66 to 850 W/m^2 | <1 | Not power or heat; the launch method and growth of industry |
| Venus solid, 31 yr | 1.6 x 10^23 W | 1.4 x 10^-3 to 2.5 x 10^-2 | 5.9 x 10^19 to 10^21 | 3 x 10^19 to 4 x 10^21 | coils alone 6 x 10^21; 1.3 x 10^7 (coils at 96.4%) to 3.5 x 10^8 W/m^2 (launch at 50%) | ~4,300 (coils only) | Heat at the planet, by orders of magnitude |
| Venus solid, 100 yr | 5 x 10^22 W | 4.3 x 10^-4 to 7.6 x 10^-3 | 1.8 x 10^19 to 3.2 x 10^20 | 9 x 10^18 to 1.3 x 10^21 | 4 x 10^6 (coils) to 1.1 x 10^8 W/m^2 (launch at 50%) | ~1,400 (coils only) | Heat |
| Venus solid, 1,000 yr | 5 x 10^21 W | 4.3 x 10^-5 to 7.6 x 10^-4 | 1.8 x 10^18 to 3.2 x 10^19 | 9 x 10^17 to 1.3 x 10^20 | 4 x 10^5 (coils) to 1.1 x 10^7 W/m^2 (launch at 50%) | ~140 (coils only) | Heat |

**Reading.** Collector area and mass are never binding: the largest collector mass (4 x 10^21 kg, Venus solid in 31 years)
is 0.08% of Venus's mass. Radiator mass is never binding either (D3). **What binds is where the heat is made.** A launcher or
beam receiver sits on the planet, so its losses must leave through the planet's own surface (or be exported in the launched
material); that surface is fixed and shrinks as the planet is taken apart. To keep Mercury's launcher losses no larger than
the sunlight it already receives, the launch chain on the planet must be at least 99.963% efficient at 31 years, 99.880% at
100 years and 98.80% at 1,000 years (D8). The best sourced figure, 96.4%, counts only coil losses. The one physical escape
found is to export the heat in the payload: at 96.4% the coil loss is 0.34 MJ/kg, which rock (0.84 kJ/kg/K, a lower bound)
can carry by leaving 400 K hotter; with a beamed receiver on the planet the loss is 4.3 MJ/kg and the rock would have to leave
5,100 K hotter, which is not possible (D8). Unmet by any source: whether launchers can run with hot payloads, and at what
coil efficiency.

### F7. Material for the collectors themselves: the bootstrapping loop (checklist 7)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Mercury surface per tonne | Si ~250 kg; Mg ~110; Al ~67; Ca 40-60; Na ~29; S 19-23; Fe 13-19 (partly sulfide); C ~14; Ti ~3; K ~1.3; Cl ~1.4; oxygen the balance; hydrogen and nitrogen scarce (polar ice 1 x 10^13 to 3 x 10^15 kg the only hydrogen) | [ME] F10, F5; [IMS] 1-2 | Primary via sibling | — | Medium |
| Where Mercury's iron is | Core, 420-470 km down; the disassembly paper's iron reflectors rest on a "30% silicate and 70% metal" bulk that is the core | [ME] F2, F9; Armstrong and Sandberg 2013 Sec. 4.1 | Primary | — | High |
| Silicon cells from local rock | Silicon extracted from lunar simulant was vacuum-evaporated onto glass and 25 µm Al foil; films ~1.1 eV and unintentionally p-type; cells need ">10 microns" of silicon; growth "exceeding 5-10 microns per hour"; evaporating dopants (As) was a limitation (DEMONSTRATED at film scale; no cell from lunar silicon reported) | Freundlich and Ignatiev (Univ. Houston), "Solar Cells for Lunar Application", NASA grant NAG 9-806 final report, Sep 1997, NTRS 19980003482 | Primary | Lunar thin-film silicon energy payback 150-300 h projected ([PR] 5) | Medium |
| Silicon per square meter of cell | 10 µm at 2.329 g/cm^3: 23.3 g/m^2, i.e. ~93 g of Mercury regolith per m^2 at 250 kg Si per tonne (DERIVED, D12) | Ioffe database (Si density); [ME] F10 | Derived | none | High (arithmetic); recovery fraction unknown |
| Energy payback of a collector at Mercury's distance | 3 to 322 hours across 0.51-3.92 kg/m^2, 16-149 kWh/kg of processing, 20-35% cells (DERIVED, D12). Energy is not what limits growth; the 5-year cycle in the disassembly model is a hardware and placement assumption | D12 from [PR] 5 | Derived | Armstrong and Sandberg: 5-year lag assumed, not derived | Medium |
| What collectors need that Mercury or Venus cannot supply at any demonstrated scale | Integrated circuits (no lithography in space; tools over 150 t), rare-earth magnets, lithium; electronics-grade chemicals need H, N, F, Cl and dopants B, P; III-V cells need Ga, In, As, Ge (CI-chondrite abundances Ga 9.51 ppm, Ge 33.2 ppm, In 0.0788 ppm; Mercury values not found); polyimide films need H and N | [PR] 3, 4; [IMS] | Primary via sibling | — | Medium-high |
| What collectors can use from Mercury | Aluminum mirrors (67 kg Al per tonne of rock); silicon cells (if dopants are supplied); glass and ceramic substrates; iron only by-product (13-19 kg/t) until the core is reached. Venus offers C, N, O, S from the air ([IMS] 4) but no reachable metal | [ME]; [IMS] | Primary via sibling | — | Medium |
| Mirror versus converter mass | Reflectors are 2.2% of SPS-ALPHA's mass; the photovoltaic and transmitter array is 94% | Mankins 2012 | Primary | OTPS RD1 heliostats concentrate 2-3 suns on PV | Medium |

## 4. Conflicts

- **K1. OTPS 2024 total mass: 585 t or 5,852 t.** The report's text says the five RD2 satellites total "1000 metric tons (MT)
  versus 585 MT" for RD1, while its mass tables give 5,852,000 kg (RD1) and 10,000,000 kg (RD2), and its summary says "5.9Mkg"
  and "10Mkg". The text figure is ten times smaller than the tables; most likely a unit slip in the text. This file uses the
  tables (0.51 and 0.53 kg/m^2). If the text were right the areal mass would be 0.05 kg/m^2, lighter than IKAROS's flown
  membrane with cells (66 g/m^2), which supports the tables.
- **K2. Temperature of a 1 au Dyson sphere: ~250 K or 160 K.** Ĝ II (2014) lists "T_waste ~ 250 K" for a classical 1 AU
  sphere (a blackbody shell radiating the Sun's luminosity outward gives about this). Wright (2020) gives 160 K for "our nominal
  1 au Dyson sphere" at maximum efficiency (97%), where work is extracted and the emitting area follows Eq. 64. Different
  definitions (pure re-radiation versus a sphere doing maximal work); not an error.
- **K3. Parker Solar Probe cell temperature limit: 120 C or 150-160 C.** The APL engineers' IEEE Spectrum article gives a
  120 C maximum for the cells; trade press gives "less than 302 degrees" F (150 C) and "320 F (160 C) or below" for the arrays.
  Possibly cell versus panel, or design versus operating limit; the engineers' figure is preferred.
- **K4. Aluminum resistivity: 2.65 or 2.82 x 10^-8 ohm m.** Textbook value for pure aluminum at 20 C versus a cleanroom
  table (likely deposited film or alloy). 6% difference; D7 uses 2.65 (pure bulk). Conductors would run hot near the Sun,
  raising resistivity further (temperature coefficient 0.0043/C, HyperPhysics), which is not included in D7.
- **K5. Armstrong and Sandberg's time to completion: 31.2 years (paper) versus 35.6 years (my re-implementation of their
  stated assumptions, D9).** The paper does not state the irradiance it used, how the seed array is counted, or how the 5-year
  lag is applied; any of these could account for 14%. The heat finding in D9 changes by less than a factor of two either way.
- **K6. Radiator areal mass spans 0.6 to 14 kg/m^2.** Liquid belt studies (0.6-1.3), NASA goals (2-4, <= 3), heat-pipe
  baselines (5, the Boeing SPS figure), reactor and NEP models (5.2-12.8; 7 at 400 K and 10 at 850 K plus 1.6 of truss), the
  flown ISS radiators (14.2 of planform). Different eras, temperatures, meteoroid armor and whether the truss is counted. The
  scale table brackets them; none changes which constraint binds.
- **K7. Mercury's binding energy: 1.79 x 10^30 J (uniform sphere, brief), 1.80 x 10^30 J (Armstrong and Sandberg), about
  1.90 x 10^30 J (two-layer model with the core of [ME] F2, D11).** The dense core raises it about 6%. The brief's figure is
  used throughout; every power in this file would rise by 6% with the two-layer value.
- **K8. Venus Express array power: ">= 1,100 W in Venus orbit" (ESA engineering page) versus "1,468 W" (a search summary, page
  not found).** Sizing minimum versus a reported value; the ESA figure is used.

## 5. Derived figures

All arithmetic run with `python3 -I`. Scripts and full outputs are in the scratch folder
`/tmp/claude-1000/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/3ccdb441-c6c0-49c3-a71c-ab4a4fdd3c1e/scratchpad/planetary_scale_power_and_heat/`
(`calc1.py`, `calc2.py` -> `calc2_out.txt`, `calc3.py` -> `calc3_out.txt`, `calc4.py` -> `calc4_out.txt`, `as_reimpl.py`).

**Inputs (all sourced):** sigma 5.670374419 x 10^-8 W m^-2 K^-4 (NIST CODATA 2022); L_sun 3.828 x 10^26 W; Mercury mass 3.3010
x 10^23 kg, radius 2,439.7 km, semimajor axis 57.909 x 10^6 km, mean irradiance 9,082.7 W/m^2, Bond albedo 0.068; Venus mass
4.8673 x 10^24 kg, radius 6,051.8 km, semimajor axis 108.210 x 10^6 km, irradiance 2,601.3 W/m^2, Bond albedo 0.77, escape
10.36 km/s, atmosphere 4.8 x 10^20 kg (NSSDC fact sheets, rows 1-3); Mercury perihelion and aphelion irradiance 14,390 and 6,250
W/m^2 ([ME] F6); 1 AU 1,361.0 W/m^2 ([LG] 3G); binding energies 1.79 x 10^30 and 1.57 x 10^32 J (brief); coating
absorptance/emittance ([LG] 3F); radiator emittance 0.85 (White 1987); efficiencies as in F2; Al 2,700 kg/m^3 and 2.65 x
10^-8 ohm m; Si 2,329 kg/m^3; rock heat capacity 0.2 cal/g/K = 837 J/kg/K at 350 K (Robie et al. 1970; 4.184 J/cal by
definition; a lower bound for hot rock); Julian year 3.15576 x 10^7 s.

**D1. Powers and areas (calc 1).** Minimum average launch power P = E/t. Irradiance recomputed from L at the semimajor axes:
9,083.8 and 2,601.5 W/m^2 (fact sheets 9,082.7 and 2,601.3). Venus atmosphere lifted to escape from the surface (ideal, no drag):
0.5 v_esc^2 = 53.66 MJ/kg, 2.576 x 10^28 J. Sunlight on each planet's own disk: Mercury 1.70 x 10^17 W, Venus 2.99 x 10^17 W,
so with only its own sunlight at 100% Mercury would take 3.3 x 10^5 years and solid Venus 1.7 x 10^7 years.

```
== Minimum average launch power P = E/t ==
Mercury (binding)               31 yr  P=1.830e+21 W  = 4.78e-06 of L_sun
Mercury (binding)              100 yr  P=5.672e+20 W  = 1.48e-06 of L_sun
Mercury (binding)             1000 yr  P=5.672e+19 W  = 1.48e-07 of L_sun
Venus solid (binding)           31 yr  P=1.605e+23 W  = 4.19e-04 of L_sun
Venus solid (binding)          100 yr  P=4.975e+22 W  = 1.30e-04 of L_sun
Venus solid (binding)         1000 yr  P=4.975e+21 W  = 1.30e-05 of L_sun
Venus atmosphere (escape)       31 yr  P=2.633e+19 W  = 6.88e-08 of L_sun
Venus atmosphere (escape)      100 yr  P=8.163e+18 W  = 2.13e-08 of L_sun
Venus atmosphere (escape)     1000 yr  P=8.163e+17 W  = 2.13e-09 of L_sun

== Sunlight on the planet's own cross-section, and minimum time at 100% / 20% if only that is used ==
Mercury      cross-section sunlight 1.698e+17 W; t_min(100%)=3.340e+05 yr; t(20%)=1.670e+06 yr
Venus solid  cross-section sunlight 2.993e+17 W; t_min(100%)=1.662e+07 yr; t(20%)=8.311e+07 yr
Venus atm    cross-section sunlight 2.993e+17 W; t_min(100%)=2.727e+03 yr; t(20%)=1.364e+04 yr

== Full-shell sunlight at the orbit; shell area; planet mass per m2 of shell ==
Mercury  shell area 4.214e+22 m2; M/A=7.83 kg/m2; outer-face T of closed black shell 633 K
Venus    shell area 1.471e+23 m2; M/A=33.08 kg/m2; outer-face T of closed black shell 463 K
```

**D2. Equilibrium temperature** T = (alpha S / (k eps sigma))^(1/4); k = 1 for an insulated back, 2 for a thin plate radiating
from both faces; a photovoltaic element exports eta S as electricity, so (alpha - eta) S is heat.

```
== D2. Equilibrium temperature of a flat element facing the Sun, T=(alpha S/(k eps sigma))^1/4 ==
black Z306 (0.95/0.89)                           Me_peri  721/ 607 | Me_mean  643/ 541 | Me_aph  586/ 492 | Ve_mean  470/ 396 | 1AU  400/ 336   (insulated back k=1 / two faces k=2), K
Z-93 white (0.17/0.92)                           Me_peri  465/ 391 | Me_mean  415/ 349 | Me_aph  378/ 318 | Ve_mean  303/ 255 | 1AU  258/ 217   (insulated back k=1 / two faces k=2), K
quartz OSR (0.065/0.80)                          Me_peri  379/ 319 | Me_mean  338/ 284 | Me_aph  308/ 259 | Ve_mean  247/ 208 | 1AU  210/ 177   (insulated back k=1 / two faces k=2), K
bare VDA aluminum (0.12/0.04), both faces bare   Me_peri  934/ 785 | Me_mean  833/ 700 | Me_aph  758/ 638 | Ve_mean  609/ 512 | 1AU  518/ 436   (insulated back k=1 / two faces k=2), K
  VDA front + eps-0.80 back, Me_peri: 436 K
  VDA front + eps-0.80 back, Me_mean: 389 K
  VDA front + eps-0.80 back, Me_aph: 354 K
  VDA front + eps-0.80 back, Ve_mean: 285 K
  VDA front + eps-0.80 back, 1AU: 242 K
  black PV element exporting 0% of incident, two faces eps 0.89: Me_peri 607 K, Me_mean 541 K, Ve_mean 396 K, 1AU 336 K
  black PV element exporting 20% of incident, two faces eps 0.89: Me_peri 572 K, Me_mean 510 K, Ve_mean 373 K, 1AU 317 K
  black PV element exporting 30% of incident, two faces eps 0.89: Me_peri 552 K, Me_mean 492 K, Ve_mean 360 K, 1AU 306 K

```

**D3. Radiators.** A = Q / (eps sigma T^4), one face, eps 0.85, sink 0 K (a two-sided panel in free space halves the area;
any warm surroundings raise the sink and enlarge it).

```
== D3. Radiator area and mass for a heat load Q, one radiating face, eps 0.85, sink 0 K ==
Q=1e+15 W T= 300 K: 390 W/m2; A=2.561e+12 m2 (= 3.42e-02 x Mercury's surface, 6.08e-11 of the Mercury-orbit shell); mass at 1/3/5 kg/m2 = 2.56e+12/7.68e+12/1.28e+13 kg (3.9e-11 of Mercury's mass at 5)
Q=1e+15 W T= 500 K: 3012 W/m2; A=3.320e+11 m2 (= 4.44e-03 x Mercury's surface, 7.88e-12 of the Mercury-orbit shell); mass at 1/3/5 kg/m2 = 3.32e+11/9.96e+11/1.66e+12 kg (5.0e-12 of Mercury's mass at 5)
Q=1e+15 W T=1000 K: 48198 W/m2; A=2.075e+10 m2 (= 2.77e-04 x Mercury's surface, 4.92e-13 of the Mercury-orbit shell); mass at 1/3/5 kg/m2 = 2.07e+10/6.22e+10/1.04e+11 kg (3.1e-13 of Mercury's mass at 5)
   SP-428 assumption 20 kg/kW at 300 K: 2.00e+13 kg
Q=1e+18 W T= 300 K: 390 W/m2; A=2.561e+15 m2 (= 3.42e+01 x Mercury's surface, 6.08e-08 of the Mercury-orbit shell); mass at 1/3/5 kg/m2 = 2.56e+15/7.68e+15/1.28e+16 kg (3.9e-08 of Mercury's mass at 5)
Q=1e+18 W T= 500 K: 3012 W/m2; A=3.320e+14 m2 (= 4.44e+00 x Mercury's surface, 7.88e-09 of the Mercury-orbit shell); mass at 1/3/5 kg/m2 = 3.32e+14/9.96e+14/1.66e+15 kg (5.0e-09 of Mercury's mass at 5)
Q=1e+18 W T=1000 K: 48198 W/m2; A=2.075e+13 m2 (= 2.77e-01 x Mercury's surface, 4.92e-10 of the Mercury-orbit shell); mass at 1/3/5 kg/m2 = 2.07e+13/6.22e+13/1.04e+14 kg (3.1e-10 of Mercury's mass at 5)
   SP-428 assumption 20 kg/kW at 300 K: 2.00e+16 kg
Q=1e+21 W T= 300 K: 390 W/m2; A=2.561e+18 m2 (= 3.42e+04 x Mercury's surface, 6.08e-05 of the Mercury-orbit shell); mass at 1/3/5 kg/m2 = 2.56e+18/7.68e+18/1.28e+19 kg (3.9e-05 of Mercury's mass at 5)
Q=1e+21 W T= 500 K: 3012 W/m2; A=3.320e+17 m2 (= 4.44e+03 x Mercury's surface, 7.88e-06 of the Mercury-orbit shell); mass at 1/3/5 kg/m2 = 3.32e+17/9.96e+17/1.66e+18 kg (5.0e-06 of Mercury's mass at 5)
Q=1e+21 W T=1000 K: 48198 W/m2; A=2.075e+16 m2 (= 2.77e+02 x Mercury's surface, 4.92e-07 of the Mercury-orbit shell); mass at 1/3/5 kg/m2 = 2.07e+16/6.22e+16/1.04e+17 kg (3.1e-07 of Mercury's mass at 5)
   SP-428 assumption 20 kg/kW at 300 K: 2.00e+19 kg

```

**D4. Chain.** eta = cell x DC-DC (0.90) x transmission x launcher.

```
== D4. End-to-end chain, sunlight -> kinetic energy of launched mass ==
hot cell 0.20 (Landis optimum near 600 K)  cable 1.5% loss (TM-89864)                                     windings only 0.964 (SP-428)       end-to-end 0.1709
hot cell 0.20 (Landis optimum near 600 K)  cable 1.5% loss (TM-89864)                                     A&S assumed launch system 0.50     end-to-end 0.0887
hot cell 0.20 (Landis optimum near 600 K)  microwave, OTPS chain w/o atmosphere (0.70*0.90*0.95*0.78*0.90) windings only 0.964 (SP-428)       end-to-end 0.0729
hot cell 0.20 (Landis optimum near 600 K)  microwave, OTPS chain w/o atmosphere (0.70*0.90*0.95*0.78*0.90) A&S assumed launch system 0.50     end-to-end 0.0378
hot cell 0.20 (Landis optimum near 600 K)  laser 0.38 x PV 0.50 (Landis 2025 components)                  windings only 0.964 (SP-428)       end-to-end 0.0330
hot cell 0.20 (Landis optimum near 600 K)  laser 0.38 x PV 0.50 (Landis 2025 components)                  A&S assumed launch system 0.50     end-to-end 0.0171
MESSENGER-class 0.28                       cable 1.5% loss (TM-89864)                                     windings only 0.964 (SP-428)       end-to-end 0.2393
MESSENGER-class 0.28                       cable 1.5% loss (TM-89864)                                     A&S assumed launch system 0.50     end-to-end 0.1241
MESSENGER-class 0.28                       microwave, OTPS chain w/o atmosphere (0.70*0.90*0.95*0.78*0.90) windings only 0.964 (SP-428)       end-to-end 0.1021
MESSENGER-class 0.28                       microwave, OTPS chain w/o atmosphere (0.70*0.90*0.95*0.78*0.90) A&S assumed launch system 0.50     end-to-end 0.0529
MESSENGER-class 0.28                       laser 0.38 x PV 0.50 (Landis 2025 components)                  windings only 0.964 (SP-428)       end-to-end 0.0462
MESSENGER-class 0.28                       laser 0.38 x PV 0.50 (Landis 2025 components)                  A&S assumed launch system 0.50     end-to-end 0.0239
OTPS 1 AU 0.35                             cable 1.5% loss (TM-89864)                                     windings only 0.964 (SP-428)       end-to-end 0.2991
OTPS 1 AU 0.35                             cable 1.5% loss (TM-89864)                                     A&S assumed launch system 0.50     end-to-end 0.1551
OTPS 1 AU 0.35                             microwave, OTPS chain w/o atmosphere (0.70*0.90*0.95*0.78*0.90) windings only 0.964 (SP-428)       end-to-end 0.1276
OTPS 1 AU 0.35                             microwave, OTPS chain w/o atmosphere (0.70*0.90*0.95*0.78*0.90) A&S assumed launch system 0.50     end-to-end 0.0662
OTPS 1 AU 0.35                             laser 0.38 x PV 0.50 (Landis 2025 components)                  windings only 0.964 (SP-428)       end-to-end 0.0577
OTPS 1 AU 0.35                             laser 0.38 x PV 0.50 (Landis 2025 components)                  A&S assumed launch system 0.50     end-to-end 0.0299
range 0.0171 to 0.2991; A&S overall assumption 1/3 x 1/10 = 0.0333

```

**D5. Scale table** (each job at 96.4% and 50% launch efficiency; sunlight for the best upstream chain 0.35 x 0.90 x 0.985 and
the worst 0.20 x 0.90 x 0.19; collector area at Mercury's mean irradiance; collector mass 0.51 kg/m^2 x best area to 3.92 kg/m^2
x worst area; "by 120 W/kg" = electric power at the launcher / 120 W/kg).

```
== D5. Scale table ==
Mercury, binding                31 yr launcher=0.964: Pk=1.83e+21 W (4.8e-06 L) Pe=1.90e+21 W | sunlight 6.1e+21-5.5e+22 W (1.6e-05-1.4e-04 L) | collector area 6.7e+17-6.1e+18 m2 | collector mass 3.4e+17-2.4e+19 kg; by 120 W/kg 1.6e+19 kg | launcher loss 6.8e+19 W = 9.14e+05 W/m2 of planet surface | Pk per m2 of planet surface 2.45e+07 W/m2
Mercury, binding                31 yr launcher=0.50: Pk=1.83e+21 W (4.8e-06 L) Pe=3.66e+21 W | sunlight 1.2e+22-1.1e+23 W (3.1e-05-2.8e-04 L) | collector area 1.3e+18-1.2e+19 m2 | collector mass 6.6e+17-4.6e+19 kg; by 120 W/kg 3.0e+19 kg | launcher loss 1.8e+21 W = 2.45e+07 W/m2 of planet surface | Pk per m2 of planet surface 2.45e+07 W/m2
Mercury, binding               100 yr launcher=0.964: Pk=5.67e+20 W (1.5e-06 L) Pe=5.88e+20 W | sunlight 1.9e+21-1.7e+22 W (5.0e-06-4.5e-05 L) | collector area 2.1e+17-1.9e+18 m2 | collector mass 1.1e+17-7.4e+18 kg; by 120 W/kg 4.9e+18 kg | launcher loss 2.1e+19 W = 2.83e+05 W/m2 of planet surface | Pk per m2 of planet surface 7.58e+06 W/m2
Mercury, binding               100 yr launcher=0.50: Pk=5.67e+20 W (1.5e-06 L) Pe=1.13e+21 W | sunlight 3.7e+21-3.3e+22 W (9.6e-06-8.7e-05 L) | collector area 4.0e+17-3.7e+18 m2 | collector mass 2.1e+17-1.4e+19 kg; by 120 W/kg 9.5e+18 kg | launcher loss 5.7e+20 W = 7.58e+06 W/m2 of planet surface | Pk per m2 of planet surface 7.58e+06 W/m2
Mercury, binding              1000 yr launcher=0.964: Pk=5.67e+19 W (1.5e-07 L) Pe=5.88e+19 W | sunlight 1.9e+20-1.7e+21 W (5.0e-07-4.5e-06 L) | collector area 2.1e+16-1.9e+17 m2 | collector mass 1.1e+16-7.4e+17 kg; by 120 W/kg 4.9e+17 kg | launcher loss 2.1e+18 W = 2.83e+04 W/m2 of planet surface | Pk per m2 of planet surface 7.58e+05 W/m2
Mercury, binding              1000 yr launcher=0.50: Pk=5.67e+19 W (1.5e-07 L) Pe=1.13e+20 W | sunlight 3.7e+20-3.3e+21 W (9.6e-07-8.7e-06 L) | collector area 4.0e+16-3.7e+17 m2 | collector mass 2.1e+16-1.4e+18 kg; by 120 W/kg 9.5e+17 kg | launcher loss 5.7e+19 W = 7.58e+05 W/m2 of planet surface | Pk per m2 of planet surface 7.58e+05 W/m2
Venus atmosphere, to escape     31 yr launcher=0.964: Pk=2.63e+19 W (6.9e-08 L) Pe=2.73e+19 W | sunlight 8.8e+19-8.0e+20 W (2.3e-07-2.1e-06 L) | collector area 9.7e+15-8.8e+16 m2 | collector mass 4.9e+15-3.4e+17 kg; by 120 W/kg 2.3e+17 kg | launcher loss 9.8e+17 W = 2.14e+03 W/m2 of planet surface | Pk per m2 of planet surface 5.72e+04 W/m2
Venus atmosphere, to escape     31 yr launcher=0.50: Pk=2.63e+19 W (6.9e-08 L) Pe=5.27e+19 W | sunlight 1.7e+20-1.5e+21 W (4.4e-07-4.0e-06 L) | collector area 1.9e+16-1.7e+17 m2 | collector mass 9.5e+15-6.6e+17 kg; by 120 W/kg 4.4e+17 kg | launcher loss 2.6e+19 W = 5.72e+04 W/m2 of planet surface | Pk per m2 of planet surface 5.72e+04 W/m2
Venus atmosphere, to escape    100 yr launcher=0.964: Pk=8.16e+18 W (2.1e-08 L) Pe=8.47e+18 W | sunlight 2.7e+19-2.5e+20 W (7.1e-08-6.5e-07 L) | collector area 3.0e+15-2.7e+16 m2 | collector mass 1.5e+15-1.1e+17 kg; by 120 W/kg 7.1e+16 kg | launcher loss 3.0e+17 W = 6.62e+02 W/m2 of planet surface | Pk per m2 of planet surface 1.77e+04 W/m2
Venus atmosphere, to escape    100 yr launcher=0.50: Pk=8.16e+18 W (2.1e-08 L) Pe=1.63e+19 W | sunlight 5.3e+19-4.8e+20 W (1.4e-07-1.2e-06 L) | collector area 5.8e+15-5.3e+16 m2 | collector mass 3.0e+15-2.1e+17 kg; by 120 W/kg 1.4e+17 kg | launcher loss 8.2e+18 W = 1.77e+04 W/m2 of planet surface | Pk per m2 of planet surface 1.77e+04 W/m2
Venus atmosphere, to escape   1000 yr launcher=0.964: Pk=8.16e+17 W (2.1e-09 L) Pe=8.47e+17 W | sunlight 2.7e+18-2.5e+19 W (7.1e-09-6.5e-08 L) | collector area 3.0e+14-2.7e+15 m2 | collector mass 1.5e+14-1.1e+16 kg; by 120 W/kg 7.1e+15 kg | launcher loss 3.0e+16 W = 6.62e+01 W/m2 of planet surface | Pk per m2 of planet surface 1.77e+03 W/m2
Venus atmosphere, to escape   1000 yr launcher=0.50: Pk=8.16e+17 W (2.1e-09 L) Pe=1.63e+18 W | sunlight 5.3e+18-4.8e+19 W (1.4e-08-1.2e-07 L) | collector area 5.8e+14-5.3e+15 m2 | collector mass 3.0e+14-2.1e+16 kg; by 120 W/kg 1.4e+16 kg | launcher loss 8.2e+17 W = 1.77e+03 W/m2 of planet surface | Pk per m2 of planet surface 1.77e+03 W/m2
Venus solid, binding            31 yr launcher=0.964: Pk=1.60e+23 W (4.2e-04 L) Pe=1.66e+23 W | sunlight 5.4e+23-4.9e+24 W (1.4e-03-1.3e-02 L) | collector area 5.9e+19-5.4e+20 m2 | collector mass 3.0e+19-2.1e+21 kg; by 120 W/kg 1.4e+21 kg | launcher loss 6.0e+21 W = 1.30e+07 W/m2 of planet surface | Pk per m2 of planet surface 3.49e+08 W/m2
Venus solid, binding            31 yr launcher=0.50: Pk=1.60e+23 W (4.2e-04 L) Pe=3.21e+23 W | sunlight 1.0e+24-9.4e+24 W (2.7e-03-2.5e-02 L) | collector area 1.1e+20-1.0e+21 m2 | collector mass 5.8e+19-4.1e+21 kg; by 120 W/kg 2.7e+21 kg | launcher loss 1.6e+23 W = 3.49e+08 W/m2 of planet surface | Pk per m2 of planet surface 3.49e+08 W/m2
Venus solid, binding           100 yr launcher=0.964: Pk=4.98e+22 W (1.3e-04 L) Pe=5.16e+22 W | sunlight 1.7e+23-1.5e+24 W (4.3e-04-3.9e-03 L) | collector area 1.8e+19-1.7e+20 m2 | collector mass 9.3e+18-6.5e+20 kg; by 120 W/kg 4.3e+20 kg | launcher loss 1.9e+21 W = 4.04e+06 W/m2 of planet surface | Pk per m2 of planet surface 1.08e+08 W/m2
Venus solid, binding           100 yr launcher=0.50: Pk=4.98e+22 W (1.3e-04 L) Pe=9.95e+22 W | sunlight 3.2e+23-2.9e+24 W (8.4e-04-7.6e-03 L) | collector area 3.5e+19-3.2e+20 m2 | collector mass 1.8e+19-1.3e+21 kg; by 120 W/kg 8.3e+20 kg | launcher loss 5.0e+22 W = 1.08e+08 W/m2 of planet surface | Pk per m2 of planet surface 1.08e+08 W/m2
Venus solid, binding          1000 yr launcher=0.964: Pk=4.98e+21 W (1.3e-05 L) Pe=5.16e+21 W | sunlight 1.7e+22-1.5e+23 W (4.3e-05-3.9e-04 L) | collector area 1.8e+18-1.7e+19 m2 | collector mass 9.3e+17-6.5e+19 kg; by 120 W/kg 4.3e+19 kg | launcher loss 1.9e+20 W = 4.04e+05 W/m2 of planet surface | Pk per m2 of planet surface 1.08e+07 W/m2
Venus solid, binding          1000 yr launcher=0.50: Pk=4.98e+21 W (1.3e-05 L) Pe=9.95e+21 W | sunlight 3.2e+22-2.9e+23 W (8.4e-05-7.6e-04 L) | collector area 3.5e+18-3.2e+19 m2 | collector mass 1.8e+18-1.3e+20 kg; by 120 W/kg 8.3e+19 kg | launcher loss 5.0e+21 W = 1.08e+07 W/m2 of planet surface | Pk per m2 of planet surface 1.08e+07 W/m2

```

**D8. Heat at the planet.** Planet-side heat Q divided by the planet's surface area, as the blackbody temperature that would
radiate it (sunlight not added). Receiver case: power arriving by microwave beam, rectenna 0.78 and DC-DC 0.90, so 29.8% of what
is received becomes heat on the planet. Allowed loss fraction for launcher losses to equal the mean sunlight flux: f = S A / P_k.
Payload heat export: Delta T = loss per kg / c_p.

```
== D8. Heat deposited at the planet, as a blackbody temperature of the whole planetary surface (eps 1, sunlight ignored) ==
Mercury, binding                31 yr windings 0.964 only                                        9.14e+05 W/m2 ->  2003 K (sunlight on that surface 9083 W/m2)
Mercury, binding                31 yr A&S launch eff 0.50                                        2.45e+07 W/m2 ->  4557 K (sunlight on that surface 9083 W/m2)
Mercury, binding                31 yr microwave receiver (rectenna 0.78*DCDC 0.90) + windings    1.17e+07 W/m2 ->  3789 K (sunlight on that surface 9083 W/m2)
Mercury, binding               100 yr windings 0.964 only                                        2.83e+05 W/m2 ->  1495 K (sunlight on that surface 9083 W/m2)
Mercury, binding               100 yr A&S launch eff 0.50                                        7.58e+06 W/m2 ->  3401 K (sunlight on that surface 9083 W/m2)
Mercury, binding               100 yr microwave receiver (rectenna 0.78*DCDC 0.90) + windings    3.62e+06 W/m2 ->  2827 K (sunlight on that surface 9083 W/m2)
Mercury, binding              1000 yr windings 0.964 only                                        2.83e+04 W/m2 ->   841 K (sunlight on that surface 9083 W/m2)
Mercury, binding              1000 yr A&S launch eff 0.50                                        7.58e+05 W/m2 ->  1912 K (sunlight on that surface 9083 W/m2)
Mercury, binding              1000 yr microwave receiver (rectenna 0.78*DCDC 0.90) + windings    3.62e+05 W/m2 ->  1590 K (sunlight on that surface 9083 W/m2)
Venus atmosphere, to escape     31 yr windings 0.964 only                                        2.14e+03 W/m2 ->   441 K (sunlight on that surface 2601 W/m2)
Venus atmosphere, to escape     31 yr A&S launch eff 0.50                                        5.72e+04 W/m2 ->  1002 K (sunlight on that surface 2601 W/m2)
Venus atmosphere, to escape     31 yr microwave receiver (rectenna 0.78*DCDC 0.90) + windings    2.73e+04 W/m2 ->   833 K (sunlight on that surface 2601 W/m2)
Venus atmosphere, to escape    100 yr windings 0.964 only                                        6.62e+02 W/m2 ->   329 K (sunlight on that surface 2601 W/m2)
Venus atmosphere, to escape    100 yr A&S launch eff 0.50                                        1.77e+04 W/m2 ->   748 K (sunlight on that surface 2601 W/m2)
Venus atmosphere, to escape    100 yr microwave receiver (rectenna 0.78*DCDC 0.90) + windings    8.47e+03 W/m2 ->   622 K (sunlight on that surface 2601 W/m2)
Venus atmosphere, to escape   1000 yr windings 0.964 only                                        6.62e+01 W/m2 ->   185 K (sunlight on that surface 2601 W/m2)
Venus atmosphere, to escape   1000 yr A&S launch eff 0.50                                        1.77e+03 W/m2 ->   421 K (sunlight on that surface 2601 W/m2)
Venus atmosphere, to escape   1000 yr microwave receiver (rectenna 0.78*DCDC 0.90) + windings    8.47e+02 W/m2 ->   350 K (sunlight on that surface 2601 W/m2)
Mercury 31 yr: loss fraction allowed for loss <= mean sunlight flux: 3.71e-04 -> efficiency >= 0.999629
Mercury 100 yr: loss fraction allowed for loss <= mean sunlight flux: 1.20e-03 -> efficiency >= 0.998802
Mercury 1000 yr: loss fraction allowed for loss <= mean sunlight flux: 1.20e-02 -> efficiency >= 0.988023

   Sensible heat carried away in launched rock (cp 0.84 kJ/kg/K, lower bound at 350 K):
   windings 0.964                   loss 0.34 MJ/kg -> temperature rise of the payload to carry it: 402 K
   A&S 0.50                         loss 9.00 MJ/kg -> temperature rise of the payload to carry it: 10755 K
   microwave receiver + windings    loss 4.30 MJ/kg -> temperature rise of the payload to carry it: 5138 K

Mercury             31 yr windings 0.964               Q=6.8e+19 W: 300K 1.8e+17 m2 (2340 x surface); 500K 2.3e+16 m2 (303 x surface); 1000K 1.4e+15 m2 (19 x surface)
Mercury             31 yr microwave receiver+windings  Q=8.7e+20 W: 300K 2.2e+18 m2 (29932 x surface); 500K 2.9e+17 m2 (3879 x surface); 1000K 1.8e+16 m2 (242 x surface)
Mercury            100 yr windings 0.964               Q=2.1e+19 W: 300K 5.4e+16 m2 (725 x surface); 500K 7.0e+15 m2 (94 x surface); 1000K 4.4e+14 m2 (6 x surface)
Mercury            100 yr microwave receiver+windings  Q=2.7e+20 W: 300K 6.9e+17 m2 (9279 x surface); 500K 9.0e+16 m2 (1203 x surface); 1000K 5.6e+15 m2 (75 x surface)
Mercury           1000 yr windings 0.964               Q=2.1e+18 W: 300K 5.4e+15 m2 (73 x surface); 500K 7.0e+14 m2 (9 x surface); 1000K 4.4e+13 m2 (1 x surface)
Mercury           1000 yr microwave receiver+windings  Q=2.7e+19 W: 300K 6.9e+16 m2 (928 x surface); 500K 9.0e+15 m2 (120 x surface); 1000K 5.6e+14 m2 (8 x surface)
Venus atmosphere    31 yr windings 0.964               Q=9.8e+17 W: 300K 2.5e+15 m2 (5 x surface); 500K 3.3e+14 m2 (1 x surface); 1000K 2.0e+13 m2 (0 x surface)
Venus atmosphere    31 yr microwave receiver+windings  Q=1.3e+19 W: 300K 3.2e+16 m2 (70 x surface); 500K 4.2e+15 m2 (9 x surface); 1000K 2.6e+14 m2 (1 x surface)
Venus atmosphere   100 yr windings 0.964               Q=3.0e+17 W: 300K 7.8e+14 m2 (2 x surface); 500K 1.0e+14 m2 (0 x surface); 1000K 6.3e+12 m2 (0 x surface)
Venus atmosphere   100 yr microwave receiver+windings  Q=3.9e+18 W: 300K 1.0e+16 m2 (22 x surface); 500K 1.3e+15 m2 (3 x surface); 1000K 8.1e+13 m2 (0 x surface)
Venus atmosphere  1000 yr windings 0.964               Q=3.0e+16 W: 300K 7.8e+13 m2 (0 x surface); 500K 1.0e+13 m2 (0 x surface); 1000K 6.3e+11 m2 (0 x surface)
Venus atmosphere  1000 yr microwave receiver+windings  Q=3.9e+17 W: 300K 1.0e+15 m2 (2 x surface); 500K 1.3e+14 m2 (0 x surface); 1000K 8.1e+12 m2 (0 x surface)

bootstrapping set, parts                 58 MJ/kg = 6.4 x Mercury escape 9.0 MJ/kg; x Mercury mass = 1.9e+31 J (11 x binding energy)
SP-413 Al refinery, elec+heat            112 MJ/kg = 12.4 x Mercury escape 9.0 MJ/kg; x Mercury mass = 3.7e+31 J (21 x binding energy)
self-replicating factory, all products   536 MJ/kg = 59.6 x Mercury escape 9.0 MJ/kg; x Mercury mass = 1.8e+32 J (99 x binding energy)
```

**D6. Night storage** = stored energy per kW / specific energy. Latent heat storage: 2,100 kWh = 7.56 x 10^9 J per kW.

```
== D6. Storage for Mercury's equatorial night and the best polar site ([ME] F6 D6; battery figures [LG] 3E/D5) ==
   equator 2,100 kWh per kW           cells 142 Wh/kg    14.8 t per kW continuous (= 1775 x the collector mass per kW at 120 W/kg)
   equator 2,100 kWh per kW           ISS ORU 76 Wh/kg   27.6 t per kW continuous (= 3316 x the collector mass per kW at 120 W/kg)
   best polar point 760 kWh per kW    cells 142 Wh/kg    5.4 t per kW continuous (= 642 x the collector mass per kW at 120 W/kg)
   best polar point 760 kWh per kW    ISS ORU 76 Wh/kg   10.0 t per kW continuous (= 1200 x the collector mass per kW at 120 W/kg)

PCM storage for 2,100 kWh of heat at 47 kJ/kg: 161 t
PCM storage for 2,100 kWh of heat at 83 kJ/kg: 91 t
```

**D7. Conductors.** For a two-wire DC line of length L carrying P at voltage V with loss fraction f: R = 2 rho_e L / A,
f = P R / V^2, so A = 2 rho_e L P / (f V^2) and m = 2 rho_m L A = 4 rho_m rho_e P L^2 / (f V^2). Bare conductor only (no
insulation, armor or supports).

```
== D7. Conductor mass for DC transmission at fixed loss fraction f: m = 4 rho_m rho_e P L^2 / (f V^2) (two conductors) ==
   TM-89864 check: 300 kW, 10 km, 13.3 kV, f 0.015: conductor 3236 kg (study's whole assembly 6,530 kg incl. tubes, bumpers)
   P=1e+09 W over 1e+06 m at 1e+06 V, 1.5% loss: 1.91e+07 kg aluminum
   P=1e+12 W over 1e+06 m at 1e+06 V, 1.5% loss: 1.91e+10 kg aluminum
   P=1e+15 W over 1e+07 m at 1e+07 V, 1.5% loss: 1.91e+13 kg aluminum
   P=1e+18 W over 1e+07 m at 1e+07 V, 1.5% loss: 1.91e+16 kg aluminum
   circumference of Mercury 1.533e+07 m; half 7.665e+06 m

```

**D9. Armstrong and Sandberg re-implemented** (`as_reimpl.py`): collector area = seed 1 km^2 + (half of the mass removed five
years earlier) / 3.92 kg/m^2; delivered power = S x area / 3; removal rate = (1/10 of delivered power) / 9 MJ/kg; Mercury mass
3.3022 x 10^23 kg. Heat at Mercury = 9/10 of delivered power (the paper's own split), over today's surface area.

```
S=9082.7 t_done=35.62 yr P at half-mass 5.05e+23 W, at end 9.88e+23 W
   waste (9/10 of delivered) per m2 of Mercury surface 6.08e+09 W/m2 -> blackbody T 18094 K
   waste (9/10 of delivered) per m2 of Mercury surface 1.19e+10 W/m2 -> blackbody T 21400 K
S=1361x6.67 t_done=35.62 yr P at half-mass 5.05e+23 W, at end 9.88e+23 W
   waste (9/10 of delivered) per m2 of Mercury surface 6.08e+09 W/m2 -> blackbody T 18094 K
   waste (9/10 of delivered) per m2 of Mercury surface 1.19e+10 W/m2 -> blackbody T 21400 K
```

**D10. Swarm and planet temperatures; intercepted fractions.** Closed shell outer face T = (L / (4 pi a^2 sigma))^(1/4);
isolated black two-face element (S / (2 sigma))^(1/4); rapid-rotator planet (S (1 - A) / (4 sigma))^(1/4). Intercepted fraction
= sunlight needed / L, equal to the optical depth of a swarm at that distance.

```
== D10. Swarm and planet temperatures ==
   Mercury orbit: closed black shell outer face 633 K; isolated black two-face element 532 K
   Venus orbit: closed black shell outer face 463 K; isolated black two-face element 389 K
   Mercury today, rapid-rotator mean equilibrium with Bond albedo 0.068: 440 K
   Venus today, effective with Bond albedo 0.77: 227 K; if lit only by a 633 K shell's IR and IR absorptivity ~1: 327 K
   Mercury 31 yr at end-to-end 0.033: fraction of L intercepted 1.43e-04; swarm optical depth if at Mercury orbit 1.43e-04
   Mercury 31 yr at end-to-end 0.054: fraction of L intercepted 8.85e-05; swarm optical depth if at Mercury orbit 8.85e-05
   Mercury 1000 yr at end-to-end 0.033: fraction of L intercepted 4.45e-06; swarm optical depth if at Mercury orbit 4.45e-06
   Mercury 1000 yr at end-to-end 0.054: fraction of L intercepted 2.74e-06; swarm optical depth if at Mercury orbit 2.74e-06
   Venus solid 31 yr at end-to-end 0.033: fraction of L intercepted 1.26e-02; swarm optical depth if at Mercury orbit 1.26e-02
   Venus solid 31 yr at end-to-end 0.054: fraction of L intercepted 7.76e-03; swarm optical depth if at Mercury orbit 7.76e-03

```

**D11. Two-layer binding energy.** U = integral of G m(r) dm / r for a core of radius r_c holding a fraction f_c of the mass and a
uniform mantle; reported as a ratio to the uniform sphere 3 G M^2 / (5 R), so the gravitational constant cancels (the script
uses 6.674 x 10^-11 only to form the ratio, a value not opened this session).

```
== D11. Two-layer Mercury binding energy (core radius 2,000 km, core mass fraction 0.70; [ME] F2) ==
   rc=1985 km fc=0.69: U=1.899e+30 J; ratio to uniform sphere 1.062 -> scaled from the brief's 1.79e30: 1.901e+30 J
   rc=2000 km fc=0.70: U=1.897e+30 J; ratio to uniform sphere 1.061 -> scaled from the brief's 1.79e30: 1.898e+30 J
   rc=2020 km fc=0.73: U=1.907e+30 J; ratio to uniform sphere 1.066 -> scaled from the brief's 1.79e30: 1.908e+30 J

```

**D12. Collector energy payback** = areal mass x processing energy / (S x cell efficiency); processing energies from [PR] 5 (16
kWh/kg bootstrapping set, 149 kWh/kg self-replicating factory).

```
== D12. Collector energy payback at Mercury's mean distance ==
   0.51 kg/m2,  16 kWh/kg, cell 0.20: 4 h
   0.51 kg/m2,  16 kWh/kg, cell 0.35: 3 h
   0.51 kg/m2, 149 kWh/kg, cell 0.20: 42 h
   0.51 kg/m2, 149 kWh/kg, cell 0.35: 24 h
   3.92 kg/m2,  16 kWh/kg, cell 0.20: 35 h
   3.92 kg/m2,  16 kWh/kg, cell 0.35: 20 h
   3.92 kg/m2, 149 kWh/kg, cell 0.20: 322 h
   3.92 kg/m2, 149 kWh/kg, cell 0.35: 184 h
   Si for a 10 um cell: 23.3 g/m2; regolith at 250 kg Si per t: 93 g/m2
   A&S mirror 3.92 kg/m2 at 1/3 of 9082.7 W/m2: 1.29 kg per kW; 120 W/kg array: 8.3 kg per kW
RD1: areal 0.510 kg/m2; DC at cells (0.35) 938 W/kg; delivered to grid 347 W/kg
RD2: areal 0.526 kg/m2; DC at cells (0.35) 909 W/kg; delivered to grid 202 W/kg
SPS-ALPHA DRM_5: 57.4 W/kg delivered; reflectors 2.2% of mass
SPS-ALPHA DRM_4: 42.4 W/kg delivered
1978 SPS 5 GW: 98-147 W/kg delivered
IKAROS membrane less tips: 66.3 g/m2
Venus Express: 193 W/m2 of array at Venus, 7.4% of 2601.3 W/m2
SP-413 refinery radiators: 5.99 kg/m2, 4.82 kg/kW
SP-428: waste 0.036 of total power
Parker: 5,900 W over ~4 m2 of radiator = 1475 W/m2 (both faces if two-sided)
```

## 6. Constraints for any inhabitant

Whoever lives or works at such an operation (human-shaped machines included) copes with the following; each is tied to a
finding above.

- **The launch and receiving sites are the hottest places in the system, not the collectors.** At Mercury the planet-side losses
  of a 31- to 1,000-year disassembly exceed the sunlight already falling on the surface by 3 to 1,300 times (F6, D8). Any site near
  a launcher or a beam receiver is a heat source to be shielded from, not a place to stand.
- **Shade and edge-on geometry are the working conditions in the collector field.** A black panel at Mercury's distance sits at
  490-610 K, a bare aluminum mirror at 700-785 K; only mirror-backed or white surfaces stay near room temperature (F1, D2). A
  human-shaped machine among collectors needs its own sunshade and radiator, as flown spacecraft do.
- **Planetary infrared adds to sunlight in low orbit.** MESSENGER's arrays were heated on both faces near Mercury and had to be
  pre-cooled before each pass (F1). Equipment in low orbit over a hot surface gets less rejection than in deep space.
- **Hardware degrades near the Sun, and temperatures creep upward with time.** Helios lost insulation performance perihelion by
  perihelion and lost array power; BepiColombo's cells lost 20% in a simulated month; a 300 kW design budgets 33% degradation (F1).
  Replacement is continuous work.
- **Night on Mercury's surface means storage measured in tonnes per kilowatt** (15-28 t/kW at the equator, 5-10 t/kW at the
  best polar point) (F5). Surface operations either sit at the poles, run from orbiting collectors by beam, or stop at night.
- **Power arrives by beam or not at all over distance.** Cable mass grows with the square of distance (F5); microwave receivers
  turn about 30% of what they receive into local heat (F2, D8); laser beams need apertures of hundreds of meters and nanoradian
  pointing ([NW] F8). Anyone working near a receiver is near a high-flux beam and its heat.
- **Electronics, magnets and dopants come from elsewhere.** The collectors' bulk (aluminum, silicon, glass) can be local; their
  electronics and some materials cannot (F7).

## 7. Candidate handwaves

Flagged plainly for the developer; none is accepted here.

- **H-1. A Mercury disassembly in 31, 100 or even 1,000 years with launchers on the surface.** Needs planet-side efficiency of at
  least 99.963%, 99.880% or 98.80% respectively for the losses merely to equal today's sunlight, against 96.4% (coil losses only)
  as the best sourced figure; otherwise the whole surface must radiate at 840-4,600 K (D8). The physics allows exporting the coil
  heat in hot payloads (about 400 K of extra payload temperature at 96.4%), but no source studies a launcher doing so.
- **H-2. Armstrong and Sandberg's 31-year schedule as an engineering result.** Their own assumptions place 10^23 to 10^24 W near
  Mercury at the end, nine-tenths as heat; radiated from Mercury that is an 18,000-21,000 K surface (D9). It works only if all
  processing and its heat happen in the swarm, off the planet, which the paper does not specify; it also assumes iron reflectors
  from a planet whose surface has 1-2% iron (F7).
- **H-3. Power beamed to a planet's surface at 10^19 to 10^21 W.** Rectennas at 78% followed by 90% DC-DC conversion would
  deposit about 3 x 10^18 to 3 x 10^20 W of heat on the surface (29.8% of what is received) (D8); no study sizes any interplanetary or planet-scale power link ([NW] F8).
- **H-4. Processing the whole of Mercury into products.** At sourced plant energies this is 11 to 99 times the binding energy
  (calc 3), with all of that heat to reject somewhere.
- **H-5. Solid Venus on any of the three timescales.** 4 x 10^-5 to 2.5 x 10^-2 of the Sun's output and 4 x 10^5 to 3.5 x 10^8
  W/m^2 of heat through Venus's surface (F6).
- **H-6. Collectors made entirely from Mercury or Venus.** Needs chips, dopants, polymer hydrogen and nitrogen, and III-V elements
  not shown to exist there in usable form (F7).
- **H-7. Equatorial surface power on Mercury through the 88-day night at scale.** 15-28 t of batteries per kW continuous (D6).
- **H-8. Launcher efficiency including the pulsed-power chain.** No sourced wall-plug figure; any figure above the 96.4% coil-only
  value is an assumption.

## 8. Open threads

- **Launcher pulsed-power efficiency, end to end** (bus to coils, including switching and storage): not found (row 78). Next:
  DTIC ADA192102 and ADA143778 (surfaced, not opened); UT-CEM compulsator reports; the papers Armstrong and Sandberg cite for
  coilgun and quenchgun efficiency (their refs 38-40).
- **Planet-side heat removal by any means other than surface radiation:** hot-payload export (D8 suggests it closes only for very
  efficient launchers), heat carried away by launched coolant, or launchers in orbit around the planet fed by tether or skyhook.
  No source found; this is the first thing to search next.
- **Sink temperature inside a dense swarm:** Wright 2023's optical-depth treatment is for the whole swarm; the radiator sink for
  elements inside a swarm of optical depth near 1 was not computed or found.
- **Degradation rates near the Sun:** MESSENGER and BepiColombo array degradation per year in flight (only the BepiColombo
  test figure in [ME] and the Helios qualitative account were found); the ICES paper "Parker Solar Probe Solar Array Cooling
  System In-Orbit Performance Review" (TTU repository, 403 both ways).
- **Hot-cell efficiency data:** Landis 2023 chapter (NTRS 20230002489, abstract only); INTA HTHI temperature coefficients
  (restricted); arXiv 2608.11113 (high-temperature PV for solar-electric Oberth maneuvers, surfaced, not opened).
- **Primaries not opened:** Dyson 1960 (Science) and 1966; Badescu 1995 (Acta Astronautica 36:135); Criswell 1986 (left to
  section 1); the full HTS cable paper (Sadeghi et al. 2024, open access); Ignatiev IAC-05 crawler paper (a ~200 kg crawler and
  "1 MW in several years" in a search summary).
- **Mercury trace elements for cells:** Ga, In, As, Ge, P, B abundances at Mercury's surface (not found; only CI-chondrite values
  in [PR]).
- **Venus's infrared absorptivity** if lit by a hot swarm instead of sunlight (D10 assumes ~1).
- **Heat capacity of silicate rock above 350 K** (D8 uses the 350 K Apollo value as a lower bound; real hot rock carries more).
- **Large-array specific power with flight mass:** iROSA wing mass (not published in what surfaced); the NASA SoA 2024 power
  chapter table (PDF not surfaced).

## 9. Rejected sources

- **Hobbyist and student coilgun pages** (coilgun.info, Menlo School, UCF senior design; 0.2-5% efficiency): not representative of
  engineered launchers; leads only.
- **Wikipedia (IKAROS, Helios), popular Dyson-sphere pages (Scientific American blog, magazines, Codidact, 3 Quarks Daily):**
  secondary; every number used was taken from the primary instead, or not used.
- **Trade press on Parker Solar Probe** (Electronic Specifier, pvbuzz, Design World): used only to record Conflict K3.
- **Search-engine summaries** whose numbers were not found on an opened page: Badescu radius formula; Dyson shell "2-3 m, 200
  g/cm^2"; C-C radiator 1.45 kg/m^2; Venus Express 821/1,468 W and -167 to +158 C; LDR "silicone 10 times lighter"; "1,000 t
  driver at 92%"; UCSB 5.3 kg/km line; "3.53 vs 6.43 kg/kWe". None used.
- **`dl/sla.pdf` from the interrupted run** (Woods et al., ITN Energy Systems, CIAS thin-film cells): URL and date not recorded;
  used only as a lead (row 4).
- **BYU cleanroom resistivity table** (2.82 x 10^-8 ohm m): likely film or alloy; recorded as Conflict K4, not used.
