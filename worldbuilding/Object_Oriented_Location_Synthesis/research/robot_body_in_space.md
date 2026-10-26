# Robot body in space and other extreme environments: research file

Created 2026-10-10; completed 2026-10-11. Real physics and engineering data only. No figure is from memory; every number in
the tables comes from a page opened in this session (see SEARCH LOG). Numbers I saw only in search summaries are not used; they
are listed as leads under Open threads.

## 1. Scope

The physical body of a human-shaped, human-sized machine (skin, clothing, gloves; the gel brain is waved per H-1 and not
covered here) in vacuum, in thermal extremes, under radiation, in dust, on low-gravity surfaces and over years of
service. Covers thermal, radiation, vacuum materials, power, mechanics, cold, and reliability. Does not consider
flight or any bending of physics.

Environments the data speak to: low Earth orbit (ISS), Earth's trapped-radiation belts, the lunar surface and lunar night, the
Mars surface, and the Antarctic plateau. Machines used as evidence: Valkyrie, Atlas, Robonaut and Robonaut 2, Canadarm2, the Mars
Exploration Rovers, Curiosity, JPL's COLDArm, and Dartmouth's Cool Robot. Humanoid body masses in the sources run 90 to 136 kg.

## 2. SEARCH LOG

(Appended as the work proceeds. Date of all entries: 2026-10-10 unless noted.)

Method note: WebSearch returns summaries only. To get numbers I downloaded the PDF or page itself with curl, converted it
to text with pdftotext, and read the passage. A number seen only in a search summary is not used in the findings; it is listed
as a lead under Open threads. Marks: useful / thin / dead (died at query = the query could not find it; died at
sources = it was found but no primary source opened or the source was blocked).

