# Space trucking and bulk transport infrastructure (physics and engineering data)

## Scope

Bulk cargo transport (tonnes to megatonnes per year) between source regions (near-Sun orbits at 0.1 to 0.5 AU, Mercury,
near-Earth and main-belt asteroids, the Moon, Venus's clouds, gas-giant atmospheres) and use regions (Earth orbit, Mars
orbit): delta-v, propulsion, throughput arithmetic, infrastructure, launch cost and cadence, cargo packaging, minimum fleets.

## SEARCH LOG

| # | Date | Search string (verbatim) or page opened | Result | Note |
|---|---|---|---|---|
| 1 | 2026-10-11 | Read-only: sibling files `belt_jupiter_saturn_and_deep_transit.md` (3D, 3E, 5.4), `moon_lagrange_and_comparables.md` (A6, B), `leo_and_orbital_habitats.md` (A4, D7, E, F), `gap_retry_leo_human_machines_power.md` (F, H, I), `mars_venus_and_transfer.md` (3.5, 3.6, 3.8 to 3.10) | useful (scope) | Used only to avoid repetition; no figure in this file is taken from them unless re-opened here. A grep with a wildcard briefly listed headings of `DEFERRED_RESEARCH.md`; nothing from it was read or used |
| 2 | 2026-10-11 | WebSearch: `NASA SP-428 Space Resources and Space Settlements 1979 mass driver asteroid retrieval delta-v` | useful | Led to the NSS-hosted SP-428 chapters |
| 3 | 2026-10-11 | Opened: NSS, SP-428 Part IV-2 "Retrieval of Asteroidal Materials", https://nss.org/settlement/nasa/spaceres/IV-2.html | useful | Read through the fetch tool's extraction (quotes); mass-driver retriever numbers |
| 4 | 2026-10-11 | WebSearch: `Jedicke 2018 delta-v requirements delivering water extracted from near-Earth objects to cis-lunar space` | useful (abstract only) | Paper paywalled (Planet. Space Sci. 2018); abstract numbers via two repository summaries |
| 5 | 2026-10-11 | Opened: Jedicke et al., "Earth's Minimoons", arXiv:1905.13457v1, 31 May 2019 (PDF, text extracted locally) | thin | Only a capture-delta-v statement; its "76 km s-1" for 2000 SG344 is an extraction or typesetting error (see Conflicts) |
| 6 | 2026-10-11 | WebSearch: `Palaszewski atmospheric mining outer solar system helium-3 Uranus aerospacecraft NASA Glenn` | useful | NTRS leads (20150006664, 20205004479, 20170004746) |
| 7 | 2026-10-11 | WebSearch: `arXiv Jedicke Sercel Gillis-Davis Morenz Gertsch "Availability and delta-v requirements" water near-Earth objects` | dead at the sources | No open full text; the arXiv link returned was the minimoons paper |
| 8 | 2026-10-11 | WebSearch: `Taylor McDowell Elvis 2018 "delta-v map of the known main belt asteroids" Acta Astronautica arXiv` | dead at the query | The search engine did not return the paper; returned Ieva 2014 and Elvis 2011 |
| 9 | 2026-10-11 | Opened: Ieva et al., arXiv:1406.5027 abstract (2014) | thin | Only a 10.5 km/s selection threshold and a 12.3 km/s "Solar System escape" comparison |
| 10 | 2026-10-11 | WebSearch: `NASA JPL NHATS near-Earth object human space flight accessible targets study delta-v 12 km/s criteria round trip` | useful | Led to CNEOS NHATS |
| 11 | 2026-10-11 | Opened: NASA JPL CNEOS, NHATS page, https://cneos.jpl.nasa.gov/nhats/ | useful | Delta-v definition and constraint menus |
| 12 | 2026-10-11 | Queried: NASA JPL SSD NHATS Data API v1.3, https://ssd-api.jpl.nasa.gov/nhats.api (default constraints; one call with a malformed `launch` value failed with code 400, dead at the query) | useful | 7,139 NHATS-compliant objects; tallied by minimum delta-v locally |
| 13 | 2026-10-11 | Opened: NSS, SP-428 index https://nss.org/settlement/nasa/spaceres/ | thin | Cover page only |
| 14 | 2026-10-11 | Downloaded: https://NSS.org/wp-content/uploads/2023/05/NASA-SP-428.pdf | dead at the sources | A one-page PDF, not the report |
| 15 | 2026-10-11 | WebSearch: `nss.org settlement nasa spaceres "Mass-Driver" reaction engine exhaust velocity Kolm Chilton O'Neill 1977 summer study` | useful | Led to SP-428 III-1 and III-3 |
| 16 | 2026-10-11 | WebSearch: `mass driver 1 MIT 1977 Kolm demonstration acceleration 33 g bucket test results` | thin | Wikipedia and newsletters only for test figures (secondary); not used for numbers |
| 17 | 2026-10-11 | Opened: SP-428 III-1 "Mass Drivers I: Electrical Design" (Chilton et al.), https://nss.org/settlement/nasa/spaceres/III-1.html | useful | Design envelope; model reached "tens of gravities" |
| 18 | 2026-10-11 | Opened: SP-428 III-3 "Mass Drivers III: Engineering" (Arnold et al.), https://nss.org/settlement/nasa/spaceres/III-3.html | useful | Lunar launcher point design (2,400 m/s, 125 MW, 650,000 t/yr) |
| 19 | 2026-10-11 | WebSearch: `BepiColombo transfer to Mercury solar electric propulsion delta-v flybys 7.2 years ESA mission design` | useful | Led to ESOC ISSFD paper |
| 20 | 2026-10-11 | WebSearch: `MESSENGER trajectory design delta-v total 2 km/s six planetary flybys Mercury orbit insertion McAdams NTRS` | useful | Led to APL Technical Digest paper |
| 21 | 2026-10-11 | Opened: McAdams et al., "Spacecraft Trajectory Planning and Execution for the MESSENGER Mission", JHU APL Tech. Digest 34(1), https://jhuapl.edu/sites/default/files/2024-09/34-01-McAdams.pdf | useful | ">2213 m/s of propulsive DV" |
| 22 | 2026-10-11 | Opened: Jehn and Schoenmaekers (ESA/ESOC), "BepiColombo trajectory options to Mercury in 2016 and 2017", ISSFD 24, 2014, https://issfd.org/ISSFD_2014/ISSFD24_Paper_S6-5_jehn.pdf | useful | Direct Hohmann about 16 km/s; SEP 4.254 km/s plus flybys; 7.5 years |
| 23 | 2026-10-11 | Opened: NASA NSSDC fact sheets: Mercury, Venus, Mars, Moon, planetary summary (all "Last Updated 11 January 2024"); JPL SSD astrodynamic parameters https://ssd.jpl.nasa.gov/astro_par.html | useful | Constants for derived delta-v |
| 24 | 2026-10-11 | WebSearch: `Gateway Power and Propulsion Element 60 kW solar electric propulsion AEPS 12 kW Hall thrusters xenon NASA` | useful | Led to Cassady et al. 2022 |
| 25 | 2026-10-11 | WebSearch: `highest power electric propulsion spacecraft ever flown kW Hall thruster flight record` | thin | A "20 kW krypton in orbit" claim came from a LinkedIn post; not used; X3 lead kept |
| 26 | 2026-10-11 | Opened: Cassady et al. (Aerojet Rocketdyne, NASA GRC), "Development of 12 kW Hall thrusters for NASA Lunar Gateway PPE", Space Propulsion 2022, NTRS 20220007037 | useful | AEPS performance table; SEP cargo-tug case to NRHO |
| 27 | 2026-10-11 | Opened: NTRS 20190004993, Hall et al., "High-Power Performance of a 100-kW Class Nested Hall Thruster", 2017 (abstract) | useful | X3: 102 kW, 5.4 N |
| 28 | 2026-10-11 | WebSearch: `Psyche spacecraft SPT-140 Hall thrusters 4.5 kW xenon 1085 kg solar arrays 21 kW NASA JPL` | thin | Search summary only for SPT-140 numbers |
| 29 | 2026-10-11 | Downloaded: https://theory.pppl.gov/news/Psyche%20talk%20Goebel.pdf | dead at the sources | Server returned an HTML page, not the PDF |
| 30 | 2026-10-11 | Opened: NASA JPL image page "Psyche's Hall thruster", 20 Sep 2021 | thin | Only "first to be used beyond lunar orbit"; no numbers |
| 31 | 2026-10-11 | WebSearch: `Dawn spacecraft ion propulsion total delta-v 11.49 km/s record NASA JPL xenon 425 kg` | useful | Led to Rayman and Garner |
| 32 | 2026-10-11 | Opened: NTRS 20210008613, Rayman and Garner, "In-Flight Operation of the Dawn Ion Propulsion System Through Completion of the Final Orbit Around Dwarf Planet Ceres", 2018 (abstract) | useful | 51,250 h, 416 kg Xe, almost 11.5 km/s |
| 33 | 2026-10-11 | WebSearch: `SpaceX Starlink V2 mini argon Hall thruster 170 mN 2500 s specific impulse 4.2 kW` | useful (secondary) | Trade press quoting SpaceX |
| 34 | 2026-10-11 | Opened: Satellite Today (R. Jewett), "SpaceX Shares Details of Higher Bandwidth V2 Mini Starlink Satellites", 27 Feb 2023 | thin | Confirms 170 mN and "never operated in space before"; the 2,500 s, 4.2 kW, 50% figures were not on this page |
| 35 | 2026-10-11 | WebSearch: `Jones "The Recent Large Reduction in Space Launch Cost" ICES-2018-81 cost per kg LEO historical dataset` | useful | Led to NTRS 20200001093 |
| 36 | 2026-10-11 | Opened: Jones (NASA Ames), "The Recent Large Reduction in Space Launch Cost", ICES-2018-81, NTRS 20200001093 (PDF, text extracted) | useful | Table A1 (36 vehicles) and A2 |
| 37 | 2026-10-11 | WebSearch: `CSIS Aerospace Security "Space Launch to Low Earth Orbit: How Much Does It Cost" cost per kilogram data` | useful | Led to CSIS and Our World in Data |
| 38 | 2026-10-11 | Opened: CSIS Aerospace Security Project, "Space Launch to Low Earth Orbit: How Much Does It Cost?", last updated 1 Sep 2022 | thin | Methodology only; values sit in an interactive chart |
| 39 | 2026-10-11 | Opened: Our World in Data grapher "Cost of space launches to low Earth orbit" (CSIS 2022 data, FY2021 dollars, updated 4 Mar 2025) and its CSV download | useful | Second dataset for the same quantity |
| 40 | 2026-10-11 | WebSearch: `SpaceX Starship payload to LEO 100-150 t reusable official specification Starship V3 2025 2026` | thin | Wikipedia and aggregators only |
| 41 | 2026-10-11 | Opened: https://www.spacex.com/vehicles/starship/ | dead at the sources | Page content not served to the fetch tool |
| 42 | 2026-10-11 | WebSearch: `SpaceX 2025 total Falcon 9 launches record year number of orbital launches mass to orbit` | useful (leads) | News only |
| 43 | 2026-10-11 | Opened: Space.com 2025 launch-record article | dead at the sources | Article body not served |
| 44 | 2026-10-11 | Opened: AIAA news item, 13 Nov 2025 | thin | Florida launch count only |
| 45 | 2026-10-11 | Opened: Jalopnik (N. Werner), 5 Jan 2026 | thin (secondary) | 165 Falcon 9, 320 world attempts; replaced by McDowell |
| 46 | 2026-10-11 | WebSearch: `Jonathan McDowell planet4589 2025 orbital launch statistics total mass to orbit tonnes` | useful | Led to McDowell's annual report |
| 47 | 2026-10-11 | Opened: McDowell, "Space Activities in 2025", Rev 1.4, 4 Feb 2026, https://planet4589.org/space/papers/space25.1.4.pdf | useful | Launch counts, payload mass launched (Table 7), mass in orbit (Table 13) |
| 48 | 2026-10-11 | WebSearch: `NASA OIG report Human Landing System Starship refueling tanker launches number propellant transfer demonstration 2026` | useful (leads) | |
| 49 | 2026-10-11 | WebSearch: `Starship ship-to-ship propellant transfer demonstration flight 2025 2026 cryogenic transfer result` | thin | Wikipedia, prediction markets |
| 50 | 2026-10-11 | WebSearch: `oig.nasa.gov audit Human Landing System Starship HLS propellant transfer launches report IG-24 OR IG-25 OR IG-26` | useful | Found IG-26-004 |
| 51 | 2026-10-11 | Opened: NASA OIG, "NASA's Management of the Human Landing System Contracts", IG-26-004, 11 Mar 2026 (PDF, text extracted) | useful | Tanker count, cadence, transfer-demo slip |
| 52 | 2026-10-11 | WebSearch (extended): `Starship vehicle-to-vehicle propellant transfer test completed 2026 two ships docked` | thin (secondary) | SpaceDaily: not attempted as of Flight 13, 24 Jul 2026 |
| 53 | 2026-10-11 | WebSearch: `Momentum-eXchange Electrodynamic Reboost MXER tether NASA study tip speed payload mass ratio NTRS` | useful | NTRS leads |
| 54 | 2026-10-11 | WebSearch: `YES2 tether 31.7 km deployment 2007 longest tether flown ESA Foton-M3 result` | thin (secondary) | Wikipedia, ScienceDaily, Guinness; 31.7 km not confirmed from a primary page (see Open threads) |
| 55 | 2026-10-11 | Opened: Bonometti and Frame (NASA MSFC), "Space Tethers Programmatic Infusion Opportunities", NTRS 20060004770 (PDF) | useful | Flight history; tether specific-mass comparison |
| 56 | 2026-10-11 | WebSearch: `Sorensen MXER tether design 2.4 km/s tip velocity facility mass payload 2500 kg GTO AIAA 2003 conceptual design` | thin | Sorensen 2003 not openable; found AIAA-2006-4521 |
| 57 | 2026-10-11 | Opened: Bonometti, Sorensen, Dankanich, Frame, "2006 Status of the MXER tether development", AIAA-2006-4521, NTRS 20060047739 (PDF) | useful | 100 km tether, 2 g tip, ground catch tests |
| 58 | 2026-10-11 | WebSearch: `Janhunen electric solar wind sail thrust per km tether 1 AU characteristic acceleration mm/s2 ESTCube-1 result` | useful | |
| 59 | 2026-10-11 | WebSearch: `aerocapture never flown NASA aerocapture technology readiness Mars Earth mass savings study Spilker OR Hall` | useful | Led to the 2016 JPL assessment |
| 60 | 2026-10-11 | Opened: Spilker et al. (JPL), "An Assessment of Aerocapture and Applications to Future Missions", JPL D-97058, 13 Feb 2016 (PDF) | useful | Never flown; ASAT payload gains |
| 61 | 2026-10-11 | WebSearch: `Mars Reconnaissance Orbiter aerobraking 2006 delta-v saved m/s number of drag passes propellant savings NASA` | useful (secondary for 600 kg) | 600 kg propellant saved is from news summaries only |
| 62 | 2026-10-11 | Opened: NTRS 20070030304, Amundsen, Dec, Gasbarre, "Thermal Model Correlation for MRO" (abstract) | useful | "over 400 aeroheating drag passes", six months from March 2006 |
| 63 | 2026-10-11 | WebSearch: `Janhunen 2010 "Electric sail for spacecraft propulsion" OR "electric solar wind sail" thrust 1/r scaling arXiv paper` | useful | |
| 64 | 2026-10-11 | Opened: Janhunen et al., "Electric solar wind sail: Toward test missions", Rev. Sci. Instrum. 81, 111301 (2010), https://www.electric-sailing.fi/paper9.pdf | useful | 1 N, about 100 kg, about 1/r |
| 65 | 2026-10-11 | WebSearch: `ESTCube-1 tether deployment failed 2013 result electric sail test outcome` | useful | |
| 66 | 2026-10-11 | Opened: eoPortal, ESTCube-1 mission page | useful | Tether never deployed; mission ended 17 Feb 2015 |
| 67 | 2026-10-11 | WebSearch: `Keck Institute for Space Studies 2012 Asteroid Retrieval Feasibility Study 500 t 7 m asteroid 40 kW solar electric propulsion $2.6 billion report pdf` | useful (abstract) | |
| 68 | 2026-10-11 | Downloaded: https://kiss.caltech.edu/final_reports/Asteroid_final_report.pdf (three routes: plain, insecure-certificate retry, www host) and the Caltech repository file link | dead at the sources | Certificate error then HTTP 404; repository 403 |
| 69 | 2026-10-11 | Opened: Caltech Authors record kqeqz-18608 (Brophy, Friedman, Culick, "Asteroid retrieval feasibility", March 2012, abstract); NSS page ?p=3430 | useful (abstract only) | 7 m, 250 to 1,000 t, 40 kW SEP, Atlas V class; the $2.6 billion figure in my query was NOT confirmed and is not used |
| 70 | 2026-10-11 | WebSearch: `Sonter 1997 "The technical and economic feasibility of mining the near-earth asteroids" net present value mass payback ratio delta-v` | useful | |
| 71 | 2026-10-11 | Opened: Sonter, "The Technical and Economic Feasibility of Mining the Near-Earth Asteroids", IAF Congress 1998 (NSS-hosted, 8 pp.) | useful | Delta-v table, 1,000 t/yr market, equipment throughput |
| 72 | 2026-10-11 | **RESUMED SESSION (re-dispatch after a usage-limit cut-off).** The earlier run logged rows 1 to 71 but wrote no Findings. Per the brief (every figure from a source opened *this* session), the sources below are re-opened before any figure is used; the notes in rows 1 to 71 are treated as leads only | n/a | |
| 73 | 2026-10-11 | Re-opened: SP-428 III-3 (Arnold et al., 1977 Ames Summer Study), https://nss.org/settlement/nasa/spaceres/III-3.html | useful | Lunar launcher figures quoted in Findings 2 |
| 74 | 2026-10-11 | Re-opened: SP-428 IV-2 (O'Leary, Gaffey, Ross, Salkeld, 1977), https://nss.org/settlement/nasa/spaceres/IV-2.html (two passes) | useful | Retrieval figures quoted; fetch tool flattened a superscript ("106" for 10^6), resolved on the second pass |
| 75 | 2026-10-11 | Re-opened: SP-428 III-1 "Mass Drivers I: Electrical Design", https://nss.org/settlement/nasa/spaceres/III-1.html | useful | Exhaust 6,000 to 10,000 m/s; "tens of gravities" model test. The fetch tool gave the author as "Arnold et al.", which conflicts with row 17 ("Chilton et al."); author attribution left unconfirmed |
| 76 | 2026-10-11 | Re-opened: JPL SSD astrodynamic parameters (DE440), https://ssd.jpl.nasa.gov/astro_par.html | useful | GM Sun, AU, GM Earth, GM Moon |
| 77 | 2026-10-11 | Re-opened: NSSDC planetary fact sheet summary (last updated 18 Mar 2025) and the Mercury (11 Jan 2024), Venus (11 Jan 2024), Earth (15 Nov 2024), Moon (11 Jan 2024), Mars (19 May 2025) fact sheets | useful | Note: the Earth and Mars sheets now carry later dates than row 23 recorded |
| 78 | 2026-10-11 | Re-opened: Jehn and Schoenmaekers, ISSFD 24 (2014) PDF, text extracted locally | useful | "about 16 km/s in total" direct Hohmann; SEP 4.254 km/s; Isp 4,022 s |
| 79 | 2026-10-11 | Re-opened: McAdams et al., JHU APL Tech. Dig. 34(1), PDF, text extracted locally | useful | ">2213 m/s"; six flybys ">91%" of total DV; MOI 861.714 m/s |
| 80 | 2026-10-11 | Re-queried: NASA JPL SSD NHATS Data API v1.3, https://ssd-api.jpl.nasa.gov/nhats.api (default constraints) | useful | 7,139 objects again; tallied locally by min delta-v and by estimated size |
| 81 | 2026-10-11 | Opened: NHATS page https://cneos.jpl.nasa.gov/nhats/ (definition of total delta-v) and API doc https://ssd-api.jpl.nasa.gov/doc/nhats.html (v1.3, Sep 2019; defaults dv 12, dur 450, stay 8, launch 2020-2045) | useful | |
| 82 | 2026-10-11 | Fetched: NSS-hosted Sonter PDF at /2017/07/Sonter-Technical-and-Economic-Feasibility-of-Mining-NEAs.pdf | dead at the query | HTTP 404; the URL was guessed |
| 83 | 2026-10-11 | WebSearch: `Sonter "Technical and Economic Feasibility of Mining the Near-Earth Asteroids" nss.org pdf` | useful | Two NSS URLs and a lead to Hein et al. 2018 |
| 84 | 2026-10-11 | Opened: Sonter, IAF 1998, https://NSS.org/wp-content/uploads/2023/05/the-technical-and-economic-feasibility-of-mining-the-near-earth-asteroids.pdf (text extracted locally) | useful | Table 2 delta-v; 1.5 km/s lunar-flyby limit; 5 t equipment, 1,000 t/day regolith |
| 85 | 2026-10-11 | Opened: Hein, Matheson, Fries, "A Techno-Economic Analysis of Asteroid Mining", IAC-18 (arXiv:1810.03836, 2018) (text extracted locally) | useful | See Findings 5 |
| 86 | 2026-10-11 | WebSearch: `Venus ascent vehicle from balloon altitude delta-v gravity drag losses km/s sample return study NTRS` | thin | Forum and mailing-list summaries (secondary); led to NTRS 20000052454 |
| 87 | 2026-10-11 | Opened: NTRS 20000052454 (Cutts et al., "Venus Aerobot Multisonde Mission", AIAA Balloon Technology Conference 1999) | dead at the sources | Not about ascent; not used |
| 88 | 2026-10-11 | WebSearch: `Palaszewski atmospheric mining outer planets ascent vehicle delta-v Uranus Saturn orbit nuclear helium-3 NTRS` | useful | Nine NTRS links |
| 89 | 2026-10-11 | Opened (PDF, text extracted): NTRS 20150006664, 20170004746, 20205004479, 20170009136, 20170005215, 20170003041 (Palaszewski, NASA GRC, 2015 to 2020) | useful | Orbital velocity table found only in the 2016 slide decks (20170005215, 20170003041) |
| 90 | 2026-10-11 | WebSearch: `"Venus Surface Sample Return" "Weighty High-Pressure Challenge" Sweetser ascent vehicle delta-v orbit` | useful | The named paper was not returned (dead at the query for that title); led to two NTRS studies |
| 91 | 2026-10-11 | Opened (PDF, text extracted): Landis and Oleson, AIAA ASCEND 2024, NTRS 20240000426; Seager et al., NIAC Phase I final report, NTRS 20250005767 | useful | VAV ~9 km/s, 1,800 kg for 10 kg |
| 92 | 2026-10-11 | Re-opened: NTRS 20220007037 (Cassady et al. 2022), via NTRS API download link SP2022_438_CASSADY.pdf (first direct-ID download failed: dead at the query, wrong filename) | useful | AEPS Table 1, PPE, SEP cargo tug Table 2 |
| 93 | 2026-10-11 | Re-opened: NTRS 20190004993 (X3), abstract via the NTRS JSON API (the HTML record page timed out) | useful | |
| 94 | 2026-10-11 | Re-opened: NTRS 20210008613 (Dawn), record page | useful | |
| 95 | 2026-10-11 | WebSearch: `Psyche SPT-140 Hall thruster flight performance thrust mN specific impulse 4.5 kW xenon 1085 kg paper` | thin | Wikipedia for 280 mN / 1,800 s (not used); NTRS 20170003033 opened: 4.5 kW nominal, up to 6 kW |
| 96 | 2026-10-11 | WebSearch: `NERVA XE engine test specific impulse thrust 1969 thrust-to-weight NASA report nuclear thermal rocket Phoebus 4000 MW` | useful | NTRS 19910018902 (Bennett) and 20150004421 (Borowski) opened |
| 97 | 2026-10-11 | WebSearch: `DARPA DRACO nuclear thermal rocket program cancelled 2025 never flown nuclear thermal propulsion in space` | thin (secondary) | News only; flight status labeled secondary |
| 98 | 2026-10-11 | WebSearch: `SNAP-10A 1965 only US nuclear reactor flown in space electrical power 500 watts ion thruster NASA report` and `SNAP-10A flight results 1965 NTRS OR osti.gov reactor 43 days 500 W thermoelectric report` | useful | ANS Nuclear News (Apr 2023) PDF opened; SAE paper 650793 paywalled (dead at the sources) |
| 99 | 2026-10-11 | WebSearch: `KRUSTY Kilopower test results 2018 NASA NTRS 1 kWe thermal power hours full power test` | useful | NTRS 20180007389, 20180005435 opened |
| 100 | 2026-10-11 | WebSearch: `nuclear electric propulsion MW-class specific mass kg/kWe NASA study human Mars 2021 NTRS alpha` | useful | NTRS 20210017337 opened; 20220017245, 20220002034 not opened (Open threads) |
| 101 | 2026-10-11 | WebSearch: `NASA Advanced Composite Solar Sail System ACS3 sail area 80 square meters deployed 2024 results characteristic acceleration` | useful | NTRS 20260000942 record opened; the 0.045 mm/s² figure in the summary came from a simulation presentation, not used |
| 102 | 2026-10-11 | WebSearch: `IKAROS solar sail JAXA 2010 measured solar radiation pressure thrust 1.12 mN 196 m2 sail results paper` | useful | JAXA press release opened (thrust only) |
| 103 | 2026-10-11 | Re-opened: Janhunen et al. 2010, https://www.electric-sailing.fi/paper9.pdf (text extracted locally); eoPortal ESTCube-1 page | useful | |
| 104 | 2026-10-11 | Re-opened: NTRS 20060047739 and 20060004770 (tethers), text extracted locally | useful | |
| 105 | 2026-10-11 | WebSearch: `Spilker "An Assessment of Aerocapture and Applications to Future Missions" JPL D-97058 2016 pdf`; opened https://solarsystem.nasa.gov/system/downloadable_items/153_AerocapRpt20D1.pdf | useful | "has yet to be implemented on a space flight mission" |
| 106 | 2026-10-11 | Re-opened: NTRS 20070030304 (MRO aerobraking) abstract via API | useful | |
| 107 | 2026-10-11 | WebSearch: `RS-25 engine vacuum specific impulse 452 seconds thrust 512,000 lbf NASA fact sheet`; opened L3Harris RS-25 spec sheet PDF (July 2024) | useful | |
| 108 | 2026-10-11 | WebSearch: `laser lightcraft flight record altitude 71 m Myrabo 2000 White Sands beamed energy propulsion NASA report`; opened Myrabo SSI paper (NSS-hosted) | useful | |
| 109 | 2026-10-11 | Re-opened: McDowell, "Space Activities in 2025", Rev 1.4 (PDF, text extracted locally) | useful | Tables 1, 7, 13 |
| 110 | 2026-10-11 | Re-opened: Jones, ICES-2018-81, NTRS 20200001093 (PDF via NTRS API) | useful | Table A2, Figure 1 text |
| 111 | 2026-10-11 | Re-downloaded: Our World in Data CSV and metadata for "cost-space-launches-low-earth-orbit" (CSIS 2022 data, constant 2021 US$, last updated 2025-03-04) | useful | |
| 112 | 2026-10-11 | WebSearch: `oig.nasa.gov IG-26-004 "Human Landing System" Starship tanker launches propellant transfer`; opened the OIG PDF (text extracted locally) | useful | Depot plus "more than 10" tankers, one per 6 days; transfer "never been done vehicle-to-vehicle" |
| 113 | 2026-10-11 | Downloaded: SpaceX Starship user's guide PDF (https://www.spacex.com/media/starship_users_guide_v1.pdf) and SpaceX Falcon Heavy page | dead at the sources | HTML shell returned; no payload figure from SpaceX obtained |
| 114 | 2026-10-11 | Opened: Caltech Authors record kqeqz-18608 (KISS 2012 abstract) | useful (abstract) | 7 m, 250 to 1,000 t, 40 kW SEP, Atlas V class, high Earth orbit |
| 115 | 2026-10-11 | WebSearch: `world annual xenon production tonnes per year air separation supply electric propulsion constraint` | useful (lead) | Market pages (secondary, not used); Lindner MPIK slides opened |
| 116 | 2026-10-11 | Opened: NIST CODATA standard gravity page | useful | |
| 117 | 2026-10-11 | WebSearch: `nss.org settlement nasa spaceres mass catcher L2 lunar material catcher design O'Neill Heppenheimer` | thin | SSI/NSS history pages only; no catcher numbers (dead at the sources for numbers) |
| 118 | 2026-10-11 | WebSearch: `NASA SP-413 Space Settlements A Design Study chapter 5 mass catcher mass driver lunar transport tonnes per year nss.org 75SummerStudy` | useful | Led to SP-413 Appendix G |
| 119 | 2026-10-11 | Opened: NASA SP-413 Appendix G "The Mass Catcher", https://nss.org/settlement/nasa/75SummerStudy/5appendG.html | useful | |
| 120 | 2026-10-11 | WebSearch: `NASA JPL Mars solar conjunction communications moratorium Sun-Earth-Mars angle degrees command moratorium 2025` | useful | |
| 121 | 2026-10-11 | Opened: JPL news 28 Sep 2021 (no angle stated: thin) and LASP/MAVEN 3 Jun 2015 ("within two degrees") | useful | |
| 122 | 2026-10-11 | WebSearch: `NASA OTPS 2024 report launch cost per kg assumption Starship future projection $/kg low Earth orbit space-based solar power` | useful | SSI-hosted copy and news; the NASA PDF opened directly |
| 123 | 2026-10-11 | Opened: NASA OTPS, "Space-Based Solar Power", 11 Jan 2024 (PDF, text extracted locally) | useful | Starship assumptions labeled as such |
| 124 | 2026-10-11 | WebSearch: `Kornuta 2019 "Commercial lunar propellant architecture" REACH cost per kg propellant delivered L1 LEO tonnes per year` | thin | Kornuta full text not returned (dead at the query for that paper); led to Metzger arXiv:2303.09011 |
| 125 | 2026-10-11 | Opened: Metzger, arXiv:2303.09011 (text extracted locally) | useful | |
| 126 | 2026-10-11 | Opened: NSS SP-413 table of contents; Appendix F "The Mass Driver"; Appendix H "Trajectories from the Moon to L2" | useful | |
| 127 | 2026-10-11 | WebSearch: `liquid hydrogen boil-off rate percent per day passive storage in orbit NASA cryogenic fluid management zero boil-off 90 K reduced boil-off NTRS` | thin | Ground tanks only; 1982 in-orbit estimate cited by a summary from yarchive (secondary; not used) |
| 128 | 2026-10-11 | Opened: NTRS 20190028305 (Krenn and Desenberg, KSC sphere) | thin | Ground tank, gallons per day; not used |
| 129 | 2026-10-11 | WebSearch (extended): `in-space liquid hydrogen storage boil-off percent per day multilayer insulation orbit tank NASA study 0.1% per day depot` | thin | Opened NTRS 20130011367 (ground tank NER 0.09 to 0.10 %/day) and 20170006481 (IRAS zero boil-off, ground; no rate grepped); **no in-orbit primary rate found: dead at the sources** |
| 130 | 2026-10-11 | WebSearch: `helium-3 abundance lunar regolith ppb tonnes regolith processed per kg helium-3 Wittenberg Kulcinski` | not used | Lunar helium-3 lies in the sibling Moon file's scope; summary figures not used |
| 131 | 2026-10-11 | Re-read locally: Palaszewski NTRS 20205004479 sections on ASC sizing and payload | useful | |
| 132 | 2026-10-11 | WebSearch (extended): `Mercury mass driver launch materials Mercurian resources export O'Neill era study escape velocity 4.25 km/s solar power` | dead at the sources | Popular pages only; no primary Mercurian mass-driver study |
| 133 | 2026-10-11 | Opened: science.gov topic page "mercurian mass-drivers energy" (first 100,000 of 814,658 characters) | thin | Only SP-428 III-3 surfaced; the rest of the page not read (Open threads) |
| 134 | 2026-10-11 | WebSearch (extended): `arXiv delta-v required to reach main belt asteroids from LEO distribution km/s Elvis McDowell Taylor 2018` (second angle on row 8, which died at the query) | useful | Author copy on planet4589.org |
| 135 | 2026-10-11 | Opened: Taylor, McDowell, Elvis 2018 (author PDF, text extracted locally) | useful | Median 9.96 km/s; 3,986 below 8 km/s |
| 136 | 2026-10-11 | WebSearch: `Satellite Today SpaceX shares details higher bandwidth V2 mini Starlink satellites argon Hall thruster 170 mN`; re-opened the Satellite Today article (27 Feb 2023) | useful (secondary) | Second pass on row 34; ratios to first-generation thrusters confirmed, absolute Isp still not stated |
| 137 | 2026-10-11 | Re-opened: Jedicke et al., arXiv:1905.13457v1 (text extracted locally) | thin | Confirms the "~76 km s^-1" typo (C5) and cites Bao et al. 2015 (< 1.8 km/s capture via lunar gravity assist) |
| — | 2026-10-11 | **Tally for the whole file (both sessions):** about 63 web searches (rows with two query strings counted twice), 137 log rows, 18 rows marked dead (at the query or at the sources). Unreadable: SpaceX vehicle pages and user's guide, KISS 2012 full report, Jedicke 2018 (paywall), SAE SNAP-10A paper (paywall), Sorensen 2003 MXER | n/a | |

## Findings

Evidence levels used in every table: **DEMONSTRATED** (flown or built), **ENGINEERING-STUDIED** (a quantitative design
study), **SPECULATIVE** (thought experiment or concept paper). Derived values (calculated here from sourced constants)
are marked **DERIVED** and their arithmetic is in *Derived figures*.

### F1. Delta-v budgets and transfer times (checklist 1)

**Sourced figures (flown missions, design studies, handbook tables).**

| Quantity | Value and units | Source (publisher, title, URL, date) | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Direct Hohmann Earth to Mercury, "launch and arrival" total | "about 16 km/s in total" (ENGINEERING-STUDIED) | Jehn and Schoenmaekers (ESA/ESOC), "BepiColombo trajectory options to Mercury in 2016 and 2017", ISSFD 24, https://issfd.org/ISSFD_2014/ISSFD24_Paper_S6-5_jehn.pdf, 2014 | Primary | DERIVED D1 gives hyperbolic excess speeds 7.55 + 7.53 = 15.1 km/s for coplanar circular orbits (Mercury's e = 0.206 and i = 7 deg raise it); impulsive LEO-to-low-Mercury-orbit is 11.2 km/s (D1). See Conflicts C1 | Medium: the paper does not define whether "16 km/s" is a sum of v-infinities or of burns |
| BepiColombo actual route (SEP + flybys) | Earth escape 3.475 km/s (Ariane 5); SEP delta-v 4.254 km/s; Isp 4,022 s (exhaust 39.5 km/s); initial mass 4,100 kg; 1 Earth, 2 Venus, 5 Mercury flybys; cruise 7.5 years (9 Jul 2016 to 1 Jan 2024 in the studied case); total impulse 16.6 MNs; Mercury-relative speed lowered by flybys to 1.82 km/s, then "weakly captured" (ENGINEERING-STUDIED; a 2014 trajectory study, not the flown trajectory) | Jehn and Schoenmaekers 2014 (as above), Table 3 and Sec. 3 | Primary | MESSENGER (next row) shows the same flyby-dominated pattern | High for the study case |
| MESSENGER propulsive delta-v, flybys | ">2213 m/s of propulsive DV"; "six planetary gravity-assist flybys" imparted ">91% of the trajectory's total velocity change"; Mercury orbit insertion (March 2011) delivered 861.714 m/s (target 862.166) into a 12-h orbit with 200 km minimum altitude; whole mission 10.8 years (DEMONSTRATED) | McAdams et al., "Spacecraft Trajectory Planning and Execution for the MESSENGER Mission", JHU APL Tech. Dig. 34(1), https://jhuapl.edu/sites/default/files/2024-09/34-01-McAdams.pdf (file dated 2024-09) | Primary | BepiColombo study above | High |
| Delta-v table (Sonter) | Earth surface to LEO 8.0; surface to escape 11.2; surface to GEO 11.8; LEO to escape 3.2; LEO to Mars or Venus transfer orbit 3.7; LEO to GEO 3.5; LEO to HEEO 2.5; LEO to Moon landing 6.3; LEO to NEA "approx 5.5"; **lunar surface to LEO (with aerobraking) 2.4**; **NEA to Earth transfer orbit "approx 1.0"**; Phobos/Deimos to LEO 8.0 (all km/s) (ENGINEERING-STUDIED, round figures) | Sonter, "The Technical and Economic Feasibility of Mining the Near-Earth Asteroids", 49th IAF Congress, Melbourne, 1998, Table 2, https://NSS.org/wp-content/uploads/2023/05/the-technical-and-economic-feasibility-of-mining-the-near-earth-asteroids.pdf | Primary (conference paper) | DERIVED D1: lunar surface to LEO with aerocapture 2.52 km/s; LEO to Mars transfer 3.57 km/s | Medium: rounded, no assumptions stated |
| NEA return: the hard part is Earth capture | "Lunar flyby is of partial use only, because it can remove only 1.5 km/s... the delta-v requirement to achieve Earth-capture, is in fact more demanding than the asteroid-departure delta-v requirement"; targets with outbound under 6 km/s and "return departure delta-v under 2 km/sec" exist; low-energy windows "at approx 2-yearly intervals" | Sonter 1998 (as above), abstract and trajectory section | Primary | SP-428 IV-2 also uses a 1.5 km/s lunar gravity-assist component (row below) | Medium |
| NHATS NEA accessibility (round trip from LEO) | Default query (dv at most 12 km/s, duration at most 450 d, stay at least 8 d, launch 2020 to 2045): **7,139 objects**. Count with minimum total delta-v at most 4 / 5 / 6 / 8 / 10 km/s: **38 / 283 / 719 / 2,173 / 4,301**; median 9.37 km/s; lowest 3.389 km/s (2021 GM1, est. 1.4 to 6.5 m). Of objects whose upper size estimate is at least 100 m: 1,236, of which 26 at 6 km/s or less and 2 at 5 or less; none of the 212 objects at least 300 m reaches 6 km/s or less. Lowest-delta-v object with a lower size estimate of at least 100 m: numbered asteroid 99942, 6.049 km/s (DEMONSTRATED dataset; trajectories computed, not flown) | NASA JPL SSD/CNEOS, NHATS Data API v1.3, https://ssd-api.jpl.nasa.gov/nhats.api, queried 2026-10-11; definitions https://cneos.jpl.nasa.gov/nhats/ and https://ssd-api.jpl.nasa.gov/doc/nhats.html | Primary (dataset) | Sonter's "approx 10% of NEAs are more accessible than the Moon" (1998, older catalog) | High for the counts on the query date; note the metric is a crewed **round trip** (depart 400 km LEO, match NEA, depart NEA, control entry speed), not a one-way cargo return to orbit |
| SP-428 asteroid retrieval delta-v | "velocity increment ΔV of 3 km/sec in 5 years" for retrieving part of a 200 m (1 x 10^7 t) asteroid; return delta-v assumed 5 km/s for a 10^6 t fragment case; 1.5 km/s lunar gravity-assist component (ENGINEERING-STUDIED, 1977) | O'Leary, Gaffey, Ross, Salkeld, "Retrieval of Asteroidal Materials", NASA SP-428 Part IV-2 (1977 Ames Summer Study, pub. 1979), https://nss.org/settlement/nasa/spaceres/IV-2.html | Primary (NASA SP, NSS transcription) | Sonter 1.5 km/s lunar flyby | Medium (1977 catalog) |
| Synodic periods (launch-window spacing) | Mercury 115.88 d; Venus 583.92 d; Mars 779.94 d (relative to Earth) | NASA NSSDC fact sheets (Mercury 11 Jan 2024; Venus 11 Jan 2024; Mars 19 May 2025), https://nssdc.gsfc.nasa.gov/planetary/factsheet/ | Primary | none sought (stable) | High |
| Constants used for DERIVED rows | GM Sun 1.32712440041279419 x 10^20 m^3/s^2; AU 149,597,870,700 m; GM Earth 398,600.435507 km^3/s^2; GM Moon 4,902.800118 km^3/s^2 (DE440); GM Mercury 0.022032, Venus 0.32486, Mars 0.042828 (x 10^6 km^3/s^2); mean radii Mercury 2,439.7, Venus 6,051.8, Earth 6,371.0, Moon 1,737.4, Mars 3,389.5 km; semimajor axes Mercury 57.909, Venus 108.210, Earth 149.598, Mars 227.956 (10^6 km); Moon orbit 0.3844 x 10^6 km, mean orbital speed 1.022 km/s | JPL SSD, https://ssd.jpl.nasa.gov/astro_par.html; NSSDC fact sheets (dates above; Earth 15 Nov 2024) | Primary | NSSDC summary sheet (18 Mar 2025) agrees on rounded values | High |

**DERIVED delta-v table (D1).** Two-impulse Hohmann, coplanar circular orbits, patched conics, no gravity assists, no
losses. "Depart" is from low orbit (Mercury 200 km, LEO 400 km, low Mars orbit 300 km) or, for 0.1/0.3/0.5 AU, from a
circular heliocentric orbit with no body. "Capture" is into the same low orbits. "Aerocapture" column assumes arrival
v-infinity is removed for free by the atmosphere (never flown; see F4). Arithmetic in *Derived figures*.

| Leg | Depart (km/s) | Arrival v-inf (km/s) | Capture to low orbit (km/s) | Total, all-propulsive (km/s) | Total if aerocaptured (km/s) | Transfer time |
|---|---|---|---|---|---|---|
| 0.1 AU circular to Earth | 32.81 | 17.08 | 12.57 | 45.38 | 32.81 | 74 d |
| 0.1 AU circular to Mars | 34.85 | 15.66 | 12.98 | 47.82 | 34.85 | 134 d |
| 0.3 AU circular to Earth | 13.07 | 9.55 | 6.78 | 19.85 | 13.07 | 96 d |
| 0.3 AU circular to Mars | 15.92 | 10.29 | 7.95 | 23.87 | 15.92 | 159 d |
| 0.5 AU circular to Earth | 6.52 | 5.47 | 4.48 | 10.99 | 6.52 | 119 d |
| 0.5 AU circular to Mars | 9.57 | 7.17 | 5.23 | 14.80 | 9.57 | 186 d |
| Low Mercury orbit to Earth | 7.55 | 7.53 | 5.54 | 13.09 | 7.55 | 105 d |
| Low Mercury orbit to Mars | 10.34 | 8.77 | 6.60 | 16.94 | 10.34 | 171 d |
| Main belt 2.2 AU to Earth | 4.21 | 5.14 | 4.33 | 8.54 | 4.21 | 370 d |
| Main belt 2.2 AU to Mars | 1.91 | 2.10 | 1.85 | 3.76 | 1.91 | 464 d |
| Main belt 2.7 AU to Earth | 4.80 | 6.20 | 4.82 | 9.62 | 4.80 | 460 d |
| Main belt 2.7 AU to Mars | 2.73 | 3.15 | 2.35 | 5.08 | 2.73 | 561 d |
| Main belt 3.2 AU to Earth | 5.16 | 6.98 | 5.23 | 10.39 | 5.16 | 556 d |
| Main belt 3.2 AU to Mars | 3.28 | 3.96 | 2.83 | 6.10 | 3.28 | 663 d |
| LEO to low Mars orbit | 3.57 | 2.65 | 2.09 | 5.66 | 3.57 | 259 d |
| Lunar surface to LEO | 2.52 (from surface, no orbit stop) | n/a (geocentric) | 3.08 | 5.60 | 2.52 | 5.0 d |
| Lunar surface to GEO | 2.44 | n/a | 1.05 | 3.50 | n/a | 5.7 d |
| Venus cloud deck (55 km) to Earth, ideal | 10.66 (no drag, no gravity loss) | 2.50 | 3.46 | 14.12 | 10.66 | 146 d |
| Venus cloud deck (55 km) to Mars, ideal | 11.82 | 4.77 | 3.37 | 15.19 | 11.82 | 218 d |

Reading the table: **near-Sun circular orbits are the most expensive sources in the set.** 0.1 AU costs about 33 km/s
just to leave on a Hohmann transfer, because the circular speed there is 94.2 km/s (D1). Main-belt material reaches
**Mars** for less delta-v than Mercury material reaches Earth. Main-belt orbits are inclined and eccentric, so these
coplanar figures are lower bounds. **Mercury and the near-Sun cases can be cut sharply with Venus and Earth flybys
over many years** (BepiColombo: 4.25 km/s of SEP plus eight flybys over 7.5 years, against about 16 km/s direct). The
same trick applies outbound from the Sun in reverse geometry, but no study giving such numbers for cargo was found
(Open threads). **Venus cloud-top ascent is a full orbital launch** (circular speed 7.29 km/s at 55 km, escape speed 10.32 km/s, D1),
from a floating platform, before any drag or gravity loss.

**F1b. Leaving deep gravity wells: Venus clouds, gas-giant atmospheres, Mercury's surface (sourced).**

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Venus Ascent Vehicle (VAV) launch delta-v from a balloon at 60 to 67 km | "Launch ΔV ~9 km/s" (vs "~5 km/s" for the Mars Ascent Vehicle); launch pressure "~0.2 bar"; launch g-load "40 g axial" (ENGINEERING-STUDIED) | Seager et al., "Venus Atmosphere and Cloud Particle Sample Return for Astrobiology", NIAC Phase I Final Report, 27 Jan 2023, rev. 14 Jul 2025, Table 10, NTRS 20250005767, https://ntrs.nasa.gov/api/citations/20250005767/downloads/NIAC_2022_PhI_Seager_VenusSampleReturn.pdf | Primary | D1: ideal circular speed at 55 km is 7.29 km/s, so about 1.7 km/s of the 9 km/s is drag, gravity and steering loss; a secondary forum lead gave "1500 m/s ballpark" for losses (not used) | Medium (Phase I study) |
| VAV mass and payload | "An 1800 kg VAV can be carried by a 27-m diameter balloon and launched from 60 km altitude to deliver a 10 kg sample canister to orbit"; baseline GLOM 1,840 kg; single-stage hypergolic option "more than 3000 kg"; solid or hybrid single stage "not viable" (ENGINEERING-STUDIED) | Seager et al. 2023/2025 (as above), findings 4a and Sec. 3.4, 5.2 | Primary | Landis and Oleson 2024 (next row): "nearly as difficult to launch into orbit from Venus as... from the surface of the Earth" | Medium. Payload is about 0.55% of lift-off mass at this tiny scale |
| Difficulty of Venus launch from altitude | "for a launch from a nominal altitude of 65 km above the surface, the atmospheric density is only slightly less that of Earth. The net result is that it is nearly as difficult to launch into orbit from Venus as it is to launch from the surface of the Earth"; proposed CO/LOX propellant made from atmospheric CO2, Isp 250 s; 2.35 t of propellant for a vehicle modeled on the SS-520 (2.6 t, 4 kg payload) (ENGINEERING-STUDIED) | Landis and Oleson (NASA GRC), "A Conceptual Architecture for Venus Surface Sample Return", AIAA ASCEND, 30 Jul to 1 Aug 2024, NTRS 20240000426 | Primary | Seager (above) | Medium. Landis gives Venus escape 10.46 km/s; NSSDC gives 10.36 (Conflicts C2) |
| Orbital velocity at 10 km altitude, giant planets (the ascent delta-v floor before losses) | Jupiter 41.897 km/s ("BIG"); Saturn 25.492 ("BIG"); Uranus 15.053 ("More acceptable"); Neptune 16.618 ("More acceptable") (ENGINEERING-STUDIED) | Palaszewski (NASA GRC), "Atmospheric Mining in the Outer Solar System: Outer Planet Orbital Transfer and Lander Analyses", 52nd AIAA/ASME/SAE/ASEE JPC, July 2016, slide "Orbital Velocities: 10 km altitude", NTRS 20170005215 (also in NTRS 20170003041) | Primary (NASA presentation) | NSSDC escape speeds (Jupiter 59.5, Saturn 35.5 km/s) are consistent with these circular speeds | High for the numbers (straight orbital mechanics) |
| Aerospacecraft (ASC) ascent capability for gas-giant mining | "The ASC total delta-V capability is 20.5 km/s", from subsonic flight at mining altitude to an 800 km orbit (Uranus case); gas-core nuclear rocket, 1,800 to 2,500 s Isp assumed (SPECULATIVE: gas-core nuclear rockets have not been built) | Palaszewski, "Atmospheric Mining in the Outer Solar System: Aerospacecraft Analysis, Propulsion, and Resource Capturing Implications", AIAA JPC 2020, NTRS 20205004479; 2016 version gives 20.1 km/s (NTRS 20170004746) | Primary | none found | Low to medium: depends on an unbuilt engine |
| Saturn mining verdict | "At Saturn ... the orbital velocity at Saturn increases the mass of the ASC and the mass of the orbital transfer vehicles"; "The need to avoid the high wind speeds in the atmosphere leads to a large delta-V for large orbital plane changes"; described as "extreme added complexity" (ENGINEERING-STUDIED) | Palaszewski, "Solar System Exploration Augmented by In-Situ Resource Utilization: Mercury and Saturn Propulsion Investigations", AIAA 2017-0421 (per the 2020 paper's reference list), NTRS 20170009136 | Primary | Consistent with the 25.5 km/s orbital velocity row | Medium |
| Helium-3 and hydrogen capture rates (Uranus case) | With 3He mass fraction 1.52 x 10^-5 and a 100,000 kg dry ASC: at 4 kg/s gas capture, 500 kg of 3He takes 95.2 days and 293,000 kg of hydrogen is produced per day; at 10 kg/s, 38.1 days and 732,600 kg of hydrogen per day; a full 1,800 s ASC needs 270,000 kg of hydrogen (SPECULATIVE) | Palaszewski, "Atmospheric Mining in the Outer Solar System: Resource Capturing, Storage, and Utilization", NTRS 20150006664 (2015) | Primary | none found | Low: an architecture concept. The ratio shows most captured gas is spent lifting the rest |
| Mercury surface ascent and round trip | Lander one-way delta-v 3.5 km/s, ascent 3.5 km/s, "approximately 19% for gravity losses" on top of 2.945 km/s orbital speed at 100 km; crewed round-trip (no landing) case: Earth departure 5.2, Mercury arrival 10.9, Mercury departure 8.7 km/s, 585 days with 40 days at Mercury; refueling with Mercury polar-ice hydrogen cuts LEO mass from about 3,900 t to 1,520 t (Isp 800 s) (ENGINEERING-STUDIED) | Palaszewski, NTRS 20170009136 (as above) | Primary | D1 gives 2.89 km/s circular speed at 200 km; MESSENGER MOI 0.86 km/s into a 12-h ellipse (not a low circular orbit) | Medium |

**F1c. Main-belt accessibility from LEO (a second angle on the main-belt rows of D1).**

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Delta-v from LEO to rendezvous with known main-belt asteroids (MBAs) | 596,713 MBAs with defined orbits: **median 9.96 km/s**; NEOs (15,922): median 9.22 km/s. 3,986 MBAs below 8 km/s (0.7% tail); 96 below 7.5 km/s; 19 below 7.3 km/s; 4 below 7 km/s. Two- and three-burn impulsive schemes, inclination changed at apoapsis; no real planetary phasing. **This is outbound from LEO; it is not the return leg** (ENGINEERING-STUDIED, catalog-wide calculation) | Taylor, McDowell, Elvis, "A Delta-V map of the known Main Belt Asteroids", Acta Astronautica 146 (2018) 73, author copy https://planet4589.org/jcm/pubs/sci/papers/2018/Taylor18.pdf | Primary (peer-reviewed) | D1 coplanar Hohmann LEO-departure analog: Earth to 2.7 AU is 4.80 km/s heliocentric before LEO departure and rendezvous burns, consistent with about 10 km/s once inclination and both ends are counted; NHATS NEO median 9.37 km/s (round trip, different metric) | High |
| Mercury mass-driver concepts (O'Neill era) | No primary study of a Mercurian mass driver was found; the only "Mercurian mass-driver" hit was the lunar SP-428 III-3 paper. DERIVED: Mercury surface escape speed sqrt(2GM/R) = 4.25 km/s (NSSDC rounds to 4.3), 9.03 MJ/kg (D5) | science.gov topic page (row 133) | n/a | none | Gap logged in Open threads |

### F2. Propulsion candidates (checklist 2)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| **Chemical (hydrogen-oxygen), largest flight engine class** | RS-25: vacuum thrust 512,300 lb (109% power), Isp vacuum 452.3 s, dry weight 7,774 lb, chamber 2,994 psia, mixture 6.03:1; flew all 135 Shuttle flights; now SLS core engine. DERIVED vacuum thrust-to-weight about 66 (DEMONSTRATED) | L3Harris (Aerojet Rocketdyne), "RS-25 Propulsion System" specification sheet, https://l3harris.com/sites/default/files/2024-07/l3harris-ar-rs-25-spec-sheet.pdf, July 2024 | Primary (manufacturer) | Search summaries quoted the same 452.3 s and 512,300 lb (Wikipedia, not used) | High |
| **Solar-electric, Hall, flight-qualifying (largest in development for flight)** | AEPS (12 kW class, from NASA HERMeS 12.5 kW): at 600 V, thrust 608 to 613 mN, Isp 2,882 to 2,896 s; at 300 V, 398 mN, about 2,020 s; HERMeS thrust efficiency 67% (excluding power processor); design life up to 50 kh; AEPS mission need 23 kh = 1,700 kg xenon throughput. Gateway PPE: 60 kW arrays, combined 48 kW EP over seven Hall thrusters (three 12 kW AEPS), up to 2,770 kg xenon, refuelable (ENGINEERING-STUDIED / ground-qualified; not yet flown as of the source) | Cassady et al. (Aerojet Rocketdyne, NASA GRC), "Development of 12 kW Hall Thrusters for NASA Lunar Gateway Power and Propulsion Element", Space Propulsion 2022 (Estoril), NTRS 20220007037, https://ntrs.nasa.gov/api/citations/20220007037/downloads/SP2022_438_CASSADY.pdf, May 2022 | Primary | X3 (next row) gives a similar kW per newton | High for test data. DERIVED power per thrust about 20 kW/N (12 kW / 0.608 N; the paper does not pair a power with each table row, so approximate) |
| **Solar/electric Hall, largest ground-tested** | X3 nested Hall thruster: up to 102 kW total; largest thrust 5.4 N ± 0.1 N at 99 kW, 400 V; efficiency 0.54 to 0.67; Isp 1,800 to 2,650 s; xenon; NASA GRC (DEMONSTRATED on the ground only). DERIVED: about 18.3 kW per newton at the max-thrust point | Hall, Jorns, Gallimore, Kamhawi et al., "High-Power Performance of a 100-kW Class Nested Hall Thruster", NTRS 20190004993 (record dated 12 Jul 2019; work 2017), abstract via NTRS API | Primary | AEPS row | High |
| **Solar-electric, ion, largest flown delta-v** | Dawn ion propulsion: about 51,250 h of operation, about 416 kg xenon, "a delta-V of almost 11.5 km/s, a record for an on-board propulsion system" (DEMONSTRATED) | Rayman and Garner (JPL), "In-Flight Operation of the Dawn Ion Propulsion System Through Completion of the Final Orbit Around Dwarf Planet Ceres", NTRS 20210008613, 9 Jul 2018 (abstract) | Primary | none sought | High |
| SPT-140 Hall thruster (Psyche) | "Nominal 4.5 kW thruster but can operate up to 6 kW" (DEMONSTRATED in flight on Psyche; thrust and Isp from a primary source not obtained) | NASA GRC, "Integration Tests of the 4 kW-class High Voltage Hall Accelerator Power Processing Unit with the HiVHAc and the SPT-140", AIAA-2016-4943 slides, NTRS 20170003033 | Primary | Search summaries gave 280 mN and 1,800 s from Wikipedia (secondary; not used) | Medium |
| **Nuclear-thermal (NTP)** | Rover/NERVA (1959 to 1972): 20 reactors/engines tested at the Nevada Test Site; engine sizes 25, 50, 75, 250 klbf; hydrogen exit 2,350 to 2,550 K (Pewee); Isp 825 to 850 s (hot-bleed, tested on NERVA-XE), 850 to 875 s (expander cycle chosen for flight engine); burn about 62 min single (NRX-A6), about 2 h accumulated with 27 restarts (NRX-XE). Bennett (1991): 1,100 MWt in NRX (55,000 lb thrust), 4,400 MWt in Phoebus (220,000 lb thrust), 28 startup cycles in NRX-XE. Proposed small engine (SNRE) for lunar use: 16.675 klbf, Isp about 900 s, hydrogen flow about 8.4 kg/s, engine thrust/weight about 3.06 (DEMONSTRATED on the ground; never flown) | Borowski and McCurdy (NASA GRC), "The Benefits of Nuclear Thermal Propulsion (NTP) in an Evolvable Mars Campaign", NTRS 20150004421 (2015); Bennett, "Nuclear Thermal Propulsion", Space Transportation Propulsion Technology Symposium, NTRS 19910018902 (1991) | Primary | The two NASA sources agree on scale; flight status: DARPA DRACO flight demonstration was cancelled in 2025 before any flight (Breaking Defense, June 2025, and NewSpace Economy, via search summaries only; secondary) | High for ground-test figures; medium for the "never flown" status (secondary) |
| **Nuclear-electric (NEP), flown** | SNAP-10A (launched 3 Apr 1965): "a 34-kW reactor paired with a power conversion unit that could produce upwards of 500 W of electricity"; automatic shutdown "after just 43 days in orbit" from a spacecraft electrical failure (DEMONSTRATED, power only; its ion-engine experiment ran under an hour per secondary sources) | American Nuclear Society, Nuclear News, "Nuclear applications for space", April 2023, https://wx1.ans.org/pubs/magazines/download/a_1328 | Primary-grade (professional society magazine) | Search summaries (Wikipedia, skyrocket.de) agree on 43 days, about 500 We | Medium-high |
| NEP, latest ground test | KRUSTY (Kilopower): 4 kWt at 800 C reactor for a 1 kWe flight concept; 28 continuous hours at the Nevada National Security Site, completed March 2018; Kilopower scalable "from 1 to 10 kWe" (DEMONSTRATED on the ground) | Gibson et al., "Kilopower Reactor Using Stirling TechnologY (KRUSTY) Nuclear Ground Test Results and Lessons Learned", NASA/TM-2018-219941, NTRS 20180007389; conference version NTRS 20180005435 | Primary | none sought | High |
| NEP, MW-class specific mass | Study range for power-system α: 2 to 30 kg/kWe; "step-like threshold between α values of 10 and 18-20 kg/kW" above which the optimizer shifts to chemical propulsion; radiator areal density assumed 7 kg/m², vs ISS radiators 8.8 kg/m² and JIMO concept 5.1 kg/m²; 4 MWe Brayton case modeled (ENGINEERING-STUDIED) | Duchek et al. (Analytical Mechanics Associates, for NASA), "Hybrid NEP-Chemical Vehicle and Propulsion Technology Study for Crewed Mars Missions", JANNAF 2021, NTRS 20210017337 | Primary | Search summary of other NTRS records: "2.5 MWe at ... no less than 20 kg/kWe" and "15 MWe at ~1 kg/kWe" (not opened; Open threads) | Medium |
| **Solar sail, flown** | IKAROS (JAXA, launched 2010): "The thrust by solar light pressure is 1.12 mili-Newton" (confirmed after deployment, June 2010) (DEMONSTRATED). Sail about 14 x 14 m (196 m²), 7.5 µm polyimide, per press summaries | JAXA press release, 9 Jul 2010, https://global.jaxa.jp/press/2010/07/20100709_ikaros_e.html (thrust only; area from secondary search summaries) | Primary (thrust) / secondary (area) | DERIVED: 1.12 mN / 196 m² = 5.7 µN/m², near the ideal ~9 µN/m² for a perfect reflector at 1 AU (the ideal value is not sourced here; Open threads) | High for thrust |
| Solar sail, NASA | ACS3: 80 m² sail from a 12U CubeSat; launched 24 Apr 2024 (Electron, New Zealand); sail deployed 28 Aug 2024; "the first practical solar sail mission for" NASA (DEMONSTRATED deployment) | Shih (ARC) and Wilkie (LaRC), "ACS3 Mission Results and Lessons Learned", NTRS 20260000942, acquired 30 Jan 2026 (record page) | Primary | Planetary Society and news summaries agree | High for deployment; no measured thrust found |
| **Electric solar-wind sail (E-sail)** | Baseline estimate: 1 N thrust at 1 AU, scaling about 1/r with solar distance, about 100 kg, about 30 deg thrust vectoring, no propellant; with 100 MPa usable tether strength, over 10 N; with hypothetical carbon-nanotube tethers (≥10 GPa), a 10^5 kg E-sail with 1,000 km tethers "might haul 10^6 kg payload at 1 mm/s²" (superscripts lost in text extraction; read as powers of ten); "could also make asteroid resource utilization economically advantageous" (SPECULATIVE) | Janhunen et al., "Electric solar wind sail: Toward test missions", Rev. Sci. Instrum. 81, 111301 (2010), https://www.electric-sailing.fi/paper9.pdf | Primary (peer-reviewed) | Flight test: ESTCube-1 (launched 7 May 2013, ended 17 Feb 2015) carried a 10 m tether: "the most important tether could not be deployed" (eoPortal, https://www.eoportal.org/satellite-missions/estcube-1) | Medium for concept; the thrust has **not** been measured in flight |
| **Beamed laser propulsion** | Lightcraft record: 2 Oct 2000, a 50 g laser-propelled craft to 71 m altitude, 10 kW ground laser at White Sands; lab lightsail tests with the 150 kW LHMEL II laser (DEMONSTRATED only at gram scale, in air) | Myrabo (RPI), "Laser-Propelled Lightsails and Lightcraft: Latest Research Developments", Space Manufacturing 13 (SSI), NSS-hosted PDF, https://space.nss.org/wp-content/uploads/Space-Manufacturing-conference-13-203-Laser-Propelled-Lightcraft.pdf | Primary (conference paper by the experimenter) | Guinness and Wikipedia summaries (secondary) agree on 71 m | High for the record; nothing larger found. **No in-space beamed propulsion demonstration found** |
| **Mass driver, lunar launcher point design** | Launch speed 2,400 m/s ("the lunar escape velocity"); acceleration "1000 Earth gravities"; length 488 m; total power 125 MW; "42-kg/sec throughput"; 650,000 t/yr; 10.5 kg payload per launch at 4 Hz; efficiency 96.4%; system mass 3.13 x 10^6 kg; caliber 0.431 m; development cost line $1,480 million (1977 dollars) (ENGINEERING-STUDIED) | Arnold, Bowen, Cohen, Kaplan, Fine, Kolm, Kolm, Newman, O'Neill, Snow, "Mass Drivers III: Engineering", NASA SP-428 Part III-3 (1977 Ames Summer Study; pub. 1979), https://nss.org/settlement/nasa/spaceres/III-3.html | Primary (NASA SP, NSS transcription) | DERIVED: kinetic energy at 2,400 m/s is 2.88 MJ/kg; x 42 kg/s = 121 MW, consistent with 125 MW. 650,000 t/yr at 42 kg/s implies about 179 days of firing per year | Medium (1977 design; never built at scale) |
| Mass driver as reaction engine | Exhaust velocity "6,000 to 10,000 m/sec"; nominal design mass "100-200 tons"; "accelerations of the order of 10^4 m/sec^2 are almost certainly realizable"; the 1977 model "operated successfully in the acceleration range of tens of gravities" (ENGINEERING-STUDIED; model DEMONSTRATED at tens of g only) | NASA SP-428 Part III-1, "Mass Drivers I: Electrical Design", https://nss.org/settlement/nasa/spaceres/III-1.html (author attribution unconfirmed, see log row 75) | Primary | SP-428 IV-2 uses Ve about 8 km/s, 2,500 t driver at 800 g, 4 kg/s propellant | Medium |
| **Momentum-exchange tether (MXER)** | Design: "nominal 100 km spinning-tether" with "2g tip acceleration with payload attached"; conductive portions 10 to 50 km for electrodynamic reboost; "Capable of ~75% Earth escape Delta-V"; development time "~10-15 years"; catch mechanisms tested in "several hundred simulated catches" on the ground; about 3 m/day creep of a 100 km tether (ENGINEERING-STUDIED) | Bonometti, Sorensen, Dankanich, Frame, "2006 Status of the MXER Tether Development", AIAA-2006-4521, NTRS 20060047739; Bonometti and Frame, "Space Tethers Programmatic Infusion Opportunities", NTRS 20060004770 | Primary | Flight history (same source): "More than sixteen tether missions have flown since 1967"; SEDS-1 and SEDS-2 full 20 km deployments; TSS-1R 19.6 km conductive; TiPS 4 km on orbit since 1996; SEDS-2 "broke in just 4 days" | Medium. **No momentum-exchange (payload throw) has been flown** |

**Bulk scale verdict from the evidence above (my synthesis, not a source's):**

| Propulsion | Tonnes per year | Kilotonnes per year | Megatonnes per year |
|---|---|---|---|
| Chemical | Yes (flown) | Only with local propellant (ISRU); see F3 for propellant fractions | Only with a local propellant source and short legs (lunar, NEA-to-Earth-orbit) |
| Solar-electric | Yes (Dawn, PPE class; F3 tug arithmetic) | Plausible with tens to hundreds of 100 kW-class tugs (F3) | Needs GW of arrays and propellant at scale; no study found that closes it |
| Nuclear-thermal | Ground-tested only | Studied (Mars campaigns) | No study found |
| Nuclear-electric | Not flown beyond 500 We | Studied at 2.5 to 15 MWe (Open threads) | No study found |
| Solar sail / E-sail | Gram-to-kg demonstrated thrust | E-sail concept claims (unflown) | E-sail 10^6 kg payload needs hypothetical nanotube tethers |
| Mass driver (surface launch) | Not built at scale | SP-428 point design: 650,000 t/yr from the Moon | The same design is in the megatonne class, on paper |
| Tethers | Deployment demonstrated (20 km) | Concept (MXER) | No study found |
| Beamed | Gram scale in air | No study found | No study found |

### F3. Throughput arithmetic (checklist 3)

Sourced anchors first; the arithmetic built on them is DERIVED (D2 to D5 in *Derived figures*).

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| SEP cargo tug, studied case (the anchor for tug counts) | Initial mass 9,750 kg (sized to the 10 t SLS Block 1B co-manifest to TLI). 2 x AEPS: 25 kW to thrusters, total delta-v 3,420 m/s, 363.1 days, **payload 6,940 kg**, final power-to-mass 3.167 W/kg. 3 x AEPS: 37.5 kW, 3,330 m/s, 281.5 days, payload 6,460 kg, 4.734 W/kg. "the savings over a lunar logistics campaign to deliver 26 t of supplies would be nearly one full year" (ENGINEERING-STUDIED) | Cassady et al. 2022, Table 2, NTRS 20220007037 (as F2) | Primary | DERIVED physics check (D3): at Isp 2,890 s the mass ratio for 3.42 km/s is 1.128, matching the 2,810 kg non-payload start mass in scale | High as a study |
| Standard gravity used to convert Isp | g0 = 9.806 65 m/s² (exact) | NIST CODATA, https://physics.nist.gov/cgi-bin/cuu/Value?gn | Primary | n/a | High |
| World xenon supply (the propellant of every flown high-power Hall and ion system above) | "Overall world-wide xenon production (before Ukraine war): ~ linearly growing. Now ca. 65 t / year; growth ca. 2t/year"; "if all ASUs in the world were equipped → ~x5 → ca. 350 t/y"; xenon is a by-product of air separation units serving steel production | Lindner (Max Planck Institute for Nuclear Physics), "Insights into the global xenon market", kton-scale xenon workshop, SLAC, slides dated 25 Oct 2023, https://indico.slac.stanford.edu/event/8015/contributions/7640/attachments/3480/9651/Lindner-kton_workshop.pdf | Primary-grade (expert workshop slides; not peer-reviewed) | Market-report search summaries give 30 to 65 t/yr (secondary; not used) | Medium |
| Argon as an alternative Hall propellant, in flight | SpaceX V2 Mini Starlink argon Hall thrusters: "170 mN of thrust", "2.4 times the thrust and 1.5 times the specific impulse of thrusters on first generation Starlink" (krypton); "never been operated in space" before (as of 27 Feb 2023); about 800 kg satellites (search summary of the same article). Absolute Isp and power not stated (DEMONSTRATED in flight since 2023) | Satellite Today, R. Jewett, "SpaceX Shares Details of Higher Bandwidth V2 Mini Starlink Satellites", 27 Feb 2023, https://www.satellitetoday.com/technology/2023/02/27/spacex-shares-details-of-higher-bandwidth-v2-mini-starlink-satellites/ (re-opened this session) | Secondary (trade press quoting SpaceX) | Spaceflight Now and SpaceNews items in the same search (not opened) | Low-medium (secondary; flagged). Relevant because it shows a flown non-xenon Hall propellant (argon supply was not researched here) |
| 2025 world launch output (scale reference) | 329 orbital launch attempts, 321 reaching orbit or marginal orbit; Falcon 9: 165 launches; Starship: 5; **total payload mass launched 3,193.4 t** (USA 2,712.0 t); cataloged mass in orbit at end of 2025: 16,185 t (13,723 t at end of 2024) | McDowell, "Space Activities in 2025", Rev 1.4, 4 Feb 2026, Tables 1, 7, 13, https://planet4589.org/space/papers/space25.1.4.pdf | Primary (dataset-grade annual report) | Jalopnik (row 45, secondary) gave 165 Falcon 9 and 320 attempts | High (author states about 10% uncertainty on masses) |

**DERIVED results (arithmetic in D2 to D5):**

1. **Propellant fraction (D2).** For the same leg, the fraction of departing mass that is propellant:

| Engine (Isp) | 1.0 km/s | 2.52 km/s (Moon to LEO, aerocaptured) | 3.42 km/s | 5.66 km/s (LEO to LMO, propulsive) | 7.55 km/s (Mercury departure) | 13.07 km/s (0.3 AU departure) | 32.81 km/s (0.1 AU departure) |
|---|---|---|---|---|---|---|---|
| Hydrolox, RS-25 (452.3 s) | 0.20 | 0.43 | 0.54 | 0.72 | 0.82 | 0.95 | 0.999 |
| Nuclear-thermal (~900 s) | 0.11 | 0.25 | 0.32 | 0.47 | 0.58 | 0.77 | 0.98 |
| Hall (2,000 s) | 0.05 | 0.12 | 0.16 | 0.25 | 0.32 | 0.49 | 0.81 |
| AEPS (2,890 s) | 0.035 | 0.085 | 0.11 | 0.18 | 0.23 | 0.37 | 0.69 |
| BepiColombo SEP (4,022 s) | 0.025 | 0.062 | 0.083 | 0.13 | 0.17 | 0.28 | 0.57 |
| Mass-driver reaction engine (Ve 8 km/s) | 0.12 | 0.27 | 0.35 | 0.51 | 0.61 | 0.81 | 0.98 |

   **Chemical cargo from 0.1 AU is physically closed off** (99.9% of departing mass would be propellant, with no tankage).
   Electric propulsion from 0.1 AU still spends 57 to 69% of departing mass as propellant, with no flybys.

2. **SEP tug count, scaled linearly from the Cassady case (D3).** 0.279 t of payload per kW per year (2 x AEPS, one way,
   no empty return leg counted); 0.224 t/kW/yr for the faster 3 x AEPS case. Over a 3.4 km/s leg:

| Cargo per year | Thruster power (2 x AEPS basis) | Tugs of 25 kW | Tugs of 100 kW (X3 class, if flown) |
|---|---|---|---|
| 1,000 t | 3.6 MW | about 143 | about 36 |
| 10,000 t | 36 MW | about 1,430 | about 360 |
| 100,000 t | 358 MW | about 14,300 | about 3,600 |
| 1,000,000 t | 3.6 GW | about 143,000 | about 36,000 |

   Longer legs scale up roughly with delta-v and trip time; return legs (empty) add more.

3. **Propellant demand vs supply (D4).** At Isp 2,890 s over 3.42 km/s, each tonne delivered costs about 0.18 t of
   propellant (counting the tug's own mass). **1,000 t/yr of cargo needs about 180 t/yr of xenon, which is about 2.8 times the
   world's current production (about 65 t/yr) and half of the most the world could make (about 350 t/yr) if every
   air-separation plant were equipped.** Kilotonne-per-year electric trucking therefore needs either a different propellant
   (argon, krypton, or something made at the source) or Earth's whole xenon output. This is a hard bottleneck that
   none of the trucking concepts read here mentions.

4. **Energy per kilogram (D5).** Ideal specific energy (no losses): Earth surface to 400 km orbit 33.1 MJ/kg; lunar surface
   to escape 2.82 MJ/kg (the SP-428 launcher gives each kilogram 2.88 MJ); Mercury surface to escape 9.03 MJ/kg; Venus at 55 km
   to circular orbit 26.6 MJ/kg (kinetic) and to escape 53.2 MJ/kg; orbital speed at 10 km above Uranus, Saturn, Jupiter:
   113, 325, 878 MJ/kg. Heliocentric circular-orbit energy changes: 0.1 AU to 1 AU, +3,992 MJ/kg; 0.3 AU to 1 AU, +1,035 MJ/kg;
   0.5 AU to 1 AU, +444 MJ/kg; 2.7 AU to 1 AU, -279 MJ/kg (energy must be shed, by propulsion or aerocapture). **Raising one kg
   from a 0.1 AU orbit to Earth's orbit takes about 120 times the energy of launching it from Earth's surface to LEO.**

5. **Power productivity (D5).** The SP-428 lunar mass driver moves about 5,200 t of cargo per MW-year (650,000 t/yr over
   125 MW) against about 280 t per MW-year for a xenon SEP tug. The mass driver does not throw away reaction mass, but it
   only works from an airless surface with low escape speed.

6. **Scale against today (D5).** 1 Mt/yr is about 313 times the whole world's 2025 launched payload mass (3,193 t),
   and about 62 times the total cataloged mass now in Earth orbit (16,185 t).

### F4. Infrastructure that bulk transport needs (checklist 4)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| **Propellant depot in LEO, the first real one being built** | Starship HLS plan: a Starship "storage depot" launched to LEO, "followed by more than 10 Starship tankers carrying propellant"; "SpaceX is targeting to launch one tanker flight every 6 days"; tankers from Starbase (Texas) and Kennedy; "SpaceX has yet to demonstrate the required 12- to 24-day turnover of its launch pad"; cryogenic transfer technologies "are entirely new and have never been done vehicle-to-vehicle"; Flight 3 transferred propellant between two tanks inside one Starship; vehicle-to-vehicle demonstration planned for 2026 on Starship version 3; 11 integrated flight tests since April 2023; Blue Origin's plan also uses a LEO "transporter" acting as a depot plus refuelers (ENGINEERING-STUDIED; intra-vehicle transfer DEMONSTRATED) | NASA Office of Inspector General, "NASA's Management of the Human Landing System Contracts", IG-26-004, 11 Mar 2026, https://oig.nasa.gov/wp-content/uploads/2026/03/final-report-ig-26-004-nasas-management-of-the-human-landing-system-contracts.pdf | Primary | SpaceDaily (row 52, secondary): not attempted as of Flight 13, 24 Jul 2026 | High for plan and status as of March 2026 |
| Cryogenic boil-off control | OIG footnote: "Cryocoolers act like heat exchangers for large propellant tanks to mitigate boiloff" (no rate given) | IG-26-004 (as above), fn. 25 | Primary | none | Low (no numbers; Open threads) |
| **Electric cargo tug** | See F3: 9.75 t initial, 25 to 37.5 kW, 281 to 363 days, 6.5 to 6.9 t delivered TLI to NRHO; PPE is refuelable with xenon in lunar orbit | Cassady et al. 2022 (F2, F3) | Primary | n/a | High as a study |
| **Mass catcher (receiver for a lunar mass driver)** | Located at Earth-Moon L2; payloads detected by radar "10 s before arrival, that is, 2000 m away"; incoming "200 m/s"; "60 such rigs on a single catcher"; 60 s cycle; one catcher can "catch 0.32 X 10^6 t/yr on a 100 percent duty cycle"; goal "catch 11 X 10^6 t in 10 yr", needing "3.5 catchers on the average" operational, "5 catchers at L2" installed (ENGINEERING-STUDIED) | NASA SP-413, "Space Settlements: A Design Study" (1975 Summer Study), Appendix G "The Mass Catcher", https://nss.org/settlement/nasa/75SummerStudy/5appendG.html | Primary (NASA SP, NSS transcription) | SP-428 III-3 launcher (F2) is of the same order (650,000 t/yr) | Medium (1975 design; never built) |
| **Momentum-exchange tether facility** | 100 km rotating tether, 2 g tip, electrodynamic reboost section 10 to 50 km; ground catch tests only (F2) | Bonometti et al. 2006 (F2) | Primary | n/a | Medium |
| **Aerobraking (bound orbit, many passes): flown** | "first demonstrated in the 1990s by the Magellan spacecraft at Venus and has been used repeatedly since"; MRO began aerobraking at Mars in March 2006, about 6 months, "over 400 aeroheating drag passes" (DEMONSTRATED) | Spilker et al., "An Assessment of Aerocapture and Applications to Future Missions", JPL D-97058, 13 Feb 2016, https://solarsystem.nasa.gov/system/downloadable_items/153_AerocapRpt20D1.pdf; Amundsen, Dec, Gasbarre, NTRS 20070030304 (2007) | Primary | MRO propellant saved (about 600 kg) found only in news summaries; not used | High |
| **Aerocapture (single pass from hyperbolic arrival): not flown** | "aerocapture is not new but has yet to be implemented on a space flight mission"; delivered-payload gain "about 15% at Mars, to more than 200% at Titan and Uranus, to more than 800% at Neptune" (NASA ASAT studies); team consensus: "technologically ready to use aerocapture at Titan, Mars, and possibly Venus now", "no flight demonstration is needed" (ENGINEERING-STUDIED) | Spilker et al. 2016 (as above) | Primary | none found for a post-2016 flight (Open threads) | High for status as of 2016 |
| **Processing node at the source (asteroid)** | "an equipment mass of 5 tonnes could process 1000 tonnes of asteroidal regolith per day, to produce 100 tonnes of volatiles per day, giving 10,000 tonnes of product in a 3-months' mining season" (assumes 200 kg/day processed per kg equipment and 10% recoverable water) (ENGINEERING-STUDIED, order-of-magnitude) | Sonter 1998 (F1) | Primary | Hein et al. 2018 assume 2.3 x 10^-4 kg/s per kg (about 20 kg/day per kg), 10 times lower (Conflicts C3) | Low to medium |
| **Processing node (retrieval mission)** | Processing equipment "560 tons"; "21-man team"; outputs from the 1977 HB scenario: water "50,000 metric tons", free metals "100,000 metric tons", carbon compounds "20,000 metric tons" (ENGINEERING-STUDIED, 1977) | SP-428 IV-2 (F1) | Primary | none | Medium-low (1977) |
| **Launch windows: synodic periods** | Mercury 115.88 d, Venus 583.92 d, Mars 779.94 d (NSSDC, F1). DERIVED (D6) for circular orbits: 0.1 AU source, windows to Earth every 11.9 d, to Mars every 11.7 d; 0.3 AU: 71.8 d / 65.8 d; 0.5 AU: 199.8 d / 159.0 d; main belt 2.2 / 2.7 / 3.2 AU: to Earth every 1.44 / 1.29 / 1.21 yr, **to Mars every 4.44 / 3.27 / 2.80 yr**. Sonter: NEA low-energy opportunities "at approx 2-yearly intervals" and "long synodic periods militate against multiple-return mining missions" | NSSDC; Sonter 1998; DERIVED D6 | Primary | DERIVED Mercury 115.9 d and Earth-Mars 779.9 d reproduce NSSDC (115.88, 779.94) | High |
| **Communications blackout near the Sun** | Mars missions stop commanding when "the sun will be within two degrees of Mars in Earth's sky" (about two weeks, every two years). DERIVED (D7): a source on a circular 0.1 AU orbit is never more than 5.7 deg from the Sun as seen from Earth and spends about 23% of each 11.9-day cycle within 2 deg; 0.3 AU: max 17.5 deg, about 7%; Mercury's distance (0.387 AU): max 22.8 deg, about 6%; 0.5 AU: about 4% (coplanar) | LASP/MAVEN, "Mars missions to pause commanding in June due to Sun", 3 Jun 2015, https://lasp.colorado.edu/maven/2015/06/03/mars-missions-to-pause-commanding-in-june-due-to-sun/; JPL news, 28 Sep 2021 (moratorium Oct 2 to 16, 2021, "every two years") | Primary (mission team pages) | JPL page did not state the angle | High for the Mars rule; the 2 deg threshold is for Mars-distance links and may differ for other links |
| **Light-time delay** | 1 AU = 499.0 s one way (DERIVED from the IAU AU and c). Source to Earth one-way: from 0.1 AU, 7.5 to 9.1 min; from the main belt at 2.7 AU, 14.1 to 30.8 min; Earth-Mars 4.4 min (0.524 AU, closest for circular orbits) to 21 min (2.524 AU) | DERIVED D7 from JPL SSD AU and c = 299,792,458 m/s (SI defined value) | Derived | n/a | High |

**Infrastructure reading (synthesis):** every bulk scheme read here needs a **receiver** at the destination
(a depot, a catcher, an aerobrake, or a tether that must absorb momentum) and a **local propellant source**
(lunar or asteroid volatiles, atmospheric CO2 at Venus, hydrogen at a gas giant). The only receiver type
demonstrated at all is aerobraking (many slow passes; months per spacecraft). The receivers that bulk volumes
need (catchers, depots, tether catches) exist only on paper or in ground tests. Main-belt cargo to **Mars**
departs in clusters about every 3 to 4.4 years, which is the clearest case of synodic bunching in the set.

### F5. Launch cost, cadence, and the cost of non-Earth material (checklist 5)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Cost per kg to LEO over time (dataset 1) | 2018 dollars, per kg to LEO: Saturn V (1968) 5.20 k (140,000 kg, $728 M); Shuttle 61.72 k (27,500 kg, $1,697 M); Falcon 9 2.72 k (22,800 kg, $62 M, advertised); Falcon Heavy 1.41 k (63,800 kg, $90 M, advertised). 1970 to 2000 average $18.5 k/kg, typical range $10 to 32 k/kg; Vanguard about 170 times Saturn V; early systems up to about $1,000 k/kg (DEMONSTRATED prices) | Jones (NASA Ames), "The Recent Large Reduction in Space Launch Cost", ICES-2018-81, NTRS 20200001093, Table A2 and Sec. II | Primary | Dataset 2 (next row) | High; note these are list prices at maximum expendable payload |
| Cost per kg to LEO over time (dataset 2) | Constant 2021 US$, by year of first successful launch: Space Shuttle (1981) 65,400; Saturn V (1967) 5,400; Atlas V (2002) 8,100; Falcon 9 (2010) 2,600; Electron (2018) 23,100; **Falcon Heavy (2018) 1,500, the lowest in the set**; 61 rows, 1962 to 2019; small < 2,000 kg, medium 2,000 to 20,000 kg, heavy > 20,000 kg | CSIS Aerospace Security Project (2022), via Our World in Data grapher "Cost of space launches to low Earth orbit", CSV and metadata (last updated 4 Mar 2025), https://ourworldindata.org/grapher/cost-space-launches-low-earth-orbit | Primary (dataset; OWID processing "minor") | Jones (above): same ordering; differences from base year (2018 vs 2021 dollars) | High |
| 2025 cadence and mass | 329 attempts / 321 to orbit; Falcon 9 165 launches; Starship 5 test flights (3 marginal orbit); 3,193.4 t of payload launched worldwide in 2025 | McDowell 2026 (F3) | Primary | Jalopnik (secondary) | High |
| Next-stage assumptions (NASA, not a vendor quote) | Starship assumed to carry 100 t to LEO; a Starship with 100 t "requires 12 refueling launches in LEO to continue to GEO"; baseline $100 M per launch ($1,000/kg; $850/kg with a 15% block discount); low case $50 M ($500/kg; $425/kg); trend case: launch cost per kg fell 36% from 2013 to 2022, "today's lowest price is $1,500/kg"; if the trend continues, "$615/kg in 2040"; propellant cost assumed $0.20/kg; Starship modeled at 355 s, 14.7 MN, 120 t fuel, 100 t dry; "we assume that no cryogenic boil off occurs in orbit" (ENGINEERING-STUDIED assumptions) | Rodgers et al., NASA Office of Technology, Policy, and Strategy, "Space-Based Solar Power", 11 Jan 2024, Report ID 20230018600, https://www.nasa.gov/wp-content/uploads/2024/01/otps-sbsp-report-final-tagged-approved-1-8-24-tagged-v2.pdf | Primary (NASA report), but the Starship figures are **assumptions** | OIG IG-26-004: HLS needs a depot plus "more than 10" tankers, consistent with "12 refueling launches"; SpaceX's own page could not be read (row 113) | Medium (assumed, not demonstrated) |
| Asteroid material to Earth orbit: 1977 cost | "For capture of a 10^6-ton asteroid, estimated total program costs are from $12-14 billion or about $24/kg of captured mass. If RDT & E are excluded, the captured mass cost reduces to about $4/kg"; comparison: delivering the same mass of terrestrial material to GSO "about $355/kg"; "A 100-MW mass driver, assembled in space with about 50 Space Shuttle flights, would retrieve about 22 percent of a 200-m-diameter (1X10^7-metric ton) asteroid through a velocity increment ΔV of 3 km/sec in 5 years"; return delta-v 5 km/s with a 10^6 t fragment "enables 532,000 tons to be brought to Earth orbit" (ENGINEERING-STUDIED, 1977 dollars and Shuttle-era cost assumptions) | O'Leary et al., SP-428 IV-2 (F1) | Primary | none modern found with the same scope | Low for the dollar figures (assumed Shuttle economics that did not happen; Jones gives Shuttle at $61.7 k/kg in 2018 dollars) |
| Asteroid retrieval, 2012 study | "NEAs with a nominal diameter of roughly 7 m corresponding to masses in the range of 250,000 kg to 1,000,000 kg"; "40-kW solar electric propulsion system"; "single Atlas V-class launch vehicle"; return to "high-Earth orbit" (ENGINEERING-STUDIED; what became of the follow-on mission was not checked this session) | Brophy, Friedman, Culick, "Asteroid retrieval feasibility", Keck Institute for Space Studies, March 2012, Caltech Authors record kqeqz-18608 (abstract; full report not obtainable, rows 68, 114) | Primary (abstract) | none | Medium |
| Asteroid mining economics, 1998 | "A teleoperated miner for return of volatiles from NEAs is economically feasible, using present technology, with an initial market of about 1000 tonnes per year"; LEO materials market "could easily exceed 1000 tonnes per year by 2010" (did not happen; see McDowell); mass payback "factors above 100 are the initial aim"; launch-price expectation then: "from the present $10,000/kg down to something like $500/kg" (ENGINEERING-STUDIED) | Sonter 1998 (F1) | Primary | Hein et al. 2018 (next row) | Low for the market forecast; medium for the method |
| Asteroid mining economics, 2018 | Water case inputs: price of water in space $20,000/kg; transport to/from asteroid $35,000/kg; 150 kg spacecraft; throughput 2.3 x 10^-4 kg/s per kg of equipment; 5% of processed material refined; 100-day mining; conservative case breakeven 5.9 years, optimistic 0.26 years. Conclusion: "mining volatiles and supplying them to cis-lunar orbit seems to be economically viable without the development of mining and refining processes with very high throughput rates"; "platinum mining requires very high throughput rates, which could be difficult to achieve" (ENGINEERING-STUDIED) | Hein, Matheson, Fries (Initiative for Interstellar Studies), "A Techno-Economic Analysis of Asteroid Mining", IAC-18 (2018), arXiv:1810.03836, Table 1 and Sec. 6 | Primary (conference paper, preprint) | Sonter (above) | Medium-low (assumed prices) |
| Lunar propellant vs Earth-launched propellant | Prior techno-economic analyses "had disagreed"; the deciding factors are the transport "gear ratio" for capital and the production mass ratio φ (product mass per unit of capital mass); competitive when φ ≳ 35; tent sublimation (Kornuta et al. 2019, Sowers) estimated φ = 441.8 and 534; "Lunar-derived rocket propellant can outcompete rocket propellant launched from Earth, no matter how low launch costs go"; Sowers' fully commercial IRR 8.84% vs 21.7% thought needed; remaining challenge "proof of operability for years in the lunar environment and especially the dust" (ENGINEERING-STUDIED) | Metzger (UCF Florida Space Institute), "Economics of In-Space Industry and Competitiveness of Lunar-Derived Rocket Propellant", arXiv:2303.09011 (2023 preprint) | Primary (preprint) | Kornuta et al. 2019 (REACH) not opened (Open threads) | Medium |

### F6. What the cargo is, and how each class is packaged and shipped (checklist 6)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| **Rock and regolith, mass-driver packaging (1975 design)** | Payload is "sintered lunar material, resembling a cinder block" carried in a bucket of "under 10 kg"; buckets decelerated (possibly by "regenerative braking") and returned to the loading zone; track about 10 km (coarse 10 km, fine 1 km, drift 1 km as transcribed); "288 m/s^2" coarse acceleration; "maximum throughput would be 2500 kg/s"; release-velocity errors "less than 10^-5 m/s" (ENGINEERING-STUDIED) | NASA SP-413, Appendix F (Chapter 5) "The Mass Driver", https://nss.org/settlement/nasa/75SummerStudy/5appendF.html | Primary (NSS transcription; "l0 km" in the transcription read as 10 km) | SP-428 III-3 (1977) is a different, shorter design (Conflicts C4) | Medium |
| Rock and regolith, flight to the catcher | Moon to L2: "transfer times under 100 hr" at "approximately 200 m/s" arrival, or "over 200 hr" at about 100 m/s; at L2 the catcher stores the material and later moves it onward (ENGINEERING-STUDIED) | SP-413 Appendix H, https://nss.org/settlement/nasa/75SummerStudy/5appendH.html; Appendix G (F4) | Primary | none | Medium |
| Rock and regolith: 1977 launcher payload | 10.5 kg per launch at 4 Hz, 0.431 m caliber (F2) | SP-428 III-3 | Primary | SP-413 (above) | Medium |
| **Water and other volatiles** | Asteroid regolith is heated and the vapor collected: "collector, soil pressurizer, grinding mill and heater, solid-vapour separator, volatiles collector bag, tailings disposal, and gas cleaner / reheater / repressurizer"; recoverable water "cannot be assumed to be greater than about 10% by mass"; volatiles can serve as the return trip's reaction mass, giving "Mass multiplication factors above 100" as an aim (ENGINEERING-STUDIED) | Sonter 1998 (F1) | Primary | Hein et al. 2018 use 5% refined fraction | Medium-low |
| Volatiles as the product that pays first | Hein et al.: water to cislunar orbit viable "without ... very high throughput rates"; Metzger: lunar propellant competitive even in LEO if production mass ratio is at least about 35 (F5) | Hein 2018; Metzger 2023 | Primary | each other | Medium |
| **Metal** | Sonter lists process options "(i) in-situ fluidization; (ii) mechanical collection and thermal or magnetic separation; (iii) carbonyl process"; SP-428 IV-2's 1977 HB case yields "Free metals: 100,000 metric tons" alongside water and carbon compounds (ENGINEERING-STUDIED) | Sonter 1998; SP-428 IV-2 | Primary | none | Low (no packaging figures found) |
| **Hydrogen and helium gas from a giant planet** | Hydrogen is "liquefied and used as rocket propellant for the ascent to orbit"; helium-3 "separated from the atmospheric hydrogen and helium (4He) captured, liquefied and stored as a payload"; earlier designs: aerospacecraft (ASC) carrying "a 1 MT payload, of which 0.5 MT was the cryogenic 3He or Deuterium"; ASC fixed mass "300,000 kg" plus 0.02 to 0.10 kg per kg of propellant; to deliver 5,000 t of fuel, "a total of 10,000 ASC flights were required", fleet mass "approximately 100,000 MT" (100-flight life); with 100 t payloads, fleet mass "13,500 MT" (10-flight life); storage in low orbit "generally not desirable", so a small moon was chosen as base (SPECULATIVE; gas-core engines unbuilt) | Palaszewski, NTRS 20205004479 (AIAA JPC 2020) | Primary | Palaszewski 2015 capture-rate case (F1b) | Low (depends on an unbuilt engine) |
| Can bulk gas be shipped up out of a deep well? | From the 2020 case: 1 t of payload per flight against a 300 t ASC dry mass plus its hydrogen load (148 to 270 t per fill in the 2015 case); orbital speed 41.9 (Jupiter), 25.5 (Saturn), 15.1 (Uranus) km/s at 10 km altitude (F1b) | Palaszewski 2015, 2016, 2020 | Primary | DERIVED D5: 878 / 325 / 113 MJ/kg kinetic energy at orbital speed | Medium. **Read plainly: shipping gas out of a giant planet is only considered at the ice giants, and only for fusion fuel worth its weight, not as bulk hydrogen** |
| **Cryogens in storage (ground reference only)** | Large ground liquid-hydrogen sphere at KSC: normal evaporation rate "0.09 percent per day" (2007 log, 26% full) and "0.10 percent per day, or 216 L per day" after an insulation retrofit (glass bubbles) | NTRS 20130011367 (KSC liquid hydrogen storage, text extracted) | Primary | Search summaries: <0.05%/day for the newest KSC tank (not opened) | Medium for ground tanks; **no in-orbit rate was obtained** (Open threads). NASA's SBSP study simply assumed zero boil-off (F5) |

**Reading by class (synthesis):** rock and metal are the easiest cargo to throw: they need no tank, survive high
acceleration (the designs above use 288 m/s² to 10,000 m/s²) and can be caught as loose material. Water ships as ice or
liquid in simple tanks and doubles as propellant. Hydrogen and helium need cryogenic tanks whose loss rate in orbit
was not found as a sourced number. From a giant planet's atmosphere, almost all the lifted mass is the vehicle and
its propellant, which is why the only study found ships fusion fuel, not bulk gas.

### F7. Minimum fleet and facilities for a first useful tonnage, and for a hundred-fold larger one (checklist 7)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| First useful tonnage, asteroid volatiles | One teleoperated miner, processing plant under 5 t, returning 1,000 t to LEO; solar thermal steam rocket, solar-PV arcjet, or solar-PV mass driver; market "about 1000 tonnes per year" (ENGINEERING-STUDIED) | Sonter 1998 | Primary | Hein 2018: one 150 kg spacecraft in the reference case | Low-medium |
| First useful tonnage, lunar cargo by SEP | One 9.75 t SEP tug (25 to 37.5 kW) moves 6.5 to 6.9 t per trip, TLI to NRHO, one trip a year; a 26 t logistics campaign (ENGINEERING-STUDIED) | Cassady et al. 2022 | Primary | n/a | High as a study |
| 100-fold larger, asteroid retrieval by mass driver (1977) | A 100 MW mass driver, about 50 Shuttle flights to assemble, retrieves 22% of a 1 x 10^7 t asteroid over 5 years (about 2.2 million t, about 440,000 t/yr averaged); or 532,000 t to Earth orbit from a 10^6 t fragment; processing plant 560 t with a crew of 21 (ENGINEERING-STUDIED) | SP-428 IV-2 | Primary | DERIVED average rate is my arithmetic (22% x 10^7 t / 5 yr) | Low-medium (1977) |
| Megatonne class, lunar mass driver plus catchers (1975 to 1977) | One lunar launcher: 650,000 t/yr, 125 MW, 3,130 t machine (SP-428). Receivers: 5 catchers at L2 (3.5 operating on average) to catch 11 million t in 10 years, 0.32 million t/yr each (SP-413) (ENGINEERING-STUDIED) | SP-428 III-3; SP-413 App. G | Primary | each other, order of magnitude | Low-medium |
| Giant-planet fusion fuel | 5,000 t of fuel: 10,000 ASC flights; 10 to 100 ASCs; fleet about 100,000 t; or 13,500 t with 100 t payloads (SPECULATIVE) | Palaszewski 2020 | Primary | none | Low |
| SEP fleet arithmetic (my scaling, not a study) | 1,000 t/yr over a 3.4 km/s leg: about 3.6 MW and 143 tugs of 25 kW, about 180 t/yr of xenon (2.8 times world output); 100,000 t/yr: about 360 MW and 14,300 such tugs (F3, D3) | DERIVED from Cassady 2022 and Lindner 2023 | Derived | n/a | Medium for scale; it assumes linear scaling and ignores return legs |

**Not found:** no study was found that sizes a fleet for **near-Sun (0.1 to 0.5 AU) material shipped to Earth or Mars
orbit** at any tonnage. The delta-v (F1) and energy (F3) figures suggest why: at 0.1 AU, leaving costs about 33 km/s
before flybys.

## Conflicts

- **C1. Earth-to-Mercury direct transfer: "about 16 km/s" (Jehn and Schoenmaekers 2014) vs 11.2 km/s or 15.1 km/s (D1).**
  The paper gives no definition. 15.1 km/s is the sum of departure and arrival hyperbolic excess speeds for circular,
  coplanar orbits; 11.2 km/s is the impulsive burn total from a 400 km LEO into a 200 km circular Mercury orbit (Oberth
  benefit at both ends). Mercury's real orbit (e = 0.206, i = 7 deg) raises both. Palaszewski 2017 uses a crewed case of
  5.2 + 10.9 km/s (Earth departure + Mercury arrival). Likely cause: different definitions (v-infinity sum vs burns) and
  real vs idealized orbits. Not resolved; the D1 numbers are lower bounds.
- **C2. Venus escape speed: 10.46 km/s (Landis and Oleson 2024) vs 10.36 km/s (NSSDC, 11 Jan 2024).** D1 from NSSDC
  GM and radius gives 10.36 at the surface. Landis may have used a different GM or radius; not resolved.
- **C3. Asteroid-processing throughput per kg of equipment: about 200 kg/day per kg (Sonter 1998) vs 2.3 x 10^-4 kg/s
  per kg = about 20 kg/day per kg (Hein et al. 2018).** A factor of ten. Sonter's is an estimate from terrestrial
  solids-handling equipment; Hein's comes from a cited parametric model. Both are unvalidated in space.
- **C4. Lunar mass driver point designs: SP-413 (1975) vs SP-428 III-3 (1977).** SP-413: about 10 km of track,
  288 m/s² coarse acceleration, maximum throughput 2,500 kg/s, buckets under 10 kg. SP-428: 488 m, 10,000 m/s² (1,000 g),
  42 kg/s, 10.5 kg payloads at 4 Hz, 125 MW. These are two successive designs; the 1977 one assumed much higher
  acceleration and is far shorter. Both reach 2,400 m/s.
- **C5. "Smallest capture Δv ~76 km s^-1" for 2000 SG344 (Jedicke et al. 2019 preprint, arXiv:1905.13457v1, line
  1005 of the extracted text).** A capture delta-v of 76 km/s is physically absurd for an object that NHATS lists at
  3.549 km/s for a full round trip from LEO (F1). Almost certainly "76 m s^-1"; the same sentence cites capture of
  NEOs at "< 1.8 km s^-1" relative speed via lunar gravity assists (Bao et al. 2015). Recorded as a typo in the source; the
  76 figure is not used.
- **C6. Launch cost per kg: Jones (2018 dollars) vs CSIS/OWID (2021 dollars).** Falcon Heavy $1.41 k vs $1,500;
  Falcon 9 $2.72 k vs $2,600; Saturn V $5.20 k vs $5,400; Shuttle $61.72 k vs $65,400. The base year accounts for most of it;
  the Falcon 9 order is reversed (2,720 vs 2,600) despite later dollars, so the payload or price basis also differs.
  Both are list price at maximum expendable payload, not cost to the operator.
- **C7. Prior lunar-propellant economic studies disagree with one another** (Metzger 2023 says so explicitly and
  attributes it to high transport "gear ratio" architectures and low production mass ratios in some studies). Not
  resolved here; recorded so the disagreement is not hidden.
- **C8. Earth and Mars fact-sheet dates moved.** Row 23 (earlier run) recorded all NSSDC sheets as 11 Jan 2024; on
  re-opening, Earth reads 15 Nov 2024 and Mars 19 May 2025. Values used here are those read this session.

## Derived figures

All derived numbers use the constants in F1 (JPL SSD DE440, NSSDC) and g0 = 9.806 65 m/s² (NIST). Scripts were run
locally; the formulas are given so anyone can repeat them.

- **D1. Hohmann transfers (F1 table).** Circular speed v = sqrt(GM/r). Transfer semimajor axis a = (r1 + r2)/2.
  Speeds on the transfer ellipse v_t = sqrt(GM_sun (2/r - 1/a)). Heliocentric burn or v-infinity at each end =
  |v_t - v_circ|. Burn from or into a low orbit of radius r_p about a body: dv = sqrt(v_inf² + 2 GM_body / r_p) -
  sqrt(GM_body / r_p) (Oberth effect included). Time = pi sqrt(a³ / GM_sun). Example, 0.1 AU to Earth: r1 =
  1.496 x 10^7 km, v_circ = 94.19 km/s, perihelion speed on the transfer 127.0 km/s, so dv = 32.81 km/s; arrival
  v-inf 17.08 km/s; capture into 400 km LEO = sqrt(17.08² + 2 x 398,600.4/6,771) - sqrt(398,600.4/6,771) = 12.57 km/s;
  time 74 days. Moon: v-inf relative to the Moon on a 384,400 x 6,771 km geocentric ellipse = 1.022 - 0.189 = 0.833 km/s;
  departure from the surface sqrt(0.833² + 2.376²) = 2.52 km/s (no orbit stop, no rotation). Venus: circular speed and
  escape speed at r = 6,051.8 + h km. Mercury check: Earth to Mercury v-inf 7.55 (depart) and 7.53 (arrive) km/s; LEO
  departure 5.55 km/s + low-Mercury-orbit capture 5.68 km/s = 11.22 km/s.
- **D2. Propellant fraction (F3).** m_prop / m_0 = 1 - exp(-dv / (Isp g0)). Example: 3.42 km/s at 2,890 s: ve = 28.34 km/s,
  1 - exp(-0.1207) = 0.114.
- **D3. SEP tug scaling (F3, F7).** Payload per kW-year = 6,940 kg / 25 kW x (365.25 / 363.1) = 0.279 t/kW/yr. Power for
  M t/yr = M / 0.279 kW. Tug count = power / 25 kW. Linear scaling assumed; no return leg, no downtime, no degradation.
  Check from physics: mass ratio exp(3,420 / 28,341) = 1.128; jet energy per kg propellant at 67% efficiency
  0.5 x 28,341² / 0.67 = 599 MJ.
- **D4. Xenon demand (F3).** Propellant per tonne delivered = (mass ratio - 1) x (initial mass / payload) =
  0.1283 x (9,750 / 6,940) = 0.180 t/t. For 1,000 t/yr: 180 t/yr, vs about 65 t/yr world production (Lindner 2023).
  Crude: it assumes the Cassady tug's mass proportions at all scales.
- **D5. Energies (F3).** Earth surface to 400 km circular, non-rotating: 0.5 v_circ² + GM(1/R - 1/r) = 29.4 + 3.7 =
  33.1 MJ/kg. Lunar escape GM/R = 2.82 MJ/kg. Mercury surface escape 9.03 MJ/kg; escape speed sqrt(2 x 22,032 / 2,439.7)
  = 4.25 km/s. Venus at 55 km: circular kinetic 0.5 GM/r = 26.6 MJ/kg; escape GM/r = 53.2 MJ/kg. Giant planets: 0.5 v² at
  Palaszewski's 10 km orbital speeds. Heliocentric circular-orbit energy change ΔE = GM_sun/2 (1/r1 - 1/r2). Mass-driver
  check: 0.5 x 2,400² x 42 kg/s = 121 MW vs 125 MW stated; 650,000 t / 42 kg/s = 179 days of firing a year.
  Mass-driver productivity 650,000 / 125 = 5,200 t per MW-yr; SEP 279 t per MW-yr.
- **D6. Synodic periods (F4).** Orbital period T = 2 pi sqrt(a³ / GM_sun); synodic S = 1 / |1/T1 - 1/T2|. Validation:
  Mercury-Earth 115.9 d and Earth-Mars 779.9 d reproduce NSSDC's 115.88 and 779.94 d.
- **D7. Sun-angle and light time (F4).** For a coplanar circular source orbit of radius a (AU) seen from Earth at 1 AU,
  the Sun-object angle was sampled uniformly over relative phase (200,000 points); maximum = arcsin(a) (5.74 deg at 0.1 AU).
  Fraction of phase within 2 deg: 0.227 (0.1 AU), 0.074 (0.3), 0.057 (0.387), 0.044 (0.5). Light time = distance / c,
  c = 299,792,458 m/s (exact by SI definition); 1 AU = 499.0 s.

## Constraints for any inhabitant

These apply to anyone living at a transport node (a depot, a catcher, a tug base, a launcher site), whoever lives there.

- **Shipping comes in pulses, not a steady stream.** Windows from the main belt to Mars recur every 2.8 to 4.4 years, to
  Earth every 1.2 to 1.4 years; Earth-Mars every 780 days; NEAs about every 2 years (F4, D6). A receiving node sees
  long gaps and then a rush.
- **Trips are long.** Hohmann legs are 3 months (Mercury, near-Sun orbits) to 1.8 years (outer main belt to Mars) (D1). Low-thrust
  tugs take about a year for a 3.4 km/s leg (F3). Electric routes from Mercury with flybys take years (BepiColombo 7.5 years).
- **Remote operation has built-in lag.** One-way light time 7.5 to 9 min from a 0.1 AU source, 14 to 31 min from the
  main belt, 4 to 21 min Earth-Mars (F4). Nothing at a source can be steered live from Earth or Mars.
- **Near-Sun links black out often.** A 0.1 AU source sits within 2 deg of the Sun as seen from Earth about 23% of the time,
  for about 2.7 days of every 11.9-day cycle, the angle at which Mars missions stop commanding (F4, D7). Local
  autonomy or relays off the Earth-Sun line would be needed.
- **Mass-driver cargo cannot carry anything fragile, a human-shaped machine included.** The launcher designs use
  288 m/s² (about 29 g) to 10,000 m/s² (about 1,000 g) (F2, F6). A human-shaped machine with joints and mass would have
  to travel by tug or rocket, not by the cargo stream.
- **Catching cargo is a hazard and a full-time job.** The SP-413 catcher receives 10 kg payloads at 200 m/s, one rig
  cycle every 60 s, 60 rigs per catcher (F4). Anyone near a receiver lives beside a continuous stream of incoming
  projectiles with a 2 km, 10 s warning distance.
- **Propellant is the binding resource.** Earth's xenon cannot supply kilotonne-a-year electric trucking (F3, D4); bulk
  transport needs propellant made where the cargo is (water, CO2-derived CO/O2, hydrogen) or a different electric propellant.
- **Leaving Venus's clouds is as hard as leaving Earth's surface** (about 9 km/s; 1,800 kg vehicle for 10 kg to orbit in a
  NIAC study) (F1b). A cloud-level settlement can export almost nothing by rocket.
- **Giant-planet atmospheres trap their gas.** 15 to 42 km/s orbital speed at 10 km altitude (F1b); the one design found
  needs a 300 t vehicle to lift 1 t of fusion fuel per flight (F6).
- **Receivers that slow cargo by atmosphere are proven only in the slow form.** Aerobraking takes months and hundreds of passes
  (MRO: about 400 passes, about 6 months); single-pass aerocapture has never flown (F4).

## Candidate handwaves

Flagged, not accepted. The developer decides.

- **HW-1. Any bulk export from near-Sun orbits (0.1 to 0.3 AU) to Earth or Mars.** 13 to 35 km/s to depart before flybys,
  20 to 48 km/s all-propulsive, about 1,000 to 4,000 MJ/kg of orbital energy (D1, D5); no fleet study found (F7). Plausible
  only with flyby chains over years or with propellantless sails (unflown at cargo scale). Treating it as routine bulk
  trucking would need physics or economics bent.
- **HW-2. Bulk hydrogen or helium export from Jupiter or Saturn's atmospheres.** 25.5 to 41.9 km/s just to orbit (F1b);
  the only study depends on gas-core nuclear rockets that have never been built and calls Saturn mining extremely complex.
- **HW-3. Kilotonne-to-megatonne electric propulsion on xenon.** Exceeds world xenon supply at about 1,000 t/yr of cargo (D4).
- **HW-4. Routine single-pass aerocapture of cargo at Earth or Mars.** Never flown (as of the 2016 assessment); called
  ready by that study, but no flight record.
- **HW-5. Mass-catchers, propellant depots and tether catches at scale.** Catchers and momentum-exchange tethers exist
  only as studies and ground tests; vehicle-to-vehicle cryogenic transfer had not been done as of March 2026 (F4).
- **HW-6. E-sail cargo hauling (10^6 kg payloads).** Needs hypothetical carbon-nanotube tethers (≥10 GPa); the only
  flight test failed to deploy its 10 m tether (F2).
- **HW-7. Cryogens stored for months in orbit without loss.** A NASA study simply assumed zero boil-off; no in-orbit
  rate was found here (F5, F6).

## Open threads

- **Near-Sun cargo transport study.** No paper found that sizes transport of material from 0.1 to 0.5 AU to Earth or
  Mars orbit. Next: search for solar-sail cargo from inner orbits (sail thrust scales as 1/r², a physics relation
  not sourced here), "sundiver" or "solar photon thruster" cargo, and the starlifting sibling file's sources.
- **Flyby-assisted cargo routes from Mercury or near-Sun orbits.** Only spacecraft (MESSENGER, BepiColombo) found.
  Next: Langevin and Yen (cited by Jehn 2014) for systematic Mercury return trajectories.
- **Mercurian mass driver.** Not found (rows 132, 133). Next: read the rest of the science.gov topic page (714,658
  characters unread), the SSI Space Manufacturing proceedings index, and Mercury-industrialization papers.
- **In-orbit cryogenic boil-off rates** (liquid hydrogen, oxygen, methane): no primary in-orbit figure found (rows 127 to
  129). Next: NASA CFM Technology Roadmap, Centaur extended-coast data, COLD-SAT / CPST reports on NTRS.
- **Starship payload and cost from SpaceX directly.** SpaceX pages not readable by the tools (rows 41, 113). NASA OTPS
  assumptions (100 t, $50 to 100 M) are used instead and labeled as assumptions.
- **Starship vehicle-to-vehicle propellant transfer outcome in 2026.** OIG (March 2026) says planned for 2026; a secondary
  source says not attempted as of 24 Jul 2026. Next: NASA HLS updates, McDowell's monthly reports.
- **Post-2016 aerocapture flights.** Not checked. Next: NASA aerocapture technology pages (2023 "ready for future mission use"
  story, found but not opened) and planetary mission lists.
- **MW-class NEP studies** NTRS 20220017245 and 20220002034 (power conversion mass modeling) found but not opened; the
  "2.5 MWe at 20 kg/kWe" and "15 MWe at ~1 kg/kWe" figures came only from a search summary and are not used.
- **Kornuta et al. 2019 (ULA "Commercial lunar propellant architecture", REACH)** not opened; numbers known only via
  Metzger 2023.
- **KISS 2012 asteroid retrieval full report** unobtainable (certificate error, 404, 403; rows 68, 114); only the abstract used.
- **Jedicke et al. 2018 (Planet. Space Sci.) water-delivery delta-v** paywalled (rows 4, 7).
- **Psyche SPT-140 thrust and Isp in flight** not obtained from a primary source (rows 28 to 30, 95).
- **Starlink argon thruster Isp and power** (2,500 s, 4.2 kW were in a search lead only); 170 mN only from trade press.
- **YES2 31.7 km tether (2007)** not confirmed from a primary source (row 54).
- **Ideal solar radiation pressure at 1 AU (about 9 µN/m² for a perfect reflector)** used only as a comparison in F2; not
  sourced this session.
- **Deep Space Network capacity** (how many links a fleet of thousands of tugs would need) not researched.
- **Tug degradation and lifetime at scale** (AEPS 23 to 50 kh life is per thruster) not translated into replacement rates.
- **Sources found but not read:** Bao et al. 2015 (lunar/Earth gravity-assist capture of NEOs, cited in Jedicke 2019);
  Elvis et al. 2011 (ultra-low delta-v objects, arXiv:1105.4152); "How Many Ore-Bearing Asteroids?" (arXiv:1312.4450);
  Sonter 1997 MSc thesis (NSS-hosted); SP-413 Appendices K ("Lunar Gas Gun Mass Driver") and L ("Passive Catchers").

## Rejected sources

- **LinkedIn post (row 25)**: claimed "20 kW krypton in orbit"; not a primary source and unconfirmed. Not used.
- **Wikipedia, Guinness, aggregators, Kerbal and NewMars forums, mailing-list archives** (rows 16, 40, 49, 54, 86, 95,
  98, 102, 108): leads only; every number used was taken from a primary source or labeled secondary.
- **Venus ascent "1500 m/s ballpark" for losses** (forum, row 86): not used; the NIAC 9 km/s figure was used instead.
- **Jalopnik launch counts** (row 45): replaced by McDowell's report.
- **Xenon market-research pages** (row 115): commercial summaries with conflicting 30 to 65 t/yr; replaced by Lindner 2023.
- **yarchive "hydrogen storage" (1982 study, 0.127 %/day)** (row 127): secondary re-post; the primary 1982 study was not opened.
- **ACS3 "0.045 mm/s²" characteristic acceleration** (row 101): from a pre-launch simulation presentation, not a measurement.
- **"$2.6 billion" KISS asteroid-retrieval cost** (row 69): in the query, not confirmed by any source. Not used.
- **Jedicke 2019 "76 km s^-1" capture delta-v** (row 5, C5): a typographical error in the preprint. Not used.
- **NTRS 20000052454 (Venus Aerobot Multisonde, 1999)** (row 87): off-topic for ascent. Not used.
- **NTRS 20190028305 (KSC ground LH2 sphere)** (row 128): ground storage in gallons per day; not relevant to orbit.
- **DRACO cancellation news (Breaking Defense, NewSpace Economy)** (row 97): used only as a labeled secondary for flight
  status; no numbers taken.
