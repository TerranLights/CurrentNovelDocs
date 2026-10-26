# Deferred research: continue later

**Created 2026-10-11 at the developer's direction.** This is the running list of things researched, not found, and parked
**on purpose** to be continued in a later session. It is separate from `SHOPPING_LIST.md`. That file lists sources the
developer might obtain. This one lists searches **an agent should run again** and what to try. Each batch notes which
research file it came from. **Do not delete an item until it is resolved, and say where in the resolving file.**

**On resume:** work these only after the orchestrator review of the completed research files, unless a class needs one
sooner. Use the "search next" leads as written. A route that failed once may still work through a different mirror,
the author's page, an agency NTRS record, or arXiv. Log each route (`_BRIEF.md`).

**All five second-tranche agents have reported; Batches 1–5 are entered.** Later searches go in Batch 6 onward.

---

## Batch 1: from `gap_retry_leo_human_machines_power.md` (418 lines; ~45 searches; ~95 documents opened; ~14 dead routes)

### Routes that failed (the pages exist; the tool could not read them)

| Source | Failure | Try next |
|---|---|---|
| **SpaceX pages** and the **Falcon user's guide** | return a JavaScript shell or a 404 | the PDF user's guide from a mirror; an independent analyst such as a government or university study |
| **Springer ISS-RAD papers** (Life Sciences in Space Research, 2023, Parts 1–3) | paywalled; three routes tried (publisher, Europe PMC, PubMed); abstracts only | author preprint copies; the NASA SRAG WRMISS 2025 slides (read; few numbers) |
| **Cucinotta 2008** (BioOne) | Incapsula wall; NTRS 20080026203 has a different abstract and no PDF | author copies; NASA-hosted version |
| **ORNL Pu-238 page** | 403 | NASA RPS program documents; National Academies radioisotope reviews |
| **MDPI paper** (4058) | blocked | a repository copy |
| **ResearchGate** "Impact of Solar Activity Cycles on ISS Orbital Decay: A Two-Decade TLE-Based Analysis (2005-2025)" | not opened; the arXiv route failed | the arXiv listing again; Space-Track TLE history for catalog number 25544 |

### Facts still not found

| # | Item | Search next |
|--:|---|---|
| 1 | **ISS reboost propellant per year** from a NASA or ESA primary (only a 1995 plan of 8–11 t/yr for the Russian segment, and per-burn data) | NASA ISS Program Office "Trajectory Operations" papers; Progress M propellant manifest tables; *Orbital Debris Quarterly News* altitude histories |
| 2 | **ISS monthly altitude decay** from a NASA primary (tool summaries gave 100 m/day and 2–4 km/month; not used) | Space-Track TLE history; JSC or ESA conference papers on ISS drag |
| 3 | **ISS eclipses per year**; longest sunlit periods (only "no eclipse above about 70° beta, one week twice a year", and 30–35 min eclipse per 90–92 min orbit) | NTRS 20250002029 (found, not opened); JSC "ISS beta angle" thermal documents |
| 4 | **Current ISS altitude** (2026) | NASA mission pages |
| 5 | **TDRS Ku-band ISS round-trip latency** (SNUG and test data used instead) | NASA SCaN documents |
| 6 | **Dose at 600 km vs 400 km** | ESA SPENVIS / ECSS-E-ST-10-04C tables; NASA/TP-2009-215779; Wu et al. 2011 (NTRS 20110015964, abstract only); STS-31 and STS-61 dose reports; Badhwar 2002 |
| 7 | **Solar Cycle 25 effect on crew dose**, quantified | beyond the ISS-RAD slides: none found |
| 8 | **The "80 / 160 mSv" claim.** Not traced to a NASA document. NASA's own figures found: **40–90 mSv** and **72 mSv** per six months. | settle against NASA primaries before any class cites a crew dose |
| 9 | **ORDEM 3.0 numeric fluxes** by size and altitude (numbers live in software and figures) | NASA/TP-20220002309 (ORDEM 3.1 verification; found, not opened); ODQN issues; Hypervelocity Impact Symposium flux tables |
| 10 | **ISS shield ballistic-limit equations and critical diameters** (only a 1 cm statement) | Christiansen (NASA JSC), "Design and performance equations for advanced meteoroid and debris shields" (NTRS); ISS document SSP 30425 |
| 11 | **Atomic oxygen at 600 km**, its solar-cycle swing, ISS ram fluence per year | a NASA primary |
| 12 | **Orbital lifetime of very large structures** (ISS ballistic coefficient was not derived because drag area and drag coefficient were not sourced) | NASA debris-office lifetime tools |
| 13 | **Modern commercial-part TID values** (only 1996 JSC classes) | NASA Goddard RADHOME / NEPP compendia (NTRS 20220010348; found, not opened); NESC COTS assessment (Majewicz, Chen); ISO 21980:2020 |
| 14 | **Typical single-event rates** beyond the 1996 per-class numbers | as above |
| 15 | **ESTL actuator data** beyond the SOT paper and the Harmonic Drive paper | ESTL's own site; NTRS 19750006982 (sputtered MoS₂ bearing endurance; seen in a summary, not opened) |
| 16 | **NASA HRP evidence reports** (cardiovascular, vestibular, SANS, immune) as primaries. The two NTRS numbers given (20150006969, 20160001745) are a panel report and a process deck. | NTRS: the "Evidence Report: Risk of Cardiovascular Adaptations Contributing to Adverse Mission Performance", and the SANS and immune reports. The plasma-volume 10–15% figure is secondary. |
| 17 | **Launch cost per kg, 2024–2026** for Falcon Heavy, Starship, Neutron, New Glenn; any government analysis | not found; SpaceX pages unreadable |
| 18 | **ISS array wing dimensions** from NASA (Lockheed numbers seen only in a summary); a 2026 power-degradation figure (only 2003 P6 data) | NASA ISS pages |
| 19 | **Propulsion and nuclear:** X3 Hall thruster (NTRS 20190001137; PEPL X3 pages); NTRS 20190029289; NTRS 20040161476 (a bibliography; the 2004 papers behind it were not opened); NASA TA-3 space power roadmap radiator numbers; Pu-238 supply and production, 2024–2026 | NASA RPS program; National Academies reviews |
| 20 | **Mars round trip:** the "Folta 2012" item resolved to a two-page abstract plus a 2005 paper. A separate 2012 full paper was not found. Bailey et al. 2013 table columns could not be aligned by year in the extracted text. | the AIAA copy, doi `10.2514/6.2013-5507` |

### Found and not opened (listed for a follow-up)

arXiv 2609.24534 (FACSAT-2 re-entry, solar cycle 25) · Frontiers `fspas.2026.1797886` · the JAXA Kibo shield page
(`iss.jaxa.jp/iss/kibo/develop_status_09_e.html`) · NASA OIG IG-22-003 PDF · GAO-17-673.

---

## Batch 2: from `robot_body_in_space.md` (751 lines; ~80 search strings; 109 log rows; 17 dead or partly dead)

### Not opened at a primary source

| # | Item | Search next |
|--:|---|---|
| 1 | **Digit, Optimus and Figure power and heat figures.** Agility and Figure publish no specifications. Tesla's AI Day 2022 figures reached the agent only through press (2.3 kWh, ~100 W sitting, ~500 W brisk walking; Digit ~1 kWh; Digit 5 ~90 min run and 9 min recharge). Unverified. | Tesla AI Day 2022 transcript or video; Agility's 2025–2026 datasheet; an independent teardown with measured watts |
| 2 | **Valkyrie continuous power draw in watts** | Radford et al., J. Field Robotics 2015; IHMC Valkyrie papers (energy per step); NASA ER4 technical memoranda |
| 3 | **Robonaut 2 thermal-vacuum test data** (only qualitative statements; a summary quoted "-25 °C to 105 °C" for two joint actuators; unverified) | NTRS: Ambrose and Berka, "Thermal Management in Hyper-Redundant Space Manipulators" (SPIE 1993); R2 joint qualification reports |
| 4 | **Humanoid heat fraction** (share of electrical power that becomes heat; energy conservation was used instead) | a measured power-balance paper on Valkyrie, TALOS, Atlas or Digit |
| 5 | **Li-ion and solid-state cell behavior in vacuum** (swelling, venting, electrolyte loss; only qualification requirements found; NTRS 20060020764 was a stub) | NASA battery workshop papers on pouch cells in thermal vacuum |
| 6 | **Hardened-processor datasheets.** BAE RAD750 datasheet: HTTP 403 (curl and WebFetch). A summary quoted 200 krad (rad-tolerant), 1 Mrad (rad-hard), latch-up-immune SEU rate below 1.6e-10 errors/bit-day; unverified. | vendor datasheet through a mirror; NASA NEPP compendia |
| 7 | **NASA per-material outgassing values** (outgassing.nasa.gov is dynamic; NASA RP-1124 Rev 4 was an unreadable scan). No TML/CVCM for skin silicone, PVC, polyurethane foam or fabrics. | JAXA matdb.jaxa.jp data lists; a library scan of RP-1124 |
| 8 | **Textile and skin solar absorptance and emittance** (Kauder lists coatings and Beta cloth only) | ECSS or NASA tables for Nomex, Kevlar and silicone elastomers |
| 9 | **Mars surface solar irradiance and dust loss** (press: Opportunity fell from ~700 Wh/sol to 22 Wh/sol in the 2018 storm at optical depth 10.8; unverified). Overlaps Batch 3's Mars retry. | Lorenz et al.; JPL MER power reports |
| 10 | **Soft-skin permeation and blistering in vacuum** (a summary quoted PDMS O₂ permeability of 800 Barrer; unverified, not used) | Merkel et al., J. Polym. Sci. B 38:415–434 |
| 11 | **PFPE lubricant radiation threshold** (mechanism only) | ESTL or Krytox radiation-stability data |
| 12 | **Convective cooling in the Mars atmosphere** (6.36 mb CO₂) for a warm body | not searched |
| 13 | **Dextre service history and design life** (Wikipedia and news only: 15-year design life) | CSA / NASA primaries; tabulate |
| 14 | **Perseverance, ISS CMG and other long-duration machine reliability data** | not searched beyond the machines covered |
| 15 | **Cold-weld experiments beyond the NASA patent; ESA tribology handbook values** | ESA tribology handbook |
| 16 | **Lunar and Mars regolith wear rates on robot joints and seals** in controlled tests (S27 reviews seals; its test data not extracted) | Proctor and Dempsey, re-read for the test tables |
| 17 | **Antarctic humanoid or legged-robot trials** (press: a Chinese hexapod run at -40 °C with an insulated battery for two hours; an Arctic quadruped traverse; no paper opened) | trial papers; Arctic/Antarctic legged-robot field reports |

### Routes that failed

BAE RAD750 datasheet (403) · NASA outgassing database (dynamic) · NASA RP-1124 Rev 4 (unreadable scan) · Merstallinger et al.
(RADHARD 2024; 404) · DTIC radiation handbooks (maintenance page) · NTRS 20060020764 (a stub).

### Found and not read (or only skimmed)

NTRS 20200000214 (Opportunity End of Mission Report; abstract only, no PDF) · NTRS 20100009705 (JPL safe charge rates and
lithium plating; abstract only) · JPL FY21 R&TD poster R22020p · NASA Glenn "SiGe" low-temperature electronics pages · NASA
NEPP "Careful COTS" guidance · NASA TM-2009-215751 (read for qualification tables and vacuum text only) · Caltech SSPD-1 /
MAPLE papers · JAXA microwave transmission papers · Daryabeigi et al., NTRS 20060019134 (high-temperature MLI; downloaded,
not read) · NASA CR-1787 sections beyond those cited.