| # | Search string or page (verbatim) | Result | Mark |
|--:|---|---|---|
| 1 | `Robonaut 2 thermal vacuum test thermal control design heat rejection NTRS` | Returned Shuttle and ISS radiator reports, no R2 thermal report | dead (query; R2 thermal vacuum report not indexed under these words) |
| 2 | `NASA Valkyrie humanoid robot power consumption watts actuators thermal` | Led to NTRS 20140011889 and arXiv 1902.00187; no continuous-watt figure in any hit | useful (leads) |
| 3 | Page: nasa.gov r5-fact-sheet.pdf | Image-only photo PDF, no specs | dead (source) |
| 4 | Page: NTRS 20140011889 (Radford, "Valkyrie, NASA's new humanoid", 25 Feb 2014 slides) | 125 kg, 44 DOF, 2 kWh battery, 44 motor controllers | useful |
| 5 | Page: arXiv 1902.00187 (Jorgensen et al., IEEE RA-L 2019) | Valkyrie actuator thermal limits and heating times | useful |
| 6 | `Robonaut 2 "thermal" design ISS external environment heater multilayer insulation actuators power dissipation` | General ISS payload thermal pages; no R2 figures | thin |
| 7 | `Robonaut 2 Systems Design thermal ISS "Robonaut 2" torso thermal radiator power 150 W` | Led to NTRS 20100040493, 20110016467 (wrong doc: Tech Briefs) | thin |
| 8 | `Robonaut 2 design hardware overview NTRS 2011 actuators torque power consumption lessons learned` | Led to NTRS 20100040493, 20140000957, 20120014462 | useful (leads) |
| 9 | Page: NTRS 20140000957 (Ahlstrom et al., R2 on ISS status update and IVA mobility, AIAA) | EVA thermal plan: heat sinking, heaters, fans, beta angle | useful |
| 10 | Page: NTRS 20100040493 (Diftler et al., "Robonaut 2, the first humanoid robot in space") | Draft text with gaps ("need reference"); no thermal or watt figures | thin |
| 11 | `Digit humanoid robot specifications battery capacity runtime power Agility Robotics` | Secondary spec aggregators only (qviro, newequipment) | thin (secondary) |
| 12 | `Tesla Optimus AI Day 2022 power consumption walking watts sitting 2.3 kWh battery` | Press coverage quoting 2.3 kWh, 100 W sitting, 500 W brisk walking | thin (secondary; no Tesla primary opened) |
| 13 | `humanoid robot walking power consumption measured watts cost of transport study Atlas Digit Valkyrie energy` | Cost-of-transport press and a Robotica paper (not opened) | thin |
| 14 | Pages: agilityrobotics.com/solution, tesla.com/AIday, figure.ai | Marketing pages, no specs / redirect stub | dead (source) |
| 15 | Page: bostondynamics.com/products/atlas/ and atlas-spec-sheet.pdf (Jan 2026) | 90 kg, 56 DOF, 4 hr, IP67, -20 to 40 C operating | useful |
| 16 | `Tesla AI Day 2022 transcript Optimus "100 watts" "500 watts" walking brisk battery pack 2.3 kilowatt hours` | Same press, no transcript | thin |
| 17 | `Boston Dynamics electric Atlas specification sheet battery capacity kWh operating temperature` | Confirms battery Wh not published | useful (negative) |
| 18 | `Agility Robotics Digit specifications datasheet operating temperature battery 1.5 kWh payload IP rating` | Secondary only; Agility publishes no temp range or IP in hits | thin |
| 19 | `BAE Systems RAD750 radiation-hardened processor datasheet total ionizing dose krad single event upset` | BAE datasheet URL found; curl and WebFetch both got 403 | thin (datasheet blocked; values from search summary only) |
| 20 | `NASA NEPP commercial off-the-shelf electronics total ionizing dose tolerance krad(Si) typical range radiation hardness assurance guideline` | Led to Sinclair and Dyer SSC13-IV-3 | useful (leads) |
| 21 | Page: Sinclair and Dyer, "Radiation Effects and COTS Parts in SmallSats", SSC13-IV-3, AIAA/USU 2013 | TID classes of COTS, shielding sectoring, tungsten, SEU example | useful |
| 22 | `lithium-ion battery cell radiation tolerance gamma total dose capacity degradation krad study` | Led to Gao et al., The Innovation 2023 (Li metal cells) | useful |
| 23 | Page: Gao et al., "Radiation effects on lithium metal batteries", The Innovation, doi 10.1016/j.xinn.2023.100468 | 20 kGy Co-60: capacity retention after 350 cycles | useful |
| 24 | Page: NASA, "Active Thermal Control System (ATCS) Overview", nasa.gov/wp-content/uploads/2021/02/473486main_iss_atcs_overview.pdf | ISS radiator capacity, area, mass, ammonia freeze point | useful |
| 25 | Page: Carrillo, Farner and Preston, "ISS Payload Thermal Environments", NASA TFAWS 2015 short course | Passive flux-cube temperatures on ISS vs absorptance/emittance ratio; EVA touch limit | useful |
| 26 | `NASA/TP-2005-212792 Spacecraft Thermal Control Coatings References solar absorptance emittance table` | Led to Kauder (NASA GSFC, Dec 2005) | useful |
| 27 | Page: Kauder, NASA/TP-2005-212792 (NTRS 20070014757) | Absorptance and emittance of coatings. The PDF text layer is a character-shifted font (every code is 29 below the real one); I decoded it with a script and read the tables | useful (decoded text; values read from decoded tables) |
| 28 | `NIST CODATA Stefan-Boltzmann constant value physics.nist.gov constants`; pages physics.nist.gov/cuu/pdf/wallet_2022.pdf and physics.nist.gov/cgi-bin/cuu/Value?sigma | The wallet PDF fetch failed (server returned an HTTP/SSL error page); the Value?sigma page opened | useful (wallet PDF dead at source) |
| 29 | `total solar irradiance 1361 W/m2 NASA SORCE TIM solar constant 1 AU`; pages arXiv 1605.09788 (IAU 2015 Resolution B3), NASA GSFC TSI science page | Nominal TSI 1361 W/m2 | useful |
| 30 | `Valkyrie humanoid robot R5 average power draw standing walking watts battery life measured IHMC` (extended) | No measured watts for Valkyrie in any hit; only battery capacity (1.8 kWh in a secondary) | dead (sources; no continuous-watt figure published in what I could reach) |
| 31 | `Atlas ATLAS humanoid hydraulic power consumption watts standing walking pump energy Boston Dynamics paper` | One secondary quote (about 15 kW for the hydraulic Atlas); no primary | thin (secondary only; not used as a bound) |
| 32 | `Robonaut 2 fact sheet weight 300 pounds power 120 VDC watts nasa.gov facts` | Mass and DOF only | thin |
| 33 | `Radford "Valkyrie: NASA's First Bipedal Humanoid Robot" Journal of Field Robotics 2015 battery thermal liquid cooling` | Paper itself not returned | dead (query or paywall) |
| 34 | `humanoid robot actuator torque density Nm/kg efficiency harmonic drive quasi-direct drive comparison review paper` | Vendor and blog numbers (25 to 39 Nm/kg harmonic, 7 to 28 Nm/kg QDD) | thin (secondary; not used) |
| 35 | Pages: NTRS 20100039862, 20110023122, 20100033240, 20110024047 (Robonaut 2 and Robonaut papers) | 20100033240 states arms use "thermal vacuum rated motors, harmonic drives"; no numeric thermal data in the others | thin |
| 36 | `Robonaut thermal vacuum chamber test arm joint actuator results cold hot temperatures EVA humanoid manipulator` (extended) | A summary claimed R2 arm actuators ran from -25 to 105 C in the JSC chamber; no primary page found | thin (unverified; not used) |
| 37 | `Robonaut 2 batpack EVA thermal design analysis battery torso heat sinking radiate NTRS` (extended) | Confirmed NTRS 20140000957 Batpack text | useful |
| 38 | `Robonaut arm joint actuators tested thermal vacuum chamber "-25" "105" harmonic drive lubricants Johnson Space Center` | No primary for the -25 to 105 C claim | dead (sources) |
| 39 | `harmonic drive gear vacuum lubricant lifetime cold temperature -40 C efficiency torque loss space mechanism study` | Led to ESMATS 2015 Roberts et al. | useful |
| 40 | Page: Roberts, Bridgeman, Jansson, Schulke and Tvaruzka, "The Performance and Life of Fluid-Lubricated Harmonic Drive Gears", ESMATS 2015 (ESTL, Harmonic Drive AG, ESA) | Vacuum life test at +90 C and cold-soak efficiency at -25 C | useful |
| 41 | Page: NASA MSC-TOPS-101 flyer (R2 arm technology) | Confirms brushless motors, harmonic drives, series elastic actuators; no numbers | thin |
| 42 | `NASA outgassing database ASTM E595 TML 1.0 percent CVCM 0.10 percent criteria silicone elastomer values` | Led to GSFC outgassing user guide and a NuSil/Avantor white paper | useful |
| 43 | `NASA RP-1124 Outgassing Data for Selecting Spacecraft Materials TML CVCM WVR table elastomers` | Led to NTRS 19970027853 | useful (leads) |
| 44 | Page: GSFC outgassing database user guide (etd.gsfc.nasa.gov, page carries a funding-lapse notice, content intact) | Test conditions and acceptance limits | useful |
| 45 | Page: NASA RP-1124 Rev 4 (NTRS 19970027853) | Scanned OCR is unreadable garbage | dead (source) |
| 46 | Pages: DTIC ADA303760; JAXA matdb Outgasdoc1 and Outgasdoc2; Wolfram data repository | DTIC returned a maintenance page; JAXA pages describe the method only; Wolfram lists 12859 rows but no per-material values opened | thin / dead (sources) |
| 47 | `Sylgard 184 outgassing NASA TML CVCM WVR values ASTM E595 cured 0.4` and `NASA outgassing data PVC polyurethane foam neoprene TML CVCM fails ASTM E595 materials not recommended for spacecraft use` | No per-material NASA values returned | dead (query; the NASA per-material database is a dynamic site I could not query) |
| 48 | Page: Avantor/NuSil white paper, "Evaluating low and ultra-low outgassing silicones for space applications" | 13 silicones with measured ASTM E595 TML/CVCM | useful (vendor, secondary) |
| 49 | `lunar dust abrasion seals joints Apollo lessons learned Gaier NASA TM-2005-213610 electrostatic adhesion` | Led to Gaier 2005 and Proctor and Dempsey | useful |
| 50 | Page: Gaier, NASA/TM-2005-213610 "The Effects of Lunar Dust on EVA Systems During the Apollo Missions" | Apollo abrasion, seal and radiator dust effects | useful |
| 51 | Page: Proctor and Dempsey, "Survey of Dust Issues for Lunar Seals and the RESOLVE Project" (NTRS 20080003835) | Downloaded; read below only if cited | see rows later |
| 52 | `lunar night survival temperature -170 C radioisotope heater unit Chang'e Yutu rover thermal design survive lunar night paper`; page ESA, "Surviving the long dark night of the Moon" (23 Mar 2017) | News pages and no engineering paper; the ESA page states lunar night temperatures "dip below -170 C" | thin (search) / useful (ESA page) |
| 53 | `Mars Exploration Rover thermal design warm electronics box RHU heaters operating temperature -40 C Spirit Opportunity winter survival` | Led to SAE papers (paywalled) and TFAWS05 Tsuyuki (EDL only) | thin |
| 54 | `lithium-ion battery low temperature performance NASA capacity at -20 C -40 C percent of room temperature discharge study` | Led to JPL poster R20129p and NTRS 20000056605 | useful |
| 55 | Pages: JPL R&TD poster R20129p (Smart et al., FY21); NTRS 20000056605 (Huang et al., JPL, Li-ion low-temperature cells) | Cell specific energy at -40 C; cathode capacity vs temperature | useful |
| 56 | `lithium plating charging lithium-ion below 0 C risk NASA Aerospace Battery Workshop charge temperature limit` | Led to NTRS 20100009705 (abstract page only; PDF not downloadable) | thin (abstract only) |
| 57 | `solid-state battery low temperature performance -40 C sulfide oxide polymer electrolyte ionic conductivity review capacity retention` (extended) | Review summaries: polymer cells need 60 to 80 C; no cold-temperature cell data from a primary | thin (not used) |
| 58 | `lithium-ion cell operation in vacuum pouch cylindrical electrolyte evaporation vent thermal runaway heat dissipation vacuum NASA test` | Thermal-runaway and venting summaries; no direct data on cell operation in vacuum | thin |
| 59 | `NASA State-of-the-Art of Small Spacecraft Technology Power chapter lithium-ion specific energy Wh/kg battery table solid-state`; page nasa.gov/wp-content/uploads/2023/05/3.-soa-power-2022.pdf | Cell specific energies, solid-state claims, low-temperature cells | useful |
| 60 | `NASA Mars fact sheet solar irradiance 590 W/m2 ...`; pages nssdc.gsfc.nasa.gov marsfact.html and moonfact.html | Mars 586.2 W/m2, gravity, temperatures; Moon equatorial 95 to 390 K | useful |
| 61 | `Mars surface solar panel power dust storm optical depth Opportunity ...` | News figures (700 to 22 Wh/sol, tau 10.8); NTRS 20190028687 not opened | thin (secondary) |
| 62 | `NASA Human Integration Design Handbook ... glove strength reduction` and `Extravehicular Mobility Unit EMU mass ... glove grip strength loss` | Led to Mesloh et al. NTRS 20100008464 and the EMU data book | useful |
| 63 | Page: Mesloh, England, Benson, Thompson and Rajulu, "The Effects of Extravehicular Activity (EVA) Glove Pressure on Hand Strength" (NTRS 20100008464) | Grip and pinch strength with Phase VI glove at 4.3 psi | useful |
| 64 | Page: NASA HIDH (NASA/SP-2010-3407 Rev 1), grep for EMU mass and glove numbers | 52908 lines of text; only qualitative glove statements found | thin |
| 65 | `Kram Domingo Ferris 1997 ... Froude number lunar Mars gravity` and `Carr Newman "The Apollo Number" ...` | Led to Carr and McGee 2009 PLoS ONE; Kram paper PDF not opened (Neptune 2005 paper opened instead, wrong paper) | useful / thin |
| 66 | Page: Carr and McGee, "The Apollo Number", PLoS ONE 4(8):e6614 (via Europe PMC XML; the PMC page is behind a reCAPTCHA) | Suited lunar walk-run Froude values | useful |
| 67 | Page: NASA EMU LSS/SSA Data Book Rev V (JSC-E-DAA-TN55224, Sept 2017) | Suit component masses, design metabolic loads, water sublimator | useful |
| 68 | `Canadarm2 Dextre lifetime anomalies replaced joint failure ...` and `NASA spacewalk Canadarm2 wrist roll joint replacement June 30 2026 ...` | News coverage (space.com, local TV) of the 2026 wrist-roll replacement and the 2002 one; no CSA/MDA statistics | thin (secondary) |
| 69 | `Curiosity wheel damage aluminum skin holes distance driven design life ...` | Summary quotes (0.75 mm skin; 3 broken grousers = 60% of life); JPL PDF not opened | thin |
| 70 | `NASA Opportunity rover mission complete 2019 ...`; pages science.nasa.gov MER mission, JPL "Six Things to Know About Opportunity", NTRS 20200000214 (abstract only; PDF has no download link) | 90 sols design, sol 5111 last contact, 45.16 km | useful (JPL page) |
| 71 | `Spirit rover wheel stuck ...`; pages JPL "NASA Concludes Attempts to Contact Mars Rover Spirit" (24 May 2011) and Spaceflight Now (24 May 2011) | Spirit's cold-survival failure and wheel failures | useful (JPL) / secondary (Spaceflight Now) |
| 72 | `multilayer insulation effective emittance 0.01 to 0.03 ...` and `Gilmore Spacecraft Thermal Control Handbook ...` | Vendor and student pages; NTRS downloads 404 for 20190025589, 20210008442, 20210004177 | dead (sources for those three) |
| 73 | `TFAWS multilayer insulation short course effective emittance ...` (extended); pages Johnson (NASA GRC) TFAWS "Multilayer Insulation for In-Space Cryogenic Applications" (NTRS 20240010471), TFAWS 2017 PT-07 | MLI heat flux 0.2 to 0.4 W/m2 at 293 K to 78 K, 30 layers, 2e-6 Torr; MLI equations valid only below 1e-4 Torr | useful |
| 74 | `radiation damage threshold polymers Gy dose Kapton PTFE silicone elastomer polyurethane mechanical properties degrade Mrad NASA materials radiation handbook` | Led to NASA CR-1787 (1971) and DTIC handbooks (DTIC returned maintenance pages) | useful (NASA CR-1787) / dead (DTIC, sources) |
| 75 | Page: Hunks and Hunzmun, NASA CR-1787, "Radiation Effects Design Handbook, Section 3: Electrical Insulating Materials and Capacitors", July 1971 (NTRS 19710020300). Scan OCR with spaced letters; numbers read by eye | Damage thresholds of PTFE, silicone rubber, polyurethane | useful (old; units "rads(C)" = carbon-equivalent absorbed dose) |
| 76 | `Juno radiation vault titanium 1 cm thickness dose reduction ...` | News and Scientific American blog only (1 cm Ti vault, factor of 800, 200 kg) | thin (secondary; kept as a lead, not tabled) |
| 77 | `Van Allen belts crossing dose per pass electronics shielding MEO orbit dose rate krad per year aluminum shielding thickness 100 mil` | Led to Carstens and Campola, NASA GSFC, 2022 | useful |
| 78 | Page: Carstens and Campola, "Total Dose Modeling of the Transit Through the Van Allen Belts", NASA GSFC Code 561, LSIC presentation 25 May 2022 (NTRS 20220007131) | TID vs aluminum shield thickness: direct Moon transfer, GTO per revolution, 2 to 10 month spiral | useful (AP-9/AE-9, solid aluminum sphere, silicon target; solar protons not included) |
| 79 | `Jones Jansen "Space Tribology" NASA/TM-2000-209924 ...` and page NTRS 20000057374 | PFPE failure mechanism, MoS2 in humid air, lubricant test results | useful |
| 80 | `cold welding vacuum clean metal surfaces ESA tribology handbook adhesion ...` and page NASA patent US 4,245,768 (NTRS 19810010928) | NASA statement on oxide monolayers, recontamination time vs pressure | useful (patent text; background section) / thin (no ESA handbook opened) |
| 81 | `Kurs Science 2007 Wireless power transfer via strongly coupled magnetic resonances ...`; abstract read through the Europe PMC API (the Science and PubMed pages are behind a CAPTCHA) | 60 W at about 40% over more than 2 m, up to 8 coil radii | useful |
| 82 | `microwave power beaming demonstration distance received power efficiency JAXA 1.8 kW 55 m Caltech MAPLE orbit results` and `Caltech MAPLE in-orbit ...`; page ard.jaxa.jp SSPS ground demonstration | JAXA page has no numbers; Caltech coverage says only that the signal was detected; JAXA 1.8 kW at 55 m is from a news summary | thin (JAXA 1.8 kW/55 m kept as an unverified lead) |
| 83 | `microwave power transmission beam collection efficiency Goubau tau parameter ...` and page Dickinson, JPL, NASA CR-157843, "Microwave Power Transmitting Phased Array Antenna Research Project Summary Report", 1978 (NTRS 19790005092) | Beam efficiency is a function of tau; SPS design tau 1.734; the efficiency curve (Fig. A-5) is a graph, not text | useful (definition and design point); curve values not extractable |
| 84 | `electronics operating at cryogenic temperatures lunar night -180 C extreme environment electronics NASA Glenn ...` and page Patterson, Hammoud and Elbuluk, "Assessment of electronics for cryogenic space exploration missions", Cryogenics 46 (2006) 231-236 | The PDF's minus signs are missing in the text layer, so temperatures cannot be read from it; only qualitative statements used | thin / useful (qualitative) |
| 85 | `legged robot cold weather test Spot Antarctica Arctic -30 C -40 C battery performance actuators problems field trial paper` | Press on Chinese hexapod at Zhongshan (-40 C, insulated battery two hours) and DEEP Robotics tests | thin (secondary; leads) |
| 86 | `Antarctic robot trials rover Cool Robot Nomad Zhongshan battery cold ...` and page Ray, Price, Streeter, Denton and Lever, "The Design of a Mobile Robot for Instrument Network Deployment in Antarctica", ICRA 2005 (Dartmouth Cool Robot) | Antarctic insolation, a 90 kg rover's design temperatures and motor power | useful |
| 87 | `Wensing Wang Seok Otten Lang Kim Proprioceptive Actuator Design in the MIT Cheetah ...` and page IEEE T-RO 33(3):509-522, 2017 (author's proof from MIT) | Motor torque density (27 vs 9 N m/kg) | useful |
| 88 | `Digit Cassie bipedal robot cost of transport measured ...` and page arXiv 2408.15632 (Wow Orin) | Simulated cost of transport for Cassie 0.762 and Unitree H1 0.718; preprint | thin (preprint; simulation) |
| 89 | Page: nasa.gov/technology/r5/ (NASA Valkyrie R5 page) | 300 lb, 6 ft 2 in, 1.8 kWh, about one hour, 44 DOF | useful |
| 90 | `clothing insulation clo definition 0.155 m2 K/W ISO 9920 ...` and page efunda.com clo | Summary only; no primary page opened | dead (sources; clo not used) |
| 91 | `silicone rubber thermal conductivity W/mK Sylgard 184 datasheet 0.27 ...` and page Dow Corning Sylgard 184 data sheet | Data sheet says 0.2 W/m K and a -45 to 200 C service range; the search summary said 0.27 | useful (data sheet) |
| 92 | `flexible thermal management method for high-power chips in humanoid robots` (ScienceDirect S2666998624004988) | WebFetch returned HTTP 403 | dead (sources) |
| 93 | `NASA High Performance Spaceflight Computing HPSC radiation tolerance ...` and page Powell, "High Performance Spaceflight Computing (HPSC) for Lunar and Planetary Missions", LPSC, 12 Mar 2025 (NTRS 20250002070) | 200 kRad TID requirement, RHBD for single events | useful |
| 94 | `Ingenuity helicopter Snapdragon 801 commercial processor radiation ...` | Vendor and press stories; no JPL paper found | dead (query; no primary reached) |
| 95 | Page: Ginosar, "Survey of Processors for Space", DASIA 2012 | RAD750: 250 nm, 133 to 166 MHz, about 300 MIPS, unit price above US$200,000 | useful (secondary survey by a space-processor vendor) |
| 96 | `all-solid-state lithium batteries low-temperature operation review ...` (extended); page Hong et al., Nature Communications 2025, "All-solid-state batteries designed for operation under extreme cold conditions" (open access, via Europe PMC API) | Panasonic 18650 retention at -20 and -40 C; solid-state coin cell at -60 C | useful |
| 97 | `lithium-ion battery cells vacuum environment testing thermal vacuum pouch cell ...` (extended); pages NASA/TM-2009-215751 (NESC Li-ion guidelines), JSC 20793 Rev C (Jan 2014), NTRS 20060020764 (a 3-line stub) | Vacuum and thermal-vacuum qualification requirements; charge and discharge limits for Mars; no data on cell physics in vacuum | useful (requirements) / thin (no cell-in-vacuum data) |
| 98 | Page: Kirchner-Burles et al., "Safety and performance implications of lithium plating induced by sub-zero temperature cycling of lithium-ion batteries", J. Power Sources 660 (2025) 238565 | Reversible plating at -10 C, irreversible at -20 C | useful |
| 99 | `NASA spacewalk Canadarm2 wrist roll joint ...` (extended); pages nasa.gov/blogs/spacestation 29 and 30 June 2026 | Canadarm2 installed 26 Apr 2001, wrist joint replaced 30 Jun 2026 | useful |
| 100 | `Dextre Special Purpose Dexterous Manipulator CSA facts ...` | Wikipedia and news only (15-year design life); NTRS 20100036524 not opened | thin (secondary; lead) |
| 101 | `Robonaut 2 returned to Earth 2018 ...` and page Rogers (NASA JSC), "Robonaut's Return to ISS", POIWG, 24 Apr 2019 (NTRS 20190025367) | Cause of the R2 anomaly | useful |
| 102 | `Curiosity wheel damage ...` page: Graser et al., "Rimmed Wheel Performance on the Mars Science Laboratory Scarecrow Rover" (JPL) | 0.75 mm skin; damage rate; 21.875 km at sol 2633 | useful |
| 103 | `water triple point 273.16 K 611.657 Pa IAPWS NIST value` and page Guildner, Johnson and Jones, J. Res. NBS 80A (1976) via Europe PMC | Vapor pressure of water at the triple point 611.657 Pa | useful |
| 104 | `polydimethylsiloxane PDMS gas permeability ... Merkel 2000` and page PMC3945670 | Europe PMC returned HTTP 500; the 800 Barrer O2 figure exists only in a search summary | dead (sources; not used) |
| 105 | `perfluoropolyether PFPE Krytox grease radiation gamma dose degradation ...` and page S. Mori et al., NASA Technical Paper 2910 (1989), "Degradation and Crosslinking of Perfluoroalkyl Polyethers Under X-Ray Irradiation in Ultrahigh Vacuum" (NTRS 19890011732) | Mechanism only; no dose threshold | thin |
| 106 | `JPL "NASA's COLDArm in Thermal Vacuum Testing"` page (jpl.nasa.gov/images/pia26162) and JPL R&TD poster R21008p (Kennett et al., FY21) | COLDArm tested at -180 C; state-of-the-art mobility actuators need heating to at least -55 C | useful |
| 107 | Page: NASA/JPL "NASA Concludes Attempts to Contact Mars Rover Spirit", 24 May 2011; Spaceflight Now same date | Cold survival failure; -67 F is from the AP/Spaceflight Now report of a NASA statement | useful |
| 108 | `Agility Robotics Digit V4 specifications sheet ...` | Secondary only (automate.org: Digit 5 90 min, 9 min recharge) | thin (secondary; lead) |
| 109 | `NASA Mars fact sheet ...`, Mars TSI search, and Opportunity dust-storm NTRS 20190028687 | The NTRS paper is about dust abrasion on solar cells, not the storm; storm power figures remain press-only | thin / dead (sources) |

Count at the time of writing: 109 numbered log rows (searches and page openings, some rows combine a search with the page it led to). Dead or partly dead rows (17): 1, 3, 14, 28, 30, 33, 38, 45, 46, 47, 72, 74, 90, 92, 94, 104, 109. Thin rows (found
something weak or secondary only) are marked in the log and are not counted as dead.

## 3. Findings

**How to read the tables.** Full citations (publisher, title, URL, date, type) are in the Source register below; each table
cell cites a key such as S3. "Primary" = space agency, peer-reviewed paper, handbook or dataset, or a manufacturer's own
spec for its own product. Units are as printed in the source; a conversion I made is marked "(conv.)" and uses only an exact
definition (1 Btu/h = 0.29307107 W; 1 lb = 0.45359237 kg). Dose units: 1 Gy = 100 rad; "krad(Si)" is dose to silicon and
"rads(C)" in the 1971 handbook is dose to carbon; they differ by a few percent for the photon spectra involved and I do not
convert between them.

### Source register

| Key | Publisher, title, URL, date | Type |
|---|---|---|
| S1 | NASA JSC (N. Radford), "Valkyrie, NASA's New Humanoid", slides, 25 Feb 2014. https://ntrs.nasa.gov/citations/20140011889 | Primary (agency slides) |
| S2 | NASA, "Valkyrie (R5)" technology page. https://www.nasa.gov/technology/r5/ (read 2026-10-10) | Primary |
| S3 | S. J. Jorgensen, J. Holley, F. Mathis, J. S. Mehling, L. Sentis, "Thermal Recovery of Multi-Limbed Robots with Electric Actuators", IEEE Robotics and Automation Letters, accepted Dec 2018 (arXiv:1902.00187v4, 21 May 2019). https://arxiv.org/abs/1902.00187 | Primary (peer-reviewed; NASA JSC authors) |
| S4 | Boston Dynamics, Atlas product page and spec sheet. https://bostondynamics.com/products/atlas/ and https://bostondynamics.com/wp-content/uploads/2026/01/atlas-spec-sheet.pdf (Jan 2026) | Primary (manufacturer, own product) |
| S5 | T. D. Ahlstrom, M. A. Diftler, R. B. Berka, J. M. Badger, S. Yayathi, A. W. Curtis, C. A. Joyce, "Robonaut 2 on the International Space Station: Status Update and Preparations for IVA Mobility", AIAA, 2013. https://ntrs.nasa.gov/citations/20140000957 | Primary |
| S6 | M. A. Diftler and R. O. Ambrose, "Robonaut: A Robotic Astronaut Assistant", NASA JSC (PDF undated; cites work to 1999, so about 2000). https://ntrs.nasa.gov/citations/20100033240 | Primary |
| S7 | D. Sinclair and J. Dyer, "Radiation Effects and COTS Parts in SmallSats", SSC13-IV-3, 27th AIAA/USU Conference on Small Satellites, 2013. https://s3vi.ndc.nasa.gov/ssri-kb/static/resources/Radiation%20Effects%20and%20COTS%20Parts%20in%20SmallSats.pdf | Primary (peer-reviewed conference) |
| S8 | T. A. Carstens and M. J. Campola, NASA GSFC Code 561, "Total Dose Modeling of the Transit Through the Van Allen Belts", LSIC presentation, 25 May 2022. https://ntrs.nasa.gov/citations/20220007131 | Primary (agency presentation) |
| S9 | Y. Gao et al., "Radiation effects on lithium metal batteries", The Innovation, 24 Jun 2023, doi:10.1016/j.xinn.2023.100468. https://ira.lib.polyu.edu.hk/handle/10397/108456 | Primary (peer-reviewed) |
| S10 | C. L. Hunks and D. J. Hunzmun (Battelle) for NASA, "Radiation Effects Design Handbook, Section 3. Electrical Insulating Materials and Capacitors", NASA CR-1787, Jul 1971. https://ntrs.nasa.gov/citations/19710020300 | Primary (agency handbook; old) |
| S11 | W. Powell (NASA STMD), "High Performance Spaceflight Computing (HPSC) for Lunar and Planetary Missions", LPSC, 12 Mar 2025. https://ntrs.nasa.gov/citations/20250002070 | Primary |
| S12 | R. Ginosar (Ramon Chips), "Survey of Processors for Space", DASIA 2012. https://www.ee.technion.ac.il/~ran/papers/SurveySpaceProcessors.DASIA2012.pdf | Secondary (conference survey by a vendor) |
| S13 | S. Mori et al., "Degradation and Crosslinking of Perfluoroalkyl Polyethers Under X-Ray Irradiation in Ultrahigh Vacuum", NASA TP-2910, 1989. https://ntrs.nasa.gov/citations/19890011732 | Primary |
| S14 | L. Kauder, "Spacecraft Thermal Control Coatings References", NASA/TP-2005-212792, Dec 2005. https://ntrs.nasa.gov/citations/20070014757 | Primary (handbook) |
| S15 | L. Carrillo, D. Farner, C. Preston, "ISS Payload Thermal Environments", NASA TFAWS 2015 short course. https://tfaws.nasa.gov/wp-content/uploads/TFAWS2015-SC-ISS-Payload-Thermal-Design.pdf | Primary |
| S16 | NASA, "Active Thermal Control System (ATCS) Overview" (ISS fact sheet, undated). https://www.nasa.gov/wp-content/uploads/2021/02/473486main_iss_atcs_overview.pdf | Primary |
| S17 | NIST, CODATA value: Stefan-Boltzmann constant. https://physics.nist.gov/cgi-bin/cuu/Value?sigma (read 2026-10-10) | Primary (dataset) |
| S18 | IAU 2015 Resolution B3, "Nominal values for selected solar and planetary quantities", arXiv:1605.09788 | Primary (peer-reviewed) |
| S19 | NASA GSFC NSSDC, "Mars Fact Sheet". https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html | Primary (dataset) |
| S20 | NASA GSFC NSSDC, "Moon Fact Sheet". https://nssdc.gsfc.nasa.gov/planetary/factsheet/moonfact.html | Primary (dataset) |
| S21 | E. W. Roberts, P. Bridgeman, M. Jansson, M. Schulke, A. Tvaruzka, "The Performance and Life of Fluid-Lubricated Harmonic Drive Gears", ESMATS 2015 (ESTL, Harmonic Drive AG, ESA). https://esrtechnology.com/wp-content/uploads/2026/06/ESMATS-16-2015-Roberts-The-Performance-and-Life-of-Fluid-Lubricated-Harmonic-Drive-Gears.pdf | Primary (peer-reviewed symposium) |
| S22 | W. R. Jones Jr. and M. J. Jansen, "Space Tribology", NASA/TM-2000-209924, Mar 2000. https://ntrs.nasa.gov/citations/20000057374 | Primary |
| S23 | B. L. Sater (NASA), "Method of Cold Welding Using Ion Beam Technology", US Patent 4,245,768, 20 Jan 1981. https://ntrs.nasa.gov/citations/19810010928 | Primary (patent background section) |
| S24 | NASA GSFC, "Outgassing Database User Guide". https://etd.gsfc.nasa.gov/capabilities/outgassing-database/user-guide/ | Primary |
| S25 | NuSil/Avantor white paper, "Evaluating low and ultra-low outgassing silicones for space applications" (undated). https://av.cmd.avantorsciences.com/rq/iddl/evaluating_low_ultra_low_outgassing_silicones_for_space_applications | Secondary (vendor) |
| S26 | J. R. Gaier, "The Effects of Lunar Dust on EVA Systems During the Apollo Missions", NASA/TM-2005-213610, Mar 2005. https://ntrs.nasa.gov/citations/20050160460 | Primary |
| S27 | M. P. Proctor and P. J. Dempsey, "Survey of Dust Issues for Lunar Seals and the RESOLVE Project", NASA GRC slides. https://ntrs.nasa.gov/citations/20080003835 | Primary |
| S28 | P. M. Wensing, A. Wang, S. Seok, D. Otten, J. Lang, S. Kim, "Proprioceptive Actuator Design in the MIT Cheetah", IEEE Transactions on Robotics 33(3):509-522, 2017. https://dspace.mit.edu/handle/1721.1/119863 | Primary (peer-reviewed) |
| S29 | L. Ray, A. Price, A. Streeter, D. Denton, J. Lever, "The Design of a Mobile Robot for Instrument Network Deployment in Antarctica", IEEE ICRA 2005. https://crobots.engineering.dartmouth.edu/papers/Crobots_ICRA2005_A4.pdf | Primary (peer-reviewed) |
| S30 | JPL, R&TD poster R20129p, M. Smart et al., "The Development of Advanced High Voltage, High Specific Energy and High Power Li-ion Cells with Improved Low Temperature Performance", FY21. https://www.jpl.nasa.gov/site/research/media/posters/2021/R20129p.pdf | Primary |
| S31 | JPL, R&TD poster R21008p, A. Kennett et al., "Long Life, High Speed, Heaterless Mobility Actuators", FY21. https://www.jpl.nasa.gov/site/research/media/posters/2021/R21008p.pdf | Primary |
| S32 | NASA JPL, "NASA's COLDArm in Thermal Vacuum Testing", 20 Dec 2023. https://www.jpl.nasa.gov/images/pia26162-nasas-coldarm-in-thermal-vacuum-testing/ | Primary |
| S33 | NASA, "State-of-the-Art of Small Spacecraft Technology", Chapter 3 Power, 2022 edition. https://www.nasa.gov/wp-content/uploads/2023/05/3.-soa-power-2022.pdf | Primary (agency report; compiles manufacturer data) |
| S34 | B. Hong et al., "All-solid-state batteries designed for operation under extreme cold conditions", Nature Communications, 2025, doi:10.1038/s41467-024-55154-5 (PMC11696891) | Primary (peer-reviewed) |
| S35 | C. Kirchner-Burles et al., "Safety and performance implications of lithium plating induced by sub-zero temperature cycling of lithium-ion batteries", Journal of Power Sources 660 (2025) 238565. https://discovery.ucl.ac.uk/id/eprint/10215263/ | Primary (peer-reviewed) |
| S36 | B. McKissock, P. Loyselle, E. Vogel, "Guidelines on Lithium-ion Battery Use in Space Applications", NASA/TM-2009-215751 (NESC-RP-08-75), May 2009. https://ntrs.nasa.gov/citations/20090023862 | Primary |
| S37 | NASA JSC, "Crewed Space Vehicle Battery Safety Requirements", JSC 20793 Rev C, Jan 2014. https://ntrs.nasa.gov/citations/20160003504 | Primary |
| S38 | C.-K. Huang, J. S. Sakamoto, S. Surampudi, J. Wolfenstine, "Li-ion cell development for low temperature applications", JPL (undated, about 2000). https://ntrs.nasa.gov/citations/20000056605 | Primary |
| S39 | A. Kurs et al., "Wireless power transfer via strongly coupled magnetic resonances", Science, 2007 (abstract read via Europe PMC, PMID 17556549) | Primary (peer-reviewed) |
| S40 | R. M. Dickinson (JPL), "Microwave Power Transmitting Phased Array Antenna Research Project Summary Report", NASA CR-157843, 1978. https://ntrs.nasa.gov/citations/19790005092 | Primary |
| S41 | M. Mesloh, S. England, E. Benson, S. Thompson, S. Rajulu (NASA JSC), "The Effects of Extravehicular Activity (EVA) Glove Pressure on Hand Strength", NTRS record 2010. https://ntrs.nasa.gov/citations/20100008464 | Primary |
| S42 | NASA JSC, "EMU LSS/SSA Data Book", Rev V, JSC-E-DAA-TN55224, Sep 2017. https://www.nasa.gov/wp-content/uploads/2017/02/esoc-13_rev._v_emu_hardware_data_book_jsc-e-daa-tn55224.pdf | Primary |
| S43 | C. E. Carr and J. McGee, "The Apollo Number: Space Suits, Self-Support, and the Walk-Run Transition", PLoS ONE 4(8):e6614, 2009 (read via Europe PMC XML) | Primary (peer-reviewed) |
| S44 | R. R. Neptune et al., "Ankle plantar flexor force production is an important determinant of the preferred walk-to-run transition speed", J. Exp. Biol. 208:799-808, 2005 | Primary (peer-reviewed; states the Froude-number fact in its introduction) |
| S45 | NASA, "Human Integration Design Handbook", NASA/SP-2010-3407 Rev 1, 5 Jun 2014. https://www.nasa.gov/sites/default/files/atoms/files/human_integration_design_handbook_revision_1.pdf | Primary (handbook) |
| S46 | NASA JPL, "Six Things to Know About NASA's Opportunity Mars Rover", 13 Feb 2019; "NASA Concludes Attempts to Contact Mars Rover Spirit", 24 May 2011. https://www.jpl.nasa.gov/news/six-things-to-know-about-nasas-opportunity-mars-rover/ ; https://www.jpl.nasa.gov/news/nasa-concludes-attempts-to-contact-mars-rover-spirit/ | Primary |
| S47 | S. Clark, Spaceflight Now, "NASA closes book on Spirit rover's historic mission", 24 May 2011. https://www.spaceflightnow.com/news/n1105/24spirit/index.html | Secondary (quotes a NASA statement) |
| S48 | E. Graser et al. (JPL), "Rimmed Wheel Performance on the Mars Science Laboratory Scarecrow Rover" (about 2020). https://robotics.jpl.nasa.gov/media/documents/Rimmed_Wheel_Performance_on_the_Mars_Science_Laboratory_Scarecrow_Rover.pdf | Primary |
| S49 | NASA, ISS blog posts, 29 and 30 Jun 2026. https://www.nasa.gov/blogs/spacestation/2026/06/30/astronauts-repair-canadarm2-robotic-arm-and-complete-spacewalk/ | Primary |
| S50 | J. Rogers (NASA JSC), "Robonaut's Return to ISS", POIWG, 24 Apr 2019. https://ntrs.nasa.gov/citations/20190025367 | Primary |
| S51 | Dow Corning, "Sylgard 184 Silicone Elastomer" product information (undated). https://www.cnfusers.cornell.edu/sites/default/files/Equipment-Resources/Sylgard_184_data_sheet.pdf | Primary (manufacturer data sheet) |
| S52 | L. A. Guildner, D. P. Johnson, F. E. Jones, "Vapor Pressure of Water at Its Triple Point", J. Res. NBS 80A, 1976 (PMC5293355) | Primary (peer-reviewed) |
| S53 | R. L. Patterson, A. Hammoud, M. Elbuluk, "Assessment of electronics for cryogenic space exploration missions", Cryogenics 46 (2006) 231-236 (NASA Glenn). https://nepp.nasa.gov/files/15442/06_281_Patterson%205%20Elsevier%20Cryogenics%20Journal%20Paper.pdf | Primary (peer-reviewed); minus signs lost in the PDF text layer |
| S54 | W. Johnson (NASA GRC), "Multilayer Insulation for In-Space Cryogenic Applications", TFAWS (NTRS 20240010471), 2024. https://ntrs.nasa.gov/citations/20240010471 | Primary |
| S55 | Wow Orin authors, "Structural Optimization of Lightweight Bipedal Robot via SERL", arXiv:2408.15632 (preprint, Aug 2024) | Secondary (preprint; simulation) |
| S56 | ESA, "Surviving the long dark night of the Moon", 23 Mar 2017. https://www.esa.int/Our_Activities/Space_Engineering_Technology/Surviving_the_long_dark_night_of_the_Moon | Primary (agency feature page) |

### 3.A Thermal

**A1. Published humanoid figures (mass, energy, power, thermal limits).**

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Valkyrie (R5) mass, height, DOF, battery | 300 lb (136 kg, conv.); 6 ft 2 in; 44 DOF; battery energy 1.8 kWh, "about an hour" of running | S2 | Primary | S1 gives 125 kg, 44 DOF, 2 kWh (2014 slides, earlier build); see Conflicts | Medium: two NASA sources disagree on mass and energy |
| Valkyrie onboard electronics | 3 Core i7 computers, 1 GPU, 44 motor controllers, 3 IMUs; two Li-ion packs | S1 | Primary | none found | High for the count |
| Valkyrie actuator temperature limits | Actuators "can operate up to 90 C"; operator-set safe limit 70 C; warning zone 75 C; ambient during test 25 C | S3 (Sec. VI-VII, footnote 3) | Primary | none found | High |
| Valkyrie heating rate | Balancing on one leg "heats up the stance leg in less than two minutes" to the warning zone; recovery to below 70 C took about one minute; right-leg actuators cooled in 21 s with contact switching | S3 (Sec. VII) | Primary | none found | High (one robot, one test, ventilated lab air) |
| Valkyrie thermal concern | Torso and leg actuators (motor drivers and cores) "naturally heat up due to the high actuator efforts needed to balance"; operations are postponed until they cool | S3 (Sec. I, III) | Primary | none found | High |
| Valkyrie actuator type | 32 actuated DOF excluding fingers; harmonic-driven series-elastic electric actuators; 3 thermistors per actuator | S3 (Sec. III) | Primary | S1 (44 motor controllers incl. hands) | High |
| Atlas (production electric) | 90 kg; 1.9 m; 56 DOF; battery life 4 hr; IP67; operating temperature -20 to 40 C; battery self-swap; instant payload 50 kg, sustained 30 kg | S4 | Primary (manufacturer) | none found; battery Wh not published | High for what is stated |
| Robonaut 2 EVA thermal approach | Batpack and torso "use fans to help cool electronics"; "main challenge ... will be heat sinking all of the electronics to sufficiently radiate heat to avoid overheating"; heaters for cold; active cooling loops "add complexity and current design concepts do not require them" | S5 (Sec. "Future upgrades for EVA") | Primary | none found | High |
| Robonaut 2 climbing legs thermal test | "some thermal vacuum testing has been performed on the actuators and motors drivers"; legs not certified for EVA | S5 | Primary | S6 says Robonaut 1 arms used "thermal vacuum rated motors" and "other scales have been built for thermal vacuum testing" | Medium: no temperatures or results given |
| Digit, Optimus, Figure power figures | Not obtained from a primary source | none | n/a | n/a | n/a (see Open threads) |
| Human metabolic baseline | Nominal crewmember 474 Btu/h (139 W, conv.); sleeping 300 Btu/h (88 W, conv.) | S45 (Sec. 6.2.3, assumptions for an 82 kg crewmember in a 21 C cabin) | Primary | S42: EMU design loads below | High |
| EMU design heat loads | Average 1000 Btu/h (293 W, conv.) for 7 h; peak 2000 Btu/h (586 W, conv.) for 15 min; 1600 Btu/h for 1 h | S42 (Sec. 1.1) | Primary | S45 | High |
| Human body surface area | 15,300 cm2 (5th-percentile female) to 22,800 cm2 (95th-percentile male); DuBois: area (cm2) = 71.84 x W^0.423 x H^0.723 (W kg, H cm) | S45 (Table 4.6-1, Sec. 4.6.2.2) | Primary | none found | High |

**A2. Radiation physics, surface optical properties, and the environment.**

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Stefan-Boltzmann constant | 5.670 374 419 x 10^-8 W m^-2 K^-4 | S17 | Primary | search summaries of CODATA 2018/2022 agree | High |
| Solar irradiance at 1 AU | nominal TSI 1361 W m^-2 | S18; S19 and S20 list 1361.0 | Primary | S19, S20 | High |
| Mars solar irradiance | 586.2 W m^-2 (the fact sheet's "solar irradiance" entry, taken to be at the planet's mean orbital distance and above the atmosphere) | S19 | Primary | none found for surface irradiance | High for the entry as printed; surface value not found |
| Mars surface pressure; diurnal temperature | 6.36 mb at mean radius (varies 4.0 to 8.7 mb); Viking 1 site 184 K to 242 K (-89 to -31 C) | S19 | Primary | none found | High |
| Moon equatorial diurnal temperature; sidereal rotation; synodic period | 95 K to 390 K; 655.72 h; 29.53 d | S20 | Primary | S56 gives "below -170 C" for lunar night | High |
| Lunar surface pressure at night | 3 x 10^-15 bar | S20 | Primary | none found | High |
| White paint Z93 | solar absorptance 0.16, normal emittance 0.92 | S14 (Table 4.2) | Primary | derived use below | High |
| Black paint Z306 | 0.96 / 0.91 | S14 (Table 4.1) | Primary | none found | High |
| Black Kapton film | 0.93 / 0.85 | S14 (Table 4.9) | Primary | none found | High |
| Beta cloth (EMU outer-layer fabric class), two examples | Beta Cloth/VDA Sheldahl 0.38 / 0.85; Beta Cloth/VDA Chemfab 500 (no silicone) 0.45 / 0.90 | S14 (Table 4.2) | Primary | none found | Medium: I did not find textile data for ordinary clothing |
| Lunar dust on radiators | IR emittance of dust about 0.88 vs 0.83 for the surface; "only 11 percent dust coverage" doubled solar absorptance; 10 psi nitrogen jet for 15 s lowered absorptance only from 0.245 to 0.239 | S26 | Primary | none found | High (ground tests on simulated dust; Apollo flight evidence agrees qualitatively) |
| ISS flux used for payload environments | 216 nmi altitude; mean solar 434.6 Btu/hr-ft2 (1371 W/m2, conv.), albedo 0.27, outgoing longwave 76.4 Btu/hr-ft2 (241 W/m2, conv.) | S15 | Primary | solar value agrees with S18 | High |
| Passive 1 ft cube on ISS ELC-1, no internal power, surface a/e = 0.18/0.84 | Night pass -46 to -51 C; orbit-average -31 to +7 C depending on location | S15 (ELC-1 table) | Primary | none found | Medium: S15 says "for trending purposes only" |
| Same cube, a/e = 0.66/0.74 | Night -46 to -51 C; day pass up to +56 C; orbit average -21 to +39 C | S15 | Primary | | Medium |
| Same cube, a/e = 0.45/0.12 | Day pass up to +155 C; orbit average +9 to +119 C; exceeds the +112.8 C EVA touch limit | S15 | Primary | | Medium |
| ISS orbit timing in S15 | night pass 30 min, day pass 60 min, orbit 90 min | S15 (Sec. 5) | Primary | | High |
| Typical ISS hardware lower limit | -40 C | S15 | Primary | S31 | High |

**A3. Heat rejection hardware and insulation (real figures).**

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| ISS Photovoltaic Radiator (PVR) | rejects up to 14 kW; 7 panels; 10.24 ft x 44.62 ft (3.12 m x 13.6 m); mass 1,633 lb (740.7 kg) | S16 | Primary | EEATCS radiator ORU has the same stated dimensions | High |
| ISS External Active Thermal Control System | 35 kW per loop, 70 kW total; ammonia freezing point -107 F (-77 C) | S16 | Primary | none found | High |
| EMU cooling method | Water sublimator: feedwater freezes and sublimates to space; liquid cooling and ventilation garment on the wearer | S42 (Sec. 1.2.1) | Primary | | High |
| MLI heat flux, vacuum | 0.2 to 0.4 W/m2 for the NASA-funded 1970s blankets listed (30 layers, 14.1 layers/cm, 293 K to 78 K, 2e-6 Torr); the cited MLI equation is "only good less than 10^-4 Torr" | S54 | Primary | S54 also lists entries at 2.7 and 5.8 W/m2 for other blanket types | High for vacuum performance |
| MLI in air | "On the launch pad ... a MLI blanket can loosely be modeled as a stagnant gas pocket"; convection removed only in vacuum | S54 | Primary | | High |

**A4. Temperature ranges of materials and components.**

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Silicone elastomer (Sylgard 184, a representative skin-class material) | service range -45 to 200 C; thermal conductivity 0.2 W/m K; linear CTE 310 ppm/C; Shore A 50; low-temperature behavior "can become more complex" at -55 C | S51 | Primary (manufacturer) | search summaries quoted 0.27 W/m K; not opened | Medium: one product; the fiction's skin material is not specified |
| Li-ion operating range | "Typical Li-Ion batteries have an operating temperature range of -20 C to 60 C" | S33 (Sec. 3.5.3) | Primary | S36: optimum 20 to 40 C | High |
| Li-ion optimum | "between 20 and 40 C" for most Li-ion batteries | S36 | Primary | S33 | High |
| Mars-mission battery qualification | Charge on Mars -10 to 40 C; discharge on Mars -30 to 40 C; cruise -30 to 40 C | S36 (qualification table) | Primary | | High |
| State-of-practice flight cell | InSight-class large-format cells operate -30 C to +35 C; at -40 C deliver 105 Wh/kg at C/5 when charged at room temperature; commercial 18650 cells "negligible capacity at -40 C" | S30 | Primary | S34: Panasonic 18650 | High |
| Commercial 18650 retention in the cold | 66% at -20 C and 5% at -40 C of room-temperature energy at rates below 0.1 C | S34 (introduction, citing a manufacturer curve) | Primary (peer-reviewed paper quoting data) | S30 | Medium |
| Cathode half-cell capacity vs temperature | 100% at +20 C, 70% at -20 C, 60% at -30 C, 46% at -40 C (LiCo0.2Ni0.8O2 half cell) | S38 | Primary (about 2000; chemistry old) | S30 | Medium (old chemistry) |
| Lithium plating on cold cycling | Cells cycled at -10 C show reversible plating; at -20 C plate irreversibly; jelly-roll collapse observed | S35 | Primary | S36 (Mars charge floor -10 C) | High |
| Solid-state (lab) cold operation | All-solid-state coin cells with an amorphous Li3N-TaCl5 electrolyte delivered 143.78 mAh/g at -40 C (rate not stated in the passage I read) and 51.94 mAh/g at -60 C at 18 mA/g (a very slow rate); 83.5% capacity retention at -30 C after 100 cycles | S34 | Primary | no flight or pack-scale data found | Low for any humanoid use: lab coin cells at low rate |
| Solid-state at the high end | Manufacturer-claimed cell values 390 to 560 Wh/kg (Solid Power), 230 to 300 Wh/kg projected (QuantumScape) | S33 (Table 3-7) | Primary (agency compilation of manufacturer claims) | none independent | Low (claims, not flight data) |
| Mobility-actuator cold limit | "the current state of the art actuators require heating to at least -55 C, in flight"; goal of -230 to +125 C without preheating | S31 | Primary | S32 | High |
| Cold-capable arm demonstrated | COLDArm tested in a thermal vacuum chamber reduced to -180 C (-292 F), using bulk metallic glass gears (no wet lubrication or heating), cold motor controllers and a cryogenic six-axis force/torque sensor | S32 | Primary | S31 | High |
| Spacecraft electronics temperature | Spacecraft electronics are normally held near 20 C with radioisotope heaters; COTS bipolar transistors lose current gain and MOSFET gate thresholds rise when cooled; one DC/DC converter's regulation worsens with falling temperature (the minus signs are missing in the PDF text, so the temperatures cannot be quoted) | S53 | Primary | | Medium (qualitative only) |
| Harmonic drive in the cold | At -25 C, efficiency is "appreciably less" than at +90 C because of viscous losses; with MAC grease, cold-soak efficiency started near 20% and fell to about 10% | S21 | Primary | S22 notes liquid-lubricated space mechanisms normally see -10 to -20 C | High |
| Robonaut 2 encoder | Original Mylar optical code disk replaced by a metal disk "that is able to survive a much greater temperature range" | S5 | Primary | | Medium |

**A5. Clothing and skin on a machine (materials constraints).**

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Habitat acceptance of non-metals on a robot | "on-orbit off gassing and flammability testing are performed on most non-metallic materials"; R2's Lycra shoulder and elbow covers were replaced by a 100% Nomex stretch material for mobile use because Lycra has undesirable flammability | S5 (Sec. IVA mobility safety) | Primary | S24 (outgassing limits) | High |
| Apollo suit outer layers | Outer layer worn through into the Mylar MLI above the boot after 8 hr of surface activity; cover gloves discarded after two EVAs; zippers, helmet and glove-disconnect seals cleaned and re-lubricated between EVAs | S26; S27 | Primary | | High |

### 3.B Radiation

**B1. Electronics: dose, single events, hardening, shielding.**

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Commercial (COTS) parts, total ionizing dose | "Most commercial components are radiation tolerant to 5 krad. Many are radiation tolerant to 20 krad or more. Some will fail before 1 krad. Without testing, it is impossible to predict which category a part will fall into." "Provided the lifetime dose is under 30 krad, a solution can probably be realized with commercial parts." | S7 | Primary | none independent found; the figure is a rule of thumb from LEO small-satellite practice | Medium |
| Lot-to-lot variation | Parts made last year may tolerate a dose that this year's lot does not; flight lots must be identical to tested lots | S7 | Primary | | High |
| Radiation-hardened parts, rated dose | "Rated radiation dose of 100 krad to > 1 Mrad"; no single-event latchup | S7 | Primary | S11: NASA's next flight computer requires 200 kRad TID with hardening by design | Medium |
| NASA HPSC computer | 200 kRad total ionizing dose requirement; hardening by design for single-event effects | S11 | Primary | | High |
| Cost and speed penalty of hardened processor | RAD750: 250 nm process, 133 to 166 MHz, about 300 MIPS, unit price above US$200,000 (survey dated 2012) | S12 | Secondary (survey by a space-processor vendor) | | Medium |
| Single-event upset example | A small-satellite supervisor processor with 67,584 RAM bits: expected upset every 4.4 x 10^6 s (52 days) for a proton flux of about 100 /cm2/s behind 0.7 cm aluminum; handled with software error correction | S7 | Primary | | Medium (one device, one orbit) |
| Shielding limit | "shielding has very small marginal benefit beyond about 5 mm (200 mil)" of aluminum for LEO trapped particles; 1 mm tungsten has the mass of 7.1 mm aluminum and stops electrons like 6 mm and protons like 4 mm of aluminum; 5-year dose 10.37 krad with a 2.5 mm aluminum chassis side falls to 2.71 krad with a 1 mm tungsten shell | S7 | Primary | S8 trend (curves flatten beyond about 5 mm) | High |
| Humanoid electronics are distributed | Valkyrie has 44 motor controllers (one per actuator, in the limbs) plus 3 Core i7 computers | S1; S3 (three thermistors and a logic board in each actuator) | Primary | | High |

**B2. Dose behind aluminum shielding for trajectories through the Earth's trapped-radiation belts** (S8: AP-9/AE-9 models, solid aluminum sphere,
silicon target, solar protons not included; units krad(Si); 1 mil = 0.0254 mm). Primary; no independent cross-check found;
confidence high that the numbers are as printed, medium that they transfer to a body of different geometry.

