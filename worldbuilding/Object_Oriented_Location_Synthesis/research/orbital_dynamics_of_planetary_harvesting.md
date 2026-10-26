# Orbital dynamics of planetary harvesting (Mercury and Venus)

*Research file, tranche 8, section 5. Complete as of 2026-10-12. Started 2026-10-11 (interrupted by a session limit after S3; resumed the same evening and finished
2026-10-12). Physics and engineering only; no setting, story or timeline is assumed. Evidence words: **DEMONSTRATED** (observed or flown),
**ENGINEERING-STUDIED** (a published quantitative study or design), **SPECULATIVE** (a thought experiment or concept), **DERIVED** (my
arithmetic from sourced constants; scripts and raw output in the scratch folder `orbital_dynamics_of_planetary_harvesting/`, named in
section 5). Cited siblings, read-only: **[MS]** `inner_system_mining_synthesis.md`, **[SYN]** `starlifting_synthesis.md`, **[NW]**
`inner_system_logistics_network.md`.*

## 1. Scope

What removing mass from **Mercury** or **Venus** (rock, metal or Venus's atmosphere) does dynamically: (a) to the planet's own orbit, spin
and interior loading; (b) to the other planets through secular (long-period) perturbations, including Earth's eccentricity cycles and
Mercury's known chaotic instability; (c) to the launched material, collectors and catchers near 0.39 and 0.72 AU (radiation forces,
Lagrange points, debris, delivery to Earth); and (d) using the removed mass as reaction mass to move or spin a planet.

## 2. SEARCH LOG

**Totals (2026-10-12):** 35 web searches (S-rows; S3 counted once though run twice), 43 pages or papers opened (F-rows), 4 calculation
runs (C-rows). Dead ends: 3 died at the source (F6 Nature paywall, F12 A&A 403, F39 TLS error; all three had an open copy or a substitute),
2 at the query (S3 tool error, re-run as S3r; S11 query built on a recalled figure), 3 at the sources (S7 no Venus-removal study exists
in what surfaced; S17 the Venus-to-Earth 30% figure could not be opened at its primary; S24 the "700,000-yr naked Venus" figure was not
on any page). Four queries were seeded with recalled numbers (S6, S11, S13, S22); each number was replaced by the opened source's value or
dropped, and S13's recalled coefficient was wrong by a factor of ten.

