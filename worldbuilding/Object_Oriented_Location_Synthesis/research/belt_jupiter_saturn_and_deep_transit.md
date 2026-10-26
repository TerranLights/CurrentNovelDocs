# Research: Asteroid Belt, Jovian System, Saturnian System, and Deep Interplanetary Transit

Date of research: 2026-10-06. Brief followed: `_BRIEF.md`. No figure is from memory; each table row cites a page opened this session. Two convention constants I did not source are flagged where used: aluminum density 2.70 g/cm3 (3B) and 4.184e15 J per megaton of TNT (3F).

## 1. Scope

The main Asteroid Belt (mass, spacing, classes, rotation, gravity, light, temperature, delta-v, light delay, radiation); the Jovian system (radiation belts, Galilean moons, magnetosphere, tides, irradiance, transfer, orbit regimes); the Saturnian system (rings, Titan, Enceladus, radiation, transfer); deep transit (cosmic-ray and solar-particle dose, propulsion, thermal rejection, transfer energy); power scaling and nuclear options; a short interstellar-precursor note.

## 2. SEARCH LOG

(Appended as work proceeds. Format: date, query or URL, rating, notes.)

All entries dated 2026-10-06. "WebFetch" returns a small-model summary of the page, not the raw page; where a number matters it is cross-checked or the raw text was read via a local download (marked "raw").

| # | Query or page | Rating | Notes |
|---|---|---|---|
| 1 | Page: https://nssdc.gsfc.nasa.gov/planetary/factsheet/jupiterfact.html | useful | Jupiter bulk, orbit, irradiance 50.26 W/m2 (WebFetch summary) |
| 2 | Page: https://nssdc.gsfc.nasa.gov/planetary/factsheet/saturnfact.html | useful | Saturn bulk and orbit |
| 3 | Page: https://nssdc.gsfc.nasa.gov/planetary/factsheet/galileanfact_table.html | useful | Galilean moons table (summary lists "mean temperature"; treat temperatures as low confidence until cross-checked) |
| 4 | Page: https://nssdc.gsfc.nasa.gov/planetary/factsheet/satusatfact.html | dead | 404, died at the URL guess, not at the sources |
| 5 | Page: https://nssdc.gsfc.nasa.gov/planetary/factsheet/saturniansatfact.html | useful | Titan and Enceladus bulk and orbit |
| 6 | Page: https://nssdc.gsfc.nasa.gov/planetary/factsheet/asteroidfact.html | useful | Total asteroid mass, Ceres/Pallas/Vesta masses |
| 7 | Page: https://nssdc.gsfc.nasa.gov/planetary/factsheet/titanfact.html | dead | 404, died at the URL guess |
| 8 | Query: asteroid belt total mass fraction of Moon mass Ceres Vesta Pallas Hygiea share of mass | useful | Led to arXiv:2603.17561 and the Lucy page |
| 9 | Page: https://arxiv.org/pdf/2603.17561 (raw, via local pdftotext) | useful | Menichella, Mar 2026 preprint; belt mass, Pitjeva and Pitjev 2018 |
| 10 | Page: https://en.wikipedia.org/wiki/Asteroid_belt | thin | Secondary; used only for leads (Kirkwood gaps, dust temperature range). First 100,000 characters read |
| 11 | Query: NASA science asteroid belt facts "mostly empty" distance between asteroids spacecraft | useful | Led to Lucy and Astronomy.com |
| 12 | Query: asteroid belt number density asteroids larger than 1 km 1 million NEOWISE Hubble size frequency distribution main belt | thin | Mostly NEO-focused results; gave 0.7 to 1.2 million range lead |
| 13 | Page: https://www.astronomy.com/science/how-do-spacecraft-avoid-collisions-in-the-asteroid-belt/ | thin | Secondary (planetarium staff, Dec 23, 2024); matches Lucy page |
| 14 | Page: https://lucy.swri.edu/MainBeltDensity.html via WebFetch | dead | TLS certificate error, died at the tool; recovered with curl -k (see 15) |
| 15 | Page: same URL, raw text via curl -k into the scratchpad | useful | Lucy mission team (SwRI), Jul 30, 2025. Mass, count, volume, spacing, "far less densely packed than films" |
| 16 | Query: Bottke Jedicke ... debiased main belt size distribution ... | dead | Died at the query: I put a remembered figure in it and results returned NEO papers; no figure from it is used |
| 17 | Query: DeMeo Carry 2013 "Solar System evolution from compositional mapping of the asteroid belt" C-complex S-complex mass fraction ... | useful | Found the Nature 2014 paper (arXiv:1408.2787); year correction 2014 not 2013 |
| 18 | Page: https://arxiv.org/pdf/1408.2787 (raw via pdftotext) | thin | Mass-weighted taxonomy by zone only in figures; text gives qualitative statements and the C-type inner-belt percentages; no single belt-wide C/S/M mass split |
| 19 | Query: M-type asteroid 16 Psyche density metal content ... | useful | Leads to NASA Psyche pages |
| 20 | Page: https://science.nasa.gov/solar-system/asteroids/16-psyche/ | thin | NASA: 30 to 60 percent metal by volume; rotation just over 4 hours; page has no density or gravity |
| 21 | Query: carbonaceous chondrite water content weight percent CI CM ... | useful | Led to Garenne et al. 2014 and Beck et al. 2021 |
| 22 | Page: https://www.isterre.fr/IMG/pdf/46_2014gca.pdf (raw) | useful | Garenne et al. 2014, GCA 137:93; CI about 20, CM about 9 wt% water (cited), TGA of 26 CMs |
| 23 | Page: https://arxiv.org/pdf/2011.00279 (raw) | useful | Beck et al. "Water abundance at the surface of C-complex main-belt asteroids": 4.5 wt% volume-average (Ceres excluded), uncertainty 4 wt% (90 percent) |
| 24 | Query: Lewis "Mining the Sky" OR Kargel metallic asteroids ... | thin | Mostly popular summaries; lead to How Many Ore-Bearing Asteroids (arXiv:1312.4450) not read |
| 25 | JPL SBDB API, physical parameters for asteroids 1, 2, 4, 10, 16, 243, 253, 433 (https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=N&phys-par=1), raw JSON | useful | Primary dataset: diameter, GM, density, rotation period, albedo, spectral type with source refs |
| 26 | Page: https://science.nasa.gov/dwarf-planets/ceres/facts/ | thin | NASA says Ceres is 25 percent of belt mass; conflicts with 39 percent (see Conflicts) |
| 27 | Query: asteroid rotation period spin barrier 2.2 hours rubble pile fast rotators distribution Pravec Harris | useful | Secondary summary of Pravec and Harris 2000; critical period 3.3 h / sqrt(density) |
| 28 | Query: Ceres Dawn gravity field Park 2016 Nature ... | thin | Confirms paper identity; numbers taken from JPL SBDB (row 25) instead |
| 29 | Pages: NSSDCA fact sheets for Sun, Mars, Earth | useful | Sun: luminosity 382.8e24 W; Earth irradiance 1361.0 W/m2; Mars 586.2 W/m2; Mars orbit; Earth orbital speed |
| 30 | Page: https://ssd.jpl.nasa.gov/astro_par.html | useful | GM of Sun, Earth, Moon, Mars system, Jupiter system, Saturn system; AU; c (DE440) |
| 31 | Query: Hohmann transfer Earth to Jupiter transfer time years delta-v ... | thin | Leads only; Wikipedia and a lecture table |
| 32 | Query: NASA JPL Basics of Space Flight interplanetary Hohmann ... | dead | Died at the sources: no JPL page returned; Earth-Mars 259 days from a secondary page, not used |
| 33 | Page: https://ocw.tudelft.nl/.../AE2104-Orbital-Mechanics-Slides_11_12.pdf | dead | Died at the tool: image-only PDF |
| 34 | Page: https://fti.neep.wisc.edu/.../lecture29.pdf (raw) | useful | Santarius, University of Wisconsin lecture, Apr 2, 2004; Hohmann table Earth to belt, Jupiter, Saturn; moon escape speeds |
| 35 | Query: Galilean moons surface radiation dose rate rem per day ... | thin | Secondary summaries only |
| 36 | Query: Juno radiation vault titanium total ionizing dose ... | thin | Popular and trade pages; 1 cm Ti, about 200 kg; leads only |
| 37 | Query: ntrs.nasa.gov Europa Clipper radiation environment total ionizing dose requirement ... (extended) | useful | Andersen et al. 2020, Space Weather: 150 krad(Si) design basis, 300 krad parts; Wiley page returned 403 (dead at the source) |
| 38 | Pages: Wiley 10.1029/2019SW002340; Springer 10.1007/s11214-025-01139-9; NTRS 20205004139 | dead | 403, login redirect, and an unrelated regulator test report respectively; died at the sources |
| 39 | Query: Cooper et al. 2001 Energetic ion and electron irradiation of the icy Galilean satellites ... | useful | Identifies Icarus 149:133; NTRS annual report 20000120581 read raw but yielded no dose figures (thin) |
| 40 | Page: https://lasp.colorado.edu/mop/files/2015/08/jupiter_ch20-1.pdf (raw) | useful | Johnson et al. chapter 20 in the Jupiter book (2004): Table 20.1 energy fluxes at each Galilean moon; 60 gigarad figure |
| 41 | Page: https://arxiv.org/pdf/1706.05356 | dead | Not relevant; no Europa dose in it (died at the query, a bad guess from a search snippet) |
| 42 | Query: Europa surface radiation dose rate Sv per day ... (extended) | useful | Secondary: 5.4 Sv/day (about 540 rem/day); leads to Paranicas 2007 and Nordheim 2019 |
| 43 | Query: Europa Lander Study 2016 Report radiation ... | useful | 2.3 Mrad or 540 rem/day, 150 krad(Si) vault requirement (secondary summary) |
| 44 | Pages: NTRS 20190027385 (raw); NTRS 20190029432 (image PDF); exordo ASEC 2017 abstract | thin | 8.5 mm Al vault, about 72 kg (abstract); the NTRS PDFs held no dose-rate figure |
| 45 | Query: Nordheim Hand Paranicas 2019 GCR bombardment of Europa's surface ... | thin | Identified paper; no numbers returned |
| 46 | Query: Juno radiation monitoring investigation total ionizing dose ... Becker 2017 (extended) | thin | Identified Becker et al. 2017 (Space Sci Rev 213:507); Springer and Wiley copies not retrievable (HTML wall, died at the sources) |
| 47 | Page: https://sci.esa.int/documents/33960/35865/1567260128466-JUICE_Red_Book_i1.0.pdf (raw) | useful | ESA JUICE Definition Study Report, Sep 2014: 50 krad per equipment, 46 W/m2 worst-case solar, Europa fluxes >20 times Ganymede, JOI about 900 m/s |
| 48 | Query: ESA JUICE radiation environment total ionising dose ... (extended) | useful | Led to EUCASS paper and ESA page |
| 49 | Page: https://www.eucass.eu/doi/EUCASS2022-7148.pdf (raw) | useful | Sarri, Witasse, Cavel 2022: 85 m2 array gives under 1 kW at Jupiter end of life, over 25 percent array degradation in 4 years, 50 krad, solar constant about 27 times lower than Earth |
| 50 | Page: https://www.esa.int/Enabling_Support/Space_Engineering_Technology/Jupiter_s_radiation_belts_and_how_to_survive_them (06/04/2023) | thin | Qualitative: under 4 years at Jupiter equals 20 years of geostationary; lethal dose on Europa in hours |
| 51 | Query: Jupiter total ionizing dose rate versus orbital radius ... GIRE (extended) | useful | Led to arXiv white paper (Galileo 30 to 40 krad per crossing) |
| 52 | Page: https://arxiv.org/pdf/1908.02339 (raw) | useful | White paper for ESA Voyage 2050 (preprint, 2019): Galileo 30 to 40 krad per belt crossing behind 2.2 g/cm2 Al; electrons above 50 MeV in inner belts |
| 53 | Page: https://arxiv.org/pdf/2006.14682 (raw) | useful | Roussos and Kollmann (AGU book chapter preprint, 2020): Saturn versus Jupiter belts |
| 54 | Page: https://link.springer.com/article/10.1007/s10686-021-09801-0 | dead | Redirect to an authentication endpoint, not followed; same content found as the arXiv white paper (row 52) |
| 55 | Query: Fieseler ... radiation effects on Galileo spacecraft systems ... | thin | Identified IEEE Trans Nucl Sci 49:2739 (2002); paper itself not opened. Dose figure via the arXiv white paper |
| 56 | Query: Juno radiation dose Io torus ... krad ... Mrad ... (NASA domains) | thin | JPL article of Jun 16, 2016: vault reduces exposure about 800 times, 172 kg |
| 57 | Page: https://www.jpl.nasa.gov/news/nasas-juno-spacecraft-to-risk-jupiters-fireworks-for-science/ | useful | Jun 16, 2016: 800 times reduction, almost 400 lb vault, 37 close approaches, 20 months |
| 58 | Pages: IOPscience 10.3847/2041-8213/ab3661 (Nordheim et al. 2019) | thin | Summarized by WebFetch only; summary line "a few Gy per second at shallowest depths" looks implausible and is NOT used. GCR peak dose 6.3e-10 Gy/s at 0.92 m and a 14 GV cutoff recorded as low confidence |
| 59 | Pages: Wiley Paranicas 2007 GRL; Wiley Bagenal and Dols 2020; ResearchGate Paranicas 2009 chapter; ADS 2007GeoRL abstract; europa.nasa.gov Lander report PDF | dead | All died at the sources (403, 405, HTML wall, 404). The 5.4 Sv/day Europa surface dose therefore rests on secondary summaries only |
| 60 | Query: Europa Lander Study 2016 Report ... radiation (3 variants) | thin | Secondary: 540 rem/day (5.4 Sv/day), 150 krad(Si) lander electronics, 8.5 mm Al vault about 72 kg |
| 61 | Pages: NASA Science Europa facts, Juno ice-shell news, Ganymede facts, Callisto facts, Io facts; ESA JUICE Callisto page | useful | Moon figures (ice shell, ocean, orbit, temperature, Io torus mass loading) |
| 62 | NASA Science URLs under /jupiter/moons/<name>/facts/ and /jupiter-moons/<name>/<name>-facts/ | dead | Several 404s; died at the URL guess. Correct pattern is /jupiter/jupiter-moons/<name>/facts/ |
| 63 | Query: Io heat flow tidal heating Juno ... | thin | Secondary news: 1 to 3 W/m2 background heat flow, about 100 TW; primary Nature paper (Park et al. 2024) not opened |
| 64 | Page: https://eos.org/research-spotlights/two-moons-and-a-magnetosphere | thin | AGU Eos research spotlight on Bagenal and Dols 2020: about 1 ton/s ionized |
| 65 | Query: HOPE Callisto surface base ... Troutman | useful | Led to the NASA Langley HOPE slides |
| 66 | Page: https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20030063128.pdf (and the api path) | dead | Died at the tool (HTML / 404). Same slides read via a mirror (row 67) |
| 67 | Page: https://eltamiz.com/files/HOPE.pdf (raw) | useful | Troutman and Bethke, NASA Langley, Feb 3, 2003 (STAIF-2003); mirror of the NTRS item, not the NTRS copy itself |
| 68 | Query: Iess 2019 Science ... ring mass | useful | Found paper and open copies |
| 69 | Page: https://www.weizmann.ac.il/.../Iess-etal-2019.pdf (raw) | useful | Ring mass (1.54 +/- 0.49) e19 kg, 0.41 Mimas mass, 10^7 to 10^8 yr age. (The first PDS-atmospheres copy of the paper failed to download: dead at the file path) |
| 70 | Page: https://arxiv.org/pdf/0912.3017 (raw) | useful | Charnoz et al. chapter 17, Saturn After Cassini-Huygens (2009 preprint): rings mainly pure water ice, little contamination |
| 71 | Page: https://science.nasa.gov/mission/cassini/science/rings/ | useful | Rings about 10 m thick; lowest recorded A-ring temperature -230 C; particle sizes micron to mountain-size |
| 72 | Query: Cuzzi 2010 "An evolving view of Saturn's dynamic rings" ... 95% | thin | Paper identified; the 95 percent figure did NOT appear and is not used. Died at the sources (paywall) |
| 73 | Query: Titan surface pressure 1.5 bar ... | useful | Led to arXiv reviews |
| 74 | Pages: arXiv 1702.08611 (Horst 2017, raw); arXiv 2410.04595 (Zhang 2024, raw) | useful | Titan: 94 K, about 1.5 bar, 95 percent N2, gravity 1.35 m/s2, winds under 1 m/s at surface |
| 75 | Query: Titan surface radiation dose GCR atmosphere shielding ... Gronoff | thin | Qualitative: atmosphere stops trapped particles, GCR is the dominant source at the surface; Gronoff et al. 2011 not opened. Column mass derived myself (see Derived figures) |
| 76 | Query: Enceladus plume mass flux kg/s ... | thin | About 200 kg/s (UVIS summary, secondary); jets over 1000 m/s; primary Hansen et al. not opened |
| 77 | Query: Enceladus south polar heat output ... Howett; Thomas 2016; Waite 2017 | useful | 15.8 GW (JPL 2011, fetched); ocean about 45 km, ice shell about 20 km (secondary, from the Thomas 2016 abstract) |
| 78 | Pages: JPL "Cassini finds Enceladus is a powerhouse"; NASA 2015 global-ocean release; NTRS Nixon chapter 6 (image PDF) | thin | 15.8 GW confirmed on the JPL page; the NASA release gave no ocean numbers; chapter unreadable by WebFetch |
| 79 | Query: Zeitlin 2013 ... MSL RAD in transit to Mars | useful | 1.8 mSv/day GCR dose equivalent in cruise; SwRI release fetched (2013-05-30) |
| 80 | Page: https://www.nasa.gov/wp-content/uploads/2023/03/radiation-protection-technical-brief-ochmo.pdf (raw) | useful | NASA-STD-3001 Rev B: 600 mSv career, 250 mSv per SPE, shelter shielding; Rev E Dec 27, 2022 |
| 81 | Query: galactic cosmic ray radial gradient heliosphere ... (extended) | thin | About 3 percent/AU (protons, inner heliosphere) and 1.5 to 2.5 percent/AU at high energy (Pioneer 10 abstracts, secondary summaries); not opened in full |
| 82 | Query: NASA nuclear thermal propulsion specific impulse ... NERVA ... | useful | Led to NTRS 20190033337 |
| 83 | Page: https://ntrs.nasa.gov/api/citations/20190033337/downloads/20190033337.pdf (raw) | useful | NASA MSFC overview slides (Wilkerson, 2019): NERVA 825 to 875 s; NTP 25 to 250 klbf, 800 to 1000 s; ion NEP 2000 to 8000 s |
| 84 | Page: NEXT-C fact sheet (www1.grc.nasa.gov) (raw) | useful | NEXT: 25 to 235 mN, 4220 s max, 0.6 to 7.4 kW |
| 85 | Query: Dawn spacecraft NSTAR ... | useful | NSTAR 19 to 92 mN, 1900 to 3100 s at 0.5 to 2.3 kW; Dawn about 11 km/s delta-v, 425 kg xenon, array over 10 kW (JPL/NASA press and NTRS titles; the Dawn press kit itself not opened) |
| 86 | Queries: Kilopower KRUSTY ...; MMRTG ... | useful | KRUSTY 1.5 to 5 kWt, 28 hours; MMRTG about 110 We, 2000 Wt, 45 kg, 6 percent BOL efficiency (search summaries of NASA fact sheets) |
| 87 | Page: https://ntrs.nasa.gov/api/citations/20200001569/downloads/20200001569.pdf (raw) | thin | Kilopower higher-power paper; no usable mass or radiator figures found |
| 88 | Page: https://ntrs.nasa.gov/api/citations/20220004670/downloads/40%20kW%20Deployable%20FSP%20Paper_FINAL.pdf (raw) | useful | Oleson et al., NASA GRC: 40 kWe lunar fission surface power, 10,046 kg with margin, 18.1 percent efficiency, 126.4 kW waste heat, 133.4 m2 radiator at 395 K |
| 89 | Page: https://ntrs.nasa.gov/api/citations/20190031807/downloads/20190031807.pdf (raw) | useful | NIAC Phase II Final Report, Thomas, Paluszek, Cohen, May 2019: Direct Fusion Drive 1 MW and 10 MW point designs, mission table |
| 90 | Queries: solar sail NEA Scout ...; VASIMR VX-200 ... | useful | NEA Scout 86 m2 sail; VX-200: 200 kW, 5000 s, 5.7 N, 72 percent |
| 91 | Pages: https://ntrs.nasa.gov/api/citations/20170001499/downloads/20170001499.pdf (raw); https://www.adastrarocket.com/technical-papers-archives/Gar_AIAA-2011.pdf (raw) | useful | NEA Scout 86 m2 confirmed; Bering et al. AIAA-2011-1071 confirmed 5.7 N, 5000 s, 72 percent (a company-affiliated paper: treat as vendor-adjacent) |
| 92 | Queries: Lubin "A Roadmap to Interstellar Flight" ...; Project Daedalus final report ... | useful | Lubin found; Daedalus found only through secondary pages |
| 93 | Page: https://arxiv.org/pdf/1604.01356 (raw) | useful | Lubin, v8 dated Jan 21, 2022: Voyager 1 17 km/s, kinetic energy formula, 0.3c about 1 Mt TNT/kg, DE-STAR 4 50 to 70 GW |
| 94 | Page: https://en.wikipedia.org/wiki/Project_Daedalus | thin | Secondary only; gave 0.12c, 50 years, 54,000 t. No link to the original JBIS 1978 report; not opened |
| 95 | Query: Bond Martin "Project Daedalus" Final Report ... pdf full text (extended) | dead | Died at the sources: the 1978 report is not online in an openable form (ADS record and CD-ROM only) |
| 96 | Page: https://arxiv.org/pdf/1307.2424 (raw) | useful | DeMeo and Carry 2013 (Icarus 226): Table 5 mass by taxonomic class, Table 6 zones |
| 97 | Page: https://arxiv.org/pdf/1109.4096 (raw) | thin | Masiero et al. 2011 NEOWISE main belt (preprint): size-frequency slopes -2.5 observed, -3.5 theoretical; kink at 15 to 25 km. Number of objects over 1 km not found here |
| 98 | Pages: https://arxiv.org/pdf/2303.05099 (raw); https://arxiv.org/pdf/1903.11876 (raw) | useful | Rotation: most periods 2.2 to 20 h; about 1,600 of 32,249 below 2.2 h (as of 2022); critical period about 2.1 h at 2.5 g/cm3 |
| 99 | Page: https://arxiv.org/abs/1908.01868 | dead | Wrong arXiv id guessed by me (it is an unrelated paper); died at the query, not at the sources |
| 100 | Page: PDS targIO.PLASMA.TORUS.cat | useful | Io torus zones in Jupiter radii, composition, density over 3000 per cm3, about 1 eV inner torus (PDS catalog text via WebFetch) |
| 101 | Query: Cassini Saturn orbit insertion burn delta-v 626 m/s ... | useful | SOI 626 m/s, 96 minutes; VVEJGA, about 6.7 years |
| 102 | Pages: DESCANSO Cassini navigation (raw), NASA Cassini fact sheet (raw) | useful | SOI delta-v 626 m/s in a JPL DESCANSO article; cruise nearly seven years |
| 103 | Pages: NIST CODATA 2022 values for c, sigma, G, standard gravity, eV to J | useful | Exact or defined constants used in derived figures |
| 104 | Query: Juno solar arrays 60 m2 18,698 cells 14 kW at Earth 500 W at Jupiter ... | useful | JPL, Jan 13, 2016: more than 60 m2, about 14 kW at Earth distance, 500 W at Jupiter |
| 105 | Page: https://www.jpl.nasa.gov/news/nasas-juno-spacecraft-breaks-solar-power-distance-record/ | useful | 793 million km from the Sun at record; maximum 832 million km; 500 W; 25 times less |
| 106 | Query: Cassini three RTGs 633 watts ... ; page: NASA Cassini RTG page | thin | Page lists RTG count and RHUs only. The 882 W beginning-of-mission figure is from a search summary of a NASA page and is medium confidence |
| 107 | Query: Callisto surface radiation dose 0.01 rem per day ... (extended) | thin | Same secondary 0.01 rem per day figure; no primary reached |
| 108 | Query: solar energetic particle radial dependence ... (extended) | useful | Peak-flux exponent between -3.7 and -2, fluence between -2.7 and -1.4 (Cao et al. 2025 via the ESA Solar Orbiter nugget), but all data inside 1 AU |
| 109 | Page: https://www.cosmos.esa.int/web/solar-orbiter/-/science-nugget-radial-dependence-of-solar-energetic-particle-peak-fluxes-and-fluences | useful | Confirms the exponents and the 0.05 to 1.01 AU data range |
| 110 | Local computation (Python, scratchpad) of Hohmann transfers, irradiance, delays, gravity, rocket equation, radiators | useful | Inputs only from rows above; results in section 5 |