| Shield (Al) | Direct Earth-to-Moon transfer (3 to 6 days typical) | GTO phase 1, per revolution (perigee 188 km, apogee 35,790 km, 10.51 h) | GTO phase 3, per revolution (perigee 33,194 km, 22.85 h) | Spiral, 2 months in belts | Spiral, 10 months in belts |
|---|---|---|---|---|---|
| 1 mil (0.03 mm) | 128 | 283 | 467 | 50,500 | 221,000 |
| 10 mil (0.25 mm) | 16.3 | 37.0 | 34.2 | 6,110 | 24,000 |
| 25 mil (0.63 mm) | 5.76 | 12.5 | 7.43 | 2,090 | 7,280 |
| 50 mil (1.27 mm) | 2.29 | 4.57 | 2.03 | 774 | 2,490 |
| 100 mil (2.54 mm) | 0.559 | 1.04 | 0.391 | 177 | 545 |
| 200 mil (5.08 mm) | 0.0437 | 0.0739 | 0.0254 | 12.5 | 36.1 |
| 300 mil (7.62 mm) | 0.0070 | 0.0126 | 0.0047 | 1.86 | 5.34 |
| 500 mil (12.7 mm) | 0.0013 | 0.0035 | 0.0014 | 0.410 | 1.29 |
| 900 mil (22.9 mm) | 0.0006 | 0.0019 | 0.0007 | 0.203 | 0.648 |

