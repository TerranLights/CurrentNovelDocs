# Benefits of mining and occupying Mercury: materials, energy, location and capability

*Research file, OOLSD library, eighth tranche (section 8). Started 2026-10-11; resumed and completed 2026-10-11 to 12 by a second
agent instance after a tool outage (log row 7). Physics and engineering only; no setting assumed. "Benefit" means a physically
grounded gain with its numbers and the conditions under which it holds, not advocacy.*

## 1. Scope

Mercury (surface, crust, polar cold traps, low orbit and its heliocentric neighborhood near 0.31 to 0.47 AU) as a source of
materials, energy, a launch site and a thermal resource, and what each of these is worth to which user at what delivery cost.
Composition, environment, launch and logistics are already sourced in the siblings [ME], [NW], [PR] and [IMS]; they are cited here, not re-derived.

## 2. SEARCH LOG

*(Spelling note: British spellings inside logged search strings and titles (for example, the British form of "aluminum"), are normalized to American spelling per the project rule; the searches were run as originally typed.) (Started 2026-10-11. Entries appended as searches are run. Sibling files read first, read-only: `_BRIEF.md`, `starlifting_synthesis.md`, `inner_system_mining_synthesis.md`, `mercury_as_industrial_site.md`, `inner_system_logistics_network.md`, `space_processing_and_fabrication.md`, `lagrange_thermal_environment.md`.)*