---

## Batch 3: from `moon_lagrange_and_comparables.md` (443 lines; ~64 searches; ~75 pages opened; 10 dead ends, 7 at the sources)

### Routes that failed

DTIC (403; reports AD0609888, AD0488532, AD0678427, ADA389253) · bas.ac.uk pages (Halley closure) · the ASCE Mir-repair paper ·
Carrer 2024 full text (abstract only) · the Lunar Sourcebook (not open online).

### Part 1 (physics): not found

| # | Item | Search next |
|--:|---|---|
| 1 | **Peak-illumination polar sites and "eternal light" figures** (not searched) | LRO LOLA/LROC illumination maps (Mazarico et al. 2011; Speyerer and Robinson 2013) |
| 2 | **Paige et al. 2010 (Diviner polar temperatures)** and **Williams et al. 2017** (only quoted through reviews) | the papers themselves |
| 3 | **Colaprete et al. 2010; Strycker et al. 2013; Spudis et al. 2010 and 2013; Mini-SAR; Lunar Prospector neutron and H data** (abstracts and reviews used) | full texts |
| 4 | **Apollo Lunar Sourcebook** (Heiken, Vaniman, French 1991): bulk soil oxide table (so oxygen wt% is quoted, not derived), respirable dust size, electrostatic charging, radiation chapter | a library copy; this is also a shopping-list candidate |
| 5 | **Dust toxicology primaries** (only the Gaier "under 5 microns" quote) | Wallace / Linnarsson / Park papers |
| 6 | **Lunar seismicity and meteoroid flux at the Moon** (not researched) | bears on lava-tube and surface design |
| 7 | **Lava tubes**: Sauro et al. 2020 (Earth-Science Reviews); Carrer et al. 2024; Chappaz et al. 2017 (GRAIL). Sizes beyond abstracts not found. | overlaps the Mars lava-tube retry |
| 8 | **Lunar mass driver**: no primary report of Mass Driver One or Two results; O'Neill's *The High Frontier* and SP-428; Kolm / Snow papers; SP-413 Appendices 5G, 5H and L | |
| 9 | **Economics**: Jones et al. (2018?), Charania and DePascuale, Bennett et al., Kornuta et al. 2019 (REACH); a dated 2024–2026 launch cost table | |
| 10 | **Lagrange points**: Earth-Moon L4/L5 as mission orbits (none flown); Kordylewski clouds; a primary on Earth-Moon L1/L2 halo thermal and radiation; Queqiao orbit parameters; ARTEMIS stationkeeping (Folta et al.); Gaia and JWST actuals; SOHO annual propellant; Sun-Earth L4/L5 (STEREO) environment; dose equivalent at L2 | |
| 11 | **Cislunar radiation** (Orion / Artemis I dosimetry) | NASA primaries |
| 12 | **Artemis II** (a flight on 1–11 April 2026 is reported in secondary pages; no NASA primary opened; no figures used); **Gateway status** (contested in 2025–2026 news; orbit physics stands regardless) | NASA primaries |
| 13 | **DRO station-keeping** (only "0 m/s" in Whitley and Martinez 2016, a qualitative table entry) | DRO long-term stability studies |

### Part 2 (mechanism comparables): not found