**B3. Batteries and soft materials.**

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Li-metal cells after 20 kGy of Co-60 gamma (20 kGy = 2 Mrad, conv.) | Capacity retention after 350 cycles at 1 C: NCM811 cell 57.7% (control 76.6%), LFP 69.6% (control 90.9%), LCO 70.3% (control 94.2%). The liquid electrolyte is the largest contributor to the loss, then the cathode material, then the binder | S9 | Primary | none found for Li-ion cells specifically | Medium: lithium-metal cells, gamma only |
| Silicone rubber (wire insulation) | no noticeable degradation of physical properties up to 8.8 x 10^5 rads(C); slight loss of resilience at 8.8 x 10^6; serious deterioration, cracking or crumbling when stressed, at 8.8 x 10^7 and above | S10 | Primary (1971 handbook) | none found | Medium: one product form, old data |
| PTFE (Teflon TFE) | approximate damage threshold 1.7 x 10^4 rads(C); 25 percent damage dose 3.4 x 10^4 rads(C); crumbles at about 10^7 rads. FEP in vacuum kept its elongation to a dose ten times higher than TFE-7 | S10 | Primary | none found | Medium |
| Polyurethane | limited data; two studies (a reactor exposure with gamma 1.4 x 10^6 rads(C), and an electron exposure) found insignificant changes in electrical properties; mechanical data are not given | S10 | Primary | none found | Low |
| Perfluoropolyether (PFPE) lubricants | X-ray irradiation in ultrahigh vacuum causes both degradation and crosslinking; the fluids become tacky; no dose threshold given | S13 | Primary | S22: PFPE contact failure is also driven by surface fluorides (tribochemistry) | Low for a dose number (none found) |

