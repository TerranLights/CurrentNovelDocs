# Benefits of mining or occupying Venus (atmosphere, clouds, surface, location)

*Research file, OOLSD library, tranche 8, section 9. Started 2026-10-11, finished 2026-10-12. Physics and engineering only;
no story, timeline or setting is assumed.*

## 1. Scope

Every physically grounded benefit of mining or occupying Venus: its atmosphere (gas, noble gases, trace species), its clouds
(acid, water), its surface (rock, and the high-temperature hardware developed for it), its energy (sunlight, wind, heat), and its
location (gravity assists, windows, aerocapture, staging). For each: the quantity, the conditions under which it holds, who could
use it, and the cost of getting it to that user. Inventories, extraction chemistry and the ascent problem are taken from the
sibling files and cited, not re-derived: **[VE]** `venus_as_extraction_site.md`, **[MVT]** `mars_venus_and_transfer.md`, **[GRV]**
`gap_retry_mars_venus_jupiter.md`, **[LSS]** `life_support_lowg_power_structures.md`, **[NW]** `inner_system_logistics_network.md`,
**[IMS]** `inner_system_mining_synthesis.md`, **[SYN]** `starlifting_synthesis.md`.

Evidence levels: **DEMONSTRATED** (flown, or run in a test rig), **ENGINEERING-STUDIED** (a quantitative design study),
**SPECULATIVE** (concept or thought experiment), **DERIVED** (arithmetic here from sourced inputs; section 5).

**The short answer.** Venus's benefits are real but almost all of them are **used at Venus or in the space next to it**. Its
atmosphere holds about 1.1 x 10^19 kg of nitrogen and 1.3 x 10^20 kg of carbon ([VE] D1), enough for a 50 kPa nitrogen buffer
on all of Mars four to seven times over (D-B), and carbon, oxygen, carbon monoxide, nitrogen, argon and sulfur can all be
made from the air at a floating platform. But **two facts cut against Venus as a supplier to anyone else**: leaving the
cloud deck costs about 9 km/s on locally made CO/LOX (payload 0.15 to 0.56% of lift-off mass, [VE] 3.7), and **Earth's
own air is a richer source of nitrogen and the noble gases** (nitrogen 34 times, argon 200 times, krypton 36 times more
concentrated by mass of air processed, D-A, D-C), from a well of about the same depth but with hydrogen for high-performance
propellant. Carbon is the exception: Venus air holds about 1,800 times more carbon per tonne than Earth air (D-R), but it pays the same ascent. On the figures found, Venus nitrogen delivered to Mars is not cheaper than Earth nitrogen and is far dearer than
asteroid nitrogen (D-D, D-E). Venus's export-free benefits are the strong ones: an industrial atmosphere that is also a
lifting gas, a radiation shield and an oxidizer; near-Earth gravity and pressure at 50 to 55 km; sunlight 1.9 times
Earth's above the clouds; gravity assists that inner-system missions already depend on (up to about 7 km/s per flyby);
aerocapture with a 92% delivered-mass gain over propulsive capture; and a scientific record of the water Venus lost.

## 2. SEARCH LOG

All entries dated 2026-10-11.