Total search-log rows: 110, covering roughly 58 web searches and roughly 70 page fetches or downloads (several rows group more than one). Dead ends (rows marked dead): 4, 7, 14, 16, 32, 33, 38, 41, 54, 59, 62, 66, 95, 99 (14 rows; some rows group several pages). Honest "thin" rows are marked thin.

## 3. FINDINGS

**How to read the tables.** Each source is given a key in the Source key below (publisher, title, URL, date, class). A row's *Source* cell names the key and the place in it. "WebFetch summary" means the page text was summarized by the fetch tool and I did not see the raw page; "raw" means I read the text myself (PDF converted locally, or a page fetched with curl). Where a number matters and I only had a summary, the Confidence cell says so. All dates are access dates 2026-10-06 unless the source date is stated.

### Source key

| Key | Publisher and title | URL | Date | Class |
|---|---|---|---|---|
| S1 | NASA NSSDCA, Jupiter Fact Sheet | https://nssdc.gsfc.nasa.gov/planetary/factsheet/jupiterfact.html | accessed 2026-10-06 (WebFetch summary) | primary (agency dataset) |
| S2 | NASA NSSDCA, Saturn Fact Sheet | https://nssdc.gsfc.nasa.gov/planetary/factsheet/saturnfact.html | accessed 2026-10-06 (WebFetch summary) | primary |
| S3 | NASA NSSDCA, Galilean Satellite table | https://nssdc.gsfc.nasa.gov/planetary/factsheet/galileanfact_table.html | accessed 2026-10-06 (WebFetch summary) | primary |
| S4 | NASA NSSDCA, Saturnian Satellite Fact Sheet | https://nssdc.gsfc.nasa.gov/planetary/factsheet/saturniansatfact.html | accessed 2026-10-06 (WebFetch summary) | primary |
| S5 | NASA NSSDCA, Asteroid Fact Sheet | https://nssdc.gsfc.nasa.gov/planetary/factsheet/asteroidfact.html | epoch JD 2457400.5 (Jan 13, 2016) for orbits (WebFetch summary) | primary |
| S6 | NASA NSSDCA, Sun, Earth and Mars Fact Sheets | https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html (also earthfact, marsfact) | accessed 2026-10-06 (WebFetch summary) | primary |
| S7 | NASA JPL Solar System Dynamics, Astrodynamic Constants (DE440, Park et al. 2021) | https://ssd.jpl.nasa.gov/astro_par.html | accessed 2026-10-06 (WebFetch summary) | primary |
| S8 | NASA JPL Small-Body Database API, physical parameters for asteroids 1, 2, 4, 10, 16, 243, 253, 433 | https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=N&phys-par=1 | accessed 2026-10-06 (raw JSON) | primary (dataset, each value carries its own paper reference) |
| S9 | M. Menichella, "Mass Inventory of the Solar System Beyond the Sun" arXiv:2603.17561 | https://arxiv.org/pdf/2603.17561 | v2, Apr 11, 2026 (raw) | primary (preprint; compiles Pitjeva and Pitjev 2018, Dawn) |
| S10 | SwRI / NASA Lucy mission, "The Density of the Asteroid Belt", I. Knudsen | https://lucy.swri.edu/MainBeltDensity.html | Jul 30, 2025 (raw via curl) | primary-institutional (mission team outreach, not peer reviewed) |
| S11 | Astronomy magazine, "How do spacecraft avoid collisions in the asteroid belt?", E. Herrick-Gleason | https://www.astronomy.com/science/how-do-spacecraft-avoid-collisions-in-the-asteroid-belt/ | Dec 23, 2024 (WebFetch summary) | secondary |
| S12 | F. DeMeo and B. Carry, "The taxonomic distribution of asteroids from multi-filter all-sky photometric surveys", Icarus 226, arXiv:1307.2424 | https://arxiv.org/pdf/1307.2424 | Jul 9, 2013 (raw) | primary (peer reviewed, preprint copy) |
| S13 | F. DeMeo and B. Carry, "Solar System evolution from compositional mapping of the asteroid belt", Nature 505, arXiv:1408.2787 | https://arxiv.org/pdf/1408.2787 | 2014 (raw) | primary |
| S14 | Garenne et al., "The abundance and stability of water in type 1 and 2 carbonaceous chondrites", Geochim. Cosmochim. Acta 137:93 | https://www.isterre.fr/IMG/pdf/46_2014gca.pdf | 2014 (raw) | primary |
| S15 | Beck et al., "Water abundance at the surface of C-complex main-belt asteroids", arXiv:2011.00279 | https://arxiv.org/pdf/2011.00279 | 2020 preprint (journal 2021) (raw) | primary (preprint) |
| S16 | NASA Science, Asteroid Psyche | https://science.nasa.gov/solar-system/asteroids/16-psyche/ | accessed 2026-10-06 | primary |
| S17 | NASA Science, Ceres Facts | https://science.nasa.gov/dwarf-planets/ceres/facts/ | accessed 2026-10-06 (WebFetch summary) | primary (outreach) |
| S18 | A. Carbognani, "The spin-barrier ratio for S and C-type main asteroids belt", arXiv:1903.11876; and MNRAS preprint arXiv:2303.05099 | https://arxiv.org/pdf/1903.11876 ; https://arxiv.org/pdf/2303.05099 | 2019; Mar 10, 2023 (raw) | primary (preprints) |
| S19 | J. Santarius, "Travel to Asteroids and Moons", Lecture 29, NEEP 533, Univ. of Wisconsin | https://fti.neep.wisc.edu/fti.neep.wisc.edu/neep533/SPRING2004/lecture29.pdf | Apr 2, 2004 (raw) | secondary (course slides) |
| S20 | ESA, "JUICE Definition Study Report" (Red Book), ESA/SRE(2014)1 | https://sci.esa.int/documents/33960/35865/1567260128466-JUICE_Red_Book_i1.0.pdf | Sep 2014 (raw) | primary |
| S21 | G. Sarri, O. Witasse, C. Cavel, "The JUICE Mission to Jupiter and its Icy Moons", EUCASS 2022, DOI 10.13009/EUCASS2022-7148 | https://www.eucass.eu/doi/EUCASS2022-7148.pdf | 2022 (raw) | primary (conference paper by mission staff) |
| S22 | E. Roussos and P. Kollmann, "The radiation belts of Jupiter and Saturn", AGU book chapter, arXiv:2006.14682 | https://arxiv.org/pdf/2006.14682 | Jun 25, 2020 (raw) | primary (preprint) |
| S23 | White paper for ESA Voyage 2050, "The in-situ exploration of Jupiter's radiation belts", arXiv:1908.02339 | https://arxiv.org/pdf/1908.02339 | 2019 (raw) | primary (preprint, community white paper) |
| S24 | R. E. Johnson et al., "Radiation effects on the surfaces of the Galilean satellites", Ch. 20 in Jupiter: The Planet, Satellites and Magnetosphere (2004) | https://lasp.colorado.edu/mop/files/2015/08/jupiter_ch20-1.pdf | 2004 (raw) | primary (handbook chapter) |
| S25 | NASA JPL, "NASA's Juno spacecraft to risk Jupiter's fireworks for science" | https://www.jpl.nasa.gov/news/nasas-juno-spacecraft-to-risk-jupiters-fireworks-for-science/ | Jun 16, 2016 (WebFetch summary) | primary (outreach) |
| S26 | NASA JPL, "NASA's Juno spacecraft breaks solar power distance record" | https://www.jpl.nasa.gov/news/nasas-juno-spacecraft-breaks-solar-power-distance-record/ | Jan 2016 (WebFetch summary) | primary (outreach) |
| S27 | Wurz et al., "An impacting descent probe for Europa and the other Galilean moons", arXiv:1711.02452 | https://arxiv.org/pdf/1711.02452 | 2017 (raw) | primary (preprint) |
| S28 | Europa Lander radiation abstract (ASEC 2017) and search summaries of the NASA 2016 Europa Lander Study report | https://programme.exordo.com/asec2017/delegates/presentation/25 | 2017 (WebFetch summary) | secondary (abstract and summaries; the report PDF could not be opened) |
| S29 | Nordheim, Jasinski, Hand, "Galactic cosmic-ray bombardment of Europa's surface", ApJ Letters 881:L29 | https://iopscience.iop.org/article/10.3847/2041-8213/ab3661 | Aug 2019 (WebFetch summary) | primary (peer reviewed; seen only through a summary) |
| S30 | NASA Science, Europa Facts; JPL, "NASA's Juno measures thickness of Europa's ice shell" | https://science.nasa.gov/jupiter/jupiter-moons/europa/europa-facts/ ; https://www.jpl.nasa.gov/news/nasas-juno-measures-thickness-of-europas-ice-shell/ | accessed 2026-10-06 (WebFetch summaries) | primary (outreach) |
| S31 | NASA Science, Ganymede Facts and Callisto Facts; ESA, "JUICE's secondary target: Callisto" | https://science.nasa.gov/jupiter/jupiter-moons/ganymede/facts/ ; https://science.nasa.gov/jupiter/jupiter-moons/callisto/facts/ ; https://sci.esa.int/web/juice/-/59907-juice-s-secondary-target-callisto | accessed 2026-10-06 (WebFetch summaries) | primary (outreach) |
| S32 | AGU Eos, "Two moons and a magnetosphere" (on Bagenal and Dols 2020); NASA PDS Io plasma torus catalog text | https://eos.org/research-spotlights/two-moons-and-a-magnetosphere ; https://pds.nasa.gov/data/pds3/releases/latest/2026/202603-naif/zzold/targIO.PLASMA.TORUS.cat | accessed 2026-10-06 (WebFetch summaries) | secondary (news summary) and primary (catalog) |
| S33 | P. Troutman and K. Bethke (NASA Langley), "Revolutionary Concepts for Human Outer Planet Exploration (HOPE)", STAIF-2003 slides | https://eltamiz.com/files/HOPE.pdf (mirror of NTRS 20030063128) | Feb 3, 2003 (raw) | primary (NASA concept study; mirror copy) |
| S34 | L. Iess et al., "Measurement and implications of Saturn's gravity field and ring mass", Science 364:eaat2965 | https://www.weizmann.ac.il/EPS/kaspi/sites/EPS.kaspi/files/uploads/Publications/Iess-etal-2019.pdf | Jun 14, 2019 (raw) | primary |
| S35 | S. Charnoz et al., "Origin and evolution of Saturn's ring system", arXiv:0912.3017 | https://arxiv.org/pdf/0912.3017 | 2009 (raw) | primary (book chapter preprint) |
| S36 | NASA Science, Cassini: Saturn Rings | https://science.nasa.gov/mission/cassini/science/rings/ | accessed 2026-10-06 (WebFetch summary) | primary (outreach) |
| S37 | S. Horst, "Titan's atmosphere and climate", JGR, arXiv:1702.08611; X. Zhang, "Atmospheres of Solar System moons and Pluto", arXiv:2410.04595 | https://arxiv.org/pdf/1702.08611 ; https://arxiv.org/pdf/2410.04595 | Mar 2017; 2024 (raw) | primary (review preprints) |
| S38 | NASA JPL, "Cassini finds Enceladus is a powerhouse"; search summaries of Thomas et al. 2016, Waite et al. 2017, Hansen et al. | https://www.jpl.nasa.gov/news/cassini-finds-enceladus-is-a-powerhouse/ | Mar 7, 2011 (WebFetch); others secondary | primary (JPL release) and secondary |
| S39 | JPL DESCANSO Article 17, "Cassini Navigation Performance Assessment" | https://descanso.jpl.nasa.gov/DPSummary/DESCANSO17_Cassini_RevA.pdf | undated in extraction (raw) | primary |
| S40 | Zeitlin et al., "Measurements of energetic particle radiation in transit to Mars on MSL", Science 340:1080; SwRI press release | https://www.swri.org/press-release/swri-led-team-calculates-radiation-exposure-associated-trip-mars | May 30, 2013 (WebFetch summary) | primary (journal, via release) |
| S41 | NASA OCHMO, "Design for Ionizing Radiation Protection", OCHMO-TB-020 Rev E | https://www.nasa.gov/wp-content/uploads/2023/03/radiation-protection-technical-brief-ochmo.pdf | Dec 27, 2022 (raw) | primary (agency technical brief derived from NASA-STD-3001) |
| S42 | R. Wilkerson (NASA MSFC), "Nuclear Thermal Propulsion: An Overview of NASA Development Efforts" | https://ntrs.nasa.gov/api/citations/20190033337/downloads/20190033337.pdf | Oct 2019 (raw) | primary (agency slides) |
| S43 | NASA GRC, NEXT-C fact sheet | https://www1.grc.nasa.gov/wp-content/uploads/NEXT-C_FactSheet_11_1_21_rev4.pdf | Nov 2021 (raw) | primary |
| S44 | Search summaries of NSTAR and Dawn ion propulsion (NASA GRC, NASA/JPL) | https://www.grc.nasa.gov/WWW/ion/past/90s/nstar.htm ; https://science.nasa.gov/mission/dawn/technology/ion-propulsion/ | accessed 2026-10-06 (search summaries only) | secondary (summaries of primary pages) |
| S45 | S. Oleson et al. (NASA GRC), "A Deployable 40 kWe Lunar Fission Surface Power Concept" | https://ntrs.nasa.gov/api/citations/20220004670/downloads/40%20kW%20Deployable%20FSP%20Paper_FINAL.pdf | 2022 (raw) | primary (NASA concept study) |
| S46 | S. Thomas, M. Paluszek, S. Cohen, "Fusion-Enabled Pluto Orbiter and Lander", NIAC Phase II Final Report | https://ntrs.nasa.gov/api/citations/20190031807/downloads/20190031807.pdf | May 15, 2019 (raw) | primary (NASA-funded concept study; not peer reviewed) |
| S47 | E. Bering et al., "Performance studies of the VASIMR VX-200", AIAA-2011-1071 | https://www.adastrarocket.com/technical-papers-archives/Gar_AIAA-2011.pdf | Jan 2011 (raw) | primary-vendor (authors affiliated with the developer) |
| S48 | L. Johnson et al., "Near Earth Asteroid (NEA) Scout" | https://ntrs.nasa.gov/api/citations/20170001499/downloads/20170001499.pdf | Dec 2016 (raw) | primary |
| S49 | P. Lubin, "A Roadmap to Interstellar Flight", arXiv:1604.01356 v8 | https://arxiv.org/pdf/1604.01356 | Jan 21, 2022 (raw) | primary (preprint of a JBIS paper) |
| S50 | NIST CODATA 2022 values: c, sigma, G, standard gravity, eV to J | https://physics.nist.gov/cgi-bin/cuu/Value?c (and sigma, bg, gn, evj) | 2022 recommended values (WebFetch summary) | primary |
| S51 | NASA Science and search summaries: Juno solar arrays, Cassini RTGs, MMRTG, KRUSTY | e.g. https://science.nasa.gov/mission/cassini/radioisotope-thermoelectric-generator/ | accessed 2026-10-06 (summaries) | primary (outreach) / secondary summaries |
| S52 | Secondary pages used for leads only: Wikipedia "Asteroid belt", "Project Daedalus"; Cosmos ESA nugget (Cao et al. 2025); AGU/Pioneer abstracts via search summaries | https://en.wikipedia.org/wiki/Asteroid_belt ; https://en.wikipedia.org/wiki/Project_Daedalus ; https://www.cosmos.esa.int/web/solar-orbiter/-/science-nugget-radial-dependence-of-solar-energetic-particle-peak-fluxes-and-fluences | accessed 2026-10-06 | secondary |