### 3.C Vacuum and materials

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Outgassing screening test | 398 K (125 C) for 24 h in vacuum; acceptance limits total mass loss (TML) at most 1.0 percent and collected volatile condensable material (CVCM) at most 0.10 percent; water vapor regained measured after 24 h at 25 C, 50 percent RH | S24 | Primary | S25 states the same limits | High |
| Silicones that pass | 13 NuSil silicones: TML 0.02 to 0.52 percent and CVCM 0.00 to 0.09 percent (e.g., one 2-part dimethyl: 0.02 / 0.00; a 1-part oxime coating: 0.52 / 0.09); an "ultra-low outgassing" tier demands TML at most 0.1 and CVCM at most 0.01 | S25 | Secondary (vendor) | S24 limits | Medium: selected space-grade grades; ordinary skin-grade silicone was not found in the database I could open |
| Habitat materials rule | Non-metallic materials on R2 undergo offgassing and flammability testing; new materials not in the JSC database must be tested | S5 | Primary | | High |
| Cold welding | "As little as one or two monolayers of metallic oxides effectively interrupt or prevent metallic bonding." A surface cleaned at one atmosphere is recontaminated by a monolayer in less than 10^-8 s; at 10^-6 torr the recontamination time is a few seconds and rises as pressure falls | S23 | Primary (NASA patent background) | none found; no ESA handbook opened | Medium |
| Harmonic drive life in high vacuum, fluid lubricated | 160:1 gear, rated 40 N m, tested at 4 N m output, 50 rpm input, +90 C: PFPE-lubricated efficiency 80 to 90 percent over the first 5 million input revolutions, 50 to 70 percent afterward, 40 percent at about 11 million, test stopped near 12 million input revolutions (about 75,000 output revolutions); post-test inspection found metal transfer at the flexspline/wave-generator interface ("lubrication having become ineffective"). MAC-grease unit: about 80 percent for about 12 million input revolutions, then low | S21 | Primary | S22: PFPE liquid lubricants in boundary contact fail by an autocatalytic fluoride reaction, abruptly | High for this test; medium for transfer to other gears |
| Other lubricants | In an ESTL linear ball-screw test the two PFPE lubricants "failed rapidly"; Braycote 601 grease with ion-plated lead and sputtered MoS2 reached the 2 million cycle requirement | S22 | Primary | | Medium |
| MoS2 dry lubricant and air | friction below 0.01 in ultrahigh vacuum, 0.01 to 0.04 in normal vacuum with long life; in humid air about 0.15 and "very limited life" | S22 | Primary | S31 (dry-lubricated gearing for -230 to +125 C is an open development goal) | High |
| Liquid-lubricated space mechanisms, temperature | "do not involve wide temperature ranges"; -10 to -20 C sometimes encountered | S22 | Primary | S21 (-25 C cold soaks) | High |
| Lunar dust, abrasion | Apollo 12: suits more worn after 8 hr of surface activity than training suits after 100 hr, worn through the outer layer into the Mylar insulation; Apollo 17 cover gloves discarded after two EVAs; surface times were 21 to 75 hr per mission | S26 | Primary | | High |
| Lunar dust, seals | Apollo 12 suit leak rate 0.15 psi/min after the first EVA and 0.25 psi/min after the second, against a 0.30 psi/min limit; all environmental and gas sample seals failed because of dust; 4 of 12 sample containers leaked because of dust or equipment on seals | S26; S27 | Primary | | High |
| Lunar dust, thermal | LRV batteries exceeded operating temperature limits on Apollo 16 and 17 because dust could not be brushed off; magnetometer temperatures about 68 F higher than expected on Apollo 12 | S26 | Primary | | High |
| Suit seal practice | Wrist bearings and rotational connectors had fabric covers against dust; glove-disconnect seals were cleaned and re-lubricated with Krytox between EVAs | S27 | Primary | | High |
| Triple point of water | vapor pressure 611.657 Pa +/- 0.010 Pa (99 percent limits) | S52 | Primary | S19: Mars mean surface pressure 6.36 mb (636 Pa) | High |
| Battery vacuum qualification | Batteries in pressurized volumes: vacuum exposure at about 0.1 psi for at least 6 h; batteries in unpressurized volumes: thermal-vacuum cycles at 1 x 10^-5 Torr; eight thermal cycles with first and last under vacuum | S37; S36 | Primary | | High |

### 3.D Power

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Li-ion cell specific energy, 18650 | 112 (Canon BP-930s), 182 (Molicel ICR18650H), 191 (LG ICR18650 B3), 243 (Panasonic NCR18650B), 260 (LG MJ1) Wh/kg; "latest cells have all exceeded 240 Wh/kg" | S33 (Table 3-4) | Primary (agency compilation of manufacturer data) | | High at cell level; pack level is lower and not found |
| Li-ion 21700 | 262 and 264 Wh/kg | S33 | Primary | | High |
| Solid-state cells | Manufacturer values 390 to 560 Wh/kg (Solid Power) and projected 230 to 300 Wh/kg (QuantumScape); not flight-proven | S33 (Table 3-7) | Primary compilation of claims | S34 (cold, lab only) | Low |
| Fuel cells | A hydrogen-peroxide fuel cell reached over 1000 Wh/kg but "cannot be recharged on orbit"; regenerative fuel cells "currently being researched"; fuel cells are "primarily being proposed for small spacecraft propulsion systems rather than for power sub-systems" | S33 (Sec. 3.3.4) | Primary | none found for a human-sized machine | Medium |
| Space solar cell efficiency | triple-junction cells over 32 percent; terrestrial silicon about 20 percent; 38 percent laboratory multi-junction | S33 | Primary | S29 used 20 percent cells | High |
| Humanoid battery energies | Valkyrie 1.8 kWh (S2) or 2 kWh (S1); Robonaut 2 Batpack about 5.79 kWh from 300 Boston Power Swing 5300 cells (24, 48, 96 V buses); Atlas 4 hr, Wh not published (S4) | S1; S2; S5; S4 | Primary | | Medium (Valkyrie sources disagree) |
| Efficiency of a wheeled 90 kg Antarctic robot | estimated 90 W average and 180 W at 0.8 m/s (resistance coefficient 0.25); target power budget about 250 W; gearboxes 90 percent efficient, 100:1, lubricated for -50 C | S29 | Primary | not a humanoid | Medium (estimate) |
| Simulated cost of transport | Cassie 0.762, Unitree H1 0.718, Wow Orin 0.407 (COT = P/(m g v), P = joint power; simulation with one training algorithm) | S55 | Secondary (preprint) | | Low |
| Antarctic solar flux | South Pole summer horizontal 200 to 500 W/m2; with elevation adjustment 800 to 1200 W/m2; November to February average about 1000 W/m2 at about 20 degrees sun elevation; diffuse 50 to 100 W/m2; efficiency rises as temperature falls | S29 | Primary | | Medium |
| Cold charging limit | Mars-mission charge range -10 to 40 C (S36); irreversible plating at -20 C (S35) | S36; S35 | Primary | | High |
| Magnetic-resonance wireless power | 60 W transferred at about 40 percent efficiency over more than 2 m, up to 8 times the coil radius | S39 | Primary | none found for a moving, human-sized receiver | High for the experiment |
| Microwave beaming, design parameter | Beam efficiency depends on tau = sqrt(A_t A_r)/(wavelength x distance); the SPS design point was tau = 1.734; the efficiency curve is a figure in the report (not extractable) | S40 | Primary | JAXA 1.8 kW at 55 m is in news summaries only | Medium |

