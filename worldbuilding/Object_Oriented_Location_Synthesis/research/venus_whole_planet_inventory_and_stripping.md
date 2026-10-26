# Venus as a whole planet: inventory, and stripping the atmosphere and solid body

## Scope

Venus as a whole body: interior layers (crust, mantle, core), bulk element inventory, the atmosphere and clouds as the
first layer to remove, the physical methods for removing or transforming that atmosphere, what the bared surface would do,
and the scale of excavating or removing the solid planet. Physics and engineering only; no setting is assumed.

*Session note: the first session (rows 1 to 11) ended at a tool session limit before any findings were written. The second
session (rows 12 onward, same date) re-read the two papers already downloaded in rows 4 and 7 from the local copies and
continued the log.*

## SEARCH LOG

All entries dated 2026-10-11.

| # | Search string or page opened | Result | Notes |
|---|---|---|---|
| 1 | Read-only sibling files: `_BRIEF.md`; `inner_system_mining_synthesis.md` (all); `starlifting_synthesis.md` (sections 0 to 1); `venus_as_extraction_site.md` (sections 1 to 3.11, Conflicts head, D6); `mars_venus_and_transfer.md` 3.7, 3.11; `gap_retry_mars_venus_jupiter.md` 3.10, 3.14, 3.15 | useful | Cited below as **VE** (`venus_as_extraction_site.md`), **MVT**, **GRV**, **SYN-I** (`inner_system_mining_synthesis.md`), **SYN-S** (`starlifting_synthesis.md`); not re-derived |
| 2 | WebSearch: `Margot 2021 Nature Astronomy spin state and moment of inertia of Venus 0.337 core radius` | useful | Leads: NTRS 20220003058, Cornell and UBC news pages (secondary); numbers confirmed in row 4 |
| 3 | WebSearch: `Venus interior structure models core radius mantle density Dumoulin 2017 tidal constraints k2 Love number` | useful | Leads: Gillmann et al. 2024 review (arXiv:2404.07669); EGU2017-12774 (Dumoulin abstract, not opened) |
| 4 | Opened (curl, PDF text): Gillmann, Arney, Avice, Dyar, Golabek, Gülcher, Johnson, Lefèvre, Widemann, "Venus", arXiv:2404.07669v2 (12 Apr 2024), sections 2, 3.1, 3.2.1, 4.1 to 4.3 | useful | Radius, mass, density, MoI 0.337 +/- 0.024, core radius 3,500 +/- 500 km, field < 1e-5 Earth, water 2 cm GEL, D/H, resurfacing age, volcanic rate |
| 5 | WebSearch: `Shah 2022 "interior structure" Venus models core mass fraction crust thickness arXiv composition sulfur core` | useful | Leads: ApJ 926:217, arXiv:2112.03225 |
| 6 | Opened: boris.unibe.ch PDF of Shah et al. 2022 | dead at the sources | Returned an HTML page, not the PDF |
| 7 | Opened (curl, PDF text): Shah, Helled, Alibert, Mezger, "Possible Chemical Composition and Interior Structure Models for Venus Inferred from Numerical Modelling", arXiv:2112.03225v1 (6 Dec 2021; published ApJ 926:217, 2022) | useful | MoI 0.317 to 0.351; core 2,930 to 4,350 km; core S, Si, O ranges by case; core mass fraction 0.22 to 0.38 (S-rich, high MoI); central P and T from Aitta 2012, Steinberger 2010, Dumoulin 2017 |
| 8 | WebSearch: `Morgan Anders 1980 PNAS "Chemical composition of Earth, Venus, and Mercury" bulk composition table` | thin | Located PMC350422; A&A 2014 table that reproduces it |
| 9 | Opened: PMC350422 (WebFetch), pnas.org PDF, PMC PDF, Europe PMC PDF render (curl) | dead at the sources | Page text has only the abstract; PDFs return anti-bot HTML. The tables are scanned images in any case |
| 10 | Opened: A&A 2014 aa22208-13 Table 6 | dead at the sources | HTTP 403 |
| 11 | WebSearch (extended): `Venus bulk composition model element abundances wt% Fe Mg Si O S table Lodders Fegley 1998 Venus core 23.6% mass` | dead at the query | Tool returned a session-limit error; no search was run. (The "23.6%" in the string is a recalled number and is not used anywhere) |
| 12 | Re-read (local text of row 4 and row 7 downloads): Gillmann et al. 2024 sec. 2, 3.1.1 to 3.2.1, 4.1 to 4.4; Shah et al. 2022 abstract, Tables 3 and 5, sec. 3.1.1 to 3.2 | useful | Second session; figures entered in 3.1 and 3.2 from these readings |
| 13 | WebSearch: `Venus bulk composition model table weight percent Fe Mg Si O S core mass fraction Lodders Fegley` | useful | Lead: Jacobson et al. 2017 (arXiv:1710.01770); no Lodders and Fegley table surfaced (that part died at the sources) |
| 14 | Opened (curl, PDF text): Jacobson, Rubie, Hernlund, Morbidelli, Nakajima, "Formation, stratification, and mixing of the cores of Earth and Venus", EPSL 474 (2017), arXiv:1710.01770, supplementary Tables 1 and 2 | useful | Mantle and core compositions and core mass fraction 0.300 of a simulated Venus-like planet (0.92 Earth masses at 0.62 AU) |
| 15 | WebSearch: `"Morgan and Anders" Venus bulk composition core 32% mantle FeO cosmochemical model equilibrium condensation Venus` | dead at the sources | Only Shah 2022 again, describing the method; the 1980 table itself not reachable (see row 9). The "32%" is a guess embedded in the query string and is not used |
| 16 | WebSearch: `Dumoulin Tobie Verhoeven Rosenblatt Rambaux 2017 "Tidal constraints on the interior of Venus" pdf composition models core radius` | useful | Leads: EGU2017-12774 and EPSC2018-856 abstracts; full JGR paper not open-access |
| 17 | Opened (curl): EGU2017-12774 abstract (Dumoulin et al.) and EPSC2018-856 abstract | useful | MoI 0.327 to 0.342, core 2,900 to 3,450 km, k2 0.25 to 0.36, solid core not ruled out; k2 below 0.27 would mean fully solid core |
| 18 | Opened (NTRS API + full text): Margot, Campbell, Giorgini, Jao, Snedeker, Ghigo, Bonsall, "Spin state and moment of inertia of Venus", Nature Astronomy 5 (2021), NTRS 20220003058 (arXiv text) | useful | C/MR^2 0.337 +/- 0.024; C = 6.01 x 10^37 kg m^2; two-layer model core 3,508 km at 10,358 kg/m^3, mantle 4,006 kg/m^3; atmospheric angular momentum 2.9 x 10^28 kg m^2/s +/- 30%; LOD varies 61 ppm |
| 19 | WebSearch: `Paul Birch "Terraforming Venus quickly" JBIS 1991 sunshade freezing atmosphere pdf` | thin | Secondary summaries (Wikipedia, phys.org, Universe Today) only; no PDF link in results |
| 20 | Opened (curl): orionsarm.com/fm_store/TerraformingVenusQuickly.pdf (scanned; OCR with tesseract at 300 dpi); paulbirch.net copies unreachable | useful | P. Birch, "Terraforming Venus Quickly", JBIS 44, 157-167 (1991), full text: cooling stages and Appendix, sunshade 2.5 x 10^14 m^2 and 7.6 x 10^10 kg, heat pipes, CO2 seas, ice-moon. OCR quality fair; every figure used was checked against the Appendix arithmetic where possible |
| 21 | WebSearch: `Fogg "The terraforming of Venus" JBIS 1987 hydrogen Bosch reaction graphite water CO2 removal mass of hydrogen required` | dead at the sources | Citation only (JBIS 40, 551-564); no open copy; Wikipedia, forums and a blog only |
| 22 | WebFetch: en.wikipedia.org/wiki/Terraforming_of_Venus (first 100,000 characters) | useful (leads only, secondary) | Leads: Pollack and Sagan 1994 (impact), Birch 1993 (spin), Nordley (mass-driver export), carbonate and basalt-injection figures, "4 x 10^19 kg of hydrogen" attributed to Birch 1991 (that attribution is not supported by the Birch text; Conflicts) |
| 23 | Opened (curl): orionsarm.com three filename guesses for Birch, "How to Spin a Planet" | dead at the sources | HTML pages, not the paper |
| 24 | WebSearch: `Birch "How to spin a planet" JBIS 1993 pdf` | thin | BIS shop page (abstract only); NTRS 19930059709 suggested |
| 25 | Opened: NTRS API 19930059709; BIS shop page 12737 (WebFetch) | NTRS dead at the sources (a different paper, Icarus 1993 on planetary spin origin); BIS page useful | Birch 1993 abstract: off-center bombardment is costly, 24 h hard to reach, atmosphere loss possible. No numbers in the abstract |
| 26 | WebSearch: `Venus rotation equilibrium atmospheric thermal tides solid body tides despinning timescale Correia Laskar without atmosphere synchronous rotation` | useful | Leads: Auclair-Desrotour et al. arXiv:1709.09478; Laskar outreach page |
| 27 | Opened (curl): Auclair-Desrotour, Laskar, Mathis, arXiv:1709.09478 (EAS 2017) | thin | Mechanism (solid vs thermal tides; synchronous state unstable when the atmospheric torque is strong) but no timescale |
| 28 | WebSearch (extended): `"Venus" spin "tidal despinning" time scale billion years Q k2 solid tides Gold Soter atmospheric torque balance estimate` | useful | Leads: Way and Del Genio 2020 (arXiv:2003.05704); Ingersoll and Dobrovolskis 1978 (Nature 275, 37) not opened; search summary's "about 10^8 years" not traced to a source opened (not used) |
| 29 | Opened (curl): Way and Del Genio, "Venusian Habitable Climate Scenarios", JGR Planets 125 (2020), arXiv:2003.05704, sec. 2 (tidal) | useful | Solid-tide-only locking within 684 Myr from a 3-day prograde start (CPL, Q = 12, k2 = 0.3, a lower limit); k2 = 0.295 +/- 0.066 (Konopliv and Yoder 1996); Q estimates below 17, about 40, about 100 |
| 30 | WebSearch: `Pollack Sagan 1994 "Planetary engineering" Resources of Near-Earth Space Venus atmosphere removal impact 700 km pdf` | useful | Leads: NTRS 19910016777 (abstract), University of Arizona Press open-access PDF of the whole book |
| 31 | Opened: NTRS 19910016777 (abstract, no download); open.uapress.arizona.edu PDF of "Resources of Near-Earth Space" (J. S. Lewis, M. S. Matthews, M. L. Guerrieri, eds., Univ. Arizona Press, 1993), 990 pp., chapter "Planetary Engineering" by J. B. Pollack and C. Sagan, pp. 921 to about 950, section III (Venus) read in full | useful | Impact erosion (about 3,000 impactors above 700 km at above 20 km/s), microbes, anti-greenhouse carbon layer (6 x 10^14 g C), sunshade 10^14 to 10^16 g, carbonate layer 400 m, Mercury Ca and Mg (0.5% of Mercury's mass) |
| 32 | WebSearch: `Nordley Venus atmosphere export mass drivers spin up Venus 30 day terraforming` | thin | Only secondary pages: the idea is from G. D. Nordley's 1991 short story "The Snows of Venus" (fiction, not a study). Checked by arithmetic in D5 |
| 33 | WebSearch: `temperature-dependent thermal diffusivity basalt crust high temperature Whittington Hofmeister Nabelek 2009 Nature mm2/s` | useful | Lead: Durham mantleplumes PDF copy of Whittington et al. 2009 |
| 34 | Opened (curl, certificate error bypassed for a read-only download): Whittington, Hofmeister, Nabelek, "Temperature-dependent thermal diffusivity of the Earth's crust and implications for magmatism", Nature 458, 319-321 (2009) | useful | Diffusivity 1.5 to 2.5 mm^2/s at room temperature falling to about 0.5 mm^2/s at mid-crustal temperatures; eq. (1) kappa = 567.3/T - 0.062 mm^2/s below 846 K; garnet, pyroxene, olivine 0.6 to 0.7 mm^2/s at upper-mantle temperatures; average crust conductivity about 3.8 falling to about 1.9 W/m/K |
| 35 | WebSearch: `basalt thermal conductivity thermal diffusivity as function of temperature laser flash measurements 300 to 1000 K W/m/K` | thin | Lead: Mostafa et al. 2004 (Egyptian basalts) |
| 36 | WebFetch: aun.edu.eg summary of Mostafa, Afify, Gaber, Abu Zaid, J. Thermal Anal. Calorim. (2004) | thin | Abstract only: conductivity 0.4 x 10^-3 to 2.01 x 10^-3 cal/(cm s K) (0.17 to 0.84 W/m/K), r.t. to 900 K; no per-temperature table. Not used for a design number (porous samples likely; Conflicts) |
| 37 | WebSearch: `Venus crustal thickness mean estimate gravity topography admittance James Zuber Phillips 2013 kilometers` | useful | Leads: MIT DSpace record of James et al. 2013; Maia and Wieczorek arXiv:2202.06971; search summary's "20-25 km" not used |
| 38 | WebFetch: dspace.mit.edu/handle/1721.1/85638 (abstract of James, Zuber, Phillips, "Crustal thickness and support of topography on Venus", JGR Planets 118, 859-875, 2013) | useful | Mean crustal thickness 8 to 25 km; dynamic mantle load at 250 km |
| 39 | Opened (curl): Maia and Wieczorek, "Lithospheric Structure of Venusian Crustal Plateaus", arXiv:2202.06971 (Feb 2022; JGR Planets) | useful | Plateau crust 15 to 34 km; global average about 20 km if Airy; crustal density assumed 2,800 kg/m^3; elastic thickness below 35 km (best 15 km); ambient heat flow 10 to 30 mW/m^2 (cited), gradient 6 to 14 C/km, 12 to 28 mW/m^2 |
| 40 | Opened (curl, HTML parsed): NSSDC fact sheets for Earth (updated 15 Nov 2024), Moon and Venus (both updated 11 Jan 2024) | useful | Venus M 4.8673 x 10^24 kg, GM 0.32486 x 10^6 km^3/s^2, R 6051.8 km, escape 10.36 km/s, Bond albedo 0.77, I/MR^2 0.337, irradiance 2601.3 W/m^2, black-body 226.6 K, a = 108.210 x 10^6 km; Earth M 5.9722 x 10^24 kg; Moon Bond albedo 0.11 |
| 41 | WebSearch: `Lamur 2018 "The mechanics of columnar jointing" basalt thermal expansion coefficient tensile strength Young's modulus cooling contraction` | useful | Lead: PMC5897544 |
| 42 | WebFetch: PMC5897544 (Lamur, Kendrick, Eggertsson, Wall, Ashworth, Lavallée, "The onset of columnar jointing in lavas", Nature Communications 9, 1432, 2018) | useful | Linear expansion about 10^-5 per C (400 to 980 C); E = 1.371 x 10^7 T(C) + 2.6157 x 10^10 Pa; tensile strength 12 to 21 MPa; failure after 87 to 144 C of cooling below the solidus; sigma = E alpha dT |
| 43 | Opened (curl, PDF text): Handbook of Mineralogy (Mineral Data Publishing / MSA) sheets for calcite, magnesite, dolomite | useful (calcite and magnesite after one retry; first attempt wrote no file) | Densities: calcite 2.7102 g/cm^3 (meas.); magnesite 3.00; dolomite 2.86 |
| 44 | WebSearch: `carbon dioxide propellant nuclear thermal rocket specific impulse CO2 NIMF Zubrin Mars hopper Isp seconds` | useful | Lead: NTRS 19910012833; forum and blog figures (226 s, 260 s) not used |
| 45 | Opened (NTRS API + text): R. M. Zubrin, "Nuclear thermal rockets using indigenous extraterrestrial propellants", NASA Lewis, Vision-21 (Apr 1990), NTRS 19910012833 | useful | Table 1 ideal Isp, CO2 row: 283, 310, 337, 381 s at 2,800, 3,000, 3,200, 3,500 K (row labels lost in the text layer; the text confirms "a specific impulse of 280 seconds" for a CO2 NIMF at 2,800 K); CO/O2 280 to 290 s |
| 46 | WebSearch: `Venus Express ASPERA-4 measured escape rate O+ H+ ions per second Barabash 2007 Nature water loss` | thin | Ratios only from the ESA page; the search summary's "1 x 10^25 and 1.6 x 10^25 s^-1" not traced to a page opened (not used) |
| 47 | WebFetch: sci.esa.int Venus Express publication page 41903 (Barabash et al. 2007); research.aber.ac.uk record | thin | Barabash et al., Nature 450, 650-653 (2007): Q(H+)/Q(O+) = 1.9, Q(He+)/Q(O+) = 0.07; no absolute rates on either page (died at the sources for the absolute rates) |
| 48 | WebSearch: `Venus Express total ion escape rate oxygen hydrogen s^-1 solar cycle Persson 2018 Fedorov 2011 Venus atmospheric loss rate kg` | useful | Lead: Gillmann et al. 2022 (arXiv:2204.08540) |
| 49 | Opened (curl, PDF text): Gillmann, Way, Avice, Breuer, Golabek, Höning et al., "The long-term evolution of the atmosphere of Venus: processes and feedback mechanisms", Space Sci. Rev. (2022), arXiv:2204.08540v2, escape section | useful | O+ escape (3 to 6) x 10^24 s^-1 (Fedorov 2011, Persson 2018); H+ 7.6 x 10^24 (solar min) to 2.1 x 10^24 s^-1 (max); O+ 2.9 to 2.0 x 10^24; neutral H* escape about 1.3 to 2.65 x 10^25 s^-1 |
| 50 | WebSearch: `dismantling Venus planet disassembly mass driver stellar engineering Venus solid body removal study` | dead at the sources | Mailing-list archives, forums, a news blog and an OrionsArm (fiction) page; no engineering study of removing Venus's solid body. A blog's "2.6 x 10^32 J" is unsourced (not used; compare D3) |
| 51 | WebSearch: `interplanetary dust meteoroid flux at Venus orbit 0.72 AU compared to 1 AU Grün model mass flux kg per year onto Venus` | useful | Lead: Sahu and Pabari arXiv:2605.12420 |
| 52 | Opened (curl, PDF text): Sahu and Pabari, "Modeling and Analysis of Main-Belt Asteroidal Dust Flux and Velocity Distribution at Inner Planets", arXiv:2605.12420v1 (12 May 2026, preprint) | useful | IDP flux near Venus 10^-4 to 10^-5 m^-2 s^-1 (Hirai et al. 2014, ALADDIN, cited); mean dust impact velocity 13.9 km/s at Venus (11.4 km/s in Carrillo-Sánchez 2020); minimum impact speed 10.4 km/s; fitted cumulative flux law F_Venus(m) = 10^-11.59 m^-0.74 (units as in the paper, not restated here) |
| 53 | WebSearch (extended): `Fegley "Venus" Treatise on Geochemistry 2014 bulk composition of Venus table Morgan Anders 1980 Goettel model core mass percent` | useful | Lead: Fegley 2004 Treatise chapter reprint at solarsystem.wustl.edu (the 2014 edition not found open) |
| 54 | Opened (curl, PDF text): B. Fegley Jr., "Venus", Treatise on Geochemistry vol. 1, ch. 1.19 (Elsevier 2004), author reprint, Tables 2 and 9 | useful | Table 9 (after Lodders and Fegley 1998): three bulk models, chondritic (Morgan and Anders 1980), equilibrium condensation (BVSP Ve1), pyrolite (BVSP Ve4), with mantle oxides, core Fe/Ni/Co/S/O and core mass fractions 0.32, 0.30, 0.24. Table 2: M 4.8685 x 10^24 kg, MoI 0.331 to 0.341 (pre-2021), Bond albedo 0.750, 740 K and 95.6 bar at modal radius. This closes the Morgan and Anders gap of rows 8 to 11 and 15 |
| 55 | WebSearch: `fate of material ejected from Venus heliocentric orbit reaccretion timescale ejecta returning to Venus Gladman simulation` | thin | The search summary's Venus figures (about 30% to Earth, 12 Myr median, over 80% reaccreted in 10^5 yr) were not traced to any page opened (not used). Leads: NTRS 19930005184, 19930005139, Gladman and Coffey arXiv:0801.4038 |
| 56 | Opened: NTRS API 19930005184 (Schultz, impact-generated winds on Venus) and 19930005139 (Izenberg, ejecta deposits) | dead at the sources | Both about cratering on Venus, not escaping ejecta |
| 57 | WebFetch: news.cornell.edu 1996 release on Gladman et al. | dead at the sources | No Venus figures (Moon and Mars only) |
| 58 | WebSearch: `Gladman Burns Duncan Lee Levison 1996 Science "exchange of impact ejecta between terrestrial planets" Venus ejecta reaccreted fraction` | thin | Citation confirmed (Science 271, 1387-1392); no open text; Gladman's publication page did not download (curl wrote no file) |
| 59 | Opened (curl, PDF text): Gladman and Coffey, "Mercurian impact ejecta: meteorites and mantle", arXiv:0801.4038 (preprint; Meteoritics and Planetary Science 2009) | useful (as an analog only) | At v_inf = v_esc, half of Mercury's ejecta is re-accreted by Mercury in 30 Myr and 20% more by Venus; 40 to 70% of ejecta swept up by Mercury, Venus and Earth within 30 Myr; at higher launch speeds about 25% returns |
| 60 | Re-read (local copy of row 54): Fegley 2004 sec. 1.19.3 and 1.19.4.2.1 | useful | Urey reaction CaCO3 + SiO2 = CaSiO3 + CO2, log10 P_CO2 = 7.97 - 4456/T (Fegley and Treiman 1992); D/H implies a past ocean at least 4 m and possibly 530 m deep (Donahue et al. 1997) |
| 61 | (No search.) Findings, Conflicts, Derived figures (scripts `venus_calc.py`, `venus_calc2.py` in the scratch folder), Constraints, Candidate handwaves, Open threads and Rejected sources written; writing finished 2026-10-12 | n/a | Totals over both sessions: 27 web searches (one never ran, row 11), 11 rows dead at the query or at the sources, the rest page opens and re-reads |

## Findings

**Reading in one paragraph.** Venus is an Earth-sized silicate planet with a metal core of uncertain size and state
(core radius somewhere in 2,900 to 4,350 km across published models; core 22 to 38% of the mass), a basaltic crust
averaging 8 to 25 km, and essentially no hydrogen. The atmosphere is the only layer anyone has seriously studied
removing, and every study that puts numbers on it lands far beyond any engineering scale: escape costs about 54 MJ/kg
(2.6 x 10^28 J for the whole atmosphere, which is about 2,700 years of *all* the sunlight Venus intercepts, at 100%
conversion); impact stripping needs about 3,000 bodies larger than 700 km; a sunshade plus freezing (Birch 1991) takes
90 to 200 years of waiting and then needs the frozen CO2 kept covered forever; chemical sequestration needs about
2 km of the crust pulverized and reacted, and only holds once the surface is below about 560 K. **No published study
of removing or excavating Venus's solid body was found;** the only numbers are binding energies, and the true
(differentiated) value is about 10% above the uniform-sphere figure (D3). The atmosphere's angular momentum is only
0.16% of the solid planet's, but the *reaction* from throwing the atmosphere off tangentially is 1.2 to 1.7 times the
planet's whole spin angular momentum, so a removal operation would set Venus's day length as a side effect (D5).

### 3.1 Interior structure (checklist 1)

| Quantity | Value and units | Source (publisher, title, URL, date) | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Mass, radius, density, gravity | 4.8673 x 10^24 kg; 6,051.8 km (no flattening); 5,243 kg/m^3; 8.87 m/s^2; GM 3.2486 x 10^14 m^3/s^2; escape 10.36 km/s | NSSDC Venus Fact Sheet, https://nssdc.gsfc.nasa.gov/planetary/factsheet/venusfact.html (11 Jan 2024) | Primary | Gillmann et al. 2024 (same mass, radius, density); Fegley 2004 Table 2 (4.8685 x 10^24 kg, GM 3.2486 x 10^14, escape 10.361 km/s) | High |
| Moment of inertia (measured) | C/MR^2 = 0.337 +/- 0.024 (bootstrap mean 0.3373; least squares 0.3350); C = (6.01 +/- 0.43) x 10^37 kg m^2; spin-axis precession 44.58 +/- 3.3 arcsec/yr; obliquity 2.6392 +/- 0.0008 deg; from Earth-based radar speckle tracking 2006 to 2020 | Margot et al., "Spin state and moment of inertia of Venus", Nature Astronomy 5 (2021), NTRS 20220003058 (arXiv text) | Primary | NSSDC 0.337; Gillmann 2024 quotes it; pre-measurement models 0.327 to 0.342 (Dumoulin 2017), 0.317 to 0.351 (Shah 2022), 0.331 to 0.341 (Fegley 2004) | Medium (7% uncertainty) |
| Core radius | Margot two-layer crude estimate 3,508 km (58% of the radius), core density fixed at 10,358 kg/m^3, mantle 4,006 kg/m^3, uncertainty above 500 km; Gillmann summary 3,500 +/- 500 km; Dumoulin 2017 models 2,900 to 3,450 km; Shah 2022 2,930 to 4,350 km over all compositions (S-free 2,930 to 3,610; nominal 2,960 to 3,890; S-rich 3,010 to 4,350); earlier single models 3,186 km (Steinberger 2010) and 3,228 km (Aitta 2012); 3,000 to 3,500 km (Amorim and Gudkova 2023) | Margot 2021; Gillmann et al., arXiv:2404.07669v2 (Apr 2024) sec. 4.1; Dumoulin et al. EGU2017-12774 and EPSC2018-856 abstracts; Shah et al., ApJ 926:217 (2022), arXiv:2112.03225 sec. 3.1.2, 3.2 | Primary | Four independent model families overlap at about 3,000 to 3,500 km | Medium for "about 3,000 to 3,500 km"; low for any single value |
| Core state | Unknown. Measured k2 = 0.295 +/- 0.066 (Konopliv and Yoder 1996, Magellan and Pioneer Venus tracking) taken to imply a liquid core (Yoder 1997); viscoelastic models give k2 0.25 to 0.36 and do not rule out a fully solid core (k2 below 0.27 would indicate one); a solid inner core "could exist for all compositions" (Shah), up to 3,330 km (S-free); a solid inner core judged unlikely from central pressures (Amorim and Gudkova 2023, via Gillmann). No intrinsic field: any dipole below 10^-5 of Earth's (Pioneer Venus Orbiter). Proposed reasons: liquid but not convecting (low core heat flow, perhaps a basal magma ocean); stably stratified core from accretion (Jacobson et al. 2017); fully frozen core | Way and Del Genio, JGR Planets 125 (2020), arXiv:2003.05704 sec. 2; Dumoulin EGU2017/EPSC2018 abstracts; Shah 2022; Gillmann 2024 sec. 2, 4.1, 4.2; Jacobson et al., EPSL 474 (2017), arXiv:1710.01770 | Primary | Sources disagree; no seismic data exist | Low |
| Central pressure and temperature (models) | 5,200 K and 275 GPa (Aitta 2012); about 285 GPa (Steinberger 2010); 271 to 299 GPa (Dumoulin 2017); up to 351 GPa (Shah, S-free case) | Shah 2022 sec. 3.2 (citing each) | Primary (review within a paper) | none opened beyond Shah | Medium (models only) |
| Crust thickness and density | Global mean 8 to 25 km (gravity and topography inversion); crustal plateaus 15 to 34 km, implying a global mean of about 20 km if Airy-compensated; density 2,800 kg/m^3 assumed (basalt), 2,650 kg/m^3 tested for felsic tesserae (adds about 2 km to thickness); basaltic crust 2.9 to 3.1 g/cm^3 (Shah) | James, Zuber, Phillips, JGR Planets 118, 859-875 (2013), abstract at dspace.mit.edu/handle/1721.1/85638; Maia and Wieczorek, arXiv:2202.06971 (2022); Shah 2022 sec. 2.2 | Primary | Two methods agree on tens of km; Fegley 2004 Fig. 3 cartoon (after Lodders and Fegley 1998) shows a thicker crust (text garbled in the copy; not used) | Medium |
| Mantle | Upper and lower mantle expected; basalt-to-eclogite and ringwoodite-to-bridgmanite transitions deeper than in Earth; no post-perovskite expected above the core; gravity-topography correlation suggests no Earth-like asthenosphere, though a low-viscosity layer "a couple of hundred kilometers" thick is permitted (Maia 2023); mantle FeO 0.03 to 15 mol% across Shah's models (13.4 wt% in Ringwood and Anderson 1977) | Gillmann 2024 sec. 4.1, 4.3; Shah 2022 | Primary | Fegley Table 9 mantle FeO 0.24 to 18.7 wt% across three models (3.2) | Low (unsampled) |
| Heat flow | Ambient 10 to 30 mW/m^2 (cited in Maia); 12 to 28 mW/m^2 from a 6 to 14 C/km gradient; hot spots above 75 mW/m^2 at some coronae and rifts; total heat loss 11 to 14.5 TW, mean 24 to 32 mW/m^2 (VE 3.6, Ruiz et al. 2024) | Maia and Wieczorek 2022 sec. on heat flow; Gillmann 2024 Fig. 5 caption; VE 3.6 | Primary | Ranges overlap | Medium |
| Surface age and present volcanism | Surface 250 to 1,000 Myr old from the crater record; global volcanic production 0.1 to 10 km^3/yr; a new flow on Maat Mons appeared within an 8-month gap in 1991 (Magellan); episodic overturn or equilibrium resurfacing both fit the crater data | Gillmann 2024 sec. 4.3, 4.4 | Primary (review) | GRV 3.14: extrusive flux about 0.4 km^3/yr (Bullock and Grinspoon 1996); Birch 1991 quotes about 1 km^3/yr | Medium |
| Rotation | Sidereal day 243.0226 +/- 0.0013 Earth days (2006 to 2020 average), retrograde; spin period varies by 61 ppm (about 20 minutes); solar day 116.75 d; equatorial surface speed 1.8 m/s (D5); cause of the retrograde spin unknown (impact, core-mantle friction, atmospheric tides or an early ocean are proposed) | Margot 2021; Gillmann 2024 sec. 2 | Primary | NSSDC; Fegley 2004 243.0185 d (older value) | High |

### 3.2 Bulk composition and whole-planet element inventory (checklist 1)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Three classic bulk models (mantle + crust oxides, wt%) | **Chondritic** (Morgan and Anders 1980): SiO2 49.8, TiO2 0.21, Al2O3 4.1, FeO 5.4, Cr2O3 0.87, MnO 0.09, MgO 35.5, CaO 3.3, Na2O 0.28, K2O 0.027. **Equilibrium condensation** (BVSP Ve1): SiO2 52.9, TiO2 0.20, Al2O3 3.8, FeO 0.24, MgO 37.6, CaO 3.6, Na2O 1.6, K2O 0.174. **Pyrolite** (BVSP Ve4): SiO2 40.4, TiO2 0.24, Al2O3 3.4, FeO 18.7, Cr2O3 0.3, MnO 0.2, MgO 33.3, CaO 3.4, Na2O 0.15, K2O 0.018 | Fegley, "Venus", Treatise on Geochemistry vol. 1 ch. 1.19 (2004), Table 9, after Lodders and Fegley 1998 (author reprint, solarsystem.wustl.edu) | Primary (handbook table) | Jacobson 2017 model mantle (next row) falls between them | Medium (the models are 1980s cosmochemistry; none is measured) |
| Core composition and core mass fraction, same three models | Chondritic: Fe 88.6, Ni 5.5, Co 0.26, S 5.1, O 0 wt%; core 0.32 of mass. Equilibrium condensation: Fe 94.4, Ni 5.6, S 0; core 0.30. Pyrolite: Fe 78.7, Ni 6.6, S 4.9, O 9.8; core 0.24 | Fegley 2004 Table 9 | Primary | Shah 2022 CMF 0.22 to 0.38; Ringwood and Anderson about 0.23 | Medium |
| A modern accretion-and-differentiation model (Venus-like planet of 0.92 Earth masses at 0.62 AU) | Mantle: SiO2 45.14, MgO 35.77, FeO 9.784, Al2O3 4.38, CaO 3.52 wt%; Na 2,390, Cr 2,990, Ni 3,966, S 1,505 ppm; H2O 60 ppm (Earth-like planet in the same run: 1,000 ppm). Core: Fe 81.9, Si 7.30, Ni 4.90, O 3.48, S 1.47, Cr 0.697, Co 0.227 wt%; H 148 ppm. Core mass fraction 0.300 | Jacobson, Rubie, Hernlund, Morbidelli, Nakajima, EPSL 474 (2017), arXiv:1710.01770, supplementary Table 2 | Primary (model) | The model planet is 13% more massive than Venus (D2), so its pressures differ | Medium (one simulated planet, not Venus) |
| Core light elements across a structure-model grid | S-free: O up to about 0.73 wt%, Si up to 13 wt%. Nominal: O 0 to 1.3, Si 0.12 to 13, S 3.9 to 7.9 wt%. S-rich: O 0 to 2.9, Si 0.04 to 12, S 9.1 to 22 wt%. S-rich, high-MoI models: CMF 0.22 to 0.38, S 21 to 32 mol%, FeO/(FeO+MgO) 0.11 to 0.28 | Shah 2022 sec. 3.1.2, 3.2 | Primary | Fegley Table 9 core S 0 to 5.1 wt% | Medium |
| **Whole-planet element inventory (DERIVED, D2)** across the four models above, applied to Venus's mass | O 1.49 to 1.66 x 10^24 kg (30.7 to 34.1%); Fe 1.38 to 1.52 x 10^24 (28.5 to 31.2%); Si 0.70 to 0.84 x 10^24 (14.4 to 17.3%); Mg 0.71 to 0.77 x 10^24 (14.6 to 15.9%); Ca 7.8 to 9.0 x 10^22 (1.6 to 1.9%); Ni 7.7 to 8.6 x 10^22 (1.6 to 1.8%); Al 6.7 to 7.9 x 10^22 (1.4 to 1.6%); S 0 to 7.9 x 10^22 (0 to 1.6%); Cr 0 to 2.0 x 10^22; Na 0.4 to 4.0 x 10^22 (0.08 to 0.83%); Ti about 4 to 5 x 10^21; Co up to 4 x 10^21; K 0.6 to 4.9 x 10^21 | DERIVED (D2) | Derived | Fe, O, Si, Mg agree within about 10 to 20% across models; S, Na, K, Cr differ by factors of several | Medium for Fe, O, Si, Mg; low for S, Na, K |
| Where the iron is | Of about 1.46 x 10^24 kg of Fe (Jacobson case), about 1.2 x 10^24 kg is in the core and about 2.6 x 10^23 kg in mantle FeO (D2); the crust (8 to 25 km) is 0.2 to 0.7% of the planet's mass (D1) | DERIVED | Derived | Surface basalt FeO 7.7 to 9.3 wt% (VE 3.6) | Medium |
| Why the models disagree | Only the mean density (about 2% below Earth's for the same composition), the MoI and k2 are measured. The trade-offs: more light element (S, O, Si) in the core gives a larger, less dense core; more FeO in the mantle gives a denser mantle and smaller core (negative correlation of mantle FeO with core size); higher MoI implies more oxidized conditions; volatile depletion is set by condensation-temperature assumptions. No samples, no seismology | Shah 2022 sec. 1, 3.1.3, 3.1.4; Gillmann 2024 sec. 4.1 | Primary | Fegley 2004 describes the three model philosophies | High (for the reasons) |
| What Venus lacks: water and hydrogen | Atmospheric water about 2 cm global-equivalent layer, about 10^16 kg (one terrestrial ocean is 1.4 x 10^21 kg); D/H with delta-D near 120,000 permil, read as large past hydrogen escape; a past ocean "at least 4 m and possibly 530 m deep" (Donahue et al. 1997, via Fegley); model mantle water 60 ppm (Jacobson case). Hydrogen in the whole atmosphere 7 x 10^14 kg (brief; VE D2) | Gillmann 2024 sec. 3.1.1, 3.2.1; Fegley 2004 sec. 1.19.3; Jacobson 2017 | Primary | D11: 2 cm GEL = 9.2 x 10^15 kg | Medium |
| Atmospheric volatiles by mass (for the inventory) | CO2 4.69 x 10^20 kg (Fegley 2014); N2 11 x 10^18 kg (Johnson and Goldblatt 2015), 2.8 times Earth's atmospheric N2; SO2 about 6 x 10^16 kg; water about 10^16 kg | Gillmann 2024 sec. 3.1.1 | Primary (review) | VE 3.1 derived C 1.28 x 10^20, N 1.08 x 10^19 kg | High for CO2, N2; medium for SO2, H2O |

### 3.3 The atmosphere as the first layer: published removal and transformation methods (checklist 2)

Total mass 4.8 x 10^20 kg (NSSDC; given). Element inventory: VE 3.1 (not re-derived). Status words: DEMONSTRATED,
ENGINEERING-STUDIED, SPECULATIVE.

| Method | Mass, energy, time and mass flow | Source | Primary or secondary | Cross-check | Status and confidence |
|---|---|---|---|---|---|
| **Launch to escape (mass driver or any launcher)** | About 50 MJ/kg; 2.5 x 10^28 J; "a terawatt ... for 850 million years" (GRV 3.14, Landis 2011). DERIVED (D4): GM/R = 53.7 MJ/kg, 2.58 x 10^28 J; 790 Myr at 1 TW; at 100% of all sunlight Venus intercepts (3.0 x 10^17 W) about 2,700 yr. To do it in 100 yr: 1.5 x 10^11 kg/s and 8.2 x 10^18 W (27 times Venus's intercepted sunlight); in 1,000 yr: 1.5 x 10^10 kg/s and 2.7 times | Landis 2011 (via GRV 3.14); DERIVED D4 | Primary / derived | Two routes agree within 3% | SPECULATIVE (no launcher of any kind studied for Venus, VE 3.7); high confidence in the energy floor |
| **Impact stripping** | Only the air above the local tangent plane can be blown off; Venus needs impactors above about 10 km for any loss and above about 700 km at above 20 km/s to clear the tangent-plane cap; "about 3000 impactors each larger than 700 km"; no loss below 20 km/s; "There is nothing like this number of large bodies in the solar system" | Pollack and Sagan, "Planetary Engineering", in Resources of Near-Earth Space (Univ. Arizona Press 1993), pp. 933-934 (open-access PDF) | Primary (book chapter) | Landis 2011 (GRV 3.14): at least 2,000 impacts even at perfect efficiency; with 10% coupling about two million 1-km or two thousand 10-km asteroids (Conflicts 3) | SPECULATIVE; judged ineffective by both |
| **Sunshade, then freeze the atmosphere out** | Shade of solar-sail film, 3 x 10^-4 kg/m^2, about 2.5 x 10^14 m^2 and 7.6 x 10^10 kg (sunshade plus support mirror), placed at about a quarter of the distance to L1 and held by light from an annular mirror; cooling stages: 730 K to 304 K (CO2 critical point), rain-out to 74 bar, cooling to the triple point 217 K at about 7 bar, freezing of CO2 seas, snow-out to about 192 K leaving about 0.8 bar CO2 and about 2 bar N2. Total 87.2 yr/emissivity, bounded 90 to 200 yr; about 20 bar rains out at once; seas form over about 70% of the surface; heat pipes (about 10^11 kg/s of water) could save about 45 yr in stage 1. The frozen CO2 must then be covered and insulated permanently | P. Birch, "Terraforming Venus Quickly", JBIS 44, 157-167 (1991) (scan, OCR) | Primary (journal paper; SPECULATIVE) | DERIVED D7 reproduces the 200 yr (198 yr) and the shade area and mass (2.6 x 10^14 m^2, 7.8 x 10^10 kg); Pollack and Sagan: a parallel-ray shield 1 um thick about 10^14 g, but about 10^16 g for full umbra; "at room temperature, essentially all the CO2 sea would become vapor" (Conflicts 4) | SPECULATIVE; medium confidence in the physics of the cooling time |
| **Chemical sequestration as carbonates** | Slightly over 1 kg of CaMgO2 per kg CO2; pulverizing at least 1 km of crust; carbonates decompose at present surface temperature (GRV 3.14, Landis 2011). Pollack and Sagan: carbonate would form a layer about 400 m deep, and an equal depth of CaO, MgO or similar must be processed; an alternative is importing Ca and Mg metal from Mercury (needing "~0.5% of the planet's mass" processed, attributed to Birch). DERIVED (D6): 4.3 x 10^20 kg MgO or 6.0 x 10^20 kg CaO; as magnesite a 650 m global layer, as calcite 855 m; Venera and Vega basalts can bind 0.17 to 0.18 kg CO2 per kg, so about 2.0 to 2.2 km of the whole crust (about 10% of a 20 km crust) must be mined, ground and reacted completely. The Urey equilibrium (log10 P_CO2 = 7.97 - 4456/T, Fegley and Treiman 1992) gives 89 bar at 740 K and 1 bar at 559 K, so carbonates hold the CO2 only after the surface is below about 560 K (D12) | GRV 3.14; Pollack and Sagan 1993 pp. 937-938; Fegley 2004 sec. 1.19.4.2.1; DERIVED | Primary / derived | The natural rate: cooling by surface-atmosphere reaction takes 10^7 to 10^8 yr (Bullock and Grinspoon 1996, GRV 3.14) | SPECULATIVE; high confidence in the stoichiometry |
| **Biological or chemical fixation as carbon** | Microbes in the clouds fixing CO2 to graphite: every mole of CO2 needs a mole of water (Venus has 3 x 10^-5 as much H2O as CO2); a recycling scheme would bury the surface under "hundreds of meters of fine graphite" and release about 65 bar of O2; pyrolysis products re-oxidize at 700 K in about an hour. DERIVED Bosch route CO2 + 2H2 -> C + 2H2O: 4.3 x 10^19 kg of hydrogen (61,000 times Venus's hydrogen), yielding 3.8 x 10^20 kg of water (an 834 m global layer, 27% of one Earth ocean) and 1.3 x 10^20 kg of carbon; the whole solar wind would need about 1,400 yr to supply that hydrogen, if all of it could be caught (D6) | Pollack and Sagan 1993 pp. 934-935; DERIVED D6 | Primary / derived | Wikipedia states "about 4 x 10^19 kg of hydrogen" and attributes it to Birch 1991; Birch's paper does not contain it (Conflicts 5) | SPECULATIVE |
| **Anti-greenhouse dust layer** (cooling, not removal) | 0.1 um carbon particles, absorption optical depth 5: about 6 x 10^14 g (one 1-km carbonaceous asteroid); lifetime a few years against vertical mixing; thermal response time of the atmosphere a few decades; daylight "perhaps only as bright as on a moonlit night"; the 90 bar remains | Pollack and Sagan 1993 pp. 935-936 | Primary | none | SPECULATIVE |
| **Splitting CO2** (not removal; changes composition) | 3.0 x 10^27 J at the thermodynamic floor to split all CO2 (VE 3.10); the plant-scale figure is 5.7 kWh per kg O2 (VE 3.3) | VE 3.3, 3.10 | (cited) | D6 reproduces 3.0 x 10^27 J | ENGINEERING-STUDIED at kg/hr scale only |
| **Natural escape** (a scale, not a method) | O+ escape (3 to 6) x 10^24 ions/s; H+ 2.1 to 7.6 x 10^24 s^-1 over the solar cycle; escape near the stoichiometric ratio of water. DERIVED: 0.09 to 0.18 kg/s, so the whole atmosphere at that rate would take about 10^14 yr (D9) | Gillmann et al. 2022, Space Sci. Rev., arXiv:2204.08540 (Fedorov 2011, Persson 2018); Barabash et al., Nature 450, 650 (2007) (ratios) | Primary | Ratios Q(H+)/Q(O+) = 1.9 (Barabash) | DEMONSTRATED (measured); medium |
| **Photodissociation as a removal route** | No study found that proposes it at scale. Natural photochemistry already splits CO2 above the clouds and the loss rate is the escape rate above; any engineered version would still need the 54 MJ/kg escape energy per kg removed | Row above; D4 | Derived | none | Not a removal method on present evidence |
| **The published comparison** | Pollack and Sagan: "making Venus habitable ... is an extremely formidable task. There does not seem to be any elegant way to do it"; "None of these proposals seems feasible for the next century". Landis 2011: terraforming would require "an unreasonable amount of energy, or the use of highly advanced technologies" (GRV 3.14). Birch 1991 claims under about 200 yr and economic break-even, on cost assumptions (orbital rings, self-funding floating colonies) that are not engineering studies | Pollack and Sagan 1993 p. 938; GRV 3.14; Birch 1991 | Primary | The three disagree on feasibility, not on the physics (Conflicts 4) | n/a |

### 3.4 What the surface does once the atmosphere is gone (checklist 3)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Present surface state | 737 K, 92 bar; basalt (SiO2 45 to 49%, FeO 8 to 9%); about 16 W/m^2 of sunlight absorbed at the ground; interior heat 24 to 32 mW/m^2 (VE 3.6) | VE 3.6; MVT 3.7 | (cited) | n/a | High |
| Temperature without an atmosphere, at present albedo | "about 240 K with the present albedo" (Pollack and Sagan); NSSDC black-body temperature 226.6 K at Bond albedo 0.77. Both use the cloud albedo, which would leave with the atmosphere | Pollack and Sagan 1993 p. 933; NSSDC | Primary | Agree within 6% | Medium (the albedo assumption is the issue) |
| Bare-rock equilibrium temperatures (DERIVED, D8) | With a lunar-like Bond albedo of 0.11 (NSSDC Moon): subsolar about 450 K (423 K at albedo 0.3); a planet-average equilibrium of 299 to 318 K. A 116.75-day solar day means about 58 days of continuous day and of night at any point, so day and night temperatures would separate widely (as on Mercury, SYN-I sec. 3), not sit at the average | DERIVED from NSSDC irradiance 2,601.3 W/m^2, NIST sigma | Derived | none | Medium (no measured bare-Venus albedo; regolith thermal inertia unknown) |
| Stored crustal heat after the atmosphere is removed (DERIVED, D8) | A half-space at 735 K with its surface held near 300 K, conductivity 2 to 3 W/m/K and diffusivity 0.7 to 1.0 mm^2/s: surface heat flux about 100 to 130 W/m^2 after 1 yr, 33 to 41 after 10 yr, 10 to 13 after 100 yr, 3 to 4 after 1,000 yr. On the night side this alone would hold the surface near 207 K (1 yr), 155 K (10 yr), 116 K (100 yr). The rock cooled by 100 K or more reaches about 8 m in 1 yr, 80 m in 100 yr, 800 m in 10,000 yr | DERIVED; inputs: Whittington et al., Nature 458, 319 (2009) (kappa = 567.3/T - 0.062 mm^2/s, giving 0.71 at 735 K; conductivity about 1.9 W/m/K for hot crust, olivine 3.0 at 1,000 K) | Derived | Birch 1991: crustal cooling limited to "a relatively thin surface layer ~30m thick" over the cooling period, adding under 3% to cooling time (agrees in order, D8) | Medium (continental-crust diffusivities used for basalt; no Venus rock measured) |
| Cracking as the crust cools (DERIVED, D8) | Basalt thermal stress sigma = E alpha dT with alpha about 10^-5 per C and E about 30 GPa: 30 MPa per 100 K of cooling, 130 to 140 MPa for 435 K, against a tensile strength of 12 to 21 MPa. In lava, columnar joints open after 87 to 144 C of cooling below the solidus. So any part of the surface that cools by more than roughly 50 to 100 K while constrained would fracture into a joint network, propagating downward with the cooling front (8 m in the first year) | Lamur et al., Nature Communications 9, 1432 (2018) (PMC5897544); DERIVED | Primary / derived | Birch 1991 expects "widespread earthquakes" and possible eruptions from loading by CO2 seas (a different mechanism) | Medium for the mechanism; low for depths (lab basalt from Iceland, no Venus rock) |
| Unloading the surface | Removing 92 bar takes 9.2 MPa off the surface, equal to about 370 m of rock (D8); against a crust of 8 to 25 km and a mantle with an elastic lid below 35 km thick (Maia), the direct mechanical effect is small; no study of decompression-triggered volcanism or outgassing on removal was found | DERIVED; Maia 2022 | Derived | Birch 1991 (loading by seas, the opposite case) | Low (no study) |
| CO2 held in surface minerals | The CO2 pressure matches the calcite-wollastonite (Urey) equilibrium at 740 K (Fegley and Treiman 1992); whether carbonates exist on Venus is open. If they do, and the atmosphere is removed while the surface is still hot, they would release CO2 toward 81 to 89 bar equilibrium at 735 to 740 K (D12) | Fegley 2004 sec. 1.19.4.2.1; DERIVED | Primary / derived | none | Low (carbonate presence unknown) |
| Unshielded surface: meteoroids | Today meteoroids ablate in the atmosphere. Interplanetary dust flux near Venus is of order 10^-4 to 10^-5 m^-2 s^-1 (Hirai et al. 2014, ALADDIN, cited); modeled mean dust impact speed at Venus 13.9 km/s (11.4 km/s in Carrillo-Sánchez 2020); minimum impact speed equals escape, 10.4 km/s. Without the atmosphere these reach the ground | Sahu and Pabari, arXiv:2605.12420 (May 2026, preprint) | Primary (preprint) | Scaled Grün model agrees with their flux within 0.09 orders of magnitude | Medium |
| Unshielded surface: radiation | Today 51 km already has an Earth-surface-like column (VE 3.11; GRV 3.12); the bared surface would sit under no column, as on the Moon or Mercury, with no intrinsic magnetic field (below 10^-5 of Earth's) | GRV 3.12; Gillmann 2024 sec. 2 | (cited) | n/a | Medium |

### 3.5 Excavating and removing the solid body (checklist 4)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Published concepts for removing Venus's solid body | **None found** (rows 50, 53). The only Venus-material concept is Landis 2003's "high-temperature fullerine tether ... to directly lift ore" (VE 3.6), with no numbers; VE found no surface-mining study | Row 50; VE 3.6 | n/a | none | Gap (stated plainly) |
| Layer masses (DERIVED, D1) | Crust 8 to 25 km at 2,800 kg/m^3: 1.0 to 3.2 x 10^22 kg (0.2 to 0.7% of the planet; 21 to 67 times the atmosphere). Core 22 to 38% of the mass (1.07 to 1.85 x 10^24 kg); the Margot two-layer case gives 0.385 (1.87 x 10^24 kg). Silicate shell 3.0 to 3.8 x 10^24 kg | DERIVED from the rows in 3.1 and 3.2 | Derived | Margot two-layer masses sum to 1.0001 of M (consistency check) | Medium |
| Depth and volume to reach the core | For a core of 2,900 / 3,500 / 4,350 km radius: depth 3,152 / 2,552 / 1,702 km; the volume above the core is 89 / 81 / 63% of the planet's volume (D1) | DERIVED | Derived | none | Medium |
| Energy to lift one kilogram from the surface to escape | 53.7 MJ/kg, 5.96 times Mercury's 9.0 MJ/kg (SYN-I) | DERIVED (D3) from NSSDC GM and R | Derived | Brief: 5.9 times | High |
| Binding energy of the whole planet | Uniform sphere 1.57 x 10^32 J (given; D3 reproduces 1.568 x 10^32); with Margot's two-layer density structure 1.73 x 10^32 J (10% higher), 96 times Mercury's uniform value (88 times uniform to uniform); mean 32 to 35 MJ per kg | DERIVED (D3) | Derived | An unsourced blog value of 2.6 x 10^32 J is rejected (Rejected sources) | High for the uniform value; medium for the two-layer value (biased model) |
| Throughput and power for total removal (DERIVED, D4) | In 31 / 100 / 1,000 yr: 5.0 x 10^15 / 1.5 x 10^15 / 1.5 x 10^14 kg/s, and 1.6 to 1.8 x 10^23 / 5.0 to 5.5 x 10^22 / 5.0 to 5.5 x 10^21 W, which is 5.4 to 5.9 x 10^5 / 1.7 to 1.8 x 10^5 / 1.7 to 1.8 x 10^4 times all the sunlight Venus intercepts. At 100% of Venus's own intercepted sunlight the minimum time is 1.8 x 10^7 yr. A collector at Venus's distance would need 1.9 to 6.8 x 10^19 m^2 (10^4 to 6 x 10^5 Venus disks) at 100% efficiency | DERIVED | Derived | none | High (arithmetic); the scale is the finding |
| Excavating under the atmosphere | The surface is 735 to 737 K at 92 bar, landers have lasted about 2 hours, and heat rejection costs 1.4 to 5.2 W of work per W (VE 3.6); so either the atmosphere is removed first (3.3) or the machinery is a high-temperature design that does not yet exist | VE 3.6 | (cited) | n/a | High |
| Where the launched material goes | Material launched at just above escape remains in heliocentric orbits that cross Venus's; for Mercury's ejecta at v_inf = v_esc, half returns to Mercury within 30 Myr and 20% more reaches Venus; at higher speeds about 25% returns (an analog; no Venus-specific figure was opened). Removal therefore needs the material sent somewhere or captured, not just launched | Gladman and Coffey, arXiv:0801.4038 (2008/2009) | Primary (preprint; analog) | Gladman et al., Science 271, 1387 (1996) not opened | Medium for the principle; no Venus number |

### 3.6 Rotation, tides and the launch direction (checklist 5)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Why Venus spins as it does | Solid-body solar tides alone would synchronize the spin to the 224.7-day orbit; solar torques on the thermally driven atmospheric tide oppose them (Gold and Soter), and the spin settles where the two balance | Margot 2021, main text; Auclair-Desrotour, Laskar, Mathis, arXiv:1709.09478 (2017) | Primary | Way and Del Genio 2020 | Medium (the mechanism is accepted; the balance point's dynamics "have not been elucidated", Margot) |
| Atmosphere's angular momentum | About 2.9 x 10^28 kg m^2/s (+/- 30%), about 180 times Earth's atmospheric value; length-of-day variations imply at least about 4% of it is exchanged with the solid planet (61 ppm, about 20 minutes, in spin period). DERIVED: the solid planet's spin angular momentum is 1.8 x 10^31 kg m^2/s, so the atmosphere holds 0.16% of it (D5) | Margot 2021 | Primary | none | Medium |
| Effect of removing the atmosphere on the spin | Directly, almost none (0.16%). Indirectly, the thermal-tide torque disappears and solid tides would drive the spin toward synchronous; scaling Way and Del Genio's constant-phase-lag result (684 Myr from a 3-day prograde start, Q = 12, k2 = 0.3, a lower limit) gives about 18 Myr from the present state (D5). Geologically fast; irrelevant on human timescales | DERIVED from Way and Del Genio 2020 sec. 2 | Derived | Q estimates range below 17, about 40 and about 100 (via Way 2020); higher Q means slower | Low (constant-torque scaling, uncertain Q) |
| Reaction from launching the atmosphere | Tangential launch of 4.8 x 10^20 kg at 7.33 to 10.36 km/s carries 2.1 to 3.0 x 10^31 kg m^2/s, 1.2 to 1.7 times the planet's spin. Launched against the rotation: sidereal day shortens to 91 to 111 d (still retrograde). Launched with it: spin reverses to a prograde day of 361 to 1,325 d. Launched radially: no change (D5) | DERIVED from Margot C and NSSDC | Derived | none | High (arithmetic) |
| Spin-up claims | Nordley's fiction (atmosphere export spinning Venus to a 30-day day) would need about 44 km/s tangential launch if only the atmosphere is thrown, or 2.0 x 10^21 kg at 10.36 km/s; a 24-hour day needs 6.9 x 10^22 kg (1.4% of Venus) thrown at 10.36 km/s, or 1.6 x 10^29 J of rotational energy (D5). Birch 1993: off-center bombardment is "costly", 24 h "not easily obtained", and "serious loss of atmosphere" may result | DERIVED; Birch, JBIS 46, 311-313 (1993), abstract | Derived / primary (abstract) | Wikipedia quotes 1.6 x 10^29 J for an Earth-like day (matches D5) | High (arithmetic); SPECULATIVE concepts |
| Launch-direction geometry for a fixed track | The planet turns 1.8 m/s at the equator, so rotation gives no launch help. The equator lies within 2.64 deg of the orbital plane, so an equatorial track can point along or against Venus's orbital motion; a fixed track points the same way relative to the Sun once per solar day, 116.75 d, sweeping about 3.1 deg per Earth day. For pure disposal to escape (atmosphere removal) direction does not matter except for spin (above) and for where the material ends up (3.5) | DERIVED from Gillmann 2024 (2.64 deg, 116.75 d) and NSSDC | Derived | SYN-I sec. 3: Mercury's fixed track gets about 2.4 usable days in six years for Earth; the same window problem applies to any Venus-to-destination launch (not computed here) | Medium |

### 3.7 Clouds and trace volatiles as a separate resource; the atmosphere as reaction mass (checklists 6 and 7)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Cloud and trace inventory | Cited, not re-derived: cloud mass about 5 x 10^13 kg; droplets 75 to 92 wt% H2SO4; S in gases 5.5 x 10^16 kg; Cl 1.6 x 10^14 kg; H 6.7 x 10^14 kg; hydrogen in the clouds about 2 x 10^12 kg (VE 3.1, D1 to D3) | VE 3.1 | (cited) | Gillmann: SO2 about 6 x 10^16 kg, giving S 3.0 x 10^16 kg (D11); water about 10^16 kg, giving H 1.1 x 10^15 kg (Conflicts 6) | Medium |
| New: sulfur and water in Birch's accounting | "probably only about 1 mm of water locked up in sulfuric acid"; acid reactions with surface silicates would mainly remove corrosives | Birch 1991 sec. 4.2 | Primary | DERIVED from VE: 2 x 10^12 kg of cloud hydrogen is about 0.04 mm of water globally (an order below Birch's estimate; Conflicts 6) | Low |
| CO2 as rocket propellant | Ideal Isp of CO2 heated in a solid-core nuclear thermal rocket: 283, 310, 337, 381 s at 2,800, 3,000, 3,200, 3,500 K; CO/O2 burned 280 to 290 s; the studied CO/LOX ascent uses 250 s (VE 3.7) | Zubrin, NTRS 19910012833 (1990), Table 1 and text | Primary (concept) | Text states 280 s for the 2,800 K CO2 vehicle | Medium (table row labels lost in the scan; ENGINEERING-STUDIED as a concept, never built) |
| Mass ratio to leave Venus with atmospheric propellants (DERIVED, D10) | To 9 km/s (cloud deck to orbit, VE 3.7): 39 (250 s), 26 (283 s), 11 (381 s). To 10.36 km/s: 68, 42, 16 | DERIVED | Derived | VE D7: 39 at 250 s | High (arithmetic) |
| Does rocket exhaust count as removed atmosphere? | No. Exhaust speeds of 2.45 to 3.74 km/s are below the 10.36 km/s escape speed, so the propellant stays bound and only the payload leaves (D10). Using the atmosphere as propellant for its own removal therefore removes little; the energy floor of 54 MJ per kg actually removed is unchanged | DERIVED | Derived | none | High |
| Venus as an intermediate base | What the atmosphere supplies in quantity and in place: CO2 and N2 as reaction mass and feedstock, O2 and CO from electrolysis (VE 3.3), carbon and nitrogen for local use (SYN-I sec. 4). What it does not supply: hydrogen, and an exit cheaper than about 9 km/s (VE 3.7) | VE 3.3, 3.7; SYN-I | (cited) | n/a | Medium |

## Conflicts

1. **Core size: 2,900 to 4,350 km.** Margot's 3,508 km comes from a two-layer, uniform-density model with the core
   density fixed at 10,358 kg/m^3 (taken from Dumoulin's PREM-scaled models); Margot calls it biased. Shah's range is wider
   because it lets the core take up to 22 wt% S and up to 15 mol% FeO into the mantle; Dumoulin's narrower 2,900 to
   3,450 km uses four compositions and two temperature profiles. The disagreement is in the light-element and redox
   assumptions, not in the data, because the only data are density, MoI (+/- 7%) and k2 (+/- 22%). Consequence: the
   Margot two-layer core holds 38.5% of the mass, near the top of Shah's 0.22 to 0.38 and above all three classic models
   (0.24 to 0.32).
2. **Core state.** k2 = 0.295 +/- 0.066 was read as "liquid core" (Yoder 1997, via Way 2020), but viscoelastic mantle
   models (Dumoulin) show a solid core cannot be ruled out, and Shah finds a solid inner core possible in every
   composition while Amorim and Gudkova (via Gillmann) judge one unlikely. The difference is rheology (elastic versus
   Andrade viscoelastic) and the assumed core melting curve. Unresolved until a better k2 and tidal lag are measured.
3. **Impact stripping: 3,000 impactors above 700 km (Pollack and Sagan) versus at least 2,000 impacts (Landis 2011,
   GRV 3.14).** Both rest on tangent-plane geometry. Pollack and Sagan scale Vickery and Melosh's Earth thresholds by the
   100-fold larger atmospheric mass and require each impactor to clear its whole cap; Landis's 2,000 is a floor at
   perfect efficiency, rising to about two million 1-km or two thousand 10-km bodies at 10% coupling. They agree that
   the method is impractical.
4. **Sunshade and freezing: Birch (under about 200 yr, economic) versus Pollack and Sagan ("far beyond anticipated human
   resources") versus Landis 2011 ("an extremely very long time to cool", GRV 3.14).** Birch's 90 to 200 yr is the cooling
   of the atmosphere alone with the crust neglected (he argues only about 30 m of rock cools in that time; D8 agrees in
   order); D7 reproduces his 198 yr. Pollack and Sagan accept the physics but object that the frozen CO2 "would become
   vapor" at room temperature if any cover leaks, and that a full-umbra shield is an order of magnitude larger (about
   10^16 g) than a parallel-ray one. Birch's own design puts the shade at about a quarter of the L1 distance with 1.27 times
   Venus's diameter for full umbra, at 7.6 x 10^10 kg. The difference is placement and assumed film thickness: Birch's
   3 x 10^-4 kg/m^2 film versus Pollack and Sagan's 1 um (about 10^-3 kg/m^2 at an assumed 1,000 kg/m^3, D7).
5. **"4 x 10^19 kg of hydrogen" attributed to Birch 1991 on Wikipedia.** The Birch 1991 text read here does not
   contain that figure or a hydrogen-bombardment proposal (it imports hydrogen only for water at colony scale and uses an
   ice moon for oceans). The number itself is reproduced by D6 (4.3 x 10^19 kg for the Bosch reaction), so the arithmetic
   is right and the attribution is doubtful (perhaps Fogg 1987 or Birch's "Supramundane Planets", neither opened).
6. **Hydrogen and water inventories.** VE derived 6.7 x 10^14 kg of hydrogen in the gases from 30 ppm water; Gillmann
   gives about 10^16 kg of water (2 cm GEL), which holds 1.1 x 10^15 kg of hydrogen (D11), a factor of 1.7 apart (the water
   mixing ratio used: 30 ppm below the clouds against a GEL that may weight a different profile). Birch's "about 1 mm" of
   water in the acid is 25 times the 0.04 mm implied by VE's cloud-hydrogen estimate (Birch gives no basis; the VE cloud mass
   is an order-of-magnitude figure).
7. **Basalt thermal properties.** Whittington et al. give 0.5 to 0.7 mm^2/s and about 1.9 W/m/K for hot crust (continental
   mineralogy) and 3.0 W/m/K for olivine at 1,000 K; the Egyptian basalt abstract gives 0.17 to 0.84 W/m/K, far lower,
   probably because of porosity (the abstract does not say). D8 brackets with 2 and 3 W/m/K; a porous or fractured
   surface layer would conduct less and cool its surface faster.
8. **Moment of inertia before and after 2021.** Fegley 2004 lists 0.331 to 0.341 (a model range, before any measurement);
   NSSDC and Margot give the measured 0.337 +/- 0.024. Not a real conflict, but older sources quote a model as if measured.

## Derived figures

Script: `/tmp/claude-1000/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/3ccdb441-c6c0-49c3-a71c-ab4a4fdd3c1e/scratchpad/venus_whole_planet_inventory_and_stripping/py/venus_calc.py`
and `venus_calc2.py` (same folder); full output in `../calc_output.txt`. Inputs: NSSDC Venus and Earth fact sheets
(M 4.8673 x 10^24 kg, R 6,051.8 km, GM 3.2486 x 10^14 m^3/s^2, irradiance 2,601.3 W/m^2, escape 10.36 km/s); NIST CODATA
(G 6.67430 x 10^-11, sigma 5.670374419 x 10^-8, u 1.66053906892 x 10^-27 kg); CIAAW conventional atomic weights; Margot 2021
(C, period, two-layer densities, AAM); Gillmann 2024 (CO2, N2, SO2, H2O masses); Fegley 2004 Table 9; Jacobson 2017 Table 2;
Whittington 2009; Lamur 2018; Handbook of Mineralogy densities; Way and Del Genio 2020; Zubrin 1990.

**D1 Layer masses.** Core (Margot two-layer) = 4/3 pi (3.508 x 10^6 m)^3 x 10,358 = 1.873 x 10^24 kg (0.385 of M); with the
4,006 kg/m^3 mantle the total is 1.0001 M. Crust shell 4/3 pi (R^3 - (R - t)^3) x 2,800: t = 8, 20, 25 km gives 1.03, 2.57,
3.21 x 10^22 kg (0.21, 0.53, 0.66% of M; 21, 54, 67 times the atmosphere). Depth to core R - Rc: 3,152, 2,552, 1,702 km for
Rc = 2,900, 3,500, 4,350 km; volume above core 89.0, 80.7, 62.9%. Planet volume 9.284 x 10^20 m^3; area 4.602 x 10^14 m^2;
disk 1.151 x 10^14 m^2.

**D2 Element inventory.** Element mass = (1 - CMF) M x oxide wt% x (n A_el / M_oxide) for the mantle, plus CMF M x wt% for
the core. Jacobson case (CMF 0.300): O 1.532 x 10^24, Fe 1.455 x 10^24, Si 8.26 x 10^23, Mg 7.35 x 10^23, Ca 8.57 x 10^22,
Ni 8.51 x 10^22, Al 7.90 x 10^22, S 2.66 x 10^22, Cr 2.04 x 10^22, Na 8.1 x 10^21, Co 3.3 x 10^21 kg (sum 99.8% of M). The
Jacobson model planet is 0.92 Earth masses = 5.49 x 10^24 kg against Venus's 4.867 x 10^24 kg (0.815 Earth), so its
fractions are applied, not its masses. Fe in core 1.196 x 10^24 kg; Fe in mantle FeO 2.59 x 10^23 kg. Fegley Table 9 cases:

| Element | Chondritic (CMF 0.32) | Equilibrium condensation (0.30) | Pyrolite (0.24) |
|---|---|---|---|
| O | 1.49 x 10^24 (30.7%) | 1.58 x 10^24 (32.5%) | 1.66 x 10^24 (34.1%) |
| Fe | 1.52 x 10^24 (31.2%) | 1.38 x 10^24 (28.5%) | 1.46 x 10^24 (29.9%) |
| Mg | 7.09 x 10^23 (14.6%) | 7.73 x 10^23 (15.9%) | 7.43 x 10^23 (15.3%) |
| Si | 7.70 x 10^23 (15.8%) | 8.42 x 10^23 (17.3%) | 6.99 x 10^23 (14.4%) |
| Ni | 8.57 x 10^22 (1.76%) | 8.18 x 10^22 (1.68%) | 7.71 x 10^22 (1.58%) |
| Ca | 7.81 x 10^22 (1.60%) | 8.77 x 10^22 (1.80%) | 8.99 x 10^22 (1.85%) |
| Al | 7.18 x 10^22 (1.48%) | 6.85 x 10^22 (1.41%) | 6.66 x 10^22 (1.37%) |
| S | 7.94 x 10^22 (1.63%) | 0 | 5.72 x 10^22 (1.18%) |
| Na | 6.9 x 10^21 (0.14%) | 4.04 x 10^22 (0.83%) | 4.1 x 10^21 (0.08%) |
| Cr | 1.97 x 10^22 (0.40%) | 0 (not listed) | 7.6 x 10^21 (0.16%) |
| K | 7.4 x 10^20 | 4.9 x 10^21 | 5.5 x 10^20 |

(Model oxide sums 99.6 to 100.1 wt%; core sums 99.5 to 100.0 wt%.)

**D3 Binding energy.** Uniform 3GM^2/5R = 1.568 x 10^32 J. Two-layer (Margot densities), U = integral of G m(r) dm / r over
200,000 shells = 1.725 x 10^32 J (ratio 1.100). Per kg mean 32.2 (uniform) and 35.4 MJ/kg (two-layer). Surface escape energy
GM/R = 53.68 MJ/kg (0.5 v_esc^2 = 53.66); ratio to Mercury's 9.0 MJ/kg = 5.96. Venus/Mercury binding (Mercury 1.79 x 10^30 J
uniform, given) = 88 (uniform) or 96 (two-layer against uniform).

**D4 Removal energy and power.** Sunlight intercepted by Venus = 2,601.3 x pi R^2 = 2.993 x 10^17 W. Atmosphere: 4.8 x 10^20 kg
x GM/R = 2.577 x 10^28 J; 31, 100, 1,000, 10,000 yr need 4.9 x 10^11, 1.52 x 10^11, 1.52 x 10^10, 1.52 x 10^9 kg/s and 88, 27.3,
2.73, 0.273 times the intercepted sunlight; 2,728 yr at 100% of it; 8.2 x 10^8 yr at 1 TW. Whole planet, 31 / 100 / 1,000 yr:
4.98 x 10^15 / 1.54 x 10^15 / 1.54 x 10^14 kg/s; 1.60 to 1.76 x 10^23 / 4.97 to 5.47 x 10^22 / 4.97 to 5.47 x 10^21 W (uniform to
two-layer); collector area at 2,601.3 W/m^2 and 100% = power/2,601.3 = 1.9 x 10^18 to 6.8 x 10^19 m^2; minimum time on Venus's
own intercepted sunlight 1.83 x 10^7 yr. No conversion losses are included; every real figure is larger.

**D5 Spin.** omega = 2 pi / (243.0226 d) = 2.9924 x 10^-7 rad/s; L = C omega = 1.787 to 1.799 x 10^31 kg m^2/s; AAM/L = 1.6 x 10^-3;
rotational energy 2.7 x 10^24 J; equatorial speed 1.811 m/s. Tangential launch of the atmosphere: dL = M_atm R v = 2.13 x 10^31
(7.33 km/s) or 3.01 x 10^31 (10.36 km/s), 1.18 or 1.67 L. New sidereal day = 2 pi C / |L +/- dL|: 111 or 91 d retrograde
(launch against rotation); 1,325 or 361 d prograde (launch with rotation). A 30-day day needs L = 1.458 x 10^32 (energy
1.77 x 10^26 J): v = (L_t - L)/(M_atm R) = 44.0 km/s, or 2.04 x 10^21 kg at 10.36 km/s. A 24-hour day: L = 4.373 x 10^33, energy
1.590 x 10^29 J, 6.95 x 10^22 kg (1.43% of M) at 10.36 km/s. Tidal relocking (constant phase lag, torque independent of rate):
684 Myr x (omega_now + omega_orbit)/(omega_3d - omega_orbit) = 684 x 6.229 x 10^-7 / 2.392 x 10^-5 = 17.8 Myr.

**D6 Chemistry.** Bosch: H/CO2 = 4 x 1.008/44.009 = 0.0916 kg/kg; 4.297 x 10^19 kg of H for 4.69 x 10^20 kg CO2 (61,000 times
7 x 10^14 kg); water 3.840 x 10^20 kg (27% of 1.4 x 10^21 kg; 834 m over 4.602 x 10^14 m^2); carbon 1.280 x 10^20 kg (2.8 x 10^5
kg/m^2). Solar wind (1.3 x 10^9 kg/s, H fraction taken as the photospheric 0.7438, given): 1,408 yr for that hydrogen.
Carbonates: MgO 0.916 kg/kg CO2 (4.30 x 10^20 kg); CaO 1.274 (5.98 x 10^20 kg); magnesite 8.99 x 10^20 kg / 3,000 kg/m^3 / area =
651 m; calcite 1.067 x 10^21 kg / 2,710.2 = 855 m. Basalt capacity = MgO% x 44.009/40.304 + CaO% x 44.009/56.077: Venera 13
0.180, Venera 14 0.169, Vega 2 0.184 kg CO2 per kg; rock 2.5 to 2.8 x 10^21 kg = 1.97 to 2.15 km global depth at 2,800 kg/m^3
(about 10% of a 20 km crust). Splitting all CO2: 4.69 x 10^20 kg / 0.044009 kg/mol x 282.98 kJ/mol = 3.02 x 10^27 J.

**D7 Cooling and shade.** Column 95 x 10^5 Pa / 8.88 = 1.070 x 10^6 kg/m^2; Birch's t = 935 kJ/kg x 95 x 10^5 / (160 x 8.88) =
6.25 x 10^9 s = 198 yr; heat removed 4.60 x 10^26 J; 160 W/m^2 over the sphere = 7.36 x 10^16 W. Shade 2.27 pi R^2 =
2.61 x 10^14 m^2 x 3 x 10^-4 = 7.8 x 10^10 kg. Pollack and Sagan's 1 um film over one disk at an assumed 1,000 kg/m^3 =
1.2 x 10^11 kg (their "~10^14 g").

**D8 Bared surface.** Subsolar T = (S(1 - A)/sigma)^0.25 = 450, 438, 423 K for A = 0.11, 0.2, 0.3; average (S(1 - A)/(4 sigma))^0.25 =
318, 309, 299 K. Half-space cooling q = k dT / sqrt(pi kappa t), dT = 435 K: k = 2, kappa = 0.7 mm^2/s gives 104, 33, 10.4, 3.3, 1.0 W/m^2 at
1, 10, 100, 1,000, 10,000 yr (k = 3, kappa = 1.0: 131, 41, 13, 4.1, 1.3); radiative floor (q/sigma)^0.25 = 207, 155, 116, 87, 65 K.
Depth cooled at least 100 K: z = 2 erfc^-1(100/435) sqrt(kappa t) = 8, 80, 798, 7,981 m at 1, 100, 10^4, 10^6 yr. Stress E alpha dT
with E = 1.371 x 10^7 T(C) + 2.6157 x 10^10 = 30.3 GPa (300 C), 31.6 GPa (400 C): 30 to 32 MPa per 100 K; 132 to 138 MPa for 435 K.
Unloading 92 x 10^5 Pa = 370 m of rock at 2,800 kg/m^3 and 8.87 m/s^2. Interior heat alone (10 to 30 mW/m^2) holds a surface at
only 20 to 27 K.

**D9 Natural escape.** (3 to 6) x 10^24 O+ /s with twice as many H: 0.090 to 0.179 kg/s; 4.8 x 10^20 kg / that = 0.85 to 1.7 x 10^14 yr.

**D10 Propellant.** v_e = Isp g0 (9.80665): 2.45, 2.78, 3.74 km/s for 250, 283, 381 s; mass ratio exp(dv/v_e) to 9 km/s 39.3, 25.6,
11.1; to 10.36 km/s 68.4, 41.8, 16.0.

**D11 Cross-checks.** 2 cm GEL x 1,000 kg/m^3 x area = 9.2 x 10^15 kg (Gillmann about 10^16); H in 10^16 kg water 1.12 x 10^15 kg;
S in 6 x 10^16 kg SO2 = 3.0 x 10^16 kg; N2 11 x 10^18 / 3.89 x 10^18 = 2.83. Cloud hydrogen 2 x 10^12 kg (VE) as water
1.8 x 10^13 kg = 0.04 mm global layer.

**D12 Carbonate stability.** log10 P_CO2 (bar) = 7.97 - 4456/T: 88.8 bar at 740 K, 80.8 at 735 K, 3.5 at 600 K, 1.0 at 559 K, 0.11 at
500 K, 6.8 x 10^-4 at 400 K. P = 1 bar at T = 4456/7.97 = 559 K.

## Constraints for any inhabitant

- **There is no shortcut through the gravity well:** 53.7 MJ per kg to leave from the surface, six times Mercury's, and every
  method of removing the atmosphere studied so far needs at least 2.6 x 10^28 J or thousands of large impactors (3.3, D4).
  Any operation that removes Venus's air or rock is energy-limited before it is machine-limited.
- **If the atmosphere were gone, the ground would not be livable either:** about 58 days of continuous sun at up to about
  450 K, 58-day nights falling toward the 100 to 200 K range in the first decades (set by stored crustal heat, D8), meteoroids
  arriving at 10 to 14 km/s with nothing to stop them, and radiation with no air column and no magnetic field (3.4).
- **A cooling crust cracks:** 30 MPa of thermal stress per 100 K of cooling against 12 to 21 MPa of strength, with the
  fractured layer deepening from meters to hundreds of meters over centuries (D8). Foundations on a bared or cooling Venus
  sit on jointed rock.
- **Venus's day is not fixed under industry:** the reaction from throwing its air off tangentially exceeds the planet's whole
  spin angular momentum, so a removal operation chooses a day length between about 90 days retrograde and about a year
  prograde unless it launches radially or balances directions (D5).
- **Hydrogen is the limiting element for any chemistry that turns the air into something solid and useful:** the Bosch route
  needs 61,000 times the hydrogen Venus has (D6); carbonate routes need about 2 km of crust ground and reacted and only hold
  below about 560 K (D6, D12).
- **Frozen CO2 is a permanent liability:** any sunshade-and-freeze scheme leaves about 90 bar of CO2 as ice or liquid that
  returns to the air if the shade or cover fails (Conflicts 4).
- **Material thrown off Venus does not simply go away:** launched near escape speed it stays on Venus-crossing orbits and much
  of it returns over millions of years unless it is sent somewhere or caught (3.5, Mercury analog).
- **Interior state is unknown:** core radius uncertain by more than 1,000 km and core state unknown (3.1); any plan that depends
  on what lies below the crust rests on models, not samples.

## Candidate handwaves (flagged, not accepted; the developer decides)

- **H-V1. Removing Venus's atmosphere on a human timescale.** Needs 27 times all the sunlight Venus intercepts, delivered as
  launch energy at 100% efficiency, to finish in a century (D4); no launcher of any kind has a Venus study.
- **H-V2. Dismantling Venus's solid body.** No published concept exists; 1.6 to 1.7 x 10^32 J and 1.5 x 10^14 kg/s for a
  1,000-year schedule (D3, D4); the material must also be kept from re-accreting (3.5).
- **H-V3. A habitable bared surface.** Requires solving 58-day thermal cycling, unshielded meteoroids and radiation, and a
  fractured cooling crust at once (3.4).
- **H-V4. Venus carbonate sequestration at planetary scale.** About 2.5 x 10^21 kg of rock ground and reacted (a 2 km global
  layer), and only after the surface is below about 560 K by some other means (D6, D12).
- **H-V5. Spin-up to a short day by atmosphere export.** A 30-day day needs about 44 km/s tangential launch speed for the
  atmosphere alone; 24 hours needs 1.4% of Venus's mass thrown at escape speed (D5). Nordley's version is fiction.
- **H-V6. Hydrogen import at the 10^19 kg scale.** About 1,400 years of the entire solar wind, perfectly captured (D6).

## Open threads

- **Fogg 1987 (JBIS 40, 551-564), Adelman 1982 (JBIS 35, 3-8), Smith 1989 (JBIS 42, 571-576), Birch 1993 (JBIS 46, 311-313,
  abstract only), Birch 1991 "Supramundane Planets" (JBIS 44, 169-182):** not open; the BIS shop sells them. The hydrogen
  figure and the Mercury Ca/Mg import (0.5% of Mercury's mass) trace to one of these.
- **Zubrin and McKay as named in the brief:** the 1993 Zubrin and McKay paper is a Mars paper (MVT 3.11); no Venus atmosphere
  removal study by them was found; Zubrin 1990 (NIMF propellants) is used here instead. A further search would target Zubrin's
  books (not primary).
- **Gladman et al. 1996 (Science 271, 1387):** the Venus ejecta fractions; not open. Would replace the Mercury analog in 3.5.
- **Correia and Laskar 2001/2003 and Ingersoll and Dobrovolskis 1978:** for a proper despinning timescale without thermal tides
  (the 18 Myr in D5 is a crude scaling).
- **Konopliv and Yoder 1996** (k2) and **Amorim and Gudkova 2023** (PREM-based structure): read only via citing papers.
- **Venus basalt thermal properties at 300 to 750 K** and a bare-surface albedo: no Venus measurement exists; D8 uses terrestrial
  values and a lunar albedo.
- **Whether carbonates exist on Venus** (Fegley 2004 lists arguments for and against): decides whether removal of the air would
  be followed by outgassing from the surface.
- **Decompression or unloading effects on volcanism** when 9.2 MPa is removed: no study found.
- **World mining throughput** as an anchor for the excavation rates in D4: not searched here (the Mercury inventory agent's
  checklist covers it; not read, per the rules).
- **Venus Express absolute ion escape rates** were read only through Gillmann 2022 (Barabash 2007 full text not open).

## Rejected sources

- **Wikipedia, "Terraforming of Venus":** used for leads only; its "4 x 10^19 kg of hydrogen" attribution to Birch 1991 is not
  supported by Birch's paper (Conflicts 5).
- **Search-engine summaries** giving "about 10^8 years" for tidal despinning, Venus ejecta fractions (30% to Earth, 12 Myr,
  over 80% reaccreted in 10^5 yr), ion escape "1 x 10^25 and 1.6 x 10^25 s^-1", and crust "20-25 km": not traced to a page opened.
- **A blog value of 2.6 x 10^32 J for Venus's binding energy** (energymatters.com.au, via search): unsourced; D3 gives 1.6 to
  1.7 x 10^32 J.
- **Forum and mailing-list pages on planetary dismantlement** (extropians archive, newmars, Kerbal forum, OrionsArm): not
  engineering sources.
- **Forum and blog Isp figures for CO2 (226 s, 260 s):** superseded by Zubrin's NTRS paper.
- **Mostafa et al. 2004 basalt conductivity:** abstract only, no per-temperature data; used only in Conflicts 7.
- **NTRS 19930059709** (returned for "How to spin a planet"): a different paper (planetary spin origin by accretion), not used.
