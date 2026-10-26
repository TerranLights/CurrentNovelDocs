# Starlifting: physics, literature and minimum infrastructure for harvesting material from the Sun

*Research file. Real physics and engineering only. Compiled 2026-10-11 (two runs; complete).*

## 1. Scope

The Sun as a source of raw material ("starlifting"): the literature's mechanisms and rates, solar composition, the energy
and mass-flow scales of lifting and of the natural solar wind, what near-Sun hardware has survived, and the smallest
collection concepts. Mercury, the Moon, asteroids, Venus, Jupiter and Saturn appear only as comparison sources for the same materials.

*Note on the session break: rows 1 to 50 were logged by the first run of this task, which was cut off by a usage limit
before any findings were written. The second run (rows 51 on) re-opened every source whose numbers it uses, so every
figure below was read in the second run, except those attributed to the two sibling files, which are cross-referenced
from them as they stand.*

## 2. SEARCH LOG

| # | Date | Search string (verbatim) or page opened | Result | Dead at |
|---|---|---|---|---|
| 1 | 2026-10-11 | Read (allowed, read-only) sibling files `belt_jupiter_saturn_and_deep_transit.md` and `moon_lagrange_and_comparables.md` (first halves, plus a grep of both for Mercury, Venus, He-3, solar wind, Genesis, Parker) | useful | Neither covers the Sun, Mercury, Venus or gas-giant He-3 harvesting; belt mass/composition and lunar resources are cross-referenced, not repeated |
| 2 | 2026-10-11 | `Criswell "star lifting" solar system industrialization interstellar migrations 1985` | useful (leads) | Identified Criswell 1985 chapter and Matloff 2017 JBIS; search summary not used for numbers |
| 3 | 2026-10-11 | `Scoggins Kipping "Lazarus stars" star-lifting stellar evolution MNRAS` | useful | Found arXiv 2210.02338 |
| 4 | 2026-10-11 | Page: https://arxiv.org/pdf/2210.02338 (raw, pdftotext), Scoggins and Kipping, v2 8 Jun 2023, MNRAS 523:3251 | useful | Read in full. MESA star-lifting rates, Eq. 2 power floor, quotes Matloff 2017 per-kg energy |
| 5 | 2026-10-11 | Page: https://bis-space.com/shop/product/star-lifting-an-application-for-alien-megastructures/ (WebFetch) | thin | Matloff 2017 abstract only; the paper body is paywalled. Died at the sources for numbers |
| 6 | 2026-10-11 | `Matloff 2017 "star lifting" JBIS 70 458 pdf mass loss laser photosphere scenarios` | thin | No open copy; surfaced Harry 2026 JBIS preprint |
| 7 | 2026-10-11 | `Criswell 1985 "Interstellar Migration and the Human Experience" star lifting pdf "solar system industrialization" full text` | dead, died at the sources | Book out of print; no open full text |
| 8 | 2026-10-11 | Internet Archive metadata API for `interstellarmigr0000unse` and `interstellarmigr0000unse_h4h6` | dead, died at the sources | Both copies are `access-restricted-item: true` (controlled lending); text not retrievable |
| 9 | 2026-10-11 | Page: https://arxiv.org/pdf/2607.13084 (raw), G. Harry, "Retaining Earth's Habitability Beyond the Life of the Sun", JBIS 79:230 (July 2026) | useful (as a concept paper; contains an arithmetic error, see Conflicts) | Sections 1, 2.1 and Table 1 read |
| 10 | 2026-10-11 | Page: https://en.wikipedia.org/wiki/Star_lifting (WebFetch) | thin (secondary, leads only) | Lists three mechanisms (heating, "huff-n-puff", centrifugal ring) and an internally inconsistent J/kg figure; no number used |
| 11 | 2026-10-11 | `Beech "Rejuvenating the Sun and Avoiding Other Global Catastrophes" star lifting mass loss rate chapter` | thin | Springer book (2008), chapter list only; no open text. Died at the sources for numbers |
| 12 | 2026-10-11 | `Criswell "huff-n-puff" star lifting magnetic field polar nozzle ring current stellar mass extraction` (extended) | thin (secondary only) | Every hit is Wikipedia, its mirrors, Orion's Arm or a blog. No primary description of the ring-current or "huff-n-puff" designs exists online; died at the sources |
| 13 | 2026-10-11 | `Caplan 2019 "Stellar engines: Design considerations for maximizing acceleration" Acta Astronautica mass loss rate kg/s` | thin | Popular coverage only (Big Think); leads |
| 14 | 2026-10-11 | `Beech asteroengineering stellar mass loss "star lifting" Journal of the British Interplanetary Society OR "Earth, Moon, and Planets" blue stragglers` | useful (lead) | Found Carrigan, arXiv 1001.5455 |
| 15 | 2026-10-11 | Page: https://arxiv.org/pdf/1001.5455 (raw), R. Carrigan (Fermilab), "Starry Messages: Searching for Signatures of Interstellar Archaeology" (preprint, Jan 2010; published JBIS 63, 2010) | useful | Pages 14-15 read: Beech's L proportional to M^5 scaling and "roughly 60%" mass dispersal; Carrigan's own feasibility judgment |
| 16 | 2026-10-11 | `Caplan "stellar engines" design considerations maximizing acceleration pdf Dyson sphere helium hydrogen jet 10^12 kg/s solar wind collection` (extended) | thin | ScienceDirect landing pages; paper paywalled |
| 17 | 2026-10-11 | Pages: ScienceDirect S0094576519312457 and S0094576520307062 (WebFetch) | dead, died at the sources | HTTP 403 |
| 18 | 2026-10-11 | Crossref API and OpenAlex API for DOI 10.1016/j.actaastro.2019.08.027; Semantic Scholar API for that DOI, 10.1016/j.actaastro.2020.11.030 and 10.1016/j.actaastro.2020.07.005 | useful | Full abstracts of Caplan 2019, Svoronos and Caplan 2021 (erratum-comment), Svoronos 2020 "Star Tug". OpenAlex also returned an unrelated 2026 Zenodo item (not used) |
| 19 | 2026-10-11 | Page: https://arxiv.org/pdf/2105.01661 (raw), Asplund, Amarsi, Grevesse, "The chemical make-up of the Sun: A 2020 vision", A&A 653, A141 (2021), v2 14 Jul 2021 | useful | Table 2 photospheric log-abundances; Table 4 X, Y, Z (present-day and proto-solar) for ten compilations |
| 20 | 2026-10-11 | Page: https://arxiv.org/pdf/0909.0948 (raw), Asplund, Grevesse, Sauval, Scott, "The chemical composition of the Sun", ARA&A 47:481 (2009) | useful | Table 1 used as the cross-check of every element |
| 21 | 2026-10-11 | Page: https://www.ciaaw.org/abridged-atomic-weights.htm (raw), IUPAC CIAAW, Abridged Standard Atomic Weights 2024 | useful | Atomic weights for the conversion of number abundance to mass fraction |
| 22 | 2026-10-11 | Local Python (scratchpad `abund.py`): number abundance to mass fraction | useful | Method check: computed He mass fraction 0.2423 equals Asplund 2021's stated Y exactly |
| 23 | 2026-10-11 | Page: https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html (raw, curl), NASA NSSDCA Sun Fact Sheet, last updated 9 May 2024 | useful | Mass, GM, radius, escape speed, luminosity, mass conversion rate, photosphere composition by number, field strengths |
| 24 | 2026-10-11 | `solar wind mass loss rate solar cycle coronal mass ejections contribution percent kg/s Mishra 2019 arXiv` | useful | Found Mishra et al. 2019 and Cranmer 2017 |
| 25 | 2026-10-11 | `Cranmer 2017 "Mass-loss rates from coronal mass ejections" solar-type stars ApJ arXiv solar wind 2e-14 solar masses per year` | useful | Confirms Cranmer 2017 identity |
| 26 | 2026-10-11 | Pages: https://arxiv.org/pdf/1904.09898 (raw), Mishra et al., MNRAS (accepted 8 Apr 2019); https://arxiv.org/pdf/1704.06689 (raw), Cranmer, ApJ 840 (2017) | useful | Wind and CME mass-loss rates, CME share of wind, total LASCO CME mass |
| 27 | 2026-10-11 | `table typical solar wind parameters at 1 AU proton density cm-3 speed km/s helium abundance slow fast wind review arXiv` | useful (leads) | Led to Larrodera and Cid 2020 and to Verscharen et al. 2019 |
| 28 | 2026-10-11 | Page: https://arxiv.org/pdf/1902.03448 (raw), Verscharen, Klein, Maruca, "The multi-scale nature of the solar wind", Living Rev. Sol. Phys. 16:5 (2019) | useful | Table 1 typical 1 au and coronal values |
| 29 | 2026-10-11 | Page: https://www.aanda.org/articles/aa/full_html/2020/03/aa37307-19/T1.html (WebFetch) | dead, died at the sources | HTTP 403; same table read from the arXiv copy (row 30) |
| 30 | 2026-10-11 | Page: https://arxiv.org/pdf/2003.09172 (raw), Larrodera and Cid, "Bimodal distribution of the solar wind at 1 AU", A&A 635, A44 (2020) | useful | Tables 1, 3, 4: slow and fast wind speed, density, field, temperature (ACE data) |
| 31 | 2026-10-11 | `Genesis mission solar wind sample total mass collected micrograms "10^20" ions NASA JPL` | thin | The "0.4 mg / 10^20 ions" figure appears only in Wikipedia and eoPortal (secondary); led to NASA PDFs |
| 32 | 2026-10-11 | `Kasper 2007 solar wind helium abundance function of speed heliographic latitude ApJ 660 901 A_He percent` | thin | Search summary only; the CfA-hosted PDF did not download (row 33). Helium abundance not taken from it |
| 33 | 2026-10-11 | Pages: Genesis JPL launch press kit (https://www.jpl.nasa.gov/news/press_kits/genesislaunch.pdf, July 2001, raw); NASA JSC ARES Genesis infographic (raw); solarsystem.nasa.gov CSUN_062504d.pdf (returned an HTML shell, dead at the sources); Kasper 2007 PDF at lweb.cfa.harvard.edu (no file returned, dead at the sources) | useful (press kit, infographic) | Press kit: goal 10-20 micrograms, spacecraft 636 kg, cost; infographic: 884 days at L1, 300 wafers |
| 34 | 2026-10-11 | `Burnett Genesis Discovery mission solar wind collector total area cm2 fluence 884 days "Space Science Reviews" OR PNAS 2011 solar composition` | useful (leads) | Led to the JSC LPSC abstracts |
| 35 | 2026-10-11 | Pages: Burkett et al., LPSC 40 (2009) abstract 1373 (raw); Burnett and Genesis Science Team, LPSC 37 (2006) overview (raw); solarsystem.nasa.gov/genesismission/gm2/mission/collecting.htm (returned only page styling; dead at the sources) | useful | Total flown collector 1,672,944 mm2; 5 arrays about 80 cm, about 54 hexagons each; concentrator factor 22; 1 keV/amu implantation |
| 36 | 2026-10-11 | `"Hydrogen fluence in Genesis collectors" solar wind H fluence atoms cm-2 value` | useful | Identified Huss et al. 2019 (PMC7120949); search-summary numbers differ from the paper and are not used |
| 37 | 2026-10-11 | Europe PMC REST fullTextXML for PMC7120949 | dead, died at the sources | HTTP 500 |
| 38 | 2026-10-11 | Page: https://pmc.ncbi.nlm.nih.gov/articles/PMC7120949 (WebFetch digest, first 100,000 characters) | useful | Huss et al., Meteorit. Planet. Sci. (2019): 853 days exposure; bulk H fluence 1.634e16 per cm2 |
| 39 | 2026-10-11 | `Parker Solar Probe closest perihelion December 24 2024 distance 6.1 million km speed heat shield temperature NASA` | useful (leads) | Led to NASA SVS 5428 |
| 40 | 2026-10-11 | `Parker Solar Probe Thermal Protection System design carbon-carbon foam 1377 C 2500 F solar array cooling water NTRS OR jhuapl technical paper` | thin | Trade and popular pages only; no NTRS paper surfaced (died at the query for a primary) |
| 41 | 2026-10-11 | Fox et al. 2016, Space Sci. Rev. 204:7 (DOI 10.1007/s11214-015-0211-6): Springer PDF via curl, Unpaywall, Europe PMC, Semantic Scholar; article page via WebFetch | dead, died at the sources | CC-BY paper, but Springer returned a bot-check page to curl and an authentication redirect to WebFetch |
| 42 | 2026-10-11 | Pages (raw, curl): parkersolarprobe.jhuapl.edu The-Mission and Spacecraft pages; science.nasa.gov/mission/parker-solar-probe/; svs.gsfc.nasa.gov/5428 | useful | Mass, TPS, arrays, 388 W, perihelion distances; the APL Spacecraft page gives two different shield temperatures (see Conflicts) |
| 43 | 2026-10-11 | `Parker Solar Probe launch press kit pdf 2018 "solar array cooling system" radiators water "475 times" sunlight intensity` | useful | Found the NASA press kit |
| 44 | 2026-10-11 | Page: https://www.nasa.gov/wp-content/uploads/2018/02/parkersolarprobe_presskit_august2018_final.pdf (raw), NASA, Aug 2018 | useful | TPS 2.4 m and 115 mm (and 2.3 m elsewhere in the same kit), tested to 1,650 C, 3.7 L water coolant 10 to 125 C, autonomy, launch energy 55 times Mars, solar wind "a million tons" per second |
| 45 | 2026-10-11 | `Parker Solar Probe perihelion "9.86" solar radii orbit 88 days final orbit 2024 2025 encounter` | useful | Led to HAO/NCAR WHPI campaign pages |
| 46 | 2026-10-11 | Page: https://whpi.hao.ucar.edu/whpi_campaign-psp22p.php (WebFetch) | useful | Perihelion 22: 11:41 UT 24 Dec 2024, about 0.046 au, 9.86 solar radii (heliocentric) |
| 47 | 2026-10-11 | `ESA Solar Orbiter heat shield 0.28 AU 13 times sunlight 500 °C titanium SolarBlack calcium phosphate feedthroughs` | useful (leads) | |
| 48 | 2026-10-11 | Page: https://www.esa.int/Science_Exploration/Space_Science/Solar_Orbiter/Preparing_for_extreme_environments (WebFetch), ESA, 7 Oct 2019 | useful | 42 million km, 13 times Earth-orbit heating, 20 titanium layers to 500 C, 30 insulation layers to 300 C, 1.8 t |
| 49 | 2026-10-11 | `Solar Probe 2005 Science and Technology Definition Team report 4 solar radii perihelion heat shield temperature 2100 C NASA TM` | useful | The 2005 report itself (NASA/TM-2005-212786) was not opened; the 2008 successor report was. The "2100 C" in my query was a guess and is not used |
| 50 | 2026-10-11 | Page: https://ntrs.nasa.gov/api/citations/20080032529/downloads/20080032529.pdf (raw), NASA/TM-2008-214161, "Solar Probe Plus: Report of the Science and Technology Definition Team", July 2008 | useful | Sections 4.6 to 4.8 and Appendix B read: 400 W/cm2 at 4 Rs versus 70 W/cm2 at 9.5 Rs; TPS about 1700 K; allowable TPS mass loss 2.5 mg/s; heat leak under 50 W; cells under 120 to 180 C; dust spallation |
| 51 | 2026-10-11 | *Second run begins.* Re-read this file's SEARCH LOG (rows 1 to 50), the brief, and the dispatch prompt | useful | No findings had been written by the first run; every number below is re-read from source in this run |
| 52 | 2026-10-11 | Re-opened (curl + pdftotext): arXiv 2210.02338 (Scoggins and Kipping), 2105.01661 (Asplund 2021), 0909.0948 (Asplund 2009), 1904.09898 (Mishra 2019), 1704.06689 (Cranmer 2017), 1902.03448 (Verscharen 2019), 2003.09172 (Larrodera and Cid), 1001.5455 (Carrigan), 2607.13084 (Harry 2026) | useful | All nine downloaded and read at the cited passages |
| 53 | 2026-10-11 | Re-opened: NASA NSSDCA Sun Fact Sheet; CIAAW abridged atomic weights 2024; NASA PSP press kit (Aug 2018); NASA/TM-2008-214161 (NTRS 20080032529); JPL Genesis launch press kit (2001) | useful | All read at the cited passages |
| 54 | 2026-10-11 | Re-ran the first run's abundance script (copied to the second run's own script folder) after checking every input against Asplund 2021 Table 2, Asplund 2009 Table 1 and CIAAW 2024 | useful | Inputs verified; He mass fraction reproduces Asplund 2021's Y = 0.2423 |
| 55 | 2026-10-11 | Re-opened: LPI, Burkett et al., LPSC 40 (2009) abstract 1373, https://www.lpi.usra.edu/meetings/lpsc2009/pdf/1373.pdf | useful | Total flown collector area 1,672,944 mm2 |
| 56 | 2026-10-11 | Page: https://www.lpi.usra.edu/meetings/lpsc2006/pdf/2327.pdf (my guess at the URL of the Burnett 2006 Genesis overview) | dead, died at the query | Returned an unrelated Mars thermal-conductivity abstract; the URL was wrong. Not used |
| 57 | 2026-10-11 | Re-opened (WebFetch): https://pmc.ncbi.nlm.nih.gov/articles/PMC7120949 (Huss et al. 2019) | useful | 853 days exposure; bulk H fluence 1.634 +/- 0.028 e16 per cm2; per-regime fluences |
| 58 | 2026-10-11 | Re-opened (WebFetch): ESA Solar Orbiter "Preparing for extreme environments" (7 Oct 2019); HAO WHPI PSP perihelion 22 page | useful | As in rows 46 and 48 |
| 59 | 2026-10-11 | Pages (curl): svs.gsfc.nasa.gov/5428; science.nasa.gov/mission/parker-solar-probe/; parkersolarprobe.jhuapl.edu/The-Spacecraft/ (two URL forms) | useful (NASA pages); dead (APL, 404, died at the sources: the page has moved since the first run) | SVS: 3.86 million miles from the surface on 24 Dec 2024. NASA mission page: shield 1,377 C, 685 kg at launch, 430,000 mph |
| 60 | 2026-10-11 | Local Python (second run's script folder): escape energy, lift-power fractions, wind kg/s, collector areas, Genesis mass, equilibrium temperatures, Mercury core mass, gas-giant He-3 fractions, Venus carbon | useful | Output used in section 5 |
| 61 | 2026-10-11 | `solar wind collection spacecraft magnetic scoop harvest helium-3 hydrogen propellant concept paper kg per year` | thin | Hits were forums, "halfbakery", Genesis status pages and lunar He-3 lectures; no quantitative space-based solar-wind collector design. Died at the sources |
| 62 | 2026-10-11 | Page: NTRS 20070014073 (Minow et al., "Genesis Radiation Environment") | thin | About the spacecraft's radiation environment, not collection yield; not used |
| 63 | 2026-10-11 | Page: Genesis 2003 status-update PDF at solarsystem.nasa.gov | dead, died at the sources | Returned an HTML shell, as in row 33 |
| 64 | 2026-10-11 | Page: fti.neep.wisc.edu NEEP 533 lecture 12 (Univ. of Wisconsin, 2004) | thin | Lecture slides on lunar He-3; secondary; not used for numbers (the sibling Moon file already holds lunar He-3 from a review) |
| 65 | 2026-10-11 | `Armstrong Sandberg "Eternity in six hours" Mercury disassembly Dyson swarm arXiv` | useful (leads) | Forums and summaries; led to the paper |
| 66 | 2026-10-11 | Page: fhi.ox.ac.uk/wp-content/uploads/intergalactic-spreading.pdf (direct) | dead, died at the sources | curl failed (site retired) |
| 67 | 2026-10-11 | Page: Internet Archive copy of the same PDF (preprint of Acta Astronautica 89:1-13, 2013) | useful | §4.1-4.2 read in full: Mercury disassembly assumptions and result |
| 68 | 2026-10-11 | `Palaszewski atmospheric mining outer solar system helium-3 Uranus Saturn Jupiter NASA technical memorandum mining rate kg` | useful | Three NTRS papers found |
| 69 | 2026-10-11 | Pages: NTRS 20150006664 (Palaszewski, "AMOSS: Resource Capturing, Storage, and Utilization"); NTRS 20170004746 ("Outer Planet Orbital Transfer and Lander Analyses"); NTRS 20205004479 (AIAA 2020, "Aerospacecraft Analysis...") | useful | Capture-rate and mining-time figures; aerospacecraft delta-v; Table I (He-3 fractions) is an image and could not be read as text |
| 70 | 2026-10-11 | Pages (curl): NASA NSSDCA Mercury, Venus, Jupiter, Saturn fact sheets (updated 11 Jan 2024, 11 Jan 2024, 2 Oct 2024, 18 Mar 2025) | useful | Bulk, escape, irradiance, atmosphere composition |
| 71 | 2026-10-11 | `Mercury core radius mass fraction MESSENGER Hauck 2013 "outer solid shell" core 2020 km metallic` | useful (leads) | |
| 72 | 2026-10-11 | Page: escholarship.org copy of Hauck et al. 2013 | dead, died at the sources | HTTP 403 (CloudFront block) |
| 73 | 2026-10-11 | Page: arXiv 1701.05060, Wicht and Heyner, "Mercury's magnetic field in the MESSENGER era" (Jan 2017) | useful | Quotes Hauck 2013 and Rivoldini and Van Hoolst 2013 core radius and densities |
| 74 | 2026-10-11 | `Mahaffy Galileo probe 3He/4He ratio Jupiter atmosphere 1.66e-4 helium mass fraction Niemann 1998` | useful (leads) | Search summary's helium mole fraction 0.1359 and Y = 0.238 were NOT found in a page I opened; not used as findings (see Open threads) |
| 75 | 2026-10-11 | Page: Mahaffy et al., "Galileo Probe Measurements of D/H and 3He/4He in Jupiter's Atmosphere", Space Sci. Rev. 84:251 (1998), umich.edu copy | useful | 3He/4He = (1.66 +/- 0.05) x 10^-4 |
| 76 | 2026-10-11 | `solar wind helium abundance He/H percent slow wind fast wind 4% Ulysses ACE arXiv FIP fractionation factor low-FIP elements enrichment slow solar wind` | useful (leads) | Led to Pilleri et al. 2015 |
| 77 | 2026-10-11 | Page: arXiv 1508.04566, Pilleri et al., "Variations in solar wind fractionation as seen by ACE/SWICS over a solar cycle and the implications for Genesis Mission results" (2015) | useful | FIP bias 1.6 to 2.3; Genesis collection dates; He/H depletion in slow wind (qualitative). No He/H number given in the text read |
| 78 | 2026-10-11 | `Nittler 2011 MESSENGER X-ray spectrometer Mercury surface composition Fe weight percent Mg/Si Al/Si low iron` | thin | Abstract-level statements only (low Fe, high Mg/Si, low Al/Si); no number opened. Smithsonian repository page returned metadata, no PDF. Died at the sources for numbers |
| 79 | 2026-10-11 | `concept study collecting solar wind ions in space magnetic collector "solar wind" harvesting "in-space" resource propellant collection rate area kilograms` (extended) | useful (one lead) | Led to the NIAC plasma-magnet report; also a Research Square preprint on solar antimatter harvesting (rejected, see section 9) |
| 80 | 2026-10-11 | Page: NIAC Phase I Final Report, J. Slough (Univ. of Washington), "The Plasma Magnet", niac.usra.edu/files/studies/final_report/860Slough.pdf | useful | Magnetic bubble over 30 km; antenna and driver under 10 kg; MagSail comparison (about 30 km radius, a few tonnes). The copy read carries no date |
| 81 | 2026-10-11 | `Cedillos-Barraza 2016 Scientific Reports hafnium carbide tantalum carbide melting point measurement highest melting point K tungsten 3695 K` | useful (lead) | The tungsten figure in my query was not confirmed by any page opened and is not used |
| 82 | 2026-10-11 | Page: nature.com/articles/srep37962 (WebFetch) | dead, died at the sources | Redirected to a login service |
| 83 | 2026-10-11 | Europe PMC REST record for DOI 10.1038/srep37962 (PMC5131352) | useful | Abstract: TaC-HfC melt at 4041 to 4232 K; HfC0.98 (4232 +/- 84) K the highest recorded compound |
| 84 | 2026-10-11 | `total mass of near-Earth asteroid population estimate kg Granvik 2018 delta-v accessible fraction lower than Moon NHATS` | thin | No total NEA mass found in any source; NHATS counts only in summaries. Died at the sources for a mass figure |
| 85 | 2026-10-11 | Page: arXiv 1304.5082, Garcia Yarnoz, Sanchez, McInnes, "Easily Retrievable Objects among the NEO Population", Celest. Mech. Dyn. Astr. 116:367 (2013) | useful | 12 objects retrievable with under 500 m/s |
| 86 | 2026-10-11 | `Kasper 2007 "Solar wind helium abundance as a function of speed and heliographic latitude" arXiv A_He` (going back to row 32, logged as thin) | useful (leads) | Same CfA PDF as row 33; led to Alterman and Kasper 2019 on arXiv |
| 87 | 2026-10-11 | Page: arXiv 1906.12273, Alterman and Kasper, "Helium Variation Across Two Solar Cycles Reveals A Speed-Dependent Phase Lag" (Jun 2019) | useful | A_He about 4%, stable 4-5% in fast wind, photospheric about 8.5% |
| 88 | 2026-10-11 | Grep (read-only) of the two permitted sibling files for helium, He-3, belt mass, escape and lunar metals | useful | Belt mass, M-type share, lunar Fe and solar-wind volatiles taken from them as cross-references (3F) |

## 3. Findings

Evidence levels used in every table: **DEMONSTRATED** (flown or built), **ENGINEERING-STUDIED** (a quantitative design
study), **SPECULATIVE** (a thought experiment or concept paper). Source keys:

- **[SK23]** Scoggins, M. T. and Kipping, D., "Lazarus Stars: Numerical investigations of stellar evolution with star-lifting as a life extension strategy", MNRAS 523:3251 (2023); arXiv 2210.02338v2, 8 Jun 2023, https://arxiv.org/pdf/2210.02338. Peer-reviewed.
- **[HA26]** Harry, G., "Retaining Earth's Habitability Beyond the Life of the Sun", JBIS 79:230-243 (July 2026), DOI 10.59332/jbis-079-07-0230; arXiv 2607.13084. Peer-reviewed society journal; a concept paper.
- **[CA10]** Carrigan, R. A., "Starry Messages: Searching for Signatures of Interstellar Archaeology", arXiv 1001.5455 (Jan 2010; JBIS 63, 2010). Peer-reviewed society journal.
- **[A21]** Asplund, M., Amarsi, A. M., Grevesse, N., "The chemical make-up of the Sun: A 2020 vision", A&A 653, A141 (2021); arXiv 2105.01661v2. Peer-reviewed.
- **[A09]** Asplund, M., Grevesse, N., Sauval, A. J., Scott, P., "The chemical composition of the Sun", ARA&A 47:481 (2009); arXiv 0909.0948. Peer-reviewed.
- **[CIAAW]** IUPAC Commission on Isotopic Abundances and Atomic Weights, Abridged Standard Atomic Weights (2024), https://www.ciaaw.org/abridged-atomic-weights.htm. Primary.
- **[NSSDC]** NASA NSSDCA, Sun Fact Sheet (D. R. Williams), last updated 9 May 2024, https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html. Primary.
- **[MI19]** Mishra, W. et al., "Mass Loss via Solar Wind and Coronal Mass Ejections During Solar Cycle 23 and 24", MNRAS (accepted 8 Apr 2019); arXiv 1904.09898. Peer-reviewed.
- **[CR17]** Cranmer, S. R., "Mass Loss Rates from Coronal Mass Ejections: A Predictive Theoretical Model for Solar-Type Stars", ApJ 840 (2017); arXiv 1704.06689. Peer-reviewed.
- **[VE19]** Verscharen, D., Klein, K. G., Maruca, B. A., "The multi-scale nature of the solar wind", Living Rev. Sol. Phys. 16:5 (2019); arXiv 1902.03448. Peer-reviewed review.
- **[LC20]** Larrodera, C. and Cid, C., "Bimodal distribution of the solar wind at 1 AU", A&A 635, A44 (2020); arXiv 2003.09172v2. Peer-reviewed; ACE data.
- **[HU19]** Huss, G. R. et al., "Hydrogen fluence in Genesis collectors: Implications for acceleration of solar wind and for solar metallicity", Meteoritics & Planetary Science (19 Dec 2019), https://pmc.ncbi.nlm.nih.gov/articles/PMC7120949. Peer-reviewed.
- **[BU09]** Burkett, P. J. et al., "Genesis Solar Wind Array Collector Cataloging Status", LPSC 40 (2009) abstract 1373, https://www.lpi.usra.edu/meetings/lpsc2009/pdf/1373.pdf. Conference abstract (NASA JSC curation staff); primary for a curation figure.
- **[GPK]** NASA/JPL, Genesis Launch press kit (July 2001), https://www.jpl.nasa.gov/news/press_kits/genesislaunch.pdf. Agency; primary for mission facts, popular in tone.
- **[PPK]** NASA, Parker Solar Probe launch press kit (Aug 2018), https://www.nasa.gov/wp-content/uploads/2018/02/parkersolarprobe_presskit_august2018_final.pdf. Agency.
- **[PMP]** NASA, Parker Solar Probe mission page, https://science.nasa.gov/mission/parker-solar-probe/ (read 2026-10-11). Agency.
- **[SVS]** NASA SVS 5428, https://svs.gsfc.nasa.gov/5428 (read 2026-10-11). Agency.
- **[WHPI]** HAO/NCAR WHPI campaign page, PSP perihelion 22, https://whpi.hao.ucar.edu/whpi_campaign-psp22p.php. Research institution.
- **[STDT08]** NASA/TM-2008-214161, "Solar Probe Plus: Report of the Science and Technology Definition Team", July 2008, https://ntrs.nasa.gov/api/citations/20080032529/downloads/20080032529.pdf. Agency technical report; ENGINEERING-STUDIED.
- **[ESA19]** ESA, "Preparing for extreme environments" (Solar Orbiter), 7 Oct 2019, https://www.esa.int/Science_Exploration/Space_Science/Solar_Orbiter/Preparing_for_extreme_environments. Agency.

### 3A. What "starlifting" means in the literature

**Plain statement.** Every starlifting treatment found is SPECULATIVE. No paper found gives an engineering design with
masses, materials and power hardware for removing material from the Sun. The two peer-reviewed numerical papers
([SK23], [HA26]) explicitly set the engineering aside and model only the *rate* a star would need to lose mass to stay
at constant brightness. The original proposer (Criswell 1985) and the main book (Beech 2008) could not be opened (rows
7, 8, 11); what they say is known here only through [SK23], [HA26] and [CA10], which cite them.

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Origin of the term and idea | "first proposed by Criswell" in 1985; "further developed by Beech (2008)"; "a simple SL analysis was explored for a Sun-like star by Matloff (2017)" | [SK23] §1 | Primary (peer-reviewed) | [HA26] §2.1 ("first popularised by David Criswell"); [CA10] p.14 (Beech) | High (attribution); the original texts were not read |
| Purpose in the literature | Life-extension of a star: remove mass so core pressure and fusion rate fall, holding the planet's irradiance constant. Not material supply | [SK23] abstract; [HA26] §2.1 | Primary | [CA10] p.14 | High |
| Mechanism 1: beamed heating of a spot on the photosphere | "a Dyson swarm... captures a portion of the Sun's power output and directs it onto a small region of the solar surface. Photospheric particles would gain kinetic energy until they move faster than the Sun's gravitational escape velocity" | [HA26] §2.1 | Primary (concept paper) | [SK23] §1: Matloff assumes "a laser which increases the star's mass ejection via stellar winds" | Medium: described, never designed. SPECULATIVE |
| Mechanism 2: "space elevator technology" | "would require as-yet uninvented materials" | [HA26] §2.1 | Primary (concept paper) | none found | High that it is unbuildable with known materials. SPECULATIVE |
| Mechanisms in Beech 2008 (as reported) | "black hole pumps, ramjets and super-sized accelerators"; also core-envelope mixing, induced mass loss, changing rotation, adding heavy elements to raise opacity | [CA10] p.14-15 | Primary (reports a book) | none (book unopened) | Medium. SPECULATIVE |
| Criswell's magnetic "ring current" and "huff-n-puff" designs | No primary description online; only Wikipedia, mirrors and fiction sites | rows 10, 12 | Secondary only | none | **Not used.** Logged as an open thread |
| Carrigan's judgment | "Many, probably most astronomers view stellar engineering as an impossible task"; "one of these engineering processes must proceed on a heroic and post twenty-first century scale if it is to happen at all" | [CA10] p.14-15 | Primary | none | High (as a stated expert view) |
| Rate to hold a Sun-like star's output constant | about 0.03 M_Ceres per yr (isoirradiance) to about 0.05 M_Ceres per yr (isoluminosity, initial); stated as Mdot ≈ 5 x 10^19 kg/yr | [SK23] abstract, §3.1, §4.1 | Primary (MESA modeling) | [HA26] §2.1 uses 5 x 10^19 kg/yr in its own MESA run | High (as a model output) |
| Life gained by that rate | Sun's main sequence extended from about 9 Gyr to about 11 Gyr (isoirradiance) or 12 Gyr (isoluminosity) | [SK23] §3.1, Fig. 1 | Primary | [HA26] Table 2: MS end delayed 4.7 to 5.1 Gyr after present; Earth's habitable-zone exit moved from 1.7 to 9.2 Gyr after present | High as a model output |
| Total mass removed in [HA26]'s run | "0.13 M_sun over 5.1 Gyr, or 1.3 x 10^29 kg" | [HA26] §2.1 | Primary | Arithmetic check: 5e19 kg/yr x 5.1e9 yr = 2.55e29 kg = 0.128 M_sun. **The kg figure is wrong by a factor of 2**; see Conflicts | High that 0.13 M_sun (2.6e29 kg) is the consistent value |
| Beech's luminosity scaling | L proportional to M^5 (Kramers opacity), so dL/L = 5 dM/M; "roughly 60% of the solar material would have to be dispersed to keep the luminosity constant to the end of the main sequence" | [CA10] p.15 | Primary (reports Beech) | [SK23]'s MESA runs need far less (0.13 M_sun in [HA26]); see Conflicts | Medium |
| Matloff 2017 scenarios (as reported) | laser-enhanced stellar wind; "the most conservative approach resulting in about a 3 percent mass loss over a 600 Myr period" | [SK23] §1 | Primary (reports a paywalled paper) | none (Matloff body paywalled, rows 5-6) | Medium |
| Minimum power, ideal (lift to infinity) | Edot ≈ G M Mdot / R (Eq. 2); for 5e19 kg/yr, "Edot ≈ 10^38 erg/yr, or about 10^-4 L_sun... a lower bound... perfect efficiency" | [SK23] §4.1 Eq. 2 | Primary | Recomputed in Derived D1: 3.0e23 W = **7.9 x 10^-4 L_sun**, i.e. nearer 10^-3 than 10^-4 | High for the formula; the paper's rounding of the ratio is loose |
| Energy per kg in Matloff 2017 (as reported) | 1.9 x 10^20 erg/kg (= 1.9 x 10^13 J/kg); gives about 10^40 erg/yr, "about 0.01 L_sun" | [SK23] §4.1 | Primary (reports Matloff) | Ideal G M/R is 1.9 x 10^11 J/kg (Derived D1), so Matloff's figure is about 100 times the ideal, consistent with an inefficient process; recomputed fraction is 0.079 L_sun, not 0.01 (Derived D1) | Medium |
| Total energy, life-extension case | "on the order of 10^47 erg, at least" | [SK23] §4.1 | Primary | none | Medium (order of magnitude) |
| Gravitational escape energy listed for the Sun | 20,000 MJ/kg | [HA26] Table 1 | Primary | NSSDC escape speed 617.6 km/s gives 0.5 v^2 = 190,700 MJ/kg. **[HA26]'s Sun entry is about 10 times too low**; its Mercury (9), Venus (54) and Jupiter (1800) MJ/kg entries do check | High that 1.9 x 10^5 MJ/kg is right |
| Stellar engines (Caplan 2019; Svoronos 2020, 2021) | Engines that use collected solar wind and Dyson-sphere power to make a jet; abstracts only, bodies paywalled (rows 16-18) | Crossref/Semantic Scholar abstracts | Primary (abstract only) | none | Low for any number; none used |

### 3B. Solar composition and how much Sun must be processed per tonne of each element

Photospheric abundances are given as log eps(X) = log10(N_X / N_H) + 12. Mass fraction = X_H x 10^(log eps - 12) x
(A_X / A_H), with X_H the hydrogen mass fraction from the same compilation and atomic weights from [CIAAW]. Method
check: helium computes to 0.2423, equal to [A21]'s stated Y. The solar *photosphere* is used because it is what lies
on top; the bulk (proto-solar) values differ slightly because heavy elements have settled inward over 4.6 Gyr.

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Photospheric mass fractions, present day | X (H) = 0.7438 +/- 0.0054, Y (He) = 0.2423, Z (all heavier) = 0.0139; Z/X = 0.0187 | [A21] §5, Table 4 | Primary | [A09]: X = 0.7381, Y = 0.2485, Z = 0.0134 | High |
| Proto-solar (bulk, initial) mass fractions | X = 0.7121, Y = 0.2725, Z = 0.0154 | [A21] Table 4 | Primary | [A09]: 0.7154, 0.2703, 0.0142 | High |
| Photosphere composition by number | H 90.965%, He 8.889%; O 774 ppm, C 330, Ne 112, N 102, Fe 43, Mg 35, Si 32, S 15 ppm | [NSSDC] | Primary | Consistent with [A09]/[A21] log eps converted to number fractions | High |
| log eps used (A21 / A09) | C 8.46/8.43; N 7.83/7.83; O 8.69/8.69; Mg 7.55/7.60; Al 6.43/6.45; Si 7.51/7.51; P 5.41/5.41; Ti 4.97/4.95; Fe 7.46/7.50; Ni 6.20/6.22; Cu 4.18/4.19; He 10.914/10.93 | [A21] Table 2; [A09] Table 1 | Primary | each value against the other compilation | High |
| Atomic weights used | H 1.0080, He 4.0026, C 12.011, N 14.007, O 15.999, Mg 24.305, Al 26.982, Si 28.085, P 30.974, Ti 47.867, Fe 55.845, Ni 58.693, Cu 63.546 | [CIAAW] | Primary | none needed | High |

**Mass fraction of each element in the photosphere, and tonnes of solar material per tonne of element** (Derived D2; A21
first, A09 in brackets):

| Element | Mass fraction (ppm) | t of solar material per t of element | Confidence |
|---|---|---|---|
| He | 242,300 (249,500) | 4 (4) | High |
| O | 5,782 (5,738) | 173 (174) | High |
| C | 2,556 (2,367) | 391 (422) | High |
| Fe | 1,188 (1,293) | 841 (773) | High |
| N | 699 (693) | 1,431 (1,442) | High |
| Si | 671 (665) | 1,491 (1,503) | High |
| Mg | 636 (709) | 1,571 (1,411) | High |
| Ni | 68.6 (71.3) | 14,600 (14,000) | High |
| Al | 53.6 (55.7) | 18,700 (18,000) | High |
| P | 5.87 (5.83) | 170,000 (172,000) | High |
| Ti | 3.30 (3.12) | 303,000 (320,000) | High |
| Cu | 0.71 (0.72) | 1,409,000 (1,388,000) | High |
| Fe + Ni + Mg + Al + Ti + Cu together | 1,951 (2,133) | **513 (469)** | High |
| All of the eleven listed builder elements (C, N, O, Mg, Al, Si, P, Ti, Fe, Ni, Cu) | 11,665 (11,602) | 86 (86) | High |

**The issue stated plainly:** about 98.6% of the Sun's surface material by mass is hydrogen and helium. Structural
metals (Fe, Ni, Mg, Al, Ti, Cu) are about 0.2% by mass: roughly **500 tonnes of solar material must be lifted and
separated for each tonne of structural metal**, and about 840 t per tonne of iron alone. Titanium needs about
300,000 t per tonne; copper about 1.4 million t per tonne. Everything heavier than helium together (Z) is 1.39%.
(The A09 helium value computes to 0.2495 against that paper's stated 0.2485 because its He log eps is a bracketed
helioseismic value; the difference does not affect the metals.)

### 3C. Energy and mass-flow scales: lifting, and the natural solar wind

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Solar mass | 1.9884 x 10^30 kg | [NSSDC] | Primary | none needed | High |
| GM | 1.32712 x 10^20 m^3/s^2 | [NSSDC] | Primary | none needed | High |
| Volumetric mean radius | 695,700 km | [NSSDC] | Primary | none needed | High |
| Escape speed at the surface | 617.6 km/s | [NSSDC] | Primary | sqrt(2GM/R) = 617.7 km/s from the same sheet | High |
| Specific energy to escape from the photosphere | **1.91 x 10^11 J/kg** (190,700 MJ/kg) | Derived D1 from [NSSDC] | Derived | [SK23] Eq. 2 uses the same G M/R | High |
| Luminosity | 3.828 x 10^26 W | [NSSDC] | Primary | none needed | High |
| Mass converted to energy by fusion | 4.26 x 10^9 kg/s | [NSSDC] | Primary | none needed | High |
| Surface gravity | 274.0 m/s^2 | [NSSDC] | Primary | none needed | High |
| Upper bound on lift rate if the *entire* luminosity did nothing but lift, at 100% efficiency | 2.0 x 10^15 kg/s (6.3 x 10^22 kg/yr) | Derived D1 | Derived | none | High as a bound |
| Solar wind mass-loss rate | average 2.1 x 10^-14 M_sun/yr for cycle 23, about 10% lower in cycle 24; "does not change even by a factor of 2" over the cycle | [MI19] §4.2 | Primary | [CR17] Eq. 1: 3.5 x 10^-17 (S + 570) M_sun/yr, i.e. 2.0 x 10^-14 at sunspot number 0 and 2.5 x 10^-14 at S = 150; "roughly 50% larger at solar maximum" | High |
| Same in kg/s | **1.3 x 10^9 kg/s** (4.2 x 10^16 kg/yr) | Derived D3 | Derived | [PPK] PDF p.21: "a million tons of matter into space every second"; [HA26] Table 1: 3 x 10^16 kg/yr | High |
| CME share of mass loss | about an order of magnitude below the wind ([MI19] abstract; [CR17] abstract); about 5% of the wind near the ecliptic and about 1% at 80 degrees latitude at cycle maximum ([MI19] §3) | [MI19], [CR17] | Primary | [CR17] §2: raw CDAW gives about 3% at maximum; older studies 10-15% | High (order); medium (exact share) |
| Total catalogued CME mass, 6,379 CMEs, Mar 1996 to Jun 2013 | 1.051 x 10^19 g (1.05 x 10^16 kg) without marginal events; 1.248 x 10^19 g with them | [CR17] §2 | Primary | [CR17] multiplies by 1.5 for undercounting | Medium (catalog undercount acknowledged) |
| CME mass loss, fit | 5.6 x 10^-18 (S + 7) M_sun/yr ([CR17] Eq. 2); 3 x 10^-18 (2.8 S + 91) M_sun/yr for cycle 23 ([MI19] §4.1) | [CR17], [MI19] | Primary | each other | Medium |
| Solar wind at 1 au, slow component | 370 +/- 60 km/s; 5 +/- 3 protons/cm^3; B 4 +/- 1 nT; T_p 0.4 x 10^5 K | [LC20] Table 3 (ACE, whole data set) | Primary | [LC20] Table 1: Hansteen 2010, 430 +/- 100 km/s and about 10 /cm^3 | High |
| Solar wind at 1 au, fast component | 500 +/- 100 km/s; 3 +/- 2 /cm^3; B 6 +/- 2 nT; T_p 0.9 x 10^5 K | [LC20] Table 3 | Primary | [LC20] Table 1: Hansteen 2010, 700-900 km/s and about 3 /cm^3 (definitions of "fast" differ; see Conflicts) | High |
| Typical 1 au values, general | n_p 3 /cm^3; T 10^5 K; B 3 x 10^-5 G (3 nT); speed 300-800 km/s; expansion time about 2.4 days | [VE19] Table 1, §1.1 | Primary (review) | [LC20] | High |
| Upper corona (about 100 Mm above the photosphere) | n 10^6 /cm^3; T 10^6 K; B about 1 G | [VE19] Table 1 | Primary | none | High (order of magnitude) |
| Solar wind proton mass flux at 1 au (slow wind, 5 /cm^3, 370 km/s) | 3.1 x 10^-15 kg m^-2 s^-1 | Derived D3 from [LC20] | Derived | Genesis-measured average H flux 2.2 x 10^8 /cm^2/s gives 3.7 x 10^-15 kg m^-2 s^-1 ([HU19], Derived D4) | High |
| Collector area needed to intercept 1 kg/s of solar wind | 3.2 x 10^14 m^2 at 1 au (about 0.6 of Earth's surface area); 3.2 x 10^12 m^2 at 0.1 au; 7 x 10^11 m^2 at 0.0465 au | Derived D3 | Derived | flux scales as 1/r^2 by mass conservation ([CR17] Eq. 4, Mdot = 4 pi rho u r^2) | High (geometry); medium (assumes slow-wind flux everywhere) |
| Collector area needed to intercept 1 tonne per year of solar wind | about 10,000 km^2 at 1 au; 920 km^2 at 0.3 au; 100 km^2 at 0.1 au; 22 km^2 at 0.0465 au (Parker's perihelion) | Derived D3 | Derived | as above | High (geometry) |
| Fraction of the whole solar wind a collector of area A at distance r intercepts | A / (4 pi r^2); e.g. a 1 km^2 collector at 1 au takes 3.6 x 10^-18 of the wind (about 0.1 to 0.15 kg per year) | Derived D3 | Derived | as above | High |
| Starlifting rate vs. natural wind | [SK23]'s life-extension rate (5e19 kg/yr) is about **1,200 times** the natural solar wind | Derived D1 | Derived | none | High |

**Note on solar wind composition.** The solar wind is not a perfect sample of the photosphere: elements are
fractionated by first-ionization potential (a fact noted in [HU19]'s title, "implications... for solar metallicity",
but the per-element factors were not read this session; see Open threads). Iron and other metals in the wind may differ
from the photosphere by a factor of order unity (fFIP 1.6 to 2.3, [PI15], see 3E).

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Solar wind helium abundance by number | protons "about 95% of the solar wind ions" and alpha particles "about 4%"; A_He = 100 n_alpha/n_p "takes on a stable value between 4% and 5%" above about 426 km/s, falls in slow wind, and "rarely exceeds 5%" | Alterman, B. L. and Kasper, J. C., "Helium Variation Across Two Solar Cycles Reveals A Speed-Dependent Phase Lag", arXiv 1906.12273 (Jun 2019; ApJL), §1, §7 | Primary (peer-reviewed) | [PI15] §3: slow-wind He/H "greatly depleted" at the cycle 23 minimum (qualitative) | High |
| Photospheric helium abundance by number, for comparison | about 8.5% (citing Asplund 2009) | Alterman and Kasper 2019, §7 | Primary | [NSSDC]: He/H = 8.889/90.965 = 9.8% by number of all particles counted there; [A21] log eps 10.914 gives 8.2% | Medium (definitions differ slightly) |

### 3D. Near-Sun engineering actually done (the lower bound on survivable hardware)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Parker Solar Probe closest approach (perihelion 22) | 11:41 UT 24 Dec 2024; about 0.046 au; 9.86 solar radii (heliocentric) | [WHPI] | Primary | [SVS]: "3.86 million miles from the solar surface"; [PMP]: "about 3.9 million miles (6.2 million kilometers) of the Sun"; Derived: 9.86 R_sun = 6.86 million km from center, 6.16 million km above the surface | High. DEMONSTRATED |
| Parker speed at closest approach | about 430,000 mph (700,000 km/h, about 190 km/s) | [PMP]; [PPK] | Primary (agency) | each other | High. DEMONSTRATED |
| Parker heat shield (TPS) | carbon-composite foam between two carbon plates, white ceramic paint on the sunward face; 4.5 in (11.43 cm, "about 115 mm") thick; 73 kg | [PPK] PDF pp.10, 30 | Primary (agency) | [PMP] same thickness | High. DEMONSTRATED |
| TPS diameter | "about 7.5 feet (2.3 meters)" ([PPK] PDF p.10) and "8 feet (2.4 meters)" ([PPK] PDF p.30) | [PPK] | Primary | The same press kit gives both; see Conflicts | Medium |
| TPS front-face temperature at perihelion | "nearly 2,500 degrees Fahrenheit (1,377 Celsius)" ([PMP]); "about 1,400 degrees Celsius" ([PPK] PDF p.30) | [PMP], [PPK] | Primary | each other | High. DEMONSTRATED |
| TPS test temperature | 3,000 F (1,650 C) | [PPK] PDF p.30 | Primary | none | High |
| Spacecraft interior behind the shield | about 85 F (30 C) | [PPK] PDF pp.11, 30 | Primary | none | High |
| Parker mass | 635 kg after fueling ([PPK]); 685 kg at launch ([PMP]) | [PPK], [PMP] | Primary | Disagree; see Conflicts | Medium |
| Parker power | solar arrays 1.6 m^2 total, 388 W | [PPK] PDF p.10 | Primary | none | High. DEMONSTRATED |
| Parker array cooling | about 3.7 L of pressurized deionized water, 10 to 125 C; two radiators; pumps | [PPK] PDF p.32 | Primary | [STDT08] §4.4: "moveable, liquid-cooled base plates"; secondary arrays partly retracted behind the shield inside 0.25 au | High. DEMONSTRATED |
| Autonomy | Light takes about 8 minutes to Earth; the craft keeps itself in the shield's shadow with Sun sensors and no human intervention | [PPK] PDF p.32 | Primary | none | High. DEMONSTRATED |
| Launch energy | "55 times that required to get to Mars" | [PPK] PDF p.28 | Primary | none | Medium (popular phrasing of C3) |
| Design solar flux at 9.5 R_sun | 70 W/cm^2 (about 510 Suns), versus 400 W/cm^2 at 4 R_sun for the cancelled 2005 design | [STDT08] §4.6, Table 4-11 | Primary. ENGINEERING-STUDIED | Derived: L / (4 pi r^2) at 9.5 R_sun = 69.7 W/cm^2; at 9.86 R_sun = 64.7 W/cm^2 | High |
| Design shield temperature and heat leak | about 1,700 K at about 4 MW total incident power; heat into the spacecraft under 50 W ("0.001% of the original flux"); shield back face 350 C target | [STDT08] §4.6 | Primary. ENGINEERING-STUDIED | [PPK]: about 1,400 C flown | High |
| Allowed shield mass loss | 2.5 mg/s | [STDT08] Table 4-11 | Primary. ENGINEERING-STUDIED | none | High (a requirement, not a measurement) |
| Shield mass and size in the 2008 design | 70.5 kg; 2.72 m diameter; 15 cm carbon foam | [STDT08] Table 4-11 | Primary | [PPK]: 73 kg flown, 11.43 cm | High |
| Spacecraft bus temperature limits | 20 to 40 C; radiator at least 0.64 m^2 for the hot case | [STDT08] §4.7 | Primary | none | High |
| Refractory parts in sunlight | plasma-wave antennas must be refractory "that will operate at temperatures up to 1500 C" | [STDT08] §3.2 | Primary | none | High |
| Dust near the Sun | submicron to several hundred microns, refractory carbon and silicate, density about 2.5 g/cm^3 (the report prints "g/cm2", a typo), relative speeds "as high as 350 km/s"; 90% of the dust in the ecliptic | [STDT08] §4.3.5, §1 | Primary | none | Medium |
| Ionizing radiation requirement | 44 krad (Si) over 7 years | [STDT08] Table 4-11 | Primary | none | High (requirement) |
| Solar Orbiter closest approach | about 42 million km ("just over a quarter of the distance" to Earth) | [ESA19] | Primary (agency) | none | High. DEMONSTRATED |
| Solar Orbiter heating and shield | 13 times the heating in Earth orbit; 20 titanium layers to 500 C; 30 lower-temperature layers to 300 C; spacecraft 1.8 t | [ESA19] | Primary | 1/0.28^2 = 12.8, consistent | High. DEMONSTRATED |
| Solar irradiance at 1 au | 1,361 W/m^2 | Derived from [NSSDC] L | Derived | none | High |

**What this sets as a lower bound.** The closest anything has survived is about 9.9 solar radii from the Sun's center
(about 8.9 radii above the surface), for hours per pass, behind a 73 kg shield at about 1,400 C that admits under 50 W
to a sub-tonne craft drawing 388 W. Nothing built has stayed near the Sun continuously, and nothing has gathered
material there. The photosphere, where starlifting would act, is about 9 solar radii deeper still, at about 6.3 x 10^7
W/m^2 surface emission ([NSSDC]), about 100 times the flux on Parker's shield.

Additional source keys for 3D to 3G:

- **[SR16]** Cedillos-Barraza, O. et al., "Investigating the highest melting temperature materials: A laser melting study of the TaC-HfC system", Scientific Reports 6:37962 (Dec 2016), abstract via Europe PMC (PMC5131352). Peer-reviewed.
- **[PI15]** Pilleri, P. et al., "Variations in solar wind fractionation as seen by ACE/SWICS over a solar cycle and the implications for Genesis Mission results", arXiv 1508.04566 (Aug 2015). Peer-reviewed (ApJ).
- **[SL]** Slough, J., "The Plasma Magnet", NIAC Phase I Final Report, University of Washington, https://www.niac.usra.edu/files/studies/final_report/860Slough.pdf (no date on the copy read). Agency-funded concept study.
- **[AS13]** Armstrong, S. and Sandberg, A., "Eternity in six hours: intergalactic spreading of intelligent life and sharpening the Fermi paradox", Acta Astronautica 89:1-13 (2013); preprint read via the Internet Archive copy of fhi.ox.ac.uk/wp-content/uploads/intergalactic-spreading.pdf. Peer-reviewed; "exploratory engineering", i.e. SPECULATIVE.
- **[NSSDC-Me], [NSSDC-V], [NSSDC-J], [NSSDC-S]** NASA NSSDCA fact sheets for Mercury (updated 11 Jan 2024), Venus (11 Jan 2024), Jupiter (2 Oct 2024), Saturn (18 Mar 2025), https://nssdc.gsfc.nasa.gov/planetary/factsheet/. Primary.
- **[WH17]** Wicht, J. and Heyner, D., "Mercury's magnetic field in the MESSENGER era", arXiv 1701.05060 (Jan 2017). Peer-reviewed review; quotes Hauck et al. 2013 and Rivoldini and Van Hoolst 2013.
- **[MA98]** Mahaffy, P. R. et al., "Galileo Probe Measurements of D/H and 3He/4He in Jupiter's Atmosphere", Space Sci. Rev. 84:251-263 (1998). Peer-reviewed.
- **[PA15], [PA17], [PA20]** Palaszewski, B. (NASA Glenn), "Atmospheric Mining in the Outer Solar System": "Resource Capturing, Storage, and Utilization" (NTRS 20150006664); "Outer Planet Orbital Transfer and Lander Analyses" (NTRS 20170004746); "Aerospacecraft Analysis, Propulsion, and Resource Capturing Implications" (AIAA 2020, NTRS 20205004479). Agency concept studies; ENGINEERING-STUDIED at a conceptual level.
- **[GY13]** Garcia Yarnoz, D., Sanchez, J. P., McInnes, C. R., "Easily Retrievable Objects among the NEO Population", Celest. Mech. Dyn. Astr. 116:367-388 (2013); arXiv 1304.5082. Peer-reviewed.

| Quantity (3D continued) | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Highest measured melting point of any compound | HfC0.98: (4232 +/- 84) K; the TaC-HfC system melts at 4041 to 4232 K | [SR16] abstract | Primary | none opened | High |
| Equilibrium temperature of a sun-facing flat plate radiating from its front only (absorptance/emittance = 1) | 394 K at 1 au; 744 K at 0.28 au; 1,838 K at 9.86 R_sun; 2,898 K at 4 R_sun; 4,081 K at 2 R_sun; 5,772 K at the photosphere | Derived D5 | Derived | [STDT08]: shield about 1,700 K at 9.5 R_sun with absorptance/emittance under 0.6 (Derived gives 1,648 K for 0.6) | High (radiative balance) |
| Closest distance at which a passive sun-facing plate stays below HfC's melting point | about 1.9 R_sun from the Sun's center (absorptance/emittance = 1); about 1.4 R_sun (0.6) | Derived D5 | Derived | none | Medium: real structures also conduct heat and are not flat plates; active cooling could go deeper only by rejecting the heat somewhere |

### 3E. The minimum infrastructure to begin collecting solar material at any rate

**Plain statement.** Only one solar-material collection has ever flown: Genesis. It returned well under a milligram
in 2.3 years. No space-based collector for solar wind *as a resource* has been designed to any engineering level in a
source found here. Magnetic-sail and plasma-magnet studies show that a large magnetic cross-section can be very light,
but they *deflect* the wind for thrust; none found designs a magnetic structure that *captures and stores* ions.
Lifting material from the photosphere itself has no design at all (3A).

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Genesis: what it was | Solar-wind sample return; passive collector arrays (ultra-pure wafers) plus an electrostatic ion concentrator that focused O and N; at the Sun-Earth L1 point | [GPK] | Primary | [PI15] §1 | High. DEMONSTRATED |
| Genesis exposure | 853 days outside the magnetosphere ([HU19]); collected "for 2.3 years between November 30, 2001 and April 1, 2004" ([PI15] §1) | [HU19], [PI15] | Primary | [GPK]: L1 orbit Nov 2001 to Apr 2004 | High |
| Genesis collector area | 1,672,944 mm^2 (about 1.67 m^2) of collector material, excluding germanium collectors | [BU09] | Primary (curation) | none | High |
| Genesis bulk H fluence | (1.634 +/- 0.028) x 10^16 atoms/cm^2; regime arrays: interstream 0.624, coronal hole 0.551, CME 0.412 (each x 10^16) | [HU19] | Primary | none | High |
| Genesis total solar wind collected | **about 0.46 mg of hydrogen** (2.73 x 10^20 H atoms); helium and heavier ions add a fraction more | Derived D4 | Derived | [GPK] stated goal "10 to 20 micrograms" (a goal, apparently for the analyzable heavy species; see Conflicts); Wikipedia's "0.4 mg" (secondary, not used) | High for the H mass |
| Genesis collection rate | about 0.2 mg per year on 1.67 m^2 at 1 au | Derived D4 | Derived | consistent with the 1 au flux in 3C | High |
| Genesis spacecraft | 636 kg at launch (494 kg dry, 142 kg fuel); $164 million development and instruments, $45 million operations and analysis | [GPK] | Primary | none | High. DEMONSTRATED |
| Genesis outcome | Collector arrays "were fractured upon landing hard in Utah in 2004"; fragments recovered and catalogued | [BU09] | Primary | none | High |
| Plasma magnet (magnetic bubble) | Dipole field inflated to "well over the 30 km scale"; "antenna and driver need weigh no more than 10 kg"; 300 V supply; "virtually propellantless as the intercepted solar wind replenishes the small amount of plasma required" | [SL] Summary | Primary (agency concept study; small lab prototype built) | [SL] §intro: Zubrin-Andrews MagSail needs a superconducting loop of about 30 km radius, "a few metric tons", with current densities "well beyond that of current high temperature superconductors" | Medium. ENGINEERING-STUDIED (lab prototype only); it deflects, it does not collect |
| Solar wind passing through a 30 km-radius cross-section at 1 au | about 8.7 x 10^-6 kg/s, i.e. **about 0.28 tonnes per year**, of which the fraction that could be captured rather than deflected is unstudied | Derived D3 | Derived | none | Medium (flux) / unknown (capture) |
| Scaling of any wind collector | Mass flux scales as 1/r^2: a fixed collector at 0.1 au sees 100 times the 1 au flux; at Parker's 0.046 au about 470 times | Derived D3 | Derived | [CR17] Eq. 4 (mass conservation) | High |
| Metals in collected wind | 1 tonne of solar wind holds about 1.2 kg of iron at photospheric proportions (Derived D2); the solar wind is enriched in low-FIP elements (Fe, Mg, Si) relative to C, O, Ne by a factor fFIP = 1.6 to 2.3 depending on regime and solar-cycle phase | [PI15] §3 | Primary | [PI15]: very fast polar-coronal-hole wind "essentially unfractionated" (citing Gloeckler and Geiss 2007) | Medium (the absolute Fe/H enrichment was not read; see Open threads) |

**The smallest literature-supported answer, summarized.** Power: solar arrays, as on Genesis and Parker (hundreds of
watts). Collector: passive implantation targets (Genesis) at about 0.2 mg per year per 1.7 m^2 at 1 au; anything
larger is an extrapolation by area (about 10,000 km^2 at 1 au, or about 100 km^2 at 0.1 au, per tonne of wind per year,
holding about 1 to 3 kg of iron). Storage: implanted in solid collectors, returned by capsule (Genesis). Transport out:
a sample-return capsule. Control: autonomous, as Parker shows (8 minutes light time each way at 1 au). Nothing in the
literature supports any rate higher than these by design rather than by area scaling.

### 3F. Alternatives for the same raw materials (comparison only)

The Moon and the main asteroid belt are covered in the sibling files `moon_lagrange_and_comparables.md` and
`belt_jupiter_saturn_and_deep_transit.md`; the key figures are cross-referenced, not repeated.

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| **Mercury** mass; escape speed; GM | 0.33010 x 10^24 kg; 4.3 km/s; 0.022032 x 10^6 km^3/s^2 | [NSSDC-Me] | Primary | escape energy GM/R = 9.0 MJ/kg (Derived D6); [AS13]: "about nine mega-joules" per kg; [HA26] Table 1: 9 MJ/kg | High |
| Mercury solar irradiance; semimajor axis | 9,082.7 W/m^2 (6.67 times Earth's); 57.909 x 10^6 km | [NSSDC-Me] | Primary | none | High |
| Mercury atmosphere | surface pressure under about 5 x 10^-15 bar; total mass under about 10,000 kg | [NSSDC-Me] | Primary | none | High |
| Mercury internal structure | liquid-core radius 2,020 +/- 30 km (Hauck et al. 2013) or 2,004 +/- 39 km (Rivoldini and Van Hoolst 2013), leaving "only the outer 16 to 19% of the mean planetary radius" to the mantle; mantle density 3,380 +/- 200 kg/m^3; core density 6,980 +/- 280 kg/m^3 (Hauck) or 7,233 +/- 267 (Rivoldini) | [WH17] | Primary (review quoting primary) | Derived D6: core mass about 2.4 x 10^23 kg = **73% of Mercury's mass**; [AS13] (citing older work): "30% silicate and 70% metal" | High |
| Mercury surface composition | Volcanic surface rocks "have a low content of iron and other heavier elements" (Nittler et al. 2011, XRS) | [WH17] | Primary (review) | search summary of Nittler 2011 (not opened): high Mg/Si, low Al/Si and Ca/Si, high S | Medium (no weight-percent number opened) |
| Mercury disassembly concept | Seed 1 km^2 of panels on Mercury; captor efficiency 1/3; 1/10 of power to mass drivers; 5-year processing lag; half of the mass usable; result: Mercury "completely disassembled in 31 years and 85 days, with most of the mass loss happening in the last 4 years"; binding energy 1.80 x 10^30 J; swarm at Mercury's orbit would need 3.92 kg/m^2, "0.5 mm" of iron | [AS13] §4.1-4.2 | Primary (peer-reviewed; exploratory engineering) | Binding energy recomputed: 3GM^2/(5R) = 1.79 x 10^30 J (Derived D6); [HA26] §2.1 cites the same 0.5 mm foil | Low as engineering (SPECULATIVE; the authors say "it would cost a lot and would be unlikely to be attempted"); high for the arithmetic |
| **Venus** atmosphere | total mass about 4.8 x 10^20 kg; 92 bar surface; 96.5% CO2, 3.5% N2 by volume; SO2 150 ppm, Ar 70, H2O 20, CO 17, He 12, Ne 7 ppm | [NSSDC-V] | Primary | none | High |
| Venus escape speed; irradiance | 10.36 km/s (escape energy 53.7 MJ/kg); 2,601.3 W/m^2 | [NSSDC-V] | Primary | [HA26] Table 1: 54 MJ/kg | High |
| Carbon and nitrogen in Venus's atmosphere | about 1.3 x 10^20 kg of carbon (as CO2) and about 1.1 x 10^19 kg of N2 | Derived D6 | Derived | none | High (arithmetic from the fact sheet) |
| **Jupiter** atmosphere | H2 89.8% (+/- 2.0), He 10.2% (+/- 2.0) by volume; CH4 3000 ppm, NH3 260, HD 28; escape speed 59.5 km/s; mass 1,898.13 x 10^24 kg; irradiance 50.26 W/m^2 | [NSSDC-J] | Primary | escape energy 1,770 MJ/kg (Derived); [HA26] Table 1: 1,800 | High |
| Jupiter 3He/4He | (1.66 +/- 0.05) x 10^-4 (Galileo probe mass spectrometer) | [MA98] abstract | Primary | meteoritic (1.5 +/- 0.3) x 10^-4 ([MA98]) | High |
| He-3 mass fraction of Jupiter's atmosphere | about 2.3 x 10^-5 (from fact-sheet volume fractions); about 43 tonnes of atmosphere per kg of He-3 | Derived D6 | Derived | none | Medium (fact-sheet He fraction; see Open threads for the Galileo Y) |
| **Saturn** atmosphere | H2 96.3% (+/- 2.4), He 3.25% (+/- 2.4) by volume; escape speed 35.5 km/s; mass 568.32 x 10^24 kg; irradiance 14.82 W/m^2 | [NSSDC-S] | Primary | escape energy 630 MJ/kg (Derived); [HA26] Table 1: 650 | High (composition: large uncertainty, as stated) |
| He-3 mass fraction of Saturn's atmosphere | about 7.9 x 10^-6 if Saturn's 3He/4He equals Jupiter's (an assumption) | Derived D6 | Derived | none | Low |
| Gas-giant atmospheric-mining studies | NASA studies size mining for **Uranus and Neptune**, not Jupiter or Saturn: Uranus and Neptune "offer vast reservoirs of fuels that are more readily accessible than those from Jupiter and Saturn"; at a He-3 fraction of 1.52 x 10^-5 (a Uranus case), capturing 500 kg of He-3 takes 95.2 days at 4 kg/s of atmosphere processed (with 293,000 kg/day of hydrogen produced) or 38.1 days at 10 kg/s; aerospacecraft dry mass 100,000 kg; total delta-v capability 20.1 to 20.5 km/s to reach an 800 km orbit | [PA15] §II-III; [PA17]; [PA20] | Primary (agency concept studies) | Mining times recomputed: 500 / (4 x 1.52e-5) s = 95.2 days (Derived D6) | Medium. ENGINEERING-STUDIED (conceptual vehicle sizing) |
| **Main asteroid belt** | total mass about 2 to 3 x 10^21 kg; M-types about 3.3% of belt mass; Psyche 30-60% metal by volume | sibling `belt_jupiter_saturn_and_deep_transit.md` §3A | (sibling's sources) | the sibling lists four independent estimates | High (per sibling) |
| **Near-Earth asteroids** | 12 known objects retrievable to the Sun-Earth L1/L2 region with under 500 m/s of delta-v (as of 2013) | [GY13] abstract | Primary | none | High for the count at that date; no total NEA mass found (Open threads) |
| **Moon** | escape 2.38 km/s, 2.83 MJ/kg; mare Fe 14-17 wt% mostly in silicates and ilmenite; native Fe about 0.5 wt%; solar-wind-implanted H about 46 ppm, He-4 about 14 ppm, He-3 about 4 ppb (top 2-3 m) | sibling `moon_lagrange_and_comparables.md` §3 A5-A6 | (sibling's sources) | sibling | Medium-high (per sibling). Note: lunar regolith is a natural, 4-billion-year solar-wind collector |

### 3G. Could harvesting from the Sun compete with the alternatives? The numbers that decide it

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Ideal energy to lift one tonne of *iron* out of the Sun (lifting 841 t of photosphere) | **1.6 x 10^17 J** (separation energy not included) | Derived D7 | Derived | none | High as a lower bound |
| Ideal energy to lift one tonne of iron-rich material off Mercury | about 1.3 x 10^10 J (9.0 MJ/kg on material 70% metal) | Derived D7 | Derived | [AS13] | High as a lower bound |
| Ratio, Sun to Mercury, per tonne of iron | **about 10^7** (12 million) | Derived D7 | Derived | none | High (order of magnitude) |
| Same per tonne of carbon: Sun vs Venus's atmosphere | Sun 7.5 x 10^16 J (391 t lifted); Venus 2.0 x 10^11 J (3.75 t of CO2 at 53.7 MJ/kg, the atmosphere being 26.7% carbon by mass), about 4 x 10^5 times less | Derived D7 | Derived | none | High (order of magnitude) |
| What the Sun has that the alternatives lack | Mass: 2 x 10^30 kg, about 8 x 10^8 times the main belt and 6 x 10^6 times Mercury; even its 1.4% of heavy elements (about 2.8 x 10^28 kg) is about 84,000 times Mercury's whole mass | [NSSDC], [A21], sibling | Derived | [HA26] Table 1 presents the Sun as the largest "metallicity inventory" | High (mass); the useful fraction is limited by energy, not by supply |
| What is NOT known | No design exists for any photospheric lifting mechanism; Criswell's and Beech's mechanisms were not readable (rows 7, 8, 11, 12); no study gives a mass-and-power budget for a solar-wind capture device; no study compares solar and planetary sources per tonne delivered | 3A, 3E | — | — | — |

**Short answer.** On the numbers found, lifting material from the Sun costs about ten million times more energy per
tonne of iron than lifting it off Mercury, and the Sun's matter is 98.6% hydrogen and helium, so about 500 t must be
lifted and separated per tonne of structural metal. The only literature that models starlifting does so to change the
Sun's evolution over billions of years, not to supply material. Skimming the natural solar wind costs no lifting energy
(the Sun already pays it) but the total wind is only about 1.3 x 10^9 kg/s spread over the whole sky; a collector
intercepts the fraction A/(4 pi r^2). The only flown example returned under a milligram. Harvesting from the Sun cannot
compete with Mercury, the Moon, asteroids, Venus's air or the gas giants for bulk material on any figure found here.
Where the Sun is unique is as a *power* source; its matter is the most expensive matter in the solar system to reach.

## 4. Conflicts

1. **Total mass removed in [HA26].** The paper states "0.13 M_sun over 5.1 Gyr, or 1.3 x 10^29 kg". At its own rate,
   5 x 10^19 kg/yr x 5.1 x 10^9 yr = 2.55 x 10^29 kg = 0.128 M_sun. The solar-mass figure and the rate agree; the kg
   figure is half of what they imply. Likely a transcription slip. Use 0.13 M_sun = 2.6 x 10^29 kg.
2. **The Sun's escape energy in [HA26] Table 1.** 20,000 MJ/kg versus 190,700 MJ/kg from [NSSDC]'s 617.6 km/s.
   The table's other entries (Mercury 9, Venus 54, Jupiter 1,800, Saturn 650) all check against the fact sheets, so
   the Sun entry alone is wrong, by about a factor of ten. Use 1.9 x 10^11 J/kg.
3. **Power as a fraction of the Sun's output in [SK23].** The paper writes 10^38 erg/yr as "about 10^-4 L_sun" and
   Matloff's 10^40 erg/yr as "about 0.01 L_sun". With L_sun = 3.828 x 10^26 W = 1.21 x 10^41 erg/yr, the ratios are
   7.9 x 10^-4 and 0.079 (Derived D1). The paper's absolute erg/yr figures are right; its conversion to L_sun is low by
   about a factor of 8. Use 8 x 10^-4 L_sun (ideal) and 0.08 L_sun (Matloff's per-kg figure).
4. **How much mass must be removed to hold the Sun's output constant.** Beech's analytic scaling (L proportional to
   M^5) as reported by [CA10]: "roughly 60%" of the Sun by the end of the main sequence. MESA runs ([SK23], [HA26]):
   0.13 M_sun over 5.1 Gyr. They answer different questions with different physics (an analytic homology relation
   versus a full evolution code with a fixed lifting rate and endpoint), so the numbers are not directly comparable. The
   MESA figure is the modern, model-based one.
5. **Parker heat-shield diameter.** The same NASA press kit gives "about 7.5 feet (2.3 meters)" ([PPK] PDF p.10) and
   "8 feet (2.4 meters)" ([PPK] PDF p.30); the 2008 design report gives 2.72 m ([STDT08]). Likely rounding in the kit,
   and design change between 2008 and the flown craft. Use "about 2.3 to 2.4 m" for the flown shield.
6. **Parker mass.** 635 kg "after fueling" ([PPK]) versus 685 kg "at launch" ([PMP]). Possibly a later mass update or a
   different accounting (adapter, margin). Not resolved from the sources read.
7. **Parker closest approach.** 6.2 million km ([PMP]), 3.86 million miles = 6.21 million km "from the solar surface"
   ([SVS]), 9.86 solar radii ([WHPI]). These agree once the reference point is fixed: 9.86 R_sun from the Sun's
   *center* is 6.86 million km; subtracting one solar radius gives 6.16 million km above the surface. Popular sources
   that say "6.1 million km" are measuring from the surface.
8. **Parker shield temperature.** 1,377 C ([PMP]), "about 1,400 C" ([PPK]), and a 2008 design value of about 1,700 K
   (1,427 C) ([STDT08]). These are consistent within rounding and design evolution.
9. **Does the solar wind's mass-loss rate vary with the cycle?** [MI19]: it "does not change even by a factor of 2" and
   is roughly anti-phased with sunspot number. [CR17] (from the Wang 1998 model): sphere-averaged rate "roughly 50%
   larger at solar maximum". [MI19] attributes the difference partly to its use of in-ecliptic data at 1 au, which it
   says is "not perfectly valid" as a global measure. Both agree on about 2 x 10^-14 M_sun/yr.
10. **CME share of mass loss.** Raw CDAW catalog: about 3% at maximum; earlier studies: 10-15%; [MI19]: about 5% near
    the ecliptic at maximum. [CR17] lists the reasons: missed halo and faint events, older instruments' bias to massive
    events, and possibly a real decline since the 1970s-80s.
11. **What "fast wind" means.** [LC20] Table 3 puts the ACE fast mode at 500 +/- 100 km/s; Hansteen 2010 (in [LC20]
    Table 1) uses 700-900 km/s. [LC20] fits a two-Gaussian distribution to all in-ecliptic data, where true polar
    coronal-hole wind is rare; Hansteen's values describe the high-latitude fast wind.
12. **Typical 1 au density.** 3 /cm^3 ([VE19], a round "typical" value) versus 5 +/- 3 (slow) and 3 +/- 2 (fast)
    ([LC20]). Not a real disagreement; the fluxes in 3C use [LC20]'s slow-wind value and are cross-checked against
    Genesis.
13. **Genesis collected mass.** The 2001 press kit's stated goal was "10 to 20 micrograms" of solar wind ([GPK]). The
    measured bulk hydrogen fluence over the flown collector area implies about 460 micrograms of hydrogen alone (Derived
    D4), 20 to 45 times the goal. Possible reasons: the goal may have referred only to the analyzable heavier elements,
    or to the area of collector expected to survive and be analyzed; the press kit does not say. Not resolved; the
    derived figure rests on two primary measurements ([HU19], [BU09]).
14. **Helium mass fraction from [A09].** Computing from [A09]'s log eps(He) = 10.93 gives Y = 0.2495, against the
    paper's stated 0.2485. [A09] brackets its He value as helioseismic; the 0.001 difference is rounding in the
    log eps. It does not affect any metal figure.
15. **Mercury's metal fraction.** "30% silicate and 70% metal" ([AS13], citing older work) versus a core of 73% of the
    mass derived from the MESSENGER-era radius and density ([WH17], Derived D6). The core is not pure metal (Fe with S
    and Si, per [WH17]), so "about 70% metal-rich core by mass" is the defensible statement.
16. **Solar wind in kg/s.** 1.3 x 10^9 kg/s from [MI19]; "a million tons" per second (1 x 10^9 kg/s) in [PPK]; 3 x
    10^16 kg/yr (0.95 x 10^9 kg/s) in [HA26]. All within the cycle-to-cycle spread. Use about 1 to 1.3 x 10^9 kg/s.

## 5. Derived figures

Constants from [NSSDC] unless stated: GM = 1.32712 x 10^20 m^3/s^2; R = 6.957 x 10^8 m (695,700 km); L = 3.828 x 10^26 W;
M = 1.9884 x 10^30 kg; 1 yr = 3.15576 x 10^7 s; 1 au = 1.495978707 x 10^11 m; proton mass 1.67262 x 10^-27 kg.

**D1. Lifting energy and power.**
- Ideal specific energy to escape from the photosphere: GM/R = 1.32712e20 / 6.957e8 = **1.908 x 10^11 J/kg**.
  Check: 0.5 x (617.6e3 m/s)^2 = 1.907 x 10^11 J/kg.
- Upper bound on lift rate if all of L went into lifting at 100%: 3.828e26 / 1.908e11 = 2.0 x 10^15 kg/s = 6.3 x 10^22 kg/yr.
- [SK23]'s rate 5 x 10^19 kg/yr = 1.58 x 10^12 kg/s. Ideal power: 1.58e12 x 1.908e11 = 3.0 x 10^23 W = **7.9 x 10^-4 L**.
- Matloff's 1.9 x 10^13 J/kg (as quoted in [SK23]) is 99.6 times GM/R; at 5e19 kg/yr it gives 3.0 x 10^25 W = **0.079 L**.
- L in erg/yr: 3.828e26 W x 3.15576e7 s x 1e7 erg/J = 1.21 x 10^41 erg/yr.
- Ratio of [SK23]'s rate to the natural wind: 1.58e12 / 1.32e9 = **about 1,200**.

**D2. Element mass fractions.** w_X = X_H x 10^(log eps_X - 12) x A_X / A_H, with X_H = 0.7438 ([A21]) or 0.7381 ([A09])
and A from [CIAAW]. Example, iron ([A21]): 0.7438 x 10^(7.46-12) x 55.845 / 1.0080 = 0.7438 x 2.884e-5 x 55.40 = 1.188 x
10^-3, so 1/w = 841 t of photosphere per t of Fe. Method check: helium gives 0.2423 = [A21]'s Y. Full output in 3B.

**D3. Solar wind flux and collector areas.**
- Mass loss: 2.1e-14 M_sun/yr x 1.9884e30 kg / 3.15576e7 s = **1.32 x 10^9 kg/s** (4.18 x 10^16 kg/yr). [CR17] Eq. 1 at
  S = 0 and 150: 2.0e-14 and 2.52e-14 M_sun/yr = 1.26 and 1.59 x 10^9 kg/s.
- Proton mass flux at 1 au, slow wind ([LC20] Table 3, 5 /cm^3 = 5e6 /m^3, 370 km/s): 5e6 x 1.67262e-27 x 3.7e5 =
  3.09 x 10^-15 kg m^-2 s^-1. Over the 1 au sphere (4 pi au^2 = 2.81 x 10^23 m^2): 8.7 x 10^8 kg/s, within a factor 1.5 of
  the global rate (helium and the fast wind make up the difference).
- Flux at distance r (au): 3.09e-15 / r^2 (mass conservation, [CR17] Eq. 4). Area for 1 kg/s = 1 / flux: 3.2 x 10^14 m^2
  at 1 au; 2.9 x 10^13 at 0.3; 3.2 x 10^12 at 0.1; 7.0 x 10^11 at 0.0465 au. Area for 1 t/yr (3.17 x 10^-5 kg/s):
  10,240 km^2; 922; 102; 22 km^2.
- A 30 km-radius cross-section (2.83 x 10^9 m^2) at 1 au: 2.83e9 x 3.09e-15 = 8.7 x 10^-6 kg/s = 0.28 t/yr.

**D4. Genesis yield.**
- Area: 1,672,944 mm^2 = 16,729 cm^2 ([BU09]). H atoms: 1.634e16 /cm^2 x 16,729 cm^2 = 2.73 x 10^20. Mass: 2.73e20 x
  1.0080 x 1.66054e-24 g = **4.6 x 10^-4 g (0.46 mg)**.
- Average H flux: 1.634e16 / (853 d x 86,400 s) = 2.2 x 10^8 /cm^2/s = 3.7 x 10^-15 kg m^-2 s^-1, agreeing with D3.
- Rate: 0.46 mg / 853 d x 365.25 = 0.20 mg/yr.

**D5. Radiative equilibrium of a sun-facing flat plate** (front side absorbs and emits; back insulated): T = (a S /
(e sigma))^(1/4), sigma = 5.670374 x 10^-8 W m^-2 K^-4, S = L / (4 pi r^2). Near the Sun the formula still holds for a
plate facing a sphere (view factor (R/r)^2), so T = 5,772 K x (R/r)^(1/2) x (a/e)^(1/4). Results in 3D. Setting T =
4,232 K (HfC): r = R x (5,772 / 4,232)^2 = 1.86 R (a/e = 1); with a/e = 0.6, r = R x (5,080 / 4,232)^2 = 1.44 R.

**D6. Comparison bodies.**
- Mercury escape energy: GM/R = 2.2032e13 / 2.4397e6 = 9.03 x 10^6 J/kg. Binding energy: 3 G M^2 / (5 R) = 3 x 6.674e-11
  x (3.3010e23)^2 / (5 x 2.4397e6) = 1.79 x 10^30 J (uniform-sphere formula; [AS13] gives 1.80 x 10^30 J).
- Mercury core mass: (4/3) pi (2.020e6 m)^3 x 6,980 kg/m^3 = 2.41 x 10^23 kg = 73% of 3.3010 x 10^23 kg.
- Venus: CO2 mass fraction = 0.965 x 44.01 / (0.965 x 44.01 + 0.035 x 28.014) = 0.977; carbon = 0.977 x 12.011 / 44.01 =
  0.267 of the atmosphere = 1.28 x 10^20 kg; N2 = 0.023 x 4.8e20 = 1.08 x 10^19 kg. Escape energy 0.5 x (10.36e3)^2 =
  53.7 MJ/kg.
- Jupiter: He mass fraction from volume fractions = 0.102 x 4.0026 / (0.102 x 4.0026 + 0.898 x 2.016) = 0.184; He-3 mass
  fraction = 0.184 x 1.66e-4 x 3.016 / 4.0026 = 2.3 x 10^-5; 1/(2.3e-5) kg = 43 t per kg of He-3. Saturn (same isotope
  ratio assumed): He 0.0628, He-3 7.9 x 10^-6. Escape energies 1,770 and 630 MJ/kg.
- [PA15] check: 500 kg / (4 kg/s x 1.52e-5) = 8.22 x 10^6 s = 95.2 days; at 10 kg/s, 38.1 days.

**D7. Energy per tonne of product, lifting only (ideal, separation excluded).**
- Sun, iron: 841 t x 1,000 kg/t x 1.908e11 J/kg = **1.6 x 10^17 J per t Fe**. Structural-metal mix: 513 t, 9.8 x 10^16 J.
  Carbon: 391 t, 7.5 x 10^16 J. Oxygen: 173 t, 3.3 x 10^16 J. Titanium: 5.8 x 10^19 J. Copper: 2.7 x 10^20 J.
- Mercury, iron-rich material at 70% metal: 9.03e6 x 1,000 / 0.7 = 1.3 x 10^10 J per t. Ratio Sun/Mercury = 1.2 x 10^7.
- Venus, carbon: 3.75 t CO2 x 53.7e6 J/kg x 1,000 = 2.0 x 10^11 J per t C. Ratio Sun/Venus = 3.7 x 10^5.
- Scale: 1.6 x 10^17 J is about 0.9 seconds of all sunlight intercepted by Earth (1.74 x 10^17 W), or
  about 5 years of the output of a 1 GW power station (1e9 W x 1.6e8 s).


## 6. Constraints for any inhabitant

Applies to any crewed or robotic presence working near the Sun or tending a solar-material operation.

- **Heat flux sets the closest approach.** Sunlight is 1,361 W/m^2 at 1 au, about 17,400 at 0.28 au (13 times), and
  about 650,000 W/m^2 at Parker's 9.86 solar radii (3C, 3D, D5). Anything inside about 0.3 au lives behind a sunshield;
  inside about 10 solar radii only a refractory carbon shield of the Parker type is proven, and only for hours per pass.
- **Nothing solid survives the photosphere's neighborhood.** A sun-facing plate passes the highest measured melting
  point of any compound (4,232 K, HfC) at about 1.4 to 1.9 solar radii from the center (D5, [SR16]). Any presence
  nearer than that needs active cooling with somewhere to put the heat, which no source here designs.
- **Shadow is life support.** Parker's shield admits under 50 W ("0.001% of the original flux") and holds the
  interior at about 30 C ([STDT08], [PPK]); its instruments sit in the umbra; a sensor seeing sunlight triggers an
  autonomous correction. A human-shaped machine near the Sun is in the same position: every part outside the shadow
  heats toward the plate temperatures above, and limbs that move out of the umbra must be refractory or briefly exposed.
- **Heat rejection is a design driver even in shadow.** Parker needs pumped water cooling (10-125 C) and radiators for
  its solar cells, and at least 0.64 m^2 of radiator to keep a 343 W bus below 40 C ([PPK], [STDT08]). A machine body
  dissipating its own power near the Sun must radiate it from the shadowed side only.
- **Autonomy.** One-way light time is about 8 minutes at 1 au ([PPK]); near the Sun the geometry is similar. Anything
  that must react to its heat environment must do so without waiting for Earth or any distant controller.
- **Dust at extreme speed.** Near-Sun dust ranges from submicron to several hundred microns and can hit at relative
  speeds up to about 350 km/s; prograde orbits cut typical impact speeds to about a quarter ([STDT08]).
- **Radiation.** Parker's design requirement was 44 krad (Si) over 7 years ([STDT08]); solar energetic particles
  and CMEs (3C) make dose episodic.
- **The material yield is tiny.** At 1 au a collector intercepts about 3 x 10^-15 kg m^-2 s^-1 of solar wind; 1 km^2
  gathers about 0.1 kg per year, almost all hydrogen and helium (3C, D3). Any occupation that depends on gathered
  solar material must cope with milligram-to-kilogram annual yields at practical sizes.
- **Mercury as the near-Sun alternative:** 6.67 times Earth's sunlight, no atmosphere to speak of, escape speed 4.3 km/s,
  and a large metal-rich core (3F).

## 7. Candidate handwaves

Flagged, not accepted. The developer decides.

1. **Any mechanism that lifts material off the photosphere.** No engineering design exists; the literature's mechanisms
   (beamed heating, magnetic schemes, "huff-n-puff", space elevators) are concept-level or need "as-yet uninvented
   materials" ([HA26]). Using starlifting at any rate is a handwave.
2. **The power to do it.** Even at 100% efficiency, a life-extension rate needs about 8 x 10^-4 of the Sun's whole
   output (3 x 10^23 W), and Matloff's figure implies about 8% ([SK23], D1). That presupposes a Dyson-swarm-scale
   collector. A *small* starlifting operation needs power in proportion to its rate: at the ideal 1.9 x 10^11 J/kg,
   lifting 1 kg/s takes 1.9 x 10^11 W (190 GW) continuously at 100% efficiency (D1), before separation.
3. **Hardware inside about 2 solar radii.** No known material survives passively (D5); doing so needs physics-bending
   materials or a cooling scheme that rejects tens of MW/m^2 somewhere.
4. **A magnetic "scoop" that captures, rather than deflects, solar-wind ions.** Light magnetic cross-sections of tens of
   km are studied for thrust ([SL]); a capture-and-store version has no design or yield in any source found.
5. **Separating metals from hydrogen-helium plasma at scale.** Required for any solar source (about 500 t processed per
   t of structural metal); no source here gives a process, energy or plant mass.

## 8. Open threads

- **Criswell (1985), the origin of starlifting:** book chapter in *Interstellar Migration and the Human Experience*; no
  open text; Internet Archive copies are lending-restricted (rows 7, 8). Next: a library or interlibrary loan.
- **Beech (2008), *Rejuvenating the Sun and Avoiding Other Global Catastrophes*** (Springer): chapter list only (row 11).
  Known here only through [CA10].
- **Matloff (2017), JBIS 70:458:** abstract only; paywalled (rows 5, 6). Its per-kg energy and scenarios are known only
  as quoted by [SK23].
- **Caplan (2019) and Svoronos (2020, 2021) stellar-engine papers:** abstracts only; ScienceDirect 403 (rows 16-18).
- **Criswell's "ring current" and "huff-n-puff" mechanisms:** no primary description online (row 12).
- **Absolute FIP enrichment of Fe relative to H in the solar wind:** [PI15] gives only ratios to Mg and the fFIP bias;
  arXiv 2411.18984 was surfaced but not read. Needed to turn "1 t of wind" into kg of each metal precisely. (He/H was
  resolved in the second run from Alterman and Kasper 2019, row 87; Kasper et al. 2007 itself was still not opened.)
- **Nittler et al. 2011 (Mercury surface XRS) numbers:** abstract-level only (row 78).
- **Hauck et al. 2013 direct:** escholarship 403 (row 72); values used come via [WH17].
- **Galileo probe helium mass fraction (Y = 0.238 per a search summary):** not confirmed in an opened page (row 74).
  Next: von Zahn et al. 1998 (JGR) or Niemann et al. 1998.
- **Palaszewski's Table I (He-3 fractions in Uranus and Neptune)** is an image in the PDF; only the 1.52 x 10^-5 case
  in the text was read.
- **Total mass of near-Earth asteroids:** not found in any source (row 84). Next: Granvik et al. 2018 (Icarus) size
  distribution integrated with assumed densities.
- **Fox et al. 2016 (Parker mission overview, Space Sci. Rev.):** CC-BY but blocked to the tools (row 41). Would give the
  flown TPS and cooling specifics.
- **Solar Probe 2005 report (NASA/TM-2005-212786)** for the 4 R_sun design (row 49): not opened.
- **Parker FIELDS antenna material** (refractory metal) and Parker's measured shield temperature: not found in a primary
  source this session.
- **Huss et al. 2019** was read only to character 100,000 of 155,196 (row 57); the remainder may give helium or
  metallicity results.
- **Sources found but not read:** arXiv 2411.18984 (slow-to-fast wind composition); arXiv 1504.08325 (FIP review);
  NTRS 20150020912 and 20230001527 (NEO/space-resources); Granvik et al. 2018 PDF; Taylor 2018 (Acta Astronautica,
  planet4589.org); arXiv 2510.21743 ("Propellantless space exploration"); arXiv 2305.04212 (rotating magnetic sail).

## 9. Rejected sources

- **Wikipedia, "Star lifting"** (row 10): secondary; its J/kg figure is internally inconsistent; used for leads only.
- **Orion's Arm, blogs, Big Think, halfbakery, Kerbal forum, LessWrong/EA forum posts** (rows 12, 13, 61, 65):
  secondary or fiction; no numbers used.
- **Wikipedia and eoPortal "0.4 mg / 10^20 ions" for Genesis** (row 31): secondary; replaced by D4 from [HU19] and [BU09].
- **Search-engine summary figures** not found in any opened page: lunar He-3 total 6.5 x 10^8 kg (sibling's row 26);
  Galileo Y = 0.238 and He mole fraction 0.1359 (row 74); "He-3 is 0.002% of the solar wind" and "average flux 3 x
  10^10 ions/cm^2/s" (row 61; the latter is about 100 times Genesis's measured 2.2 x 10^8 /cm^2/s and is rejected); a
  tungsten melting point (row 81); NHATS counts (row 84).
- **Research Square preprint, "A Cycling Spacecraft for Harvesting Antimatter from the Sun"** (row 79): not
  peer-reviewed, and antimatter harvesting is outside this topic.
- **University of Wisconsin NEEP 533 lecture 12** (row 64): lecture slides; secondary; the sibling Moon file already
  holds lunar He-3 from a review.
- **NTRS 20070014073, Genesis radiation environment** (row 62): off-topic for yield.