### 3.E Mechanical

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Motor torque density (rotor-stator, no gearbox) | custom MIT Cheetah motor saturation torque density about 27 N m/kg versus 9 N m/kg for a catalog frameless motor (Emoteq HT-5001); catalog torque density scales roughly as gap radius^0.8 | S28 | Primary | | High |
| Gear efficiency, new | harmonic drive 80 to 90 percent in vacuum at +90 C; 100:1 planetary 90 percent | S21; S29 | Primary | | High |
| Walk-run transition | humans switch gait at a Froude number (v^2/(g L)) of about 0.5 (S44 says this holds in reduced gravity; S43 expects about 0.9 for unsuited walkers in lunar gravity, see Conflicts 9); suited Apollo lunar gait events gave Fr* = 0.358 +/- 0.057 (Apollo number Ap* = 0.684 +/- 0.102) | S44; S43 | Primary | | Medium (human data; a machine's gait is not bound by it, but dynamic similarity is) |
| Surface gravity | Moon 1.62 m/s2; Mars 3.73 m/s2 (mean) | S20; S19 | Primary | | High |
| Microgravity translation | R2 translates on IVA handrails and seat tracks, which "have load and moment limits that R2 must remain below"; the climbing legs have no electromagnetic brakes, so joint motors hold position | S5 | Primary | | High |
| EVA suit mass | Enhanced suit assembly with two arms and two gloves 143.73 lb (65.2 kg, conv.); life-support subsystem 196.7 lb (89.2 kg, conv.), of which the primary life-support pack (PLSS) is 101.4 lb; operating 4.3 psid | S42 (Sec. 1.5.3, Fig. 1.10) | Primary | | High |
| Pressurized glove strength | Phase VI glove at 4.3 psi, 8 subjects: grip 58 percent of bare-hand without the thermal micrometeoroid garment, 46 percent with it (66 and 55 percent unpressurized); lateral pinch 83 to 86 percent | S41 | Primary | S45 (gloves reduce tactility even unpressurized) | High (small sample) |

### 3.F Cold (additional rows; see also 3.A4)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Lunar night | temperatures "dip below -170 C"; the equatorial range is 95 K to 390 K | S56; S20 | Primary | each other | High |
| Mars rover thermal design | The rovers' Warm Electronics Box (batteries, computer) must stay within -40 to +40 C; gold-painted insulated walls, silica aerogel, thermostat and heaters, and a heat-rejection system protect it from a daily temperature swing of 113 C | S29 (description of the Mars rovers) | Primary (secondary description of MER) | S19 (diurnal range) | Medium |
| Spirit, loss of survival heat | "With inadequate energy to run its survival heaters, the rover likely experienced colder internal temperatures last year than in any of its prior six years on Mars. Many critical components and connections would have been susceptible to damage from the cold." Reported internal temperature likely about -67 F | S46 (quote); S47 (the -67 F figure) | Primary / secondary | | High for the loss mechanism; medium for the number |
| Antarctic design point | A 90 kg robot designed for -40 C ambient (South Pole summer average -20 to -40 C), with an insulated cold-room test of the drive train | S29 | Primary | S31 | Medium |
| Insulation in vacuum | MLI: 0.2 to 0.4 W/m2 at 293 K to 78 K (30 layers, 2e-6 Torr) | S54 | Primary | | High |

### 3.G Fatigue and lifetime

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Opportunity | Prime mission 90 days; worked more than 14 years; drove 28.06 mi (45.16 km); the right-front wheel drew more current than the others so engineers drove backward to extend its life; last contact sol 5111 (10 Jun 2018) in a dust storm | S46 (JPL 2019) | Primary | NTRS 20200000214 abstract (not downloadable) | High |
| Spirit | Landed Jan 2004 for a 3-month mission; last contact 22 Mar 2010; 4.8 mi driven; two of six wheels stopped rotating and the rover stalled in a sand pit in May 2009; NASA ended contact attempts 25 May 2011 | S46 (dates, mission); S47 (wheels, sand pit, distance) | Primary / secondary | | Medium |
| Curiosity wheels | Aluminum wheel skin 0.75 mm thick; on Sol 490, 4.6 km into the prime mission, "an unexpectedly high rate of damage" was seen; as of Sol 2555 (14 Oct 2019) two broken grousers on the left middle wheel and one on the right middle; 21.875 km by Sol 2633 (1 Jan 2020) | S48 | Primary | | High |
| Canadarm2 | installed 26 Apr 2001; on 27 May 2026 the arm "drew elevated motor current and did not move as expected"; a wrist joint was replaced on 30 Jun 2026 in a 7 h 20 min spacewalk; "designed with replaceable components" | S49 | Primary | an earlier wrist-roll replacement in 2002 is in news only | High |
| Robonaut 2 | On ISS from 2011; returned Feb 2018; cause of the failure was a missing return wire for the computer-chassis power, so current used an undersized path and a backpack connector overheated and opened; the fault was in the original design and only appeared when higher-power processors were added; six crew members, 10 sessions of troubleshooting; "very difficult to repair on-orbit" | S50 | Primary | | High |
| Dextre | design life and service history | not obtained from a primary source | n/a | | n/a (see Open threads) |
| Fluid-lubricated gear life | about 75,000 output revolutions in vacuum at 10 percent of rated torque before efficiency fell to 40 percent | S21 | Primary | | High for the test |

## 4. Conflicts

1. **Valkyrie mass and battery energy.** S1 (NASA JSC slides, Feb 2014): 125 kg and "2 KWhr" battery. S2 (NASA R5 page, 2023
   fact sheet era): 300 lb (136 kg) and 1.8 kWh. Likely cause: S1 describes the first-generation robot built for the 2013
   robotics challenge; S2 describes the later R5 configuration. I use S2 for derived figures and show S1 in the tables.
2. **Silicone thermal conductivity.** S51 (data sheet I opened) prints 0.2 W/m K for Sylgard 184. Search summaries quoted 0.27
   W/m K from other documents I did not open. Likely cause: different data-sheet revisions or measurement methods. I use 0.2
   (opened). The skin-resistance result below changes by less than 2 percentage points between the two.
3. **How much capacity a Li-ion cell keeps in the cold.** S38 (cathode half cell, about 2000): 70 percent at -20 C, 46 percent
   at -40 C. S34 (commercial 18650 full cell, below 0.1 C): 66 percent at -20 C, 5 percent at -40 C. S30 (flight large-format
   cell at C/5): 105 Wh/kg at -40 C, against 180 to 230 Wh/kg ambient for small-format cells. These do not contradict: they
   measure a half cell vs a full cell, different electrolytes, and different rates. For a humanoid pack, the full-cell,
   commercial-cell figure (S34) is the relevant one unless a cold electrolyte is specified.
4. **Cold-survival of COTS electronics.** S7 says "most" commercial parts tolerate 5 krad but also that under 30 krad commercial
   parts can "probably" be used. These are consistent only because tolerance is lot-dependent (S7 says so). I treat 5 krad as the
   untested floor and 20 to 30 krad as the best case for a tested lot.
5. **Lunar night temperature.** S56 says "below -170 C"; S20 says the equatorial minimum is 95 K (-178 C). Likely cause: S56 is
   a round figure for typical night; S20 is the equatorial extreme. Permanently shadowed craters are colder and I did not
   find a figure.
6. **Dose units.** S10 uses rads(C) (dose to carbon), S7 and S8 use krad(Si) (dose to silicon), S9 uses kGy (1 Gy = 100 rad). I
   did not convert between krad(Si) and rads(C). The conversion between rad and Gy is exact; the Si/C difference is a few
   percent for photons but I did not verify it for belt electrons, so polymer thresholds (S10) and electronics thresholds (S7,
   S8) are compared only to an order of magnitude.
7. **Robonaut 2 battery arithmetic.** S5 states about 5.79 kWh for 300 cells; 300 cells x 3.6 V x 5.3 Ah (the "5300" in the cell
   name, an assumed nominal rating) gives 5.72 kWh. The 1.2 percent difference is within the uncertainty of the assumed
   nominal voltage. I quote S5.
8. **Spirit's final temperature.** S46 (JPL) gives no number, only "colder than any of the prior six years". S47 (a news
   report of NASA's statement) gives -67 F. I mark that figure secondary.
9. **Walk-run Froude number in reduced gravity.** S44 states the transition occurs at a Froude number of about 0.5 "even in reduced
   gravity environments". S43 hypothesizes that for unsuited walkers the value rises to about 0.9 in lunar gravity, and measures 0.358 +/- 0.057
   for suited Apollo astronauts. Likely cause: different methods of simulating reduced gravity (harness unloading vs. other apparatus) and
   a suit effect. I carry 0.5, 0.9 and 0.358 as a range in D12.

## 5. Derived figures

All arithmetic below uses figures from section 3 and the stated assumptions. Assumptions are my own choices and are marked
"(assumed)". Results are bounds or order-of-magnitude checks, not predictions.

**D1. Radiated flux of a gray surface to cold space (no environment).** q = epsilon x sigma x T^4, sigma = 5.670374419e-8 W
m^-2 K^-4 (S17).
- T = 300 K: sigma T^4 = 5.670374419e-8 x 8.1e9 = 459.3 W/m2. With epsilon = 0.9: 413 W/m2.
- T = 320 K: 0.9 x 5.670374419e-8 x (320^4 = 1.0486e10) = 535 W/m2. T = 340 K: 682 W/m2. T = 360 K: 857 W/m2.
- A low-emittance surface (epsilon 0.05) at 300 K radiates 23 W/m2; at 0.02, 9.2 W/m2.
- Basis: the surface sees only cold space; real surfaces also absorb sunlight, planetary infrared and each other.

**D2. Ceiling on heat a human-sized skin can reject.** Body surface area by the DuBois formula in S45: 71.84 x W^0.423 x H^0.723.
- Valkyrie size (136.08 kg, 188 cm): 71.84 x 136.08^0.423 x 188^0.723 = 25,303 cm2 = 2.53 m2.
- Atlas size (90 kg, 190 cm; S4): 2.14 m2.
- Ceiling with every square meter seeing cold space (a view factor of 1, not possible for a body whose limbs see each other and
  the torso) and epsilon 0.9: Valkyrie size 1,046 W at 300 K and 1,354 W at 320 K; Atlas size 885 W and 1,146 W.
- Compare: S2 says a 1.8 kWh pack runs Valkyrie for "about an hour", an implied average of up to 1.8 kW if the pack is fully
  used in that hour (basis: the run condition is not stated). That would exceed the Valkyrie-size ceiling at 320 K skin
  temperature.
- Compare: S42 designs a suited human for 293 W average and 586 W peak, and uses a water sublimator to reject it.

**D3. Equilibrium temperature of a sunlit, unpowered standing cylinder.** T = (alpha x S / (pi x epsilon x sigma))^(1/4), S = 1361
W/m2 (S18). Assumptions: a cylinder whose total lateral area is pi times its projected area, uniform temperature, no
planetary infrared, albedo or ground (so this is open space or a lunar surface with the body held clear of the ground).
| alpha / epsilon (source) | Equilibrium temperature |
|---|---|
| 0.16 / 0.92, white paint Z93 (S14) | 191 K (-82 C) |
| 0.18 / 0.84 (S15 optical ratio 1) | 201 K (-72 C) |
| 0.66 / 0.74 (S15 optical ratio 2) | 287 K (+14 C) |
| 0.96 / 0.91, black paint Z306 (S14) | 300 K (+26 C) |
| 0.9 / 0.9 (a dark surface, assumed) | 296 K (+22 C) |
| 0.45 / 0.12 (S15 optical ratio 3) | 411 K (+138 C) |
- Cross-check: S15's passive cube in low Earth orbit, ratio 1, orbit-average -31 to +7 C is warmer than 201 K because low Earth
  orbit adds planetary infrared (241 W/m2, conv., S15) and albedo; the direction is right. Lunar noon blackbody:
  (1361 / 5.670374419e-8)^(1/4) = 394 K, against 390 K in S20.
- Meaning: a dark-clothed human-shaped body in full sun at 1 AU, with no internal power, already sits near room temperature.
  Every watt the body itself dissipates raises it above that.

**D4. Sunlight absorbed.** With a projected area of 0.54 m2 (assumed: 0.3 m wide x 1.8 m tall): 0.16 x 1361 x 0.54 = 118 W; 0.3 x
1361 x 0.54 = 220 W; 0.9 x 1361 x 0.54 = 661 W.

**D5. Heat loss in the dark (lunar night), and the energy it costs.** Lateral area of the cylinder = pi x 0.3 m x 1.8 m = 1.70 m2
(assumed dimensions), body at 300 K, sink near 0 K (the 95 K ground adds less than 1 percent: 696 W vs 703 W).
- Bare surface, epsilon 0.9: 413 W/m2 x 1.70 = 703 W.
- Effective emittance implied by S54's blankets: epsilon_eff = q / (sigma x (293^4 - 78^4)) with q = 0.294 to 0.411 W/m2 (best
  listed entries) gives 7.1e-4 to 9.9e-4; the poorest entries, q = 2.681 and 5.813 W/m2, give 6.4e-3 and 1.4e-2. Applied to
  the same 1.70 m2 at 300 K: 0.55 W to 0.77 W (best), 5.0 W and 10.9 W (poorest entries). These are laboratory-style blankets in vacuum
  at 2e-6 Torr with no joints or seams; a body that must bend has joints.