| # | Item | Search next |
|--:|---|---|
| 14 | **Antarctic**: COMNAP Antarctic Station Catalog (PDF not opened); Concordia / Dome C winter-over logistics (IPEV/PNRA/ESA); the NSF 2016 evacuation release; the Vostok 1982 fire in a primary; Stonehouse 1953 "Fire precautions at Antarctic Stations" (*Polar Record*); NSF/USAP incident statistics; McMurdo and Pole winter populations by year; per-person mass flows (the Panel's Figure 1 is a graph) | |
| 15 | **Submarines**: atmospheric-equipment redundancy (SUBSAFE is hull integrity); NRL submarine atmosphere papers; the NRC 1988 report cited by NRC 2007; oxygen consumption per person; emergency backup (oxygen candles, LiOH) in a primary; a primary for "food is the limit" | |
| 16 | **ISS**: ORU counts and failure rates from the NASA Logistics and Maintenance database; actual annual cargo up-mass. **The OIG crew-time shares (13% maintenance) conflict with delivered research hours**: that 13% is a planning share, not a measured fraction. | NASA ECTM validation (NTRS 20220013436, 20150009469); later OIG reports (2017–2018) |
| 17 | **Mir**: the claim that repair reached 50% of cosmonaut work | the blocked ASCE paper |
| 18 | **Biosphere 2**: Silverstone and Nelson 1996 full text | |
| 19 | **Analog habitats** (HI-SEAS, Mars-500, MDRS): no maintenance-time data searched | |

### Found and not read

NTRS 20220011365 · NTRS 20220019129 · NTRS 20230010822 and 20230010792 · ISSFD 2024 paper 20-13 · the Polito DRO thesis ·
NTRS 20210026714 (Deitrick, regolith size) · arXiv 2408.05823 (review of lunar construction) · arXiv 2602.03829 (open database
of regolith properties).

---

## Batch 4: from `life_support_lowg_power_structures.md` (591 lines; 45 searches; ~50 document groups opened; 2 searches wholly dead, 6 more dead on the figure sought; 6 page-level dead ends)

### Not opened

BVAD Revision 2 (only Rev 1 found) · the Lunar Sourcebook · MMPDS and CMH-17 · NCRP and ICRP fetal-dose figures (search-summary
numbers only; not used) · the ESA 3D-printing study PDF (the nebula.esa.int URL returned HTML) · the BIS paper "Docking with
Rotating Space Systems".

### Not found

| # | Item | Search next |
|--:|---|---|
| 1 | **BVAD Revision 2**, and **NASA-STD-3001 Vol. 1–2** (CO₂ and O₂ limits). Table 4-99 (growing area by diet) has misaligned columns; per-crop yields not used. | NTRS "Baseline Values and Assumptions Document Rev 2"; Wheeler / Hall / Ruminsky diet studies |
| 2 | **Closed-ecology full texts**: Lunar Palace 365 (peer-reviewed; only the bioRxiv preprint read); Salisbury, Gitelson and Lisovsky 1997 (*BioScience* 47(9):575); Gitelson, Lisovsky and MacElroy 2003; Lunar Palace 1 (105-day); MELiSSA whole-loop numbers; Severinghaus et al. 1994 (Biosphere 2) | |
| 3 | **Modern LED efficacy and crop yield per kWh** (BVAD's 1.6–10 g/kWh predates LEDs) | |
| 4 | **ISS ECLSS**: oxygen generation power and mass; a primary table of total ECLSS power and mass per crew member | |
| 5 | **Low-pressure (<57 kPa) human tolerance**, the original Norcross 2013 report; **fire in partial gravity** (only the 1 g Test 1 method paper read) | |
| 6 | **Fetal dose limits**: NCRP / ICRP figures (summaries quoted 5 mSv per pregnancy and 0.5 mSv per month; unverified); ICRP Publication 84 | |
| 7 | **Reproductive hazards in space**: Mishra and Luderer 2019 (*Nat Rev Endocrinol*); the 2020 Chinese mouse-embryo space experiment (Lei et al., *Natl Sci Rev*); Ronca and Alberts 2000 | |
| 8 | **NASA HRP evidence reports** (SANS, muscle, bone, cardiovascular); countermeasures (lower-body negative pressure, fluid loading) | overlaps Batch 1 item 16 |
| 9 | **Rotational gravity in humans since 1994?**; short-radius centrifuge studies in orbit; **partial-gravity primate or large-mammal data** (none found); plants at Mars gravity (abstract only); animal and plant fertility at partial gravity | |
| 10 | **Radiator areal mass** (kg/m²) and measured heat rejection per m² (summaries quoted 1.5–3.6 kg/m²; not used) | SAE and NASA primaries |
| 11 | **Kilopower** (KRUSTY) reports; orbital-habitat nuclear studies; Brayton vs Stirling at 100 kWe–MWe; reactor shielding for a habitat | |
| 12 | **Solar**: iROSA dimensions; decades-long array degradation at 1 AU; battery or regenerative fuel cell mass for eclipses. **SP-413's radiator area (4.9×10⁵ m²)** could not be reconciled with a blackbody calculation (K9). | |
| 13 | **Structures**: MMPDS / CMH-17 allowables (composites here are manufacturer typical values); NASA SP-8007 shell buckling; fatigue of pressure-cycled and spinning shells; TransHab burst factor and Kevlar / Vectran allowables; BEAM leak rate and pressure; Bigelow B330 numbers | |
| 14 | **MMOD**: ORDEM 3.0 numeric fluxes vs size at 400 km and beyond LEO; Grün 1985 flux; SSP-30425; Christiansen's Whipple rear-wall equations (OCR-damaged) | overlaps Batch 1 items 9–10 |
| 15 | **Docking to a rotating hub**: Hall's AIAA 99-4524; SP-413 appendices A, F, G, I, K, M; NASA SP-8024; any rotating-station momentum budget; artificial-gravity.com PDFs AIAA-2015-4613 and AIAA-2017-5140 | |
| 16 | **Regolith and ISRU**: the Lunar Sourcebook (density, composition, specific heat at high temperature; the sintering heat floor was not computed); Cesaretti 2014; strength of full-scale printed structures; thermal cycling of sintered regolith; peer-reviewed confirmation of the 2024 molten-regolith electrolysis run and the 311 kW figure; MMPACT reports; Mars regolith processing (perchlorate removal) and sulfur concrete | overlaps Batch 3 item 4 |

### Found and not read

Jensen arXiv:2408.00155 (abstract only) · NTRS 20170005618, 20160009739, 20200003267 (headers only) · NTRS 20240011694
(skimmed) · NASA TN D-5772 (header) · Frontiers in Physiology AGBRESA protocol (PMC9492851; abstract only).

---

## Batch 5: from `gap_retry_mars_venus_jupiter.md` (516 lines; 101 numbered log rows; 18 dead at the sources, 1 at the query)

### Routes that failed

Springer bot wall (Martinez 2017; the 2025 Space Science Reviews cave review) · Crossref (no abstract) · CDC / ATSDR (403 on both
hosts) · OU and UCL repositories (403) for Dartnell · eight routes for Seiff 1985 · NSSDC IDs for Venera 13 (guessed; errors) ·
JPL Magellan conjunction pages (403) · NTRS 20210007725, 20220000754 and 20210002012 (records with no file).

### Not closed

| # | Item | Search next |
|--:|---|---|
| 1 | **Measured Mars temperature by latitude and season** (Martinez 2017; Viking IRTM, Kieffer 1977; Pathfinder, REMS, TWINS, MEDA). Mars Climate Database v6.2 **model output** was substituted and is labeled as a model. | Europe PMC for open-access REMS and MEDA papers; the PDS atmospheres node for REMS reduced data |
| 2 | **Mars solar irradiance under dust beyond the Viking sites** (the tables are for VL1 and VL2 only) | |
| 3 | **Lava tubes**: measured roof thickness (none exists); Cushing 2012 and 2015; the 2025 cave review; Rostel et al. 2020 numbers | a third route for each |
| 4 | **Perchlorate**: the ATSDR toxicological profile; NRC 2005; inhalation toxicity of perchlorate dust (EPA: no value); lunar and Martian dust inhalation studies (not searched) | |
| 5 | **Dundas et al. 2018 full text** and the eight sites' latitudes; the SWIM maps (data products) | |
| 6 | **Dust storms**: SL19's table S1 (properties of each global storm); Montabone and Forget 2018; **a count after 2018** (no later event documented in anything opened; no claim made about 2019–2026) | |
| 7 | **Launch windows for crewed or cargo missions** (the BURKE dates are 2010 mission-design minima, not NASA announcements) | mission-specific plans |
| 8 | **MARIE dose equivalent in mSv/day** (Zeitlin; Cleghorn); Mars-orbit habitat dose at a specific shielding mass in g/cm²; Zeitlin 2013 and Hassler 2014 supplement | |
| 9 | **Partial gravity**: human bed-rest or centrifuge studies at 0.38 g (none found); bone results of the MARS mouse missions | |
| 10 | **Venus VIRA tables** (Seiff 1985): no web table found | NASA PDS archives for the Pioneer Venus probes; the NSSDC "Venus Atmosphere" listing; a library request for *Advances in Space Research* vol. 5 no. 11; Venus-GRAM outputs |
| 11 | **Venera 13 from a Soviet or NASA SP primary** (Ksanfomaliti et al. 1983) | |
| 12 | **Dartnell et al. 2015 full paper**; Nordheim et al. 2015 (ionization of Venus) | |
| 13 | **Birch 1991 (JBIS 44:157)**: obtained from no route (Fogg 1995 and Wikipedia are secondary) | |
| 14 | **Europa surface dose** in absorbed-dose units: Paranicas 2002 / 2007 / 2009; Nordheim 2016 / 2017 (*Nature Astronomy*); Europa Clipper radiation requirements | |
| 15 | **Callisto and Ganymede human-unit dose** (Cooper 2001 full text); **Juno measured radiation** (Becker et al.); **Galileo** (Fieseler 2002 full text) | |
| 16 | **Saturn versus Jupiter in common units** (numeric); Cassini MIMI datasets (PDS); Titan surface dose | |
| 17 | **Enceladus**: Hansen et al. 2020 full text. **Io**: Veeder et al. 2012 and 2004; Davies et al. final version | |

### Found and not read

Limaye et al. 2018 (*Space Sci. Rev.* 214) · arXiv:2603.22602 · arXiv:2605.09052 · Putzig et al. handbook chapter · Hansen et al.
UVIS plume paper (*Icarus* 2020).

---

## Status of the second tranche

All five agents have reported; Batches 1–5 are in. New searches belong in a Batch 6 and later.


---

## Batch 6: from `waste_heat_utilization.md` (441 lines; 52 searches; 11 dead ends)

**Routes that failed:** NSF 1992 power-upgrade page (404) · NREL and Antarctic Sun (host not resolved) · PNAS site (403; PMC copy used) ·
KIST (firewall) · maritime.edu (403) · ADS Ewert 1989 (405).

| # | Item | Search next |
|--:|---|---|
| 1 | **Absorption chillers and membrane distillation on low-grade (40–60 °C) heat.** No primary opened; the one absorption concept read regenerates at up to 120 °C. | ASHRAE or DOE/ORNL absorption chiller fact sheets; membrane-distillation reviews; Ewert 1989, *J. Spacecraft and Rockets* 26:303 (title seen in a snippet only) |
| 2 | **Kerrebrock's three-quarters rule** (derived, not sourced) | a space-power textbook (Angelo and Buden); Ewert 1989 |
| 3 | **Polar-station heat recovery and ship / submarine heat reuse**, from primaries | NSF Office of Polar Programs environmental assessments for South Pole; Naval Ships' Technical Manual chapters on distilling plants |
| 4 | **Fission surface power / Kilopower waste-heat reuse** for water or habitat heat | NASA FSP user interface requirements; Artemis base architecture papers; 1-ACT / NASA papers on Kilopower heat pipes and high-temperature water heat pipes |
| 5 | **Energy per kg for molten regolith electrolysis**; carbothermal in flight-like form | Sibille et al. 2024 TFAWS; NTRS 20110008524; NTRS 20205007780 |
| 6 | **Regolith ice-mining thermal energy** (NIAC Aqua Factorem; the search-summary numbers 800 kW and 2.4 kW are not used) | the opsjournal paper; NIAC pages |
| 7 | **Heat of reaction of ilmenite hydrogen reduction** (only 294,000 J/kg, from an unopened reference) | compute from formation enthalpies of FeTiO₃ and TiO₂ |
| 8 | **ASRG hot-end and cold-end temperatures** (only system efficiencies read) | |
| 9 | **ISS cabin-level heat flows** (kW for the cabin air condensing heat exchanger; total internal heat collected); **measured ISS radiator temperatures and rejection** (not design capacity) | NTRS 20130000766; ICES 2024 ISS ECLSS presentation |
| 10 | **Commercial humanoid thermal designs** (Digit, Optimus, Figure, Atlas electric) | patents; IEEE thermal papers on humanoid actuator cooling; the KIST cold-plate paper (firewalled) |
| 11 | **Orbital-habitat reactor waste heat** (no orbital study found; the sibling file also found none) | |
| 12 | **Mars heat-pump studies; 2020s Artemis heat-pump hardware** (only 1990s–2010s items) | |

**Found and not read:** IAPWS-95 · Mainstream Engineering heat pump SBIR news · NTRS 20110008524 and 20130012503 · TFAWS 2024 ID-04 ·
NTRS 20210026557 · Meier APM details · EPFL graph pages on thermochemical cycles · JAXA repository thermal control hits.

---

## Batch 7: from `lagrange_thermal_environment.md` (292 lines; 46 searches; 61 page opens; 13 dead ends: 3 at the query, 10 at the sources)

*(Entered 2026-10-11 by the orchestrator from the agent's section 8; the agent's wording is condensed.)*

| Open thread | Why it matters | Search next |
|---|---|---|
| Numerical eclipse statistics for Earth-Moon L4/L5 libration orbits | settles the conflict with the "once or very few times per month" remark (`lagrange_eclipse_calculation.md` §5.9-5.10) | He et al. 2026 (Springer, paywalled); the 2024 Acta Astronautica paper on 3:1 resonant axial orbits (HTTP 403); author preprints, CNKI or a library copy |
| Earth-Moon L4/L5 station-keeping delta-v per year | the cost of the unstable point (e-folding 318 days) or of a large orbit | Salnikova, Stepanov and Shuvalova 2018; Schutz and Tapley (1970s); Farquhar's thesis (NASA TR R-346) |
| Kordylewski cloud number density; Igenbergs et al. 2012 (Hiten Munich Dust Counter); the Wang et al. 2021 review PDF | hazard to a station near the points | the Igenbergs chapter; the review PDF via another route |
| Queqiao orbit (13,000 km Z-amplitude, 14-day period) and any eclipse history | a flown Earth-Moon halo orbit's eclipse record | Zhang Lihua 2021 via another mirror; Chinese Journal of Space Science |
| JWST orbit page text (STScI user docs) and the L2 umbra radius | thermal comparison | the STScI pages; the gaia.ac.uk PDF returned 403 |
| Sun-Earth L4/L5 radiation dose | a station there | ESA Vigil requirements (the radiation analysis returned 404); STEREO HET/LET publications |
| STEREO L4/L5 results (Trojan search outcome, dust counts) | dust at Sun-Earth L4/L5 | not found |
| Lucy thermal design (radiator, louvers, cold-case temperatures at 5.7 AU) | an L4/L5-class thermal case far from the Sun | an ICES or TFAWS paper on Lucy thermal design |
| Flown radiator areal mass other than ISS (Shuttle panel mass) | radiator mass per kW | NASA Shuttle thermal reports |
| End-of-life absorptance specific to a free-space orbit at 1 AU | radiator sizing at end of life | NASA radiator degradation studies; the handbook says interplanetary rates differ only in intensity |
| MER radioisotope heater count and survival-heater energy | night survival heritage | a MER thermal design paper (the search summary's 8 x 1 W and 100 Wh were not confirmed on an opened page) |
| Flown lunar-night storage other than RHUs | heat battery heritage | none found beyond concepts |

**Sources found and not read:** the Gaia "IN_L2_orbit" note (403); the Wang et al. 2021 full text; Igenbergs et al. 2012; the ESA Vigil objectives document; the Planetary Society Queqiao explainer (secondary).

---

## Batch 8: from `starlifting_physics_and_minimum_infrastructure.md` (580 lines; 16 open threads)

*(Entered 2026-10-11 from the source file's "Open threads" section; the source's wording is kept. "Next:" is the source's own suggestion; where the source gave none, the cell says so.)*

| # | Item | Search next |
|--:|---|---|
| 1 | **Criswell (1985), the origin of starlifting:** book chapter in *Interstellar Migration and the Human Experience*; no open text; Internet Archive copies are lending-restricted (rows 7, 8). | a library or interlibrary loan. |
| 2 | **Beech (2008), *Rejuvenating the Sun and Avoiding Other Global Catastrophes*** (Springer): chapter list only (row 11). Known here only through [CA10]. | (none stated in the source) |
| 3 | **Matloff (2017), JBIS 70:458:** abstract only; paywalled (rows 5, 6). Its per-kg energy and scenarios are known only as quoted by [SK23]. | (none stated in the source) |
| 4 | **Caplan (2019) and Svoronos (2020, 2021) stellar-engine papers:** abstracts only; ScienceDirect 403 (rows 16-18). | (none stated in the source) |
| 5 | **Criswell's "ring current" and "huff-n-puff" mechanisms:** no primary description online (row 12). | (none stated in the source) |
| 6 | **Absolute FIP enrichment of Fe relative to H in the solar wind:** [PI15] gives only ratios to Mg and the fFIP bias; arXiv 2411.18984 was surfaced but not read. Needed to turn "1 t of wind" into kg of each metal precisely. (He/H was resolved in the second run from Alterman and Kasper 2019, row 87; Kasper et al. 2007 itself was still not opened.) | (none stated in the source) |
| 7 | **Nittler et al. 2011 (Mercury surface XRS) numbers:** abstract-level only (row 78). | (none stated in the source) |
| 8 | **Hauck et al. 2013 direct:** escholarship 403 (row 72); values used come via [WH17]. | (none stated in the source) |
| 9 | **Galileo probe helium mass fraction (Y = 0.238 per a search summary):** not confirmed in an opened page (row 74). | von Zahn et al. 1998 (JGR) or Niemann et al. 1998. |
| 10 | **Palaszewski's Table I (He-3 fractions in Uranus and Neptune)** is an image in the PDF; only the 1.52 x 10^-5 case in the text was read. | (none stated in the source) |
| 11 | **Total mass of near-Earth asteroids:** not found in any source (row 84). | Granvik et al. 2018 (Icarus) size distribution integrated with assumed densities. |
| 12 | **Fox et al. 2016 (Parker mission overview, Space Sci. Rev.):** CC-BY but blocked to the tools (row 41). Would give the flown TPS and cooling specifics. | (none stated in the source) |
| 13 | **Solar Probe 2005 report (NASA/TM-2005-212786)** for the 4 R_sun design (row 49): not opened. | (none stated in the source) |
| 14 | **Parker FIELDS antenna material** (refractory metal) and Parker's measured shield temperature: not found in a primary source this session. | (none stated in the source) |
| 15 | **Huss et al. 2019** was read only to character 100,000 of 155,196 (row 57); the remainder may give helium or metallicity results. | (none stated in the source) |
| 16 | **Sources found but not read:** arXiv 2411.18984 (slow-to-fast wind composition); arXiv 1504.08325 (FIP review); NTRS 20150020912 and 20230001527 (NEO/space-resources); Granvik et al. 2018 PDF; Taylor 2018 (Acta Astronautica, planet4589.org); arXiv 2510.21743 ("Propellantless space exploration"); arXiv 2305.04212 (rotating magnetic sail). | (none stated in the source) |

---

## Batch 9: from `space_trucking_and_transport_infrastructure.md` (565 lines; 18 open threads)

*(Entered 2026-10-11 from the source file's "Open threads" section; the source's wording is kept. "Next:" is the source's own suggestion; where the source gave none, the cell says so.)*

| # | Item | Search next |
|--:|---|---|
| 1 | **Near-Sun cargo transport study.** No paper found that sizes transport of material from 0.1 to 0.5 AU to Earth or Mars orbit. | search for solar-sail cargo from inner orbits (sail thrust scales as 1/r², a physics relation not sourced here), "sundiver" or "solar photon thruster" cargo, and the starlifting sibling file's sources. |
| 2 | **Flyby-assisted cargo routes from Mercury or near-Sun orbits.** Only spacecraft (MESSENGER, BepiColombo) found. | Langevin and Yen (cited by Jehn 2014) for systematic Mercury return trajectories. |
| 3 | **Mercurian mass driver.** Not found (rows 132, 133). | read the rest of the science.gov topic page (714,658 characters unread), the SSI Space Manufacturing proceedings index, and Mercury-industrialization papers. |
| 4 | **In-orbit cryogenic boil-off rates** (liquid hydrogen, oxygen, methane): no primary in-orbit figure found (rows 127 to 129). | NASA CFM Technology Roadmap, Centaur extended-coast data, COLD-SAT / CPST reports on NTRS. |
| 5 | **Starship payload and cost from SpaceX directly.** SpaceX pages not readable by the tools (rows 41, 113). NASA OTPS assumptions (100 t, $50 to 100 M) are used instead and labeled as assumptions. | (none stated in the source) |
| 6 | **Starship vehicle-to-vehicle propellant transfer outcome in 2026.** OIG (March 2026) says planned for 2026; a secondary source says not attempted as of 24 Jul 2026. | NASA HLS updates, McDowell's monthly reports. |
| 7 | **Post-2016 aerocapture flights.** Not checked. | NASA aerocapture technology pages (2023 "ready for future mission use" story, found but not opened) and planetary mission lists. |
| 8 | **MW-class NEP studies** NTRS 20220017245 and 20220002034 (power conversion mass modeling) found but not opened; the "2.5 MWe at 20 kg/kWe" and "15 MWe at ~1 kg/kWe" figures came only from a search summary and are not used. | (none stated in the source) |
| 9 | **Kornuta et al. 2019 (ULA "Commercial lunar propellant architecture", REACH)** not opened; numbers known only via Metzger 2023. | (none stated in the source) |
| 10 | **KISS 2012 asteroid retrieval full report** unobtainable (certificate error, 404, 403; rows 68, 114); only the abstract used. | (none stated in the source) |
| 11 | **Jedicke et al. 2018 (Planet. Space Sci.) water-delivery delta-v** paywalled (rows 4, 7). | (none stated in the source) |
| 12 | **Psyche SPT-140 thrust and Isp in flight** not obtained from a primary source (rows 28 to 30, 95). | (none stated in the source) |
| 13 | **Starlink argon thruster Isp and power** (2,500 s, 4.2 kW were in a search lead only); 170 mN only from trade press. | (none stated in the source) |
| 14 | **YES2 31.7 km tether (2007)** not confirmed from a primary source (row 54). | (none stated in the source) |
| 15 | **Ideal solar radiation pressure at 1 AU (about 9 µN/m² for a perfect reflector)** used only as a comparison in F2; not sourced this session. | (none stated in the source) |
| 16 | **Deep Space Network capacity** (how many links a fleet of thousands of tugs would need) not researched. | (none stated in the source) |
| 17 | **Tug degradation and lifetime at scale** (AEPS 23 to 50 kh life is per thruster) not translated into replacement rates. | (none stated in the source) |
| 18 | **Sources found but not read:** Bao et al. 2015 (lunar/Earth gravity-assist capture of NEOs, cited in Jedicke 2019); Elvis et al. 2011 (ultra-low delta-v objects, arXiv:1105.4152); "How Many Ore-Bearing Asteroids?" (arXiv:1312.4450); Sonter 1997 MSc thesis (NSS-hosted); SP-413 Appendices K ("Lunar Gas Gun Mass Driver") and L ("Passive Catchers"). | (none stated in the source) |

---

## Batch 10: from `space_processing_and_fabrication.md` (491 lines; 17 open threads)

*(Entered 2026-10-11 from the source file's "Open threads" section; the source's wording is kept. "Next:" is the source's own suggestion; where the source gave none, the cell says so.)*

| # | Item | Search next |
|--:|---|---|
| 1 | **Whole-humanoid bill of materials by mass and element**: not found (rows 86-88). | teardown reports with primary data, IEEE/IFR robot material inventories, Boston Dynamics or Agility documentation, a peer-reviewed LCA of a legged robot. |
| 2 | **Magnet-free actuators** (induction, switched reluctance, ferrite) torque density versus NdFeB, as a route around the rare-earth bottleneck: not searched. | (none stated in the source) |
| 3 | **Primary text of Guerrero-Gonzalez and Zabel** (MRE, ilmenite-carbonyl and FFC plant models; duty cycle behind the 311 kW): seen only through [AZ24]. | (none stated in the source) |
| 4 | **Lomax et al. 2020 full paper** (FFC energy per kg, current efficiency): accepted-version download returned HTML (row 21). | (none stated in the source) |
| 5 | **Schlüter and Cowley review** of oxygen-extraction techniques with energy table: paywalled (row 16). | (none stated in the source) |
| 6 | **Carbonyl (Mond) process operating conditions** from a primary (temperatures and pressures for Fe and Ni carbonyl formation and decomposition): only tertiary sources surfaced (row 34); Vale's page gives no conditions. | (none stated in the source) |
| 7 | **Vapor refining / vacuum pyrolysis** of asteroid metal and of regolith (energy, yields): no primary found. | (none stated in the source) |
| 8 | **Measured energy per kg of water from carbonaceous asteroid material**: no primary (rows 30, 122-124); the 2025 Acta Astronautica optical-mining paper (ScienceDirect S0094576525002334) not opened. | (none stated in the source) |
| 9 | **ESA metal-printer sample analysis** (strength, porosity versus ground): ESA said "in the coming weeks" as of 21 Jul 2026; ESA image page of 1 Oct 2026 (row 39) was not re-opened in the resumed session. | (none stated in the source) |
| 10 | **Wake Shield film-quality numbers** (mobility, defect density, measured wake vacuum): ADS and ScienceDirect blocked (row 56). | (none stated in the source) |
| 11 | **ZBLAN fiber quality after return** (Flawless Photonics): not published in what was read. | (none stated in the source) |
| 12 | **AMF build volume and largest polymer part printed in orbit**: user guide behind a login (row 42). | (none stated in the source) |
| 13 | **China's 2020 in-orbit continuous-fiber composite printing**: press only (row 44); a CAST primary would settle part size. | (none stated in the source) |
| 14 | **Pressure needed to solidify helium**: Swenson abstract gives no number; a handbook value was not opened. | (none stated in the source) |
| 15 | **Lunar copper and rare-earth abundances by site** (beyond urKREEP): not searched beyond Crawford. | (none stated in the source) |
| 16 | **Clean-room and ultrapure-water requirements of a semiconductor fab** (mass and power per wafer start): not searched. | (none stated in the source) |
| 17 | **Freitas and Merkle KSRM Table/Appendix A** (all 9 artificial replicator data points): only section 5.2 text read. | (none stated in the source) |

---

## Batch 11: from `industrial_ramp_timelines.md` (480 lines; 16 open threads)

*(Entered 2026-10-11 from the source file's "Open threads" section; the source's wording is kept. "Next:" is the source's own suggestion; where the source gave none, the cell says so.)*

| # | Item | Search next |
|--:|---|---|
| 1 | **Lackner and Wendt (1995)** "Exponential growth of large self-reproducing machine systems" was not reachable; the auxon doubling time stays secondary (via Freitas and Merkle). | journal site or an institutional repository. |
| 2 | **Chirikjian NIAC final report** (2004) not opened; only the KSRM summary was read. | (none stated in the source) |
| 3 | **Freitas and Gilbreath, CP-2255 appendix 5I and the full NTRS copy (19830007081)**: the NSS scan was used; the NTRS original was not opened for an OCR cross-check of Table 5.2. | (none stated in the source) |
| 4 | **Robot learning rate:** no primary Wright's-law estimate for industrial robots was found; the IFR price index stops in 2005. | combine the IFR index (1990 to 2005) with IFR cumulative installations to compute one (not done here because the installations series was not opened), or search the Santa Fe Institute performance-curve database. |
| 5 | **Container shipping 1956 to 1980:** first-unit (Ideal X, 1956) to 10x and 100x could not be measured because the opened series starts in 1980. | Levinson, *The Box*, or UNCTAD Review of Maritime Transport back issues (the 2003 edition returned HTTP 403). |
| 6 | **Internet backbone before 1990** and **submarine cable lit capacity by year** (TeleGeography historical series) not found as a primary year-by-year table. | (none stated in the source) |
| 7 | **Tiangong** dates are from secondary sources only; | CMSA (cmse.gov.cn) English releases. |
| 8 | **ISS EVA totals** (159 EVAs, 1,000 hours at assembly completion) are secondary; NASA confirms 157 by 22 May 2011. | (none stated in the source) |
| 9 | **NREL transformer report** (McKenna, Abraham, Wang 2024) was unreachable (DNS failure for nrel.gov from this machine). | (none stated in the source) |
| 10 | **NASA OIG IG-24-016** full PDF not opened; ML-2 figures are at search-summary level. | (none stated in the source) |
| 11 | **World Nuclear Association** "121 months for 2023 connections" not opened (IAEA table used instead). | (none stated in the source) |
| 12 | **Mars settlement studies** beyond Musk (2017) and Salotti (2020): no NASA or academic analysis of time and cargo to a stated Mars population was opened (for example the Mars Society city-state contest entries, or Do et al. 2016 on the Mars One plan). | "Do Owens Ho Schreiner de Weck 2016 Acta Astronautica Mars One spares launches". |
| 13 | **Modern space-solar-power schedules** beyond NASA OTPS and Frazer-Nash: ESA SOLARIS and Caltech SSPD-1 were not covered. | (none stated in the source) |
| 14 | **Jamestown tobacco exports** (50,000 lb by 1617) seen only in a search summary; NPS plantation-system article not opened. | (none stated in the source) |
| 15 | **Terzi and Nicoli (2026)**: the last 31,000 characters of the article (methods and supplementary) were not read. | (none stated in the source) |
| 16 | **Industrial "ramp to 10x and 100x" for semiconductor fabs** (as opposed to build time) not found. | (none stated in the source) |

---

## Batch 12: from `cyclers_and_large_slow_vehicles.md` (308 lines; 13 open threads)

*(Entered 2026-10-11 from the source file's "Open threads" section; the source's wording is kept. "Next:" is the source's own suggestion; where the source gave none, the cell says so.)*

| # | Item | Search next |
|--:|---|---|
| 1 | **Primary cycler papers not obtained:** Byrnes, Longuski, Aldrin 1993 (JSR 30(3)); McConaghy et al. 2002 (AIAA 2002-4420) and 2004 (JSR 41(4)) full texts; Russell and Ocampo 2004/2005; Chen, Landau, Longuski 2006 (low-thrust Aldrin cycler); Landau, Longuski, Aldrin 2007 (JBIS) full text; Landau and Longuski 2005 semi-cyclers. Purdue faculty-page PDFs returned a JavaScript gate (rows 5, 11); AIAA returned 403. | interlibrary or the Purdue e-Pubs dissertation PDFs of McConaghy (2004) and Landau (2007). |
| 2 | **Earth-Venus and Mars-belt cyclers:** only Hollister and Menning citations and the Jones et al. 2017 abstract (triple cyclers, average transit-leg excess speed below 5 km/s). No Mars-belt, Mars-Jupiter or Earth-Ceres cycler study was found (dead at the sources, row 78). Russell and Strange 2009 (moon cyclers) not opened (JPL repository handle dead, rows 76-77). | (none stated in the source) |
| 3 | **Leads found late, not opened:** IAC-16 "Mission analysis of potential Earth-Mars cycler" (iafastro.directory, IAC-16/A5/2/34350); "Two classes of cycler trajectories in the Earth-Moon system" (UAB portal); Rogers 2014 Purdue dissertation (AAI3636504). | (none stated in the source) |
| 4 | **A mass budget comparing a cycler to direct conjunction transfer on equal assumptions:** Landau dissertation (2007) and Landau and Longuski "Part 2" are the likely sources; not opened. | (none stated in the source) |
| 5 | **A quantitative study of a habitat larger than about 200 t that thrusts while spinning:** none found. | Borowski et al., "Conventional and Bimodal NTR Artificial Gravity Mars Transfer Vehicle Concepts" (NTRS 20140017461, found, not read); NTRS 19800022950 full text (found, not read); Coyner 1982 and Weddell 1978 full texts. |
| 6 | **Hoffman and Kaplan, "Human Exploration of Mars: The Reference Mission," NASA SP-6107 (1997)**: not opened; DRA 5.0 used instead. | (none stated in the source) |
| 7 | **NCOS (1986) "Pioneering the Space Frontier" 460-t cycler mass breakdown**: cited by Nock; not opened. | (none stated in the source) |
| 8 | **Navigation accuracy for hyperbolic rendezvous** (position and velocity error budgets, tracking support): no figures found; Landau's dissertation chapter on flyby guidance is the next source. | (none stated in the source) |
| 9 | **Solar sail cargo (Frisbee 2002)**: numbers only from a search summary; the AIP paper not opened. | (none stated in the source) |
| 10 | **Hoyt and Uphoff, "Cislunar Tether Transport System," JSR 37(2), 2000**: not opened (citeseerx returned HTML); NIAC appendices (C, E, K, P, R) not read; PHLOTE (NTRS 20190000916) not read. | (none stated in the source) |
| 11 | **SP-428 papers III-1, III-2, II-1, IV-1, IV-3**: fetched, not read. | (none stated in the source) |
| 12 | **Rolffs 2025 "Rotation of Space Habitats" PDF**: not opened. | (none stated in the source) |
| 13 | **Morrison 2018 thesis** (halo-orbit insertion of cyclers): PDF bot-gated (row 79). | (none stated in the source) |

---

## Batch 13: from `mercury_as_industrial_site.md` (582 lines; 11 open threads)

*(Entered 2026-10-11 from the source file's "Open threads" section; the source's wording is kept. "Next:" is the source's own suggestion; where the source gave none, the cell says so.)*

| # | Item | Search next |
|--:|---|---|
| 1 | **Free-metal content of the regolith.** Not measured; BepiColombo MIXS and a landed XRD (>1 wt% detection) are the routes. | McCubbin et al. 2017 (JGR) on Si-rich metal; BepiColombo MIXS first results. |
| 2 | **Regolith bulk density, grain size, strength, thermal inertia.** Mitchell and de Pater 1994 (Icarus 110:2-32) and Vasavada et al. 1999 (Icarus 141:179) could not be opened (403/404). | BepiColombo MERTIS first results; Bauch et al. 2021 (Icarus, surface temperatures for MERTIS). |
| 3 | **North-pole maximum illumination fraction.** Not found; Hamill et al. 2020 (PSJ 1:57) located but the PDF was dead. | (none stated in the source) |
| 4 | **Radiation dose at Mercury and on its surface.** No dose rate found. BERM (Pinto et al. 2022, Space Sci. Rev.) located but no dose number seen; MESSENGER design dose requirement not found. | (none stated in the source) |
| 5 | **BepiColombo MPO array design limits** (nominal and survival cell temperatures, power, test degradation): seen only in a search summary of E3S/DOAJ pages that returned 403. | ESA ESPC proceedings mirror, or Airbus papers. |
| 6 | **Processing of high-sulfur, high-alkali regolith.** No study found. | molten oxide electrolysis and sulfur; vacuum pyrolysis volatility series for Na and K; McCubbin 2017 smelting hypothesis. |
| 7 | **Electrolytic magnesium from silicate feed, energy per kg.** Only a terrestrial silicothermic figure in coal equivalent was found. | (none stated in the source) |
| 8 | **Mercury mass driver / launch loop / Mercury industrialization studies.** None found in three extended searches here and in the sibling. | Criswell 1986 (planet deconstruction), Ehricke's Mercury studies (AIAA 67-28, cited by [PAL17]), JBIS archives. |
| 9 | **Low circular orbit lifetime at Mercury.** Only MESSENGER's eccentric-orbit decay found. | frozen-orbit studies for BepiColombo MPO (480 x 1,500 km) such as the Zaragoza averaged-model paper (located, not read). |
| 10 | **Exact conjunction durations** with Mercury's real orbit (eccentricity and inclination); D10 is a circular model. | (none stated in the source) |
| 11 | **Sources found but not read:** Peplowski et al. 2016 (Nature Geoscience, carbon) full text; Lawrence et al. 2013 (Science, ice) full text; Chabot et al. 2018 polar deposits chapter; BERM paper; Hamill 2020; Zaragoza Mercury orbit paper (zaguan.unizar.es record 130420); NTRS 20120010094 (polar, not opened). | (none stated in the source) |

---

## Batch 14: from `venus_as_extraction_site.md` (437 lines; 14 open threads)

*(Entered 2026-10-11 from the source file's "Open threads" section, which is headed "Not found, or not confirmed:"; the source's wording is kept. "Next:" is the source's own suggestion; where the source gave none, the cell says so.)*

| # | Item | Search next |
|--:|---|---|
| 1 | A real (not ideal) energy figure for nitrogen separation from a CO2-N2 mixture (membrane, adsorption or cryogenic); only the thermodynamic floor is here (D5). | (none stated in the source) |
| 2 | Any plant-scale study of sulfuric acid droplet collection, or of acid cracking for hydrogen on Venus; the liquid-phase enthalpy of formation and vaporization enthalpy of H2SO4 were not sourced (the NIST page gave the gas only). | (none stated in the source) |
| 3 | A clean (not OCR-degraded) density table for 75 to 92 wt% sulfuric acid. | (none stated in the source) |
| 4 | Gamma-ray K, U and Th abundances from Venera 8, 9, 10 and Vega 1, 2 (named in Klingelhoefer and Fegley 2000; not extracted). | (none stated in the source) |
| 5 | Any study of electromagnetic launch, rotating tethers, or beamed propulsion for Venus ascent. | AIAA and JBIS for "Venus" with "tether" and "launch", and NIAC final reports. |
| 6 | Venus surface mining or ore-lifting engineering (none exists in what was found). | (none stated in the source) |
| 7 | Lorenz 2018 lightning review (Springer login loop); Gilmore et al. 2017 surface composition review (same); Marcq et al. 2018 composition review (HAL, ANU, ORFEO all failed); Fedorova et al. 2008 (HAL failed); Hecht et al. 2021 MOXIE instrument paper (MIT DSpace 405) for MOXIE's power breakdown; Treiman 2007 (Wiley). | (none stated in the source) |
| 8 | Kerzhanovich et al. 2005 dual-balloon full text (lift numbers); TOBIAS tether length and towbody mass. | (none stated in the source) |
| 9 | Total near-Earth-object mass and measured volatile contents of returned C-type samples (Ryugu, Bennu) for a better comparison than CI chondrites (not searched; would be the next angle on checklist 2). | (none stated in the source) |
| 10 | Newer lunar polar water totals (LRO, Mini-RF, later analyses) to replace the 2.9 x 10^12 kg upper scenario. | (none stated in the source) |
| 11 | Primary VEGA balloon paper (Sagdeev et al., Science 1986) for envelope mass; only Dorrington's account was read. | (none stated in the source) |
| 12 | The VIRA tables (Seiff et al. 1985), still missing (GRV), which would settle Conflicts 4. | (none stated in the source) |
| 13 | Post-2016 status of aerocapture readiness at Venus. | (none stated in the source) |
| 14 | **Found but not read:** Lorenz 2018 (Prog. Earth Planet. Sci., doi:10.1186/s40645-018-0181-x); arXiv:2208.05582 (aerial platform mission architecture); arXiv:2412.06830 ("A New Strategy for the Exploration of Venus"); NTRS 20205007668 (deep space habitat with a Venus flyby); Dorrington, "Venus atmospheric platform options revisited", Adv. Space Res. (2010, ScienceDirect); the 2026 mass-inventory compilation arXiv:2603.17561; ResearchGate "Evaluation of materials for Venus aerobot applications". | (none stated in the source) |

---

## Batch 15: from `inner_system_logistics_network.md` (849 lines; 12 open threads)

*(Entered 2026-10-11 from the source file's "Open threads" section; the source's wording is kept. "Next:" is the source's own suggestion; where the source gave none, the cell says so.)*

| # | Item | Search next |
|--:|---|---|
| 1 | **Mercury-to-Earth and Mercury-to-Venus cargo trajectories with flybys:** no study found; only outbound (Earth-to-Mercury) designs (rows 4-6, 12, 22, 50). | Langevin, Acta Astronautica 47 (2000) 443-452 (paywalled); C. W. Yen, "Ballistic Mercury orbiter mission via Venus and Mercury gravity assists", J. Astronautical Sciences 37 (1989) (not located); NTRS 19740013378 (found, not opened); the ScienceDirect paper "Solar sail missions to Mercury with Venus gravity assist" (found, not opened). |
| 2 | **Earth-Venus cycler numbers:** Hollister and Menning's own papers and the Jones-Hernandez-Jesick triple-cycler full text (ResearchGate, not readable by the tools) were not obtained; only abstracts (rows 13-21, 109). | (none stated in the source) |
| 3 | **BepiColombo transfer-module array power versus Sun distance:** Steiger et al. Fig. 14 is a plot (not extracted as numbers); the ESPC 2017 array papers returned HTTP 403 (row 34); the "about 13 kW peak" figure came only from a search summary. | ESA BepiColombo Red Book, the 2011 ESPC paper via another host. |
| 4 | **Sail lifetime and degradation near the Sun**, and optimal-control sail transfer times above about 0.5 mm/s^2 (D6's simple law fails there). | McInnes, *Solar Sailing* (1999); Dachwald's slides (found, not opened); NASA sail degradation studies. |
| 5 | **High-Isp electric propulsion on water** (performance of AQUAHET or ion thrusters on water): no figures found (rows 94-96). | (none stated in the source) |
| 6 | **Release accuracy of a mass driver for an interplanetary throw**, and catcher dynamics at Sun-Mercury L1/L2 (Mercury's Hill radius about 221,000 km): no source. | (none stated in the source) |
| 7 | **A sized destination processing node** for bulk inner-system cargo: none found. | (none stated in the source) |
| 8 | **Relay constellations for conjunctions** (count, orbit, power): only the qualitative recommendation of Morabito and Hastrup (row 77). | (none stated in the source) |
| 9 | **Radiation dose to electronics at 0.3 to 0.5 AU** (MESSENGER and BepiColombo radiation-monitor data), and solar-wind and dust environment at Mercury orbit: not searched in depth. | (none stated in the source) |
| 10 | **Venus cloud-level composition** (the NSSDC mixing ratios are near-surface): not searched. | (none stated in the source) |
| 11 | **Space solar power exported from Mercury or another inner site:** no published engineering concept found (row 87). | (none stated in the source) |
| 12 | **Sources found but not read:** arXiv 1706.05443 (SEP radial dependence model); arXiv 0809.3535 (beryllium hollow-body sail; likely source of the killed 1,000 K claim, row 63); Kim, Hu, Cucinotta (AIAA 2005) on acute exposure; Posner, Space Weather (2007) paper itself; NASA STRG page on an Earth smallsat aerocapture test; Georgia Tech aerocapture theses; Hughes, Macdonald et al., "Terrestrial planet sample return missions using solar sail propulsion" (Strathprints 6245). | (none stated in the source) |

---

## Batch 16: from `planet_deconstruction_literature_and_engineering.md` (353 lines; 12 open threads)

*(Entered 2026-10-12 from the source file's "Open threads" section; the source's wording is kept. "Next:" is the source's own suggestion; where the source gave none, the cell says so.)*

| # | Item | Search next |
|--:|---|---|
| 1 | **Dyson 1966** ("The search for extraterrestrial technology"): text not found online; it would give Dyson's own disassembly mechanism and numbers. | a library copy of *Perspectives in Modern Physics* (1966), or Dyson's *Selected Papers* (1996). |
| 2 | **Criswell 1985** chapter (pp. 50-87): lending-restricted on the Internet Archive | a library loan. Wright cites it as the reference for deconstructing planets. |
| 3 | **Published A&S** (*Acta Astronautica* 89, 2013): closed access; check whether sec. 4.2 and its numbers survived publication. | (none stated in the source) |
| 4 | **Benz et al. 2007** ("The Origin of Mercury", *Space Sci. Rev.* 132): blocked by the publisher's cookie redirect; Asphaug and Reufer 2014 (*Nature Geoscience*) not opened. | (none stated in the source) |
| 5 | Kolm et al. 1980 MIT report on electromagnetic guns (A&S ref. 37) and the coilgun-efficiency claims behind A&S sec. 4.3: not opened. | (none stated in the source) |
| 6 | No peer-reviewed critique of A&S's disassembly section was found; only forum discussion (rejected). Searching citing papers of A&S (96 citations per OpenAlex) for "Mercury" would be the next step. | (none stated in the source) |
| 7 | Slingatron throughput and status (Tidman's NSS papers surfaced, not read). No source at all was found for electromagnetic acceleration of loose, uncontained material (as opposed to payload packages); every launcher design read throws discrete payloads. | (none stated in the source) |
| 8 | A second, independent source for Lacki's collision-time ratio at Mercury's distance (only his 1 AU and 0.32 AU rows were used). | (none stated in the source) |
| 9 | Catching and orbital processing at planetary rates: no source found that sizes the orbital factories or a placement rate. | (none stated in the source) |
| 10 | Hephaistos contamination and radio follow-up papers (arXiv:2405.14921, 2501.05152) surfaced by title only. | (none stated in the source) |
| 11 | The thermodynamic concentration limit in suns (Gleckman et al. 1989 PDF) not read; the étendue point here rests on the photosphere-flux arithmetic and the paper's abstract. | (none stated in the source) |
| 12 | The Galaxies 2022 Kardashev-timeline paper and Hanson's "Burning the cosmic commons" surfaced and were not read (forecasts and economics, not engineering). | (none stated in the source) |

---

## Batch 17: from `mercury_whole_planet_inventory_and_extraction.md` (392 lines; 12 open threads)

*(Entered 2026-10-12 from the source file's "Open threads" section; the source's wording is kept. "Next:" is the source's own suggestion; where the source gave none, the cell says so.)*

| # | Item | Search next |
|--:|---|---|
| 1 | **Measured bulk composition:** none exists; BepiColombo enters Mercury orbit in November 2026 (row 59) and may tighten C/MR^2, the core radius and the inner core. Re-search after its first interior results. | (none stated in the source) |
| 2 | **Morgan and Anders 1980 table:** could not be opened (rows 3-4); [ES17] states its assumptions are invalidated, so it was not pursued further. | (none stated in the source) |
| 3 | **Hauck et al. 2013 (JGR Planets), Namur et al. 2016a/b, Knibbe and van Westrenen 2015/2018, Brown and Elkins-Tanton 2009:** cited inside the reviews read; full texts not opened. | arXiv or institutional repositories. |
| 4 | **Present-day surface heat flux:** only derived here (13.8-16.7 mW/m^2); [KNI25] Fig. 2c plots it but was not read off. | Tosi 2013 full text; Peterson 2021. |
| 5 | **Temperature profile with depth:** only boundary values found; the linear interpolation in D3 is a stand-in. | PRMM temperature table, Tosi 2015 3-D models. |
| 6 | **Melt fraction on unloading:** needs a thermodynamic melting model (pMELTS-type) for Mercury mantle compositions under instant unloading; none found. | (none stated in the source) |
| 7 | **Low-pressure liquidus of Fe-Si-S alloys and their vapor pressures (Si, S):** not searched beyond pure Fe (time spent on the bulk models instead). | Fe-Si phase-diagram handbooks. |
| 8 | **Nitrogen and noble gases on Mercury:** no measurement found (row 45). | (none stated in the source) |
| 9 | **Total rock moved on Earth per year including waste rock:** not found; only recoverable content, all materials and tailings. | (none stated in the source) |
| 10 | **Primary source for Bagger 293 capacity** (TAKRAF document) and for the Kola borehole: only secondary pages. | (none stated in the source) |
| 11 | **Any engineering study of planetary-scale excavation, liquid-metal handling, or tailings disposal:** none found (rows 38-39). | (none stated in the source) |
| 12 | **Sources found but not read:** Schandl et al. 2024 (J. Ind. Ecol., 403); UNEP GRO 2024 full report (403); Global Tailings Review ch. VII (HTML shell); Maclennan 2002 (HTML shell); Tosi et al. 2013 full text. | (none stated in the source) |

---

## Batch 18: from `venus_whole_planet_inventory_and_stripping.md` (395 lines; 10 open threads)

*(Entered 2026-10-12 from the source file's "Open threads" section; the source's wording is kept. "Next:" is the source's own suggestion; where the source gave none, the cell says so.)*

| # | Item | Search next |
|--:|---|---|
| 1 | **Fogg 1987 (JBIS 40, 551-564), Adelman 1982 (JBIS 35, 3-8), Smith 1989 (JBIS 42, 571-576), Birch 1993 (JBIS 46, 311-313, abstract only), Birch 1991 "Supramundane Planets" (JBIS 44, 169-182):** not open; the BIS shop sells them. The hydrogen figure and the Mercury Ca/Mg import (0.5% of Mercury's mass) trace to one of these. | (none stated in the source) |
| 2 | **Zubrin and McKay as named in the brief:** the 1993 Zubrin and McKay paper is a Mars paper (MVT 3.11); no Venus atmosphere removal study by them was found; Zubrin 1990 (NIMF propellants) is used here instead. A further search would target Zubrin's books (not primary). | (none stated in the source) |
| 3 | **Gladman et al. 1996 (Science 271, 1387):** the Venus ejecta fractions; not open. Would replace the Mercury analog in 3.5. | (none stated in the source) |
| 4 | **Correia and Laskar 2001/2003 and Ingersoll and Dobrovolskis 1978:** for a proper despinning timescale without thermal tides (the 18 Myr in D5 is a crude scaling). | (none stated in the source) |
| 5 | **Konopliv and Yoder 1996** (k2) and **Amorim and Gudkova 2023** (PREM-based structure): read only via citing papers. | (none stated in the source) |
| 6 | **Venus basalt thermal properties at 300 to 750 K** and a bare-surface albedo: no Venus measurement exists; D8 uses terrestrial values and a lunar albedo. | (none stated in the source) |
| 7 | **Whether carbonates exist on Venus** (Fegley 2004 lists arguments for and against): decides whether removal of the air would be followed by outgassing from the surface. | (none stated in the source) |
| 8 | **Decompression or unloading effects on volcanism** when 9.2 MPa is removed: no study found. | (none stated in the source) |
| 9 | **World mining throughput** as an anchor for the excavation rates in D4: not searched here (the Mercury inventory agent's checklist covers it; not read, per the rules). | (none stated in the source) |
| 10 | **Venus Express absolute ion escape rates** were read only through Gillmann 2022 (Barabash 2007 full text not open). | (none stated in the source) |

---

## Batch 19: from `planetary_scale_power_and_heat.md` (650 lines; 10 open threads)

*(Entered 2026-10-12 from the source file's "Open threads" section; the source's wording is kept. "Next:" is the source's own suggestion; where the source gave none, the cell says so.)*

| # | Item | Search next |
|--:|---|---|
| 1 | **Launcher pulsed-power efficiency, end to end** (bus to coils, including switching and storage): not found (row 78). | DTIC ADA192102 and ADA143778 (surfaced, not opened); UT-CEM compulsator reports; the papers Armstrong and Sandberg cite for coilgun and quenchgun efficiency (their refs 38-40). |
| 2 | **Planet-side heat removal by any means other than surface radiation:** hot-payload export (D8 suggests it closes only for very efficient launchers), heat carried away by launched coolant, or launchers in orbit around the planet fed by tether or skyhook. No source found; this is the first thing to search next. | (none stated in the source) |
| 3 | **Sink temperature inside a dense swarm:** Wright 2023's optical-depth treatment is for the whole swarm; the radiator sink for elements inside a swarm of optical depth near 1 was not computed or found. | (none stated in the source) |
| 4 | **Degradation rates near the Sun:** MESSENGER and BepiColombo array degradation per year in flight (only the BepiColombo test figure in [ME] and the Helios qualitative account were found); the ICES paper "Parker Solar Probe Solar Array Cooling System In-Orbit Performance Review" (TTU repository, 403 both ways). | (none stated in the source) |
| 5 | **Hot-cell efficiency data:** Landis 2023 chapter (NTRS 20230002489, abstract only); INTA HTHI temperature coefficients (restricted); arXiv 2608.11113 (high-temperature PV for solar-electric Oberth maneuvers, surfaced, not opened). | (none stated in the source) |
| 6 | **Primaries not opened:** Dyson 1960 (Science) and 1966; Badescu 1995 (Acta Astronautica 36:135); Criswell 1986 (left to section 1); the full HTS cable paper (Sadeghi et al. 2024, open access); Ignatiev IAC-05 crawler paper (a ~200 kg crawler and "1 MW in several years" in a search summary). | (none stated in the source) |
| 7 | **Mercury trace elements for cells:** Ga, In, As, Ge, P, B abundances at Mercury's surface (not found; only CI-chondrite values in [PR]). | (none stated in the source) |
| 8 | **Venus's infrared absorptivity** if lit by a hot swarm instead of sunlight (D10 assumes ~1). | (none stated in the source) |
| 9 | **Heat capacity of silicate rock above 350 K** (D8 uses the 350 K Apollo value as a lower bound; real hot rock carries more). | (none stated in the source) |
| 10 | **Large-array specific power with flight mass:** iROSA wing mass (not published in what surfaced); the NASA SoA 2024 power chapter table (PDF not surfaced). | (none stated in the source) |

---

## Batch 20: from `orbital_dynamics_of_planetary_harvesting.md` (420 lines; 9 open threads)

*(Entered 2026-10-12 from the source file's "Open threads" section; the source's wording is kept. "Next:" is the source's own suggestion; where the source gave none, the cell says so.)*

| # | Item | Search next |
|--:|---|---|
| 1 | **No N-body study of removing or reducing Venus or Mercury exists in what surfaced** (S3r, S7). | run a REBOUND or Mercury6 ensemble (with GR) with Venus's mass ramped down over 10^3 to 10^7 yr, measuring Mercury's e and Earth's eccentricity spectrum; search terms "planet mass removal secular resonance sweeping terrestrial", "Venus mass Milankovitch", and the Kane / Horner / Vervoort group's other papers (refs 28, 38, 74 in F8 not opened). |
| 2 | Second-order secular theory or a published secular code would place g5 correctly; my estimates bracket the error instead. | (none stated in the source) |
| 3 | Gladman et al. 1996 Science 271:1387 (paywalled) and Melosh & Tonks 1993 not opened; the 30% Venus-to-Earth figure is second-hand. | (none stated in the source) |
| 4 | Stenborg & Howard 2018 and Jones et al. 2013/2017 not opened directly (numbers via NASA news). | (none stated in the source) |
| 5 | Station-keeping cost at Sun-Mercury and Sun-Venus L1/L2 with solar radiation pressure: no study found | "libration point orbit Mercury Sun L1 BepiColombo station keeping" and "solar sail displaced L1 Mercury". |
| 6 | Correia & Laskar 2001 and 2004 (Nature) read only at abstract level; Margot et al. 2012 C/MR^2 and Genova et al. 2019 only via summary. | (none stated in the source) |
| 7 | No study of launch torque on a planet's spin, of mass-driver recoil on a planet's orbit, or of tidal stress during planetary unloading was found. | "mass driver torque planet rotation", "asteroid spin change mass driver ejecta" (asteroid-deflection literature is the nearest analog), "global unloading decompression melting planet". |
| 8 | The heliocentric dust-input rate of the natural cloud (600 to 10,000 kg/s in summaries) was not confirmed on a page. | (none stated in the source) |
| 9 | Not covered: Yarkovsky drift of meter-to-kilometer cargo near Mercury (Xu et al. 2022 and Lacki 2025 point to it); the effect of a large co-orbital swarm's own mass on Mercury (negligible unless the swarm approaches a planetary mass). | (none stated in the source) |

---

## Batch 21: from `oxygen_and_hydrogen_supply_for_mars_water.md` (432 lines; 13 open threads)

*(Entered 2026-10-12 from the source file's "Open threads" section; the source's wording is kept. "Next:" is the source's own suggestion; where the source gave none, the cell says so.)*

| # | Item | Search next |
|--:|---|---|
| 1 | **Comet and Kuiper-belt water inventories**: the Choukroun et al. 2020 review (Space Sci. Rev. 216) could not be read (bot walls at HAL and BORIS; DLR abstract has no numbers). | arXiv copy of the review; Rosetta 67P mass and porosity papers. |
| 2 | **Phobos and Deimos water and oxygen content**: unmeasured; MMX returns samples in 2031. | Murchie or Fraeman spectral papers on 2.7 um band depths. |
| 3 | **Any oxygen process on a high-sulfur, high-alkali feed (Mercury)**: none found twice (rows 62-63; sibling F10). | (none stated in the source) |
| 4 | **Non-rocket export from Venus**: none found twice (row 61; sibling row 76). | (none stated in the source) |
| 5 | **A capture-and-store solar-wind collector**: none found (rows 29-31). The SWIFT papers (IAC-14, IAC-15) were read as abstracts only; their full texts might give inlet mass per area. | (none stated in the source) |
| 6 | **In-orbit LH2 boil-off measured on a flight tank**: not found; only models and ground tests (rows 47-51). | CRYOTE and Starship propellant-transfer flight data when published. |
| 7 | **Hydrogen and oxygen flammability and detonation limits** (for the safety row in F8): not sourced this session. | (none stated in the source) |
| 8 | **Water fusion and sublimation enthalpies** (for ice-melting energy): the NIST phase-change page did not return values (row 58). | (none stated in the source) |
| 9 | **Clathrate hydrate and hydrazine handling data**, and metal-hydride release temperatures: not sourced. | (none stated in the source) |
| 10 | **Iron(III) oxide reduction enthalpies**: NIST pages without values (row 54). | (none stated in the source) |
| 11 | **Mars mid-latitude ice volume**: only qualitative here ("100s of meters"); SHARAD volume papers not opened. | (none stated in the source) |
| 12 | **A low-thrust Mercury-to-Mars trajectory study**: none; D7's 30 km/s is an Edelbaum-style estimate. | (none stated in the source) |
| 13 | Found and not read: arXiv 1407.4258 (CME review), arXiv 1204.2776 (slow-wind helium), arXiv 2306.03164 (Metzger thermal extraction model), NTRS 20160013682 (M-WIP NTRS copy), NASA Mars ice drilling assessment, NTRS 20070014073 (lunar solar-wind volatile loss). | (none stated in the source) |

---

## Batch 22: from `mars_water_budget_and_retention.md` (415 lines; 8 open threads)

*(Entered 2026-10-12 from the source file's "Open threads" section; the source's wording is kept. "Next:" is the source's own suggestion; where the source gave none, the cell says so.)*

| # | Item | Search next |
|--:|---|---|
| 1 | Papers seen only as abstracts or press releases: Stone et al. 2020 (Science 370:824; LPL copy 404); Chaffin et al. 2021 full text (INAF copy no connection, OU 403); Gunell et al. 2018 (A&A 403); Haberle et al. 2001 JGR (only a search summary; the NTRS hit was a different paper); Nerozzi and Holt 2019 GRL; Levy et al. 2014 JGR; Putzig et al. 2009 Icarus (Smithsonian copy 403; dust fraction of the NPLD not found); Wernicke and Jakosky 2021 (hydrated minerals; DOI unknown); Stuurman et al. 2016 GRL; Orosei et al. 2018 (LPL copy returned HTML); Melosh and Vickery 1989; McKay et al. 1991 (Nature); Villanueva 2015 full paper; Lasue et al. 2013 (HAL bot wall). | (none stated in the source) |
| 2 | **Energy-limited cap on hydrogen escape** if delivered water raised the upper-atmosphere hydrogen far above today's: needs the XUV flux at Mars and an efficiency (Ramstad 2017's F_XUV scaling is a lead). | "energy-limited escape Mars hydrogen XUV flux MAVEN EUVM". |
| 3 | **How a deliberately thickened, warmed atmosphere changes the cold trap**: a GCM study of water transport to the homopause under 10 to 1,000 mbar (Green 2017 planned such runs; none published found). The closest analog found is the high-obliquity model (Gilli 2025, 18.5 x more H loss in a wetter atmosphere). | "Mars GCM thicker atmosphere water vapor homopause hydrogen escape terraformed". |
| 4 | **Emirates Mars Mission hydrogen escape 2021 to 2023** (Chaffin et al., EGUsphere 2023): abstract read (seasonal factor >10); absolute rates and the full paper not opened. Space Science Reviews 2024 review "Mars' water cycle and escape" behind a login. | (none stated in the source) |
| 5 | **Rock oxygen inventory of Mars** (for combining imported hydrogen with local oxygen): not quantified here; sibling section 6 (`oxygen_and_hydrogen_supply_for_mars_water.md`) is the place; I did not read it (not in my read list). | (none stated in the source) |
| 6 | **The solar wind's own hydrogen mass fraction** was not sourced; D6 uses the photosphere value (0.7438) as a stand-in. | (none stated in the source) |
| 7 | **Infiltration rate** of delivered liquid water into Martian regolith and megaregolith: no number found. | (none stated in the source) |
| 8 | **Nitrate inventory**: only "about 300 ppmw" in sands (Ansari, citing Stern 2015); a global inventory was not found. | (none stated in the source) |

---

## Batch 23: from `benefits_of_mining_mercury.md` (454 lines; 9 open threads)

*(Entered 2026-10-12 from the source file's "Open threads" section; the source's wording is kept. "Next:" is the source's own suggestion; where the source gave none, the cell says so.)*

| # | Item | Search next |
|--:|---|---|
| 1 | **No Mercury process study** (regolith to oxygen, Mg, Al, Si) and no Mercury regolith density, strength or free-metal content ([ME] Open threads). | BepiColombo MIXS/MERTIS results; McCubbin et al. 2017 on Si-rich metal. |
| 2 | **Aluminum and magnesium energy, second primary source.** IAI statistics pages render by script (rows 5, 9) and the BlueGreen benchmark is a chart only (row 65). | IAI annual statistical PDFs; IEA Aluminum tracking report; a peer-reviewed magnesium life-cycle study that states whole-plant electricity (none was opened this session). |
| 3 | **Silicon metal energy, second source.** Schei, Tuset, Tveit, *Production of High Silicon Alloys* (1998), cited by [KSI16], not opened; NREL fy25osti/89464 not reachable (row 22). | (none stated in the source) |
| 4 | **Low-iron glass specification** (Fe2O3 limit and transmittance) from a standard or peer-reviewed source (rows 59-60). | (none stated in the source) |
| 5 | **Heat-engine power between sunlit rims and cold traps at Mercury**: no concept found (row 35). | lunar thermal-wadi and regolith thermal-storage papers (HAL 02887846 located, not opened) adapted to Mercury's 88-day night. |
| 6 | **Mercury-sourced sunshades or collectors** for Venus or Earth: none found (rows 42-47). Venus-sunshade masses in terraforming reviews were seen only in summaries (row 45). | (none stated in the source) |
| 7 | **Near-Sun missions using Mercury or Mercury flybys** to reach low perihelia: none found; the D2 arithmetic is impulsive and coplanar and ignores flybys of Venus or Mercury that a real trajectory would use. | (none stated in the source) |
| 8 | **Dose at Mercury for electronics** (needed for F6): still no number ([ME] Open threads). | (none stated in the source) |
| 9 | **Sources found but not read**: Harrop and Schulze-Makuch 2010 (IJAsB 9:89, solar-wind power satellite); Google's Suncatcher preprint; Hamill 2020 polar illumination; HAL 02887846 (lunar thermal storage). | (none stated in the source) |

---

## Batch 24: from `benefits_of_mining_venus.md` (416 lines; 13 open threads)

*(Entered 2026-10-12 from the source file's "Open threads" section; the source's wording is kept. "Next:" is the source's own suggestion; where the source gave none, the cell says so.)*

| # | Item | Search next |
|--:|---|---|
| 1 | **A real separation energy for N2 from a CO2-N2 mixture** (membrane, adsorption, cryogenic); only the floor is known ([VE] D5). | (none stated in the source) |
| 2 | **Crop nitrogen inventory per person in a closed habitat** (biomass plus soil); SP-413 lists masses but not nitrogen content. | (none stated in the source) |
| 3 | **Bulk nitrogen of Ryugu and Ceres**, and the confirmed comet values (Fray et al. 2017, Bardyn et al. 2017, MNRAS; both blocked by Cloudflare at OUP and Anubis at HAL) | ADS full text, Rosetta archive summaries. |
| 4 | **The nitrogen release temperature and yield from carbonaceous material** (only water release was found, via [SYN]). | (none stated in the source) |
| 5 | **A delta-v figure for the Venus-swing-by saving on crewed Mars missions** (NTRS abstracts give none | the Drake 2013 slides and Wooster et al. 2007, "Mission design options for human Mars missions"). |
| 6 | **Titan as a nitrogen source** (lecture-slide lead: about 9 x 10^18 kg of N2) | NSSDC Saturnian satellite fact sheet and Huygens surface pressure, to derive it. |
| 7 | **A molten-carbonate electrolysis plant energy figure at scale** from a peer-reviewed source (the Tampere/Elsevier paper returned HTML; the Licht figure is from a competition submission). | (none stated in the source) |
| 8 | **The Acta Astronautica papers** "Feasibility of power beaming through the Venus atmosphere" (2023) and "Venus Aerial Platforms: Long-Lived Balloons with ISRU for Buoyant Gas Replacement" (2026): found, paywalled, not read. | (none stated in the source) |
| 9 | **A shielding comparison with numbers** (dose per g/cm^2 for carbon, CO2 ice or basalt against polyethylene). | (none stated in the source) |
| 10 | **Plant nitrogen minimum** (the "10 mbar" attributed to McKay et al. 1991): needs the Nature paper or McKay and Marinova 2001. | (none stated in the source) |
| 11 | **Basalt-fiber properties and composition limits** from a peer-reviewed review (MDPI blocked). | (none stated in the source) |
| 12 | **Phosphorus in the lower cloud** (Vega, [VE] 3.1): no abundance found; phosphorus is a fertilizer input Venus may or may not supply. | (none stated in the source) |
| 13 | Found but not read: Penn State pure.psu.edu records on lithium-combustion power (2018 to 2020); the Southampton Hall-thruster propellant review; Wikipedia's Parker Solar Probe page (not needed). | (none stated in the source) |

---

## Batch 25: from `benefits_of_mining_the_sun.md` (440 lines; 11 open threads)

*(Entered 2026-10-12 from the source file's "Open threads" section; the source's wording is kept. "Next:" is the source's own suggestion; where the source gave none, the cell says so.)*

| # | Item | Search next |
|--:|---|---|
| 1 | **Gloeckler and Geiss (1998), Space Sci. Rev. 84:275** (Ulysses SWICS 3He/4He in slow vs fast wind): record found, every copy blocked (rows 22, 23). | an ADS full-text scan or a library copy. |
| 2 | **Bochsler (2007), "Minor ions in the solar wind"** (A&A Rev.): both copies dead (first-run rows 15, 16). Would give a second compilation of wind abundances by regime. | (none stated in the source) |
| 3 | **Genesis Mg and Fe fluences (Jurewicz et al. 2019; Burnett et al. 2017):** appear only in a search summary (row 19); the 2020 Jurewicz paper read (row 69) gives isotopes only. They would fix the absolute metal yield without the H normalization. | (none stated in the source) |
| 4 | **The APL Interstellar Probe study report and the full McNutt et al. 2022 paper:** the SOM verdict is read only through Centauri Dreams (rows 44 to 47). | the report on the APL Interstellar Probe site. |
| 5 | **Solar-thermal propulsion flight Isp with hydrogen**; the "760 s demonstrated" claim is only in a search summary (row 63). | AIAA papers on the Solar Thermal Upper Stage; McNutt AIAA-2001-3377 (dead copy, row 43). |
| 6 | **Sail degradation near the Sun** (polyimide limit 520 K, [NW]) | McInnes, *Solar Sailing* (1999), and the Solar Cruiser materials data. |
| 7 | **A measured escaping-positron flux in the corona or solar wind**: none found (rows 58, 59). | PSP or Solar Orbiter energetic-particle instrument papers on positrons. |
| 8 | **Caplan (2019) and Svoronos (2020) full texts**: abstracts only. | (none stated in the source) |
| 9 | **NASA OTPS appendix tables** (mass by subsystem) were not read line by line; they would resolve Conflict 6. | (none stated in the source) |
| 10 | **Sources found but not read:** arXiv 2307.12411 ("Chasing Nomadic Worlds"); Energy Institute 2026 Review PDF (blocked); journaldephysique jp4:1999309 (blocked); Fleishman et al. (flare positrons, microwave detection). | (none stated in the source) |
| 11 | **Not searched:** UV dose for sterilization near the Sun (dry heat suffices, F6); the economics of any solar product (sibling `value_and_markets_of_inner_system_materials.md` covers markets). | (none stated in the source) |

---

## Batch 26: from `value_and_markets_of_inner_system_materials.md` (507 lines; 12 open threads)

*(Entered 2026-10-12 from the source file's "Open threads" section; the source's wording is kept. "Next:" is the source's own suggestion; where the source gave none, the cell says so.)*

| # | Item | Search next |
|--:|---|---|
| 1 | **Xenon, krypton and argon prices.** USGS publishes none; NASA's 2015 paper shows the history only in a figure. | the original Betzendahl or Linde market reports, or Lindner 2023's price slide ([TR] source), read directly. |
| 2 | **Current helium-3 price.** Only the 2011 CRS figure is primary. | the DOE Isotope Program (isotopes.gov) price list or a NIDC auction notice. |
| 3 | **Current vendor launch prices.** SpaceX's capabilities and rideshare pages are script-rendered and returned no text (rows 15, 17). | an archived copy (Internet Archive) or a GAO or NASA OIG report quoting the contract price. |
| 4 | **Space solar-array cost per watt.** No primary source found (rows 50, 51). | AFRL ROSA program reports, or NASA OTPS 2024 Appendix B (its manufacturing cost inputs), which I did not read. |
| 5 | **Mass-produced spacecraft cost per kg** (Starlink, OneWeb): no primary source found; Hein's $10,000/kg rests on it. | (none stated in the source) |
| 6 | **Studies cited only through Metzger:** Kornuta et al. 2019 (paywalled, row 61), Jones et al. SciTech 2019, Charania and DePasquale 2007, Bennett et al., Shisko's review, Ross et al. 2009 and Andrews and Andrews (elasticity). Not opened. | (none stated in the source) |
| 7 | **Earth-return mass fraction for valuable cargo** (capsule mass per kg returned): only secondary figures found (row 60). | (none stated in the source) |
| 8 | **A historical analog of a supply flood** (for example aluminum's price after electrolytic production, USGS Data Series 140 historical statistics): not searched; it would test Nachtrieb and Smith's 5.5-fold collapse against history. | (none stated in the source) |
| 9 | **World electricity 2025** read only from a search summary (row 58); IEA *Electricity 2026* not opened. | (none stated in the source) |
| 10 | **No study prices any material from Mercury, Venus or the solar wind**, and none sizes a receiving and processing node ([NW] F5). Every Mercury, Venus and solar-wind figure in F and G is this file's derivation. | (none stated in the source) |
| 11 | **NASA OTPS LCOE method** (C6): the discounting and availability assumptions behind $0.61/kWh not read in full. | (none stated in the source) |
| 12 | **Mars-surface delivered price**: no observed price exists (no commercial Mars delivery); the floor in D6 is propellant-only. | (none stated in the source) |

---

## Proposed research topics

| # | Topic | Raised | Notes |
|--:|---|---|---|
| P1 | **DONE 2026-10-11** (`research/waste_heat_utilization.md`; open threads in Batch 6). **Waste-heat utilization in a vacuum habitat.** Can a station use the heat it must reject to drive other processes (heat pumps to raise radiator temperature, thermoelectric and organic Rankine conversion, endothermic chemistry, distillation and drying, thermochemical processes)? What the second law and real systems allow at low temperatures. | developer, 2026-10-11 | The developer asked Grok about this "several months ago" and believes the answer was pasted into a file. **Searched on 2026-10-11 and not found:** the only Grok conversation on orbital infrastructure (`to-be-integrated/Conversation with Grok - theoretical logistics for orbital infrastructure.rtf`; an identical copy is in CurrentNovelDocs) is the mass-budget discussion and has no heat content. Treat any Grok answer as an unverified lead; re-source from primary literature. Ask the developer to point to the file or re-paste it. |
| P2 | **PARTLY DONE 2026-10-11: eclipse and shade statistics, sunlight and the heliocentric case are calculated in `body_orbit_eclipse_calculation.md` (Moon, Mars, Jupiter, Saturn; validated on Earth GEO). Still open: heat-storage figures for the Jovian and Saturnian cases beyond the per-kW table there, the battery-cycle-life and PCM-cycling evidence (companion file `lagrange_thermal_environment.md`), orbits about the outer moons, Saturn's rings.** **Heat batteries (thermal energy storage) for stations in orbit** around the Sun, Moon, Mars, Jupiter and Saturn: eclipse and shade statistics per body, storage figures for the Jovian and Saturnian cases, comparison with oversizing batteries or radiators; the heliocentric case (no planetary eclipse). | developer, 2026-10-11 | Synthesis in `waste_heat_utilization.md` §10.2. The file's storage cases are lunar night and ISS-class eclipse only. |
| P3 | **CALCULATED 2026-10-11 in `lagrange_eclipse_calculation.md` (circular model, validated on lunar eclipses; cross-checked with JPL Horizons DE441); sourced mission and heritage evidence in `lagrange_thermal_environment.md` (agent, complete). Results: the Earth-Moon points themselves are unstable (e-folding 318 days) and a station sits on a large one-month orbit; along it about 1 to 1.5 total eclipses a year (at most about 182 min) and 2.4 to 3.2 dimming events a year (at most about 352 min); Sun-Earth L4/L5 have none; a heat battery does not pay at either; a heat pump does not pay in area against the cold sink.** **Thermal environment and heat use at Earth-Moon and Sun-Earth L4/L5 ("grav-locked" stations):** eclipse and Sun-angle statistics from orbital mechanics (calculate, arithmetic shown); radiator and heat-pump sizing for a stated power; which heat uses apply when there is little or no eclipse; what JWST at L2 shows. | developer, 2026-10-11; **for 2026-10-12** | §10.3 of the waste-heat file frames the questions. Results become parameters of an "Orbital habitat at a Lagrange point" class (not yet written). |