### 3A. Asteroid Belt

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Total mass of the main belt | 2.39e21 kg (about 4.0e-4 Earth masses, plus or minus 20 percent); other estimates 2.1e21 (Dawn-based, SwRI), 2.3e21 (NSSDCA), 2.7e21 (DeMeo and Carry total), 3.0e21 (Kuchynka and Folkner, cited by S12) | S9 sec. 3.3.2; S10; S5; S12 sec. 8 | Primary (preprint compiling ephemeris fits); primary-institutional; primary | Four independent statements, all within 2.1 to 3.0e21 | High for "2 to 3 e21 kg"; medium for the third digit (see Conflicts) |
| Belt mass relative to the Moon | About 3 percent (derived 3.25 percent from 2.39e21 over 7.346e22 kg); S10 says 3 to 4 percent | S9 (Moon mass in its table) and S10 | Primary | S10 | High |
| Extent of the belt | 2.06 to 3.27 AU (edges at the 4:1 and 2:1 resonances with Jupiter); most main-belt asteroids lie between 2.2 and 2.9 AU | S9 sec. 3.3; S5; S52 (Kirkwood gaps) | Primary; secondary | S5 and S9 agree | High |
| Mass concentration | Ceres 939.3e18 kg (Dawn) is 39 percent; Ceres, Vesta (259.076e18 kg), Pallas, Hygiea together 1.49e21 kg or 62 percent of 2.39e21 | S9 sec. 3.3.1 | Primary | S12: Ceres, Vesta, Pallas, Hygiea are about 31, 9, 7, 3 percent of 3.0e21 | High |
| Number of asteroids | 0.7 to 1.9 million with diameter of 1 km or more; about 10,000 above 10 km; hundreds of millions down to dust sizes | S10 | Primary-institutional | S11: 1.1 to 1.9 million (secondary); S52: over 200 above 100 km, 0.7 to 1.7 million above 1 km (secondary) | Medium (range is wide; debiased survey paper not opened) |
| Size-frequency slope | Theoretical strengthless collisional slope -3.5; preliminary observed slope for smaller objects -2.5; a change of slope between 15 and 25 km | Masiero et al. 2011 preprint (arXiv:1109.4096, raw; log row 97) | Primary (preprint, labeled preliminary) | None found | Low (preliminary, not debiased) |
| Volume of space the belt occupies | A few e25 km3 (S10); 2e26 km3 (S11); my derivation from a 2.1 to 3.2 AU annulus 1 AU thick gives 6.1e25 km3 | S10; S11; section 5.1 | Primary-institutional; secondary; derived | Derivation agrees with S10 | Medium |
| Spacing of objects: published statements | S10: average distance between asteroids larger than 1 km is "a few e5 km". S11 (and S52): "about 965,600 km". Probe collision odds "under 1 in a billion"; about 15 missions have flown through or past the belt and Lucy never has to maneuver | S10; S11; S52 | Mixed | Derived spacing for 1 km objects is 3 to 4.6 million km (section 5.1); the published figures do not reproduce from the published counts and volumes | Medium for the qualitative picture (a vast near-empty volume); low for the specific spacing numbers (see Conflicts) |
| Published reality versus popular depiction | S10 states the real belt "is far less densely packed than those often shown in the movies", and that a ship would "probably be alright" | S10 | Primary-institutional | S11 same statement | High |
| Composition by mass (all classes, total 2.70e21 kg) | C 52.5 percent (1.42e21 kg), B 11.1, P 11.0, V 9.6 (almost all Vesta), S 8.4, M 3.3 (8.82e19 kg), D 2.0, K 0.95, L 0.68, A 0.37, E 0.05. With Ceres, Pallas, Vesta, Hygiea removed (45 percent of mass remains): C 14.4, P 11.0, S 8.4, B 3.6, M 3.3 | S12 Table 5 | Primary | S13 states primitive (C, P) material is more than half by mass excluding the top four | High for ranking; medium for decimals (the paper says it does not claim that precision) |
| Zonal distribution by mass | Inner belt: V 69, S 21, C 6 percent. Middle belt: C 70, B 15, S 8, P 4. Outer belt: C 52, P 15, B 13, M 10, S 5. All types occur in every region | S12 Table 6; S13 | Primary | S13 text agrees | High |
| Water in carbonaceous material | CI chondrites about 20 wt percent water, CM about 9 wt percent (cited values); C-complex asteroid surfaces average 4.5 wt percent (volume-weighted, Ceres excluded), range 0 to 11.5, uncertainty 4 wt percent at 90 percent confidence; Ceres up to 25 percent water per NASA | S14 (abstract and intro); S15 (abstract, sec. 5); S17 | Primary; primary (preprint); primary (outreach) | S14 and S15 differ by design (meteorite versus asteroid surface); S15 attributes the gap to space weathering | Medium (meteorite values are cited, not measured here; asteroid values carry a 4 wt percent error) |
| Metal in M-type bodies | Psyche is 30 to 60 percent metal by volume; density 4.172 plus or minus 0.145 g/cm3; dimensions 278 by 238 by 171 km; rotation 4.196 h; M-types are 3.3 percent of belt mass by S12 | S16; S8 (Farnocchia 2024, Shepard 2021); S12 Table 5 | Primary | S8 and S16 agree on a mix of rock and metal | Medium (single large body; M-class assignment is degenerate per S12) |
| Density of a stony body | Eros (S-type): 2.67 g/cm3 with porosity 10 to 30 percent | S8 (Yeomans et al. 2000) | Primary | None | High |
| Rotation periods | Most small bodies have periods between 2.2 and 20 h; about 1,600 of 32,249 bodies with accurate periods (as of 2022) are below 2.2 h. Large bodies larger than 0.15 km show a "spin barrier" near 2.2 h; critical period about 2.1 h at 2.5 g/cm3 (Pravec and Harris; scales as 1 over the square root of density) | S18 (both papers, raw) | Primary (preprints) | Two independent preprints agree | High |
| Rotation of named bodies | Ceres 9.074 h, Vesta 5.342 h, Pallas 7.813 h, Hygiea 13.828 h, Psyche 4.196 h, Eros 5.27 h, Ida 4.634 h, Mathilde 417.7 h | S8 | Primary | None | High |
| Mass, size, density of named bodies | Ceres GM 62.6284 km3/s2, diameter 939.4 km, density 2.162 g/cm3; Vesta GM 17.2882844, 522.77 km, 3.460; Pallas GM 13.63, 513 km, 2.89; Hygiea GM 7 (poor), 407 km; Psyche GM 1.601, 222 km, 4.172; Eros GM 4.463e-4, 16.84 km, 2.67; Ida GM 0.00275, 32 km, 2.6; Mathilde GM 0.00689, 52.8 km, 1.3 | S8 | Primary | Ceres 939.3e18 kg (S9) matches S8 GM over G | High (Hygiea GM low) |
| Surface gravity and escape speed | See section 5.2: Ceres 0.284 m/s2 (2.9 percent of standard gravity) and 516 m/s; Vesta 0.253 m/s2 and 364 m/s; Psyche 0.130 m/s2 and 170 m/s; a 1 km rubble body at 2,000 kg/m3 about 2.8e-4 m/s2 and 0.5 m/s | derived from S8 and S50 | Derived | None needed (direct formula) | High for GM-based values |
| Solar irradiance at belt distances | 321 W/m2 at 2.06 AU, 218 at 2.5 AU, 127 at 3.27 AU (23.6, 16.0, 9.4 percent of the Earth value 1361.0 W/m2); derivation section 5.3 | derived from S6, S7 | Derived (inverse square) | Method reproduces S6 Mars 586.2 and S1 Jupiter 50.26 W/m2 | High |
| Temperature at belt distances | Equilibrium of a rapidly rotating black sphere: 194 K at 2.06 AU, 176 K at 2.5 AU, 154 K at 3.27 AU. Published range for dust particles: 200 K at 2.2 AU down to 165 K at 3.2 AU (secondary) | derived from S6 and S50; S52 | Derived; secondary | Same order; dust figure is warmer than a black sphere, which is expected for small grains that emit poorly | Medium (real surface temperatures depend on albedo, rotation, regolith; not measured here) |
| Delta-v and transfer time, belt | Earth heliocentric orbit to belt (Hohmann, circular coplanar): 8.75 km/s total at 2.06 AU, 11.18 km/s at Ceres' distance, 12.28 km/s at 3.27 AU; time 0.95 to 1.56 years. Lecture table: 11.7 km/s and 1.4 years. From Mars orbit: 3.36 to 7.39 km/s, 1.2 to 1.9 years | S19 table; derived (section 5.4) | Secondary (course slides); derived from S7 | Derived values bracket the lecture value (lecture matches about 2.9 AU) | High for method; medium for the specific number because it depends on which belt radius is meant |
| Communication delay to the belt | One way 8.8 min (nearest, 1.06 AU) to 35.5 min (farthest, 4.27 AU) on a circular-coplanar approximation; light time over 1 AU is 499.0 s | derived from S7 (AU, c) | Derived | S6 and S1 give Earth distances for Mars and Jupiter that reproduce the same method | High |
| Radiation at belt distances | No direct belt dose measurement was found. Galactic cosmic rays dominate and vary only slowly with distance (published inner-heliosphere radial gradient about 3 percent per AU for protons, from Pioneer 10 abstracts); solar particle peak intensity falls as heliocentric distance to the power -3.7 to -2 (data between 0.05 and 1.01 AU only) | S52 (search summaries and ESA nugget); S41 | Secondary summaries; primary brief for the dose rate used in section 5.7 | Two independent statements on SEP scaling; GCR gradient from two abstracts | Low to medium (extrapolation beyond the measured distance range) |