- Energy over one lunar night. Night length is taken as half the synodic period: 29.53 d / 2 x 24 h = 354.4 h (S20; an
  equatorial approximation). A bare body: 703 W x 354.4 h = 249 kWh. A body at an assumed 15 W (a number I chose to show the
  scale; it lies between the best and poorest S54-derived values and a seam-affected blanket): 15 W x 354.4 h = 5.3 kWh.
  The S54 poorest entry, 10.9 W: 3.9 kWh.
- Compare: Valkyrie's pack 1.8 kWh lasts 1,800 Wh / 703 W = 2.6 h bare; the Robonaut 2 Batpack, 5.79 kWh, lasts 8.2 h bare.

**D6. Radiator area and mass from ISS flight hardware.** The Photovoltaic Radiator rejects 14 kW (S16). Emitting area, assuming both
faces of 7 panels count: 2 x 3.12 m x 13.6 m = 84.9 m2 (the two-face assumption is mine; the source gives the folded
dimensions).
- 14,000 W / 84.9 m2 = 165 W per m2 of emitting surface. Mass 740.7 kg / 84.9 m2 = 8.7 kg/m2, or 52.9 kg per kW rejected.
- Cross-check: epsilon 0.9 at 270 K gives 271 W/m2 before absorbed environment; 165 W/m2 net is consistent.
- Applied to loads, at ISS-radiator performance and mass: 293 W (S42 average): 1.8 m2 and 15.5 kg. 586 W (S42 peak): 3.6 m2 and 31 kg.
  1,000 W: 6.1 m2 and 53 kg. 1,800 W: 10.9 m2 and 95 kg.
- Meaning: at ISS radiator performance, a 1.8 kW load needs 4.3 times the entire skin area of a Valkyrie-size body.

**D7. Solar charging area.** A = P / (eta x flux), then divided by an assumed 0.85 packing factor.
| Case (500 W continuous electrical charge) | Cell efficiency | Area, no packing | Area with 0.85 packing |
|---|---|---|---|
| 1 AU, 1361 W/m2 (S18); triple-junction (S33, "over 32 percent") | 0.32 | 1.15 m2 | 1.35 m2 |
| 1 AU; 20 percent silicon (S33, S29) | 0.20 | 1.84 m2 | 2.16 m2 |
| Mars top of atmosphere, 586.2 W/m2 (S19) | 0.32 | 2.67 m2 | 3.14 m2 |
| Mars top of atmosphere | 0.20 | 4.26 m2 | 5.02 m2 |
| Antarctic vertical panel, 1000 W/m2 (S29) | 0.32 | 1.56 m2 | 1.84 m2 |
| Antarctic vertical panel | 0.20 | 2.50 m2 | 2.94 m2 |
- A body covered in cells over its whole projected area (0.54 m2, assumed) and facing the Sun makes at most 0.54 x 0.32 x 1361 =
  235 W at 1 AU, 101 W at Mars top-of-atmosphere flux, and 173 W with a 1000 W/m2 Antarctic panel (0.32 efficient) or 108 W at 0.20.
  To recharge 1.8 kWh at 235 W takes 7.7 h of full sun. The Mars figures are top-of-atmosphere flux, so surface values are lower;
  I found no surface irradiance source (see Open threads).
- Cells convert about 32 percent; the other 68 percent is heat that the body must also reject.

**D8. Joint revolution budget (fluid-lubricated harmonic drive, S21).** The test stopped near 12 x 10^6 input revolutions at 160:1: 12e6 /
160 = 75,000 output revolutions (efficiency 40 percent). The high-efficiency period (80 to 90 percent) was the first 5e6 input
revolutions: 5e6 / 160 = 31,250 output revolutions.
- Duty assumed: a knee-like joint that moves 60 degrees each way once per second: 120 degrees = 0.333 revolutions per second
  of walking, or 1,200 revolutions per hour of walking.
- 31,250 / 1,200 = 26 h and 75,000 / 1,200 = 62.5 h of continuous walking.
- Basis and limits: the test ran at 4 N m, 10 percent of the 40 N m rating, at +90 C, high vacuum; heavier load or a
  different gear type changes the result. The 40 percent efficiency failure criterion is the authors' choice; a body that
  needs backdrivability or positioning accuracy may fail earlier.

**D9. Shield mass for belt crossings (S8 tables; areal density = g/cm2 in the table x 10 = kg/m2).**
- For the 10-month spiral to stay below about 20 krad (the best-case COTS tolerance in S7), 250 mil of aluminum is needed (12.4 krad):
  1.714 g/cm2 = 17.1 kg/m2. For 5 krad (the S7 "most parts" figure), 300 mil (5.34 krad, 2.06 g/cm2 = 20.6 kg/m2) is about right.
- Applied to a 0.2 m cube of electronics (0.24 m2 surface, assumed): 4.1 kg at 250 mil, 4.9 kg at 300 mil. Applied to the whole
  1.70 m2 body surface: 29 kg and 35 kg.
- For distributed electronics: 44 controllers (S1), each assumed 0.1 m on a side (0.06 m2): 1.03 kg of aluminum each, 45 kg in
  total at 250 mil, before computers.
- For a direct Earth-to-Moon transfer (3 to 6 days, S8) 5 krad lies between 25 mil (0.63 mm, 5.76 krad) and 50 mil (1.27 mm, 2.29 krad) of
  aluminum: at 50 mil that is 3.4 kg/m2, or 0.8 kg for the 0.24 m2 box.
- Per crossing: GTO phase 1 behind 100 mil gives 1.04 krad per revolution (about 5 revolutions to 5 krad); behind 200 mil, 0.0739 krad per
  revolution (68 revolutions to 5 krad, 271 to 20 krad); phase 3 behind 100 mil gives 0.391 krad per revolution (13 to 5 krad).
- Basis: S8 uses a solid sphere around the target; a box or a distributed set of boards differs, and S7 warns of diminishing return
  above about 5 mm.

**D10. Wireless power at a distance.**
- Magnetic resonance (S39): useful range up to 8 coil radii. For a body-sized coil of radius 0.2 m (assumed) that is 1.6 m; at 40 percent
  efficiency, delivering 60 W requires 60 / 0.4 = 150 W drawn, so 90 W is dissipated in the transmitter and receiver.
- Microwave (S40): tau = sqrt(A_t x A_r) / (lambda x R). With the SPS design value tau = 1.734 and the 2.45 GHz wavelength S40 used
  (12.236 cm), A_t x A_r = (1.734 x 0.12236 x R)^2. For a body-mounted receiving area A_r = 0.3 m2 (assumed): R = 3 m needs A_t = 1.35 m2;
  R = 10 m needs 15 m2; R = 30 m needs 135 m2. At 5.8 GHz (lambda 5.17 cm; a frequency I chose, not from S40) the same
  tau needs 0.24, 2.7 and 24 m2.
- Every watt received and not converted is also body heat: rectification is not 100 percent efficient (no figure found).

**D11. Walking power from cost of transport (S55 simulated values; joint power only).** P = COT x m x g x v.
- 90 kg (Atlas mass) at 1.4 m/s: COT 0.718 gives 887 W, 0.762 gives 942 W. 136 kg (Valkyrie mass) at 1.4 m/s: 1,341 W and 1,423 W.
- At 1.0 m/s: 634 W to 673 W (90 kg) and 958 W to 1,017 W (136 kg).
- g = 9.81 m/s2 (S19 prints 9.82 and S20 prints 9.80 for Earth; the difference is under 0.3 percent).
- Basis: S55's values are for 31 kg and 47 kg robots in simulation; they exclude compute, sensors and standing losses. They are an order-of-
  magnitude check and not a measured humanoid figure.
- Energy conservation (basis, not a number from a source): in level steady walking the net mechanical work per stride is near zero, so
  nearly all electrical energy consumed becomes heat unless a regenerative path stores it; S3 shows this for standing balance, where
  there is no external work but actuators still heat.

**D12. Gait transition speed with gravity.** v = sqrt(Fr x g x L) with leg length L = 0.9 m (assumed). Fr = 0.5 (S44): Earth 2.10 m/s,
Mars 1.30 m/s, Moon 0.85 m/s. Fr = 0.358 (suited Apollo gait, S43): Earth 1.78 m/s, Mars 1.10 m/s, Moon 0.72 m/s. Fr = 0.9 (S43's expected unsuited value in lunar gravity): Moon 1.15 m/s. Gravity ratios from S19
and S20: Moon 0.165, Mars 0.380 of Earth.

**D13. Skin versus radiation film.** 3 mm silicone (assumed), k = 0.2 W/m K (S51): R_skin = 0.003 / 0.2 = 0.015 m2 K/W. Radiative film
coefficient at 300 K, epsilon 0.9: h_r = 4 x 0.9 x sigma x T^3 = 5.51 W/m2 K, R_rad = 0.181 m2 K/W. The skin is 7.6 percent of
the series resistance at 300 K (5.9 percent at 273 K, 9.1 percent at 320 K). With k = 0.27, R_skin = 0.011 and the share is 5.8 percent. The
limit is the emitting surface, not the skin thickness.

**D14. Water at the Mars surface.** Mars mean pressure 6.36 mb = 636 Pa (S19). Triple-point pressure of water 611.657 Pa (S52).
Ratio 1.04. Over the seasonal range 4.0 to 8.7 mb (400 to 870 Pa) the ratio is 0.65 to 1.42.

**D15. EMU mass.** Enhanced suit assembly with two arms and two gloves 143.73 lb + life-support subsystem with a METOX CO2 canister and a
2000-series battery 196.7 lb = 340.4 lb = 154 kg (S42, Fig. 1.10). This is one configuration; the figure lists the service-and-cooling
umbilical (15.7 lb) and the airlock adapter plate (20.5 lb) separately and they are not in the sum.

## 6. Constraints for any inhabitant

Every item below is a bound a designer cannot cross, tied to a finding. Items marked "(inference)" combine two findings; the
rest restate one.

**Thermal**
- Vacuum rejects heat only by radiation (physics; D1). A surface at 300 K with epsilon 0.9 sheds 413 W/m2 at most; a Valkyrie-size body
  (2.53 m2) sheds no more than 1,046 W at 300 K or 1,354 W at 320 K (D1, D2; S17, S45). A heat load above that raises the temperature until a
  limit trips.
- The best-known actuator thermal behavior is that a balancing humanoid heats its leg actuators past a 75 C warning limit in under two minutes
  and must then rest about a minute, in air at 25 C (S3). In vacuum there is no air cooling; the body must also reject through
  radiation (inference from S3 and D1).
- A sunlit unpowered cylinder-shaped body at 1 AU settles at 191 K to 300 K (white to black surface), and higher with a low-emittance coating
  (D3; S14, S15, S18). Skin and clothing optical properties set the body's temperature as much as its own power does.
- Working humanoid temperature limits that are published: Valkyrie actuators 90 C maximum (S3); Atlas -20 to +40 C operating (S4); typical
  ISS spares lower limit -40 C (S15); Li-ion cells -20 to +60 C operating, +20 to +40 C optimum (S33, S36). These do not cover lunar night
  (-170 C, S56), Mars night (-89 C, S19) or low Earth orbit shade without added heat or insulation.
- A silicone-class skin is rated -45 to +200 C and has a large expansion coefficient, 310 ppm/C (S51). Below about -45 C it is outside its stated
  service range.
- Insulation of the vacuum-MLI kind works only in vacuum; in air it behaves as a stagnant gas pocket and its published performance does not hold
  (S54). A body that lives in air and in vacuum cannot rely on one insulation layer for both (inference).
- Surviving a lunar night with a body at room temperature costs energy: a bare body loses 703 W (D5), which exhausts a 1.8 kWh pack in 2.6 h;
  with a blanket-grade insulating layer the loss is 0.6 W to 11 W (laboratory-derived from S54), which is 0.2 to 3.9 kWh over a night
  (D5). No source gives the performance of such insulation on a flexing body.
- Sunlight absorbed by a body is large against its own electrical power: 118 to 661 W for 0.54 m2 (D4; S14, S18).

**Radiation**
- Untested commercial electronics fail somewhere between under 1 krad and 20 krad or more; lots vary (S7). A tested lot is plausibly good to 20 to 30
  krad (S7). Hardened parts are rated 100 krad to above 1 Mrad (S7); NASA's next flight computer is specified at 200 krad (S11).
- Hardened processors are far slower and more expensive than commercial ones; the RAD750 is 133 to 166 MHz, about 300 MIPS, and over $200,000 (S12).
  Commercial parts used in a robot of Valkyrie's class run 3 Core i7 computers (S1). The two cannot be swapped without a large performance loss
  (inference).
- Crossing the Earth's trapped-radiation belts costs between about 0.0006 krad (900 mil of aluminum) and 128 krad (1 mil) for a one-way direct
  transfer; a long belt spiral costs 5.34 krad at 300 mil and 545 krad at 100 mil (S8). Repeated crossings add: a body that crosses an elliptical
  belt orbit 270 times behind 200 mil absorbs 20 krad (D9).
- Shielding returns diminish beyond about 5 mm of aluminum (S7) and cost 17 to 21 kg/m2 at the thicknesses that matter (D9). A body whose
  electronics are spread through its limbs (44 controllers, S1) cannot be protected by one central shield (inference from S1, S7, D9).
- Soft skin outlasts the electronics: silicone rubber insulation shows no noticeable change at 8.8 x 10^5 rads (880 krad) and serious damage at
  8.8 x 10^7 rads (S10). Against the 5 to 30 krad commercial-electronics figures in S7 that is 29 to 176 times the no-change dose and
  2,900 to 17,600 times the serious-damage dose. PTFE is much weaker: damage starts near 1.7 x 10^4
  rads (S10). PFPE lubricants degrade under X-rays (S13).
- Li-ion cells do not set the radiation limit: lithium-metal cells given 20 kGy kept 57.7 to 70.3 percent of capacity after 350 cycles against 76.6 to
  94.2 percent for controls (S9), with the electrolyte the weak point.

**Vacuum and materials**
- Every non-metal inside a habitat or flown outside is screened for outgassing (at most 1.0 percent mass loss, 0.10 percent condensable at 125 C, 24 h,
  S24) and flammability (S5). Silicones of space grade pass (S25); an arbitrary skin or fabric is not guaranteed to.
- Clean metal surfaces cold-weld: a clean surface recontaminates in seconds at 10^-6 torr and under 10^-8 s at one atmosphere (S23). Bare same-metal
  sliding joints in vacuum are a design hazard (inference from S23).
- Fluid-lubricated precision gears in vacuum last on the order of 31,000 to 75,000 output revolutions before efficiency drops (S21), which at one
  knee-like cycle per second is 26 to 62 hours of walking (D8). PFPE lubricants in steel contacts can fail abruptly (S22).
- Dry lubricant (MoS2) works well in vacuum and poorly in humid air (S22). A body that goes between humid habitat air and vacuum meets both.
- Dust: lunar dust wore an Apollo suit through its outer layer in 8 hours of use, seals leaked at 0.15 to 0.25 psi/min against a 0.30 psi/min limit,
  and a 10 psi nitrogen jet removed almost none of the fine dust (S26). Dust on radiating surfaces doubled absorptance at 11 percent coverage (S26).
- Water-bearing layers: the vapor pressure of water at 273.16 K is 611.657 Pa (S52). That is about Mars's mean surface pressure (636 Pa, range 400
  to 870 Pa, S19) and far above the Moon's (3 x 10^-15 bar, S20); liquid water in an exposed layer evaporates or freezes unless contained
  (inference from S52, S19, S20).