| # | Search string (verbatim) or page opened | Result | Notes |
|---|---|---|---|
| 1 | Read-only: sibling files `inner_system_mining_synthesis.md` (whole), `starlifting_synthesis.md` (whole), `venus_as_extraction_site.md` (whole), `mars_venus_and_transfer.md` 3.7 to 3.11, `inner_system_logistics_network.md` F1, F2, F5, `life_support_lowg_power_structures.md` A1 to A4 | useful | Cited as **[IMS]**, **[SYN]**, **[VE]**, **[MVT]**, **[NW]**, **[LSS]**; not re-derived |
| 2 | WebSearch: `Mars terraforming nitrogen buffer gas requirement partial pressure nitrogen inventory McKay` | useful (lead) | Turyshev 2026 (already in MVT 3.11); forums (newmars) not used |
| 3 | WebSearch: `Ryugu Bennu returned sample nitrogen content wt% carbon content bulk analysis` | useful | Led to Glavin et al. 2025 (NTRS PDF) |
| 4 | WebSearch: `Venus atmosphere thermal gradient heat engine power generation balloon concept paper` | useful | IAC-13 aerobot heat engine; NIAC heat-exchange aircraft |
| 5 | Opened: Yao, Song, Fan, Li (CAST), "A novel aerobot with a heat engine utilizing atmospheric temperature gradient for planetary exploration", IAC-13,A3,5,5,x17862 (2013), abstract PDF (text extracted locally) | thin | Concept: heat engine between warm low and cool high air during altitude oscillation, working fluid doubles as lift gas; **no numbers in the abstract** |
| 6 | Opened: NASA NIAC page "Heat Exchange-Driven Aircraft for Low-Altitude and Surface Exploration of Venus" (PI E. Noe Dobrea, PSI, 2020) | useful | Lithium heat store: "about 3.25 times more heat energy in Lithium metal than the potential energy required to lift that metal to 40 km"; required end-to-end efficiency "greater than about 31%" |
| 7 | Opened: Glavin, Dworkin, Alexander et al., "Abundant ammonia and nitrogen-rich soluble organic matter in samples from asteroid (101955) Bennu", Nature Astronomy, 23 Jan 2025, doi:10.1038/s41550-024-02472-9, NTRS 20250001355 PDF (text extracted locally) | useful | Bennu bulk C 4.5 to 4.7 wt%, N 0.23 to 0.25 wt% (early analyses, confirmed); ammonia about 13.6 umol/g in the hot-water extract, about 40% of extract N; 121.6 g returned |
| 8 | WebSearch: `"Making Mars habitable" McKay Toon Kasting 1991 nitrogen requirement plants mbar buffer gas` | useful (lead) | The "about 10 mbar of nitrogen" minimum for plants appeared only in the search summary at this point |
| 9 | WebSearch: `Ryugu bulk nitrogen concentration wt% Yokoyama 2022 Science CI chondrite comparison elemental abundances` | thin | Okazaki et al. 2022 (noble gases and N) located; no bulk wt% in the results |
| 10 | WebSearch: `Stanford torus or O'Neill space colony nitrogen requirement atmosphere imported from Earth tonnes NASA SP-413` | thin | Wikipedia and NSS secondary: 50.8 kPa, 26.5% O2 (already in [LSS] A2); no tonnage |
| 11 | Opened: NTRS 19910063790 record, McKay, Toon, Kasting, "Making Mars habitable", Nature 352, 489-496 (1991) | useful | Abstract: CO2 release to 100 mbar; plants in 100 to 100,000 yr; O2-rich atmosphere "in perhaps 100,000 yrs"; breathable only "if sufficient N2 could be released from putative soil deposits"; **no nitrogen pressure in the abstract** |
| 12 | WebSearch: `nss.org 75SummerStudy space settlements design study atmosphere nitrogen "from Earth" mass of atmosphere tonnes` | thin | Pointer to the NSS copy of SP-413 |
| 13 | Opened: esdpubs.nasa.gov "Making Mars Habitable"; nss.org SP-413 index | dead at the tool | WebFetch session limit reached; retried by curl (rows below) |
| 14 | Opened (curl): NTRS API PDF route for 19910063790 (McKay, Toon, Kasting 1991) | dead at the sources | NTRS returns a JSON stub, no PDF (Nature article, not deposited) |
| 15 | WebSearch: `Mars habitability limits plants nitrogen partial pressure "1 mbar" OR "10 mbar" N2 nitrogen fixation McKay Marinova terraforming table` | thin | Search summary again attributes "about 10 mbar of nitrogen" for plants to McKay et al. 1991 via the Turyshev preprint; no opened page states it; **not used as a figure** |
| 16 | Opened (curl): S. G. Turyshev (JPL), "Terraforming Mars: Mass, Forcing, and Industrial Throughput Constraints", arXiv:2603.00402 (version dated 21 Apr 2026), PDF text | useful | Eq. 21: pN2 = 50 kPa buffer gas on Mars needs about 1.9 x 10^18 kg N2; Eq. 22: import energy about 10^25 J at 5 km/s; Eq. 26: regional 1.35 x 10^16 kg per 10^6 km^2 at 50 kPa; NH3 as carrier needs 1.21 kg per kg N2; Mars fixed-N inventory "poorly constrained" |
| 17 | WebSearch: `McKay Marinova 2001 "The Physics, Biology, and Environmental Ethics of Making Mars Habitable" table habitability limits plants nitrogen partial pressure` | thin | Paper located (Astrobiology 1, 89-109, 2001); table not reachable |
| 18 | Opened: NTRS API record 20040087967 (McKay and Marinova 2001) | thin | Abstract only: N2 total "unknown", "may be enough in the subsurface"; no plant N2 threshold; no PDF |
| 19 | WebSearch: `Stern 2015 PNAS Curiosity nitrate Mars sediment "ppm" nitrogen indigenous Rocknest John Klein Cumberland abundance` | useful (lead) | Pointed to the PNAS paper; numbers confirmed only from row 22 |
| 20 | Opened: escholarship.org item 5g07m7vx (Stern et al. 2015) | dead at the sources | Page returned empty to the fetch tool |
| 21 | Opened: HAL insu-01149378 (Stern et al. 2015) | dead at the sources | Anubis anti-bot page |
| 22 | Opened (curl): Europe PMC REST record for doi:10.1073/pnas.1420932112 (Stern et al., PNAS 112(14), 4245-4250, 2015; PMC4394254), abstract | useful | Nitrate equivalent 110-300 ppm (Rocknest), 70-260 ppm (John Klein), 330-1,100 ppm (Cumberland); N fixation by impact or lightning |
| 23 | Opened (curl): NASA SP-413, "Space Settlements: A Design Study" (1977), NSS mirror, table of contents and Chapters 3, 4, 5, 6, appendices 4A-4C, 5A, 5B, 6A (https://space.nss.org/settlement/nasa/75SummerStudy/) | useful | Table 4-1: single torus volume 6.9 x 10^7 m^3, mass of atmosphere 44 kt; cylinder 14,612 kt; Table 4-3: O2 22.7, N2 26.6, total 50.8 kPa; "Because nitrogen must come from the Earth ... a substantial expense"; Table 5-3 internal masses (plants 5,000 t; soil 220,000 t); Table 5-13 lunar base "Atmosphere leak replacement 18 t/yr" for 150 people; Ch. 6: H, C, N "not present in lunar ore"; Ch. 4: comets and asteroids "possibly nitrogen" |
| 24 | WebSearch: `Ceres nitrogen abundance ammonium phyllosilicates Dawn wt% nitrogen content bulk Ceres ammonia inventory` | thin | Dawn VIR: ammoniated phyllosilicates widespread, NH4 salts in faculae; **no wt% nitrogen or bulk inventory in any result**; died at the sources (the quantity seems unpublished) |
| 25 | WebSearch: `comet 67P ammonium salts nitrogen budget NH3 abundance relative to water percent Altwegg 2020 Nature Astronomy missing nitrogen` | thin | Altwegg et al. 2020: ammonium salts explain the comae's N depletion; no bulk N mass fraction in the results |
| 26 | WebSearch: `Fray 2017 COSIMA 67P dust nitrogen N/C ratio 0.035 MNRAS; Bardyn 2017 carbon-rich dust 45 wt% organic matter` | useful (lead) | NOTE: the "0.035" in my query was recalled; the search summary returned N/C 0.018 to 0.06, mean 0.035 +/- 0.011 (27 particles), and "45 wt%" organic matter; neither confirmed on an opened page (rows 27 to 30) |
| 27 | Opened: utupub.fi full record (Fray et al. 2017) | dead at the sources | HTTP 403 |
| 28 | Opened: IAS Paris-Saclay node/1614 (Fray et al. 2017) | dead at the sources | HTTP 404 |
| 29 | Opened (curl): Crossref API title queries for both COSIMA papers | useful (bibliographic only) | Fray et al., MNRAS 469 (Suppl. 2), S506-S516, doi:10.1093/mnras/stx2002; Bardyn et al., MNRAS 469, S712-S722, doi:10.1093/mnras/stx2640 |
| 30 | Opened (curl): doi.org redirects to academic.oup.com for both; HAL insu-02766152; Europe PMC and arXiv API queries; TU Wien publik PDFs 275238, 275240, 284586, 276382 | dead at the sources | Cloudflare challenge (OUP); Anubis (HAL); no Europe PMC or arXiv record; TU Wien timed out. **Comet N figures therefore enter only as an unconfirmed lead** |
| 31 | WebSearch: `xenon krypton world production tonnes per year air separation byproduct concentration ppm atmosphere supply electric propulsion` | useful (lead) | gasworld (trade press), Linde pages, a Southampton review (eprints) and an Air Liquide workshop deck |
| 32 | Opened (curl): Southampton eprints 483809, "Review of Alternative Propellants in Hall Thrusters" (accepted manuscript PDF) | dead at the sources | Returned an HTML page, not the PDF |
| 33 | Opened (curl): Air Liquide, "Rare Gases: focus on Xe", presentation to the XeSAT/SLAC workshop, 25 Oct 2023, indico.slac.stanford.edu (PDF, 24 pp.) | useful | Air: Kr 1.14 ppm, Xe 0.087 ppm, Ne 18.2 ppm; Kr and Xe are byproducts of oxygen production; "AL Estimate of total natural Xe production WW: 60-100t/y"; space use: "Krypton preferred to Xenon for 'constellations'". Industry presentation (template marked internal, publicly posted) |
| 34 | WebSearch: `SpaceX Starlink V2 mini argon Hall thruster thrust specific impulse 2023 first argon flight` | useful (lead) | Trade press; "krypton is too rare" (Musk, via TechCrunch) |
| 35 | Opened: Via Satellite (satellitetoday.com), "SpaceX Shares Details of Higher Bandwidth V2 Mini Starlink Satellites", 27 Feb 2023 | useful (secondary) | Argon Hall thrusters, 170 mN, "2.4 times the thrust and 1.5 times the specific impulse" of first-generation thrusters, attributed to SpaceX; the 4.2 kW and 2,500 s figures appear only in the search summary |
| 36 | WebSearch: `Venus wind power turbine lander or aerobot wind energy harvesting NASA study watts surface winds Venus` | useful | NTRS 20240000076 located; Space Apps Challenge team pages (student work) not used; JPL HAR-V figures (0.3 to 1.3 m/s, 9 W goal) appear only in the summary, not used |
| 37 | Opened (curl): A. Colozza (NASA GRC), "Feasibility Analysis for a Small Vertical-Axis Wind Turbine on Venus Surface", NASA/CR-20240000076 (2025), full text | useful | Surface density 67 kg/m^3; most probable wind about 0.5 m/s; design point 0.5 m diameter, 0.5 m blades, 3 blades, 41% efficiency, **3.57 Wh per hour**; needs at least 1.8 m/s to self-start; a starting motor required |
| 38 | WebSearch: `Venus lander lithium combustion carbon dioxide power system stored chemical energy Stirling NASA Glenn Penn State "lithium" CO2 Venus atmosphere oxidizer` | useful | ALIVE (NIAC/COMPASS) located; Penn State pure.psu.edu records (not opened) |
| 39 | Opened (curl): Paul, Oleson, McGuire et al., "Advanced Lithium Ion Venus Explorer (ALIVE)", NASA COMPASS/NIAC report, NTRS 20190000924 (2019), abstract and full text | useful | Li burned with atmospheric CO2: about 14,000 W of heat at 1,300 C; Duplex Stirling gives about 300 W electric and removes about 300 W; Li fuel 200 kg for 5 days; power system 259 kg; payload vessel at 25 C |
| 40 | WebSearch: `Licht molten carbonate electrolysis CO2 to carbon nanotubes C2CNT energy kWh per tonne carbon electrolysis voltage efficiency` | useful (lead) | arXiv 1710.07246; RSC 2025; patents (not used) |
| 41 | Opened (curl): S. Licht (GWU), "Carbon dioxide to carbon nanotube scale-up", Team C2CNT Carbon XPRIZE round 2 submission extract, arXiv:1710.07246 (Oct 2017) | useful (preprint, not peer reviewed) | Molten Li2CO3 at 770 C; about 1 V and 4 electrons per CO2 (observed 0.8 to 2 V); "2.4 MWh per ton CO2", about 7 MWh per t CNT after a turbine credit; small-scale crucible runs described; the "modules of 100 t CO2 per year" and "wools for textiles" phrases came from the search summary and are **not** in the text read, so not used |
| 42 | WebSearch: `USGS Mineral Commodity Summaries 2025 sulfur sulfuric acid uses phosphate fertilizer percent world production` | useful | USGS MCS PDFs located |
| 43 | Opened (curl): USGS, Mineral Commodity Summaries 2026, "Sulfur" (S. H. Saloum), https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-sulfur.pdf | useful | World sulfur production 84 Mt (2025e) vs 83.9 Mt (2024); "About 90% of sulfur consumed was in the form of sulfuric acid" (US); uses: processing phosphate rock into fertilizer, high-pressure acid leaching of nickel; price $180/t (US 2025e) |
| 44 | WebSearch: `FAOSTAT world nitrogen fertilizer use 2022 million tonnes N agricultural use total nutrient analytical brief` | useful | FAO brief located; a Statista "314 million tons" figure (product mass, not N) not used |
| 45 | Opened (curl): FAO, "Inorganic fertilizers 1990-2021", FAOSTAT Analytical Brief 68 (2023), https://www.fao.org/3/cc6823en/cc6823en.pdf | useful | 2021: 109 Mt N, 46 Mt P, 40 Mt K used in agriculture; total nutrient use about 25 kg per capita |
| 46 | WebSearch: `NASA study Mars crewed mission Venus swingby opposition class trajectory delta-v reduction NTRS Venus flyby Mars round trip` | useful (qualitative) | NTRS records; space.com (secondary, not used) |
| 47 | Opened (curl): NTRS API records 20130010385 (Drake 2013, no abstract), 20205007668, 19710008021, 19960023699, 19870008296, 20120006135 | thin | Abstracts confirm Venus swing-bys lower IMLEO or delta-v for opposition-class Mars missions and add abort options; **no delta-v saving is stated in any abstract** |
| 48 | Opened (curl): Prasad, Adinolfi, Evans, Simon, "Conceptual Design and Analysis of a Deep Space Habitat on a Venus Flyby", AIAA ASCEND 2020, NTRS 20205007668, full text | useful (qualitative) | Opposition-class mission about 760 d (habitat sized for 1,100 d) with a Venus flyby; habitat passes 0.62 AU (bound 0.55 AU); "Venus flybys are often leveraged to lower the total delta-V"; no delta-v figure |
| 49 | WebSearch: `Parker Solar Probe seven Venus gravity assists perihelion lowered 9.86 solar radii NASA mission page` | useful (lead) | APL ISSFD paper located; Wikipedia not used |
| 50 | Opened (curl): Guo, McAdams, Ozimek, Shyong (JHU APL), "Solar Probe Plus Mission Design Overview and Mission Profile", ISSFD 24 (2014), PDF | useful | Launch C3 up to 154 km^2/s^2; seven Venus gravity assists (V7GA) lower perihelion to 9.86 R_S with "no additional deep space maneuvers"; "a spacecraft cannot get close to the Sun from Earth directly"; 6.4 yr to complete the flybys; closest flyby 317 km |
| 51 | WebSearch: `Venus D/H ratio 150 times Earth Pioneer Venus Donahue 1982 Science water lost ocean evidence deuterium` | useful (lead) | arXiv reviews; the "150 +/- 30" and "4 to 525 m" figures in the summary are attributed to Way et al.; checked against row 52 instead |
| 52 | Opened (curl): Garvin, Getty, Arney et al., "Revealing the Mysteries of Venus: The DAVINCI Mission", arXiv:2206.07211 (2022; Planetary Science Journal) | useful | D/H "at least 120 times that on Earth"; Pioneer Venus ~0.016 (~100x); ground-based 0.019 +/- 0.006 (120 +/- 40x); Venus Express implies ~0.025 bulk and up to ~0.06 at 70-95 km; noble-gas and D/H measurements as the record of water loss and possible past oceans; Xe only upper limits |
| 53 | WebSearch: `NASA Glenn silicon carbide JFET high temperature electronics applications jet engine sensors deep well drilling automotive spinoff 500 C` | useful | NTRS records; IEEE Spectrum (secondary, not used) |
| 54 | Opened (curl): NTRS API abstracts 20180003391 (Neudeck, Spry, Krasowski, Prokop, "Yearlong 500 C Operational Demonstration of Up-Scaled 4H-SiC JFET Integrated Circuits", 2018) and 20160014879 (Spry, Neudeck et al., 2016) | useful | Over one year at 500 C in air; 175 or more transistors per chip (7-fold over 24 in 2016); applications named by NASA: "combustion engine sensing and control, planetary exploration, deep-well drilling monitoring" |
| 55 | WebSearch: `continuous basalt fiber production melt temperature 1450 C tensile strength GPa review composition requirements SiO2 basalt suitability` | thin | Patents and an MDPI review; the summary's composition window (SiO2 45 to 60 wt%, Al2O3 12 to 25 wt%) is from a patent; not used |
| 56 | Opened (curl): MDPI Fibers 7(7):65 (basalt fiber review); Shi 2020 PDF (baztech) | dead at the sources | MDPI returned a 406-byte block page; baztech returned HTML, not the PDF |
| 57 | Read-only: `life_support_lowg_power_structures.md` G3 (basalt glass and fiber) | useful | Cited as [LSS] G3: basaltic simulant melted at 1,200 C (solar) and 1,450 to 1,600 C (JSC-1) to make glass and fiber (secondary there) |
| 58 | WebSearch: `graphite versus polyethylene galactic cosmic ray shielding effectiveness dose equivalent per areal density hydrogen content NASA HZETRN comparison carbon` | thin | Qualitative only: hydrogen-rich polyethylene outperforms carbon and aluminum per areal density; no dose-per-g/cm^2 numbers in the results |
| 59 | Opened (curl): NTRS API abstract 20040073505, "Graphite/Ultra-High Modulus Polyethylene Hybrid Fiber Composites ... for Cosmic Radiation Shielding" | thin | "the high hydrogen (H) content of polyethylene makes the material an excellent shielding material"; no numbers |
| 60 | Opened (curl): NASA NSSDC fact sheets, Earth (updated 15 Nov 2024), Venus (11 Jan 2024), Mars (19 May 2025), Mercury (11 Jan 2024) | useful | Escape speed Earth 11.186, Venus 10.36, Mars 5.03 km/s; surface gravity Venus 8.87 m/s^2 (0.903 of Earth), Mars 3.73; irradiance Venus 2,601.3, Earth 1,361.0, Mars 586.2 W/m^2; Earth atmosphere 5.1 x 10^18 kg, M 28.97 |
| 61 | WebSearch: `delta-v required to reach low Earth orbit including gravity and drag losses 9.4 km/s NASA technical report launch vehicle ascent losses typical values` | thin (secondary) | Course notes and slides: "between 9 and 10 km/s" to low Earth orbit with 1.5 to 2 km/s of losses; NOTE the "9.4" in my query was recalled; used only as a secondary bracket |
| 62 | WebSearch (extended): `Venus cloud habitat agriculture greenhouse crops sunlight carbon dioxide aerostat food production study paper` | dead at the sources | Blogs, a fiction encyclopedia, Medium posts; **no agricultural study of a Venus cloud habitat exists in what was found** |
| 63 | WebSearch (extended): `Venus atmosphere power generation temperature gradient between altitudes thermoelectric or Stirling balloon altitude cycling energy harvesting watts study` | useful | No altitude-cycling heat-engine study with numbers; led to the NIAC power-beaming final report and an Acta Astronautica 2023 paper (not opened, paywall) |
| 64 | Opened (curl): E. Brandon et al. (JPL), "Power Beaming for Long Life Venus Surface Missions", NIAC 2019 Phase I Final Report, nasa.gov PDF | useful | Microwave beaming (2 to 100 GHz) "not technically feasible, due to significant atmospheric absorption"; orbit-to-surface beaming also infeasible; laser from an aircraft below the clouds proposed; array 271 W/m^2 at 47 km (3.7 m^2 per kW); 112 W/m^2 at 20 km; LiAl-FeS battery at 465 C, 80 Wh/kg; surface winds "very uncertain", may approach 0 m/s |
| 65 | Re-opened: Air Liquide deck (row 33), atmospheric composition slide | useful | Earth air: N2 78.09%, O2 20.94%, Ar 0.93%, Ne 18.2 ppm, Kr 1.14 ppm, Xe 0.087 ppm; Kr and Xe extraction needs very large air separation plants (1,000,000 m^3 of air per 1 m^3 of Kr-Xe) |
| 66 | WebSearch: `molten carbonate CO2 electrolysis carbon deposition energy consumption kWh per kg carbon cell voltage 2.0 V Li2CO3 review 2023 solid carbon product` | useful (second angle) | LUT/TAU HYGCEL reports; RSC Advances 2017; an Elsevier article (tuni.fi copy) |
| 67 | Opened (curl): Tampere University repository PDF of S1452398124000968 | dead at the sources | HTML returned, not the PDF |
| 68 | Opened (curl): LUT University / Tampere University, HYGCEL WP5 Task 5.2, "Energy efficient CO2 electrolysis" (project report, undated, about 2024) | useful (qualitative) | Molten carbonate electrolysis "has not yet reached a commercial stage"; products are a mix of nanotubes, nano-onions, platelets and amorphous carbon depending on electrolyte, temperature (700 to 775 C) and cathode; corrosion degrades product purity; no kWh figure |
| 69 | Opened (curl): NSSDC Mercury fact sheet (row 60), radius row | useful | Mercury volumetric mean radius 2,439.7 km |
| 70 | Opened (curl): NIST CODATA, Faraday constant, https://physics.nist.gov/cgi-bin/cuu/Value?f | useful | 96,485.332 12 C/mol (exact) |
| 71 | Calculations run locally (Python 3, `python3 -I`) on 2026-10-11; script and output kept in the scratch folder `benefits_of_mining_venus/scripts/` (calc.py, calc_output.txt), not in the repository | n/a | See Derived figures |
| 72 | Re-opened: Brandon et al. NIAC report (row 64), sections 2.2.4 and 3.4.2 | useful | Surface winds "very uncertain and likely to be too low (~2 m/s) or too sporadic" for a long-life lander; below the clouds the upward flux is about the downward flux minus 40 W/m^2, so bifacial or vertical cells gain; the 271 W/m^2 at 47 km comes from their Fig. 10 model |
| 73 | WebSearch (extended): `importing nitrogen to Mars from Titan or Venus atmosphere terraforming buffer gas source comparison paper` | thin | University lecture slides and a Cloudflare-blocked thesis; no peer-reviewed source comparison |
| 74 | Opened (curl): LMU Digital Commons thesis "System Engineering Analysis of Terraforming Mars ..." | dead at the sources | Cloudflare challenge page |
| 75 | Opened (curl): M. C. Miller (U. Maryland), ASTR 380 lecture slides 27, "Terraforming Other Planets" (2009) | thin (secondary) | Options for Mars N2: Earth, Venus ("requires separation of 3.5% N2 from 96.5% CO2"), Titan (98.4% N2, "approx. 9x10^18 kg N2"); buffer gas "at least twice as much ... as O2", 32 kPa; lead only, no figure used |
| 76 | Opened (curl): Europe PMC record, Okazaki et al., "Noble gases and nitrogen in samples of asteroid Ryugu record its volatile sources and recent surface evolution", Science (2023 print), doi:10.1126/science.abo0431 | thin | Abstract supports "a close relationship between Ryugu and CI chondrites"; no bulk N wt% in the abstract (second angle on row 9: still no Ryugu number) |
| 77 | WebSearch (extended): `Venus in-situ resource utilization review resources available cloud level carbon nitrogen sulfur oxygen propellant benefits human exploration architecture 2024 2025` | useful | No review sizing benefits; led to VIP-INSPR (NIAC 2016); Acta Astronautica 2026 ISRU-balloon paper (paywall, abstract already covered by Horn et al. in [VE]); EurekAlert news on Lu et al. 2026 (already in [VE]) |
| 78 | Opened (curl): R. V. Bugga et al. (JPL), "Venus Interior Probe Using In-situ Power and Propulsion (VIP-INSPR)", NIAC 2016 Phase I report, nasa.gov PDF | useful | Hydrogen from cloud acid needs "either a very large pump or a very long dwell time" (blower above 10,000 L/min for dwell under 5 days); water vapor capture judged simpler (no sulfur poisoning); minimum work to concentrate water from 5 ppm, 357.7 Wh per 42.3 mol; SOEC nickel electrodes are poisoned by sulfur; 84.7 g of H2 stores 2 kWh at 60% fuel-cell efficiency. **Its Table 2 air volumes are about 100 times smaller than the arithmetic gives** (Conflicts 3) |
| 79 | Calculations re-run (D-P, D-Q added) on 2026-10-12 | n/a | calc.py and calc_output.txt in the scratch folder |
| 80 | **Tally** (rows 1 to 79): 32 web searches (4 in extended mode: rows 62, 63, 73, 77); about 45 pages or documents opened; 12 rows marked dead (13, 14, 20, 21, 27, 28, 30, 32, 56, 62, 67, 74): 11 died at the sources (paywalls, Cloudflare or Anubis pages, HTML in place of a PDF, empty pages) and 1 at the tool (row 13, a WebFetch session limit, recovered by curl); row 62 is a dead end that suggests the study sought (agriculture in a Venus cloud habitat) does not exist; 16 rows marked thin | n/a | Unreadable: Stern 2015 full text, Fray 2017 and Bardyn 2017 (OUP Cloudflare, HAL), the Southampton Hall-propellant review, the MDPI basalt-fiber review, the LMU terraforming thesis, the Tampere molten-carbonate paper |

## 3. Findings

### 3.1 Atmospheric products, their amounts, and their end uses (checklist 1)

Inventories, concentrations and extraction energies are [VE] 3.1 to 3.3 and D1 to D5; only the end uses and the new numbers
are added here.

| Quantity | Value and units | Source (publisher, title, URL, date) | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Element inventory of the air (cited) | C 1.28 x 10^20 kg; O 3.41 x 10^20; N 1.08 x 10^19 (0.84 to 1.42 x 10^19); S in gases 5.5 x 10^16; Ar 2.9 x 10^16; Kr about 4 x 10^13; H 6.7 x 10^14 kg; cloud droplets about 5 x 10^13 kg | [VE] 3.1, D1, D3 (NSSDC fact sheet; Johnson and de Oliveira 2019) | Derived from primary | Xe: below 40 ppb, so **below 5.8 x 10^13 kg** (DERIVED D-A, an upper limit only; DAVINCI paper: "Only upper limits exist for xenon") | High for C, O, N; medium for trace species |
| Concentration at a platform (cited) | Air at 55 km holds about 250 g of C and 21 g of N per m^3; 3.75 t of air per t of C, 44 t of air per t of N (4,000 and 47,000 m^3 at 55 km) | [VE] D2; DERIVED D-C, D-R | Derived | none | Medium |
| **Oxygen** (breathing, oxidizer) | Solid-oxide electrolysis of CO2: MOXIE 6 to 12 g/hr (DEMONSTRATED on Mars); full-scale plant 5.7 kWh per kg O2 (ENGINEERING-STUDIED); floor 4.9 kWh/kg ([VE] 3.3). DERIVED D-M: a 1 kg/hr plant (5.67 kW) supplies **29 people** at 0.816 kg O2 per person-day, about 190 W per person | [VE] 3.3; [LSS] A1 (BVAD 0.816 kg/CM-d) | Primary / derived | Wheeler 2019 (via [LSS]): 0.83 kg/d | High (chemistry); medium (plant scale) |
| **Carbon monoxide** (fuel, lifting gas) | Co-product of the same electrolysis; CO/LOX burns at Isp 250 s; CO lifts 0.33 kg/m^3 at 55 km; CO and O2 replace lost helium and can be recombined for power at night in a 10-year ISRU aerobot design | [VE] 3.3, 3.4, 3.7 (Landis and Oleson 2024; Horn et al. 2026) | Primary | none | Medium |
| **Solid carbon** (nanotubes, fibers, graphite) from CO2 | Molten Li2CO3 electrolysis at 770 C, about 1 V and 4 electrons per CO2 (observed 0.8 to 2 V): "2.4 MWh per ton CO2" = **8.8 MWh per t of carbon** (DERIVED D-H); the enthalpy floor for CO2 to C + O2 is 9.1 kWh per kg C, so the 1 V figure sits at the thermoneutral point; each kg of C also yields 2.66 kg of O2. Status: laboratory and pilot; "has not yet reached a commercial stage"; product is a mix of tubes, onions, platelets and amorphous carbon that depends on electrolyte, 700 to 775 C and cathode, and corrosion degrades purity | S. Licht (GWU), "Carbon dioxide to carbon nanotube scale-up", arXiv:1710.07246 (2017, XPRIZE submission, not peer reviewed); LUT/Tampere, HYGCEL WP5 T5.2 report (about 2024) | Preprint / project report | Two independent groups; numbers from one only | Medium for chemistry and energy; low for product quality at scale. **Benefit:** a structural carbon product that **needs no hydrogen**. **Cost:** the electrolyte is a lithium salt, which Venus does not supply ([SYN] 4: lithium is an import dependency) |
| **Polymers and plastics** | Need hydrogen: polyethylene is 14.4% H by mass (DERIVED D-G); all of Venus's hydrogen would make at most 4.7 x 10^15 kg of polyethylene, and getting it costs 0.7 to 4.6 million m^3 of air per kg of H (D-P) | DERIVED from [VE] D1 and CIAAW atomic weights | Derived | SP-413: plastics and wood "must come from Earth, or be made from carbon, nitrogen and hydrogen brought from Earth" | High (arithmetic) |
| **Nitrogen** (buffer gas, fertilizer) | Separation floor 0.30 to 0.45 MJ per kg N2 ([VE] D5; no real plant figure). As buffer gas: usable directly. As fertilizer: ammonia needs 0.216 kg of H per kg of N; Venus's whole hydrogen inventory fixes at most 3.1 x 10^15 kg of N as NH3, **0.03% of Venus's nitrogen**, though that equals 28,000 years of world fertilizer N at 109 Mt/yr (D-G). **The limit on Venus fertilizer is hydrogen, not nitrogen** | [VE] D5; FAO Analytical Brief 68 (2023); DERIVED D-G | Primary / derived | none | High (arithmetic); low for any rate (no extraction study) |
| **Argon** (electric-propulsion propellant, inert gas) | 70 ppm by volume: 15,500 kg of Venus air per kg of Ar, against 78 kg of Earth air (Earth air 0.93% Ar), **about 200 times leaner** (D-A). Argon Hall thrusters are flying (Starlink V2 Mini, from Feb 2023; 170 mN, "2.4 times the thrust and 1.5 times the specific impulse" of the first-generation thrusters) | Air Liquide, "Rare Gases: focus on Xe", XeSAT/SLAC workshop, 25 Oct 2023; Via Satellite, 27 Feb 2023 (citing SpaceX); DERIVED D-A | Industry deck / secondary | TechCrunch quote (via search): "krypton is too rare" | Medium (flight status from trade press) |
| **Krypton and xenon** | Kr 47 ppb: 1.1 x 10^7 kg of air per kg Kr (36 times leaner than Earth air at 1.14 ppm); Venus holds about 2.6 times Earth's atmospheric krypton in absolute mass. Xe: only an upper limit (below 40 ppb). World natural xenon output 60 to 100 t/yr, a byproduct of oxygen plants; krypton "preferred to Xenon for 'constellations'" | Air Liquide 2023 deck; [VE] 3.1; DERIVED D-A | Industry deck / derived | [SYN] 3: world xenon about 65 t/yr | Medium |
| **Sulfur and sulfuric acid** | Gas-phase S 5.5 x 10^16 kg (= 650,000 years of world sulfur production at 84 Mt/yr, D-L); cloud droplets 75 to 92 wt% H2SO4 holding about 1.2 to 1.5 x 10^13 kg of S. On Earth "about 90% of sulfur consumed was in the form of sulfuric acid" (US), mainly to process phosphate rock into fertilizer and, increasingly, to leach nickel ore under pressure | USGS, Mineral Commodity Summaries 2026, "Sulfur"; [VE] 3.1, D3 | Primary | none | High (inventory); the acid's local use for leaching rock at Venus is SPECULATIVE (no study) |
| **Water and hydrogen** | Vapor about 30 ppmv below the clouds, about 6 ppm above; droplets 10 to 24 mg/m^3 in the lower cloud. DERIVED D-P: per kg of hydrogen, 0.7 x 10^6 m^3 of air at 30 ppmv vapor, 3.8 to 4.6 x 10^6 m^3 at 5 to 6 ppmv, and 1.0 to 3.6 x 10^6 m^3 from droplets. A JPL study judged vapor capture simpler than acid capture (no sulfur to poison the electrolyzer, no decomposition step) | Bugga et al. (JPL), VIP-INSPR, NIAC 2016 Phase I report; [VE] 3.1, D3 | Primary (study report) | Minimum work to concentrate water from 5 ppm, 358 Wh per 42.3 mol, reproduced here (D-P) | Medium (the report's air volumes are wrong, Conflicts 3) |
| **Deuterium** (a concentration benefit, no study) | D/H about 0.016 (Pioneer Venus, ~100 times terrestrial), 0.019 +/- 0.006 (ground-based, 120 +/- 40 times), about 0.025 bulk and up to about 0.06 at 70 to 95 km (Venus Express). DERIVED D-K: Venus holds only 2 to 3 x 10^13 kg of D, **about 0.06% of the deuterium in Earth's hydrosphere**, but at 100 to 160 times the concentration | Garvin et al., "Revealing the Mysteries of Venus: The DAVINCI Mission", arXiv:2206.07211 (2022) | Primary | Search summary: Donahue et al. 150 +/- 30 times (not opened) | Medium for D/H; SPECULATIVE as a resource |
| Shielding | The atmosphere itself is the shield (1,290 g/cm^2 above 50 km, [MVT] 3.8). As an exportable shield material, carbon is inferior to hydrogen-rich polyethylene per unit areal density (qualitative only; no dose numbers found) | NTRS 20040073505 (abstract); search summaries (row 58) | Primary (abstract) / secondary | none | Low (no numbers) |
| Life-support consumables | O2 (above), N2 (above), CO2 for crops. But crops prefer 0.10 to 0.20 kPa of CO2 and lose productivity at about 1.0 kPa, and crew limits are about 0.5 kPa ([LSS] A2): Venus air (96.5% CO2) must be scrubbed, not breathed or fed to plants directly | [LSS] A2 (BVAD) | Primary (cited) | SP-413 Table 4-3: CO2 below 0.4 kPa | High |
| Lifting gases made locally | CO or N2 0.33, O2 0.25, breathable air 0.31 kg/m^3 at 55 km; H2 and He would lift 0.85 to 0.89 but are scarce | [VE] D-lift | Derived (cited) | [MVT] 3.9 | Medium |

### 3.2 The nitrogen and carbon case (checklist 2)

**Who needs nitrogen, and how much:**

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Rotating habitat (SP-413 torus, 10,000 people) | Atmosphere 22.7 kPa O2 + 26.6 kPa N2 (50.8 kPa total); volume 6.9 x 10^7 m^3; **mass of atmosphere 44 kt**, so about 22 kt of N2, **about 2.2 t of N2 per person** (DERIVED D-B). Cylinder option: 14,612 kt of atmosphere (about 7.3 Mt N2). "Because nitrogen must come from the Earth, its inclusion in the habitat's atmosphere means there is a substantial expense"; hydrogen, carbon and nitrogen "are not present in lunar ore" | NASA SP-413, "Space Settlements: A Design Study" (1977), Tables 4-1, 4-3, Ch. 4 and 6, NSS mirror https://space.nss.org/settlement/nasa/75SummerStudy/ | Primary (NASA study) | DERIVED D-Q: 0.611 kg/m^3 x 6.9 x 10^7 m^3 = 42 kt, within 4% | High |
| Make-up nitrogen for leakage | SP-413 lunar base: "Atmosphere leak replacement 18 t/yr" for 150 people (120 kg per person-year). DERIVED D-Q for the torus: 110 to 220 kg N2 per person-year at Biosphere 2's 5 to 10% per year, 400 to 1,130 kg at BVAD's spacecraft design leak rates of 0.05 to 0.14% per day | SP-413 Table 5-13; [LSS] A2 (BVAD Table 4-1), A4 (Biosphere 2) | Primary / derived | none | Medium (design allowances scaled to a different structure) |
| Mars, open-air buffer gas | 50 kPa of N2 over Mars needs about **1.9 x 10^18 kg** (DERIVED check 1.94 x 10^18; 3.87 x 10^16 kg per kPa); a 10^6 km^2 region at 50 kPa needs 1.35 x 10^16 kg; importing ammonia as the carrier needs at least 1.21 kg per kg of N2; delivery at 5 km/s costs about 10^25 J of kinetic energy alone; Mars's own fixed nitrogen is "poorly constrained" and shallow regolith would need percent-level N | S. G. Turyshev (JPL), arXiv:2603.00402 (21 Apr 2026, preprint), Eq. 21, 22, 26, 25 | Preprint | DERIVED from Mars radius ([MVT]) and NSSDC gravity: 1.94 x 10^18 kg | Medium (order-of-magnitude paper) |
| Venus's nitrogen against that need | Global Mars buffer = **13 to 23% of Venus's nitrogen**; one 10^6 km^2 region = 0.13%; one SP-413 torus = 2 x 10^-12 of it (D-B). Mars's present N2 (4.2 x 10^14 kg) is 0.022% of the 50 kPa target | DERIVED D-B | Derived | none | Medium (inventory range carries the N2 fraction conflict, [VE] Conflicts 1) |
| Mars's own nitrogen | Nitrate equivalent 110 to 300 ppm (Rocknest sand), 70 to 260 ppm (John Klein) and 330 to 1,100 ppm (Cumberland mudstone): **4,000 to 63,000 t of material per t of N** (D-C) | Stern et al., PNAS 112(14), 4245-4250 (2015), Europe PMC abstract | Primary | Turyshev 2026: "poorly constrained" | Medium (three sites) |
| Agriculture | World agriculture used 109 Mt of N in fertilizer in 2021 (with 46 Mt P, 40 Mt K; about 25 kg of nutrients per person). In a closed habitat the N recycles; no crop nitrogen-inventory figure for a habitat was found (Open threads) | FAO, FAOSTAT Analytical Brief 68 (2023) | Primary | none | High for the world figure |

**The alternatives, per tonne of nitrogen or carbon:**

| Source | N mass fraction; t of feed per t N | C; t of feed per t C | Cost to reach the user | Source |
|---|---|---|---|---|
| **Venus air** | 2.25%; **44** | 26.7%; **3.75** | About 9 km/s from the cloud deck to orbit at Isp 250 s (payload 0.15 to 0.56%); 11.8 km/s ideal from 55 km straight onto a Mars or Mercury transfer (D-D) | [VE] D1, 3.7; D-C, D-R |
| **Earth air** | 75.5%; **1.3** | at 350 ppm CO2, 0.0145%; 6,900 (air only; Earth's other carbon sources not researched) | 9 to 10 km/s to low orbit (secondary bracket); 11.6 km/s ideal onto a Mars transfer; hydrogen-based propellant available (RS-25 class 452 s, [SYN] 3) | Air Liquide 2023; NSSDC Earth; D-C, D-R |
| **CI-type carbonaceous asteroid** | 0.295%; 339 | 3.48%; 29 | Main belt to Mars 1.91 km/s departure (3.76 all-propulsive), 464 d ([SYN] 3); release by heating (more than 95% of water below 600 C, [SYN] 4; N release temperature not found) | [VE] 3.2 (Lodders 2010) |
| **Bennu (returned sample)** | 0.23 to 0.25%; 400 to 435 | 4.5 to 4.7%; 21 to 22 | A near-Earth object (delta-v to Mars not researched here); ammonia about 40% of the hot-water-extractable N | Glavin et al., Nature Astronomy (2025), NTRS 20250001355 (row 7) |
| **Ryugu** | "close relationship" to CI (no bulk wt% in the abstract read) | n/a | as above | Okazaki et al., Science (2023) |
| **Ceres** | ammoniated phyllosilicates widespread; **no N mass fraction published in what was found** | n/a | Mars-Ceres v-infinity 3.27 / 2.81 km/s ([NW] D1) | row 24 |
| **Comets** | ammonium salts carry the "missing" N (Altwegg 2020); dust N/C atomic 0.018 to 0.06, mean 0.035 (**unconfirmed**: search summary of Fray et al. 2017; paper not opened) | dust about 45 wt% organic matter (**unconfirmed**, Bardyn et al. 2017) | not researched | rows 25 to 30 |
| **Moon (regolith)** | 81 ppm; 12,300 | 124 ppm; 8,100 | 2.52 km/s to low Earth orbit with aerocapture ([SYN] 3) | [VE] 3.2 (Crawford 2015) |
| **Mars soil nitrate** | 16 to 250 ppm N; 4,000 to 63,000 | n/a | in place | Stern 2015 |

**Reading (DERIVED D-D, D-E, D-S).**

- **For Mars, Venus nitrogen is not competitive on any figure found.** From the cloud deck straight onto a Mars transfer is
  11.8 km/s ideal, almost exactly Earth's 11.6 km/s from its surface. But Venus offers only CO/LOX at 250 s, so the ideal mass
  ratio is **124 against 13.6** for hydrolox from Earth (a factor of 9.1), before Venus's ascent losses (about 1.7 km/s in the
  studied 9 km/s) and before the studied payload fractions (0.15 to 0.56% to low orbit alone). Earth's air is also 34 times
  richer in nitrogen. The main belt reaches Mars with 1.91 km/s; its 339 t of rock per tonne of N is a processing burden but
  not a gravity-well burden.
- **For Mercury,** Venus is the nearer source in delta-v (16.8 km/s ideal from the cloud deck to low Mercury orbit, against
  21.0 km/s from Earth's surface), but at 250 s against 452 s the ideal mass ratio is still about 960 against 115 (D-S).
  Venus wins for Mercury only if the Venus ascent is done without rockets (no study exists; handwave H-1).
- **Energy to lift one kilogram off Venus on local propellant:** 175 to 650 kg of CO/LOX at 6.4 to 7.4 MJ/kg = **0.31 to 1.34 MWh
  per kg of payload to low Venus orbit** (D-E). One tonne a year to orbit needs 41 to 153 kW of continuous power, 317 to 1,185 m^2
  of array at 55 km (full-cycle mean), not counting the vehicles, which are the larger cost (180 to 670 kg of vehicle and
  propellant lifted per kg delivered; no reusable Venus ascent vehicle has been studied).
- **For carbon,** Venus air (3.75 t per t C) is far richer than Earth's air (6,900 t per t C) and richer than any carbonaceous
  asteroid (21 to 29 t per t C). The ascent cost is the same as for nitrogen, so carbon too is a benefit for use at Venus.
- **Who therefore uses Venus nitrogen and carbon:** platforms in Venus's atmosphere (no ascent), and whatever is in Venus orbit
  only at the ascent price. Every other customer has a cheaper source on the figures found.

### 3.3 Energy (checklist 3)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Sunlight above the atmosphere | 2,601.3 W/m^2, **1.911 times Earth's** 1,361.0 | NASA NSSDC Venus fact sheet (11 Jan 2024) | Primary | [MVT] 3.7: 2,613.9 mean (Colozza) | High |
| Array output by altitude (cited) | Triple-junction, noon, sun near zenith: 256 W/m^2 at 50 km, 404 at 55 km, 559 at 60 km; full-cycle mean of a flat panel 81, 129, 178 W/m^2; nights of about 50 to 66 hours on a drifting platform | [VE] 3.5, D9 (Landis and Haag) | Primary (model) | Brandon et al. 2019: 271 W/m^2 at 47 km, 112 W/m^2 at 20 km (Conflicts 1) | Medium |
| Two-sided collection | Upward reflected flux at 60 km about 90% of the downward flux ([MVT] 3.8); below the clouds the upward flux is about the downward flux minus 40 W/m^2, and the light is nearly isotropic below 60 km, so cells "could be oriented at any angle" | Brandon et al., "Power Beaming for Long Life Venus Surface Missions", NIAC 2019 Phase I Final Report (JPL) | Primary (study report) | [MVT] 3.8 | Medium |
| Power beaming into or within the atmosphere | Microwave beaming (2 to 100 GHz) "not technically feasible, due to significant atmospheric absorption"; an orbiting beaming platform likewise infeasible; laser beaming from an aircraft that descends below the clouds is the proposed route (10 W average at a lander) | Brandon et al. 2019 | Primary | none | Medium. **Consequence:** solar power collected in Venus orbit cannot be sent down into the atmosphere by microwave on this study's finding |
| Wind at the surface | Most probable about 0.5 m/s at 67 kg/m^3; a 0.5 m, three-blade vertical-axis turbine at 41% efficiency averages **3.57 W** (about 14 W/m^2 of swept area) and needs at least 1.8 m/s to start itself; a starting motor is required. A second study: surface winds "very uncertain and likely to be too low (~2 m/s) or too sporadic" for a long-life lander | Colozza (NASA GRC), NASA/CR-20240000076 (2025); Brandon et al. 2019 | Primary | DERIVED: 0.5 x 67 x 0.5^3 = 4.2 W/m^2 of wind power flux at 0.5 m/s | Medium |
| Wind at cloud level | A free balloon moves with the wind (100 to 120 m/s zonal), so the only usable wind is **shear between altitudes**: about 10 m/s across a multi-kilometer tether (TOBIAS, NIAC 2025, which uses it for power). DERIVED D-I: 0.5 rho v^3 at 55 km = 59, 468 and 3,750 W/m^2 at 5, 10 and 20 m/s; at the 41% turbine efficiency above, about 190 W/m^2 at 10 m/s | [VE] 3.5; DERIVED D-I | Primary / derived | none | Low (SPECULATIVE; no Venus tethered-turbine study with numbers) |
| Heat engines on the temperature gradient | Carnot limits between altitudes (DERIVED D-J, secondary VIRA-based temperatures): 45 to 55 km 22%; 50 to 60 km 24%; 50 to 70 km 34%; 40 to 55 km 28%; surface (735 K) to 55 km (300 K) 59%. Concepts: an aerobot whose working fluid doubles as lift gas, cycling in altitude (IAC-13, no numbers); a lithium heat store carrying "about 3.25 times more heat energy" than the work to lift it to 40 km, needing end-to-end efficiency above about 31% (NIAC 2020) | Yao et al., IAC-13,A3,5,5,x17862 (2013, abstract; row 5); NASA NIAC page, Noe Dobrea (PSI) 2020 (row 6); DERIVED D-J | Primary (abstracts) / derived | none | Low for any power figure (none published) |
| The atmosphere as an oxidizer | ALIVE: lithium burned with atmospheric CO2 gives about 14,000 W of heat at 1,300 C; a Duplex Stirling makes about 300 W and removes about 300 W from a 25 C payload vessel; 200 kg of Li runs 5 days; whole power system 259 kg. DERIVED: about 30 MJ of heat per kg of Li | Paul, Oleson, McGuire et al., NASA COMPASS/NIAC, NTRS 20190000924 (2019) | Primary (study) | none | Medium. **Benefit:** any reactive metal brought or made at Venus burns with free oxidizer |
| Energy budget of local industry (DERIVED) | 1 kg/hr of O2 (5.67 kW) needs about 44 m^2 of array at 55 km plus about 280 kWh to cross a 50-hour night ([VE] D9); 1 t/yr lifted to low Venus orbit on local CO/LOX needs 41 to 153 kW continuous (D-E); carbon at 8.8 MWh per t needs about 1.0 kW continuous per t/yr | [VE] D9; D-E; D-H | Derived | HAVOC robotic airship: 50.4 m^2, 11.6 kWe ([MVT] 3.9) | Medium |

### 3.4 Location as a hub (checklist 4)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Venus gravity assists, flown | Parker Solar Probe: seven Venus gravity assists lower perihelion to 9.86 solar radii with "no additional deep space maneuvers"; launch C3 up to 154 km^2/s^2; "a spacecraft cannot get close to the Sun from Earth directly"; 6.4 years to complete the flybys; closest pass 317 km. Mercury mission designs use two Venus flybys (the Yen-type chemical route, the BepiColombo study case, the 2035 Mercury Lander concept) ([NW] F2) | Guo, McAdams, Ozimek, Shyong (JHU APL), ISSFD 24 (2014); [NW] F2 | Primary | [NW] F2 (Yamakawa 1999): Venus swingbys lower aphelion "nearly to the radius of Venus's orbit" | High (DEMONSTRATED) |
| Size of one Venus flyby (DERIVED D-F) | Periapsis 300 km: turn angle 122, 99, 74, 57, 46 degrees at v-infinity 2.7, 4.0, 5.8, 7.5, 9.0 km/s; maximum velocity change **4.7, 6.1, 7.0, 7.1, 7.0 km/s** | DERIVED from JPL GM (via [VE]) | Derived | Parker's seven-flyby sequence | High (arithmetic) |
| Venus flybys on crewed Mars missions | Opposition-class Mars missions use outbound or inbound Venus swing-bys to lower total delta-v and initial mass in low Earth orbit; a 2020 habitat design assumes about 760 days and a pass to 0.62 AU (0.55 AU bound); Venus swing-bys add abort options. No delta-v saving is stated in the abstracts read | Prasad et al., AIAA ASCEND 2020, NTRS 20205007668; NTRS 19960023699 and 19870008296 (abstracts) | Primary | none | Medium (qualitative) |
| Windows (cited) | Venus-Earth every 583.9 d (146 d Hohmann, v-infinity 2.71 / 2.50 km/s); Venus-Mars every 333.9 d (217.5 d, 5.76 / 4.77); Venus-Mercury every 144.6 d (75.6 d, 5.78 / 6.77); Venus-Ceres every 259.4 d; real 2030 to 2035 windows: Venus to Earth 3 in 6 years, total v-infinity 5.7 to 6.9 km/s; Venus to Mars 7, 11.5 to 12.1 km/s | [NW] F1 D1, D2 | Derived (cited) | [MVT] 3.10 | High |
| Departure from low Venus orbit (DERIVED D-D) | 300 km orbit to Earth transfer 3.32 km/s; to Mars transfer 4.49; to Mercury transfer 4.50 km/s | DERIVED | Derived | [NW] F5: 3.3 km/s to Earth | High (arithmetic, circular coplanar) |
| Aerocapture and aerobraking (cited) | Aerobraking DEMONSTRATED (Magellan 1993, 70 days); aerocapture not flown anywhere; at Venus a 92% delivered-mass gain over propulsive capture, 687 vs 374 vs 111.5 kg in the 2006 point design; corridor +/-0.76 degree; heating beyond any tested tile | [VE] 3.8; [NW] F5 | Primary (cited) | none | High as studies |
| Venus as a staging point for Mercury cargo (DERIVED, no study) | Mercury-to-Venus cargo arrives at v-infinity 4.98 to 9.05 km/s (entry 11.4 to 13.7 km/s) ([NW] D8); from low Venus orbit Earth is 3.32 km/s away, and arrival at Earth from Venus is at about 2.5 km/s v-infinity. Direct Mercury-to-Earth cargo arrives at 6.5 to 11 km/s and needs 5 to 7 km/s to stop. **Whether a Venus stop saves propellant overall has not been studied** (it would need aerocapture beyond tested heating) | [NW] D1, D8; D-D | Derived | none | Low (SPECULATIVE) |
| Venus as a staging point for asteroid cargo | Ceres by minimum-energy transfer 0.95 yr from Venus against 1.05 yr from Earth | Landis 2003 (via [MVT] 3.10) | Primary (concept paper) | none | Low |
| Contact gaps | Solar conjunction: about 20 days of autonomy (2011), 7 days with no contact (2013), every about 584 days | [GRV] 3.13 | Primary (cited) | none | High |

### 3.5 Floating habitat and industry (checklist 5)

Cited from [MVT] 3.8, 3.9 and [GRV] 3.10, 3.12 unless marked new.

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Gravity | 8.87 m/s^2 = 0.903 of Earth's (new: fact-sheet ratio) | NSSDC Venus fact sheet | Primary | [MVT] 3.7 | High |
| Pressure and temperature | 1 bar near 50.6 km at about 70 C; 20 C near 55.9 km at about 0.46 to 0.48 bar; 0.91 bar at about 50 km by radio occultation | [GRV] 3.10 | Primary / derived from secondary | Landis 2011: 1 atm "slightly over 54 km" ([GRV] Conflicts 8) | Medium |
| Radiation | Column overhead 1,290 g/cm^2 at 50 km (Earth sea level 1,020); GCR absorbed dose 0.86 mGy/yr at 51 km and 70 mGy/yr at 62 km (Earth ground 4.4 in the same model); worst modeled solar event 0.09 Gy at 62 km | [MVT] 3.8; [GRV] 3.12 | Primary (models) | none | Medium |
| Lift and envelope | Breathable air lifts about 0.5 kg/m^3, so the whole envelope can be habitable volume; near-zero pressure difference, so a tear leaks slowly | [MVT] 3.9 (Landis 2003) | Primary (concept) | [VE] D-lift 0.31 at 55 km | Medium |
| What these enable for manufacturing | Feedstock gas arrives at the intake at about ambient pressure (no compressor, Landis and Oleson 2024, [VE] 3.3); CO2 is a free oxidizer (3.3 above); near-Earth gravity. **No study of manufacturing at cloud level, and no agricultural study of a cloud habitat, was found** (row 62) | [VE] 3.3; rows 62, 77 | Primary / gap | none | n/a (gap) |
| What they do not give | Crops and people need the CO2 scrubbed to below about 0.4 to 1 kPa (3.1); the outside is 69 to 107 C at 50 to 55 km in one model (about 75 C at 50 km in others) in acid aerosol | [LSS] A2; [VE] 3.11 | Primary (cited) | none | High |

### 3.6 The surface (checklist 6)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Rock as a resource (cited) | Basalt: SiO2 45 to 49%, Al2O3 16 to 18%, FeO 8 to 9%, MgO 8 to 11.5%, CaO 7 to 10% at three sites; no measured metal enrichment | [VE] 3.6 | Primary (cited) | none | High for three sites |
| Basalt glass and fiber | Basaltic simulant melted at 1,200 C (solar furnace) and JSC-1 at 1,450 to 1,600 C to make glass and fibers | [LSS] G3 (Azami et al. 2024, secondary there) | Secondary | none | Low |
| Melting from a hot start (DERIVED D-T) | Starting at 464 C saves 28 to 37% of the temperature rise to 1,200 to 1,600 C (sensible heat only, constant heat capacity assumed; latent heat ignored) | DERIVED | Derived | none | Low (rough) |
| Access | Landers to date about 2 hours; LLISSE about 60 days; no surface-mining study; ore lifting about 50 km unstudied ([VE] 3.6) | [VE] 3.6 | Primary (cited) | none | High |
| High-temperature electronics (spin-off value, DEMONSTRATED in rigs) | SiC JFET integrated circuits: "stable electrical operation ... for over one year at 500 C in air", 175 or more transistors per chip (a 7-fold increase over 2016); 60 days in the GEER Venus chamber ([VE] 3.6). Applications named by NASA: "combustion engine sensing and control, planetary exploration, deep-well drilling monitoring, and other harsh-environment applications" | Neudeck, Spry, Krasowski, Prokop, NTRS 20180003391 (2018); Spry et al., NTRS 20160014879 (2016) | Primary (abstracts) | [VE] 3.6 (Neudeck 2024: 7 Mrad, -190 to +812 C) | High |
| High-temperature storage | LiAl-FeS battery at 465 C, 80 Wh/kg, 60% depth of discharge for 100 to 5,000 cycles (design assumptions); prototypes 118 days at 450 C ([VE] 3.6) | Brandon et al. 2019; [VE] 3.6 | Primary | none | Medium |
| Surface energy | Sunlight 8.7 W/m^2 at noon to a 29% array ([VE] 3.5); wind about 14 W/m^2 of swept area (3.3); geothermal 24 to 32 mW/m^2 ([VE] 3.6); the 735 K air is a heat source only against a colder sink (59% Carnot to 55 km, D-J), which is 50 km away | cited; DERIVED | mixed | none | Medium |

### 3.7 Scientific value (checklist 7, brief)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Record of lost water | D/H "at least 120 times that on Earth"; possible explanations: escape after ocean evaporation, a steam atmosphere that never condensed, or water outgassed in the last 0.5 to 1 billion years; tropospheric D/H never measured, which DAVINCI targets at 0.2 to 1% precision | Garvin et al., DAVINCI, arXiv:2206.07211 | Primary | VEXAG goals as listed in Brandon et al. 2019 ("whether liquid water was ever present") | High (that the record exists); open (what it says) |
| Noble gases as an outgassing record | Xe only upper limits; Kr and Xe isotopes "the most potential to see deep into Venus's history" | DAVINCI paper | Primary | [VE] 3.1 | Medium |
| Climate instability | The present atmosphere is in "a state of unstable equilibrium"; surface-atmosphere cooling timescales 10^7 to 10^8 years | [GRV] 3.14 (Bullock and Grinspoon 1996) | Primary (cited) | none | High |

### 3.8 Costs and conditions that cut each benefit (checklist 8)

| Condition | Value | Source | Which benefits it cuts |
|---|---|---|---|
| Ascent from the cloud deck | About 9 km/s; CO/LOX at 250 s gives a mass ratio of 39; studied payload fractions 0.15 to 0.56% (180 to 670 kg lifted per kg); 0.31 to 1.34 MWh of propellant energy per kg (D-E); no studied non-rocket method; no stationary elevator possible | [VE] 3.7; [IMS] 4; D-E | Every export (N, C, O, Ar, S, D) |
| Hydrogen scarcity | 6.7 x 10^14 kg in all (water-equivalent 6 x 10^15 kg, 4.3 x 10^-6 of Earth's hydrosphere); 0.7 to 4.6 million m^3 of air per kg of H (D-P) | [VE] D1; D-G, D-P | Plastics, ammonia, water, high-Isp propellant, crops, hydrogen lift gas |
| Acid | 75 to 92 wt% droplets; intakes need filters; sulfur poisons the nickel electrodes of solid-oxide cells, so "some kind of sulfur sequestration" is needed | [VE] 3.3, 3.11; Bugga et al. 2016 | Every gas-processing plant |
| Platform lifetime | VEGA 46.5 hours in situ (DEMONSTRATED); 30 days of room-temperature lab exposure; a 10-year ISRU aerobot is a design | [VE] 3.4 | Every platform-based benefit |
| No station-keeping | A platform circles the planet in 4 to 5 days; nights of 50 to 66 hours | [VE] 3.5, 6 | Surface access, solar power, beaming |
| Imports Venus cannot supply | Lithium (molten-carbonate electrolyte, Li batteries, ALIVE fuel), chips, magnets ([SYN] 4); helium for lift (12 ppm) | rows 39, 41; [SYN] 4 | Carbon production, power storage, every machine |
| Concentration penalty against Earth | Earth air holds 34 times more N, 200 times more Ar and 36 times more Kr per tonne processed (D-A, D-C) | D-A, D-C | Every gas benefit except carbon |
| Contact | 20-day conjunction gaps every 584 days | [GRV] 3.13 | Remote operation |

### 3.9 Ranked table: who could use each benefit, and the cost to deliver it (checklist 9)

Ranked by cost to deliver to the user, cheapest first. **"No export" means the benefit is used where it is made.** All costs
are from rows above; none is a published economic study (none exists, [VE] 3.9, row 88 of [VE]).

| Rank | Benefit | Who could use it | Cost to deliver | Export from Venus needed? | Status |
|---|---|---|---|---|---|
| 1 | Gravity assists (4.7 to 7.1 km/s per flyby) | Any spacecraft bound for Mercury, the Sun, or (opposition-class) Mars | Nothing but the timing: windows every 584 d from Earth, years of flight for multi-flyby routes | No | DEMONSTRATED (Parker Solar Probe); studied for Mercury and Mars routes |
| 2 | Scientific record (D/H, noble gases, climate) | Planetary science | Probe missions | No (data only) | DEMONSTRATED (Pioneer Venus, Venus Express); DAVINCI planned |
| 3 | High-temperature electronics and storage know-how | Jet engines, drilling, other hot environments (per NASA) | Development cost only | No (knowledge) | DEMONSTRATED in rigs |
| 4 | Habitat environment at 50 to 55 km (0.9 g, about 1 bar, 1,290 g/cm^2 of shielding, air as lift gas) | People and machines living at Venus | Arrival (aerocapture-friendly) plus the platform | No | ENGINEERING-STUDIED (HAVOC); no long-life platform flown |
| 5 | O2, CO, N2, Ar, CO2 at the intake | Platforms at Venus (life support, lift-gas makeup, CO/LOX, buffer gas, argon electric propulsion) | 5.7 kWh per kg O2; 0.3 to 0.45 MJ per kg N2 floor; intake filtering | No | O2/CO DEMONSTRATED on Mars (MOXIE); others unstudied at Venus |
| 6 | Solid carbon (nanotubes, fibers) without hydrogen | Platforms at Venus (structure, envelopes, tethers) | About 8.8 MWh per t C plus a lithium-salt electrolyte | No | Laboratory/pilot on Earth |
| 7 | Sunlight 1.9 times Earth's above the clouds; two-sided collection inside them | Platforms at Venus; spacecraft in Venus orbit | Arrays only; but not beamable into the atmosphere by microwave | No | Model on mission-measured light (Landis and Haag); no array has yet operated in the clouds |
| 8 | CO2 as an oxidizer for metal fuels | Surface and low-altitude probes and machines | The metal fuel (200 kg Li for 5 days at 300 W electric) | No (fuel imported) | ENGINEERING-STUDIED (ALIVE) |
| 9 | Aerocapture and staging in Venus orbit | Cargo and crews arriving at Venus; possibly Mercury cargo | Aeroshell (30% of launch mass in the 2006 design); +/-0.76 degree corridor | No | ENGINEERING-STUDIED; not flown |
| 10 | Nitrogen, carbon, oxygen, argon, sulfur to Venus orbit | Industry in Venus orbit | 180 to 670 kg lifted and 0.31 to 1.34 MWh per kg delivered | Yes (ascent) | DERIVED; no study |
| 11 | Nitrogen and carbon to Mars, Mercury, the Moon or habitats | Mars atmosphere and agriculture, Mercury industry, rotating habitats | Ascent plus 4.5 km/s from low Venus orbit; mass ratio 124 ideal to a Mars transfer at 250 s against 13.6 from Earth at 452 s | Yes | **Not competitive on any figure found** (Earth air and carbonaceous asteroids are cheaper) |
| 12 | Deuterium at 100 to 160 times terrestrial concentration | Fusion or heavy-water users | Ascent plus 0.7 to 4.6 million m^3 of air per kg of hydrogen, of which 3 to 5% is deuterium | Yes | SPECULATIVE; no study; total only 2 to 3 x 10^13 kg |
| 13 | Surface basalt (glass, fiber, cast rock) | Platforms at Venus (if surface access existed) | Surface operations (none possible yet) plus lifting rock about 50 km | No (but needs surface access) | No study |

## 4. Conflicts

1. **Array output inside the clouds: 271 W/m^2 at 47 km (Brandon et al. 2019) against about 181 at 45 km and 256 at 50 km
   (Landis and Haag, [VE] 3.5).** Brandon's figure comes from their own Fig. 10 model, which draws on the same Landis work
   but with their cell-efficiency model (32%) and notes on upward flux; Landis and Haag tabulate a downward-only, horizontal
   array. A two-sided or differently modeled array would read higher. Not resolved; the lower figures are used for sizing.
2. **Argon mass: 2.9 x 10^16 kg ([VE] D1) against 3.09 x 10^16 kg (D-A here).** [VE] used a mean atomic mass of 38 because
   Venus argon is about half 36Ar; D-A used the standard 39.95. [VE]'s value is the better one and is the one cited in 3.1;
   the Earth comparison (about half of Earth's atmospheric argon) is unaffected in substance.
3. **VIP-INSPR (Bugga et al. 2016) Table 2 air volumes are about 100 times too small.** The table puts 42.3 mol of water at
   30 ppm in 3.2 x 10^5 L of air; 42.3 / 30 x 10^-6 = 1.41 x 10^6 mol of air, about 3.5 x 10^7 L at 1 atm and 300 K (D-P). The
   same report's minimum-work figure (357.7 Wh at 5 ppm) is reproduced exactly, so the error is in the volume column only. In
   its Table 1 the concentration row runs in the opposite order to the volume row (the lower-cloud volume, 1.7 x 10^8 L, implies
   24 mg/m^3, matching [VE] D3); the volume row is taken as correct. The report's conclusion that vapor is the easier hydrogen
   source survives at 30 ppmv but not at the 5 to 6 ppmv found above the clouds (D-P).
4. **SP-413 torus atmosphere: 44 kt stated against 42.2 kt derived** from the stated volume and composition at 20 C. A 4%
   difference, within the temperature (20 +/- 5 C) and humidity ranges of Table 4-3.
5. **Carbonaceous nitrogen: Bennu 0.23 to 0.25 wt% against CI 0.295 wt%.** Different bodies and methods (returned sample against
   meteorite average); Ryugu is reported as closely related to CI but no bulk value was read. Feed per tonne of N spans 339 to 435 t.
6. **Earth launch delta-v: 9 to 10 km/s (secondary course notes) against Venus's studied 9 km/s from 60 to 67 km.** Landis and
   Oleson's "nearly as difficult ... as from the surface of the Earth" ([VE] 3.7) is the primary statement; the comparisons in
   3.2 use ideal from-surface figures for both bodies (11.81 and 11.57 km/s) so that losses do not bias them.
7. **Make-up nitrogen per person spans tenfold** (110 to 1,130 kg per year): Biosphere 2's measured leak (5 to 10% per year)
   against BVAD's spacecraft design allowances (0.05 to 0.14% per day). Different structures and different meanings (measured
   against allowed).
8. **"About 10 mbar of nitrogen is the minimum for plants" (attributed to McKay et al. 1991)** appeared in two search
   summaries and in no page that could be opened. Not used.
9. **Comet dust N/C (0.035) and organic fraction (45 wt%)** were returned by a search summary only; the papers were blocked.
   Shown as unconfirmed; not used in any derivation.

## 5. Derived figures

Constants: JPL GM (Venus 324,858.592; Earth 398,600; Mercury 22,031.868551 km^3/s^2; via [VE] and NSSDC); radii Venus 6,051.8,
Earth 6,371.0, Mercury 2,439.7 km, Mars 3,389.5 km ([MVT]); escape speed Earth 11.186 km/s; gravity Mars 3.73 m/s^2 (NSSDC fact
sheets); g0 9.80665 m/s^2, R 8.314462618 J/(mol K), Faraday 96,485.33212 C/mol (NIST CODATA); CIAAW 2024 atomic weights.
Script: `benefits_of_mining_venus/scripts/calc.py` in the scratch folder; output `calc_output.txt` (run 2026-10-12, `python3 -I`).

| # | Figure | Arithmetic | Result | Basis and caution |
|---|---|---|---|---|
| D-A | Noble gases, Venus against Earth air | mass = x n M; air per kg = 1/(x M_gas / M_air); n_V = 4.8e20/0.04345, n_E = 5.1e18/0.02897 mol | Ar: Venus 3.09e16 kg (use [VE] 2.9e16), Earth 6.54e16; 15,500 vs 78 kg air per kg (199x). Kr: 4.35e13 vs 1.68e13 kg (2.6x); 1.1e7 vs 3.0e5 kg air per kg (36x). Xe: Venus below 5.8e13 kg (limit), Earth 2.0e12 kg | Venus x from [VE] 3.1; Earth x from Air Liquide 2023 |
| D-B | Nitrogen needs against Venus's N | torus N2 = 44 kt x w_N2, w_N2 = 26.6(28.014)/[26.6(28.014)+22.7(31.998)+1.0(18.015)] = 0.500; Mars = 4 pi R^2 p / g | torus 22 kt N2, 2,200 kg per person; cylinder 7.3 Mt; Mars 50 kPa 1.94e18 kg (3.87e16 per kPa); 13.4 to 22.6% of Venus N; region 0.125%; Venus N = 9.9e7 years of world fertilizer N | SP-413; Turyshev 2026; FAO |
| D-C | Feed per tonne of N | 1 / w_N | Venus air 44; Earth air 1.32; CI 339; Bennu 400 to 435; Moon 12,350; Mars nitrate 4,000 to 63,000 t | nitrate N = 14.007/62.004 of nitrate mass |
| D-D | Delta-v and mass ratios | from a surface: sqrt(v_inf^2 + v_esc^2); from a circular orbit: sqrt(v_inf^2 + 2 mu/r) - sqrt(mu/r); MR = exp(dv / (Isp g0)) | Venus 55 km to Mars transfer 11.81 km/s (MR 124 at 250 s); to Mercury 11.82; to Earth 10.66 (MR 77.5); Earth surface to Mars 11.57 (MR 13.6 at 452 s, 112 at 250 s); to Mercury 13.48; low Venus orbit (300 km) to Earth 3.32, Mars 4.49, Mercury 4.50 km/s; low Earth orbit (400 km) to Mars 3.57, Mercury 5.53; Mercury capture to 200 km from v-inf 6.77: 5.02, from 9.61: 7.55 km/s | Ideal, circular coplanar, v-infinities from [NW] D1; ascent losses (about 1.7 km/s at Venus) excluded |
| D-E | Energy to lift 1 kg to low Venus orbit on local CO/LOX | propellant = 0.975 / payload fraction; energy = propellant x (6.43 MJ/kg floor to 7.42 MJ/kg = 5.67 kWh/kg O2 x 3.6 x 0.364) | 0.56%: 174 kg, 1.12 to 1.29 GJ (0.31 to 0.36 MWh); 0.15%: 650 kg, 4.18 to 4.82 GJ (1.16 to 1.34 MWh); 1 t/yr needs 41 to 153 kW, 317 to 1,185 m^2 of array at 129 W/m^2 | Stoichiometric CO + 1/2 O2 assumed (the source does not state the mixture ratio, [VE] Conflicts 3); vehicle manufacture excluded |
| D-F | Single Venus flyby | e = 1 + r_p v_inf^2 / mu; turn = 2 asin(1/e); dv = 2 v_inf sin(turn/2); r_p = 6,351.8 km | 4.73, 6.09, 7.00, 7.14, 6.97 km/s at v_inf 2.7, 4.0, 5.8, 7.5, 9.0 | Maximum (full turn used); real flybys use part of it |
| D-G | Hydrogen-limited products | NH3: 3(1.008)/14.007 = 0.216 kg H per kg N; PE: 2(1.008)/14.027 = 0.144 | Venus H fixes 3.1e15 kg N (0.03% of Venus N; 28,000 yr of world fertilizer N) or makes 4.7e15 kg PE; water-equivalent 6.0e15 kg = 4.3e-6 of Earth's hydrosphere | [VE] D1 |
| D-H | Carbon by electrolysis | 4 F x 1 V / 0.012011 kg; Licht 2.4 MWh/t CO2 x 44.009/12.011; floor 393.51 kJ/mol / 0.012011 | 8.93 kWh/kg C (17.9 at 2 V); 8.79 MWh/t C; floor 32.8 MJ = 9.10 kWh/kg C; 2.66 kg O2 per kg C | Faradaic efficiency 100% assumed |
| D-I | Wind power flux | 0.5 rho v^3 | surface 0.5 m/s: 4.2 W/m^2, 1.4 m/s: 92; 55 km shear 5, 10, 20 m/s: 59, 468, 3,748 W/m^2 (x 0.41: 24, 192, 1,537) | rho 67 (Colozza) and 0.937 kg/m^3 ([GRV] secondary) |
| D-J | Carnot limits | 1 - T_cold / T_hot | 59% (0 to 55 km); 28% (40 to 55); 24% (50 to 60); 34% (50 to 70); 22% (45 to 55) | Temperatures from the VIRA-based secondary table in [GRV] 3.10 |
| D-K | Deuterium | D mass share of H = 2r/(1 + 2r); Earth D/H = 0.019/120 = 1.58e-4 (from the DAVINCI paper's own ratio) | Venus D 2.1e13 to 3.2e13 kg; Earth hydrosphere D about 5.0e16 kg; ratio 6.4e-4 | Approximate D mass = 2 x H mass |
| D-L | Sulfur | 5.5e16 kg / 84e9 kg/yr; droplet S = 5e13 x w x 32.06/98.08 | 6.5e5 years; 1.2e13 to 1.5e13 kg in the clouds | [VE] D1, D3; USGS |
| D-M | Oxygen per person | 24 kg/day / 0.816 kg per person-day | 29 people per kg/hr of O2; 193 W per person at 5.67 kWh/kg | BVAD via [LSS] |
| D-N | ALIVE lithium | 14 kW x 5 d / 200 kg | 30 MJ (heat) per kg Li | Thermal output, not electric |
| D-P | Hydrogen from vapor and droplets | air per kg water = 1/(x 18.015/43.45); per kg H x 18.015/2.016; droplets: 1/(loading x H fraction) | vapor 30 ppmv: 0.77e6 m^3 per kg H; 5 to 6 ppmv: 3.8 to 4.6e6; droplets 10 to 24 mg/m^3: 0.97 to 3.6e6 m^3 per kg H; VIP-INSPR check (Conflicts 3) | rho 0.937 kg/m^3 at 55 km |
| D-Q | Habitat N2 make-up | 44 kt x leak rate x 0.500 | 110 to 1,130 kg N2 per person-year; torus check 0.611 kg/m^3 x 6.9e7 m^3 = 42.2 kt | BVAD rates are spacecraft allowances |
| D-R | Feed per tonne of C | 1 / w_C | Venus air 3.75 t (4,000 m^3 at 55 km); Earth air at 350 ppm CO2 6,891 t; CI 29; Bennu 21 to 22; Moon 8,065 t | Earth's non-air carbon not researched |
| D-S | Venus against Earth as a source | MR ratio | To Mars: 124 / 13.6 = 9.1; to low Mercury orbit: 962 (Venus, 16.84 km/s, 250 s) against 115 (Earth, 21.03 km/s, 452 s) | Ideal |
| D-T | Basalt hot start | (464 - 25) / (T_melt - 25) | 37%, 31%, 28% of the temperature rise for 1,200, 1,450, 1,600 C | Sensible heat only |

## 6. Constraints for any inhabitant (physics and engineering only)

- **What Venus supplies is used at Venus.** Every export pays about 9 km/s from the cloud deck on 250 s propellant, 180 to 670
  kg lifted per kg delivered, 0.3 to 1.3 MWh per kg (3.8, D-E). A settlement there is self-supplied in C, N, O, S, Ar and
  importer of H, Li, chips and magnets.
- **Hydrogen is the scarce element, not nitrogen.** Water, plastics, fertilizer and high-performance propellant all need it, at
  roughly a million cubic meters of air per kilogram (D-P, D-G).
- **The air must be scrubbed before people or crops can use it** (96.5% CO2 against 0.4 to 1 kPa limits, 3.1).
- **Power comes from the Sun in two-to-three-day pulses** (50 to 66 hour nights on a drifting platform) with storage between,
  or from burning imported metal with the CO2 (3.3). Wind is usable only across altitude shear, which no study has sized.
- **Every intake and electrolyzer fights acid and sulfur** (3.8).
- **Gravity near Earth's (0.90 g) and about 1 bar at 50 to 55 km**, with an atmosphere overhead that shields about as well as
  Earth's (3.5).
- **Arrival is the cheap direction** (aerocapture 92% gain; gravity assists of up to about 7 km/s), leaving is the expensive
  one; contact gaps of about 20 days every 1.6 years (3.4).
- **A human-shaped machine** working at cloud level works in 69 to 107 C acid aerosol on a buoyant structure; its coatings,
  seals and joints face the same acid as the envelopes; nothing in this file gives it any material it could not get there
  except hydrogen-bearing polymers, lithium and electronics (3.1, 3.8).

## 7. Candidate handwaves (flagged, not accepted; the developer decides)

1. **H-1. Venus as a nitrogen or carbon exporter to Mars, Mercury, the Moon or habitats.** On the figures found, Earth air
   and carbonaceous asteroids are cheaper (mass ratio 9.1 times Earth's to a Mars transfer; delta-v many times the belt's).
   It needs a non-rocket ascent (no study exists; [VE] handwave 1) or hydrogen imported for high-Isp propellant (which
   inverts the purpose).
2. **H-2. Venus as a source of noble gases for electric propulsion elsewhere.** Venus air is 200 times leaner in argon and 36
   times leaner in krypton than Earth air, and its xenon is only an upper limit.
3. **H-3. Venus deuterium as a fusion-fuel supply.** The concentration is real (100 to 160 times terrestrial); the total is 2 to 3
   x 10^13 kg, 0.06% of Earth's, and each kilogram of hydrogen costs about a million cubic meters of air. No study exists.
4. **H-4. Wind farms at cloud level.** A balloon moves with the wind; only shear across a tether gives power, and no Venus
   study sizes it.
5. **H-5. Microwave power beaming from Venus orbit into the atmosphere.** The one study found calls it not technically feasible
   (atmospheric absorption at 2 to 100 GHz).
6. **H-6. Large-scale manufacturing or agriculture in Venus cloud habitats as a demonstrated benefit.** No study of either was
   found; the benefits in 3.5 are environmental, not process-tested.

## 8. Open threads

- **A real separation energy for N2 from a CO2-N2 mixture** (membrane, adsorption, cryogenic); only the floor is known ([VE] D5).
- **Crop nitrogen inventory per person in a closed habitat** (biomass plus soil); SP-413 lists masses but not nitrogen content.
- **Bulk nitrogen of Ryugu and Ceres**, and the confirmed comet values (Fray et al. 2017, Bardyn et al. 2017, MNRAS; both blocked
  by Cloudflare at OUP and Anubis at HAL); next: ADS full text, Rosetta archive summaries.
- **The nitrogen release temperature and yield from carbonaceous material** (only water release was found, via [SYN]).
- **A delta-v figure for the Venus-swing-by saving on crewed Mars missions** (NTRS abstracts give none; next: the Drake 2013
  slides and Wooster et al. 2007, "Mission design options for human Mars missions").
- **Titan as a nitrogen source** (lecture-slide lead: about 9 x 10^18 kg of N2); next: NSSDC Saturnian satellite fact sheet and
  Huygens surface pressure, to derive it.
- **A molten-carbonate electrolysis plant energy figure at scale** from a peer-reviewed source (the Tampere/Elsevier paper
  returned HTML; the Licht figure is from a competition submission).
- **The Acta Astronautica papers** "Feasibility of power beaming through the Venus atmosphere" (2023) and "Venus Aerial Platforms:
  Long-Lived Balloons with ISRU for Buoyant Gas Replacement" (2026): found, paywalled, not read.
- **A shielding comparison with numbers** (dose per g/cm^2 for carbon, CO2 ice or basalt against polyethylene).
- **Plant nitrogen minimum** (the "10 mbar" attributed to McKay et al. 1991): needs the Nature paper or McKay and Marinova 2001.
- **Basalt-fiber properties and composition limits** from a peer-reviewed review (MDPI blocked).
- **Phosphorus in the lower cloud** (Vega, [VE] 3.1): no abundance found; phosphorus is a fertilizer input Venus may or may not
  supply.
- Found but not read: Penn State pure.psu.edu records on lithium-combustion power (2018 to 2020); the Southampton Hall-thruster
  propellant review; Wikipedia's Parker Solar Probe page (not needed).

## 9. Rejected sources

- **Search-summary figures not traced to an opened page:** "about 10 mbar of nitrogen" for plants; comet N/C 0.035 and 45 wt%
  organics (kept only as unconfirmed leads); "100 t CO2 per year" C2CNT modules and "wools for textiles"; Starlink argon
  "4.2 kW" and "2,500 s"; Statista "314 million tons" of nitrogenous fertilizer (product mass, not N); JPL HAR-V "9 W" wind
  goal; the "4 to 525 m" paleo-ocean range.
- **Numbers recalled in my own query strings** (rows 26 "0.035", 61 "9.4 km/s"): used only to steer searches.
- **Student and hobby sources:** NASA Space Apps Challenge team pages (Venus wind, power), Kerbal and newmars forums,
  Medium posts, sciencearray, Orion's Arm (fiction), interestingengineering, steamcommunity: no figure taken.
- **Trade press** (gasworld, TechCrunch, space.com, spaceflightnow): leads only; the Via Satellite article is used once, as
  secondary, for the argon thruster's existence and thrust.
- **The University of Maryland ASTR 380 slides:** a lecture, secondary; lead only.
- **Patents** (basalt fiber, molten-carbonate processes): not used.