### 3B. Jupiter and the Galilean moons

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Jupiter bulk and orbit | Mass 1,898.13e24 kg; equatorial radius 71,492 km; rotation 9.9250 h; mean distance from the Sun 778.479e6 km (perihelion 740.595e6, aphelion 816.363e6); orbital period 4,332.589 d; escape speed 59.5 km/s | S1 | Primary | GM 126,712,764.1 km3/s2 for the Jupiter system (S7) | High |
| Irradiance at Jupiter | 50.26 W/m2 (mean). Derived perihelion and aphelion values 55.5 and 45.7 W/m2. JUICE design worst case 46 W/m2. Jupiter is about 27 times fainter than Earth (S21); Juno article says "25 times" | S1; S20 sec. 5.2.2; S21 sec. 3.2; S26 | Primary | Four statements agree to rounding; aphelion derivation reproduces S20's 46 | High |
| Distance from Earth and light delay | 588.5e6 to 968.5e6 km; one-way light time 32.7 to 53.8 minutes (derived); sunlight takes 43 minutes from the Sun | S1; S31 (Ganymede page, 43 min); derived | Primary; derived | JUICE round trip about 90 minutes (S21) | High |
| Magnetic field | Dipole 4.30 gauss times radius cubed; surface 4 to 13 gauss | S1 | Primary | S23 says the field is "20,000 times stronger than Earth's" (as stated; not defined there) | Medium (the 20,000 figure lacks a stated definition) |
| Radiation belt layout | Synchrotron (innermost) belt from 1.1 to 3 radii, electrons to tens of MeV; the belts' "core region" lies inward of Io's orbit (5.9 radii) at low magnetic latitudes; inner electrons exceed 50 MeV; magnetospheric particles fill the magnetosphere out to the magnetopause; inner region is under 10 radii, middle 10 to 40, outer over 40 | S20 sec. 2.2.2.1; S23 sec. 1.1 to 1.2; S22 | Primary | Three sources agree on the layout | High |
| Dose accumulated by a spacecraft in the belts | Galileo accumulated 30 to 40 krad per crossing of the belts' core behind 2.2 g/cm2 of aluminum (about 0.8 cm Al, derived with 2.70 g/cm3 for Al, which I did not source); about 9 such orbits equal Galileo's whole 6.5 years and 34 orbits | S23 (citing Fieseler et al. 2002 and Atwell et al. 2005) | Primary (preprint citing journal papers) | None found in a second raw source | Medium |
| Design dose anchors | Juno: 1 cm titanium vault, "about 800 times" lower exposure, almost 400 lb (172 kg), 37 close approaches over 20 months, closest approach 4,667 km above the cloud tops. JUICE: 50 krad at the outside of each equipment unit; array degradation over 25 percent in 4 years; mission external dose about 200 Mrad (S27). Europa Clipper: 150 krad(Si) design value, parts rated 300 krad, over 2 Mrad total ionizing dose expected over the mission (search summary of Andersen et al. 2020; paper not opened). Europa Lander study: electronics limit 150 krad(Si); a vault wall of about 8.5 mm aluminum, about 72 kg | S25; S20 sec. 5.2.1; S21 sec. 3.1; S27; S28 | Primary (JPL, ESA); secondary (Clipper and Lander numbers, summaries only) | Juno 1 cm Ti agrees with S25 and a search summary of a 2011 trade article (not opened) giving a vault of about 200 kg including more than 20 electronics assemblies | High for Juno and JUICE; low for Clipper and Lander |
| Which orbits are survivable | Missions have avoided the core: Clipper stays beyond about 9 radii and JUICE mostly beyond 15 radii; Juno uses a polar orbit that crosses the belts quickly and dives below them near the planet; Galileo's equatorial passes inside Europa's orbit were the high-dose ones | S23 Table 1 and sec. 1.3; S25 | Primary | S20 says JUICE's trajectory "will remain outside of Jupiter's inner radiation belts" | High |
| Surface dose, Europa | About 5.4 Sv per day (about 540 rem per day) at the surface, "lethal within hours" (ESA wording); energy flux of ions and electrons above about 10 keV 5e10 to 8e10 keV per cm2 per second (about 0.08 to 0.13 W/m2, derived), uncertain by plus or minus 50 percent | secondary summaries of S28 and ESA (https://www.esa.int/.../Jupiter_s_radiation_belts_and_how_to_survive_them, 2023-04-06); S24 Table 20.1 | Secondary (5.4 Sv per day); primary (energy flux) | S24 states the dose rate at Europa's surface is about 10^2 to 10^3 times the solar-wind dose rate at the lunar surface (a ratio, not an absolute dose); ESA says lethal within hours | Low for the Sv per day figure (primary papers were behind a paywall); medium for energy flux |
| Surface dose, other moons | Energy flux above about 10 keV: Io 1e9, Ganymede 2e8 (equator) and 5e9 (polar caps), Callisto 2e8 keV per cm2 per second. Callisto surface about 0.01 rem per day (0.1 mSv per day). Europa fluxes more than 20 times those at Ganymede (JUICE) | S24 Table 20.1; secondary summaries (Callisto dose); S20 sec. 5.1.3 | Primary (flux); secondary (Callisto dose) | S24 flux ratio Europa to Callisto is 250 to 400; ESA says Callisto sees lower radiation than Ganymede and Europa; see Conflicts for why dose and energy flux ratios differ | Medium (flux), low (Callisto dose) |
| Galactic cosmic ray dose at Europa | Peak GCR dose about 6.3e-10 Gy per second at about 0.92 m depth, about 0.02 Gy per year; magnetospheric particles dominate the top meter except at high latitudes; Jupiter's field blocks the part of the GCR spectrum below a 14 GV cutoff | S29 (summary) | Primary (via summary) | S29 abstract (via search) says the same qualitative result | Low (summary only) |
| Galilean moon bulk data | Io: diameter 3,643 km, mass 89.3e21 kg, 1.80 m/s2, escape 2.6 km/s, orbit 422e3 km (5.9 radii), period 1.8 d. Europa: 3,122 km, 48.0e21, 1.31 m/s2, 2.0 km/s, 671e3 km (9.4 radii), 3.6 d. Ganymede: 5,262 km, 148.2e21, 1.43 m/s2, 2.7 km/s, 1,070e3 km (15.0 radii), 7.2 d. Callisto: 4,821 km, 107.6e21, 1.24 m/s2, 2.4 km/s, 1,883e3 km (26.3 radii), 16.7 d. Eccentricities 0.004, 0.009, 0.001, 0.007 | S3; radii in Jupiter radii derived with 71,492 km (S1) | Primary | S19 escape speeds from the surface 2.56, 2.02, 2.74, 2.44 km/s; Ganymede orbit 1,070,000 km (S31) | High |
| Surface temperature | Mean temperatures listed as -155 C (Io), -170 C (Europa), -160 C (Ganymede), -155 C (Callisto); Ganymede daytime range 90 to 160 K | S3 (summary); S31 | Primary | Ganymede's -160 C (113 K) is inside S31's 90 to 160 K range | Medium (S3 values come from a summary) |
| Europa ice and ocean | Ice shell 15 to 25 km thick, ocean 60 to 150 km deep, about twice the water of Earth's ocean; Juno microwave radiometer: shell averages about 29 km in the region of the 2022 flyby, about 5 km thinner if the ice contains dissolved salt | S30 | Primary (outreach) | The two numbers differ by definition (region and method) | Medium |
| Ganymede and Callisto interiors | Ganymede: ocean about 100 km thick under about 150 km of mostly ice; the only moon with its own magnetic field. Callisto: possible ocean about 250 km down, evidence "less compelling"; surface about 4 billion years old; tidal heating not significant | S31 | Primary (outreach) | ESA and NASA pages agree on Callisto | Medium |
| Io tidal and volcanic activity | Tidal surface bulge about 100 m; "hundreds of volcanoes", 50 to 100 erupting at once; about 1 ton of Io's gas ionized per second; heat flow 1 to 3 W/m2, about 100 TW total (news summaries of Park et al. 2024; derived check in section 5.9) | S32; S31 (Io facts) ; search summary of Park et al. | Secondary (news); primary (NASA Io page) | Derived 2.4 W/m2 from 100 TW and Io's radius agrees | Medium |
| Io plasma torus | Extends from inside Io's orbit (about 5 radii) to about Europa's orbit; zones: inner 5 to 5.4, precipice 5.4 to 5.6, ribbon 5.6 to 6 (density over 3,000 per cm3), ledge 6 to 7.5, ramp beyond 7.5; mainly sulfur and oxygen ions; cold (about 1 eV) in the inner torus | S32 (PDS catalog) | Primary (catalog text) | S23 Figure 1 shows the torus and plasma disk | Medium |
| Transfer from Earth | Hohmann: 2.7 years and total 14.4 km/s (course table); derived 2.73 years and 14.44 km/s (departure excess 8.79, arrival excess 5.64 km/s). JUICE arrival excess 5.59 to 5.82 km/s; Jupiter orbit insertion about 900 m/s; total mission delta-v 2.6 km/s because of gravity assists | S19; derived (section 5.4); S20; S21 | Secondary; derived; primary | Three-way agreement on arrival excess (5.64 versus 5.59 to 5.82) | High |
| Transfer from Mars orbit | Derived: departure excess 5.88 km/s, arrival 4.27 km/s, sum 10.15 km/s, 3.08 years | derived from S6, S7 | Derived | Method validated against Earth rows | Medium (circular coplanar idealization) |
| Orbit regimes in the published literature | (a) Callisto surface base for crews, outside the belts: reactors of about 400 kWe at 30 kg/kWe, metals that work at 100 K, crew time away under 5 years, total trip under 5 years (NASA Langley HOPE, 2003). (b) Ganymede polar orbit at 500 km altitude after Callisto and Ganymede resonances, with Ganymede's own field giving partial shielding (JUICE). (c) Europa and Callisto flybys from distant orbits (Clipper beyond about 9 radii). (d) Polar orbit with fast belt crossings (Juno). (e) Simulations summarized as showing 60 to 75 percent lower dose in 100 to 500 km circular orbits around Europa (search summary only). | S33; S20; S21; S23; S25 | Primary (a to d); secondary (e) | (a) and (b) agree that the Callisto and Ganymede regions are the reachable ones | Medium |

### 3C. Saturn, its rings, Titan, Enceladus

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Saturn bulk and orbit | Mass 568.32e24 kg; equatorial radius 60,268 km; rotation 10.656 h; semi-major axis 1,432.041e6 km; perihelion 1,357.554e6, aphelion 1,506.527e6; period 10,755.699 d; escape speed 35.5 km/s; magnetic dipole 0.215 gauss times radius cubed, surface field 0.18 to 0.84 gauss | S2 | Primary | GM 37,940,584.84 km3/s2 for the Saturn system (S7) | High (see Conflicts for the AU figure) |
| Irradiance at Saturn | Derived 14.85 W/m2 at the mean distance (1.09 percent of Earth's 1361.0 W/m2), 16.5 at perihelion, 13.4 at aphelion. NASA text (search summary): the Sun is "nearly 90 times fainter" than at Earth, which is 1 over 91.7 from the derivation | derived from S6, S2; S51 | Derived; secondary | Method reproduces Mars and Jupiter published irradiance | High |
| Distance from Earth and light delay | 1,205.5e6 to 1,658.6e6 km; one-way 67.0 to 92.2 minutes (derived), round trip 134 to 184 minutes | S2; derived | Primary; derived | JUICE Jupiter round trip of about 90 minutes is consistent with the same method | High |
| Rings: mass | (1.54 plus or minus 0.49)e19 kg, which is 0.41 plus or minus 0.13 of the mass of Mimas; implied age 10 million to 100 million years. Derived: 0.64 percent of the asteroid belt's mass | S34 (raw) | Primary | S35 (earlier estimates "one to several Mimas masses") | High for order of magnitude, medium for the central value (the error is 32 percent) |
| Rings: thickness, composition | "About 10 m (30 ft) thick or so"; almost completely water ice; particle sizes from smaller than a grain of sand to mountain size; moonlets about 1 km; coldest recorded A-ring temperature -230 C. Mostly pure water ice with little contamination (S35) | S36; S35 | Primary (outreach); primary (chapter) | Two sources agree on water ice; no percentage found (the 95 percent figure I searched for did not appear in any source and is not used) | Medium |
| Titan bulk and orbit | Mass 1,345.5e20 kg, radius 2,575 km, density 1,880 kg/m3, gravity about 1.35 m/s2, escape about 2.64 km/s, orbit 1,221.87e3 km (20.27 Saturn radii), period 15.945 d, eccentricity 0.0292 | S4 (gravity and escape are "calculated values" in S4) | Primary | S37 Table 1: mass 13.457e22 kg, radius 2,575.0 km, gravity 1.35 m/s2 | High |
| Titan atmosphere and surface | Surface pressure about 1.5e5 Pa (1.5 bar); surface temperature 94 K; 95 percent nitrogen, under 5 percent methane, 0.1 percent hydrogen; scale heights 15 to 50 km; winds under 1 m/s at the surface rising to about 40 m/s near 60 km; surface sculpted by liquids and wind: dunes at low latitudes, hydrocarbon lakes and seas at high latitudes, river networks; surface conditions near the triple point of methane; water-ice bedrock | S37 (both, raw); NASA chapter 6 (title only) | Primary | Two independent reviews agree | High |
| Titan atmospheric shielding | Derived column mass about 11,100 g/cm2, 10.8 times Earth's 1,030 g/cm2. Qualitative: the thick atmosphere stops trapped magnetospheric particles; the dominant energetic radiation at the surface is a reduced flux of galactic cosmic rays; GCR protons and alpha particles ionize mainly near 65 km altitude (search summaries of Gronoff et al.) | derived from S37; secondary summaries | Derived; secondary | None for the dose itself | Medium for the column mass; low for dose (no number found) |
| Enceladus bulk and orbit | Mass 1.08e20 kg; radii 257 by 251 by 248 km; density 1,610 kg/m3; orbit 238.02e3 km (3.95 Saturn radii); period 1.370 d; escape about 0.24 km/s as listed in S4 (reproduced by my derivation). S4's summary also gave a surface gravity of about 0.027 m/s2, which does NOT follow from its own mass and radii: derived gravity is about 0.11 m/s2 (section 5.2), so the 0.027 figure is rejected (see Conflicts) | S4 | Primary | Gravity re-derived from mass and mean radius in section 5.2 gives 0.11 m/s2, not 0.027 | High |
| Enceladus plumes and water | Water vapor injection about 200 kg/s (UV occultations); more than 90 percent of the plume is water vapor; gas jets with Mach 5 to 8 and speeds above 1,000 m/s; internal power of the south polar terrain about 15.8 GW; a global ocean about 45 km deep under an ice shell about 20 km thick (under 5 km at the south pole); molecular hydrogen in the plume indicating hydrothermal reactions; Enceladus feeds the E ring | S38 (15.8 GW fetched; others from search summaries) | Primary (JPL 15.8 GW); secondary (the rest) | None for the 200 kg/s and ocean numbers | Medium for 15.8 GW; low for the rest |
| Saturn radiation environment, compared with Jupiter | Qualitative and published: Saturn's ion belt (over 10 MeV) spans from near the planet to Tethys (4.9 radii) and is segmented by moons and rings; the electron belt lies outside the A ring (beyond 2.27 radii), peaks near 2.5 radii, and MeV electrons are measurable only to about 7 radii; at Jupiter significant intensities reach several tens of MeV; Saturn's belts have "much lower particle fluxes" because moons and rings absorb particles and the magnetic and rotation axes are aligned. No dose-rate comparison in common units was found | S22 sec. 3 and 5 | Primary (preprint) | S23 states Saturn's belts are limited in extent while Jupiter's fill the magnetosphere | Medium (qualitative, no numbers) |
| Transfer from Earth | Hohmann: 6.0 years and 15.7 km/s (course table); derived 6.08 years and 15.74 km/s (departure excess 10.30, arrival excess 5.44). Cassini: about 6.7 years by Venus-Venus-Earth-Jupiter gravity assists; Saturn orbit insertion 626 m/s over 96 minutes | S19; derived; S39 | Secondary; derived; primary | Derived and lecture agree to 0.1 km/s | High |
| Transfer from Jupiter | Derived Hohmann Jupiter orbit to Saturn orbit: 10.04 years, 3.35 km/s heliocentric (departure excess 1.81, arrival 1.55) | derived from S1, S2, S7 | Derived | Method validated | Medium |

### 3D. Deep transit: radiation, propulsion, thermal rejection, transfer cost

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| GCR dose rate in interplanetary cruise | 1.8 mSv per day average dose equivalent inside the MSL spacecraft during its 253-day cruise (about 1 AU to 1.5 AU); about 0.66 Sv for a round trip with current propulsion; solar particles were about 5 percent of the cruise dose; "even an aluminum hull a foot thick wouldn't change the dose very much" | S40 | Primary (journal result via the SwRI release) | S41 uses 1.5 mSv per day for a transit example and about 0.5 mSv per day as the surface-mission environment | High for the 1 AU to 1.5 AU rate; shielding-specific (MSL hardware) |
| Human exposure limits | Career effective dose under 600 mSv, universal across age and sex; design reference solar particle event under 250 mSv; exposure from nuclear technologies on board under 20 mSv per mission year | S41 (raw, NASA-STD-3001 Vol. 1 Rev B) | Primary | The brief and a second search summary agree | High |
| Solar particle shelter | For a vehicle with 20 g/cm2 aluminum, a storm shelter adds 10 cm of water-equivalent shielding for a centennial event and 20 cm for a millennial event; about 95 percent of events need only "as low as reasonably achievable" practice | S41 | Primary | None | High |
| GCR dependence on distance | Published inner-heliosphere radial gradient about 3 percent per AU for protons (about 2.2 for helium); 1.5 to 2.5 percent per AU at high energy; the dose differs with solar cycle | search summaries of Pioneer 10 and IMP/Voyager papers (Webber 2004 and others, not opened) | Secondary summaries of primary papers | Two summaries agree to a few percent per AU | Low to medium |
| SEP dependence on distance | Peak intensity scales as heliocentric distance to the power -3.7 to -2; fluence -2.7 to -1.4; a power of -3 is the diffusion-theory expectation; data cover only 0.05 to 1.01 AU, so beyond 1 AU this is extrapolation | S52 (Cao et al. 2025 via ESA nugget) | Secondary summary of a primary paper | Search summary also cites an older 1/r2 assumption for scaling to Mars | Low |
| Chemical rocket | LH2 and LOX engine RS-25: vacuum specific impulse 452.3 s, vacuum thrust 512.3 klbf; J-2: 421 s, 232.3 klbf | S42 table | Primary | None | High |
| Nuclear thermal rocket | Rover and NERVA era (1955 to 1972): 20 reactors built and ground-tested; sizes tested 25, 50, 75, 250 klbf; hydrogen exit temperatures 2,350 to 2,550 K; specific impulse 825 to 850 s (hot bleed cycle, tested) and 850 to 875 s (expander cycle, chosen for the flight engine); longest single burn about 62 minutes, accumulated burn above 3.5 hours; thrust-to-weight about 3 for a 75 klbf engine. Summary band for NTP: 800 to 1,000 s at 25 to 250 klbf. HOPE slide table: 980 s or more for a bimodal engine | S42 (raw); S33 (raw) | Primary | Two NASA documents agree on the 800 to 1,000 s class | High |
| Gridded ion thrusters | NSTAR: 19 to 92 mN over 0.5 to 2.3 kW, specific impulse 1,900 to 3,100 s. NEXT: 25 to 235 mN over 0.6 to 7.4 kW, maximum 4,220 s, maximum thruster efficiency 70 percent, thruster mass under 14 kg, power processor under 36 kg. Dawn (three NSTAR engines, two used): 91 mN maximum per engine, 425 kg xenon, delta-v about 11 km/s, arrays above 10 kW | S44 (summaries); S43 (raw) | Primary (NEXT); secondary summaries (NSTAR, Dawn) | Derived thruster efficiency 61 percent for NSTAR at 2.3 kW and 35 percent at 0.5 kW from F, Isp and power (section 5.8), consistent with a throttling curve | High (NEXT), medium (NSTAR, Dawn) |
| Course-slide NEP band | Ion NEP vacuum specific impulse 2,000 to 8,000 s; thrust 2e-5 to 2e-2 klbf (about 0.09 to 89 N) | S42 | Primary (slides) | Consistent with NSTAR, NEXT, VX-200 | Medium |
| High-power electric thruster | VASIMR VX-200 test: 200 kW, specific impulse 5,000 s, thrust 5.7 N, thruster efficiency 72 percent; derived jet power 140 kW, 70 percent of 200 kW | S47 (raw) | Primary-vendor (authors tied to the developer) | Derived efficiency agrees with the reported 72 percent | Medium (vendor-adjacent; laboratory test in a vacuum chamber) |
| Electric options in the HOPE study | NEP with MPD thrusters: 8,000 s (TRL 3, 748 listed initial mass, crew time away 4.5 years); NEP with VASIMR: 5,000 to 30,000 s (TRL 2, 784, 5 years); magnetized target fusion: 75,000 s (TRL 1, 650 to 750, under 2 years). Units of the mass column are not legible in my extraction (probably metric tons) | S33 comparison table (raw) | Primary (NASA concept study, 2003) | None | Low to medium (the table was read from flattened text) |
| Fusion propulsion concept (Direct Fusion Drive) | 1 MW fusion: 4 to 5 N, 8,000 to 8,500 s, specific power 0.75 kW/kg, reactor mass 1,345 kg (magnets 285, radiators 305, shielding 160). 10 MW: 35 to 55 N, 9,900 to 12,000 s, 1.25 kW/kg, 9,400 kg. Stated mission cases: Mars 110 days (40 Mg payload, delta-v 29.4 km/s, initial mass 112,000 kg); Jupiter 1.2 years (1 Mg payload, 1 MW, exhaust 80 km/s, delta-v 55 km/s, initial mass 4,950 kg); Pluto 5 years; 125 AU in 10 years (delta-v 244 km/s). Authors' roadmap: first flight unit by about 2040 "with sufficient support"; D-3He fusion not yet demonstrated (current experiment about 0.1 T versus about 5 T needed) | S46 sec. 3.7 and Tables 19 to 23 (raw) | Primary (NASA-funded concept study, not peer reviewed) | S33's magnetized-target-fusion entry is a second fusion concept; the report's own thrust and jet power numbers disagree (see Conflicts) | Low as a design basis (concept); high as a statement of what the study claims |
| Solar sail | NEA Scout: one 86 m2 sail as primary propulsion. Radiation pressure from the solar constant: 4.54 micronewtons per m2 (absorbing) and 9.08 (ideal reflector) at 1 AU, falling as distance squared (section 5.10) | S48 (raw); derived from S6, S50 | Primary; derived | Pressure equals irradiance over c | High |
| Thermal rejection law | In vacuum a body can shed heat only by radiation: power per area equals emissivity times sigma times T to the fourth. 5.670374419e-8 W/m2/K4 | S50; section 5.11 | Primary constant; derived | S45 radiator sizing agrees in order of magnitude (section 5.11) | High |
| Thermal rejection, a published fission system | 40 kWe lunar surface system: 126.4 kW of waste heat rejected by a 133.4 m2 deployable radiator at the pole (216.2 m2 at the equator, because the surface is warmer), radiator at 395 K nominal, emissivity 0.84, solar absorptivity 0.14; end-to-end thermal-to-electric efficiency 18.1 percent (Stirling 26.1 percent); total element masses 10,046 kg with growth allowance and margin | S45 Tables I, IV and Fig. 6 (raw) | Primary (NASA concept study) | Derived 947 W/m2 over the quoted area versus 1,160 W/m2 per side from the Stefan-Boltzmann law (section 5.11) | Medium |
| Thermal rejection, a fusion concept | Radiators are 22.7 percent (1 MW) to 30.3 percent (10 MW) of reactor mass; radiator areal mass 4.2 kg/m2 in one table and 2.1 kg/m2 with emissivity 0.95 in another; radiator temperatures 300 K and 453 K | S46 Tables 21 to 28 (raw) | Primary (concept study) | Two different areal masses within the same report | Low |
| Energy and mass cost of large transfers | Derived: from a 300 km circular Earth orbit to Jupiter and capture at Callisto's orbit radius needs about 11.0 km/s; to Saturn and Titan's orbit radius about 11.3 km/s. Propellant fraction at that delta-v: 92 percent with a chemical stage (452 s), 73 to 74 percent with a nuclear thermal rocket (850 s), 20 to 31 percent with ion or plasma options (3,100 to 5,000 s), 13 percent at 8,000 s | derived from S7, S3, S42, S43, S47 | Derived | The Hohmann sums reproduce the S19 table to 0.1 km/s | Medium (impulsive idealization; low-thrust spirals add delta-v) |

### 3E. Power at distance, and nuclear alternatives

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Solar irradiance scaling | Irradiance equals luminosity over 4 pi d squared; with L = 382.8e24 W (S6) and 1 AU = 149,597,870.7 km (S7) the 1 AU value is 1361.2 W/m2, against the published 1361.0 (S6). Values: Mars 586.2, belt 321 to 127, Jupiter 50.26, Saturn 14.85 W/m2 (section 5.3) | S6; S7; derived | Primary data; derived | Reproduces three published irradiance values (Earth, Mars, Jupiter) | High |
| Array performance, real systems | Juno: more than 60 m2, 18,698 cells, about 14 kW at Earth distance and 500 W at Jupiter, which is 17.1 percent and 16.6 percent of the incident power (derived). JUICE: 85 m2 array giving about 800 W (under 1 kW) at Jupiter end of life, 18.7 percent of incident (derived), after more than 25 percent radiation degradation over 4 years; the array also needs rotation and a drive to stay sun-pointed | S26; S21 sec. 3.1 to 3.2 | Primary | Two spacecraft give 17 to 19 percent as an end-to-end figure | High |
| Collector area per kilowatt (derived from the 17 percent figure) | 10 m2 per kW at Mars, 18 to 46 m2 at the belt edges (2.06 to 3.27 AU), 117 m2 at Jupiter, 396 m2 at Saturn (section 5.3) | derived | Derived (assumes the Juno-demonstrated 17 percent) | Juno array: 60 m2 gives 0.5 kW, so 120 m2 per kW, matching 117 | High at Jupiter; medium elsewhere (efficiency assumed constant; real cells lose efficiency at low light and low temperature, which is why S21 says "LILT") |
| Solar power at Saturn | Cassini used three radioisotope generators: 882 W at beginning of mission (search summary of a NASA page); NASA text says the Sun at Saturn is "nearly 90 times fainter" | S51 | Secondary summary of primary pages | Derived 396 m2 per kW at 17 percent | Medium |
| Radioisotope generator | MMRTG: about 110 W electrical at launch from about 2,000 W thermal (4.8 kg plutonium dioxide), mass 45 kg, beginning-of-life efficiency 6 percent, about 72 W at 17 years; derived 2.4 W per kg | S51 (search summary of NASA fact sheets) | Secondary summary of primary pages | Derived 5.5 percent efficiency agrees with 6 percent | Medium |
| Small fission power | KRUSTY test: 1.5 to 5.0 kW thermal, fuel temperature up to 880 C, 28 consecutive hours, Stirling converters about 90 W electrical each at about 35 percent component efficiency and about 25 percent system efficiency; Kilopower aims at 1 to 10 kWe; four units to power an outpost | S51 (search summaries of NASA TM and release) | Secondary summary of primary pages | Matches the S45 lineage (Kilopower to 40 kWe) | Medium |
| Large fission surface power | 40 kWe, 10 years: NASA requested under 6,000 kg; the deployable concept came to 10,046 kg with margin (about 251 kg per kWe, or about 4 W per kg), with waste heat 126.4 kW; shielding to hold a crew at 1 km to 5 rem per year | S45 (raw); S51 for the 6,000 kg request | Primary | Concept exceeded the mass goal (S45 says so) | High |
| Radioisotope fuel supply limits | Not found. Only per-unit fuel mass (4.8 kg PuO2 per MMRTG, 2,000 W thermal) is documented here | S51 | Secondary | None | Gap: see Open threads |

### 3F. Interstellar-precursor constraints (brief, published concept studies only)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Current-technology interstellar speed | Voyager 1, launched 1977, left the Solar System after 37 years at 17 km/s, less than 0.006 percent of light speed; at current propulsion the nearest stars take "100 millennia" | S49 abstract (raw) | Primary (preprint) | 17 km/s over c is 5.7e-5, matching "under 0.006 percent" | High |
| Kinetic energy law | KE equals rest mass times (gamma minus 1) times c squared; at 0.3 c the kinetic energy is about 1 megaton of TNT per kg; derived 1.04 Mt per kg using the 4.184e15 J per megaton convention, which I did not source | S49 sec. 2.8 (raw) | Primary | Derived 1.037 Mt per kg | High |
| Directed-energy concept | A 50 to 70 GW array ("DE-STAR 4") pushing a gram-scale wafer with a 1 m sail to about 26 percent of light speed in about 10 minutes, reaching Alpha Centauri in about 20 years; the same driver for 100 kg gives about 1 percent of light speed | S49 abstract and sec. 1 (raw) | Primary (concept) | None | Low as a design basis; the energy figure is from the paper |
| Fusion-pulse starship concept | Project Daedalus (British Interplanetary Society, 1973 to 1978): 12 percent of light speed, 50 years to a star 5.9 light years away, 54,000 t total, 50,000 t propellant, 250 pellets per second, first-stage exhaust about 10,600 km/s | S52 (Wikipedia; original report not opened) | Secondary | S46's 125 AU case gives a smaller interstellar-precursor point of 244 km/s in 10 years | Low (secondary only) |
| Light delay for a precursor | 125 AU is 17.3 hours one way (derived at 499.0 s per AU) | derived from S7 | Derived | None | High |


## 4. CONFLICTS

Each item shows both values and the likeliest reason. None is resolved by picking a winner unless stated.

1. **Belt total mass.** 2.1e21 kg (Dawn-based, S10), 2.3e21 (S5), 2.39e21 (S9, from the ephemeris fit of Pitjeva and Pitjev 2018), 2.7e21 (S12, sum of its classes including the outer zones), 3.0e21 (Kuchynka and Folkner, cited in S12). Likely reasons: different epochs and ephemeris fits; whether Hungaria, Cybele, Hilda and Trojan objects are counted; Ceres' measured mass entering the fit only after Dawn. Use "about 2 to 3 e21 kg".
2. **Ceres' share of the belt.** 39 percent (derived from Dawn's 939.3e18 kg over S9's 2.39e21), 31 to 35 percent (S12, larger total), 25 percent (S17, an older NASA outreach statement). Likely reason: S17 predates the Dawn mass and uses an older total mass. Use 39 percent with the stated total.
3. **Belt mass relative to the Moon.** "About 3 percent" (S52), "3 to 4 percent" (S10), derived 3.25 percent (S9). Likely reason: rounding and the 2.1 to 2.7e21 range in item 1.
4. **Spacing between asteroids.** S10: "a few e5 km" for objects over 1 km. S11 and S52: "about 965,600 km" (600,000 miles). My derivation from S10's own counts (0.7 to 1.9 million) and volume (a few e25 km3): 3 to 4.6 million km if uniformly spread. The 3e5 km spacing would need about 2e9 objects and the 965,600 km figure about 7e7 to 2e8 objects in the stated volumes. I cannot tell which definition each source used (nearest neighbor, mean spacing, a smaller size threshold). The qualitative result agrees in every source: the belt is almost entirely empty space.
5. **Belt volume.** A few e25 km3 (S10) versus 2e26 km3 (S11). My derivation for a 2.1 to 3.2 AU annulus 1 AU thick gives 6.1e25 km3, supporting S10. S11 probably assumes a thicker belt.
6. **M-type share.** 3.3 percent of belt mass (S12) versus "about 10 percent of the belt" in popular summaries (secondary). Likely reasons: mass versus number, and the M class is degenerate with other X-types (S12 says so).
7. **Psyche's density.** 4.172 plus or minus 0.145 g/cm3 (S8, 2024 mass), 3,400 to 4,100 kg/m3 (NASA outreach as summarized in search), 3.9 g/cm3 (older, secondary). Likely reason: successive mass and volume determinations. Use S8.
8. **Saturn's mean distance in AU.** The summary of S2 printed 9.537 AU, but 1,432.041e6 km divided by 149.5979e6 km is 9.573 AU. I used the km figure. Probably a transcription error in the summary; the raw page was not seen.
9. **Enceladus' surface gravity.** The summary of S4 printed about 0.027 m/s2 with escape speed 0.24 km/s. Those two are inconsistent (escape speed squared over twice the radius gives 0.11 m/s2) and the mass and radii give 0.1135 m/s2. I rejected the 0.027 and used the derived value.
10. **Europa's surface dose units.** One secondary summary gave "2.3 Mrad or 540 rem per day". 540 rem is 5.4 Sv, which is about 540 rad for electron and gamma radiation; 2.3 Mrad is about 4,000 times larger. The two cannot both be per day at the same depth. 2.3 Mrad is more likely an accumulated or depth-specific figure from the lander study. I used only "about 5.4 Sv per day", flagged low confidence, and did not use 2.3 Mrad per day.
11. **Dose ratio between Europa and Callisto.** 5.4 Sv per day over 0.1 mSv per day is a ratio of 54,000; the Galileo energy-flux ratio in S24 is 250 to 400 and a secondary source says "300 times". Likely reason: the energy flux is dominated by keV to MeV particles that stop in the first millimeters, while the human dose is set by penetrating MeV electrons and their X-rays, which fall off faster with distance from Jupiter. Both statements can be true; do not mix them.
12. **Share of JUICE's lifetime dose from Europa.** "About a third" from two Europa flybys (ESA page) versus "about 25 percent" (a search summary of an ESA document). I did not open the underlying document for the 25 percent.
13. **Juno vault mass.** "Almost 400 pounds (172 kg)" (S25) versus "about 200 kg" including more than 20 electronics assemblies (a trade article seen only in a search summary). Likely definition: empty vault versus loaded vault.
14. **Hohmann delta-v to the belt.** 11.7 km/s and 1.4 years (S19) versus 8.75 to 12.28 km/s and 0.95 to 1.56 years (derived for 2.06 to 3.27 AU). The slide's value corresponds to about 2.9 AU; it does not say which radius it used.
15. **Direct Fusion Drive thrust.** S46 Table 19 lists 4 to 5 N at 1 MW with jet power 0.46 MW and 8,000 to 8,500 s. Thrust from jet power is 2 times power over exhaust speed, which gives 11.0 to 11.7 N. At 10 MW the same formula gives 95 to 115 N against 35 to 55 N listed. A factor of 2 to 3 within the report; the report's mission table uses an exhaust speed of 80 km/s. I used the table values as "what the study claims" and did not correct them.
16. **Radiator areal mass in S46.** 4.2 kg/m2 in the nominal parameter table and 2.1 kg/m2 in a figure label. Unreconciled.
17. **Irradiance at Jupiter in words.** "25 times less" (S26, rounded), "27 times lower" (S21), derived 1 over 27.1 from 1361.0 and 50.26. No real conflict; rounding.

## 5. DERIVED FIGURES

Constants (all from S50 and S7 unless stated): c = 299,792.458 km/s; 1 AU = 149,597,870.7 km; Sun GM = 1.32712440041e11 km3/s2; G = 6.67430e-11 m3/kg/s2; sigma = 5.670374419e-8 W/m2/K4; standard gravity 9.80665 m/s2; 1 eV = 1.602176634e-19 J; Earth GM 398,600.4355 km3/s2; Jupiter system GM 126,712,764.1; Saturn system GM 37,940,584.84. Orbits are treated as circular and coplanar with the fact-sheet semi-major axes. Computations were run in Python in the scratchpad; the inputs are the figures cited above.

### 5.1 Belt volume and object spacing (uniform-spread idealization)

- Volume V = pi (b squared minus a squared) t, with a = 2.1 AU, b = 3.2 AU, t = 1 AU (S10's stated extent): pi times (10.24 minus 4.41) = 18.3 AU3, times 3.348e24 km3 per AU3 = 6.13e25 km3. For 2.06 to 3.27 AU and t = 1 AU: 6.78e25 km3; for t = 0.5 AU: 3.39e25.
- Mean spacing d = (V over N) to the one third. For V = 6.13e25 km3: N = 7e5 gives 4.4e6 km; N = 1e6 gives 3.9e6 km; N = 1.9e6 gives 3.2e6 km; N = 1e4 (objects over 10 km) gives 1.8e7 km. For t = 0.5 AU and N = 1e6 the spacing is 3.2e6 km.
- Objects needed for a given spacing in 6.13e25 km3: 3e5 km needs 2.3e9; 965,600 km needs 6.8e7 (2.2e8 using S11's 2e26 km3).
- Caveat: real asteroids are concentrated toward the ecliptic and the mid-belt, so local densities can be several times the mean; the order of magnitude (millions of km between objects of 1 km or more) is not changed by that. Small objects below 1 km are far more numerous and not counted here.

### 5.2 Surface gravity and escape speed

Formulas: g = GM over R squared; escape speed = square root of (2 GM over R); R = half the mean diameter in S8; equatorial centrifugal acceleration = (2 pi over P) squared times R. Spherical approximation (Eros and Ida are very elongated, so local values vary by several times).

| Body | R (km) | g (m/s2) | Percent of standard gravity | Escape speed (m/s) | Centrifugal at equator over g |
|---|---|---|---|---|---|
| Ceres | 469.7 | 0.2839 | 2.9 | 516 | 0.06 |
| Vesta | 261.4 | 0.2530 | 2.6 | 364 | 0.11 |
| Pallas | 256.5 | 0.2072 | 2.1 | 326 | 0.06 |
| Hygiea (GM poor) | 203.6 | 0.169 | 1.7 | 262 | 0.02 |
| Psyche | 111.0 | 0.1299 | 1.3 | 170 | 0.15 |
| Eros (mean) | 8.42 | 0.0063 | 0.06 | 10.3 | 0.15 |
| Ida | 16.0 | 0.0107 | 0.11 | 18.5 | 0.21 |
| Mathilde | 26.4 | 0.0099 | 0.10 | 22.9 | about 0 |
| Generic 1 km rubble body, 2,000 kg/m3 | 0.5 | 2.8e-4 | 0.003 | 0.53 | n/a |
| Generic 10 km body | 5 | 2.8e-3 | 0.03 | 5.3 | n/a |
| Generic 100 km body | 50 | 2.8e-2 | 0.29 | 52.9 | n/a |
| Enceladus (mass 1.08e20 kg, mean R 252 km) | 252 | 0.1135 | 1.2 | 239 | n/a |
| Titan (S4 mass, R 2,575 km) | 2,575 | 1.354 | 13.8 | 2,641 | n/a |
| Io, Europa, Ganymede, Callisto (S3 mass and diameter) | 1,821; 1,561; 2,631; 2,411 | 1.796; 1.315; 1.429; 1.236 | 18.3; 13.4; 14.6; 12.6 | 2,558; 2,026; 2,742; 2,441 | n/a |

Spin-limit check: critical period 3.3 h over the square root of density in g/cm3 gives 2.24 h for Ceres (density 2.162, actual 9.07 h) and 2.02 h for Eros. Small bodies spinning near the barrier have surface speeds close to their escape speed (Eros circular speed at the surface 7.3 m/s).

### 5.3 Irradiance, equilibrium temperature and collector area

Irradiance S = 1361.0 W/m2 over d squared (d in AU). Equilibrium temperature for a rapidly rotating gray sphere with albedo 0 and emissivity 1: T = (S over 4 sigma) to the one fourth. Subsolar black plate facing the Sun: T = (S over sigma) to the one fourth. Collector area per kilowatt = 1,000 W over (S times efficiency) with efficiency 0.17 (the end-to-end figure Juno achieved: 14 kW over 60 m2 at 1 AU is 17.1 percent, 500 W over 60 m2 at 50.26 W/m2 is 16.6 percent; because Juno's area is "more than 60 m2" these are upper bounds).

| Location | d (AU) | S (W/m2) | Fraction of Earth | T sphere (K) | T subsolar (K) | m2 per kW at 17 percent |
|---|---|---|---|---|---|---|
| Mars | 1.524 | 586.1 | 0.431 | 225.5 | 318.9 | 10.0 |
| Belt inner edge | 2.06 | 320.7 | 0.236 | 193.9 | 274.2 | 18.3 |
| Belt middle | 2.50 | 217.8 | 0.160 | 176.0 | 248.9 | 27.0 |
| Ceres' distance | 2.76 | 178.6 | 0.131 | 167.5 | 236.9 | 32.9 |
| Belt outer edge | 3.27 | 127.3 | 0.0935 | 153.9 | 217.7 | 46.2 |
| Jupiter (mean) | 5.204 | 50.26 | 0.0369 | 122.0 | 172.5 | 117 |
| Saturn (mean) | 9.573 | 14.85 | 0.0109 | 90.0 | 127.2 | 396 |

Perihelion and aphelion irradiance: Mars 713 and 490 W/m2; Jupiter 55.5 and 45.7; Saturn 16.5 and 13.4. Checks: derived Mars 586.15 (published 586.2) and Jupiter 50.26 (published 50.26); L over 4 pi AU squared gives 1361.17 W/m2 against 1361.0. An albedo A lowers sphere temperature by the factor (1 minus A) to the one fourth; for Ceres (A = 0.09, S8) that is 2.3 percent.

### 5.4 Heliocentric Hohmann transfers (circular, coplanar)

Vis-viva: departure excess = |v_perihelion of transfer minus v_circular(origin)|; arrival excess = |v_circular(destination) minus v_aphelion of transfer|; time = pi times the square root of (a_t cubed over GM_Sun), a_t = (r1 + r2) over 2. "Sum" is the total heliocentric speed change, excluding departure from or capture into a planetary orbit.

| From Earth (r = 149.598e6 km) to | Departure excess (km/s) | Arrival excess (km/s) | Sum (km/s) | Time (d) | Time (years) | Delta-v from a 300 km Earth orbit (km/s) |
|---|---|---|---|---|---|---|
| Mars | 2.945 | 2.649 | 5.594 | 258.9 | 0.71 | 3.59 |
| Belt 2.06 AU | 4.776 | 3.975 | 8.751 | 345.6 | 0.95 | 4.20 |
| Belt 2.5 AU | 5.815 | 4.598 | 10.412 | 422.8 | 1.16 | 4.65 |
| Ceres' distance | 6.321 | 4.861 | 11.182 | 472.6 | 1.29 | 4.90 |
| Belt 3.27 AU | 7.076 | 5.198 | 12.275 | 569.7 | 1.56 | 5.29 |
| Jupiter | 8.793 | 5.643 | 14.437 | 997.7 | 2.73 | 6.30 |
| Saturn | 10.296 | 5.440 | 15.735 | 2,219.7 | 6.08 | 7.29 |

The last column assumes departure from a circular orbit of radius 6,371 + 300 km: delta-v = sqrt(v_inf squared + 2 GM/r) minus sqrt(GM/r), where the 300 km altitude is my assumption (circular speed there is 7.73 km/s). S19's table (5.56, 11.7, 14.4, 15.7 km/s; 0.71, 1.4, 2.7, 6.0 years for Mars, belt, Jupiter, Saturn) matches to 0.1 km/s except the belt (see Conflicts).

| From Mars orbit (r = 227.956e6 km) to | Departure excess (km/s) | Arrival excess (km/s) | Sum (km/s) | Time (years) |
|---|---|---|---|---|
| Belt 2.06 AU | 1.742 | 1.615 | 3.357 | 1.20 |
| Belt 2.5 AU | 2.768 | 2.444 | 5.212 | 1.43 |
| Ceres' distance | 3.279 | 2.819 | 6.098 | 1.57 |
| Belt 3.27 AU | 4.054 | 3.338 | 7.392 | 1.86 |
| Jupiter | 5.882 | 4.269 | 10.151 | 3.08 |
| Saturn | 7.565 | 4.582 | 12.147 | 6.53 |

Jupiter orbit to Saturn orbit: 1.805 plus 1.547 = 3.353 km/s, 10.04 years.

Capture into a circular orbit with periapsis at a given radius (one burn): delta-v = sqrt(v_inf squared + 2 GM/r) minus sqrt(GM/r). With the Earth-Jupiter arrival excess of 5.643 km/s: radius of Io's orbit 7.82 km/s (circular speed 17.33 km/s), Europa's 6.50, Ganymede's 5.51, Callisto's 4.70 (circular speed 8.20, period 16.7 days), 10 Jupiter radii 6.34, 1.5 Jupiter radii 14.57 (circular speed 34.4 km/s, period 5.4 h). Saturn with arrival excess 5.440 km/s: Enceladus' orbit radius 6.04 km/s, Titan's 4.00 km/s (circular speed 5.57 km/s), 10 Saturn radii 4.54 km/s. For comparison JUICE's actual capture into a long resonant orbit cost about 900 m/s and Cassini's 626 m/s; one-burn capture into a circular orbit is the expensive extreme.

### 5.5 Light delay

Light time over 1 AU = 149,597,870.7 km over 299,792.458 km/s = 499.00 s. One way to Mars 3.0 to 22.3 minutes (54.6e6 to 401.4e6 km, S6). Belt 8.8 minutes (1.06 AU) to 35.5 minutes (4.27 AU). Jupiter 32.7 to 53.8 minutes (588.5e6 to 968.5e6 km, S1); round trip 65 to 108 minutes. Saturn 67.0 to 92.2 minutes (1,205.5e6 to 1,658.6e6 km, S2); round trip 134 to 184 minutes. A target at 125 AU: 17.3 hours one way.

### 5.6 Orbits and tides in the giant planet systems

- Moon orbit radii in planet radii: Io 5.90, Europa 9.39, Ganymede 14.97, Callisto 26.34 Jupiter radii (71,492 km); Enceladus 3.95, Titan 20.27 Saturn radii (60,268 km). Orbital speeds (circular, from GM): Io 17.33, Europa 13.74, Ganymede 10.88, Callisto 8.20 km/s; periods 42.5 h, 85.2 h, 171.6 h, 400.6 h; circular speed at 1.1 Jupiter radii 40.1 km/s.
- Synchronous orbit radius (period equals rotation period) from the fact-sheet rotation periods: Jupiter 160,020 km = 2.24 radii (inside the synchrotron belt layer of 1.1 to 3 radii, S20); Saturn 112,248 km = 1.86 radii.
- Tidal acceleration difference across a rigid structure of length L at orbital radius r around a planet of GM: about 2 GM L over r cubed. For Jupiter at Io's orbit: 3.4e-7 m/s2 per 100 m, 3.4e-6 per km, 3.4e-5 per 10 km; at Europa 8.4e-8 per 100 m; at Ganymede 2.1e-8; at Callisto 3.8e-9. Compare Io's own surface gravity 1.80 m/s2: tides matter for very long structures and for the moons' interiors, not for ordinary structures.

### 5.7 Galactic cosmic ray dose accrual during transit

At 1.8 mSv per day (S40, inside MSL's hull, taken as constant) against the 600 mSv career limit (S41, reached after 333 days): Earth to Mars Hohmann (258.9 days) 0.47 Sv or 78 percent of the limit; Earth to belt 345.6 to 569.7 days 0.62 to 1.03 Sv (104 to 171 percent); Earth to Ceres' distance 472.6 days 0.85 Sv; Earth to Jupiter 997.7 days 1.80 Sv (3.0 times the limit); Earth to Saturn 2,219.7 days 4.0 Sv (6.7 times). A linear 3 percent per AU gradient would add about 3 to 7 percent at the belt, 13 percent at Jupiter and 26 percent at Saturn at the destination (S52 gradient, extrapolated; ignores solar-cycle variation and the shielding used). With the lower 0.5 mSv per day figure (S41, surface-mission environment) the limit is reached after 1,200 days. These are dose-rate scalings of one measured rate, not a radiation-transport result.

### 5.8 Propulsion relations

Exhaust speed v_e = Isp times 9.80665 m/s2; jet power = F v_e over 2, so thrust per megawatt of jet power = 2 MW over v_e.

| Option | Isp (s) | v_e (km/s) | v_e squared over 2 (MJ per kg of exhaust) | Thrust per MW jet power (N) |
|---|---|---|---|---|
| Chemical LH2 and LOX | 452.3 | 4.44 | 9.8 | 451 |
| Nuclear thermal (NERVA class) | 850 | 8.34 | 34.7 | 240 |
| NSTAR maximum | 3,100 | 30.4 | 462 | 66 |
| NEXT maximum | 4,220 | 41.4 | 856 | 48 |
| VX-200 | 5,000 | 49.0 | 1,202 | 40.8 |
| Direct Fusion Drive 1 MW class | 8,000 | 78.5 | 3,077 | 25.5 |
| Direct Fusion Drive 10 MW class | 12,000 | 117.7 | 6,924 | 17.0 |

Checks: VX-200 jet power 5.7 N times 49.03 km/s over 2 = 139.7 kW, which is 69.9 percent of 200 kW (reported 72 percent). NSTAR at 92 mN and 3,100 s: 1.40 kW jet power, 60.8 percent of 2.3 kW; at 19 mN and 1,900 s it is 35.4 percent of 0.5 kW. DFD: see Conflicts item 15.

### 5.9 Io heat flux check

100 TW (secondary news figure) over the surface area 4 pi R squared with R = 1,821.3 km (S37 Table 1, Io) = 100e12 W over 4.169e13 m2 = 2.40 W/m2, inside the quoted 1 to 3 W/m2 range. Io's radius is also consistent with S3's 3,643 km diameter.

### 5.10 Solar sail force

Radiation pressure = S over c = 1361.0 over 299,792,458 = 4.540e-6 N/m2 absorbing, 9.080e-6 N/m2 for an ideal reflector at normal incidence. Ideal-reflector pressure and the area needed for 1 N: 1 AU 9.08 micropascals and 110,137 m2; 2.5 AU 1.45 and 688,355 m2; 5.2 AU 0.335 and 2.98e6 m2; 9.57 AU 0.099 and 1.01e7 m2. An 86 m2 sail at 1 AU gives at most 0.78 mN, 0.029 mN at Jupiter's distance.

### 5.11 Radiator sizing

Per side, emissivity eps, temperature T: q = eps sigma T to the fourth. 300 K, eps 0.85: 390 W/m2; 300 K, 0.95: 436; 400 K, 0.85: 1,234; 400 K, 0.95: 1,379; 500 K, 0.9: 3,190; 800 K, 0.9: 20,900. One-sided area per megawatt rejected: 2,561 m2 at 300 K (0.85), 810 m2 at 400 K (0.85), 314 m2 at 500 K (0.9), 48 m2 at 800 K (0.9), assuming a sink at 0 K (deep space; sunlight or a warm planet raises the load). Published case S45: 126,400 W over 133.4 m2 = 947 W/m2 of quoted area, against 1,160 W/m2 per side from eps 0.84 at 395 K (the difference includes the view to a warm lunar surface and the 45-degree sun case). Specific mass of S45's 40 kWe system: 10,046 kg over 40 kWe = 251 kg per kWe (3.98 W per kg), versus S46's 1,345 kg for a 1 MW fusion core (0.74 kW of fusion power per kg; the report lists 0.75), and 2.4 W per kg for an MMRTG (110 W over 45 kg).

### 5.12 Rocket equation, impulsive

Mass ratio = exp(delta-v over v_e); propellant fraction = 1 minus 1 over mass ratio. From a 300 km Earth orbit, delta-v 3.59 km/s (to Mars transfer): chemical 55.5 percent, nuclear thermal 35.0, NSTAR 11.1, VX-200 7.1, DFD 4.5. Delta-v 11.0 km/s (Jupiter transfer plus capture at Callisto's orbit radius): chemical 91.6 percent (mass ratio 11.9), nuclear thermal 73.3 (3.74), NSTAR 30.4 (1.44), VX-200 20.1 (1.25), DFD at 8,000 s 13.1 (1.15). Delta-v 11.3 km/s (Saturn transfer plus capture at Titan's orbit radius): 92.2, 74.2, 31.0, 20.6, 13.4 percent. Low-thrust spiral escape and capture add to these delta-v values.

### 5.13 Other ratios

Titan atmospheric column: 1.5e5 Pa over 1.35 m/s2 = 1.11e5 kg/m2 = 11,100 g/cm2; Earth 1.01e5 Pa over 9.81 m/s2 = 1,030 g/cm2; ratio 10.8 (inputs from S37 Table 1). Saturn's rings over the belt: 1.54e19 over 2.39e21 = 0.64 percent; over Ceres 1.6 percent. Belt over Moon 2.39e21 over 7.346e22 = 3.25 percent; top four over total 1.49e21 over 2.39e21 = 62.3 percent. Europa energy flux in power units: 5e10 to 8e10 keV per cm2 per second times 1.602e-16 J per keV times 1e4 cm2 per m2 = 0.080 to 0.128 W/m2; Callisto 3.2e-4 W/m2; Io 1.6e-3; Ganymede 3.2e-4 (equator) and 8.0e-3 (poles).

## 6. CONSTRAINTS FOR ANY INHABITANT

Whoever builds or occupies a works, outpost or orbital installation in these regions meets the following. Each item cites the finding it rests on (section 3 table, or section 5 derivation). Where a human-shaped machine is affected, the constraint is stated in general terms: a machine body has mass, waste heat, electric charge and joints, and obeys the same physics.

**Asteroid Belt**

- The belt is a very large, nearly empty volume. Objects of 1 km or more are millions of kilometers apart (3A spacing rows, 5.1) and probes pass through without maneuvering (3A, S10). The difficulty of the belt is distance, transfer time and delta-v, not collisions with other bodies.
- Transfer cost sets supply: 0.95 to 1.56 years and 8.8 to 12.3 km/s heliocentric from Earth's orbit, plus 4.2 to 5.3 km/s to leave a 300 km Earth orbit; from Mars' orbit 1.2 to 1.9 years and 3.4 to 7.4 km/s (3A delta-v row, 5.4). Every kilogram arrives with propellant penalties that grow with the exhaust speed gap (5.12).
- Light delay of 9 to 36 minutes one way (3A, 5.5) rules out real-time remote operation from Earth or Mars; local work needs autonomy or accepted lag.
- Light is 24 percent (2.06 AU) to 9 percent (3.27 AU) of Earth's (3A, 5.3): about 18 to 46 m2 of collector per kilowatt at the 17 percent end-to-end efficiency real arrays have reached (3E). Equilibrium temperatures of a body are about 154 to 194 K; a warm machine or habitat must be insulated against a cold background and must shed its waste heat only by radiation (5.11).
- Surface gravity is tiny: 0.28 m/s2 on Ceres, 0.13 on Psyche, about 0.006 to 0.01 on bodies of 10 to 50 km, about 3e-4 on a 1 km body (5.2). Escape speeds range from 0.5 m/s (1 km) through 10 m/s (Eros) to 516 m/s (Ceres). Anything moved faster than the escape speed leaves for good: a joint-driven body can push itself off the surface, cannot fly by flapping, and needs anchoring and traction aids because its weight is almost nothing. Tools, spoil and thruster plumes are lost to space on small bodies.
- Rapidly rotating small bodies are near the spin barrier (rotation periods mostly 2.2 to 20 hours; critical period near 2.1 h at 2.5 g/cm3, 3A rotation rows); centrifugal acceleration reaches 15 to 21 percent of gravity at the equator of small bodies (5.2), and rubble-pile structure is expected for bodies above about 0.15 km. Surface thermal cycling follows the same few-hour rotation periods (Ceres 9.07 h, Vesta 5.34 h, Psyche 4.20 h).
- Resources are not uniform: C-type material is about half the mass of the population (52.5 percent) while S-types are 8.4 percent and M-types 3.3 percent (3A composition row). Hydrated carbonaceous meteorites hold about 9 to 20 wt percent water, but the surfaces of C-complex asteroids average about 4.5 wt percent with a 0 to 11.5 range (3A water row), and the water is bound in minerals that release it at several hundred degrees Celsius (dehydroxylation between 400 and 770 C, S14). Metal-rich bodies exist (Psyche 30 to 60 percent metal by volume) but are a few percent of the belt's mass.
- Galactic cosmic rays dominate the radiation at belt distances (3A radiation row). Hull thickness barely reduces their dose (3D, S40); transit time sets the dose (5.7): the 600 mSv career limit is reached after about 333 days at the measured cruise rate.

**Jupiter and the Galilean moons**

- The inner magnetosphere is the most severe radiation environment in the Solar System (S20). The belts' core lies inside Io's orbit (5.9 Jupiter radii); Galileo took 30 to 40 krad per crossing behind about 0.8 cm of aluminum equivalent (3B). Any installation between the planet and Europa's orbit (9.4 radii) must be built for tens to hundreds of megarad external dose; electronics are the limiting item (design values 50 krad per box for JUICE, 150 krad design and 300 krad parts for Clipper), typically met with centimeter-scale metal vaults (Juno: 1 cm titanium, factor about 800, 172 kg; Lander study: about 8.5 mm aluminum, about 72 kg) (3B).
- Surface dose differs sharply by moon: energy flux at Europa 5e10 to 8e10 keV per cm2 per s (0.08 to 0.13 W/m2) versus 2e8 at Callisto and at Ganymede's equator and 5e9 at Ganymede's polar caps; unshielded exposure at Europa is described as lethal to humans within hours (3B). Callisto (26.3 radii) is the published candidate for a low-dose base; its surface dose is quoted at about 0.01 rem per day (low confidence) (3B).
- Arrays degrade in the belts: more than 25 percent loss over 4 years for JUICE's array (3B, 3E). Power at Jupiter is 3.7 percent of Earth's (50.26 W/m2): about 117 m2 per kilowatt at 17 percent, or about 120 m2 per kilowatt as flown by Juno. Large loads need nuclear power; the published surface-fission concept is about 251 kg per kWe (3E, 5.11).
- Light delay of 33 to 54 minutes one way (5.5) means supervised autonomy, not remote control, for any works.
- Transfers cost 2.7 years and 14.4 km/s heliocentric from Earth's orbit (about 3.1 years and 10.2 km/s from Mars' orbit); arriving at 5.6 km/s relative to Jupiter means 4.7 km/s of capture to a circular orbit at Callisto's radius in one burn, 5.5 km/s at Ganymede's, 6.5 at Europa's and 7.8 at Io's (5.4). Gravity assists and long elliptical captures cut this (JUICE: about 900 m/s, total mission 2.6 km/s) at the price of time.
- Jupiter's well is deep: escape speed from Callisto's orbit radius is 11.6 km/s, from Io's 24.5 km/s (3B bulk and 5.4); the moons' own escape speeds are 2.0 to 2.7 km/s (3B).
- Near Io, a dense cold sulfur and oxygen plasma (above 3,000 per cm3 at 5.6 to 6 radii) and about 1 ton per second of ionized gas fill the region out to Europa's orbit (3B). Surface charging and plasma interaction were not quantified in my sources.
- Tidal forces over structure scales are negligible (3.4e-7 m/s2 across 100 m at Io's orbit, 5.6); tides matter for the moons' heating (Io 1 to 3 W/m2; Europa and Ganymede interior oceans).
- Moon gravity is 12 to 18 percent of standard (1.24 to 1.80 m/s2), and surface temperatures are about 90 to 160 K (3B).

**Saturn, its rings and moons**

- Sunlight is about 1.1 percent of Earth's (14.85 W/m2): about 396 m2 per kilowatt at 17 percent, so power must be nuclear for any substantial load (Cassini flew three radioisotope generators; 3C, 3E).
- Light delay of 67 to 92 minutes one way (134 to 184 round trip) (5.5). Transfers: 6.1 years and 15.7 km/s from Earth's orbit (Cassini: about 6.7 years with gravity assists), 4.0 km/s to capture to a circular orbit at Titan's radius, 10.0 years and 3.35 km/s from Jupiter's orbit (3C, 5.4).
- Saturn's radiation belts are bounded by rings and moons and are described as much weaker than Jupiter's, with MeV electrons measurable only to about 7 radii and an ion belt that ends at Tethys' orbit (4.9 radii) (3C radiation row); no common-unit dose comparison was found, so treat the lower flux as a qualitative statement only.
- The rings are about 1.54e19 kg of mostly water ice in a layer about 10 m thick, particle sizes from sand to mountain; Enceladus vents about 200 kg/s of water (low confidence) with escape speed 0.24 km/s and gravity 0.11 m/s2 (3C, 5.2). Water ice is available in orbit without a gravity well; the cold (ring temperatures down to -230 C) and the fine, high-surface-area particles are the working conditions.
- Titan has a 1.5 bar nitrogen atmosphere at 94 K with 10.8 times Earth's overhead mass (3C, 5.13). That atmosphere stops trapped particles, leaving cosmic rays as the main source at the surface; surface liquids are hydrocarbons; surface winds are under 1 m/s. Materials and machines must work at 94 K in a dense cold gas; heat retention rather than heat rejection is likely to be the thermal problem (my inference from the 94 K ambient; no number found).

**Deep transit**

- Cruise dose is about 1.8 mSv per day inside a spacecraft hull, shielding-insensitive for cosmic rays; a flat rate reaches the 600 mSv limit in 333 days and totals 1.8 Sv to Jupiter and 4.0 Sv to Saturn on a Hohmann trip (3D, 5.7). A solar particle storm shelter needs 10 cm (centennial event) to 20 cm (millennial event) of water-equivalent on top of a 20 g/cm2 aluminum vehicle (3D).
- Thrust and exhaust speed trade against power: 1 N at 80 km/s exhaust needs about 39 kW of jet power; 1 kN at that exhaust speed needs about 39 MW (5.8, derived). At the published fission surface-power mass (about 4 W/kg) a 1 MW electrical plant would be about 250 t (5.11). Chemical rockets need a 92 percent propellant fraction for the Jupiter or Saturn transfers from low Earth orbit; a nuclear thermal rocket at 850 s needs about 73 to 74 percent (3D, 5.12).
- Waste heat must be radiated: 390 to 436 W/m2 per side at 300 K, 1,234 to 1,379 W/m2 at 400 K (5.11). The published 40 kWe fission concept needs 126 kW of waste heat rejected and 134 m2 of radiator (3D). Any large power source is also a large radiator.

**Later-era interstellar flight (brief)**

- The energy cost of relativistic travel is set by the kinetic energy formula: about 1 megaton of TNT per kilogram at 0.3 c (3F). Current propulsion at 17 km/s takes on the order of 100,000 years to the nearest stars (3F). Light delay grows to 17 hours at 125 AU (5.5).

## 7. CANDIDATE HANDWAVES

Each item would require physics to be bent, or a technology not yet demonstrated. Flagged, not accepted. The developer decides.

1. **Fusion propulsion for fast interplanetary transit** (Mars in 110 days, Jupiter in 1.2 years, S46). The study itself calls D-3He fusion undemonstrated (present experiment about 0.1 T versus about 5 T needed) and puts a flight unit around 2040 "with sufficient support". It assumes 55 keV electron temperatures, 95 percent synchrotron wall reflection, a specific power of 0.75 to 1.25 kW per kg and radiator mass of 2 to 4 kg/m2 (3D). Treat any fusion-driven fast transit as a handwave unless the developer chooses to accept it.
2. **A specific power far above present fission systems.** The published 40 kWe fission concept is about 4 W/kg (251 kg per kWe) while the fusion concept claims about 750 to 1,250 W/kg; the gap is two to three orders of magnitude (3D, 5.11). Any large electrical or propulsion plant lighter than that is a handwave.
3. **High thrust and high exhaust speed at once** (for example hundreds of N at 80 km/s or more): needs tens of MW of jet power and the radiators to match (5.8, 5.11). The largest demonstrated electric thruster in these sources produced 5.7 N at 200 kW (3D).
4. **Crewed transits to Jupiter or Saturn within the dose limit without large shielding mass.** At the measured cruise rate a 2.7-year trip delivers about 1.8 Sv and a 6.1-year trip 4.0 Sv (5.7); no source here shows a way to cut galactic cosmic ray dose with moderate shielding (3D). Assuming it away is a handwave. (Machine electronics have their own limits: the parts ratings in these sources are 50 to 300 krad(Si); single-event effects are not addressed.)
5. **Habitats or works inside Europa's orbit without very heavy shielding or deliberate belt-avoiding orbits.** The published practice is to stay outside about 9 radii, or to cross quickly (3B). Long residence inside Io's orbit would be a handwave.
6. **Real-time communication across 33 to 92 minutes of light delay.** Needs a faster-than-light link; there is none (5.5).
7. **A dense, obstacle-filled belt that requires piloting through "fields" of rocks.** The published reality is millions of km between objects of 1 km or more (3A, 5.1). A dense belt would contradict the measured mass and counts.
8. **Solar power for large loads at Saturn.** Not a violation of physics, but about 396 m2 per kilowatt (5.3); if the developer wants "light" infrastructure there, nuclear power is the published route (3E).
9. **Ocean, ring and moon water used without any energy or thermal budget.** Extraction from hydrated minerals needs heating to hundreds of degrees (3A, S14); ice mining needs power; not a handwave by itself but easy to under-count.
10. **Interstellar travel at fractions of light speed with reaction mass or with onboard fuel.** The published concepts either use enormous external beam power (50 to 70 GW for a gram-scale craft, S49) or a 54,000 t fusion-pulse starship (S52, secondary). Anything faster, cheaper or with crews is a handwave.
11. **Robot body.** Only the gel brain is waved by the brief. The body still has to reject its heat by radiation in vacuum (about 400 W/m2 per side at 300 K), carry electronics inside a dose budget, and obey escape-speed limits on small bodies (5.2, 5.11).

## 8. OPEN THREADS

What I could not find, and what I would search next.

- **Europa surface dose from a primary source.** The 5.4 Sv per day figure rests on secondary summaries. Primary candidates not retrievable here: Paranicas et al. 2007 GRL (403 on Wiley), Paranicas et al. 2009 chapter in Europa (ResearchGate wall), the NASA Europa Lander Study 2016 report (PDF link not found). Next: try the NASA Technical Reports Server records for the Europa Lander Study and for Europa Clipper radiation design reports.
- **Callisto and Ganymede surface dose from a primary source** (the 0.01 rem per day figure is secondary, probably from the HOPE-era literature). Next: Cooper et al. 2001, Icarus 149:133 (read only an annual report, not the paper), and Ganymede's polar-cap dose from the same work.
- **Dose rate as a function of radial distance and shielding for Jupiter** in a single table (krad per day versus Jupiter radii behind 1 to 10 mm aluminum). Found only the Galileo per-crossing figure. Next: Fieseler et al. 2002 (IEEE Trans. Nucl. Sci. 49:2739), Becker et al. 2017 (Space Sci. Rev. 213:507), Divine and Garrett 1983, and the GIRE3 model description.
- **Juno measured dose and the Juno Radiation Monitoring results** (Becker et al. 2017). Springer and Wiley pages blocked.
- **JUICE "240 krad behind 10 mm of aluminum" and the 25 percent Europa share.** Seen only in search summaries; the underlying ESA document was not opened.
- **Saturn versus Jupiter radiation in common units.** Only qualitative statements (S22). Next: Kollmann et al. 2018 and Roussos et al. 2018 (cited in S22) for intensity numbers, and Cassini MIMI dose estimates for Titan and Enceladus orbits.
- **Titan surface radiation dose, hydrocarbon inventory and bedrock properties.** Gronoff et al. 2011 (NASA Langley copy: spaceradiation.larc.nasa.gov) not opened; Lorenz et al. 2008 hydrocarbon inventory not searched.
- **Enceladus plume flux, ocean depth and ice thickness from primary papers.** Only secondary summaries (Hansen et al., Thomas et al. 2016, Waite et al. 2017).
- **Io heat flow primary source** (Park et al. 2024, Nature, not opened) and the Io plasma torus numbers from the review (Bagenal and Dols 2020, paywalled).
- **Measured conditions inside the belt**: surface temperatures and radiation from Dawn at Ceres and Vesta (Dawn instrument papers), the Psyche mission's measurements when available; no measured dose in the belt found.
- **Debiased asteroid size-frequency distribution** (counts above 1 km, 100 m). Searched but only NEO-focused results and a preliminary preprint; next: Bottke et al. 2005 (Icarus), Gladman et al. 2009, and the NEOWISE debiased main-belt papers.
- **Spacing definition.** Which definition S10 and S11 use for "a few e5 km" and "965,600 km"; ask the Lucy team or find the original source of the 965,600 km figure.
- **Radioisotope fuel supply limits** (Pu-238 production rate, availability) and per-mission fuel inventory; not found. Next: NASA RPS program documents and National Academies reviews.
- **Propulsion benchmarks I did not retrieve:** NASA nuclear electric propulsion reference studies (specific mass, kg per kW), high-power Hall and magnetoplasmadynamic thrusters, and radiator technology roadmaps (areal mass per m2). Pages found but not read: NTRS 19910018902 (NTP symposium), 20120003776, 20150004421, Les Johnson's solar sail status (NTRS 20190030798), NASA Solar Cruiser (NTRS 20205002406).
- **Mars-orbit departure and Mars-based supply** for belt and Jupiter trips with real mission-design tools (porkchop, launch windows) instead of circular-coplanar Hohmann estimates; synodic periods were not derived.
- **Interstellar studies:** Project Daedalus' original report (JBIS 1978), Project Icarus papers, Breakthrough Starshot system model (Parkin 2018), and energy-per-kg estimates for slow (precursor-class, 0.001 to 0.01 c) missions. Daedalus numbers here are secondary.
- **Single-event effects and electronics tolerance for humanoid machine bodies** under cosmic-ray flux: not searched (outside the planetary-environment scope).

Pages found and not read (listed for a follow-up): arXiv 1312.4450 "How many ore-bearing asteroids?"; Lorenz 2008; arXiv 1209.3799 "Regolith grain sizes of Saturn's rings from Cassini CIRS"; arXiv 2604.01927 (Geant4-IcyMoons, 2026) and arXiv 2503.06971 (Europa near-surface ice, 2025), which may carry surface dose rates; NASA Juno vault image article; ESA RADEM; arXiv 2107.06795 (Mercury Lander concept study mentions electric propulsion); NASA OCHMO Rev E figures.

## 9. REJECTED SOURCES

- **Wikipedia (Asteroid belt, Project Daedalus):** used only for leads and clearly marked secondary where a figure appears; no number from it is used as a sole basis except the Daedalus parameters and the belt dust temperature range, both labeled low confidence.
- **Fandom wikis, forum posts and slideshare copies** (nasa.fandom.com Callisto, terraforming.fandom, newmars forum, nasaspaceflight forum, slideshare "Project HOPE"): not used, not authoritative. The Callisto 0.01 rem per day figure appears in them and in search summaries, so it is carried only as a low-confidence secondary value.
- **Popular summaries giving "2.3 Mrad per day" for Europa and "200 or 100 krad per day behind 2.2 or 5.0 g/cm2 at the core of the belts" and "Galileo 3 to 4 times design dose":** the first is internally inconsistent with 540 rem per day (Conflicts 10); the second and third appeared only in search summaries I could not trace to a raw page, so they are not used.
- **Search summary figure for Saturn's ring "95 percent water ice":** did not appear in any opened source; not used.
- **Search summary figure of "9.537 AU" for Saturn and "0.027 m/s2" for Enceladus gravity:** tool summary errors, rejected against the km figures and the mass and radius (Conflicts 8 and 9).
- **Numbers I typed into search queries from memory as hints** (log rows 16, 31, 72, 82, 85, 91, 92, 106, 107 and some others, for example the Hohmann, NERVA, Dawn, VX-200, Daedalus and Cassini RTG values): no figure was used because it appeared in my query. Every figure in the tables comes from a page I opened (raw text or a fetch summary, as marked). Where a hinted number came back confirmed by a source it is cited to that source (for example the VX-200 values are in the raw Bering et al. paper); where it did not come back (the Cuzzi 95 percent, the million-object count, a 633 W Cassini figure) it is not used.
- **ResearchGate stubs, Wiley and Springer pages that returned walls or redirects:** nothing taken from them except search-summary leads.
- **Mirror copy of the NASA HOPE slides (eltamiz.com):** used because the NTRS download failed, with the mirror status stated in the source key; the NTRS record number is 20030063128.