**Power**
- Cell-level specific energy is 182 to 264 Wh/kg for Li-ion (S33). A 1.8 kWh pack needs at least 6.8 kg of cells at 264 Wh/kg (1,800 / 264) and 7.4
  kg at 243 Wh/kg, before packaging.
- Li-ion cells lose most of their energy in the cold (5 percent left at -40 C at a slow rate for a commercial 18650, S34), plate lithium irreversibly
  when cycled at -20 C (S35), and are qualified for charging only above -10 C on Mars missions (S36).
- Body-mounted solar cells at 1 AU yield at most about 235 W on 0.54 m2 (D7). Recharging a pack from the body alone takes hours and is useless in
  shade; on Mars top-of-atmosphere flux the same area yields about 101 W.
- Wireless charging by magnetic coupling reaches only a few coil radii (S39), and by microwave needs transmitting aperture on the order of square
  meters at tens of meters (D10; S40). Neither is free of heating (D10).

**Mechanical and surface**
- Torque density of the best published frameless motor is about 27 N m/kg (S28); catalog motors are about 9 N m/kg. Gear efficiency starts at 80 to 90
  percent (S21), so a standing, balancing body dissipates the rest as heat (S3).
- Walk-run transition speed scales with the square root of gravity (S43, S44): a 0.9 m leg gives 0.85 m/s on the Moon and 1.30 m/s on Mars (D12).
- A pressurized suit glove leaves 46 to 58 percent of bare-hand grip (S41); an EMU weighs about 154 kg in one configuration (S42). A robot that
  wears a pressure garment inherits these costs; a robot that does not must put every part of itself through vacuum (inference).
- In microgravity translation is by handrails whose load and moment limits cap the force a body may apply (S5).

**Lifetime**
- Long-duration machines fail mostly at wheels, joints, motors and power distribution, and are fixed by replacement or by changing how they are used:
  Opportunity's right-front wheel was driven backward to extend its life (S46); Curiosity's 0.75 mm wheel skin was damaged faster than expected (S48);
  Canadarm2 needed a wrist joint swapped after 25 years (S49); Robonaut 2's anomaly was a power-return wiring fault that overheated a connector and
  could not be fixed on orbit (S50).
- Cold survival depends on power: Spirit lost its survival heaters and did not wake (S46).

## 7. Candidate handwaves

Nothing here is accepted. The developer decides. Each is a place where a design that matches the fiction's look (realistic skin,
clothing and gloves; human size; vacuum-capable) meets a bound above. Each item is tagged **bend** (physics would have to give if the
scene is shown as imagined) or **cost** (physics holds, but a mechanism, mass, power or duty cycle must be accepted and shown).

1. **[bend if shown as imagined; cost if a mechanism is added] Rejecting a full day's body heat through human-sized skin in vacuum at a body temperature that skin and clothing survive.**
   D2 shows a ceiling of about 1.0 to 1.35 kW for a Valkyrie-size body even with ideal view factors; real bodies have limb-to-limb view factors,
   absorbed sunlight (118 to 661 W, D4) and planetary infrared. A machine that does heavy work for hours in sun would need a heat-rejection
   mechanism beyond radiation from its skin (an expendable-fluid sublimator like the EMU, S42, or a deployable radiator like the ISS's, S16) or a
   duty cycle that rests it in shade. A "walks in vacuum all day in sunlight" scene needs an explicit mechanism.
2. **[cost] Survival through a lunar night or Mars night without a heat source.** The numbers in D5 show a bare body cannot do it on a battery; a
   blanket-grade insulating layer under realistic clothing, or a radioisotope or reactor heat source, is required. Realistic skin rated only to -45
   C (S51) is outside its range for the night.
3. **[cost] Realistic polymer skin and fabric that is also vacuum-safe.** Ordinary skin-grade silicone and clothing fabric are not shown to meet outgassing and
   flammability screening without selection (S5, S24, S25), and trapped gas or water in a soft layer reacts to vacuum. Not a physics bend; a materials
   choice that the fiction must make (for example, space-grade silicone skin; fabrics like Nomex).
4. **[bend] A body that works for years without servicing joints.** S21 shows fluid-lubricated precision gears wearing out in tens of hours of walking duty
   under assumed conditions, and S49 and S50 show that even long-lived space robots are repaired by swapping parts. A fiction where a robot walks for
   years in dust and vacuum without a rebuild would bend D8 and S26; a fiction where such bodies have routine part replacement does not.
5. **[bend] Radiation-hard brain-and-body control electronics at human body scale with commercial-grade performance.** The fiction waves the gel brain (H-1)
   only. The body's motor control, sensors and power conditioning are electronics and fall under S7, S8, S11 and S12. Surviving repeated trapped-belt
   crossings without a heavy shield and without rad-hard performance penalties would bend D9 (shielding mass) or S12 (hardened-part speed).
6. **[bend] Recharging from a distance without large apertures or heating.** D10 shows that wireless power at meter range needs coils of body size and
   dissipates most of the energy as heat, and that microwave power at tens of meters needs square-meter-scale apertures. A robot that "plugs into the air"
   at long distance would bend S39 and S40.
7. **[cost] Charging a Li-ion pack outdoors in the cold.** S35 and S36 show charging below about -10 C damages cells. A fiction in which robots recharge
   outdoors at Antarctic temperatures needs a warmed pack or a different cell chemistry; none is flight-proven in the sources found (S34 is lab-scale).
8. **[cost] Clothing that is both cloth-like in air and insulating in vacuum.** If clothing is only cosmetic, the body has no insulation in vacuum (D5: 703 W lost when bare). If clothing
   is to act as insulation it must be vacuum-grade multilayer insulation, which behaves like a stagnant gas pocket in air (S54), so insulation in
   vacuum is not a free property of cloth.

## 8. Open threads

**Checklist items not satisfied from a primary source, with the reason.**
- **Digit, Optimus and Figure power and heat figures (checklist A and D).** Agility's and Figure's sites publish no specifications; Tesla's AI Day 2022
  figures reached me only through press (search summaries quoted 2.3 kWh, about 100 W sitting and about 500 W brisk walking; Digit about 1 kWh,
  Digit 5 about 90 min run and 9 min recharge). None opened at a primary. Next: the Tesla AI Day 2022 transcript or video; Agility's 2025-2026
  datasheet; independent teardown or paper with measured watts.
- **Valkyrie continuous power draw in watts.** Not published in anything I reached. Next: Radford et al., J. Field Robotics 2015; IHMC
  papers on Valkyrie (energy per step); NASA ER4 technical memoranda.
- **Thermal vacuum test data for Robonaut 2.** I found only qualitative statements (S5, S6). A search summary quoted "-25 C to 105 C" for two
  R2/Robonaut arm joint actuators in the JSC chamber with new lubricants; not verified. Next: NTRS search for Ambrose and Berka, "Thermal
  Management in Hyper-Redundant Space Manipulators" (SPIE 1993), and R2 joint qualification reports.
- **Humanoid heat fraction.** No source gives the share of electrical power that becomes heat in a humanoid. I used energy conservation (D11).
  Next: a measured power-balance paper on a humanoid (Valkyrie, TALOS, Atlas, Digit).
- **Li-ion and solid-state cell behavior in vacuum.** I found only qualification requirements (S36, S37), not data on cell swelling, venting, or
  electrolyte loss during use in vacuum. Next: NASA battery workshop papers on pouch cells in thermal vacuum (NTRS 20060020764 was a stub).
- **Hardened-processor datasheets.** BAE's RAD750 datasheet returned HTTP 403 (curl and WebFetch). A search summary quoted 200 krad (rad-tolerant)
  and 1 Mrad (rad-hard) and a latch-up-immune single-event rate below 1.6e-10 errors/bit-day; unverified.
- **NASA per-material outgassing values.** The NASA database (outgassing.nasa.gov) is dynamic and I could not query it; NASA RP-1124 Rev 4 was an
  unreadable scan. I have no TML/CVCM for ordinary skin silicone, PVC, polyurethane foam or fabrics. Next: JAXA matdb.jaxa.jp data lists, or a
  library scan of RP-1124.
- **Textile and skin optical and thermal properties.** I found no solar absorptance and emittance for ordinary clothing fabric or skin-colored
  silicone. Kauder (S14) lists coatings and Beta cloth only. Next: ECSS or NASA tables for Nomex, Kevlar and silicone elastomers.
- **Mars surface solar irradiance and dust loss.** S19 gives top-of-atmosphere flux only. Press reports quoted Opportunity falling from about 700 Wh
  per sol to 22 Wh per sol in the 2018 storm (optical depth 10.8); unverified. Next: Lorenz et al. or JPL MER power reports.
- **Permeation and blistering of soft skins in vacuum.** A search summary quoted PDMS oxygen permeability of 800 Barrer (Merkel et al., 2000);
  unverified, not used. Next: Merkel et al., J. Polym. Sci. B 38:415-434.
- **PFPE radiation dose threshold.** S13 gives mechanism only. Next: the ESTL or Krytox radiation stability data (a vendor page exists; not opened).
- **Convective cooling in the Mars atmosphere** (6.36 mb of CO2) for a warm body; not searched.
- **Dextre service history and design life.** Only Wikipedia and news reached me (15-year design life, tool-change and camera swap history); not tabulated.
- **Perseverance, ISS CMG or other long-duration machine reliability data**; not searched beyond the machines above.
- **Cold-weld experiments beyond the NASA patent**, and ESA tribology handbook values; not opened.
- **Lunar and Mars regolith wear rates on robot joints and seals in controlled tests** (beyond Apollo reports); S27 reviews seals but I did not extract its test data.
- **Antarctic humanoid or legged-robot trials.** Press mentions a Chinese hexapod run at -40 C with an insulated battery for two hours and an Arctic
  quadruped traverse; no paper opened. Next: Zhongshan trial papers; Arctic/Antarctic legged robot field reports.

**Sources found but not read (or only skimmed).**
- NTRS 20200000214 (Opportunity End of Mission Report): abstract only; no downloadable PDF.
- NTRS 20100009705 (JPL, safe charge rates and lithium plating): abstract page only.
- JPL FY21 R&TD poster R22020p; NASA Glenn "SiGe" low-temperature electronics pages; NASA NEPP "Careful COTS" guidance.
- Merstallinger et al. (RADHARD 2024) tribology and radiation abstract (page returned 404).
- NASA TM-2009-215751 (read for qualification tables and vacuum text only, not the whole report).
- S27 (Proctor and Dempsey): read for seal slides only.
- Caltech SSPD-1 / MAPLE papers; JAXA microwave transmission papers.
- Daryabeigi et al. NTRS 20060019134 (high-temperature MLI), downloaded, not read.
- The 1971 handbook NASA CR-1787 Sections beyond the polymers cited; DTIC radiation handbooks (maintenance page).

## 9. Rejected sources

- **Wikipedia and Wikipedia mirrors** (Robonaut, Dextre, Valkyrie, Opportunity, Canadarm2): used only for leads; no number taken.
- **Press and marketing pages for Tesla Optimus, Digit, Figure, Atlas specs aggregators** (benzinga, tomsguide, siliconcanals, qviro,
  aiwiki, robotsguide, humanoid.press, robozaps): secondary and inconsistent; kept as leads only.
- **Vendor pages on energy-per-kilogram and torque-density claims** (firgelli, patsnap, thehumanoid.ai, longsingtech): blog-grade figures with no
  measurement method; replaced by S28 and S33.
- **A search summary quoting 15 kW for the hydraulic Atlas**: no primary behind it; not used.
- **Search-summary-only figures** for Juno's 1 cm titanium vault (a factor of 800), JAXA 1.8 kW at 55 m, PDMS permeability, RAD750 datasheet values, and
  the R2 "-25 to 105 C" claim: listed under Open threads, not used in tables or derivations.
- **The clo unit (0.155 m2 K/W)**: seen only in search summaries and encyclopedic pages; not needed after D13.
- **Patterson et al. (S53) Table 1 temperatures**: the minus signs are missing from the PDF text layer, so every temperature in that table reads as
  positive; I used only its qualitative statements.
- **Wow Orin arXiv preprint (S55)** is kept in the tables as secondary, simulation-only, and not used as a bound, only as an order-of-magnitude check
  in D11.
- **The NASA RP-1124 scan (NTRS 19970027853) and DTIC ADA303760**: unreadable or unavailable.
