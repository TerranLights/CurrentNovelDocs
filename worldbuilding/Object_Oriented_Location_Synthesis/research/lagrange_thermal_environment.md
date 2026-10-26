# Lagrange-point thermal environment and heat management (research)

Research agent file, 2026-10-11. Brief: `_BRIEF.md`. Every figure below comes from a source opened this session.

## 1. Scope

Thermal environment and heat management for structures at the Earth-Moon and Sun-Earth Lagrange points, with weight on L4/L5:
flown missions at Sun-Earth L1/L2, Earth-Moon L1/L2 and the Jupiter Trojans; published stability, eclipse and dust data for
Earth-Moon and Sun-Earth L4/L5; heat storage, batteries, radiator coatings and the solar constant at 1 AU. Eclipse and Sun-angle
statistics for L4/L5 are **not computed here** (the orchestrator computes them); this file gives the published figures to check
them against. Physics and engineering only.

## 2. SEARCH LOG

All entries 2026-10-11. S = search, F = fetch (page opened).

| # | Search string (verbatim) or page opened | Result | Notes |
|---|---|---|---|
| S1 | `JWST sunshield five layers hot side temperature cold side temperature NASA` | useful | Lead to NASA "How does Webb stay cold" page; popular pages (Universe Today, Naked Scientists) not used |
| F1 | science.nasa.gov/mission/webb/science-overview/science-explainers/how-does-webb-stay-cold | useful | Five Kapton layers, 358 K hot side, about 40 K cold side, MIRI 7 K |
| S2 | `SP-413 Space Settlements L5 eclipses rare duration` | thin | Search summary claimed SP-413 says occultation is rare; traced to a different document (F3) |
| S3 | `Gaia Lissajous orbit eclipse avoidance maneuver Earth shadow` | useful | ESA ops page, Gaia Collaboration 2016 paper |
| F2 | esa.int/Enabling_Support/Operations/Gaia_s_biggest_operation_since_launch (15 Jul 2019) | useful | Eclipse consequences quoted; no delta-v figure on the page |
| F2b | arxiv.org/pdf/1609.04153 (Gaia Collaboration, Prusti et al. 2016, A&A 595, A1) | useful | WebFetch could not parse; downloaded and extracted with pdftotext. Lissajous amplitudes, 14 m/s eclipse-avoidance maneuver, CCDs passively cooled to 163 K |
| S4 | `"Space Settlements: A Design Study" chapter 4 "occultation" L5 sun` | useful | Located the CoEvolution-book appendix and the SP-413 table of contents |
| F3 | nss.org/settlement/nasa/CoEvolutionBook/APPENDIX.HTML (opened twice) | useful | "Occultation of the sun in that orbit is rare and brief" (O'Neill-era appendix citing Physics Today Sept 1974). No number. |
| F4 | nss.org/settlement/nasa/75SummerStudy/s.s.doc.html and Table_of_Contents1.html | useful (navigation) | Chapter URLs |
| F5 | nss.org/settlement/nasa/75SummerStudy/Chapt4.html | thin | Eclipse rejection of near-Earth orbits quoted; **no eclipse number for L5** (dead at the sources for the number) |
| F6 | nss.org/settlement/nasa/75SummerStudy/Chapt.2.html | useful | 1,390 W/m2; L4/L5 orbit period "about one month"; no eclipse statement |
| F7 | pure.bit.edu.cn ... eclipse-analysis-of-periodic-orbit-families-at-earth-moon-librati (He, Meng, Qiao, Li, AFC 2025, Springer 2026) | thin | Abstract only: L3/L4/L5 orbits shadow less than L1/L2; large-amplitude L4/L5 orbits better. No numbers in abstract; paywalled chapter not read |
| S5 | `eclipse duration triangular libration point Earth-Moon L4 orbit Earth shadow analysis` (extended) | useful | Richichi et al. 2024 MNRAS; Kordylewski part I; arXiv Sun-visibility paper (not opened, see Open threads) |
| F8 | academic.oup.com/mnras/article/527/3/6616/7453664 (opened twice) | thin | One sentence on solar eclipses from L4: "once or very few times per month ... of order of a few hours"; the body causing the eclipse is not stated in the quoted paragraph |
| S6 | `Patel 2023 Earth-Moon L4 spacecraft mission concept Kordylewski clouds solar corona eclipse orbit` | thin | Did not find Patel et al. 2023 itself (dead at the query); found the ELTE PDF and the DARKO concept |
| F9 | arago.elte.hu/sites/default/files/KordylewskiDustClouds-L4+L5_MNRAS.pdf (Slíz-Balogh et al. 2023, MNRAS 518, 5236) | useful | WebFetch failed (expired certificate); downloaded with curl -k into scratch, read as text. Detection counts; no density |
| S7 | `Hiten Munich Dust Counter Kordylewski clouds L4 L5 dust flux no enhancement` | useful | Lead to Part II paper |
| S8 | `Kordylewski cloud size degrees density estimate spacecraft hazard Wang 2021 review` | thin | Wang et al. 2021 review located; size "15 by 10 degrees" appears only in popular pages (National Geographic), not confirmed |
| F10 | sciopen.com/article/10.34133/2021/6597921 (Wang et al. 2021, Space: Science & Technology) | thin | Abstract only; full PDF not retrieved |
| F11 | arxiv.org/pdf/1910.07471 (Slíz-Balogh, Barta, Horváth, Part II, 2019) | useful | Downloaded and extracted. Hiten MDC found no obvious dust increase; Roach 1975: angular size about 6 degrees |
| S9 | `Earth-Moon L4 L5 station keeping delta-v per year solar perturbation bicircular quasi-periodic orbit` (extended) | thin | **No published Earth-Moon L4/L5 station-keeping delta-v per year found** (dead at the sources for the number: the hits discuss the need for corrections, give no figure). Led to Folta et al. 2012 |
| S10 | `Heppenheimer Colonies in Space L5 eclipse "Earth's shadow" colony` | thin | Search summary asserted "L5 experiences no eclipses"; not found in any opened page; not used |
| F12 | nss.org/?p=30196 (Heppenheimer, "L5: A Place in Space", L5 News) | useful | Colony orbit "about 90,000 miles from its central libration point"; no eclipse statement |
| S11 | `nss.org Heppenheimer "Colonies in Space" chapter libration point orbit "eclipse"` | dead (at the query) | Full book text not located |
| S12 | `Kamel 1970 stability of motion near sun-perturbed Earth-Moon triangular libration points NASA CR` | useful | Search summary misread the orbit size as "about 2,000 miles"; the PDF says otherwise (see F14) |
| F13 | engineering.purdue.edu ... 2012_IAA_FolWooPavHaaHow.pdf (Folta, Woodard, Pavlak, Haapala, Howell, IAA-AAS-DyCoSS1-05-10, 2012) | useful | WebFetch could not parse; extracted locally. ARTEMIS actual station-keeping cost per year |
| F14 | ntrs.nasa.gov/api/citations/19700026379 (Kamel, NASA CR-1622, Aug 1970) | useful | Extracted locally; OCR is poor in the abstract. Schechter: 60,000 mi; Kolenkiewicz and Carpenter: 90,000 and 88,000 mi; one-month stable orbits synchronized with the Sun |
| S13 | `ARTEMIS THEMIS spacecraft long eclipse lunar shadow survival battery heater 2010` | useful | Led to the LRO thermal paper |
| F15 | ntrs.nasa.gov/api/citations/20110022486 (Baker, Cottingham, Peabody, "LRO Thermal On-Orbit Performance", AIAA/ICES 2011) | useful | Extracted locally. 151 min Earth-shadow eclipse; pre-heating avionics to store heat in thermal mass |
| S14 | `JWST halo orbit L2 avoid Earth shadow eclipse why not at L2 point solar power` | useful (leads) | Hits mostly secondary; JWST user docs |
| S15 | `JWST sunshield attenuates sunlight factor "SPF" 1,000,000 kilowatts 1 milliwatt NASA` | useful | Led to Gardner et al. 2006 |
| F16 | jwst-docs.stsci.edu/display/Latest/JWST+Orbit | thin | Only the navigation part of the page was returned; orbit text not read |
| F17 | arxiv.org/pdf/astro-ph/0606175 (Gardner et al. 2006, Space Sci. Rev. 123, 485) | useful | Downloaded and extracted. About 200 kW on the sunshield reduced to milliwatts; sunshield about 19.5 x 11.4 m; 8 m2 ISIM radiator; orbit "avoids Earth and Moon eclipses" |
| S16 | `JWST on-orbit thermal performance commissioning sunshield layer 1 temperature layer 5 measured kelvin paper` | useful | Led to Rigby et al. 2023 |
| F18 | arxiv.org/pdf/2207.05632 (Rigby et al. 2023, PASP 135:048001) | useful | Downloaded and extracted. Flight temperatures, 1.5 kW load, more than 20 yr of propellant |
| S17 | `Webb sunshield layer 1 "383" K layer 5 "36" K NASA sunshield membrane` | useful | |
| F19 | nasa.gov/universe/nasas-james-webb-space-telescope-clears-critical-sunshield-deployment-testing (21 Oct 2019) | useful | 383 K outer layer max, 36 K coldest layer (modeled) |
| S18 | `SOHO spacecraft thermal control subsystem L1 halo orbit radiators heaters solar flux design ESA` | useful | |
| F20 | esa.int/esapub/bulletin/bullet84/vdbus84.htm (Vandenbussche, ESA Bulletin 84, Nov 1995) | useful | Heaters, substitution heaters, +/-1 C, 1,500 W array, two 20 Ah NiCd batteries |
| S19 | `DSCOVR L1 Lissajous orbit solar exclusion zone thermal design spacecraft bus Triana` | useful | |
| F21 | ntrs.nasa.gov/citations/20220011043 (Long et al. 2022) | useful | SEZ burn-through: 31 kg fuel, 100 m/s preserved. No thermal data |
| S20 | `Queqiao relay satellite Earth-Moon L2 halo orbit eclipse avoidance shadow orbit maintenance paper` | thin | Only secondary pages (Wikipedia, news); "80 g of fuel about every 9 days" unconfirmed by a primary; not used |
| S21 | `Lucy spacecraft thermal design Jupiter Trojans 5.7 AU solar arrays heaters survival temperature NASA` | useful (leads) | |
| F22 | nasa.gov/solar-system/nasas-lucy-stretches-its-wings-in-successful-solar-panel-deployment-test (6 Apr 2021) | useful | 7.3 m arrays, about 500 W, 853 million km |
| S22 | `Levison 2021 "The Lucy Mission" Planetary Science Journal spacecraft solar arrays power Trojan 5.7 au` | dead (at the query) | Paper not surfaced |
| S23 | `Lucy spacecraft thermal control system ICES paper louvers heaters cold case Trojan encounter` (extended) | useful | Found the Lucy spacecraft chapter and the NASA SoA thermal chapter |
| F23 | ntrs.nasa.gov/api/citations/20250001468 (Cox et al., "The Lucy Spacecraft", Lockheed Martin; Space Sci. Rev. 2025) | useful | Downloaded and extracted. 18 kW at Earth vs 500 W at Jupiter's distance; heaters below 192 W; battery 44 Ah, 32 V, about 3 h |
| F24 | nasa.gov/wp-content/uploads/2025/02/7-soa-thermal-2024.pdf (NASA Small Spacecraft Technology State of the Art, ch. 7 Thermal, 2024 ed.) | useful | Downloaded and extracted. Coating absorptivity (BOL only), PCM heat-of-fusion table, BOL/EOL guidance; **no emissivity column and no EOL numbers** |
| S24 | `silver Teflon optical solar reflector Z-93 white paint solar absorptance emissivity beginning of life end of life table NASA ntrs` (extended) | useful | Gilmore handbook ch. 4; NASA RP-1121 |
| F25 | matthewwturner.com/.../Spacecraft Thermal Control Handbook/04.pdf (Gilmore, Stuckey, Fong, ch. 4 "Thermal Surface Finishes", Spacecraft Thermal Control Handbook vol. I, Aerospace Press, 2nd ed. 2002) | useful | Downloaded from a personal mirror (provenance flagged); Table 4.1 BOL alpha/epsilon; degradation text |
| F26 | apps.dtic.mil/sti/tr/pdf/ADA305864.pdf | dead (at the sources) | DTIC returned an HTML page, not the PDF |
| S25 | `NASA RP-1121 Henninger "Solar absorptance and thermal emittance of some common spacecraft thermal-control coatings" ntrs` | useful | |
| F27 | ntrs.nasa.gov/api/citations/19840015630 (Henninger, NASA RP-1121, Apr 1984) | useful | Extracted. Z-93, S-13G, silver/aluminum-backed Teflon alpha/epsilon; UV-degraded values for some paints |
| S26 | `spacecraft radiator areal mass kg/m2 flight radiator panel heat pipe NASA ntrs comparison lightweight radiator` (extended) | useful | |
| F28 | isnps.unm.edu/reports/ISNPS_Tech_Report_103.pdf (El-Genk, NASA ESI grant 80NSSC22K0263 final report, 14 Feb 2025) | useful | Table 2: design-study radiator areal densities 5.24 to 12.76 kg/m2; these are concepts, not flown |
| S27 | `Space Shuttle orbiter payload bay door radiator panels total area mass heat rejection kW ntrs` | useful | 175 m2, 30.5 kW; **no mass found** |
| F29 | ntrs 19850008616 (Williams et al., "Challenges in the development of the Orbiter radiator system") and ntrs 19890000746 (NASA TM-100972, "The Solar Dynamic Radiator with a Historical Perspective") | useful | Extracted. 175 m2, 30.5 kW, silver-backed Teflon |
| S28 | `ISS lithium-ion battery ORU replacement 134 Ah GS Yuasa cells mass energy Wh/kg ntrs Dalton` | useful | |
| F30 | ntrs 20170004112 (Dalton et al., "ISS Lithium-Ion Battery", NASA Aerospace Battery Workshop, 15 Nov 2016) | useful | Extracted. about 15 kWh per ORU, 435 lb ORU, 3,530 g cell, 30 cells, 10 yr / 60,000 cycle target |
| F31 | ntrs 20150000878 (NASA GRC 2014 electrochemical overview) | thin | Cell development numbers; LEO cycling about 20% DOD; not used for flown packs |
| F32 | nasa.gov/wp-content/uploads/2025/02/3-soa-power-2024.pdf (NASA SoA ch. 3 Power, 2024) | useful | Extracted. 18650 cell table with flight heritage, Wh/kg |
| S29 | `geosynchronous satellite lithium-ion battery eclipse seasons 92 eclipses per year 72 minutes maximum depth of discharge life test` | useful | |
| F33 | ntrs 20190001376 (Tucker, Bauer, Springer, Lee, Ma, "GOES-R Lithium-Ion Battery Life Test", NASA Aerospace Battery Workshop 2018) | useful | 44-day eclipse seasons, up to 70 min, 75% DOD, 20 seasons = 10 yr, no capacity loss |
| S30 | `NASA solar irradiance perihelion aphelion W/m2 1412 1321 Earth orbit variation 6.9 percent` | useful | ECSS table; Wikipedia not used |
| F34 | nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html (updated 15 Nov 2024) | useful | 1361.0 W/m2; perihelion 147.095, aphelion 152.100 x 10^6 km |
| F35 | spenvis.oma.be/ecss/e_st_10_04c/ecss_06_03_02.htm (ECSS-E-ST-10-04C Table 6-2, via SPENVIS) | useful | 1,366.1; aphelion 1,321.6; perihelion 1,412.9 W/m2 |
| S31 | `Kopp Lean 2011 total solar irradiance 1360.8 W/m2 solar minimum SORCE TIM new lower value` | useful | |
| F36 | espo.nasa.gov/node/30086 (Kopp and Lean 2011, GRL 38) | useful | 1360.8 +/- 0.5 W/m2 vs older 1365.4 +/- 1.3 |
| S32 | `2010 TK7 Earth Trojan asteroid discovery Connors Wiegert Veillet Nature 2011 libration orbit L4` | useful | |
| F37 | physics.uwo.ca/~pwiegert/2010TK7/ (discoverer's page) | useful | 195-year cycles; no closer than 20 million km in 10,000 yr |
| F38 | cfht.hawaii.edu/en/news/EarTro/ | thin | "stable for at least ten thousand years"; no other number |
| S33 | `STEREO spacecraft passage through Sun-Earth L4 L5 search for Earth Trojans dust observation 2009` | useful | |
| F39 | svs.gsfc.nasa.gov/3591 (9 Apr 2009) | thin | States the search goal only; no results reported |
| F40 | ntrs 20150002915 (John, Graham, Abell, NASA JSC, LPSC abstract) | useful | 2010 TK7: about 300 m, e = 0.191, 0.81 to 1.19 AU, i = 20.9 deg |
| S34 | `Sun-Earth L4 L5 space weather mission Vigil ESA L5 radiation environment interplanetary dust station-keeping delta-v` | useful (leads) | |
| F41 | lws.larc.nasa.gov ... Vigil mission objectives PDF | dead (at the sources) | Host did not resolve (DNS failure); curl and WebFetch both failed |
| F42 | esa.int/Space_Safety/ESA_Vigil_overview | dead (at the sources) | 404 |
| S35 | `ESA Vigil L5 spacecraft transfer time to L5 "Lissajous" orbit design delta-v paper` | useful | |
| F43 | iafastro.directory ... IAC-24,C1,IPB,21,x81846.brief.pdf (Renk, ESA, IAC 2024) | useful | Extracted. Transfer architecture; no numbers in abstract |
| F44 | arxiv.org/pdf/1109.2929 (Gopalswamy et al. 2011, EASCO, NASA GSFC MDL study) | useful | Extracted. Transfer about 2 yr, delta-v about 1.5 km/s (EP) or about 950 m/s (chemical); array operating temperature 70 C assumed |
| S36 | `space colony L5 Earth shadow eclipses per year hours "L5" colony solar power interruption lunar eclipse analogous` (extended) | **rejected** | The search summary applied **geostationary** eclipse figures (about 70 min, near the equinoxes) to "L5". Not used; see Rejected sources |
| S37 | `eclipse.gsfc.nasa.gov lunar eclipse statistics number per year maximum duration totality umbral 106 minutes Espenak` | useful | |
| F45 | eclipse.gsfc.nasa.gov/SEpubs/5MKLE.html (Espenak and Meeus, NASA TP-2009-214173, Jan 2009) | useful | 12,064 lunar eclipses in 5,000 yr, by type |
| F46 | eclipsewise.com/lunar/LEhelp/LEstatistics.html (Espenak) | useful | 2 to 5 lunar eclipses per calendar year; longest totality about 99.8 min; longest partial about 210 min |
| S38 | `Planck Herschel L2 Lissajous orbit eclipse free large amplitude Earth shadow ESA mission analysis` | useful | |
| F47 | sci.esa.int/web/herschel/-/34699-orbit-navigation (updated 1 Sep 2019) | useful | Herschel orbit about 700,000 km amplitude, 178 d, maintenance about monthly |
| F48 | issfd.org/ISSFD_2009/InterMissionDesignI/Bauske.pdf (Bauske, ESOC, ISSFD 2009) | useful | WebFetch could not parse; extracted locally. Eclipse requirements; Planck orbit-change cases with Earth and Moon eclipse counts; Herschel 10.72 kg/yr allocation |
| S39 | `Queqiao halo orbit Earth-Moon L2 amplitude 13000 km eclipse avoidance Chang'e-4 relay satellite design paper Zhang Lihua` (extended) | thin | Search summary gives a 13,000 km Z-amplitude, 47,000 to 79,000 km from the Moon, 14-day period, 66 m/s capture burn |
| F49 | spj.science.org/doi/10.34133/2021/3471608 (Zhang Lihua, "Development and Prospect of Chinese Lunar Relay Communication Satellite", Space: Sci. & Tech. 2021) | dead (at the sources) | HTTP 403. **Queqiao numbers therefore remain unconfirmed by a page I opened; not entered in Findings** |
| S40 | `lunar night survival thermal design radioisotope heater unit Chang'e-3 Yutu lunar night temperature paper` | thin | Secondary pages only for Yutu; led to the TFAWS 2023 paper |
| S41 | `Lunar Roving Vehicle wax heat sink thermal control "Lunar Roving Vehicle" paraffin n-octadecane LRV operations handbook NASA` | useful | |
| F50 | ntrs.nasa.gov/citations/19720055484 (Elliott, Paoletti, Britt, "Lunar roving vehicle thermal control system", Aug 1972) | useful (abstract only) | "fusible mass heat sinks"; no mass or capacity in the abstract |
| F51 | ntrs 20110010960 and 20100040644 (Quinn, Hodgson, Stephan, "Phase Change Material Trade Study: Wax and Water for Manned Spacecraft", ICES 2010) | useful | Extracted. LRV "two boxes of wax"; pentadecane 162.8 kJ/kg (+43.3 kJ/kg solid-solid); PCM mass fraction 29% to 51% by design; radiator mass factor 1.0 lb/ft2 assumed |
| F52 | ntrs 20110008723 (Leimkuehler and Stephan, ice PCM heat exchangers) | useful | Wax about 200 kJ/kg vs water 333 kJ/kg; evaporant about 2,500 kJ/kg |
| F53 | tfaws.nasa.gov/wp-content/uploads/TFAWS23-PT-52-Presentation.pdf (Slusser, Wilcox, Hernandez, TFAWS 2023) | useful | Night heat deficit 204 Wth, 125 h, 26.3 kWh; RHU about 1 Wth; Lunokhod Po-210 and Chang'e-3/Yutu Pu-238 heritage |
| S42 | `Mars Exploration Rover warm electronics box radioisotope heater units eight 1 W night survival thermal design JPL paper` | useful (lead) | Search summary gives 8 RHUs x 1 W and 100 Wh survival heating; not confirmed on an opened page |
| F54 | mer-portal.spacescience.org/docs/MER-Rover-and-Payload_with-bibliography_SBC-2015.pdf | thin | Confirms WEB approach (insulation, electronics waste heat, RHUs, survival heaters; +50 to -40 C); no RHU count or Wh figure |
| F55 | arxiv.org/abs/2408.04208 (Lee et al. 2024) | dead (at the sources, for this topic) | Sun-visibility geometry for solar observing; no eclipse content |
| S43 | `Earth resonant dust ring trailing blob Spitzer Reach 2010 density enhancement behind Earth circumsolar ring` | useful | |
| F56 | authors.library.caltech.edu/records/97z32-0dg04 (Reach 2010, Icarus 209, 848) | useful | Dust enhancement centered 0.2 AU behind Earth, width 0.08 AU |
| S44 | `radiation environment Sun-Earth L5 mission galactic cosmic rays solar energetic particles total ionizing dose design STEREO measurements` | thin | Search summary quoted a Lagrange-mission radiation analysis (20 krad, 4.3 mm Al, 0.7 AU) |
| F57 | bexus.org ... LGR-IS-KIE-AN-0002_iss1_rev0_MEPS-Radiation_Analysis.pdf | dead (at the sources) | HTTP 404 (curl returned HTML; WebFetch 404). Not used |
| F58 | gaia.ac.uk ... IN_L2_orbit.pdf | dead (at the sources) | HTTP 403; the "13,000 km eclipse zone" figure stays unconfirmed |
| F59 | blogs.esa.int/rocketscience/?p=984 (Scuka, ESA, 7 Jan 2014) | useful | Gaia Lissajous box 263,000 x 707,000 x 370,000 km; eclipse-free about five years without a maneuver |
| F60 | link.springer.com/chapter/10.1007/978-981-95-3034-2_9 | dead (at the sources) | Paywall redirect |
| S45 | `Earth-Moon L4 L5 spacecraft "eclipse" duration hours Earth umbra short period orbit power design navigation constellation` (extended) | thin | Search summary: halo-orbit Earth eclipses "3 to 4 hours"; lunar 1 to 4 hours (source not opened; not used) |
| F61 | sciencedirect.com/science/article/abs/pii/S0094576524003412 | dead (at the sources) | HTTP 403 |
| S46 | `"Cislunar L4 and L5 axial orbits and their applications" Acta Astronautica 2024 eclipse` | thin | Abstract via search: 3:1 resonant L4/L5 axial orbits best for eclipse avoidance; no numbers |

**Search count:** 46 searches (S1 to S46), 61 page opens (F1 to F61). **Dead ends:** 13 (at the query: S11, S22, S6 in part; at the sources: F26, F41, F42, F49, F55, F57, F58, F60, F61, and F5 for the number). **Not used although found:** Queqiao figures (S20, S39), the MER 8 x 1 W RHU and 100 Wh figures (S42), the L5 radiation-analysis figures (S44), the halo-eclipse "3 to 4 hours" (S45), the Kordylewski "15 by 10 degrees" (S8).

## 3. Findings

### 3A. Flown Lagrange-point missions: thermal control and eclipse avoidance

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| JWST sunshield | Five layers of Kapton, each "about the thickness of plastic wrap"; vapor-deposited aluminum on all layers; doped-silicon coating on the two outermost layers. Size about 19.5 m x 11.4 m; "Five layer 'V' groove radiator design reduces solar energy to 10's of mW" | NASA, "Webb clears critical sunshield deployment testing", 21 Oct 2019 (F19); NASA "How does Webb stay cold" (F1); Gardner et al. 2006, Space Sci. Rev. (F17) | Primary | Gardner: "reduces the ∼200 kW incident solar radiation ... to milliwatts incident on the telescope and ISIM" | High |
| JWST hot and cold sides | Outermost layer maximum **383 K**; coldest layer modeled minimum **36 K** (2019 article). The explainer page: hot-side parts "as high as 358 kelvins (85 degrees Celsius)", cold side "about 40 kelvins" | F19; F1 | Primary | See Conflicts (C1) | High (different definitions) |
| JWST flight temperatures | Primary mirror segments 35 to 55 K, secondary 29.3 K, near-IR instruments 35 to 39 K, MIRI 6.4 K (cryocooler); temperatures "extremely stable with time"; changes below 0.1 K within sensor noise | Rigby et al. 2023, PASP 135:048001 (F18) | Primary | F1 gives MIRI 7 K as the design figure | High |
| JWST radiators and power | ISIM: "8 m2 of thermal radiator area"; observatory generating 1.5 kW to match the load, capability above 2 kW | F17 (design, 2006); F18 (flight, 2023) | Primary | none | High |
| JWST orbit and eclipses | "This orbit avoids Earth and Moon eclipses of the Sun, ensuring continuous electrical power"; 6-month period about L2; propellant now projected for more than 20 yr (requirement 10.5 yr) | F17; F18 | Primary | Sibling file: 21-day maneuvers, 2.43 m/s per year design budget (Dichmann 2014) | High |
| JWST degradation drivers at L2 | Mirrors and sunshield "expected to slowly degrade from micrometeoroid impacts"; "sunshield and multilayer insulation will degrade from space weathering"; micrometeoroid hit rate about 2.5 per month on the primary mirror (2022) | F18 | Primary | none | High for statement; rate is early-mission |
| Gaia orbit and eclipses | Lissajous amplitudes 120,000 x 340,000 km in the ecliptic and 180,000 km perpendicular, period about 180 days; "not impacted by eclipses of the Sun by the Earth during its five-year nominal lifetime, although small (percent level) partial eclipses by the Moon typically occur once per year"; **14 m/s eclipse-avoidance maneuver** (July 2019) for Earth-eclipse-free operation to 2025; CCDs passively cooled to 163 K; temperature shows "long-term trends ... owing to the seasonal variation in the spacecraft-Sun distance" | Gaia Collaboration (Prusti et al.) 2016, A&A 595, A1 (F2b) | Primary | ESA ops page (F2): eclipses "would prevent sufficient sunlight from reaching Gaia's solar panels that the observatory would shut down" and "cause a thermal disturbance, affecting the spacecraft's scientific data acquisition for weeks" | High |
| Gaia eclipse rationale | Cannot enter Earth's shadow "since its thermal balance must be very carefully controlled. The sudden drop in temperature would cause its instruments to cease functioning"; eclipse-free about five years without a dedicated maneuver | ESA Rocket Science blog, Scuka, 7 Jan 2014 (F59) | Primary (agency blog) | F2b | High |
| Herschel and Planck eclipse rules | Both: "no eclipses by the Earth may occur during transfer and science phases and no eclipses by the Moon during the transfer phase"; orbit size limited by Sun-spacecraft-Earth angle (Herschel below 40 deg). A Planck change to a smaller orbit cost 50.6 to 75.7 m/s (four cases) and the resulting orbits contained 1 to 2 Earth eclipses and 4 to 11 Moon eclipses; Herschel allocation for attitude control plus orbit maintenance 10.72 kg/yr | Bauske, ESOC, ISSFD 2009 (F48) | Primary | ESA Herschel page (F47): about 700,000 km amplitude, 178 d, maintenance "roughly once each month" | High |
| SOHO at Sun-Earth L1 | Dedicated adjustable heaters; "Substitution heaters replace the heat inputs of the experiments at times when the latter are switched off"; front sunshield "maintained to within +-1 deg C for two months"; PLM/SVM interface 20 +/- 2.5 C; 1,500 W solar array with two 20 Ah NiCd batteries | Vandenbussche, ESA Bulletin 84, Nov 1995 (F20) | Primary | none | High |
| DSCOVR at Sun-Earth L1 | The constraint at L1 is a 4-degree Solar Exclusion Zone (radio interference), not an eclipse; a 2021 burn-through campaign saved 31 kg of fuel / 100 m/s | Long et al., NTRS 20220011043 (F21) | Primary (abstract page) | search summary for the 4-degree half-angle (not opened in full) | Medium |
| ARTEMIS at Earth-Moon L1/L2 | Projected station-keeping per year: P1 about 7.39 m/s at L2 and 5.28 m/s at L1; P2 about 5.09 m/s; pre-flight budgets about 15 and 12 m/s; a floor of "about 5 m/s per year" | Folta et al., IAA-AAS-DyCoSS1-05-10, 2012 (F13) | Primary | Sibling: 0.31 and 0.41 m/s per month (Whitley and Martinez 2016) | High |
| LRO lunar eclipse (Earth's shadow at lunar distance) | 21 Dec 2010: "the Earth shadowed the Moon for 151 minutes", against normal LRO nights of at most 50 min. Operations **pre-heated the avionics "to use excess electrical power prior to the eclipse and store some of the heater power in the thermal mass of the spacecraft"**; avionics reached maximum temperature in 3.5 h; no large avionics heaters (otherwise up to 100 W) needed; battery had more than 100% margin against the 70% DOD design | Baker, Cottingham, Peabody, "LRO Thermal On-Orbit Performance", AIAA/ICES 2011, NTRS 20110022486 (F15) | Primary | none | High |
| Lucy (Sun-Jupiter L4/L5 Trojans) | Arrays 7.3 m diameter; "capable of producing up to 18,000 Watts in Earth orbit"; "at Jupiter's orbit Lucy will only generate 500 Watts"; heater power "projected to be less than 192 Watts"; thermal control by "temp sensors, heaters, multi-layer insulation blankets, special coatings, heat spreaders and isolators"; battery 8 series x 16 parallel small cells, 32 V nominal, 44 Ah, about 3 h of spacecraft power; launch mass 1,500 kg (712 kg dry) | Cox et al. (Lockheed Martin), "The Lucy Spacecraft", Space Sci. Rev. 2025, NTRS 20250001468 (F23) | Primary | NASA, 6 Apr 2021 (F22): about 500 W, 853 million km from the Sun | High |

### 3B. Earth-Moon L4/L5: stability, eclipses, dust

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Stable orbits about the Sun-perturbed points | The exact points are not usable; one-lunar-month periodic orbits exist, synchronized with the Sun. Schechter: retrograde ellipse about L4 with semimajor axis about **60,000 mi**; Kolenkiewicz and Carpenter: about **90,000 mi** and a second of about **88,000 mi**; Kamel (third-order Lie-transform analysis): "two large stable one-month elliptic periodic orbits synchronized with the sun", which become quasi-periodic with lunar eccentricity, the effect on size "small" | Kamel, NASA CR-1622, Aug 1970 (F14) | Primary | SP-413 ch. 2 (F6): stable equilibrium "possible only in particular orbits around L4 and L5", period "about one month"; Heppenheimer (F12): colony orbit "about 90,000 miles from its central libration point" | High for existence and order of size; the abstract's own number is lost to OCR |
| Station-keeping at Earth-Moon L4/L5 | **No published annual delta-v found** | S9 | — | — | Gap (see Open threads) |
| Eclipses at Earth-Moon L5 (qualitative) | "Occultation of the sun in that orbit is rare and brief. L4 is equally usable." | Appendix to O'Neill-era colony material citing Physics Today Sept 1974, nss.org CoEvolution book (F3) | Primary-era document via NSS mirror; no number | SP-413 ch. 4 (F5): near-Earth and near-Moon orbits rejected "because of the frequency and duration of solar eclipses"; it gives no L5 figure | Medium (qualitative only) |
| Solar eclipses from an L4 orbit (by the Moon) | "a total solar eclipse from L4 which, depending on the details of the orbit, should occur only once or very few times per month and last of order of a few hours" | Richichi et al. 2024, MNRAS 527, 6616 (F8) | Primary (peer-reviewed; a side remark, not an analysis) | none; the paragraph does not name the occulting body | Low-medium. Flag for the orchestrator's calculation |
| Shadow statistics across Earth-Moon libration orbits | Over one simulated year, L3, L4, L5 orbit families have "superior shadow performance" to L1/L2; "triangular libration point orbits benefit from large amplitudes"; multiple shadow-free intervals exist | He, Meng, Qiao, Li, AFC 2025, Springer LNME 2026, DOI 10.1007/978-981-95-3034-2_9 (F7, abstract) | Primary (abstract only) | Acta Astronautica 222 (2024) 457: 3:1 resonant L4/L5 axial orbits optimal for eclipse avoidance (search abstract) | Medium (no numbers) |
| Earth's shadow at lunar distance (analog for L4/L5, same distance from Earth) | 12,064 lunar eclipses in 5,000 yr: 4,378 penumbral, 4,207 partial, 3,479 total; 2 to 5 lunar eclipses per calendar year; longest totality about 99.8 min; longest partial eclipse about 210 min; longest penumbral about 296.5 min | Espenak and Meeus, NASA TP-2009-214173 (F45); Espenak, EclipseWise statistics (F46) | Primary (NASA TP) + author's site | LRO: 151 min in shadow on 21 Dec 2010 (F15) | High for the Moon itself; **an analog only**: the points lead or trail the Moon by 60 degrees, so their shadow passages are not the Moon's |
| Kordylewski dust clouds: status | L5 cloud detected 16 times, L4 cloud 5 times (visual/photometric); first polarimetric evidence for L4 on 3 Jul 2022, L5 again on 31 Oct 2021; clouds are "very faint in scattered light"; simulated structure "inhomogeneous, temporally changing particle density composed of several particle clusters"; 2 to 4 dust conglomerates per pattern; L5 can capture up to 9% more particles than L4 | Slíz-Balogh et al. 2023, MNRAS 518, 5236 (F9) | Primary | Part II (F11) | High for detection claims; existence still debated in the literature it cites |
| Kordylewski clouds: in-situ dust | Hiten's Munich Dust Counter "passed through the L4 and L5 points ... but did not find an obvious increase in dust concentration compared to the surrounding space"; Roach (1975, OSO-6): angular size "about 6o as seen from the Earth" | Slíz-Balogh, Barta, Horváth 2019, Part II, arXiv 1910.07471 citing Igenbergs et al. 2012 and Roach 1975 (F11) | Primary (cites primary) | none opened (Igenbergs chapter not read) | Medium. **No number density found anywhere** |
| Particle residence | Test particles near L5 can stay "even for 10^6 d", with "long-existing (for 30–50 yr) particle islands" | F9 (citing simulations) | Primary | none | Medium |

### 3C. Sun-Earth L4/L5 and Earth trojans

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| 2010 TK7 | About 300 m object found by WISE; librates about Sun-Earth L4; e = 0.191 giving 0.81 to 1.19 AU each year; i = 20.9 deg | John, Graham, Abell (NASA JSC), LPSC abstract, NTRS 20150002915 (F40), citing Connors, Wiegert, Veillet 2011, Nature 475, 481 | Primary | Discoverer's page (F37): "195-year cycles"; no closer than 20 million km in the next 10,000 yr; CFHT (F38): stable at least 10,000 yr | High |
| Earth-trojan status | 2010 TK7 was "Earth's first, and to date only-known, Trojan asteroid" at that writing; Sun-Earth L4/L5 "points of quasi-stable equilibria" | F40 | Primary (abstract) | none (later discoveries not searched) | Medium (dated) |
| STEREO at L4/L5 | 2009: the spacecraft imaged the L4 and L5 regions "in the hopes of finding material that might have been left over from the original formation of the Solar System" | NASA SVS 3591, 9 Apr 2009 (F39) | Primary (agency) | no results page found | Medium (goal only) |
| Dust near Earth's orbit | Earth's resonant ring: "a relative paucity of particles within 0.1 AU of the Earth, followed by an enhancement in a cloud that is centered 0.2 AU behind Earth with a width of 0.08 AU"; sky "~3% brighter at 8 µm" inside it | Reach 2010, Icarus 209, 848 (F56) | Primary | Kordylewski paper (F9) cites the same result | High. The blob is about 11 deg behind Earth (derived), **not at L5** (60 deg) |
| Published spacecraft design at Sun-Earth L5 | EASCO (NASA GSFC Mission Design Lab): transfer about 2 yr; delta-v about 1.5 km/s with electric propulsion (about 55 kg xenon) or about 950 m/s chemical (about 300 kg); final orbit a = 1 AU, e at most 0.0167; solar array 13.71 m2, **operating temperature 70 C assumed**; 24 Ah battery for launch and contingencies only | Gopalswamy et al. 2011, arXiv 1109.2929 (F44) | Primary (study) | ESA Vigil: transfer period "2 months + n*years", out-of-plane component reduces delta-v (Renk, IAC 2024, F43) | Medium-high (study) |
| Station or habitat at Sun-Earth L4/L5 | **No published analysis of a crewed station found** | — | — | — | Gap |

### 3D. Heat storage with flight heritage or flight-qualified development

(Builds on sibling `waste_heat_utilization.md` 3E, which already holds IceCube hexadecane, LRV/Orion pentadecane at about 48.8 kJ/kg system level, the LiCl absorber and the regolith wadi.)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| LRV heat sinks | "fusible mass heat sinks" in a passive system that "stores internally generated energy during operation with subsequent radiation to space" | Elliott, Paoletti, Britt, Aug 1972, NTRS 19720055484 (F50) | Primary (abstract) | Quinn et al. (F51): "two boxes of wax to absorb heat from the battery and the drive control electronics" | High |
| PCM system-level mass fraction | Design estimates for a 54 lb pentadecane sink: wax 29% to 51% of unit mass (compact exchanger), 31% to 39% (packed bed), 35% to 39% (shell-in-tube); "unlikely to have a mass percentage over 40%, even with significant development"; trade baseline 30.8% | Quinn, Hodgson, Stephan, ICES 2010, NTRS 20110010960 (F51) | Primary | Sibling R25: about 30% PCM, about 50 kJ/kg | High |
| Heat of fusion, common PCMs | Paraffin 140 to 280 kJ/kg (20 to 60 C); water 333; glycerol 199; PEG 600 146; pentadecane 162.8 (plus 43.3 solid-solid) | NASA SoA 2024 ch. 7, Table 7-8 (F24); F51 | Primary | F52: wax about 200, water 333 kJ/kg | High |
| Ice vs wax | Water ice heat sink can lower equivalent system mass; freezing expansion is the engineering problem | F51; Leimkuehler and Stephan (F52) | Primary | none | High |
| Use of thermal storage | Thermal storage units are used for "repeated temperature cycling", high-dissipation events, "or a temporary change in the environment such an eclipse"; hard on small satellites "because of the extra mass of the housing" | F24 | Primary | none | High |
| Spacecraft thermal mass as storage (flown) | LRO pre-heated avionics before a 151-min eclipse to "store some of the heater power in the thermal mass of the spacecraft" | F15 | Primary | none | High |
| Lunar-night survival by radioisotope heat | Flight heritage: Lunokhod (Po-210), Chang'e-3/Yutu (Pu-238), RHUs on Mars rovers; RHU "≈1 W th each"; a crewed-rover study: night heat deficit 204 Wth over 125 h = 26.3 kWh, against "≈125 hours rather than >350 hours" if sites with short nights are chosen | Slusser, Wilcox, Hernandez, TFAWS 2023 (F53) | Primary (NASA workshop) | MER WEB (F54): insulation + electronics waste heat + RHUs + survival heaters keep +50 to -40 C | High for heritage list; study figures are analysis |

### 3E. Batteries as the eclipse-power alternative

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| ISS Li-ion ORU | 1 Li-ion ORU replaces 2 NiH2 ORUs; about **15 kWh** vs about 4 kWh each; 30 GS Yuasa 134 Ah cells (LiCoO2/graphite), 3,530 g each; ORU spec weight 435 lb; "10 year/60,000 cycle life target (minimum 48 A-hr capacity at end of life)" | Dalton et al., NASA Aerospace Battery Workshop, 15 Nov 2016, NTRS 20170004112 (F30) | Primary | none | High |
| Flown 18650 cells | LG ICR18650 B3 191 Wh/kg; Panasonic NCR18650B 243; Molicel 182; Canon BP-930s 112; LG MJ1 260 (PACE); "latest cells have all exceeded 240 Wh/kg"; typical Li-ion operating range -20 to 60 C | NASA SoA 2024 ch. 3 Power (F32) | Primary | none | High (cell level only) |
| GEO eclipse-season life test | Season 44 days, one discharge per day, eclipses "from a few minutes to 70 minutes"; maximum eclipse discharge 75% of nameplate (85 Ah of 113.5 Ah); 20 accelerated seasons = 10 yr; "No degradation in 20 °C capacity after 20 seasons" | Tucker et al., GOES-R Li-ion life test, NASA Aerospace Battery Workshop 2018, NTRS 20190001376 (F33) | Primary | none | High (one chemistry, one vendor) |
| LRO battery in a long eclipse | Designed to 70% DOD; more than 100% margin in the 151-min eclipse | F15 | Primary | none | High |

### 3F. Radiator coatings and radiator mass at 1 AU

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| OSRs and metallized Teflon, BOL | 8-mil quartz mirror alpha 0.05 to 0.08, epsilon 0.80; 5-mil silvered Teflon 0.05 to 0.09 / 0.78; 2-mil silvered Teflon 0.05 to 0.09 / 0.66; 5-mil aluminized Teflon 0.10 to 0.16 / 0.78 | Gilmore, Stuckey, Fong, Spacecraft Thermal Control Handbook vol. I, ch. 4, Table 4.1 (F25) | Primary (handbook; unofficial mirror) | RP-1121 (F27): silver-backed Teflon 2 / 5 / 10 mil = 0.08/0.68, 0.08/0.81, 0.09/0.88; aluminum-backed 0.08/0.66, 0.13/0.81, 0.13/0.87; NASA SoA (F24): FEP/Ag/Inconel 0.07 to 0.08, Thales OSR 0.08 (alpha only) | High |
| White paints, BOL | Z93 0.17 to 0.20 / 0.92; S13G-LO 0.20 to 0.25 / 0.85; ZOT 0.18 to 0.20 / 0.91; Chemglaze A276 0.22 to 0.28 / 0.88 | F25 | Primary | RP-1121: Z-93 0.17/0.92, S-13G 0.20/0.90, A-276 0.26/0.88 | High |
| End-of-life behavior | Degradation raises solar absorptance "with little or no effect on IR emittance"; S13GLO-type white paint "may rise from around 0.20 to 0.70 in just a few years"; quartz mirrors take "essentially no damage from UV and charged particles", contamination only; Teflon degradation "strongly depends on orbit" (worse in GEO than LEO); interplanetary missions see "the same degradation environments ... only at different intensities"; radiators are oversized for end-of-life solar load and run cold early, sometimes needing heaters | F25 | Primary | RP-1121: A-276 0.26 to 0.44 after 1,036 equivalent Sun hours of UV; Z-202 0.25 to 0.40 after 1,000 ESH; NASA SoA: BOL datasheet values "should not be used for EOL modeling" | High (qualitative and Earth-orbit figures); **no free-space 1 AU EOL figure found** |
| Kapton and blanket outer layers | Kapton and Beta cloth "can turn almost black after several years in GEO"; less severe in LEO | F25 | Primary | none | Medium-high |
| Radiator areal mass, design studies | 5.24 to 12.76 kg/m2 for heat-pipe radiators in reactor-system designs (SP-100 8.00, Kilopower 5.24, JIMO 7.16, Prometheus FSPS 5.89, SAIRS 11.7 to 12.8); NASA target at most 3 kg/m2; a project design at 2.97 kg/m2 | El-Genk, NASA ESI final report, 14 Feb 2025 (F28) | Primary (grant report; designs, not flown) | Quinn et al. (F51) assumed 1.0 lb/ft2 = 4.88 kg/m2 (derived); sibling ISS ORU 14.2 kg/m2 planform (flown) | Medium |
| Shuttle radiators (flown) | Eight panels, 175 m2, up to 30.5 kW, silver-backed Teflon, Freon-21 loops; about 20 kW in the popular attitude | Williams et al., NTRS 19850008616; NASA TM-100972 (F29) | Primary | the two reports agree | High; **no mass found** |

### 3G. Solar constant at 1 AU

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Mean | 1361.0 W/m2; perihelion 147.095 and aphelion 152.100 x 10^6 km; e = 0.0167 | NASA Earth Fact Sheet, updated 15 Nov 2024 (F34) | Primary | Kopp and Lean 2011 (F36): 1360.8 +/- 0.5 W/m2 at the 2008 minimum, vs the older 1365.4 +/- 1.3 | High |
| Perihelion / aphelion | 1,412.9 / 1,321.6 W/m2 (with 1,366.1 at 1 AU) | ECSS-E-ST-10-04C Table 6-2 via SPENVIS (F35) | Primary (standard) | Derived from F34: 1,407.7 / 1,316.6 W/m2 (Section 5) | High |
| Variability | 1-sigma about 0.6 W/m2; solar-cycle about 1.4 W/m2 | F35 | Primary | none | Medium-high |
| SP-413 value | "1390 W of sunlight" per m2 | SP-413 ch. 2 (F6) | Primary (1975) | superseded by F34, F36 | Low for current use |

## 4. Conflicts

- **C1. JWST hot side: 358 K or 383 K.** NASA's explainer: "parts of Webb" on the hot side reach 358 K. The 2019 test article: the *outermost sunshield layer* maximum is 383 K. Different objects (spacecraft parts vs. outer membrane); both are design or model values. Use 383 K for the membrane.
- **C2. JWST cold side: 40 K, 36 K or flight 35 to 55 K.** 36 K is the modeled minimum of the coldest layer; "about 40 K" is the round explainer figure for the cold side; 35 to 55 K is the measured primary-mirror range, hotter near the sunshield. Definition differences.
- **C3. Gaia orbit size.** Gaia Collaboration: amplitudes 120,000 x 340,000 and 180,000 km. ESA blog: a box of 263,000 x 707,000 x 370,000 km. The box is full extent, roughly twice each amplitude; consistent.
- **C4. Solar constant.** 1361.0 (NASA 2024), 1360.8 +/- 0.5 (TIM, 2008 minimum), 1366.1 (ECSS, older radiometer scale), 1390 (SP-413, 1975). Calibration epoch; the 0.37% gap between 1366.1 and 1361.0 is the old scale. The ECSS perihelion/aphelion values inherit it; the derived 1,407.7 / 1,316.6 are on the new scale.
- **C5. Earth-Moon L4/L5 orbit size.** 60,000 mi (Schechter), 88,000 and 90,000 mi (Kolenkiewicz and Carpenter), "about 90,000 miles" (Heppenheimer). Different analyses (analytical order, planar vs 3-D, inclusion of lunar eccentricity); Kamel says the third-order result differs from Ref. 14 by about 3%. A search-engine summary's "about 2,000 miles" was an OCR or reading error and is not used.
- **C6. Lucy power ratio.** 18,000 W to 500 W is a factor of 36; the inverse square from 1 to 5.70 AU is 32.5 (at 5.2 AU, 27). The extra loss is plausibly cold, low-light array behavior and different operating points. The source gives no breakdown; inference only.
- **C7. Pentadecane latent heat.** 162.8 kJ/kg (F51, solid-liquid only) vs "approximately 200 kJ/kg" for wax (F52, generic). Generic vs specific compound.
- **C8. Teflon emittance at 5 mil.** 0.78 (Gilmore) vs 0.81 (RP-1121). Measurement sets and film batches; both are BOL.

## 5. Derived figures

All arithmetic run in Python 3 (`python3 -I`), rounded. sigma = 5.670374419e-8 W m-2 K-4 (constant as used in the sibling file; not re-sourced this session).

- **D1. Perihelion/aphelion flux from NASA numbers.** 1361.0 x (149.598/147.095)^2 = 1,407.7 W/m2; 1361.0 x (149.598/152.100)^2 = 1,316.6 W/m2. Ratio 1.0692 (6.9%); ECSS ratio 1,412.9/1,321.6 = 1.0691. A station at L4/L5 of the Sun-Earth system or the Earth-Moon system has this same annual swing (it stays at about 1 AU).
- **D2. Coating equilibrium temperature at 1 AU (S = 1361 W/m2, Sun normal, no internal power).** T = (alpha S / (k epsilon sigma))^(1/4), k = 1 for a sunlit plate with an insulated back, 2 for a thin plate radiating from both faces, 4 for an isothermal sphere.
  - Silver Teflon 5 mil (0.08/0.81): 221 / 186 / 156 K. Quartz OSR (0.065/0.80): 210 / 177 / 149 K.
  - Z-93 (0.17/0.92): 258 / 217 / 182 K. S13G BOL (0.20/0.90): 270 / 227 / 191 K.
  - White paint degraded to alpha 0.70 (epsilon 0.85): 375 / 315 / 265 K. A-276 after 1,036 ESH (0.44/0.88): 331 / 278 / 234 K.
  - Black Z306 (0.95/0.89): 400 / 336 / 283 K. Bare VDA (0.12/0.04): 518 / 436 / 366 K.
- **D3. Net radiator capacity per m2 (one face, 0 K sink).** Edge-on to the Sun vs Sun-normal: silver Teflon at 300 K 372 vs 263 W/m2, at 280 K 282 vs 173; Z-93 at 300 K 423 vs 191, at 280 K 321 vs 89; degraded white paint (0.70/0.85) at 300 K 390 edge-on vs **-562 W/m2 Sun-normal** (it absorbs more than it emits). Basis: no Earth or Moon infrared or albedo; at Earth-Moon L4/L5 the Earth adds a small infrared and albedo load not computed here.
- **D4. Shuttle radiators.** 30.5 kW / 175 m2 = 174 W/m2 of radiating area at the design peak.
- **D5. ISS Li-ion ORU.** 435 lb = 197.3 kg; 15 kWh / 197.3 kg = **76 Wh/kg at ORU level**. 30 x 3.53 kg = 105.9 kg of cells; 15,000 Wh / 105.9 kg = 142 Wh/kg cell-level implied. Basis: the "~15 kWh" is a rounded slide figure, likely nameplate; usable energy is lower by the DOD limit.
- **D6. Lucy.** 853 x 10^6 km / 149.598 x 10^6 km = 5.70 AU; 1/5.70^2 = 1/32.5. Battery 44 Ah x 32 V = 1,408 Wh nominal; over 3 h, about 470 W.
- **D7. JWST sunshield.** 19.5 m x 11.4 m = 222 m2; 222 m2 x 1361 W/m2 = 303 kW at normal incidence (the paper's "~200 kW" reflects the tilted geometry and real outline).
- **D8. PCM at system level.** 162.8 kJ/kg x 0.29 to 0.51 = 47 to 83 kJ/kg; at 30.8%, 50 kJ/kg. (Latent only; sensible heat ignored.)
- **D9. Lunar-eclipse rates (analog).** 12,064 / 5,000 yr = 2.41 per year of any kind; partial + total (umbral) 7,686 / 5,000 = 1.54 per year; total 0.70 per year.
- **D10. Unit conversions.** 60,000 mi = 96,561 km; 88,000 mi = 141,622 km; 90,000 mi = 144,841 km. 1.0 lb/ft2 = 4.88 kg/m2. Reach's dust cloud: 0.2 AU behind Earth is about 11.5 deg along the orbit; width 0.08 AU about 4.6 deg.

## 6. Constraints for any inhabitant

- **Continuous sunlight and steady rejection.** Every flown Lagrange mission is designed so it is never or almost never eclipsed (JWST, Gaia, Herschel, Planck; 3A). A station near L4/L5 sees the same: the thermal design problem is continuous rejection of all power used plus absorbed sunlight, not riding out a night (3A, 3B; D3).
- **Sun-facing surfaces must be selected and replaced.** A radiator facing the Sun works only with low absorptance (silver Teflon, OSR; D3), and that absorptance rises over years while emittance stays; white paints can triple (3F). Radiators are oversized for end-of-life and need heaters early in life (3F).
- **Shading is the strongest tool.** A multilayer shield cuts about 200 kW to milliwatts and holds a cold side near 36 to 55 K with a hot side near 383 K (3A). The cost: a fixed attitude to the Sun, and torque from sunlight that has to be dumped with propellant (3A).
- **Seasonal swing of about 7% in sunlight**, 1,317 to 1,408 W/m2 (D1), with no day-night cycle; Gaia shows it in long-term temperature trends (3A).
- **Rare, long shadows where shadows exist.** Near the Earth-Moon points, Earth's shadow at lunar distance lasts up to about 1.7 h total and about 3.5 h partial for the Moon (3B, analog), versus 50 min orbital nights in low lunar orbit. LRO survived 151 min by pre-heating its own structure and drawing on a battery sized to 70% DOD (3A). Rare events still size the power and thermal system.
- **Avoiding a shadow costs propellant and must be planned years ahead.** Gaia spent 14 m/s; Planck orbit changes cost 50 to 76 m/s and still crossed shadows (3A).
- **Orbit, not point.** At Earth-Moon L4/L5 a station circles the point once a month on an orbit tens of thousands of miles across (3B). It does not hold a fixed position.
- **Dust and debris.** Micrometeoroids slowly degrade exposed optics and blankets (JWST, 3A). Kordylewski clouds, if real, are faint and variable; one in-situ pass found no obvious enhancement (3B).
- **Heat storage is mass.** Flown PCM units deliver about 50 kJ/kg at system level (3D, D8); a flown Li-ion pack about 76 Wh/kg = 274 kJ/kg of electricity (D5). A human-shaped machine, or any equipment, that must ride through a shadow on stored heat carries this penalty.
- **Far from the Sun the same machine needs heaters, not radiators.** Lucy keeps its heater budget below 192 W out of 500 W at about 5.7 AU (3A).

## 7. Candidate handwaves

- **A Sun-facing radiator that stays white for decades.** All data opened show solar absorptance rising with exposure (3F). Any design that assumes BOL coatings over a long station life is bending the record. Not accepted.
- **"No eclipses ever" at Earth-Moon L4/L5.** Sources say only "rare and brief" (3B); the orchestrator's calculation decides. A design that assumes zero shadow is unsupported. Not accepted.
- **Station-keeping cost at Earth-Moon L4/L5 taken as zero.** No published figure was found (3B); Sun-perturbed orbits are stable in the analyses, but real-spacecraft costs (solar pressure, model error) are unknown. Not accepted.
- **Kordylewski clouds as a hazard or a resource.** No density figure exists in any source opened. Treating them as either is invention. Not accepted.

## 8. Open threads

- **Earth-Moon L4/L5 eclipse numbers.** He et al. 2026 (Springer, paywall) and the 2024 Acta Astronautica axial-orbit paper (HTTP 403 when opened) likely hold numerical shadow statistics. Next: author preprints, CNKI, or a library copy. The Richichi et al. remark needs a check against the orchestrator's geometry.
- **Earth-Moon L4/L5 station-keeping delta-v per year.** Not found. Next: Salnikova, Stepanov and Shuvalova 2018; Schutz and Tapley (1970s) on L4/L5 station-keeping; Farquhar's thesis (NASA TR R-346) for the L4/L5 discussion.
- **Kordylewski cloud number density and Igenbergs et al. 2012 (Hiten MDC).** Not read; the Wang et al. 2021 review PDF not retrieved.
- **Queqiao.** The 13,000 km Z-amplitude, 14-day period and any eclipse history are unconfirmed (403 on the primary). Next: Zhang Lihua 2021 via another mirror; Chinese Journal of Space Science.
- **JWST orbit page text** (STScI user docs) not read beyond navigation; the L2 umbra radius (the "13,000 km" figure) is unconfirmed (gaia.ac.uk PDF 403).
- **Sun-Earth L4/L5 radiation dose.** The ESA Lagrange/Vigil radiation analysis returned 404; the Vigil objectives PDF host did not resolve. Next: ESA Vigil mission requirements, STEREO HET/LET publications.
- **STEREO L4/L5 results** (Trojan search outcome, dust impact counts) not found.
- **Lucy thermal design detail** (radiator, louvers, cold-case temperatures at 5.7 AU): only the summary paragraph found. Next: an ICES or TFAWS paper on Lucy thermal design.
- **Flown radiator areal mass other than ISS** (Shuttle panel mass): not found.
- **EOL absorptance specific to a free-space orbit at 1 AU** (not LEO or GEO): not found; Gilmore says interplanetary rates differ in intensity only.
- **MER RHU count and survival-heater energy:** a search summary gave 8 x 1 W and 100 Wh; not confirmed on an opened page.
- **Lunar-night PCM or regolith storage flown:** none found beyond the sibling's concepts; RHUs are the flown answer.
- **Sources found and not read:** Gaia "IN_L2_orbit" note (403); Wang et al. 2021 full text; Igenbergs et al. 2012; ESA Vigil objectives document; Planetary Society Queqiao orbit explainer (secondary).

## 9. Rejected sources

- **S36 search summary**: it gave "at L5 ... eclipse ... approximately 70 minutes ... ±22 days of the equinox ... 0.7% of the time". Those are geostationary-orbit figures attached to "L5"; rejected as a conflation.
- **S10 search summary** "L5 experiences no eclipses": not present in any opened source; contradicts "rare and brief" (F3).
- **S12 search summary** "semimajor axes about 2,000 miles": misreading of the garbled OCR in Kamel's abstract; the body text gives 60,000 to 90,000 mi.
- **S8 popular pages** (National Geographic, Live Science, Astronomy.com) for the Kordylewski "15 by 10 degrees" size: secondary; not confirmed in the primary papers, which cite about 6 degrees (Roach 1975).
- **Wikipedia, Universe Today, Naked Scientists, Space.com, Centauri Dreams, Discover, PopSci**: secondary; used only as leads.
- **F55 (arXiv 2408.04208)**: on topic for Sun visibility, not for eclipses or thermal environment.