| # | Date | Search string (verbatim) or page opened | Result | Note |
|---|---|---|---|---|
| P1 | 2026-10-11 | Read sibling files (read-only, permitted): `_BRIEF.md`, `inner_system_mining_synthesis.md`, `starlifting_synthesis.md`, `inner_system_logistics_network.md` F4 (Mercury launcher direction, Hill sphere 221,000 km DERIVED), `cyclers_and_large_slow_vehicles.md` E, `lagrange_eclipse_calculation.md` §3-4 | useful | Cited, not re-derived. Mercury launcher direction already covered in [NW] F4. |
| F1 | 2026-10-11 | https://nssdc.gsfc.nasa.gov/planetary/factsheet/mercuryfact.html (updated 11 Jan 2024) | useful | Mass 0.33010e24 kg; GM 0.022032e6 km^3/s^2; R 2439.7 km; a 57.909e6 km; P 87.969 d; v mean 47.36, max 58.97, min 38.86 km/s; e 0.2056; i 7.004 deg; sidereal rotation 1407.6 h; day 4222.6 h; perihelion 46.000e6, aphelion 69.818e6 km; I/MR^2 0.35; J2 50.3e-6; escape 4.3 km/s; g 3.70 m/s^2; density 5429 kg/m^3. |
| F2 | 2026-10-11 | https://nssdc.gsfc.nasa.gov/planetary/factsheet/venusfact.html (updated 11 Jan 2024) | useful | Mass 4.8673e24 kg; GM 0.32486e6 km^3/s^2; R 6051.8 km; a 108.210e6 km; P 224.701 d; v 35.02 km/s; e 0.0068; i 3.395 deg; sidereal rotation -5832.6 h; day 2802.0 h; I/MR^2 0.337; J2 4.458e-6; escape 10.36 km/s; g 8.87; atmosphere ~4.8e20 kg; 92 bar; surface wind 0.3 to 1.0 m/s. |
| F3 | 2026-10-11 | https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html (updated 9 May 2024) | useful | Sun mass 1,988,400e24 kg; GM 132,712e6 km^3/s^2. |
| F4 | 2026-10-11 | https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html (updated 15 Nov 2024) | useful | Earth mass 5.9722e24 kg; GM 0.39860e6; a 149.598e6 km; P 365.256 d; v 29.78 km/s; e 0.0167. |
| S1 | 2026-10-11 | `Laskar Gastineau 2009 Nature existence of collisional trajectories of Mercury Mars Venus with the Earth 1% probability` | useful | Leads: IMCCE press page, RePEc record. |
| F5 | 2026-10-11 | https://perso.imcce.fr/jacques-laskar/obs-press-colli/colli.en.shtml (IMCCE press note, 2009) | useful (secondary, author's own press page) | "over 2500 trajectories"; "in about 1% of the cases ... collisions ... in less than 5 billion years"; "complete destabilization of the inner Solar System ... in 3.4 Gyr" (one solution); model includes general relativity. No g1-g5 statement on the page. |
| F6 | 2026-10-11 | https://www.nature.com/articles/nature08096 | dead at the source (paywall redirect to login) | Not read. |
| S2 | 2026-10-11 | `Laskar Gastineau "Existence of collisional trajectories" arXiv abstract 2501 orbits general relativity Mercury eccentricity` | thin | No arXiv copy surfaced; RePEc record only. |
| F7 | 2026-10-11 | https://ideas.repec.org/a/nat/nature/v459y2009i7248d10.1038_nature08096.html (Nature 459, 817-819, June 2009, record) | useful | Summary text: "2,501 solutions ... over a 5-billion-year period ... 1% of the solutions lead to a large increase in Mercury's eccentricity, sufficient to allow collisions with Venus or the Sun ... destabilizes all the terrestrial planets after about 3.34 billion years". |
| S3 | 2026-10-11 | `solar system stability numerical experiment remove Mercury inner planets chaos "without Mercury"` | dead at the query (tool error: session limit reached mid-run) | To be re-run. |
| C1 | 2026-10-11 | (resumed session) ran `calc1.py` from the scratch subfolder; output saved as `calc1_out.txt` | useful | Arithmetic for checklist items 1, 3, 4, 6 (Derived figures). |
| S3r | 2026-10-11 | `solar system stability numerical experiment remove Mercury inner planets chaos "without Mercury"` (re-run) | thin | No study removing Mercury or Venus surfaced. Leads: Laskar "Chaos in the Solar System" (astro-ph/0111600), "Long-term dynamics of the solar system inner planets" (arXiv 2105.14976), Batygin, Morbidelli & Holman 2015 "Chaotic disintegration of the inner Solar System" (arXiv 1411.5066), Zeebe 2015. |
| S4 | 2026-10-11 | `Lithwick Wu 2011 theory of secular chaos Mercury g1 g5 resonance` | useful (leads) | Leads: Boue, Laskar & Farago 2012 A&A "simple model of the chaotic eccentricity of Mercury" (arXiv 1210.5221); Lithwick & Wu 2014 PNAS (arXiv 1311.1214); Mogavero & Laskar subdiffusion (arXiv 2306.11870). |
| S5 | 2026-10-11 | `Earth eccentricity 405,000 year cycle g2-g5 Venus Jupiter secular frequencies Laskar 2004` | useful (leads) | Leads: La2010 (arXiv 1103.1084); Kane, Vervoort & Horner 2025 Mars-mass study; g2-g5 disruption paper (arXiv 2403.09332). |
| F8 | 2026-10-11 | https://arxiv.org/html/2512.02108v2 (Kane, Vervoort & Horner, "The Dependence of Earth Milankovitch Cycles on Martian Mass", preprint 4 Dec 2025; PASP 137, 124402 per the USQ repository link) | useful | Nearest published analog of a planet-mass change: Mars mass varied 0 to 200% in 10% steps plus 1000%; 22 runs, 10^8 yr, 1-day step, Mercury hybrid integrator. 405 kyr cycle "persists at all Mars masses"; it is "driven by g2 (Venus) and g5 (Jupiter)"; 2.4 Myr cycle "absent when Mars approaches zero mass"; at 200% "~1.4 Myr". |
| F9 | 2026-10-11 | https://www.soest.hawaii.edu/oceanography/faculty/zeebe_files/Publications/ZeebeApJ15.pdf (Zeebe, "Dynamic stability of the Solar System: statistically inconclusive results from ensemble integrations", ApJ 798:8, 2015) | useful | Mercury eccentricity rise is associated with g1 shifting toward g5; GR "move[s] g1 up (by ~0.43"/yr at present) and away from the (g1-g5) resonance"; "currently assumed likelihood of ~1%" of large eM rise in 5 Gyr; P(eM rises above 0.53 in 500 Myr) 40-55% (heliocentric) vs >90% (Jacobi); Lyapunov times 3.2 and ~6 Myr (2.8 and 5.5 Myr from separation of nearby orbits); a 2.73 m offset in Mercury's initial distance is the perturbation used. Masses in solar masses: Mercury 1.66013679527193035E-07, Venus 2.44783833966454472E-06. |
| F10 | 2026-10-11 | https://arxiv.org/abs/0802.3371 (Laskar, "Chaotic diffusion in the Solar System", Icarus 2008, abstract) | useful | "the probability of the eccentricity of Mercury to reach 0.6 in 5 Gyr is about 1 to 2%"; 1,001 secular integrations; more high-e orbits without GR; two direct integrations reach e > 0.8 in 1.3 and 2.8 Gyr; cause: secular resonance between Jupiter's and Mercury's perihelia. |
| S6 | 2026-10-11 | `Mercury perihelion precession contributions by planet Venus 277 arcsec per century Jupiter 153 Earth 90 Clemence 1947` | useful (leads) | Summary quoted Venus 278, Jupiter 153, Earth 90"/cy, Newtonian total ~531"/cy (Clemence 1947); summary not used as a number. Lead to Fitzpatrick's text. |
| F11 | 2026-10-11 | https://farside.ph.utexas.edu/teaching/celestial/Celestial/node134.html (R. Fitzpatrick, *Newtonian Dynamics*, UT Austin lecture text, Table B.1, undated web edition) | useful (textbook, secular theory) | Contributions to Mercury's perihelion precession ("/yr): Venus 2.7745, Earth 0.9084, Mars 0.0248, Jupiter 1.5400, Saturn 0.0731, Uranus 0.0014, Neptune 0.0004; total 5.3226. Venus supplies 52% of it. |
| S7 | 2026-10-11 | `N-body simulation Earth orbit eccentricity obliquity if Venus were removed OR "without Venus" Milankovitch` | thin | **No study removing or reducing Venus found** (died at the sources: the literature varies Jupiter's orbit, Horner et al. 2019/2020, and Mars's mass, Kane et al. 2025). Leads: Horner et al. arXiv 1910.14250; Horner et al. arXiv 1401.6741. |
| S8 | 2026-10-11 | `Laskar 1990 secular frequencies g1 5.59 g2 7.45 g5 4.257 arcsec/yr table fundamental frequencies solar system` | useful (leads) | Summary gave La2004/Laskar 2011 table values; not used as numbers until opened (F13). |
| F12 | 2026-10-11 | https://www.aanda.org/articles/aa/full/2004/46/aa1335/table3.html (Laskar et al. 2004 Table 3) | dead at the source (HTTP 403) | Not read. |
| F13 | 2026-10-11 | https://arxiv.org/pdf/2106.00584 (Hoang, Mogavero & Laskar, "Chaotic diffusion of the fundamental frequencies in the Solar System", A&A, arXiv v2 20 Feb 2023), Table 2, downloaded and read | useful | Centers of the long-term frequency distributions ("/yr): g1 5.759, g2 7.448, g3 17.269, g4 17.896, g5 4.257454, g6 28.245226, g7 3.087957, g8 0.673024; s1 -5.652, s2 -6.709, s3 -18.773, s4 -17.707, s6 -26.347866, s7 -2.992527, s8 -0.691737. |
| F14 | 2026-10-11 | https://arxiv.org/abs/1910.14250 (Horner, Vervoort, Kane et al., "Quantifying the Influence of Jupiter on the Earth's Orbital Cycles", AJ 2019/2020, abstract page) | thin (abstract only) | Varied Jupiter's orbit with the others fixed; "Earth's modern orbital cycles fall in the middle of the range seen in our runs". No numbers used. Shows the method exists; no Venus-mass analog. |
| F15 | 2026-10-11 | https://nssdc.gsfc.nasa.gov/planetary/factsheet/ (NSSDC Planetary Fact Sheet, updated 18 Mar 2025) | useful | Mass (10^24 kg) 0.330/4.87/5.97/0.642/1898/568/86.8/102; distance (10^6 km) 57.9/108.2/149.6/228.0/778.5/1432.0/2867.0/4515.0; e 0.206/0.007/0.017/0.094/0.049/0.052/0.047/0.010. Used only as a cross-check of F16. |
| F16 | 2026-10-11 | https://ssd.jpl.nasa.gov/planets/approx_pos.html (Standish & Williams, JPL "Approximate Positions of the Planets", Table 1, J2000 ecliptic, valid 1800-2050) | useful | a (au), e, I, long. perihelion, long. node for all eight planets; inputs to calc3. Mercury 0.38709927 au, e 0.20563593; Venus 0.72333566, 0.00677672; EM bary 1.00000261, 0.01671123; Jupiter 5.20288700, 0.04838624 (rest in calc3 header). |
| C2 | 2026-10-11 | Wrote and ran `calc2_secular.py` (Laplace-Lagrange, summary-sheet a), then `calc3_secular_amplitudes.py` (same with F16 elements and mode amplitudes) | useful | Validation: LL g1 5.875 (Laskar 5.59 present / 5.759 center), g2 7.427 (7.448-7.452), g3/g4 17.38/18.04 (17.27/17.90); LL g5 3.732 vs 4.257 and g6 22.5 vs 28.2 (known LL failure for Jupiter-Saturn near the 5:2 commensurability; stated in Conflicts). GR adds 42.98"/cy to Mercury in the script (Zeebe: ~0.43"/yr). Venus-on-Mercury diagonal term 2.863"/yr vs Fitzpatrick 2.7745 (3% apart). calc2's last loop crashed on a labeling bug; superseded by calc3. |
| C3 | 2026-10-11 | Wrote and ran `calc4_sweep.py` (resonance passage of g1 through g5 as Venus's mass falls) | useful | Derived figures D5. |
| S9 | 2026-10-11 | `sweeping secular resonance eccentricity excitation depends on sweep rate Ward 1981 scanning secular resonance theory formula Δe` | useful (leads) | Leads: Heppenheimer 1980 and Ward 1981 ("scanning secular resonance theory"); Minton & Malhotra 2011. |
| S10 | 2026-10-11 | `Minton Malhotra 2011 secular resonance sweeping asteroid belt eccentricity excitation analytical "sweep rate"` | useful | arXiv 1102.3131 opened (F17). |
| F17 | 2026-10-11 | https://arxiv.org/pdf/1102.3131 (Minton & Malhotra, "Secular resonance sweeping of the main asteroid belt during planet migration", ApJ 732:53, 2011), downloaded and read pp. 9-10, 19 | useful | Eq. 32-33: e_min,max = abs(e_i +/- delta_e), delta_e = eps sqrt(pi/abs(lambda)) / sqrt(a); "the magnitude of eccentricity change is inversely related to the speed of planet migration"; sweeping can excite or damp depending on phase; an initially circular orbit ends with e = delta_e; Saturn migration slower than ~0.15 AU/Myr would have pushed inner-belt asteroids to planet-crossing e. |
| S11 | 2026-10-11 | `NASA Earth orbit eccentricity varies between 0.0034 and 0.058 Milankovitch cycles` | thin | The 0.0034-0.058 figure in my query was not found on any page (a query built on a recalled number; dropped). |
| F18 | 2026-10-11 | https://science.nasa.gov/science-research/earth-science/milankovitch-orbital-cycles-and-their-role-in-earths-climate/ (NASA Science editorial team, 27 Feb 2020) | thin (secondary) | Eccentricity cycle "about 100,000 years"; obliquity 22.1 to 24.5 deg, ~41,000 yr; axial precession ~25,771.5 yr, climatic ~23,000 yr. No eccentricity range given. |
| S12 | 2026-10-11 | `Earth orbital eccentricity range over past 250 Myr minimum maximum value La2004 La2010 numerical solution "eccentricity of the Earth" ranges` (extended mode) | thin | Summary: "between almost zero and about 0.06" and the 405 kyr cycle "the only relatively stable metronome over at least the past 250 million years" (La2010, A&A 532 A89). Not confirmed on the page; used only as a low-confidence check of calc3's 0 to 0.065. |
| S13 | 2026-10-11 | `Burns Lamy Soter 1979 radiation forces on small particles in the solar system beta = 5.7e-4 Q_pr / (rho s) Poynting-Robertson lifetime formula` | useful | **My query's coefficient (5.7e-4) was wrong; the paper gives 5.7e-5** (F19). A recalled constant caught by opening the source. |
| F19 | 2026-10-11 | https://www.kwasan.kyoto-u.ac.jp/~isobe/tmp/dust/1-s2.0-0019103579900502-main.pdf (Burns, Lamy & Soter, "Radiation forces on small particles in the solar system", Icarus 40, 1-48, 1979; university-hosted copy of the publisher PDF), read eq. 19, 50 and pp. 15-16, 29 | useful | beta = F_r/F_g = (3L/16 pi G M c)(Q_pr/rho s) = 5.7 x 10^-5 Q_pr/(rho s) (cgs); S0 = 1.36 x 10^6 erg cm^-2 s^-1; beta independent of distance; particles released from circular orbits "need only have beta = 1/2" to be hyperbolic; t_PR = a^2/4 eta Q_pr = 7.0 x 10^6 s rho R^2/Q_pr yr = 400 R^2/beta yr (R in AU, s in cm, rho in g/cm^3); solar-wind drag about 0.1 of PR drag for grains above about 1 micron (their Fig. 11, obsidian at 1 AU). |
| S14 | 2026-10-11 | `Mercury circumsolar dust ring STEREO Stenborg 2018 density enhancement; Venus dust ring Jones 2013 Helios Parker Solar Probe` | useful (leads; secondary summaries) | Mercury ring: brightness excess 1.5-2.5% over the F-corona, excess density about 3-5% (Stenborg et al. 2018 ApJ); Venus ring: about 10% density enhancement (Jones et al. 2013 Science, 2017). Not yet confirmed on primary pages; see S16. |
| S15 | 2026-10-11 | `Gladman Coffey 2009 Mercurian impact ejecta meteorites fraction reaching Earth Venus Sun percent` | useful | arXiv 0801.4038 opened (F20). |
| F20 | 2026-10-11 | https://arxiv.org/pdf/0801.4038 (Gladman & Coffey, "Mercurian impact ejecta: meteorites and mantle", Meteoritics & Planetary Science 44(2) 285-291, 2009; preprint read in full for the results) | useful | Material leaving Mercury: 2-5% reaches Earth in 30 Myr ("several percent", 2-3x less than from Mars); 0.7% in 30 Myr at v_inf 4 km/s; ~0.6%/10 Myr at 9 km/s; Venus takes 20% in 30 Myr (13% and 8% at v_inf 20 and 25 km/s); at v_inf = v_esc = 4 km/s "fully half of the ejecta" is re-accreted by Mercury in 30 Myr, "about one third ... in as little as 2 Myr"; at high speeds ~25% returns; ~2/3 of 20-25 km/s ejecta still in space after 30 Myr. PR spiral time 7 Myr (rho/1 g cc)(r/1 cm)(a/1 AU)^2/Q_pr; a 10 cm, 3 g/cc meteoroid at a 0.7 AU, e 0.5: ~70 Myr. Escape speed 4.2 km/s. |
| S16 | 2026-10-11 | `Venus ejecta transfer to Earth fraction impact rate numerical simulation Gladman 1996 Science "transfer of material between planets"` | useful (leads) | Summary said ~30% of Venus ejecta reaches Earth, median 12 Myr (attributed via a review to Gladman et al. 1996); not used until confirmed (F22). |
| F21 | 2026-10-11 | https://www.news.cornell.edu/stories/1996/03/planetary-material-shared-throughout-inner-solar-system (Cornell news, March 1996) | thin (secondary) | "Less than 1 percent of particles launched from Mercury can find their way to Earth" (the 1996 estimate, superseded by F20). No Venus number. Cites Gladman, Burns, Duncan, Lee & Levison, Science 8 Mar 1996. |
| S17 | 2026-10-11 | `"Venus" ejecta "falls on the Earth" OR "reach Earth" median 12 Myr reaccreted by Venus percent Gladman Burns Duncan Lee Levison 1996` (extended) | thin | Science 271:1387 is paywalled (died at the source); the 30% / 12 Myr figure traced only to a secondary review summary. Lead: Cabot & Laughlin 2020. |
| F22 | 2026-10-11 | https://arxiv.org/pdf/2010.02215 (Cabot & Laughlin, "Lunar exploration as a probe of ancient Venus", PSJ 2020), read sect. 4.1-4.2 | useful | Venus-to-Earth transfer 10% (their Sim. 1, 10 Myr; about 40% still in orbit, so a lower bound); Melosh & Tonks 1993 give ~30% (difference attributed to start conditions and method); in 1 Myr: Moon 0.03%, Earth 4.48%, re-accreted by Venus 34.71%; ejecta v_inf of order 7 km/s; prograde ejecta reach a ~1.3 AU. |
| S18 | 2026-10-11 | `Tabachnik Evans 2000 asteroids in the inner solar system existence long-lived stable orbits Mercury Venus Earth Mars Trojans` | useful | Leads: arXiv astro-ph/0005400; Earth-Trojan stability arXiv 1812.01244. |
| F23 | 2026-10-11 | https://arxiv.org/abs/astro-ph/0005400 (Tabachnik & Evans, "Asteroids in the inner Solar System I - Existence", MNRAS 2000, abstract) | useful | Integrations to 100 Myr with the Sun and 8 planets: "Mercury is the least likely planet, as it is unable to retain tadpole orbits over 100 million year timespans" (search summary adds: long-lived co-rotating horseshoe orbits at small inclination); Venus survey 25 Myr, ~40% of survivors tadpoles, "only test particles close to the orbital plane are stable"; Earth: stable bands at i < 16 deg and 24-34 deg. |
| S19 | 2026-10-11 | `Venus co-orbital asteroids source of Venus dust ring Pokorny Kuchner 2019 stability 4.5 Gyr` | useful | Leads: Pokorny & Kuchner 2019 ApJL 873 L16 (arXiv 1904.12404); Xu et al. 2022 A&A 666 A88 (arXiv 2206.06114). |
| F24 | 2026-10-11 | https://arxiv.org/abs/1904.12404v1 (Pokorny & Kuchner, "Co-orbital asteroids as the source of Venus's zodiacal dust ring", ApJL 873:L16, 2019, abstract) | useful | 10,000,000+ dust particles modeled; only a hypothetical Venus co-orbital asteroid population reproduces the ring; ~8% of 1:1-resonant asteroids survive 4.5 Gyr. |
| F25 | 2026-10-11 | https://www.nasa.gov/solar-system/what-scientists-found-after-sifting-through-dust-in-the-solar-system/ (NASA, March 2019) | useful (agency news; secondary for the numbers) | Mercury ring "9.3 million miles wide", ~5% brightness/density increase (Stenborg & Howard, ApJ 21 Nov 2018); Venus ring ~16 million miles top to bottom, 6 million miles wide, ~10% denser; "about 800" of 10,000 test asteroids survived 4.5 Gyr. |
| F26 | 2026-10-11 | https://arxiv.org/abs/2206.06114 (Xu, Zhou, Lhotka, Zhou & Ip, "Trojan asteroids and co-orbital dust ring of Venus", A&A 666 A88, 2022, abstract) | useful | "Venus Trojans have poor orbital stability and cannot survive the age of the Solar system"; most stable on low-inclination, low-e horseshoe orbits; "The Yarkovsky effect may drive nearly all Venus Trojans out of the Trojan region in a relatively short time"; GR minor. **Conflicts with F24** (Conflicts section). |
| S20 | 2026-10-11 | `Margot 2021 Nature Astronomy spin state and moment of inertia of Venus length of day variations 61 ppm atmospheric angular momentum` | useful | arXiv 2103.01504 opened (F27). |
| F27 | 2026-10-11 | https://arxiv.org/pdf/2103.01504 (Margot et al., "Spin state and moment of inertia of Venus", Nature Astronomy, 29 Apr 2021; preprint read pp. 1-9, Table 2) | useful | Sidereal day 243.0226 +/- 0.0013 d; obliquity 2.6392 deg; C/MR^2 0.337 +/- 0.024; C = 5.972 (LS) / 6.013 (bootstrap) x 10^37 kg m^2; LOD variations 61 ppm (~20-21 min); atmospheric angular momentum L ~ 2.9 x 10^28 kg m^2/s +/- 30%; full transfer would change P by ~ -9.4 h; "4-day atmospheric superrotation"; torques ~1.9 x 10^21 N m inferred from day-to-day changes; solid-body solar tides "would synchronize the spin of Venus to its 225-day orbital period" absent the atmospheric thermal-tide torque (Gold & Soter mechanism). |
| S21 | 2026-10-11 | `Correia Laskar 2001 Nature four final rotation states of Venus atmospheric thermal tides core-mantle friction` | useful (leads) | Correia & Laskar 2001 Nature 411: four final rotation states; atmospheric tides, core-mantle friction and obliquity control the end state. Abstract-level only. |
| S22 | 2026-10-11 | `Mercury 3:2 spin-orbit resonance libration amplitude 38.5 arcsec (B-A)/C free libration period 12 years Margot 2012 moment of inertia` | thin | Libration amplitude 38.5 +/- 1.6" (Margot et al. 2012), 455 +/- 19 m at the equator (summary). No (B-A)/C or free-libration period surfaced; query part built on a recalled "12 years", not used. |
| F28 | 2026-10-11 | https://arxiv.org/pdf/1710.09686 (Stark et al., "The reference frames of Mercury after MESSENGER", 2017/2018), Table read | useful | Libration amplitude 38.5 +/- 1.6" (Margot et al. 2012, radar) and 38.9 +/- 1.3" (Stark et al. 2015b, MESSENGER); rotation rate 6.138506839 deg/d. |
| S23 | 2026-10-11 | `Venus solid body tidal torque despinning timescale without atmosphere synchronous rotation time scale Myr Leconte 2015 Science asynchronous rotation atmospheric tides` | thin (leads) | Summary claimed a "naked Venus" would invert in ~700,000 yr (gamma ~2e-7 /s) and synchronize in ~1 Myr, source unclear; not used. |
| F29 | 2026-10-11 | https://arxiv.org/pdf/1709.09478 (Auclair-Desrotour, Laskar & Mathis, EAS 2017) and https://arxiv.org/pdf/1709.10148 (Auclair-Desrotour et al., A&A 2017) | thin | Mechanism stated (solid tides drive synchronization, thermal tides push away); no naked-Venus time scale in either. |
| S24 | 2026-10-11 | `"Venus" rotation "would become prograde" without atmosphere solid tides inversion 700 000 years relaxation γ Correia Laskar` (extended) | dead at the sources | The 700,000-yr figure was not found on any page opened; dropped. |
| F30 | 2026-10-11 | https://arxiv.org/pdf/1611.05678 (Auclair-Desrotour, Laskar, Mathis & Correia, A&A 2017) | thin | Theory of the four equilibria; no naked-Venus time. |
| S25 | 2026-10-11 | `Revol 2023 "Spin evolution of Venus-like planets subjected to gravitational and thermal tides" arXiv` | useful | arXiv 2303.00084 opened (F31). A&A html returned 403. |
| F31 | 2026-10-11 | https://arxiv.org/pdf/2303.00084 (Revol et al., "Spin evolution of Venus-like planets subjected to gravitational and thermal tides", A&A 2023), sect. 3.2 read | useful | Solid tides only, Venus-like multilayer interior, initial 100-day rotation, inclination 5 deg: "the tides act to synchronize the rotation of the planet in 5.5 x 10^7 years"; at 50 and 120 deg inclination capture in the 2:1 spin-orbit resonance for a few 10^7 yr. With thermal tides and an evolving Sun, "Venus may never reach a spin equilibrium state". |
| S26 | 2026-10-11 | `Mercury gravity field C22 J2 (B-A)/C value MESSENGER Mazarico 2014 Genova 2019 libration Cm/C 0.431 C/MR2 0.346` | useful (leads) | Summary: C/MR^2 0.346 +/- 0.014, Cm/C 0.431 +/- 0.025 (Margot et al. 2012), Genova et al. 2019 C/MR^2 0.333 +/- 0.005, normalized C22 1.24973e-5. Only the C22 used, after opening F33. |
| S27 | 2026-10-11 | `Correia Laskar 2004 Nature Mercury's capture into the 3/2 spin-orbit resonance as a result of its chaotic dynamics probability 55.4%` | useful (abstract-level, RePEc/Nature record via summary) | Capture into 3:2 the most probable outcome, 55.4% of 1,000 orbits over 4 Gyr, because chaotic e can exceed 0.325; Nature 429:848-850 (2004). Record only; no number used in derived work. |
| F32 | 2026-10-11 | https://arxiv.org/pdf/astro-ph/0507117 (Peale, "The free precession and libration of Mercury", 2005 preprint), pp. 1-4 | useful | Eq. 2: phi0 = (3/2)(B-A)/Cm (1 - 11e^2 + 959/48 e^4); eq. 3: (B-A)/(M R^2) = 4 C22; free libration in longitude ~10 yr ("9.2 year period, for (B-A)/Cm = 3.5 x 10^-4"); free precession O(1000 yr); free wobble O(500 yr); core-mantle damping O(10^5 yr). |
| F33 | 2026-10-11 | https://arxiv.org/pdf/1608.01360 (Verma & Margot, "Mercury's gravity, tides, and spin from MESSENGER radio science data", JGR-Planets 2016 preprint) | useful | C2,0 = -5.033 x 10^-5, C2,2 = 8.067 x 10^-6 (unnormalized); normalized C22 1.24973 x 10^-5 (HgM005); k2 = 0.464 +/- 0.023 (Mazarico et al. 2014: 0.451 +/- 0.014). |
| S28 | 2026-10-11 | `Jull McKenzie 1996 deglaciation Iceland decompression melting eruption rate increase 30 times postglacial unloading volcanism` | useful | Lead to Eksinchol, Rudge & Maclennan 2019 (F34). |
| F34 | 2026-10-11 | https://arxiv.org/pdf/1902.00697 (Eksinchol, Rudge & Maclennan, "Rate of melt ascent beneath Iceland from the magmatic response to deglaciation", G-cubed 2019 preprint) | useful (analog only) | Eruption rates rose "5-30 fold" over steady state during the last deglaciation; Jull & McKenzie (1996) rebound raised the upper-mantle decompression rate "by up to 50-fold"; ice load modeled as 2 km (Jull & McKenzie) or 1.39 km average over a 300 km radius; ice density 830-917 kg/m^3; melt ascent >= 50 m/yr. |
| S29 | 2026-10-11 | `Korycansky Laughlin Adams 2001 astronomical engineering strategy for modifying planetary orbits Earth asteroid flyby energy numbers` | useful | arXiv astro-ph/0102126 opened (F35). |
| F35 | 2026-10-11 | https://arxiv.org/pdf/astro-ph/0102126 (Korycansky, Laughlin & Adams, "Astronomical engineering: a strategy for modifying planetary orbits", Ap&SS 275:349-366, 2001) | useful | Earth's orbital energy -2.7 x 10^40 erg; moving Earth to a circular 1.5 AU orbit needs 8.7 x 10^39 erg (8.7 x 10^32 J); grazing flyby transfers 2.4 x 10^12 erg per g of flyby body (Niehoff 1966); one 10^22 g encounter about every 6,000 yr. (SPECULATIVE concept, quantitative.) |
| S30 | 2026-10-11 | `Birch 1991 "Terraforming Venus quickly" JBIS soletta mass drivers spin up Venus atmosphere removal` | thin | Only secondary summaries (Universe Today, phys.org): Birch 1991 sunshade at L1, freeze the CO2; Nordley 1991 short story spins Venus to a 30-day day by exporting its atmosphere via mass drivers (**fiction; rejected as a source**). JBIS paper not opened (paywalled shop). |
| S31 | 2026-10-11 | `McInnes 2002 astronomical engineering revisited planetary orbit modification using solar radiation pressure Acta Astronautica` | useful | Corrects my query: published in Ap&SS 282:765-772 (2002), not Acta Astronautica. |
| F36 | 2026-10-11 | https://strathprints.strath.ac.uk/6236/ (McInnes, "Astronautical engineering revisited: planetary orbit modification using solar radiation pressure", Ap&SS 2002, abstract) | useful (abstract only; full text not in the repository) | A sail held in static equilibrium relative to the planet slowly accelerates the planet-sail system; sail mass "four orders of magnitude less" than the mass processed in the flyby scheme; time scale of order 10^9 yr. |
| S32 | 2026-10-11 | `spin up Venus rotation mass drivers energy required angular momentum terraforming Fogg Birch "spin" Venus day length paper` | thin (forums only) | Forum claim "~2 x 10^29 J" for a 24-h Venus day and "even if we expel every atom of air, we just can't get to a Venusian 24 hour day" - recorded as a lead, checked by my own arithmetic (D9), not cited. |
| S33 | 2026-10-11 | `Dyson swarm collisional cascade Kessler syndrome orbital debris stability of a swarm of collectors around the Sun paper` | useful | Lacki 2025 (F37). |
| F37 | 2026-10-11 | https://arxiv.org/abs/2504.21151 (Lacki, "Ground to dust: collisional cascades and the fate of Kardashev II megaswarms", ApJ 985:191, 2025, abstract) | useful | "The collisional time is roughly an orbital period divided by the covering fraction of the swarm"; structuring orbits does not prolong the first collision time if randomness remains; cascades "can develop extremely rapidly for hypervelocity collisions"; planetary perturbations (Lidov-Kozai) can cross orbits within millions of years; Yarkovsky destabilizes; megaswarms short-lived "without active upkeep". |
| S34 | 2026-10-11 | `Sun-Earth L1 halo orbit station keeping delta-v per year SOHO ACE meters per second` | useful | Lead to NTRS 20110008638 (F38). Summary's "just over 2 m/s per year for SOHO" not confirmed on the page opened (which says SOHO much less than 1 m/s); not used. |
| F38 | 2026-10-11 | https://ntrs.nasa.gov/citations/20110008638 (Roberts, "Long term missions at the Sun-Earth libration point L1: ACE, SOHO, and WIND", AI Solutions for NASA GSFC, 2011) | useful | "Typical annual stationkeeping costs have been around 1.0 m/sec for ACE and WIND, and much less than that for SOHO"; burns about every three months, each much less than 0.5 m/s; cost "doubling time constant is approximately 16 days". **Cross-check of calc1: Earth L1 e-folding 22.95 d = doubling 15.9 d.** |
| S35 | 2026-10-11 | `total mass of the zodiacal cloud kg Nesvorny 2010 or Fixsen Dwek 2002 estimate 10^16 kg mass input rate` | useful | Lead to Nesvorny et al. 2010 (F39). Input rates in the summary (600-1000, 1000-1500, ~10,000 kg/s) not confirmed on a page; not used. |
| F39 | 2026-10-11 | https://www.boulder.swri.edu/~bottke/Reprints/Nesvorny_2010_ApJ_713_816_Comet_Origin_Zodiacal_Cloud.pdf | dead at the source (curl TLS error, exit 60) | Same paper read from arXiv instead (F40). |
| F40 | 2026-10-11 | https://arxiv.org/pdf/0909.4322 (Nesvorny, Jenniskens, Levison, Bottke et al., "Cometary origin of the zodiacal cloud and carbonaceous micrometeorites", ApJ 713:816, 2010) | useful | Inner zodiacal cloud (<5 AU) "1-2 x 10^19 g" (10^16 kg), mainly 100-200 micron grains; Earth accretes 20,000-60,000 t/yr (LDEF, Love & Brownlee 1993); impact probability of a JFC grain on Earth "~5 x 10^-9 yr^-1 per one particle". |
| F41 | 2026-10-11 | https://arxiv.org/abs/1411.5066 (Batygin, Morbidelli & Holman, "Chaotic disintegration of the inner Solar System", ApJ 2015, abstract) | thin | Orbits "can spontaneously transition from bounded to unbound chaotic states"; secular interactions drive Mercury's transition. No number used. |
| F42 | 2026-10-11 | https://arxiv.org/abs/2105.14976 (Mogavero & Laskar, "Long-term dynamics of the solar system inner planets", A&A 655 A1, 2021, abstract) | useful | 1,000 solutions over 100 Gyr; confirms "the destabilizing influence of the g1-g5 secular resonance" and the current metastable state. |
| C4 | 2026-10-11 | Wrote and ran `calc5_spin_and_dust.py` and `calc6_sudden_loss.py` | useful | Derived figures D6-D11. Check: libration amplitude 38.5" with C22 8.067e-6 and C/MR^2 0.35 gives Cm/C = 0.423 (published 0.431 +/- 0.025, via S26 summary). PR time for a 1 cm, 3 g/cc grain at 0.387 AU: 3.15 Myr (Burns) = Gladman & Coffey's formula (7 Myr x 3 x 1 x 0.15). |
| F43 | 2026-10-12 | https://nssdc.gsfc.nasa.gov/planetary/factsheet/venusfact.html (re-opened, updated 11 Jan 2024) | useful | Second look to confirm inputs used in calc1/calc5 that F2 did not record: mean density 5,243 kg/m^3; surface pressure 92 bar; surface gravity 8.87 m/s^2; length of day 2,802.0 h. |

## 3. Findings

### 3.1 Constants used throughout

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Mercury mass, GM, radius, orbit | 0.33010 x 10^24 kg; GM 0.022032 x 10^6 km^3/s^2; R 2,439.7 km; a 57.909 x 10^6 km; P 87.969 d; e 0.2056; i 7.004 deg; perihelion 46.000, aphelion 69.818 x 10^6 km; mean orbital speed 47.36 km/s; sidereal rotation 1,407.6 h; I/MR^2 0.35 | NSSDC Mercury Fact Sheet, 11 Jan 2024 (F1) | Primary | Mass ratio 1.6601 x 10^-7 of the Sun = Zeebe 2015 table (F9); Standish & Williams a 0.38709927 au, e 0.20563593 (F16) | High |
| Venus mass, GM, radius, orbit, spin | 4.8673 x 10^24 kg; GM 0.32486 x 10^6 km^3/s^2; R 6,051.8 km; a 108.210 x 10^6 km; P 224.701 d; e 0.0068; sidereal rotation -5,832.6 h; solar day 2,802.0 h; I/MR^2 0.337 | NSSDC Venus Fact Sheet, 11 Jan 2024 (F2) | Primary | Mass ratio 2.4478 x 10^-6 = Zeebe (F9); sidereal day 243.0226 d and C/MR^2 0.337 +/- 0.024 (Margot et al. 2021, F27) | High |
| Sun GM | 132,712 x 10^6 km^3/s^2 | NSSDC Sun Fact Sheet, 9 May 2024 (F3) | Primary | Kepler periods from it reproduce the sheets' periods to 0.003 d (calc1 section 0) | High |
| Planetary elements for secular theory | a, e, I, perihelion and node longitudes of all eight planets, J2000 | Standish & Williams, JPL "Approximate Positions of the Planets", Table 1 (F16) | Primary (JPL) | NSSDC summary sheet, 18 Mar 2025 (F15) | High |
| Planet masses for secular theory | Mercury to Neptune, solar masses (Earth includes the Moon) | Zeebe 2015, ApJ 798:8, Table 1 note (F9) | Primary | NSSDC summary masses (F15) to 3 significant figures | High |

### 3.2 Reaction on the planet: recoil, orbit and period (checklist 1)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Recoil law | Planet velocity change = v_inf x ln(M0/M1) for many shots in one direction (m/M for one small shot), where v_inf is the launched mass's speed after leaving the planet's gravity; **a shot at exactly escape speed (v_inf = 0) leaves no net momentum with the planet once it is clear** | DERIVED from momentum conservation (D1) | Derived | Gladman & Coffey 2009 use the same v_inf = sqrt(v_ej^2 - v_esc^2) (F20) | High |
| Leverage of a velocity change on the orbit | Per 1 m/s along the orbit: Mercury's semimajor axis changes by 2,393 km at its mean speed (1,964 km at aphelion, 2,981 km at perihelion); Venus's by 6,183 km. Per 1 m/s radial: e changes by 2.1 x 10^-5 (Mercury), 2.9 x 10^-5 (Venus); along-track up to twice that | DERIVED (D1; Gauss's equation da = 2a^2 v dv / mu) | Derived | vis-viva speeds at Mercury's apsides 58.978 and 38.858 km/s match the sheet's 58.97 and 38.86 | High (first order) |
| Mass that must leave in one direction to move the orbit | Mercury, change of a by **1 km: 1.4 x 10^16 to 1.4 x 10^17 kg**; by **1,000 km: 1.4 x 10^19 to 1.4 x 10^20 kg**; by **1% of a: 7.9 x 10^21 to 7.1 x 10^22 kg (2.4 to 21% of Mercury)** for v_inf 10 to 1 km/s. Venus: 1 km: 7.9 x 10^16 to 7.9 x 10^17 kg; 1,000 km: 7.9 x 10^19 to 7.9 x 10^20 kg; 1%: 8.4 x 10^22 to 7.8 x 10^23 kg (1.7 to 16% of Venus) | DERIVED (D1) | Derived | none found (no published study of launch recoil on a planet's orbit surfaced) | High as arithmetic; it is a bound for perfectly one-directional launch |
| Venus's whole atmosphere launched in one direction | 4.8 x 10^20 kg along the orbit at v_inf 1 / 3 / 10 km/s: Venus's speed changes 0.099 / 0.30 / 0.99 m/s; a by 609 / 1,828 / 6,094 km; period by 164 / 492 / 1,640 s | DERIVED (D1) | Derived | none | High as arithmetic |
| Mass loss with no recoil (material leaves at the planet's own velocity, or is launched symmetrically) | The heliocentric two-body parameter falls by the planet's share: 1.66 x 10^-7 (Mercury), 2.45 x 10^-6 (Venus). Slow loss keeps a x mu and e constant: **removing all of Mercury moves its orbit (the remnant's, or the debris centroid's) out by 9.6 km and lengthens P by 2.5 s; all of Venus: 265 km and 95 s.** Sudden loss: Mercury +6.3 to +14.6 km, de about +/-1 to 2 x 10^-7; Venus +261 to +269 km, de about +/-2.4 x 10^-6 | DERIVED (D2) | Derived | none | High |
| Reading | **The orbit of the planet being mined is not the thing at risk.** Undirected loss of the whole planet moves its orbit by kilometers (Mercury) to hundreds of kilometers (Venus). A measurable orbit change needs a deliberate, one-directional launch of 10^19 to 10^23 kg | from the rows above | - | - | High |

### 3.3 Effects on the other planets: secular dynamics and stability (checklist 2)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Mercury's long-term instability (present Solar System) | Probability that Mercury's e reaches 0.6 in 5 Gyr "about 1 to 2%"; driven by a secular resonance between Mercury's and Jupiter's perihelia (g1 = g5); more unstable without general relativity | Laskar 2008, Icarus (F10) | Primary | Laskar & Gastineau 2009, Nature 459:817: 1% of 2,501 solutions reach e high enough for collision with Venus or the Sun; destabilization of all terrestrial planets in one solution after ~3.34 Gyr (F5, F7); Zeebe 2015: "currently assumed likelihood of ~1%", numerical method changes the odds (F9); Mogavero & Laskar 2021 (F42) | High that the channel is g1-g5; medium on the exact percent (F9 shows integrator dependence) |
| What keeps Mercury off the resonance | General relativity raises g1 "by ~0.43"/yr" and away from g5; Lyapunov time 2.8 to 6 Myr | Zeebe 2015 (F9) | Primary | my secular model: GR shifts the Mercury mode by +0.41"/yr (5.462 to 5.875, calc3) | High |
| Present fundamental frequencies | g1 5.759, g2 7.448, g3 17.269, g4 17.896, **g5 4.257454**, g6 28.245, g7 3.088, g8 0.673 "/yr; s1 -5.652, s2 -6.709, s3 -18.773, s4 -17.707 "/yr (centers of the long-term distributions) | Hoang, Mogavero & Laskar 2023, Table 2 (F13) | Primary | La2004 table values via search summary g1 5.59, g2 7.452, g5 4.257452 (S8, page itself 403) | High |
| Who drives Mercury's perihelion precession | Venus 2.7745, Earth 0.9084, Jupiter 1.5400, Saturn 0.0731, Mars 0.0248 "/yr; total 5.3226 "/yr: **Venus supplies 52%** | Fitzpatrick, *Newtonian Dynamics* (UT Austin), Table B.1 (F11) | Primary (textbook) | my Laplace-Lagrange diagonal terms: Venus 2.863, Earth 0.966, Jupiter 1.603 "/yr (3 to 6% higher); Clemence 1947 via summary: 278, 90, 153 "/century (S6) | High |
| **Removing Venus sweeps Mercury across the g1 = g5 resonance** | Mercury's own secular frequency falls almost linearly as Venus's mass falls, by about 2.7 to 2.8 "/yr from present to zero: 5.875 (full Venus) to 4.511 (half) to 3.101 (none), Laplace-Lagrange. It equals g5 at a Venus mass fraction of **about 0.25 (pure first-order theory), 0.41 (first-order g1 against the true g5 = 4.257), or 0.52 (g1 offset to Laskar's present 5.59)**. So the crossing happens when Venus has lost roughly half to three-quarters of its mass | DERIVED (D4, calc3) | Derived | **No published study removing or reducing Venus was found** (S7). Nearest analogs: Kane, Vervoort & Horner 2025 vary Mars's mass 0 to 1000% (F8); Horner et al. 2019 vary Jupiter's orbit (F14). The mechanism (g1 near g5 drives Mercury's e) is the published one (F9, F10, F42) | Medium: first-order theory, which places g5 13% low (stated in Conflicts); the crossing itself is robust to that error because g1 falls through all three candidate values |
| Size of the kick from that crossing | Linear passage estimate: **e kick 0.001 (removal over 100 yr), 0.003 to 0.004 (1,000 yr), 0.010 to 0.014 (10^4 yr), 0.03 to 0.04 (10^5 yr), 0.10 to 0.14 (10^6 yr), 0.30 to 0.44 (10^7 yr)**, on top of Mercury's present 0.206. **The kick grows as the square root of the removal time: slow removal is the dangerous case** | DERIVED (D5); scaling as in Minton & Malhotra 2011 eq. 33, delta_e proportional to eps x (sweep rate)^-1/2 (F17) | Derived | Minton & Malhotra: sweeping "can potentially both excite and damp" e, and the change is "inversely related to the speed" of the sweep (F17); same physics as the nu6 sweep that sculpted the asteroid belt | Low to medium: linear theory near a resonance, Mercury's e already large and chaotic; for removal faster than ~2 x 10^4 yr the stationary-phase formula overestimates (the sweep is then non-adiabatic) |
| Mercury's orbit after Venus is gone (static) | Mercury's e would oscillate between 0.193 and 0.250 (now 0.13 to 0.23 in the same model), with its free frequency (about 3.1 "/yr in first-order theory, about 2.8 to 3.1 corrected) **close to g7 = 3.088 "/yr (Uranus)**; the g7 forcing on Mercury is weak (0.0017 amplitude) | DERIVED (D4) | Derived | none | Low (first-order; new resonance proximity flagged, not evaluated) |
| Earth's eccentricity with Venus removed (static, present initial orbits) | Earth's own mode moves from about 17.4 to 7.7 "/yr; the strongest eccentricity cycle becomes the g3-g5 beat: **about 376 kyr** with the true g5 (326 kyr first-order); the ~95 to 130 kyr band nearly vanishes (largest remaining term 0.0021 against 0.015 now); **Earth's maximum e falls from 0.065 to 0.043** in the same model | DERIVED (D4) | Derived | Model baseline gives Earth e 0 to 0.065 and a "405 kyr" beat that with Laskar's frequencies is 1,296,000"/(7.452 - 4.257) = 405.6 kyr; La2010 range "almost zero and about 0.06" (S12, summary only) | Medium for direction and order of magnitude; low for exact values (secular, not N-body; climate consequences not evaluated) |
| Earth's eccentricity with Mercury removed | Venus's mode shifts by -0.18 "/yr; with Laskar's values the 405 kyr cycle lengthens to **about 430 kyr**; Earth's maximum e 0.065 to 0.058; ~100 kyr band unchanged | DERIVED (D4) | Derived | none | Medium (the shift is small and first-order theory handles g2 well: 7.427 vs 7.448) |
| Whether the 405 kyr cycle is robust to other planets' masses | "persists at all Mars masses" (0 to 1000% of Mars); it is "driven by g2 (Venus) and g5 (Jupiter)"; the 2.4 Myr cycle is "absent when Mars approaches zero mass" | Kane, Vervoort & Horner 2025 (F8) | Primary (preprint; PASP 137, 124402) | Hoang et al. 2023: 405 kyr is the strongest component (F13) | High |

### 3.4 The launched material: radiation forces, lifetimes, debris and delivery to Earth (checklist 3)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Radiation-pressure parameter | beta = F_rad/F_grav = 5.7 x 10^-5 Q_pr/(rho s) (cgs; sphere); independent of distance; released from a circular orbit a body is unbound if beta >= 1/2 | Burns, Lamy & Soter 1979, Icarus 40 (F19) | Primary | none needed (defining paper) | High |
| Poynting-Robertson infall time | t_PR = 7.0 x 10^6 s rho R^2/Q_pr yr = 400 R^2/beta yr (R in AU) | Burns et al. 1979 eq. 50 (F19) | Primary | Gladman & Coffey 2009 eq. 2 (F20), identical | High |
| Thin collectors (flat, absorbing) | Critical areal density (beta = 1) 0.76 g/m^2 absorbing, 1.52 g/m^2 reflecting. At Mercury's distance, **a 1 kg/m^2 collector feels 30 micro-m/s^2 of radiation force and, uncontrolled, spirals into the Sun in ~79,000 yr; 0.1 kg/m^2: ~7,900 yr; 0.01 kg/m^2: ~790 yr**. At Venus: 275,000, 27,500, 2,750 yr | DERIVED (D8) from Burns et al. | Derived | none | Medium (absorbing flat plate face-on; a tilted or reflecting surface differs by up to 2x and gains a sideways force) |
| Small particles from processing losses | At Mercury (rho 3): 1 micron grain beta 0.19, PR life 315 yr; 10 micron 3,150 yr; 1 mm 3.2 x 10^5 yr; 1 cm 3.2 Myr; 10 cm 32 Myr. Grains below roughly 0.4 micron radius (beta > 0.5 for Q_pr near 1 and rho 3) are blown out of the Solar System | DERIVED (D8) | Derived | Gladman & Coffey: a 10 cm meteoroid at a 0.7 AU, e 0.5: ~70 Myr (F20) | Medium (Q_pr taken as 1; sub-micron Q_pr is smaller) |
| Natural dust rings at Mercury and Venus | Mercury: brightness excess 1.5-2.5%, density excess 3-5% (ring ~9.3 million miles wide); Venus: density excess ~10% | Stenborg & Howard 2018 ApJ and Jones et al. 2013/2017, via NASA (F25) and search summary (S14) | Secondary for the numbers (NASA news) | two independent summaries agree | Medium |
| Size of the natural dust cloud | Inner zodiacal cloud (<5 AU) 1-2 x 10^19 g = **1-2 x 10^16 kg**; Earth sweeps up 20,000-60,000 t/yr; a dust grain's chance of hitting Earth ~5 x 10^-9 per year | Nesvorny et al. 2010, ApJ 713:816 (F40) | Primary | Fixsen & Dwek 2002 ~5 x 10^18 g (summary S35, not opened) | Medium (density assumption per the paper) |
| **Lost material against that cloud** | Mercury's mass is 1.7 to 3.3 x 10^7 zodiacal clouds: **losing 3 to 6 parts in 10^8 of Mercury as dust equals the entire present inner zodiacal cloud.** Venus's atmosphere is 2.4 to 4.8 x 10^4 clouds | DERIVED (D10) | Derived | none | High as arithmetic; what fraction of a harvest is lost as dust is unknown (no study) |
| Where ejected rock goes (Mercury) | 2-5% reaches Earth in 30 Myr (0.7% at v_inf 4 km/s); Venus takes 20% (8-13% at v_inf 20-25 km/s); at v_inf = 4 km/s half is re-accreted by Mercury in 30 Myr, a third in as little as 2 Myr; ~2/3 of fast ejecta is still in space after 30 Myr | Gladman & Coffey 2009 (F20) | Primary (N-body, 18,000 particles per case) | Cornell 1996 summary of Gladman et al. 1996: "less than 1 percent" (F21; superseded) | High for natural ejecta, which is the right analog for lost or stray cargo (DEMONSTRATED as a model, not observed) |
| Where ejected material goes (Venus) | Venus to Earth 10% (10 Myr; 40% still in orbit so a lower bound); 4.48% to Earth and 34.71% re-accreted by Venus within 1 Myr; 0.03% to the Moon | Cabot & Laughlin 2020, PSJ (F22) | Primary | Melosh & Tonks 1993 ~30% (as cited by F22; also S16 summary of Gladman et al. 1996) | Medium (differs 3x between studies) |
| Swarm collision time | "roughly an orbital period divided by the covering fraction"; cascades develop "extremely rapidly" at hypervelocity; swarms "short-lived ... without active upkeep" | Lacki 2025, ApJ 985:191 (F37) | Primary (SPECULATIVE subject, physical analysis) | Kessler-type cascade (concept only) | Medium |
| Natural co-orbital material | Mercury cannot hold Trojan (tadpole) orbits over 100 Myr, long-lived low-inclination horseshoe orbits possible; Venus holds low-inclination tadpole and horseshoe families over 25 Myr; ~8% of Venus co-orbitals survive 4.5 Gyr (Pokorny & Kuchner) vs none survive the age of the Solar System, Yarkovsky drives them out (Xu et al.) | Tabachnik & Evans 2000 (F23); Pokorny & Kuchner 2019 (F24); Xu et al. 2022 (F26) | Primary | the two Venus results conflict (section 4) | Medium |

### 3.5 Lagrange points, catchers and launch direction (checklist 4)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Sun-planet L1 and L2 distances | Mercury 220,395 / 220,955 km (Hill radius 175,000 km at perihelion to 266,000 km at aphelion); Venus 1,008,006 / 1,014,305 km | DERIVED (D3; restricted three-body, circular) | Derived | [NW] F4: Mercury Hill sphere about 221,000 km | High (circular approximation; Mercury's e makes L1 breathe by +/-20%) |
| Instability of L1/L2 | e-folding time **5.6 d at Mercury (doubling 3.9 d), 14.1 d at Venus (9.8 d), 23.0 d at Earth (15.9 d)**; a small error grows about 7 x 10^6-fold per orbit | DERIVED (D3) | Derived | **Roberts 2011 (NASA L1 operations): station-keeping cost "doubling time constant is approximately 16 days"** at Earth (F38), matching 15.9 d | High |
| Station-keeping, measured at Earth L1 | ~1.0 m/s per year (ACE, WIND), SOHO much less; burns every ~3 months | Roberts 2011 (F38) | Primary | none | High |
| Station-keeping at Mercury and Venus L1 | No study found. Scaling by the instability rate suggests burns about 4 times as often at Mercury (every ~3 weeks) and 1.6 times at Venus, with costs of order a few m/s per year if navigation errors match Earth's | DERIVED, heuristic (D3) | Derived | none | Low |
| Radiation force on a catcher at Mercury L1 | For an absorbing area of 0.1 / 1 / 10 kg/m^2 the radiation acceleration is 66% / 7% / 1% of Mercury's own pull at L1 (4.5 x 10^-4 m/s^2); the equilibrium point of a large-area catcher is displaced sunward | DERIVED (D8) | Derived | none | Medium |
| L1 moves as the planet loses mass | L1/L2 distance scales as (remaining mass)^(1/3): 0.965x at 90% left, 0.794x at 50%, 0.464x at 10%, 0.215x at 1% (Mercury: 220,000 to 175,000 to 102,000 to 48,000 km) | DERIVED (D3) | Derived | none | High |
| Mercury launcher direction | Rotation does not aim a fixed track; asymptote alignment repeats once per 175.9-d solar day | [NW] F4 (cited, not re-derived) | - | - | as [NW] |
| Venus launch direction | Sidereal day 243.0226 d retrograde, solar day 116.75 d (2,802 h); equatorial ground speed 1.8 m/s (DERIVED), no launch assist; a fixed surface track faces a given direction of Venus's orbital motion once per 116.75 d. A platform at cloud level rides the "4-day atmospheric superrotation", so it faces every direction every few days | NSSDC (F2); Margot et al. 2021 (F27) | Primary | none | High for the periods; platform launch itself has no study ([MS] section 4) |
| Venus has no surface-anchored catcher geometry | A stationary orbit lies 1.5 times outside Venus's Hill sphere | [MS] section 4 / [VE] 3.7 (cited) | - | - | as cited |

### 3.6 Tides and spin (checklist 5)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Mercury's 3:2 lock: physical parameters | C22 = 8.067 x 10^-6; (B-A)/MR^2 = 4 C22; libration amplitude 38.5 +/- 1.6" (radar), 38.9 +/- 1.3" (MESSENGER); free libration about 10 yr; k2 = 0.464 +/- 0.023 | Verma & Margot 2016 (F33); Stark et al. 2017 table (F28); Peale 2005 (F32) | Primary | My check: these give Cm/C = 0.423 against the published 0.431 +/- 0.025 (S26) | High |
| Width of the lock in spin rate | The spin can be pushed **0.9% (whole planet, long term) to 1.4% (mantle only, short term)** off exact 3:2 before the lock breaks; small-amplitude libration period 17.9 yr (whole) / 11.7 yr (mantle) | DERIVED (D6) | Derived | Peale: ~10 yr for a larger (B-A)/Cm of 3.5 x 10^-4 (F32) | Medium (pendulum model; Mercury's e varies) |
| **Launching from Mercury's surface torques its spin** | Net one-directional launch along the equator at 4.25 km/s relative to the ground: **7.4 x 10^17 kg delivered faster than a libration period breaks the 3:2 lock** (5.2 x 10^17 at 6 km/s, 3.1 x 10^17 at 10 km/s; about 2 parts in 10^6 of Mercury). The resonance's largest restoring torque is 4.2 x 10^19 N m; a sustained one-directional launch above **5 x 10^16 to 1.3 x 10^17 kg/yr** overpowers it | DERIVED (D6) | Derived | none (no study of launch torque on a planet's spin found) | Medium; a balanced (two-way or radial) launch puts no net torque on the spin |
| Uneven excavation and the lock | The permanent asymmetry that the Sun grips is equivalent to **1.1 x 10^19 kg (3 parts in 10^5 of Mercury)** placed at the equator; removing that much mass unevenly in longitude could cancel or double it | DERIVED (D6) | Derived | none | Low to medium (point-mass model; real mass distribution unknown at depth) |
| How Mercury got into 3:2 | Capture was the most probable outcome (55.4% of 1,000 orbits over 4 Gyr) because chaotic e exceeded 0.325 at times | Correia & Laskar 2004, Nature 429 (S27, abstract-level) | Primary (record) | none opened | Medium |
| Venus's spin is a balance of tides | Solid-body solar tides would synchronize Venus; the thermal atmospheric tide pushes the other way; the spin "settles where the two torques balance" | Margot et al. 2021 (F27) | Primary | Correia & Laskar 2001; Auclair-Desrotour et al. 2017 (S21, F29, F30) | High |
| What removing Venus's atmosphere does to its spin, short term | Atmospheric angular momentum 2.9 x 10^28 kg m^2/s +/- 30%, 1.6 x 10^-3 of the solid planet's; full transfer would change the day by about -9.4 h (my figure -9.46 h). Day-to-day LOD swings already reach 61 ppm (~20 min) | Margot et al. 2021 (F27) | Primary | my arithmetic D7 | High |
| ... and long term | With the thermal tide gone, solid tides alone synchronize a Venus-like planet from a 100-d spin in **5.5 x 10^7 yr** (one model; at high obliquity capture in 2:1 for a few 10^7 yr) | Revol et al. 2023, A&A (F31) | Primary | A "700,000 yr" figure seen only in a search summary was not found on any page (S23, S24) | Medium (one model) |
| Unloading the surface | Venus's atmosphere presses 9.2 MPa on the surface (= ~350 m of rock at an assumed 3,000 kg/m^3). Analog: removing Iceland's ~1.4-2 km ice sheet (~12-18 MPa) raised eruption rates 5-30-fold, upper-mantle decompression rate up to 50-fold | DERIVED (D7); Eksinchol et al. 2019 citing Jull & McKenzie 1996 (F34) | Derived; primary for the analog | none | Low as a prediction: Iceland is a rift over hot mantle and its load was local (flexure); a global, uniform unloading drives less lateral flow. SPECULATIVE |
| Tidal heating during unloading | No study found; Mercury's k2 = 0.46 sets its tidal response; uniform-sphere central pressure falls from 24.5 GPa to 15.4 GPa at half mass (Venus 141 to 89 GPa) | Verma & Margot 2016 (F33); DERIVED (calc1 section 7) | Derived | none | Low (uniform-sphere bound only) |

### 3.7 Using removed mass to move or spin a planet (checklist 6)

| Quantity | Value and units | Source | Primary or secondary | Cross-check | Confidence |
|---|---|---|---|---|---|
| Published planet-moving concepts | Gravity-assist energy transfer from Jupiter to Earth: moving Earth to 1.5 AU needs 8.7 x 10^32 J; one 10^19 kg (10^22 g) body flyby every ~6,000 yr over ~10^9 yr (SPECULATIVE). Solar-sail alternative: sail mass four orders of magnitude below the flyby scheme's processed mass, ~10^9 yr (SPECULATIVE) | Korycansky, Laughlin & Adams 2001 (F35); McInnes 2002 (F36) | Primary | My orbital-energy formula gives 8.83 x 10^32 J for Earth to 1.5 AU (D11), matching | High that these are the published concepts; neither uses a planet's own mass as reaction mass |
| **A planet as its own rocket** | No published study of a planet expelling its own mass to move itself was found. DERIVED: Mercury out by 1% in a takes 0.24 km/s and expels 7.6% / 2.4% / 0.79% of Mercury at v_inf 3 / 10 / 30 km/s (launch energy 3.4 x 10^29 to 1.2 x 10^30 J); out by 10% takes 2.2 km/s and 52% / 20% / 7.2%. Venus out by 1%: 5.6% / 1.7% / 0.58%; to 1 AU (x 1.382): 5.2 km/s, 83% / 41% / 16% of Venus, 2.1 to 3.9 x 10^32 J | DERIVED (D11) | Derived | none | High as arithmetic; it ignores launch losses and needs the launch direction to track the orbit |
| Spinning Venus with its own atmosphere | Launching all 4.8 x 10^20 kg tangentially at escape speed gives 1.68 times Venus's spin angular momentum: **at best a 90.5-d retrograde day or a 355-d prograde day; at 30 km/s, 41 to 63 d. It cannot approach a 24-h day**, which (taking a round 24.0 h sidereal day as the target) needs 1.6 x 10^29 J of spin energy and the tangential launch of 7.2 x 10^22 kg at 10 km/s (1.5% of Venus) or 2.4 x 10^22 kg at 30 km/s | DERIVED (D9) | Derived | Forum claims (S32) reach the same conclusion; no primary found | High as arithmetic |
| Fiction source for the idea | Nordley 1991 short story "The Snows of Venus": Venus spun to a 30-day day by exporting its atmosphere by mass drivers | search summary (S30) | Secondary (fiction) | D9 shows a 30-day day needs more than the whole atmosphere at escape speed | Rejected as a source; recorded as the origin of the idea |

## 4. Conflicts

- **Venus co-orbitals: survive or not.** Pokorny & Kuchner 2019 find ~8% of Venus 1:1-resonant asteroids survive 4.5 Gyr (enough to feed the
  observed dust ring); Xu et al. 2022 find Venus Trojans "cannot survive the age of the Solar system" and that the Yarkovsky effect empties the
  region quickly, so the ring is "more likely a sporadic phenomenon". Likely reasons: Xu et al. include Yarkovsky drift and a different initial
  population; Pokorny & Kuchner's survivors are mainly low-inclination horseshoe orbits. For harvesting, both agree that **material parked
  near Venus's L4/L5 is not held passively forever**; small bodies are pushed out by sunlight.
- **Venus-to-Earth transfer of ejecta:** 10% in 10 Myr (Cabot & Laughlin 2020, lower bound with 40% still in flight) against ~30% (Melosh &
  Tonks 1993, and the summary of Gladman et al. 1996). Different launch conditions, integrators and durations; the order (several to tens of
  percent) is what matters here.
- **Mercury-to-Earth transfer:** "less than 1 percent" (1996, F21) and 0.1% in 10 Myr (Gladman 2003, as cited in F20) against 2-5% in 30
  Myr (Gladman & Coffey 2009). The later study integrates three times longer and launches at Mercury's true high impact-driven speeds.
- **Probability of Mercury's instability:** ~1% (Laskar & Gastineau 2009), 1-2% for e > 0.6 (Laskar 2008), and Zeebe 2015 shows the
  odds depend on the integrator's coordinates (P(e rises above 0.53 in 500 Myr) 40-55% heliocentric vs >90% Jacobi). The definition of
  "unstable" also differs (e > 0.6, collision, or a 5 Gyr window).
- **Present vs long-term secular frequencies:** g1 = 5.59 "/yr (La2004 table, present) vs 5.759 "/yr (center of the 5 Gyr distribution,
  Hoang et al. 2023). Mercury's frequency diffuses chaotically; I bracketed the crossing estimate with both.
- **My first-order secular model vs Laskar:** first-order Laplace-Lagrange gives g5 = 3.73 and g6 = 22.5 "/yr against the true 4.257 and
  28.245, because Jupiter and Saturn sit near a 5:2 commensurability that first-order theory omits (a known limitation of the method, not
  re-sourced here). The inner-planet frequencies come out close (g2 7.43 vs 7.45; g3, g4 within 1%; g1 5.88 vs 5.59-5.76). The g1 = g5
  crossing is therefore stated as a range of Venus mass fractions (0.25 to 0.52), not a point.
- **Venus-on-Mercury precession:** Fitzpatrick's secular value 2.7745 "/yr vs my Laplace-Lagrange 2.863 "/yr (3%); Clemence 1947 via a
  summary ~278 "/century. Differences in eccentricity terms retained.
- **Mercury C/MR^2:** NSSDC sheet 0.35 (used); Margot et al. 2012 0.346 +/- 0.014; Genova et al. 2019 0.333 +/- 0.005 (both via a search
  summary, S26). A 4% lower C would narrow the spin-lock figures in D6 by about 2%.
- **Iceland ice load:** 2 km (Jull & McKenzie 1996) vs 1.39 km average (Eksinchol et al. 2019 model input); both quoted in F34.

## 5. Derived figures

Scripts and raw output (scratch folder `/tmp/claude-1000/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/3ccdb441-c6c0-49c3-a71c-ab4a4fdd3c1e/scratchpad/orbital_dynamics_of_planetary_harvesting/`):
`calc1.py` / `calc1_out.txt` (recoil, mass loss, Hill and collinear points, planet as rocket, central pressure); `calc2_secular.py` /
`calc2_out.txt` (first secular run, superseded); `calc3_secular_amplitudes.py` / `calc3_out.txt` (secular frequencies and amplitudes);
`calc4_sweep.py` / `calc4_out.txt` (resonance passage); `calc5_spin_and_dust.py` / `calc5_out.txt` (spin lock, Venus spin, radiation forces,
debris); `calc6_sudden_loss.py` / `calc6_out.txt`. Downloaded papers are in `pdf/`. All run with `python3 -I`.

**D1. Recoil.** Momentum: a planet of mass M launching mass dm with hyperbolic excess v_inf gains dv = v_inf dm/M; for a sustained launch in one
direction dv = v_inf ln(M0/M1). Orbit: Gauss's equation for an along-track change, da = 2 a^2 v dv / mu, mu = G(M_sun + M_p); radial dv on a
near-circular orbit leaves a unchanged and gives de = dv/v. Inputs NSSDC (F1-F3). Key lines of `calc1_out.txt`:
```
Mercury: to change a by 1 km (dv 0.0004178 m/s) with v_inf 1 / 3 / 10 km/s: launch 1.379e17 / 4.597e16 / 1.379e16 kg
Mercury: to change a by 1000 km (dv 0.4178 m/s): 1.379e20 / 4.597e19 / 1.379e19 kg
Mercury: to change a by 5.791e5 km (1%, dv 241.9 m/s): 7.094e22 / 2.558e22 / 7.891e21 kg (21% / 7.7% / 2.4%)
Venus: 1 km: 7.876e17 / 2.625e17 / 7.876e16 kg; 1000 km: 7.876e20 / 2.625e20 / 7.876e19 kg; 1% (1.082e6 km, dv 175.1 m/s): 7.818e23 / 2.760e23 / 8.449e22 kg
Mercury perihelion: v = 58.978 km/s, da per 1 m/s = 2981 km; aphelion: 38.858 km/s, 1964 km
de per 1 m/s radial: Mercury 2.111e-05, Venus 2.856e-05 (tangential up to 2x)
4.8e20 kg at v_inf 1 / 3 / 10 km/s all prograde: Venus dv 0.0986 / 0.2959 / 0.9862 m/s; da 609 / 1828 / 6094 km; dP 164 / 492 / 1640 s
```
Note: Gauss's equation was evaluated at the sheet's mean orbital speed (Mercury 47.36 km/s; circular speed at a is 47.87 km/s), a 1% effect.

**D2. Mass loss without recoil.** Slow loss: a mu = constant, e constant, so da/a = dmu/mu and dP/P = 2 dmu/mu (calc1 section 2). Sudden loss:
vis-viva with the same r and v and the smaller mu (calc6). Output:
```
Mercury: GM_p/(GM_sun+GM_p) = 1.6601e-07; all removed: da = 9.61 km, dP = 2.52 s (slow); sudden at perihelion +14.59 km, de +2.0e-7; at aphelion +6.33 km, de -1.3e-7
Venus:   2.4479e-06; all removed: da = 265 km, dP = 95 s (slow); sudden at perihelion +268.5 km, de +2.5e-6; at aphelion +261.3 km, de -2.4e-6
```

**D3. Hill radius, L1/L2 and their instability.** r_H = a (m/3M)^(1/3); collinear points and the linearized unstable exponent lambda from the
circular restricted three-body problem (c2 = (1-mu)/r1^3 + mu/r2^3; lambda^2 = (c2 - 2 + sqrt(9c2^2 - 8c2))/2), in units of the mean motion n.
```
Mercury L1: 220,395 km; c2 4.0230; lambda 2.5175 n; e-folding 5.56 d; growth per orbit 7.4e6
Venus   L1: 1,008,006 km; c2 4.0568; lambda 2.5309 n; e-folding 14.13 d
Earth   L1: 1,491,553 km; c2 4.0608; lambda 2.5326 n; e-folding 22.95 d  (doubling 15.9 d; Roberts 2011 measured ~16 d)
Mercury r_H at perihelion 175,293 km, at aphelion 266,057 km; remaining mass 0.9/0.5/0.1/0.01 -> 213,060 / 175,150 / 102,428 / 47,543 km
```
Station-keeping heuristic: Earth L1 costs ~1 m/s/yr with burns every ~3 months (F38). If the burn interval scales with the doubling time and
the per-burn correction with the same navigation error, the burn rate scales with n: x4.15 at Mercury, x1.63 at Venus. This is a scaling
guess, not a design.

**D4. Secular theory with Venus or Mercury reduced** (`calc3`). First-order Laplace-Lagrange: A_jj = (n_j/4) sum_k m_k/(M_sun+m_j)
alpha alphabar b^(1)_3/2(alpha); A_jk = -(n_j/4) m_k/(M_sun+m_j) alpha alphabar b^(2)_3/2(alpha); B analogous with b^(1); GR term
3(GM)^1.5/(c^2 a^2.5 (1-e^2)) added to A_jj (gives Mercury 42.98 "/century). Mode amplitudes from the J2000 elements (F16). Key output:
```
baseline: g = 0.634, 2.708, 3.732, 5.875, 7.427, 17.377, 18.035, 22.512 "/yr
  Mercury e 0.1287-0.2332; Earth e 0.0000-0.0649; Earth beats 91, 351, 122, 95 kyr
Venus x0.5: Mercury mode 4.511; Earth e 0-0.0433; Earth beats 346, 94, 128, 116 kyr
Venus x0.0: g = 0.634, 2.707, 3.101 (Mercury), 3.729, 7.707 (Earth), 17.334, 22.511
  Mercury e 0.1930-0.2501; Earth e 0-0.0426, largest terms 0.0194 @ g5, 0.0182 @ 7.707, 0.0021 @ 17.334; beats 326, 95, 135, 69 kyr
Mercury x0.0: Venus mode 7.249; Earth e 0-0.0580; beats 91, 368, 121, 95 kyr
Fine scan, Mercury mode vs Venus mass fraction f: f=1.00 5.875; 0.75 5.204; 0.50 4.511; 0.45 4.371; 0.40 4.231; 0.30 3.950; 0.25 3.730 (= LL g5); 0.20 3.667; 0.10 3.385; 0.00 3.101
  (linear theory's Mercury e max diverges near f = 0.20-0.25: 0.852 at f = 0.20, the resonance; not physical)
```
Crossing with the true g5 = 4.257: first-order g1 reaches 4.257 at f = 0.41 (interpolating 0.40 -> 4.231, 0.45 -> 4.371). Offsetting g1 to
Laskar's present 5.59 and using the slope 2.73-2.77 "/yr per unit f: 5.59 - 2.77 (1 - f) = 4.257 at f = 0.52. Converting to periods: 1,296,000"
/ (g_a - g_b) per cycle; with Laskar values g2 - g5 = 3.195 "/yr gives 405.6 kyr. Mercury removed: g2 falls 0.178 "/yr, so with Laskar values
g2 - g5 = 3.017 "/yr, 429.6 kyr. Venus removed: Earth's mode 7.707 against the true g5: 1,296,000 / 3.450 = 375.7 kyr.

**D5. Resonance passage.** Forced oscillator z = e exp(i varpi), dz/dt = i g1 z + i nu exp(i g5 t); away from resonance |z_forced| =
nu/|g1 - g5|, so nu = |z_forced| |g1 - g5|; a passage at d(g1 - g5)/dt = lambda gives |dz| = nu sqrt(2 pi / lambda) (stationary phase). From
calc3, nu = 0.0285 to 0.0416 e "/yr (1.4 to 2.0 x 10^-7 rad/yr) between f = 0.45 and 1.0; slope 2.728 "/yr per unit f; Venus removed at a
constant rate over T years: lambda = 2.728/(206,265 T) rad/yr^2.
```
T = 1e2 yr: kick 0.0010-0.0014;  1e3: 0.0030-0.0044;  1e4: 0.0095-0.0139;  1e5: 0.0301-0.0439;  1e6: 0.0952-0.1389;  1e7: 0.3010-0.4393
```
Validity: the resonant passage lasts ~sqrt(2 pi/lambda) = 22,000 yr at T = 1,000 yr, longer than the whole removal, so for T below ~10^4 yr the
passage is effectively sudden and the kick is bounded instead by the jump between the before and after secular states (Mercury e range
0.13-0.23 before, 0.19-0.25 after). For T of 10^6 yr or more the linear estimate approaches Mercury's own e and is no longer reliable;
nonlinear behavior near g1 = g5 is exactly the published instability channel.

**D6. Mercury's spin lock** (`calc5` A). C = 0.35 M R^2 = 6.877 x 10^35 kg m^2; B - A = 4 C22 M R^2 = 6.340 x 10^31 kg m^2; (B-A)/C = 9.22 x
10^-5; libration amplitude 38.5" gives (B-A)/Cm = 2.18 x 10^-4, Cm/C = 0.423. Pendulum model of the 3:2 resonance, gamma'' = -(3/2) n^2
((B-A)/C) H sin 2 gamma with H = (7/2)e - (123/16)e^3 = 0.653 (the eccentricity factor in Peale's eq. 4): small-amplitude frequency w0 =
n sqrt(3 ((B-A)/C) H), separatrix half-width in spin rate = w0; maximum restoring torque = (3/2) n^2 (B-A) H.
```
whole planet: w0 = 0.0134 n, period 17.9 yr, half-width 0.90% of the spin; mantle only: 0.0207 n, 11.7 yr, 1.38%
max restoring torque 4.243e19 N m
equatorial tangential launch at 4.25 / 6 / 10 km/s: impulsive mass to break the lock 7.367e17 / 5.218e17 / 3.131e17 kg; sustained rate limit 1.291e17 / 9.146e16 / 5.488e16 kg/yr
point-mass equivalent of (B-A): 1.065e19 kg (3.23e-5 of Mercury)
```
The torque of a launch is m v R for mass m leaving tangentially at speed v relative to the ground. Launch toward escape in a direction set by
the orbit (not by the ground) still has a tangential component at the track; the sign depends on which way the track points.

**D7. Venus spin and unloading** (`calc5` B). Solid spin angular momentum C w = 5.972 x 10^37 x 2 pi/(243.0226 d) = 1.787 x 10^31 kg m^2/s;
AAM/solid = 1.62 x 10^-3; dP = -9.46 h if all of it were transferred. Surface load M_atm g/(4 pi R^2) = 9.25 MPa (92 bar on the sheet).

**D8. Radiation forces** (`calc5` C, D). From Burns eq. 19, 3L/(16 pi G M c) = 5.7 x 10^-5 g/cm^2 for a sphere, so for a flat absorbing plate
beta = L/(4 pi G M c sigma) = (4/3)(5.7 x 10^-5 g/cm^2)/sigma = 0.760 g/m^2 / sigma (reflecting: 1.52 g/m^2). PR time 400 R^2/beta yr.
```
Mercury distance: solar gravity 39.6 mm/s^2; 0.01 / 0.1 / 1 / 10 kg/m^2 plate: beta 7.6e-2 / 7.6e-3 / 7.6e-4 / 7.6e-5; PR infall 788 / 7,883 / 78,826 / 788,258 yr
Venus distance: 11.3 mm/s^2; PR 2,751 / 27,512 / 275,121 / 2,751,205 yr
grains (rho 3) at Mercury: 1 um beta 0.19, 315 yr; 10 um 3,150 yr; 1 mm 3.15e5 yr; 1 cm 3.15e6 yr; 10 cm 3.15e7 yr
collector at Mercury L1, 0.1 / 1 / 10 kg/m^2: radiation 3.01e-4 / 3.01e-5 / 3.01e-6 m/s^2 vs Mercury's pull 4.54e-4 m/s^2
```

**D9. Spinning Venus with its own atmosphere.** Angular impulse of the whole atmosphere launched tangentially at speed v: 4.8 x 10^20 v R.
```
v = 10.36 km/s: 3.010e31 = 1.68 x spin -> 90.5 d retrograde (with the spin) or 355.2 d prograde (against it)
v = 20 km/s: 5.810e31 = 3.25 x -> 57.2 d retrograde or 108.0 d prograde;  v = 30 km/s: 8.715e31 = 4.88 x -> 41.4 d or 62.7 d
spin energy at a 24.0 h sidereal day (round target) 1.579e29 J (present 2.674e24 J); mass to launch for it: 7.206e22 kg at 10 km/s, 2.402e22 kg at 30 km/s
```
(C held constant; it would fall slightly as mass leaves.)

**D10. Debris against the zodiacal cloud** (`calc5` F). Zodiacal cloud 1-2 x 10^16 kg (F40). Mercury = 1.7-3.3 x 10^7 clouds; loss fraction equal to
one cloud = 3.0-6.1 x 10^-8. Venus atmosphere = 2.4-4.8 x 10^4 clouds. A launch stream of 10^12 kg/yr losing 1% as small debris adds 10^10 kg/yr,
10^-6 of the cloud per year; 10^15 kg/yr at 1% adds 10^-3 of the cloud per year.

**D11. A planet as its own rocket** (calc1 section 5). Low-thrust spiral between circular orbits, dv = |v1 - v2|; expelled fraction =
1 - exp(-dv/v_inf); launch energy (v_esc^2 + v_inf^2)/2 per kg, no losses.
```
Mercury a x1.01: dv 0.238 km/s; expel 7.61% / 2.35% / 0.789% at v_inf 3 / 10 / 30 km/s; launch energy 3.40e29 / 4.58e29 / 1.20e30 J; orbital energy change 3.75e30 J
Mercury a x1.1:  dv 2.228 km/s; 52.4% / 20% / 7.16%; 2.34e30 / 3.89e30 / 1.08e31 J
Mercury a x1.5:  dv 8.785 km/s; 94.7% / 58.5% / 25.4%
Venus a x1.01:   dv 0.174 km/s; 5.63% / 1.72% / 0.578%; 1.59e31 / 8.70e30 / 1.42e31 J
Venus a x1.1:    dv 1.630 km/s; 41.9% / 15% / 5.29%
Venus to 1 AU (x1.382): dv 5.231 km/s; 82.5% / 40.7% / 16%; 2.34e32 / 2.06e32 / 3.92e32 J; orbital energy change 8.25e32 J
check: Earth to a circular 1.5 AU orbit = 8.83e32 J by this formula; Korycansky et al. 2001 give 8.7e32 J
```
Note the launch energy can be smaller than the orbital energy gained: the expelled mass carries away energy of the opposite sign (the rocket
equation's bookkeeping); the figures are the energy the launcher must supply, not the planet's orbital-energy change.

## 6. Constraints for any inhabitant

- **The ground under a Mercury operation turns at a fixed 3:2 rate held by a weak grip.** A net one-directional launch of ~5 x 10^16 kg/yr or
  more along the equator (or ~7 x 10^17 kg in a burst) would knock the planet out of its 3:2 spin; launch tracks that balance east and west, or
  launch radially, avoid it (3.6, D6). Uneven excavation of ~10^19 kg changes the asymmetry that holds the lock.
- **Anything parked near Mercury or Venus on the Sun line drifts away within days** (e-folding 5.6 d and 14 d); catchers and depots at
  L1/L2 need burns several times a month at Mercury and continuous autonomous control (3.5).
- **Light structures are pushed and dragged by sunlight.** A 1 kg/m^2 collector near Mercury carries 30 micro-m/s^2 of radiation force and,
  left alone, spirals into the Sun in ~79,000 yr; a 10 g/m^2 film in ~800 yr; lost micron-to-millimeter dust in centuries to ~10^5 yr, and grains under ~0.4 micron are blown out of the Solar System (3.4, D8).
- **Lost material does not stay local.** A few percent of rock leaving Mercury, and 5 to 30% leaving Venus, reaches Earth over 1 to 30 Myr;
  losses of 10^-7 of Mercury's mass equal the whole present zodiacal cloud, raising the dust and meteoroid flux everywhere inside ~1 AU (3.4).
- **Swarms of collectors collide on a time scale of an orbital period divided by their covering fraction** once guidance lapses; at Mercury
  the orbital period is 88 d (3.4).
- **A Venus with its atmosphere gone keeps its day only briefly by geological standards:** solid tides alone would drive the spin toward
  synchronous over ~10^7 to 10^8 yr; the immediate change is at most ~9 h of a 243-d day (3.6).
- **Unloading may stir the interior.** Removing a load of ~9 MPa (Venus's atmosphere) or ~1 km of rock (Mercury) is the same order as the
  ice load whose removal multiplied Iceland's eruption rate 5 to 30 times; whether a global unloading does this is not studied (3.6).
- **Removing most of Venus is not a local act:** it sweeps Mercury through the resonance that makes Mercury chaotic, and it reshapes Earth's
  eccentricity cycles (the ~100 kyr band nearly vanishes, the dominant cycle becomes ~376 kyr, maximum e falls to ~0.043). A fast removal
  (under ~10^4 yr) disturbs Mercury less than a slow one (3.3, D5).

## 7. Candidate handwaves

Flagged for the developer; none accepted.

- **H-1. Harvesting more than about half of Venus with no consequence for Mercury.** On first-order secular theory, Mercury's precession
  crosses Jupiter's (g1 = g5) when Venus is reduced to 25-52% of its mass; a slow removal (10^6-10^7 yr) gives Mercury an eccentricity kick of
  0.1 to 0.4. Avoiding it needs a fast removal (kick ~0.01 at 10^4 yr), an N-body study showing it is harmless, or active control of Mercury.
- **H-2. Unlimited one-directional launching from Mercury's surface.** More than ~5 x 10^16 to 1.3 x 10^17 kg/yr of net tangential launch
  overpowers the 3:2 spin lock (D6). A planet-scale harvest (the published thought experiment runs ~10^22 kg/yr) is 10^5 times above that.
- **H-3. Free-flying catchers or depots parked at Sun-Mercury or Sun-Venus L1/L2 without continuous station-keeping.** The points are
  unstable with 3.9-d and 9.8-d doubling times.
- **H-4. A clean harvest.** Any process losing more than ~10^-7 of Mercury's mass as fine debris equals today's zodiacal cloud; no loss figure
  for any extraction method exists.
- **H-5. Moving Mercury or Venus "a little" with its own mass.** A 1% change in a costs 2.4-21% of Mercury or 1.7-16% of Venus expelled in one
  direction (D11); no published design.
- **H-6. Spinning Venus up to a short day by exporting its atmosphere.** Physically impossible: the whole atmosphere at escape speed reaches
  at best a 90-d day (D9).

## 8. Open threads

- **No N-body study of removing or reducing Venus or Mercury exists in what surfaced** (S3r, S7). Next: run a REBOUND or Mercury6 ensemble
  (with GR) with Venus's mass ramped down over 10^3 to 10^7 yr, measuring Mercury's e and Earth's eccentricity spectrum; search terms "planet
  mass removal secular resonance sweeping terrestrial", "Venus mass Milankovitch", and the Kane / Horner / Vervoort group's other papers
  (refs 28, 38, 74 in F8 not opened).
- Second-order secular theory or a published secular code would place g5 correctly; my estimates bracket the error instead.
- Gladman et al. 1996 Science 271:1387 (paywalled) and Melosh & Tonks 1993 not opened; the 30% Venus-to-Earth figure is second-hand.
- Stenborg & Howard 2018 and Jones et al. 2013/2017 not opened directly (numbers via NASA news).
- Station-keeping cost at Sun-Mercury and Sun-Venus L1/L2 with solar radiation pressure: no study found; next search "libration point orbit
  Mercury Sun L1 BepiColombo station keeping" and "solar sail displaced L1 Mercury".
- Correia & Laskar 2001 and 2004 (Nature) read only at abstract level; Margot et al. 2012 C/MR^2 and Genova et al. 2019 only via summary.
- No study of launch torque on a planet's spin, of mass-driver recoil on a planet's orbit, or of tidal stress during planetary unloading was
  found. Next: "mass driver torque planet rotation", "asteroid spin change mass driver ejecta" (asteroid-deflection literature is the nearest
  analog), "global unloading decompression melting planet".
- The heliocentric dust-input rate of the natural cloud (600 to 10,000 kg/s in summaries) was not confirmed on a page.
- Not covered: Yarkovsky drift of meter-to-kilometer cargo near Mercury (Xu et al. 2022 and Lacki 2025 point to it); the effect of a large
  co-orbital swarm's own mass on Mercury (negligible unless the swarm approaches a planetary mass).

## 9. Rejected sources

- **Nordley, "The Snows of Venus" (1991 short story)**: fiction; recorded only as the origin of the atmosphere-export spin-up idea (S30).
- **NewMars forum and Kerbal forum threads** on spinning Venus (S32): unsourced; my own arithmetic (D9) was used instead.
- **Universe Today / phys.org / Sci.News / ScienceAlert / SpaceRef / EarthSky** summaries (S14, S20, S30): leads only.
- **Search-result summaries carrying numbers** (S6, S12, S16, S23, S26, S34, S35): no number used unless confirmed on an opened page; S23's
  "700,000 yr" and S34's "just over 2 m/s per year for SOHO" were not confirmed and were dropped.
- **Wikipedia (Poynting-Robertson effect, Moment of inertia factor, Terraforming of Venus)**: surfaced, not opened; primaries used.
- **Cornell 1996 news release** (F21): superseded by Gladman & Coffey 2009 for Mercury; kept only in Conflicts.