| # | Date | Search string (verbatim) or page opened | Result | Notes |
|---|---|---|---|---|
| 1 | 2026-10-11 | Read (allowed, read-only) siblings: `mercury_as_industrial_site.md` [ME] in full; `inner_system_mining_synthesis.md` [IMS]; `starlifting_synthesis.md` [SYN] sections 0-3; `space_processing_and_fabrication.md` [PR] findings 1-7; `inner_system_logistics_network.md` [NW] F3-F4 | useful | Composition, environment, launch, logistics already sourced there; cited, not re-derived |
| 2 | 2026-10-11 | `USGS Mineral Commodity Summaries 2026 magnesium metal price world production` | useful | Located the MCS 2026 per-commodity PDFs |
| 3 | 2026-10-11 | Pages (curl + pdftotext): USGS MCS 2026 sheets for magnesium metal, aluminum, silicon, sulfur, titanium, nickel, lime, graphite, salt, potash, soda ash, iron and steel, iron ore (pubs.usgs.gov/periodicals/mcs2026/mcs2026-<name>.pdf, Feb 2026) | useful | World production, 2025 prices and end-use splits (F1b). Two guessed file names (`iron-and-steel`, `iron_and_steel`) returned HTML: dead at the query (wrong URL), right name `iron-steel` |
| 4 | 2026-10-11 | `International Aluminum Institute primary aluminum smelting power consumption kWh per metric ton 2024 statistics` | thin | Located the IAI statistics pages |
| 5 | 2026-10-11 | Page (WebFetch, then curl): IAI "Primary Aluminum Smelting Energy Intensity" (international-aluminum.org and archive.international-aluminum.org/?p=1745) | dead at the source | Definitions only; the numbers are rendered by script and absent from the page text |
| 6 | 2026-10-11 | `"kWh/t" world average primary aluminum smelting AC power consumption 2023 IAI "14," Hall-Heroult` | dead (tool) | **WebSearch and WebFetch both returned "session limit, resets 11:40 pm" at 21:48 local.** From here until the reset, searches were run against public bibliographic APIs by curl (NASA NTRS API, arXiv API, Crossref API, OSTI API), and pages were opened by curl + pdftotext. Each query string is logged verbatim with the API named |
| 7 | 2026-10-11 | *(Resumed 23:41 local by a fresh agent instance after the tool reset; siblings re-read in full: [ME] all sections, [IMS], [SYN] §0-2, [PR] §1 and §5 table, [NW] F3 and F8, [LT] `lagrange_thermal_environment.md` 3D-3G.)* WebSearch restored | useful | |
| 8 | 2026-10-11 | `International Aluminum Institute primary aluminum smelting power consumption 2024 kWh/t world average` | thin | Search summary claimed "12.5-12.9 kWh/t" world average: a unit error (the industry figure is per kg, i.e. MWh per t). **Not used.** |
| 9 | 2026-10-11 | Page (WebFetch): international-aluminum.org/statistics/primary-aluminum-smelting-power-consumption/ | dead at the source | Second IAI page that renders its numbers by script; definitions only (third attempt at IAI, see rows 4-5) |
| 10 | 2026-10-11 | `Hall-Héroult cell specific energy consumption "13" "MWh/t" aluminum theoretical minimum 6.3 kWh/kg review paper` | useful | Led to the Frontiers in Chemistry review; patent hits not used |
| 11 | 2026-10-11 | Page (WebFetch): Wu, Xie, Hao et al., "Ionic liquids as electrolytes in aluminum electrolysis", Front. Chem. 10:1014893 (3 Nov 2022) | useful | Hall-Héroult 13-15 kWh/kg Al, >950 C, efficiency <=50%; theoretical minimum 6.23 kWh/kg; Table 3 gives 13,000-19,000 kWh/t |
| 12 | 2026-10-11 | Page (curl): corpora.tika.apache.org govdocs1 233644.pdf (a DOE aluminum energy report, per the search listing) | dead at the source | Download produced no file |
| 13 | 2026-10-11 | Local: pdftotext of the 14 USGS MCS 2026 sheets downloaded in row 3; extracted world production, 2025 prices and end-use statements | useful | F1b. The cobalt sheet was also downloaded (row 3 omitted it) |
| 14 | 2026-10-11 | `Jones "The Recent Large Reduction in Space Launch Cost" ICES 2018 NTRS cost per kg Falcon Heavy` | useful | |
| 15 | 2026-10-11 | Page (curl + pdftotext): NTRS 20200001093, H. W. Jones (NASA Ames), "The Recent Large Reduction in Space Launch Cost", ICES-2018-81 (8 Jul 2018) | useful | Falcon 9 $2,720/kg, Falcon Heavy $1.4k/kg to LEO; 1970-2000 average $18.5k/kg; shuttle $54.5k/kg |
| 16 | 2026-10-11 | Page (curl + pdftotext): arXiv 2011.15066, Beuthe et al. 2020 (GRL), §2.1 | useful | Pore-free crustal density 2,785-3,149 kg/m^3, average 2,957; mantle 3,200 kg/m^3 at the crust-mantle boundary (model input) |
| 17 | 2026-10-11 | Page (curl + pdftotext): arXiv 1712.02187, Nittler, Chabot, Grove, Peplowski 2018 [NIT18], §2.4 and §2.6, Tables 2.2, 2.3 | useful | Pre-melting mantle oxides (NSP and IcP-HCT mass balances); bulk model inputs (core r 2,020 km, 6,980 kg/m^3; silicate shell 3,380 kg/m^3; +1 wt% Fe, +7 wt% S) |
| 18 | 2026-10-11 | `silicon metal submerged arc furnace specific electrical energy consumption MWh per metric ton Si carbothermic reduction quartz paper` | useful | |
| 19 | 2026-10-11 | Page (curl + pdftotext): Machulec, Bialik, Gil, "Relation between active power of the submerged arc furnace and the electric energy consumption indicator in the process of ferrosilicon smelting", Arch. Metall. Mater. 64(2):633-638 (2019) | useful | FeSi75: energy indicator "should not exceed 8 MWh/Mg" |
| 20 | 2026-10-11 | Page (WebFetch): hrcak.srce.hr 347941, Kozłowski et al., Metalurgija (2026), FeSi75 six-electrode furnace | thin (not used) | Abstract gives only a ~120 kWh/Mg improvement, no total |
| 21 | 2026-10-11 | `metallurgical grade silicon production "11-13 MWh" OR "12 MWh" OR "11–13 MWh" per metric ton electricity submerged arc furnace` | useful | |
| 22 | 2026-10-11 | Page (curl): NREL fy25osti/89464.pdf (two URL forms) | dead at the source | No file returned (redirect or block) |
| 23 | 2026-10-11 | Page (curl): Ksiazek, Tangstad, Ringdalen, "Five furnaces five different stories", *Silicon for the Chemical and Solar Industry XIII* (Kristiansand, June 2016), p. 41 (NTNU FlippingBook HTML) | useful | Si process "requires temperature above 1800 C hence electrical energy consumption in the order of 11-13 MWh per ton", citing Schei et al. |
| 24 | 2026-10-11 | `electrolytic magnesium production MgCl2 electrolysis energy consumption kWh per kg Mg cell 13 kWh peer-reviewed review` | thin | Lab cells only; no industrial plant figure |
| 25 | 2026-10-11 | Page (WebFetch): avesis.metu.edu.tr record, Demirci and Karakaya, "Molten Salt Electrolysis of MgCl2 in a Cell with Rapid Chlorine Removal Feature", TMS Magnesium Technology 2012 | useful | 7.0 kWh/kg Mg achieved (lab); theoretical minimum 6.2 kWh/kg Mg |
| 26 | 2026-10-11 | `solar power satellite near Mercury orbit concept beamed power inner solar system Dyson swarm statite paper energy Landis OR Criswell` (extended mode) | thin | Mostly popular pages and a fan wiki (not used); two papers located (rows 27, and Harrop and Schulze-Makuch 2010, IJAsB 9:89, not opened) |
| 27 | 2026-10-11 | Page (curl + pdftotext): arXiv 2109.11443, J. Smith (undergraduate, Edinburgh), "Viability of a Dyson Swarm as a Form of Dyson Sphere" (physics.pop-ph, 20 Sep 2021), §2.1 | thin (low weight; used only for its qualitative Mercury-vs-Mars reasoning) | Prefers Mars over Mercury on heat and access; its "23 times larger" collector-area ratio for Mars vs Mercury is wrong (inverse-square from NSSDC distances gives 15.5: Rejected sources) |
| 28 | 2026-10-11 | `Geisz 2020 Nature Energy six-junction III-V solar cell 47.1% efficiency 143 suns concentration AM1.5D arXiv OR NREL` | useful | |
| 29 | 2026-10-11 | Page (WebFetch): nrel.gov press release on the six-junction cell | dead at the source | DNS failure (ENOTFOUND) |
| 30 | 2026-10-11 | Page (WebFetch): RePEc record of Geisz et al., Nature Energy 5(4):326-335 (Apr 2020) | useful | 47.1% under 143 suns (direct spectrum); 39.2% at 1 sun global; single-junction flat plates limited to about 30% |
| 31 | 2026-10-11 | `NASA solar dynamic power Brayton ground test demonstration 2 kW efficiency space station solar concentrator NTRS` | useful | |
| 32 | 2026-10-11 | Page (curl + pdftotext): Shaltens and Mason, "Early Results From Solar Dynamic Space Power System Testing", NASA TM-107252 (Jul 1996), NTRS 19960047096 | useful | 2 kWe closed-Brayton ground demo in vacuum with simulated Sun: engine 21.5-26.4%, Sun-to-user 13.8-16.1%; concentrator facets >85% reflective, ~2.5 kg/m^2; receiver stores heat in LiF-CaF2 melting at 1,041 K |
| 33 | 2026-10-11 | `Mercury surface power heat engine permanently shadowed crater cold sink thermoelectric OR Stirling concept polar lander power study` (extended mode) | useful | One Mercury-specific concept found (row 34); Wikipedia and a NASA SVS page not used |
| 34 | 2026-10-11 | Page (curl + pdftotext): Stoica, Ingham, Tamppari, Mitchell, Quadrelli (JPL), "TransFormers for Extreme Environments", NIAC Phase I Final Report (May 2014), NTRS 20180008682, §2.4.2 | useful | Mercury north-pole scenario: reflector on a sunlit rim (~550 K) beams sunlight into a crater floor at 80-350 K; needs ~300 W/m^2 delivered 10-20 km; 300 W rover alternative is an RTG rejecting ~2 kW of heat. **ENGINEERING-STUDIED (Phase I concept)** |
| 35 | 2026-10-11 | `"Mercury" polar crater rim sunlit "temperature difference" power generation thermoelectric heat engine cold trap ISRU paper` | thin | No paper that uses the hot-ground/cold-trap difference at Mercury for power; leads to a 1977 Mercury-orbiter thermoelectric study (row 36) and lunar regolith thermal-storage work (not opened) |
| 36 | 2026-10-11 | Page (curl + pdftotext, OCR-quality scan) and NTRS API record: NTRS 19780016702, "Solar Thermoelectric Generators" (study for a Mercury-orbiter power source; publication date 29 Jul 1977) | useful | Silicon-germanium STG sized for 300 W at 0.45 AU: about 20 W at Earth, over 900 W at 0.30 AU; optimum specific power about 11-12 W/lb at a ~550 C difference. **ENGINEERING-STUDIED (never flown)** |
| 37 | 2026-10-11 | `Parker Solar Probe mission design launch C3 154 km2/s2 seven Venus gravity assists perihelion 9.86 solar radii trajectory paper` | useful | Wikipedia and CNES pages not used |
| 38 | 2026-10-11 | Page (curl + pdftotext): Guo, McAdams, Ozimek, Shyong (APL), "Solar Probe Plus Mission Design Overview and Mission Profile", ISSFD 24 (2014) | useful | Max launch C3 154 km^2/s^2; seven Venus flybys; 6.4 yr from launch to the first 9.86 R_sun perihelion; final orbit 9.86 R_sun x 0.73 AU, 88-day period |
| 39 | 2026-10-11 | Local Python `calc/c1_nearsun.py`: v-infinity and burns to lower perihelion from Earth vs Mercury, solar escape (D3) | useful | **Result cuts against the premise:** Mercury is cheaper only for perihelia down to about 0.1 AU; to reach a few solar radii it is costlier than Earth unless departure is at Mercury's aphelion |
| 40 | 2026-10-11 | `vulcanoid search STEREO Heliospheric Imager upper limit diameter km Steffl 2013 Icarus no vulcanoids found` | useful | |
| 41 | 2026-10-11 | Page (curl + pdftotext): arXiv 1301.3804, Steffl, Cunningham, Shinn, Durda, Stern, "A Search for Vulcanoids with the STEREO Heliospheric Imager" (Icarus, 2013) | useful | Vulcanoid zone 0.07-0.21 AU; no vulcanoids larger than 5.7 km (3 sigma); a 100 km pure-iron body at 0.06 AU evaporates in <4.5 Gyr |
| 42 | 2026-10-11 | `space sunshade made from lunar or asteroid material L1 mass Bewick McInnes 2012 OR Angel 2006 PNAS "20 million tons" sunshade flyers` | useful | Wikipedia and NSS pages not used |
| 43 | 2026-10-11 | Page (WebFetch): PMC1859907, R. Angel, "Feasibility of cooling the Earth with a cloud of small spacecraft near the inner Lagrange point (L1)", PNAS 103(46) (3 Nov 2006) | useful | 1.8% of flux; 4.7 x 10^6 km^2; 4.2 g/m^2; 20 Mt (23 Mt with losses); gram-scale flyers; $50/kg transport target; **explicitly launched from Earth, not made from lunar or asteroid material** |
| 44 | 2026-10-11 | Page (WebFetch): Strathprints 41028 abstract, Bewick, Sanchez Cuartielles, McInnes, "Gravitationally bound geoengineering dust shade at the inner Lagrange point", Adv. Space Res. 50(10):1405-1410 (2012) | useful | Captured-asteroid-anchored dust cloud: up to 6.58% insolation reduction; 1.7% needed to offset 2 C; largest NEAs lack the mass alone |
| 45 | 2026-10-11 | `Venus sunshade terraforming L1 mass sunshade material sourced from Mercury paper OR "Mercury" solar collector swarm material study Armstrong Sandberg "Eternity in six hours" Mercury disassembly numbers` (extended mode) | thin | No concept sources a sunshade from Mercury. Summary's "245 g/m^2" for the Mercury swarm is **wrong** (the paper says 3.92 kg/m^2, row 47); a Venus sunshade "7.6 x 10^10 kg" was not traced to an opened primary (not used) |
| 46 | 2026-10-11 | Pages (curl): aleph.se and truevaluemetrics.org copies of Armstrong and Sandberg | dead at the source | aleph.se site closed; the other returned an HTML stub |
| 47 | 2026-10-11 | Page (curl + pdftotext): Armstrong and Sandberg, "Eternity in six hours: intergalactic spreading of intelligent life and sharpening the Fermi paradox", preprint submitted to Acta Astronautica (12 Mar 2013), §4.1-4.2 (flightfromperfection.com copy) | useful | Swarm at Mercury's semi-major axis: area 4.21 x 10^22 m^2; 50% of Mercury's mass gives 3.92 kg/m^2 (0.5 mm of iron); 1/3 captor efficiency; 1/10 of power to mass drivers; 31 yr 85 d; "unlikely to be attempted". Assumes "30% silicate and 70% metal, mainly iron or iron oxides" |
| 48 | 2026-10-11 | `Sandberg 1999 "The physics of information processing superobjects" Jupiter brains Matrioshka brain heat dissipation temperature Landauer limit` | useful | Wikipedia and popular pages not used |
| 49 | 2026-10-11 | Page (curl + pdftotext): A. Sandberg, "The Physics of Information Processing Superobjects: Daily Life Among the Jupiter Brains", J. Evolution and Technology 5(1):1-34 (Dec 1999), §6, §6.3, §10.2 | useful | Bit erasure costs k_B T ln 2 (2.9 x 10^-21 J at room temperature); shell efficiency 1 - T_u/T_shell; the bit-erasure-maximizing shell radius for the Sun is 6.8 x 10^14 m (629 light-hours), "far too large to be practical"; feasible shells "either use most of their energy for cooling, or beam the concentrated energy out"; unshielded object at 1 AU works at 395 K. **SPECULATIVE (exploratory physics)** |
| 50 | 2026-10-11 | `Google "Project Suncatcher" space-based AI compute constellation paper arXiv 2025 radiation testing TPU launch cost $200/kg` | useful | Trade press not used |
| 51 | 2026-10-11 | Page (WebFetch): Google Research blog, "Exploring a space-based, scalable AI infrastructure system design" (Agüera y Arcas et al., 4 Nov 2025) | useful (company research post; the preprint itself not opened) | Panel "up to 8 times more productive than on earth" in a dawn-dusk sun-synchronous orbit at 650 km; launch "less than $200/kg by the mid-2030s" (projection); TPU HBM irregularities after 2 krad(Si), no hard failure to 15 krad(Si); 750 rad(Si) expected in 5 yr shielded |
| 52 | 2026-10-11 | `BepiColombo science objectives Mercury origin and evolution planet close to parent star magnetic field core test of general relativity ESA` | useful | |
| 53 | 2026-10-11 | Page (WebFetch): ESA, "BepiColombo: Science objectives" (esa.int; no page date shown) | useful | Seven objectives verbatim (origin near the parent star, interior, internal field, surface processes and polar deposits, exosphere, magnetosphere, general relativity) |
| 54 | 2026-10-11 | `Mercury hollows Blewett 2011 Science "hollows" volatile loss sublimation sulfides MESSENGER unique landform abstract` | useful | Popular pages not used |
| 55 | 2026-10-11 | Page (WebFetch): repository.si.edu record of Blewett et al. 2011 | dead at the source | HTTP 403 |
| 56 | 2026-10-11 | Page (WebFetch): DLR elib 73581, Blewett et al., "Hollows on Mercury: MESSENGER Evidence for Geologically Recent Volatile-Related Activity", Science 333:1856-1859 (2011) | useful | Hollows tens of meters to a few km across, high-reflectance interiors and halos; volatile-related origin |
| 57 | 2026-10-11 | `lunar sulfur concrete NASA Grugel Toutanji compressive strength sulfur content percent regolith simulant waterless concrete NTRS` | useful | Wikipedia not used |
| 58 | 2026-10-11 | Page (curl + pdftotext): Toutanji and Grugel, "Performance of 'waterless concrete'", NTRS 20090033079 (UAH / NASA MSFC, 2008) | useful | Sulfur concrete 12-22 wt% S commercially; sulfur melts ~119 C, mixed at 130-140 C, so it must stay below sulfur's melting point; 35 MPa non-cycled vs 7 MPa after cycling to liquid nitrogen; lunar soils 474-794 µg S/g; S extractable by heating soil above 1,100 C in vacuum |
| 59 | 2026-10-11 | `low-iron solar glass Fe2O3 content percent transmittance photovoltaic cover glass iron oxide absorption study` | thin | Patents only; the summary's 0.01 vs 0.1 wt% Fe2O3 transmittance figures were not found in the patent opened (row 60). **Not used** |
| 60 | 2026-10-11 | Page (WebFetch): Google Patents US8664132B2, "High transmittance glass" (PPG / Vitro, 4 Mar 2014) | dead at the source (for the figure sought) | No low-iron vs conventional comparison in the text |
| 61 | 2026-10-11 | Pages (curl): NASA NSSDCA Earth (15 Nov 2024), Moon (11 Jan 2024) and Mercury (11 Jan 2024) fact sheets | useful | Escape 11.186 / 2.38 / 4.3 km/s; Mercury solar irradiance 9,082.7 W/m^2 (6.674 x Earth), black-body temperature 439.6 K vs Earth 254.0 K; Mercury GM 0.022032 x 10^6 km^3/s^2 |
| 62 | 2026-10-11 | Local Python `calc/c2_benefits.py` (D1-D11) and `calc/c3_compute_temp.py` (D12) | useful | Inventories, value framing, Earth-to-Mercury mass ratio, collector power per kg, industry power, carbon limit, sulfur ratio, ice draw-down, Carnot and radiator sinks, Landauer per area. **Self-check:** the stoichiometric oxygen balance (449 kg/t) plus the listed elements (563 kg/t) closes to 1,012 kg/t, within the composition uncertainty |
| 63 | 2026-10-11 | **Second-angle pass (LAW 0-R) begins.** `IEA aluminum tracking electricity intensity primary aluminum smelting kWh per metric ton global average 2022` | (see next row) | Re-query of row 8-11 (aluminum energy) from another publisher |
| 64 | 2026-10-11 | (result of row 63) | thin | Summary's "13,990 kWh/t" world average was attributed to IAI but no page carrying it was opened (**not used**); IAI GHG pages and trade press not opened |
| 65 | 2026-10-11 | Page (curl + pdftotext): Hasanbeigi, Springer, Shi, "Aluminum Climate Impact: An International Benchmarking of Energy and CO2 Intensities", Global Efficiency Intelligence for BlueGreen Alliance (Feb 2022), §4.1 Fig. 7 | thin | Smelter energy intensities for 12 countries (2019) are only in a bar chart (axis 0-18 kWh/kg); "does not vary a huge amount between the countries"; no number extractable. Second angle on aluminum energy died at the source |
| 66 | 2026-10-11 | `delta-v required to reach the Sun from Earth orbit cancel Earth's orbital velocity 29.8 km/s solar impact mission design harder than solar escape NASA` | thin (secondary only) | Forums and a university Q&A page: "cancel about 24 km/s", outward-then-inward and Venus flybys cheaper. Qualitatively consistent with D3; no primary; numbers not used |
| 67 | 2026-10-11 | `NTRS OR AIAA OR JBIS "Mercury" industrialization OR "Mercury base" solar energy export laser beaming propulsion "inner solar system" power station study` (extended mode; second angle on rows 26 and [ME] row 88) | thin | Still no Mercury power-export or industrialization study; one near-Sun laser idea (row 68) |
| 68 | 2026-10-11 | Page (curl + pdftotext): L. Johnson (NASA MSFC) and E. Montgomery, "From Solar Sails to Laser Sails" (talk, 15 Dec 2017), NTRS 20170012350 | thin (concept slide) | "Laser in low Solar orbit ... Located near sun, laser would enjoy ample power harnessed from solar energy"; status "To Be Determined - Much study needed". **SPECULATIVE** |
| 69 | 2026-10-11 | Page (curl + pdftotext): Millis, Greason, Stevenson, "Breakthrough Propulsion Study", NASA grant NNX17AE81G first-year report, NTRS 20180006480 | dead at the source | No Mercury or near-Sun power content (the search summary's sentence came from row 68) |
| 70 | 2026-10-11 | `industrial magnesium electrolysis plant energy consumption "kWh/kg" Mg anhydrous MgCl2 cell 10-12 kWh life cycle assessment magnesium production comparison Pidgeon electrolytic` (second angle on rows 24-25) | useful | Lab-cell figures repeated; one whole-plant figure (row 71) |
| 71 | 2026-10-11 | Page (WebFetch): Google Patents US9499880B2, Battelle, "System and process for production of magnesium metal and magnesium hydride from magnesium-containing salts and brines" (22 Nov 2016), background section | useful (patent background; secondary for the plant figure) | US Magnesium plant "requires 44 kWh/kg of energy at a production cost of $3.31/kg"; ARPA-E METALS targets 27 kWh/kg and $2/kg |
| 72 | 2026-10-11 | Search log closed for this pass; writing sections 3-9. Totals: 72 rows (28 searches, 37 pages opened, 7 local, sibling or bookkeeping rows). **Dead ends: 10** (rows 5, 9, 12, 22, 29, 46, 55, 60, 69 died at the source; row 6 died at the tool). **Thin or not used: 14** (rows 4, 8, 20, 24, 26, 27, 35, 45, 59, 64, 65, 66, 67, 68); in rows 8, 45, 59 and 64 a search summary gave a number that no opened page confirmed; the numbers in rows 8 and 45 were wrong, as was one figure in the opened preprint of row 27 | — | |

## 3. Findings

Source tags are expanded in the **Source key** at the end of this section. Sibling tags: **[ME]** `mercury_as_industrial_site.md`,
**[NW]** `inner_system_logistics_network.md`, **[PR]** `space_processing_and_fabrication.md`, **[LT]** `lagrange_thermal_environment.md`,
**[IMS]** `inner_system_mining_synthesis.md`, **[SYN]** `starlifting_synthesis.md`. D-numbers are in section 5.
Evidence words: **DEMONSTRATED** (flown, built or measured), **ENGINEERING-STUDIED** (a quantitative design or test-backed study),
**SPECULATIVE** (thought experiment or concept without a design).

**The answer in brief.**

1. **Mercury's material benefits are real but local.** The crust holds 0.5 to 2 x 10^21 kg each of silicon, magnesium and aluminum and
   about 10^20 kg of sulfur and carbon (D1), all at the bottom of a shallow gravity well (escape 9.0 MJ/kg against Earth's 62.6).
   On Earth these are cheap commodities ($0.09 to $15 per kg, F1b); their value off Earth is set by the cost of not launching them from
   Earth (now $1,400 to $2,720 per kg to low Earth orbit, 93 to 30,000 times their Earth price, D3) and, at Mercury, by the
   19.5-to-1 propellant ratio of shipping from Earth orbit to low Mercury orbit by direct chemical transfer (D4). **None of this makes Mercury an
   exporter to Earth**: [IMS] shows that leg fails at scale. The benefits hold for use at Mercury or nearby.
2. **Energy is the strongest benefit.** Sunlight is 4.6 to 10.6 times Earth's (6.67 mean), so a collector of fixed mass yields 6.67
   times the power (D6). A 1 Mt/yr aluminum, silicon or magnesium industry needs 0.8 to 5 GW of continuous power, which takes
   0.4 to 2.8 km^2 of 20%-efficient collectors in space near Mercury against 2.9 to 18 km^2 at 1 AU (D7). The catch: arrays must run
   hot and off-normal ([ME] F6), and the surface has 88-day nights at the equator.
3. **Mercury is not a better base for reaching the Sun itself.** Its orbital speed must be cancelled to fall inward, so reaching a
   few solar radii costs more from Mercury (v-infinity 25 to 40 km/s) than from Earth (21 to 27 km/s) unless departure is at
   Mercury's aphelion, where it is about equal (D2). Mercury is cheaper only for targets down to about 0.1 AU, and the vulcanoid zone
   (0.07 to 0.21 AU) holds no known body larger than 5.7 km (F3).
4. **The thermal benefit is mostly "absence of hot ground", not "presence of a cold sink".** A 300 K radiator rejects 411 W/m^2 into
   a polar-shadow sink and 413 W/m^2 into deep space, but nothing into equatorial daylight (D11). Cold traps help where heat must be
   dumped near hot ground; the large Carnot ratios (0.82 to 0.90) need radiators at 100 K, which reject only about 5 W/m^2.
5. **Computation and megastructures near the Sun are bounded by heat.** Per square meter of collector a near-Sun computer can
   erase about 4 times more bits than at 1 AU (D12), but it runs at 530 to 630 K and the bit-erasure-optimal shell for the whole Sun
   lies at 6.8 x 10^14 m, far outside the planets ([SAN99]). Mercury is the material-efficient place; it is not the energy-efficient one.

### F1. Materials: what the surface and interior hold, and what each product is worth

**F1a. Amounts.** Surface grades are from [ME] F1 and D1 (MESSENGER XRS, GRS); per-metric-ton values multiply wt% by 10. Whole-crust
figures **assume the surface composition holds through the crust** (not measured; the crust is volcanic and laterally variable,
[ME] F2).

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Crustal density (pore-free surface rock) | 2,785 to 3,149 kg/m^3, average 2,957 kg/m^3; mantle 3,200 kg/m^3 at the crust-mantle boundary (model input) | [BEU20] §2.1 | Primary | [NIT18] silicate shell 3,380 kg/m^3 (whole shell, model input) | Medium-high |
| Crust mass | 4.4 x 10^21 kg (20 km) / **7.6 x 10^21 kg (35 km)** / 1.08 x 10^22 kg (50 km); 1.3 to 3.3% of Mercury's mass (D1) | D1 from [BEU20], [ME] F2 thickness 20-50 km | Derived | none | Medium |
| Regolith mass, whole planet | 4.6 x 10^17 kg (3.7 m) to 5.7 x 10^17 kg (4.6 m) to 5.0 x 10^18 kg (40 m), at an **assumed** lunar density of 1,660 kg/m^3 (D1) | D1 from [ME] F3 depth conflict; density assumption from [IMS] §3 | Derived | none | Low (density and depth both uncertain) |
| Top 1 km of rock | 2.2 x 10^20 kg (D1) | D1 | Derived | none | Medium |
| Elements in a 35 km crust (surface grades assumed) | Si 1.9 x 10^21; Mg 8.4 x 10^20; Al 5.1 x 10^20; Ca 3.1-4.6 x 10^20; Na 2.2 x 10^20; S 1.5-1.8 x 10^20; Fe 1.0-1.5 x 10^20; C 1.1 x 10^20; Ti 2.3 x 10^19; Cl 1.1 x 10^19; K 1.0 x 10^19 kg (D1) | D1 | Derived | none | Medium-low (assumption flagged) |
| Oxygen at the surface | **~450 kg/t** if Si, Mg, Al, Ca, Na and Ti are fully oxidized (stoichiometric balance; closes the mass to 1,012 kg/t); GRS O/Si 1.2 gives **~300 kg/t**, which [NIT18] treat cautiously as possible smelting-like alteration (D2) | D2 from [ME] F1 | Derived | [NIT18] §2.3.3: stoichiometry predicts O/Si ~1.7 | Medium (the two bases differ by 1.5 times; see Conflicts K2) |
| Silicate shell (crust plus mantle), model | 8.9 x 10^22 kg (r_core 2,020 km, 6,980 kg/m^3; shell 3,380 kg/m^3); from the average of the two pre-melting mantle estimates plus 1 wt% Fe and 7 wt% S: Si 22.8 wt% (2.0 x 10^22 kg), Mg 20.8 wt% (1.85 x 10^22 kg), Al 2.2 wt% (1.9 x 10^21), Ca 2.0 wt% (1.8 x 10^21), Na 1.1 wt% (1.0 x 10^21), S 7 wt% (6.2 x 10^21), Fe 1 wt% (8.9 x 10^20), O 42.9 wt% (3.8 x 10^22 kg) (D1) | [NIT18] §2.4, §2.6, Table 2.2; D1 | Primary model, derived arithmetic | NSSDC total mass 3.3010 x 10^23 kg; the model sums to 3.300 x 10^23 | Medium-low (the 7 wt% S is a mantle prediction, Namur 2016, via [NIT18]) |
| Mantle is magnesium-rich, crust is the aluminum source | Pre-melting mantle MgO 36.9-37.6 wt% and Al2O3 4.2-4.6 wt%; surface lavas Al2O3 8.8-13.8 wt% (NSP highest) | [NIT18] Table 2.2 | Primary | [ME] F1 surface Al/Si 0.268 | Medium. **For aluminum the crust is the richer source; for magnesium the mantle (400 km thick) is** |
| Core | 2.3 to 2.4 x 10^23 kg, 69 to 73% of the planet, Fe 75-95 wt%, Ni ~5 wt% (assumed), 420 to 470 km down | [ME] F2, D2; [NIT18] Table 2.3 | Primary / derived | sibling | High that it is unreachable by surface mining ([ME] F2: no study of reaching it) |
| Polar water ice | 2.1 x 10^13 to 1.4 x 10^15 kg (MESSENGER range); upper limit ~3 x 10^15 kg | [ME] F5 | Primary (via sibling) | [ME] K9 | Medium (thickness unknown) |
| Polar ice lifetime at a stated draw | At 1 Mt/yr: 21,000 to 3,000,000 years; at 100 Mt/yr: 210 to 30,000 years (D10). Present-day delivery ~1.8 x 10^4 kg/yr is negligible ([ME] F5) | D10 | Derived | none | Medium (inventory uncertain about 100 times) |

**F1b. Industrial value and end uses on Earth (USGS Mineral Commodity Summaries 2026, February 2026).** These are Earth prices, given
so the scale of value is visible; **an Earth commodity price is not the value of the same material in space** (see F1c and D3).

| Product | 2025 price (as stated) | 2025 world production | Main end uses (as stated) | Source | Confidence |
|---|---|---|---|---|---|
| Aluminum (primary) | U.S. ingot 180 c/lb (about $3.97/kg; a 39% rise over 2024 under 25-50% tariffs) | 74.0 Mt (2024: 72.8) | U.S.: transportation 36%, packaging 24%, building 13%, electrical 9%, consumer durables 8%, machinery 8% | [USGS-Al] | High (price is U.S.-specific and tariff-inflated) |
| Magnesium metal | Europe $2,500/t; U.S. spot $3.20/lb | 1.10 Mt (2024: 1.08) | U.S. primary use: castings 69% (mostly automotive), aluminum alloys 15%, desulfurization of iron and steel 9% | [USGS-Mg] | High |
| Silicon | Silicon metal 130 c/lb (about $2.87/kg); ferrosilicon 75% 140 c/lb Si | Si metal 4.6 Mt (2025), ferrosilicon 5.0 Mt Si content | Ferrosilicon to steel and foundries; silicon metal to aluminum alloys and silicones; refined further to polysilicon (semiconductor and solar grade) | [USGS-Si] | High |
| Titanium | Sponge $12/kg; TiO2 pigment $3,200/t | Sponge 0.37 Mt | Metal mostly aerospace; pigment to paints, plastics, paper | [USGS-Ti] | High |
| Sulfur | $180/t (U.S. f.o.b.; 2024: $46) | 84 Mt | About 90% consumed as sulfuric acid | [USGS-S] | High (price volatile) |
| Nickel | LME $15,000/t | 3.9 Mt | (not needed here) | [USGS-Ni] | High |
| Lime | Quicklime $260/t | 420 Mt | (steel, chemicals) | [USGS-lime] | High |
| Graphite (natural) | Flake imports $1,000/t | 1.8 Mt | (refractories, batteries) | [USGS-gr] | High |
| Salt / soda ash / potash | Vacuum-pan salt $260/t; soda ash $150/t; potash $1,200/t K2O | 270 Mt / 71 Mt / 49 Mt K2O | (soda ash is a glass raw material) | [USGS-salt], [USGS-soda], [USGS-K] | High |
| Iron ore / steel | Iron ore $89/t (U.S. mine unit value) | 2,600 Mt ore; 1,900 Mt raw steel | — | [USGS-FeO], [USGS-FeSt] | High |

**F1c. What changes off Earth, and what is specific to Mercury's material.**

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Launch cost to low Earth orbit | Falcon 9 $2,720/kg; Falcon Heavy $1.4k/kg; 1970-2000 average $18.5k/kg (2018 dollars) | [JON18] | Primary (NASA Ames paper) | Google projection: "less than $200/kg by the mid-2030s" [GOO25] (a forecast) | High for the 2018 figures; low for the projection |
| Launch cost relative to Earth price | Aluminum 353-685x; magnesium 560-1,088x; silicon metal 488-949x; titanium sponge 117-227x; sulfur 7,800-15,100x; even at a projected $200/kg, 13x (nickel) to 2,200x (iron ore) (D3) | D3 | Derived | none | High (arithmetic); the conclusion that **in-space value is set by avoided transport, not by Earth price** follows directly |
| Earth-orbit mass per kg placed in low Mercury orbit | Direct impulsive chemical (Isp 450 s **assumed**; Palaszewski's Mercury landers use 480 s, [ME] F12): 13.10 km/s (5.55 departing LEO + 7.55 capture), propellant mass ratio **19.5** before any stage mass; with Venus and Mercury flybys (~2.8 km/s, ~4.2 yr) about **1.9** (D4) | D4 from [NW] C1, [IMS] §5 | Derived | [IMS]: flyby routes trade propellant for years | Medium (no stage mass; real vehicles are worse) |
| Escape energy | Mercury 9.03 MJ/kg (2.51 kWh/kg), Earth 62.56 MJ/kg (17.4 kWh/kg), Moon 2.83 MJ/kg (0.79 kWh/kg) (D5) | D5 from [NSSDC] | Derived | [ME] F8: 9.0 MJ/kg | High |
| Carbon as an in-place reductant | Graphite ~14 kg/t (to ~50 kg/t in low-reflectance material, [ME] F1). Carbothermal silicon needs 0.855 kg C per kg Si, so in-place carbon could reduce at most **16 kg of the 250 kg of silicon per metric ton (6.5%)**, or 58 kg/t (23%) in carbon-rich deposits, unless the CO is recycled (D8) | D8 | Derived | [PR] §1e: carbothermal routes need >= 1,650 C | Medium. **Carbon is a useful but limiting reductant; the bulk of Mercury's silicon would need another route (electrolysis)** |
| Sulfur grade relative to the Moon | Mercury 19-23 kg/t against Apollo soils 0.474-0.794 kg/t: **24 to 49 times** (D9) | [ME] F1; [TOU08] Table 1 | Derived from primary | none | High |
| Sulfur concrete | Commercial sulfur concrete 12-22 wt% S, no water; 35 MPa uncycled, 7 MPa after cycling to liquid-nitrogen temperature; sulfur melts ~119 C, so service temperature must stay below that. One metric ton of Mercury regolith carries the sulfur for 86-192 kg of sulfur concrete (D9) | [TOU08] | Primary (NASA MSFC / UAH) | none | Medium. **It cannot be used on sunlit equatorial ground (up to ~700 K, [ME] F4); usable in polar shade, under cover, or indoors** |
| Glass and fiber | Regolith simulant melted at 1,450-1,600 C and drawn into glass fiber that raised sulfur-concrete flexural strength by up to 45% | [TOU08] | Primary (lab) | [PR] §1d (glass, ceramics) | Medium (lunar simulant, not Mercury material) |
| Iron in glass | Mercury regolith carries 1.3-1.9 wt% Fe, partly as sulfide ([ME] F1). Whether melts would be clear enough for optical or cover glass without iron removal was **not established** (low-iron glass specifications were not found in an openable source, log rows 59-60) | [ME] F1 | — | none | Gap |

**End uses by product, for a user near Mercury** (inferences from the sourced grades and process data; the processes themselves are in [PR]):
silicon (structural glass, PV substrate after purification, ferrosilicon reductant for magnesium); magnesium and aluminum (light
structure, reflective coatings, conductors); calcium and lime-type oxides (fluxes, ceramics); sulfur (sulfur concrete in shade,
sulfuric acid for leaching); sodium and potassium (driven off first in any melt, [ME] F10); carbon (limited reductant, D8);
oxygen (the largest single product by mass, about 30-45 wt%, as propellant oxidizer and breathing gas); polar water (hydrogen and
oxygen, propellant, life support, and the only local hydrogen); bulk regolith (shielding mass). Iron and nickel are by-products at
13-19 kg/t ([IMS] §3).

### F2. Energy: sunlight, conversion at high intensity, export, and energy-intensive industry

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Irradiance at Mercury | 9,082.7 W/m^2 mean (6.674 x Earth); 6,248 (aphelion) to 14,394 W/m^2 (perihelion), 4.59 to 10.58 x | [NSSDC] Mercury sheet; [ME] F6, D4 | Primary | [ME] K4: 4.7 to 11.1 x (rounded distances) | High |
| Power per unit collector mass | Proportional to irradiance: a collector of given areal density gives **6.67 times** the power at Mercury's mean distance as at 1 AU; e.g. at the Armstrong-Sandberg 3.92 kg/m^2, 347 W/kg incident at 1 AU vs 2,317 W/kg at Mercury (D6) | D6 | Derived | [SMI21] (low weight): "23 times larger" area at Mars, which is wrong (15.5 by inverse square; Rejected) | High (geometry). The benefit holds only where the collector can reject the extra heat |
| Concentrator cell efficiency (Earth spectrum) | Six-junction III-V cell **47.1% at 143 suns** (direct spectrum); 39.2% at 1 sun global; single-junction flat plates "fundamentally limited to about 30%" | [GEI20] | Primary (Nature Energy) | none opened | High for the lab record; **not a Mercury figure**: cell temperature and the space spectrum are different |
| Hot-cell penalty at Mercury | Flown and designed arrays hold cells at 150-230 C by mirrors (2/3 of area) and tilt, and still degrade (20% in a simulated month for BepiColombo); optimum bandgap rises to ~2 eV near 1,000 K | [ME] F6 | Primary (via sibling) | [NW] F3: arrays off-pointed below 0.62 AU | High. **The 6.67x sunlight is not 6.67x electricity with today's cells** |
| Solar-dynamic (heat engine) conversion | 2 kWe closed-Brayton ground demo in vacuum: engine 21.5-26.4%, Sun-to-user 13.8-16.1%; concentrator facets >85% reflective at ~2.5 kg/m^2; heat stored in LiF-CaF2 melting at 1,041 K for eclipse operation. **DEMONSTRATED (ground, 1996)** | [SHA96] | Primary (NASA TM) | none | High. A heat engine tolerates a hot environment better than PV, but its radiator must see a cold sink (F4) |
| Thermoelectric conversion near Mercury | A 1977 Mercury-orbiter study sized a silicon-germanium solar thermoelectric generator for 300 W at 0.45 AU: about 20 W at Earth, over 900 W at 0.30 AU; optimum specific power about 11-12 W/lb (about 24-26 W/kg) at a ~550 C difference. **ENGINEERING-STUDIED (never flown)** | [STG77] | Primary (NASA-archived study; authors not shown in the record) | none | Medium. Output rises much faster than irradiance because the temperature difference rises too |
| Solar furnace concentration | Ideal concentration to reach 1,650 C: 54x (perihelion) to 124x (aphelion) at Mercury against 570x at 1 AU | [ME] F6, D5 | Derived (sibling) | none | High (geometry). Smaller, cheaper mirrors for the same process heat |
| Electricity needed by energy-intensive products | Aluminum (Hall-Héroult) 13-15 kWh/kg, >950 C, theoretical minimum 6.23; silicon metal (submerged arc, >1,800 C) 11-13 MWh/t; ferrosilicon 75% <= 8 MWh/t; magnesium: lab cell 7.0 kWh/kg (minimum 6.2), whole U.S. plant 44 kWh/kg, silicothermic reduction stage ~8-13 kWh(th)/kg | [WU22]; [KSI16]; [MAC19]; [DEM12]; [BAT16]; [ME] D9 | Primary (paper, proceedings), patent background for the 44 | Al: [PR] SP-413 refinery 18.7 kWh(e) + 12.3 kWh(th)/kg | Medium-high for Al and Si; medium for Mg (cell vs plant, Conflicts K3) |
| Power and collector area for 1 Mt/yr of product | Continuous power: Al 1.48-1.71 GW; Si 1.25-1.48 GW; Mg 0.80 GW (lab-cell basis) to 5.02 GW (plant basis). 20%-efficient collector area in space: Al 0.82-0.94 km^2 near Mercury vs 5.4-6.3 km^2 at 1 AU; Mg 0.44-2.76 km^2 vs 2.9-18.4 km^2 (D7) | D7 | Derived | none | Medium (power only; plant mass and heat rejection not included) |
| Surface power penalty | Equatorial night 88 days: 2,111 kWh of storage per kW of continuous load; for a 1.48 GW smelter, 3.1 x 10^9 kWh (D7, [ME] D6). Best polar point lit ~82% of the solar day ([ME] F4) | [ME] F4, F6 | Derived | none | High (arithmetic). **Continuous industry on the surface needs a polar site, orbit-based collectors, or very large storage** |
| Published Mercury power-satellite or power-export concepts | **None found** (rows 26, 67; [ME] row 88; [NW] F8). Concepts that touch it: whole-planet disassembly into a solar-collector swarm (F5); a near-Sun laser for sails ("To Be Determined") [JOH17] | — | — | [NW] F8: microwave links need 67-226 km apertures at these ranges; lasers hundreds of meters | High that no engineering study exists |

**Who could use it, and the condition.** Industry located in the Mercury region (on the surface at a polar site, or in heliocentric
or Mercury orbit with collectors that never see night). Export of the energy itself has no study and faces the aperture limits in
[NW] F8; export of energy embodied in products (refined metal, glass) runs into the transport limits in [IMS] §5.

### F3. Location as a launch site, and as a base for near-Sun work

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Launch to Mercury escape | 4.25 km/s, 9.0 MJ/kg; 0.92 km of track at 1,000 g; 0.30 GW average for 1 Mt/yr; no atmosphere | [ME] F8, D8 | Derived (sibling) | [IMS] §3 | High as physics; no Mercury launcher design exists ([ME] F9) |
| Material placed into heliocentric orbit near Mercury | Escape alone (9.0 MJ/kg) puts material on a heliocentric orbit close to Mercury's own: the only launch cost for a structure built in Mercury's orbital neighborhood (D5) | D5, [ME] F8 | Derived | [IMS] §6 row "material that never needs to reach Earth" | High |
| Parker Solar Probe benchmark (from Earth) | Launch C3 up to 154 km^2/s^2 (v-infinity 12.4 km/s); seven Venus flybys; 6.4 years to the first 9.86 R_sun perihelion; final orbit 9.86 R_sun x 0.73 AU, 88-day period | [GUO14] | Primary (APL mission design) | none | High |
| Cost to lower perihelion, from Earth vs Mercury (impulsive, coplanar, no flybys) | To 9.86 R_sun: v-infinity 21.0 km/s from Earth; 25.8 from Mercury's mean orbit; **20.4 from Mercury's actual aphelion**. To 2-4 R_sun: 24.1-25.7 from Earth; 33.4-37.5 from Mercury mean; 26.8-30.2 from aphelion. To the solar surface: 26.9 (Earth), 40.5 (Mercury mean), 32.7 (aphelion). To 0.20 AU: 12.6 (Earth), **8.4** (Mercury mean), 5.1 (aphelion). To 0.10 AU: 17.1 (Earth), 17.2 (Mercury mean), 13.0 (aphelion) (D2) | D2 | Derived | Secondary Q&A pages: "cancel about 24 km/s" from Earth (row 66) | High as physics. **Mercury's orbital speed (47.36 km/s mean, 38.86 at aphelion to 58.97 at perihelion, [NSSDC]) is a handicap for falling inward, not an asset**; its advantage holds only for perihelia above about 0.1 AU, and its aphelion is the best departure point |
| Solar escape | v-infinity 12.3 km/s from Earth vs 19.8 from Mercury's mean orbit (17.0 at perihelion) (D2) | D2 | Derived | none | High. Mercury is a worse departure point for the outer system too |
| Bodies deeper in the Sun's well | Vulcanoid zone 0.07-0.21 AU (15-45 R_sun); **no vulcanoids larger than 5.7 km** (3 sigma, STEREO HI-1); a 100 km pure-iron body at 0.06 AU evaporates in <4.5 Gyr | [STE13] | Primary (Icarus) | none | High for the limit. **No known body exists sunward of Mercury to be supplied** |
| Near-Sun missions and structures as Mercury customers | Near-Sun hardware would be supplied from Mercury's orbit at the D2 costs; one near-Sun concept found is a laser in low solar orbit powering sails (SPECULATIVE, [JOH17]); near-Sun probes so far are built on Earth and use Venus flybys ([GUO14]) | [JOH17]; [GUO14] | Primary (talk; mission paper) | none | Low. No study proposes Mercury as a base for solar missions |
| Light-sail and solar-electric performance near Mercury | Sail acceleration scales as 1/r^2 (lightness number independent of distance); arrays power-capped by heat below 0.62 AU | [NW] F3 | Primary (via sibling) | none | High |

### F4. Location as a thermal resource

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Temperatures available | Subsolar ground up to 724 K near perihelion; hot poles ~700 K, warm poles ~570 K; night ~110 K; polar cold traps ~100 K annual average (max ~170 K) | [ME] F4 | Primary (via sibling) | [STO14]: crater rim "550K and above", interior "350-80K" | High |
| Ideal (Carnot) efficiency between these | 0.86 (700 K ground to 100 K trap); 0.82 (550 K rim to 100 K); 0.90 (1,041 K solar receiver to 100 K); 0.71 (1,041 K to a 300 K radiator) (D11) | D11 | Derived | none | High (as limits). Real engines reach a fraction of Carnot: 21.5-26.4% engine efficiency in the Brayton demo [SHA96] |
| What the cold sink is worth to a radiator | Radiating at 300 K (emissivity 0.9): 411 W/m^2 into an 83 K polar-shadow sink, 413 W/m^2 to deep space, **none** into the ~580 K equatorial day sink. At 150 K: 23 W/m^2 (shadow) vs 26 (space) (D11) | D11 from [ME] D11 sinks | Derived | none | High (physics). **The polar benefit is shelter from hot ground; a radiator in shadow performs like one in deep space, no better** |
| Cold-side cost of high Carnot ratios | A radiator at 100 K rejects about 5 W/m^2 (D11 scaling, sigma T^4 x 0.9) | D11 | Derived | none | High. Large temperature ratios require very large cold radiators or a conductive sink |
| Published Mercury thermal-resource concepts | (a) Reflectors on a sunlit polar rim beaming sunlight into a permanently shadowed floor (TransFormers, NIAC Phase I, 2014): needs ~300 W/m^2 delivered 10-20 km to replace a 300 W RTG that must shed ~2 kW of heat. **ENGINEERING-STUDIED (Phase I).** (b) Solar thermoelectric generator for a Mercury orbiter (1977): power rises from 300 W at 0.45 AU to >900 W at 0.30 AU. **ENGINEERING-STUDIED.** (c) No concept found that runs an engine between hot ground and a cold trap | [STO14]; [STG77]; rows 33, 35 | Primary | none | Medium |
| Heat storage for the night | Solar-dynamic receiver stores heat in LiF-CaF2 (melts 1,041 K) | [SHA96] | Primary | [LT] 3D: wax and water PCMs, ~30% PCM mass fraction at system level | Medium. Sizing for an 88-day night is not studied anywhere found |

### F5. Construction in the Mercury region: building near the material

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Whole-planet collector swarm at Mercury's distance | Sphere at Mercury's semi-major axis 4.21 x 10^22 m^2; half of Mercury's mass gives 3.92 kg/m^2 (0.5 mm of iron); captor efficiency 1/3; 1/10 of power to mass drivers; disassembly in 31 years 85 days after a 1 km^2 seed; "unlikely to be attempted". Assumes "30% silicate and 70% metal, mainly iron or iron oxides". **SPECULATIVE** | [AS13] §4.1-4.2 | Primary (exploratory-engineering preprint) | [ME] F9; [WRI20] via [ME] | Low as a plan. **The assumed metal-rich bulk is the core; the surface is 1-2 wt% Fe ([ME] F1)** |
| Thin-film collectors from the crust alone | A complete sphere at Mercury's distance at the Angel flyer areal density (4.2 g/m^2) masses 1.77 x 10^20 kg: **2.3% of a 35 km crust** (D6). At 3.92 kg/m^2 it needs 1.65 x 10^23 kg, i.e. the core | D6 from [ANG06] areal density, [AS13] area | Derived | none | Medium (areal density is a sunshade's, not a power collector's) |
| Sunshade benchmark (Earth L1) | 1.8% of sunlight blocked by 4.7 x 10^6 km^2 of 4.2 g/m^2 flyers: 20 Mt (23 Mt with losses); designed to be launched from Earth by electromagnetic launch at a target $50/kg, **explicitly not made from lunar or asteroid material** | [ANG06] | Primary (PNAS) | Asteroid-anchored dust cloud: up to 6.58% insolation reduction, 1.7% needed to offset 2 C; the largest NEAs alone lack the mass [BEW12] | High (as a study) |
| Mercury as a sunshade source | **No study found** that sources a sunshade or collector swarm from Mercury except the whole-planet disassembly (rows 42-47). Delivery from Mercury to Sun-Earth L1 would face the same transfer costs as any Mercury-to-Earth cargo ([IMS] §5) | rows 42-47 | — | none | High that no study exists |
| Area-scale industry near Mercury | 1 Mt/yr of aluminum needs about 0.8-0.9 km^2 of 20% collectors near Mercury (D7); the 20 Mt Angel sunshade equals about 20 years of that output if the sunshade were aluminum (inference) | D7; [ANG06] | Derived | none | Low (an order-of-magnitude comparison only) |
| Why build near the source | Only the 4.25 km/s escape (9.0 MJ/kg) is needed to place Mercury material on a heliocentric orbit near Mercury, against 7.55 km/s from low Mercury orbit (13.1 km/s all-propulsive) to reach Earth ([IMS] §5) | [ME] F8; [IMS] §5 | Derived (siblings) | none | High |
| Where the heat goes | A collector near Mercury runs at the plate temperatures of D12 (530-630 K at mean distance); Mercury-region structures must be built for that, which is the reason one Dyson-swarm preprint preferred Mars ([SMI21], low weight) | D12; [SMI21] | Derived / secondary | [ME] F11 | Medium |

### F6. Computation and other energy-hungry uses placed near the Sun

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Thermodynamic cost of computing | Erasing one bit costs at least k_B T ln 2: 2.9 x 10^-21 J at room temperature; 2.87 x 10^-23 J at 3 K | [SAN99] §6 | Primary (J. Evol. Technol., exploratory) | D12 recomputes the same values | High (physics) |
| Optimal radius for a computing shell around the Sun | Balancing bit-erasure cost against thermodynamic efficiency gives T_shell = 2 T_u and r = 6.8 x 10^14 m (629 light-hours), "far too large to be practical"; practical shells "either use most of their energy for cooling, or beam the concentrated energy out". **SPECULATIVE** | [SAN99] §6.3 | Primary (exploratory) | none | High as an argument; it is a bound, not a design |
| Near-Sun computing per unit collector area | A flat plate rejecting only by radiation runs at 532-633 K at Mercury's mean distance vs 331-394 K at 1 AU; the Landauer-limited erasure rate per m^2 is about **4.1 times** higher near Mercury (1.5-1.8 x 10^24 vs 3.6-4.3 x 10^23 bits/s/m^2) (D12) | D12 | Derived | none | High as a bound. **More computation per kilogram of collector; less per joule of sunlight** |
| Hot-electronics ceiling | SiC integrated circuits ran over 1 year at 500 C (773 K) at 175+ transistors; mainstream electronics are kept near room temperature behind shades | [ME] F11 | Primary (via sibling) | none | High. A near-Sun computer either runs on SiC-class logic or spends energy and radiator area on cooling |
| Present-day space computing benchmark | Google's Suncatcher design study: dawn-dusk LEO at 650 km, panels "up to 8 times more productive than on earth"; TPU memory irregularities after 2 krad(Si), no hard failure to 15 krad; launch "less than $200/kg by the mid-2030s" (projection) | [GOO25] | Primary (company research post; preprint not opened) | none | Medium. It is placed near Earth, where its users are, not near the Sun |
| Radiation near Mercury | Solar-particle peak intensities ~3-19 times 1 AU; no shielding above tens of MeV | [ME] F7 | Primary (via sibling) | none | Medium. Adds to the dose budget of any electronics stationed there |

### F7. Science and exploration value (brief)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Mission-level objectives | Origin and evolution of a planet close to its star; interior structure and composition; origin of its internal magnetic field; cratering, tectonics, polar deposits, volcanism; exosphere; magnetosphere; a test of general relativity from precise orbit tracking | [ESA-BC] | Primary (agency) | [ME] F1-F5 | High |
| Unique features | Hollows: fresh, shallow, rimless depressions tens of meters to a few km across with bright halos, attributed to volatile loss | [BLE11] | Primary (Science) | [ME] F1: S, Na, K, Cl and graphite enrichments | High |
| Composition extremes | Most reduced terrestrial planet (log fO2 about IW-5.4); sulfur at least 10 times Earth's or the Moon's silicate portion; graphite-bearing crust; core 69-73% of the mass | [ME] F1, F2 | Primary (via sibling) | none | High |
| Unexplored by landers | No lander has operated; the 2020 lander study is the only detailed surface design | [ME] F12 | Primary (via sibling) | none | High |

### F8. Costs and conditions that cut each benefit (from the siblings)

| Benefit | What cuts it | Numbers | Source |
|---|---|---|---|
| Materials for use near Mercury | No Mercury process study; regolith density, strength and free-metal content unmeasured; high sulfur and alkalis complicate melts | Fe 13-19 kg/t; regolith 3.7-40 m; S 2-4 wt% | [ME] F1, F3, F10 |
| Materials exported to Earth or Mars | Transfer cost, two-week windows every 116 days, arrival at 6.5-11 km/s, fleets that fail at kt/yr by xenon | 7.55 km/s from LMO; 2.4 t propellant per t delivered (SEP direct) | [IMS] §5; [NW] F1-F6 |
| Surface solar energy | 88-day equatorial night; arrays capped at 150-230 C; 20% loss in a simulated month (BepiColombo) | 2,111 kWh per kW of load | [ME] F4, F6 |
| Orbital solar energy | Heat: off-pointing below 0.62 AU; hardware degradation | BepiColombo 2024 power fault | [NW] F3 |
| Energy export | Diffraction: microwave apertures 67-226 km; lasers ~300-670 m with nanoradian pointing | — | [NW] F8 |
| Launch site | No launcher design; fixed track aligns with an Earth window about 2.4 days in six years | 4.25 km/s escape, 10.5 km/s direct to Earth | [ME] F8; [NW] F4 |
| Near-Sun access | Orbital speed handicap (F3) | +4.8 to +13.6 km/s v-infinity vs Earth to reach 1-9.86 R_sun from Mercury's mean orbit | D2 |
| Thermal resource | 700 K ground by day; radiators must be shaded; cold radiators are huge | 12.7 kW/m^2 ground IR at 700 K; ~580 K day sink | [ME] F11 |
| Every benefit | Radiation (SEP several to ~19x), communications 4.3-12.3 min one way with conjunction outages, lander gaps of 6 weeks | — | [ME] F7, F12; [NW] F7 |

### F9. Benefits ranked by who could use them and what delivery costs

Ranking rule (stated so it can be challenged): strength of the physical gain times how cheaply it reaches its user, using only the
figures above. **"Earth transport needed?" = no** means the benefit is realized without any material or energy reaching Earth.

| Rank | Benefit | Who could use it | Delivery cost (sourced) | Earth transport needed? | Evidence level | Key limit |
|---|---|---|---|---|---|---|
| 1 | Sunlight for energy-intensive processing (Al, Si, Mg, glass, oxygen) | Industry in Mercury orbit or the Mercury neighborhood; polar surface plants | None for the energy; 0.4-2.8 km^2 of 20% collectors per Mt/yr of product vs 2.9-18 km^2 at 1 AU (D7) | No | Physics DEMONSTRATED; Mercury plant SPECULATIVE | Hot arrays (150-230 C limits, degradation); 88-day night on the equator |
| 2 | Bulk crustal material (Si, Mg, Al, Ca, O, S) for structures built near Mercury | Builders of collectors, shields, habitats, shades in Mercury's heliocentric neighborhood | 9.0 MJ/kg to escape (2.5 kWh/kg), 4.25 km/s | No | Inventory DEMONSTRATED (orbital remote sensing); processing ENGINEERING-STUDIED on lunar analogs only | No Mercury process study; carbon limits carbothermal routes to 6.5-23% of Si (D8) |
| 3 | Polar water ice (hydrogen, oxygen, propellant, life support, cooling) | Polar bases, orbital depots, water-propellant tugs ([IMS] §5) | Polar surface operations; ascent 3.5 km/s (Palaszewski) | No | Ice DEMONSTRATED (radar, neutrons); extraction ENGINEERING-STUDIED ([ME] F9) | Inventory uncertain 100x; 21,000-3,000,000 yr at 1 Mt/yr (D10) |
| 4 | Oxygen from oxides (30-45 wt% of regolith) | Life support, oxidizer near Mercury | Same as rank 2 plus process energy (24-135 kWh/kg O2 on lunar processes, [PR] §5) | No | Process DEMONSTRATED (ground, lunar simulant) | Electricity, which rank 1 supplies |
| 5 | Sulfur (24-49x lunar grade) | Sulfur concrete in shade or indoors; sulfuric acid for leaching | Local | No | Sulfur concrete DEMONSTRATED (lab, lunar simulant) | Melts at ~119 C; useless on sunlit ground |
| 6 | Cheap high-temperature process heat (solar furnaces 54-124x vs 570x at 1 AU) | Smelting, glassmaking near Mercury | Local | No | Geometry; solar-thermal DEMONSTRATED (ground) | Night; furnace hardware unstudied at Mercury |
| 7 | Shelter from hot ground for heat rejection at polar sites | Any polar facility | Local | No | Physics | Shadowed area 1.3-1.5 x 10^4 km^2 north ([ME] F4); a cold sink is no better than deep space |
| 8 | Launch base for the 0.1-0.47 AU heliocentric region | Near-Sun observatories, collectors, sails | v-infinity 5.1-8.4 km/s to reach a 0.20 AU perihelion vs 12.6 from Earth (D2) | No | Physics | No body sunward to supply ([STE13]); worse than Earth below ~0.1 AU |
| 9 | Computation per kilogram of collector (about 4x at 1 AU) | Heat-tolerant computing near Mercury | Local | No | Physics bound; SiC logic DEMONSTRATED small-scale | Worse per joule; users are elsewhere; light time to Earth 4-12 min |
| 10 | Science (most reduced planet, field, hollows, polar volatiles, relativity) | Researchers | Lander-class missions ($1.5 billion, [ME] F9) | Data only | DEMONSTRATED (orbiters) | No lander yet |
| 11 | Refined material shipped to Venus, Earth or Mars | Inner-system industry | 7.55 km/s from LMO to Earth; fleets fail at kt/yr ([IMS] §5) | Yes | SPECULATIVE at scale | The leg itself |
| 12 | Energy exported by beam | Earth, Venus, Mars | 67-226 km microwave apertures; hundreds-of-meter lasers ([NW] F8) | Yes (energy) | No study | Diffraction and pointing |
| 13 | Iron and nickel | Any | By-product at 13-19 kg/t; core 420-470 km down | — | DEMONSTRATED (grade) | [IMS] M-1 |
| 14 | Base for reaching the Sun's surface or a few solar radii | Solar missions | 4.8-13.6 km/s more v-infinity than from Earth from the mean orbit; about equal only from aphelion (D2) | No | Physics | Orbital speed |

### Source key

- **[NSSDC]** NASA NSSDCA fact sheets: Mercury (last updated 11 Jan 2024), Earth (15 Nov 2024), Moon (11 Jan 2024), https://nssdc.gsfc.nasa.gov/planetary/factsheet/. Primary.
- **[BEU20]** Beuthe, Charlier, Namur, Rivoldini, Van Hoolst, "Mercury's crustal thickness correlates with lateral variations in mantle melt production", GRL 47 (2020), arXiv 2011.15066. Primary.
- **[NIT18]** Nittler, Chabot, Grove, Peplowski, "The Chemical Composition of Mercury", in *Mercury: The View after MESSENGER* (Cambridge, 2018), arXiv 1712.02187. Primary.
- **[USGS-xx]** U.S. Geological Survey, *Mineral Commodity Summaries 2026* (February 2026), commodity sheets at https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-<name>.pdf: aluminum, magnesium-metal, silicon, titanium, sulfur, nickel, lime, graphite, salt, potash, soda-ash, iron-ore, iron-steel. Primary (dataset).
- **[JON18]** H. W. Jones, "The Recent Large Reduction in Space Launch Cost", ICES-2018-81 (8 Jul 2018), NTRS 20200001093. Primary.
- **[GOO25]** Agüera y Arcas et al., "Exploring a space-based, scalable AI infrastructure system design", Google Research blog (4 Nov 2025). Primary for the company's own figures; projections are forecasts.
- **[WU22]** Wu, Xie, Hao et al., "Ionic liquids as electrolytes in aluminum electrolysis", Front. Chem. 10:1014893 (3 Nov 2022). Primary (review).
- **[KSI16]** Ksiazek, Tangstad, Ringdalen, "Five furnaces five different stories", *Silicon for the Chemical and Solar Industry XIII* (Kristiansand, June 2016), p. 41. Primary (proceedings, citing Schei et al.).
- **[MAC19]** Machulec, Bialik, Gil, Arch. Metall. Mater. 64(2):633-638 (2019), doi 10.24425/amm.2019.127591. Primary.
- **[DEM12]** Demirci and Karakaya, "Molten Salt Electrolysis of MgCl2 in a Cell with Rapid Chlorine Removal Feature", TMS Magnesium Technology (2012), METU record. Primary (abstract).
- **[BAT16]** Battelle, US9499880B2 (22 Nov 2016), background section. Patent (secondary for the plant figure it quotes).
- **[GEI20]** Geisz et al., "Six-junction III-V solar cells with 47.1% conversion efficiency under 143 Suns concentration", Nature Energy 5(4):326-335 (Apr 2020), RePEc record. Primary.
- **[SHA96]** Shaltens and Mason, "Early Results From Solar Dynamic Space Power System Testing", NASA TM-107252 (Jul 1996), NTRS 19960047096. Primary.
- **[STG77]** "Solar Thermoelectric Generators" (study of an STG for a Mercury-orbiting spacecraft), NTRS 19780016702, publication date 29 Jul 1977. Primary (scanned report; authors not shown in the record).
- **[STO14]** Stoica, Ingham, Tamppari, Mitchell, Quadrelli, "TransFormers for Extreme Environments", NIAC Phase I Final Report (May 2014), NTRS 20180008682. Primary.
- **[GUO14]** Guo, McAdams, Ozimek, Shyong, "Solar Probe Plus Mission Design Overview and Mission Profile", ISSFD 24 (2014). Primary.
- **[STE13]** Steffl, Cunningham, Shinn, Durda, Stern, "A Search for Vulcanoids with the STEREO Heliospheric Imager", Icarus (2013), arXiv 1301.3804. Primary.
- **[JOH17]** L. Johnson and E. Montgomery, "From Solar Sails to Laser Sails" (15 Dec 2017), NTRS 20170012350. Primary (talk slides).
- **[ANG06]** R. Angel, "Feasibility of cooling the Earth with a cloud of small spacecraft near the inner Lagrange point (L1)", PNAS 103(46) (2006), PMC1859907. Primary.
- **[BEW12]** Bewick, Sanchez Cuartielles, McInnes, "Gravitationally bound geoengineering dust shade at the inner Lagrange point", Adv. Space Res. 50(10):1405-1410 (2012), Strathprints 41028 (abstract). Primary.
- **[AS13]** Armstrong and Sandberg, "Eternity in six hours: intergalactic spreading of intelligent life and sharpening the Fermi paradox", preprint submitted to Acta Astronautica (12 Mar 2013). Primary (exploratory engineering).
- **[SMI21]** J. Smith, "Viability of a Dyson Swarm as a Form of Dyson Sphere", arXiv 2109.11443 (physics.pop-ph, 2021). Secondary (undergraduate preprint; low weight).
- **[SAN99]** A. Sandberg, "The Physics of Information Processing Superobjects: Daily Life Among the Jupiter Brains", J. Evolution and Technology 5(1):1-34 (1999). Primary (exploratory).
- **[TOU08]** Toutanji and Grugel, "Performance of 'waterless concrete'", NTRS 20090033079 (2008). Primary.
- **[ESA-BC]** ESA, "BepiColombo: Science objectives", esa.int (no page date). Primary (agency).
- **[BLE11]** Blewett et al., "Hollows on Mercury: MESSENGER Evidence for Geologically Recent Volatile-Related Activity", Science 333:1856-1859 (2011), DLR elib 73581 (abstract). Primary.

## 4. Conflicts

- **K1. Aluminum smelting electricity.** [WU22] text: 13-15 kWh/kg; its Table 3: 13,000-19,000 kWh/t. The wider table range
  likely spans older cells and different system boundaries (cell only vs. with auxiliaries). A search summary's "12.5-12.9 kWh/t"
  world average (row 8) is a unit error and was not used; a "13,990 kWh/t" world average (row 64) was not traced to an opened page.
- **K2. Surface oxygen.** Stoichiometric balance of the measured cations gives ~450 kg O per metric ton (closing the mass to 1,012 kg/t);
  the GRS O/Si of 1.2 gives ~300 kg/t. [NIT18] report the GRS value as lower than stoichiometry predicts (~1.7) and suggest
  near-surface alteration by degassing; they caution against over-interpretation. The true oxygen yield of a process is unknown.
- **K3. Magnesium energy.** Lab cell 7.0 kWh/kg (minimum 6.2) [DEM12]; whole U.S. electrolytic plant 44 kWh/kg [BAT16];
  silicothermic reduction stage ~8-13 kWh(th)/kg ([ME] D9). Different boundaries: cell electrolysis only vs. brine
  dehydration, chlorination and plant losses vs. one thermal stage. The D7 range (0.80-5.02 GW per Mt/yr) carries the full spread.
- **K4. Dyson-swarm areal mass and location.** [AS13]: 3.92 kg/m^2 from half of Mercury's mass, at Mercury's distance. A search
  summary gave "245 g/m^2" (row 45), not in the paper. [SMI21] prefers Mars over Mercury, partly on a collector-area ratio of
  "just over 23 times", which inverse-square geometry puts at 15.5 (Mars a = 1.524 AU vs 0.387 AU). [AS13] assumes a 70%-metal
  bulk "mainly iron or iron oxides"; MESSENGER finds the metal is the core and the surface is 1-2 wt% Fe ([ME] F1-F2).
- **K5. Plate temperature at 1 AU.** [SAN99] gives 395 K for an unshielded object at 1 AU; NSSDC gives Earth's black-body
  temperature as 254 K. Different bodies: a flat plate absorbing and emitting on one face (394 K in D12) versus a rotating sphere
  with Earth's albedo radiating from all of its surface.
- **K6. Near-Sun access from Mercury.** Popular framing treats Mercury as the natural staging point for the Sun; the arithmetic (D2)
  shows it is the worse departure point for perihelia below about 0.1 AU unless departing at aphelion. Not a source conflict but a
  premise conflict, reported as found.

## 5. Derived figures

Scripts and full output: scratch folder `benefits_of_mining_mercury/calc/` (`c1_nearsun.py`, `c2_benefits.py`, `c3_compute_temp.py`
and their `_out.txt` files). Inputs are sourced constants named in each line.

- **D1. Inventories.** Shell mass (4/3) pi (R^3 - (R-t)^3) rho, R = 2,439.7 km. Crust (rho 2,957 [BEU20]): 4.387 x 10^21 kg (20 km),
  7.631 x 10^21 (35 km), 1.083 x 10^22 (50 km); top 1 km 2.211 x 10^20. Regolith at an assumed 1,660 kg/m^3: 4.594 x 10^17 (3.7 m),
  5.711 x 10^17 (4.6 m), 4.966 x 10^18 (40 m). Elements = crust mass x ([ME] D1 kg/t) / 1,000. [NIT18] model: shell (2,020-2,440 km,
  3,380 kg/m^3) 8.897 x 10^22 kg; core (6,980 kg/m^3) 2.410 x 10^23; sum 3.300 x 10^23 vs NSSDC 3.3010 x 10^23. Shell composition:
  average of Table 2.2 NSP and IcP-HCT pre-melting oxides (sum 99.47 wt%) scaled to 92% to leave the added 1 wt% Fe and 7 wt% S;
  element fraction = oxide wt% x (cation mass / oxide mass): Si 22.84, Mg 20.78, Al 2.16, Ca 2.02, Na 1.12, Ti 0.12, K 0.03 wt%;
  O 42.9 wt%.
- **D2. Near-Sun and solar-escape costs.** Retrograde departure from a circular orbit r onto an ellipse with perihelion q:
  v_inf = sqrt(mu/r) - sqrt(mu (2/r - 2/(r+q))), mu = 1.32712440041 x 10^20 m^3/s^2; R_sun 695,700 km; AU 149,597,870,700 m.
  From 1 AU / Mercury 57.909 x 10^6 km / Mercury aphelion 69.818 x 10^6 km treated as circular / exact aphelion speed 38.86 km/s:
  9.86 R_sun 20.96 / 25.84 / 25.16 / 20.42 km/s; 4 R_sun 24.09 / 33.38 / 31.53 / 26.79; 2 R_sun 25.74 / 37.50 / 34.98 / 30.24;
  1 R_sun 26.92 / 40.50 / 37.47 / 32.73; 0.10 AU 17.08 / 17.20 / 17.70 / 12.96; 0.20 AU 12.59 / 8.36 / 9.83 / 5.09. Burns from
  200 km parking orbits sqrt(v_inf^2 + 2 mu_p/r_p) - sqrt(mu_p/r_p): e.g. 9.86 R_sun 15.90 (LEO) vs 17.93 (LMO, exact aphelion);
  0.20 AU 8.94 (LEO) vs 3.64 (LMO, exact aphelion). Solar escape v_inf (sqrt 2 - 1) v_circ: 12.34 (Earth), 19.83 (Mercury mean),
  16.98 from Mercury perihelion (exact). PSP check: C3 154 km^2/s^2 = v_inf 12.41 km/s (plus seven Venus flybys).
- **D3. Value framing.** Launch $/kg divided by 2025 USGS price $/kg: Al $3.97 (180 c/lb x 2.20462): 353 (Falcon Heavy $1,400),
  685 (Falcon 9 $2,720), 50 ($200 projection); Mg $2.50: 560 / 1,088 / 80; Si $2.87: 488 / 949 / 70; Ti $12: 117 / 227 / 17;
  Ni $15: 93 / 181 / 13; S $0.18: 7,778 / 15,111 / 1,111; iron ore $0.089: 15,730 / 30,562 / 2,247.
- **D4. Earth orbit to low Mercury orbit.** LEO (200 km) departure for v_inf 7.53 km/s ([NW] C1): sqrt(7.53^2 + 2 x 398,600.4/6,578.1)
  - sqrt(398,600.4/6,578.1) = 5.55 km/s; capture into 200 km LMO 7.55 km/s ([ME] D8); total 13.10 km/s; with an assumed Isp of 450 s, mass ratio
  exp(13,100 / (450 x 9.80665)) = 19.5. Flyby route 2.8 km/s: 1.89.
- **D5. Escape energy** v^2/2: Earth 11.186 km/s, 62.56 MJ/kg (17.38 kWh/kg); Moon 2.38, 2.83 MJ/kg; Mercury 4.25, 9.03 MJ/kg (2.51 kWh/kg).
- **D6. Collector power and mass.** Incident power per kg = S / sigma_A: at 3.92 kg/m^2, 347 W/kg (1,361 W/m^2) vs 2,317 W/kg
  (9,082.7 W/m^2); at 4.2 g/m^2, 3.24 x 10^5 vs 2.16 x 10^6 W/kg. Sphere at 57.909 x 10^9 m: 4.214 x 10^22 m^2; x 4.2 g/m^2 = 1.77 x 10^20 kg
  (2.32% of a 35 km crust); x 3.92 kg/m^2 = 1.65 x 10^23 kg.
- **D7. Industry power and area.** P = E (kWh/kg) x 10^9 kg / 8,766 h: Al 13 / 15 -> 1.48 / 1.71 GW; Si 11 / 13 -> 1.25 / 1.48 GW;
  Mg 7.0 / 44 -> 0.80 / 5.02 GW. Area = P / (0.20 x S): Al 0.82-0.94 km^2 (Mercury mean) vs 5.4-6.3 km^2 (1 AU); Si 0.69-0.82 vs 4.6-5.4;
  Mg 0.44-2.76 vs 2.9-18.4. Storage for 1.48 GW through an 88-day night: 1.48 x 10^6 kW x 2,111 h = 3.1 x 10^9 kWh.
- **D8. Carbon limit.** SiO2 + 2C -> Si + 2CO: 2 x 12.011 / 28.086 = 0.855 kg C per kg Si; 14 kg/t C -> 16.4 kg/t Si (6.5% of 250);
  50 kg/t -> 58.5 kg/t (23%).
- **D9. Sulfur.** 19 / 0.794 = 24; 23 / 0.474 = 49. Sulfur concrete mass bound per metric ton of regolith: 19 / 0.22 = 86 kg to 23 / 0.12 = 192 kg.
- **D10. Ice draw-down.** Inventory / rate: 2.1 x 10^13 kg at 1 Mt/yr = 21,000 yr; 1.4 x 10^15 = 1.4 x 10^6 yr; 3 x 10^15 = 3 x 10^6 yr;
  at 100 Mt/yr: 210, 14,000, 30,000 yr.
- **D11. Heat engines and radiators.** Carnot 1 - Tc/Th as listed in F4. Net radiated flux 0.9 sigma (T_r^4 - T_s^4),
  sigma 5.670374419 x 10^-8: T_r 300 K -> 411 W/m^2 (83 K sink), 413 (3 K); 400 K -> 1,304 / 1,306; 200 K -> 79 / 82; 150 K -> 23 / 26;
  any T_r below 580 K gains heat from the equatorial day sink (negative net). 100 K radiator: 0.9 sigma 100^4 = 5.1 W/m^2.
- **D12. Computing near the Sun.** Plate temperature T = (S / (n sigma))^(1/4) with n = 1 (one emitting face) or 2: 1 AU 394 / 331 K;
  Mercury aphelion 576 / 484; mean 633 / 532; perihelion 710 / 597 K. Landauer bound per m^2: S / (k_B T ln 2): 1 AU 3.61-4.30 x 10^23;
  Mercury mean 1.50-1.78 x 10^24 bits/s/m^2 (ratio 4.1-4.2, i.e. S^(3/4)); per joule the near-Sun case is worse by T ratio 1.6.

## 6. Constraints for any inhabitant

- **The useful wealth is local.** What Mercury offers in quantity (silicon, magnesium, aluminum, oxygen, sulfur, some carbon, polar
  water, and above all sunlight) pays off where it is used near Mercury; sending it to Earth or Mars is the expensive part (F1c, F8;
  [IMS] §5). A settlement here makes things for itself and its neighborhood.
- **Energy is abundant but hot.** Six to ten times Earth's sunlight, but collectors must run at 150-230 C or hotter and degrade;
  the equator has 88-day nights; continuous industry lives at a polar site or in orbit (F2).
- **Shade is the scarce resource, not cold.** A radiator in polar shadow works no better than one in open space; what matters is
  not seeing 700 K ground (F4). Permanently shadowed ground is about 1.3 x 10^4 km^2 in the north ([ME] F4).
- **Water is finite and local.** 10^13 to 3 x 10^15 kg of polar ice is the only hydrogen; at 100 Mt/yr the low estimate lasts about
  two centuries (D10).
- **Sulfur-rich ground** makes waterless sulfur concrete possible, but only out of the sun and below ~119 C (F1c).
- **Carbon is scarce relative to need**: in-place graphite covers a small share of carbothermal reduction (D8).
- **Leaving inward is not cheap.** Mercury is a poor base for reaching the Sun's immediate vicinity and there is nothing sunward to
  mine (F3).
- **Machines that think near the Sun run hot** or pay for cooling (F6); human-shaped machines need shade, cooled enclosures or
  high-temperature parts ([ME] F11).

## 7. Candidate handwaves

Flagged, not accepted. The developer decides.

- **HW-B1. Mercury energy exported to Earth or Mars by beam.** No study; microwave apertures of 67-226 km, laser apertures of
  hundreds of meters with nanoradian pointing ([NW] F8).
- **HW-B2. Room-temperature PV harvesting the full 6.67x sunlight.** Flown arrays at Mercury throw most of it away by mirrors and
  tilt (F2). A design that converts it all needs cells that work at 450 C or a heat engine with a large shaded radiator.
- **HW-B3. Mercury as the natural staging point for missions to the Sun's surface.** Costs 4.8-13.6 km/s more v-infinity than from
  Earth from the mean orbit (D2); only aphelion departures match Earth.
- **HW-B4. A Mercury-built sunshade or collector swarm delivered to Earth's L1.** No study; delivery faces the Mercury-to-Earth
  transfer limits ([IMS] §5, M-3). Angel's design deliberately uses Earth-launched material.
- **HW-B5. Near-Sun computing that is more energy-efficient than computing farther out.** The Landauer bound runs the other way per
  joule (F6, D12).
- **HW-B6. Sulfur concrete on sunlit Mercury ground.** Sulfur melts near 119 C (F1c).
- **HW-B7. Whole-crust inventories as recoverable reserves.** The D1 crust figures assume surface composition to 20-50 km depth;
  nothing has measured it.

## 8. Open threads

- **No Mercury process study** (regolith to oxygen, Mg, Al, Si) and no Mercury regolith density, strength or free-metal content
  ([ME] Open threads). Next: BepiColombo MIXS/MERTIS results; McCubbin et al. 2017 on Si-rich metal.
- **Aluminum and magnesium energy, second primary source.** IAI statistics pages render by script (rows 5, 9) and the BlueGreen
  benchmark is a chart only (row 65). Next: IAI annual statistical PDFs; IEA Aluminum tracking report; a peer-reviewed
  magnesium life-cycle study that states whole-plant electricity (none was opened this session).
- **Silicon metal energy, second source.** Schei, Tuset, Tveit, *Production of High Silicon Alloys* (1998), cited by [KSI16], not opened;
  NREL fy25osti/89464 not reachable (row 22).
- **Low-iron glass specification** (Fe2O3 limit and transmittance) from a standard or peer-reviewed source (rows 59-60).
- **Heat-engine power between sunlit rims and cold traps at Mercury**: no concept found (row 35). Next: lunar thermal-wadi and
  regolith thermal-storage papers (HAL 02887846 located, not opened) adapted to Mercury's 88-day night.
- **Mercury-sourced sunshades or collectors** for Venus or Earth: none found (rows 42-47). Venus-sunshade masses in terraforming
  reviews were seen only in summaries (row 45).
- **Near-Sun missions using Mercury or Mercury flybys** to reach low perihelia: none found; the D2 arithmetic is impulsive and
  coplanar and ignores flybys of Venus or Mercury that a real trajectory would use.
- **Dose at Mercury for electronics** (needed for F6): still no number ([ME] Open threads).
- **Sources found but not read**: Harrop and Schulze-Makuch 2010 (IJAsB 9:89, solar-wind power satellite); Google's Suncatcher
  preprint; Hamill 2020 polar illumination; HAL 02887846 (lunar thermal storage).

## 9. Rejected sources

- **Search summary "12.5-12.9 kWh/t"** world-average aluminum smelting (row 8): a unit error by three orders of magnitude.
- **Search summary "245 g/m^2"** for the Mercury swarm (row 45): not in [AS13], which gives 3.92 kg/m^2.
- **[SMI21]'s "just over 23 times larger" collector area at Mars vs Mercury** (row 27): inverse-square gives 15.5; the preprint is an
  undergraduate pop-physics paper and is used only for its qualitative argument.
- **Search summaries with unopened numbers**: "13,990 kWh/t" (row 64), a Venus sunshade mass of 7.6 x 10^10 kg (row 45), low-iron
  glass transmittances (row 59), "11-13 kWh/kg ... 4.7-5 t CO2" (row 21, superseded by [KSI16], which was opened).
- **Fan wiki, Wikipedia, popular and trade pages** (rows 26, 37, 42, 48, 50, 54, 57, 66): leads only.
- **Breakthrough Propulsion Study** (row 69): no relevant content.
