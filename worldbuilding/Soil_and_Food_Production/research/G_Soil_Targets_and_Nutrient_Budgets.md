## PROGRESS (tick after each question is fully written to this file)
- [x] Q1
- [x] Q2
- [x] Q3
- [x] Q4
- [x] Q5
- [x] Q6
- [x] FINAL

# G — Soil Targets and Nutrient Budgets (real-world research)

*Research slice G of the Soil and Food Production spec. Real-world agronomy and soil science only; nothing about the fictional setting. Started 2026-10-25. Written as it went: each question was appended as soon as it was finished.*

**Status markers:** SOURCED = taken from a source that was opened and read · COMPUTED = arithmetic shown, assumptions stated · UNVERIFIED = seen only secondhand or in a snippet, not confirmed against the original · NOT FOUND = searched and not located.

---

## 1. Findings summary and key-figures table

**Summary (written at the end, 2026-10-25).**
- **A usable soil** has quantitative targets that published sources do state: bulk density below ~1.4 g/cm³ for loams (root restriction above 1.47–1.80 depending on texture), at least 10% air-filled porosity, available water of roughly 0.13–0.19 m³/m³ for loams and silt loams, crop-specific pH targets of 6.0–6.8 (blueberry 4.8, scab-prone potato 5.2), and salinity thresholds from 1.0 dS/m (bean, carrot) to 8 dS/m (barley). It also needs CEC (organic matter supplies 200–400 cmol/kg against 1–5 for sand), soil-test sufficiency levels, and depth (> 75 cm counts as "highly suitable" for most field crops in one implementation of the Sys et al. scheme). No source gave a single sourced "target SOM %".
- **Built soils are classifiable.** WRB 2022 classifies any material within 2 m of the surface, including soils on roofs and in pots (Isolatic). A mixture becomes a Technosol at ≥ 20% artefacts. Historical built soils (hortic, plaggic, terric, pretic) have explicit SOC, P and thickness thresholds. Terra preta holds ~2.7× the organic carbon of neighboring soils and up to 70× the black carbon. Its anthropic origin was challenged in 2021 and defended in 2022.
- **Nutrient budget:** a person excretes about as much N and P as they eat: 4.4–4.6 kg N, 0.55–0.58 kg P and 1.2–1.8 kg K per year. For 100,000 people that is ~440–455 t N, 55–58 t P and 120–180 t K in the food eaten. At world-average cereal fertilizer efficiencies, the fertilizer-equivalent need is ~1,250–1,300 t N, ~340–365 t P and ~630–950 t K. Real urine-diversion systems captured 36–60% of excreted N.
- **Supply:** Haber–Bosch at best practice uses 28 GJ/t NH₃ (34 GJ/t N); the all-electric route uses 36 GJ of electricity per t NH₃ (12.2 MWh per t N). Plasma NOx's best figure is ~5× worse. Phosphate rock reserves are 73 Gt and potash reserves > 5.9 Gt K₂O (USGS 2026).
- **Water:** seasonal crop needs run 300–800 mm for most food crops. Tomato water use runs from 100–300 L/kg in open fields down to 4 L/kg in a closed Dutch greenhouse.
- **Area:** soil-based complete diets need ~1,300–10,800 m² per person on real US land (diet-dependent). Biosphere 2's soil-and-sunlight agriculture needed ~250 m² per person for 81% of the diet. Electric-lit BIOS-3 and NASA designs need ~40–56 m².

| # | Figure | Value | Unit | Source | Date | Status |
|---|---|---|---|---|---|---|
| 1 | Bulk density restricting roots, loam / clay | > 1.80 / > 1.47 | g/cm³ | SDSU Extension (Klopp and Bly) Table 1 | 2023 | SOURCED |
| 2 | Minimum air-filled porosity (LLWR limit) | 10 | % by volume | da Silva, Kay and Perfect, SSSAJ | 1994 | SOURCED |
| 3 | Penetration resistance limit (LLWR) | 2.0 | MPa | da Silva, Kay and Perfect | 1994 | SOURCED |
| 4 | Available water, loam / silt loam | 0.13–0.18 / 0.13–0.19 | m³/m³ | FAO-56 Table 19 | 1998 | SOURCED |
| 5 | Rooting depth, wheat (spring) / potato / lettuce | 1.0–1.5 / 0.4–0.6 / 0.3–0.5 | m | FAO-56 Table 22 | 1998 | SOURCED |
| 6 | Salinity threshold ECe: bean / maize / wheat / barley | 1.0 / 1.7 / 6.0 / 8.0 | dS/m | FAO Paper 29 Annex 1 (Maas–Hoffman) | 1985 / 1999 | SOURCED |
| 7 | Target pH, most crops / alfalfa / blueberry | 6.0 / 6.8 / 4.8 | water pH | Univ. of Delaware (Gartley, Shober, Sims) | 2024 | SOURCED |
| 8 | CEC of SOM / sand / clay | 200–400 / 1–5 / > 30 | meq/100 g | UGA Circular 1040 | 2022 | SOURCED |
| 9 | Microbial diet C:N (immobilization above) | 24:1 | ratio | USDA NRCS C:N sheet | 2011 | SOURCED |
| 10 | DTPA critical levels Zn / Fe / Mn / Cu (corn) | 0.8 / 4.5 / 1.0 / 0.2 | ppm | Lindsay and Norvell, SSSAJ | 1978 | SOURCED |
| 11 | Soil depth "highly suitable", cereals and vegetables | > 75 | cm | `soilassessment` R package citing Sys et al. 1993 | — | UNVERIFIED vs original |
| 12 | Technosol threshold | ≥ 20 | % artefacts by volume, upper 100 cm | IUSS WRB 4th ed. | 2022 | SOURCED |
| 13 | Terra preta OC stock vs adjacent soils (0–30 cm) | 2.7× (≈ 250 Mg ha⁻¹ m⁻¹) | — | Glaser et al., Naturwissenschaften | 2001 | SOURCED |
| 14 | Plaggen accumulation rate | 1.14 | mm/yr | Choi et al., SOIL | 2024 | SOURCED |
| 15 | N removal: wheat / soybean / potato | 20.0 / 55.0 / 3.1 | kg N per t harvested | IPNI via Univ. Arkansas FSA2176; CDFA | — | COMPUTED from SOURCED |
| 16 | P₂O₅ / K₂O removal, winter wheat grain | 6.5 / 5.5 | kg per t fresh | PDA / AHDB RB209 | 2020 | SOURCED |
| 17 | Excreted per person, Sweden: N / P | 4.55 / 0.548 | kg/yr | Jönsson et al. (EcoSanRes) Table 1 | 2004 | SOURCED |
| 18 | Excreted per person, world 2023 diet: N / P | 4.37 / 0.58 | kg/yr | Jönsson equations × OWID/FAO protein supply | 2023 data | COMPUTED |
| 19 | Biosolids per person | 21 | kg dry solids/yr | National Research Council | 2002 | SOURCED |
| 20 | 100,000 people, N / P / K in food eaten | 437–455 / 55–58 / 120–180 | t/yr | this file §3e | — | COMPUTED |
| 21 | 100,000 people, fertilizer-equivalent at world cereal efficiencies (N 35%, P 16%, K 19%) | 1,250–1,300 N / 343–365 P / 630–950 K | t/yr | this file §3e | — | COMPUTED |
| 22 | Urine diversion + fecal separation recovery N / P / K | 60 / 46 / 43 | % | Vinnerås and Jönsson, Bioresource Tech. | 2002 | SOURCED |
| 23 | P recovery from sewage sludge ash | 60–90 | % of wastewater P | Egle et al., Sci. Total Environ. | 2016 | SOURCED |
| 24 | Alfalfa N fixation | 50–300 (56–336) | lb/acre/yr (kg/ha/yr) | Alabama Extension ANR-3023 | 2023 | SOURCED (kg COMPUTED) |
| 25 | Global agricultural BNF | 50–70 | Tg N/yr | Herridge, Peoples and Boddey, Plant Soil | 2008 | SOURCED |
| 26 | Haber–Bosch BAT energy (natural gas, net) | 28 (≈ 34 per t N) | GJ/t NH₃ | IEA Ammonia Technology Roadmap | 2021 | SOURCED (per N COMPUTED) |
| 27 | Electrolytic ammonia electricity | 36 GJ/t NH₃ = 12.2 MWh/t N | — | IEA | 2021 | SOURCED / COMPUTED |
| 28 | Plasma NOx best energy | 2.4 MJ/mol N (≈ 171 GJ/t N) | — | Rouwenhorst et al., EES (corr. 2023) | 2021 | SOURCED / COMPUTED |
| 29 | World phosphate rock reserves / production | 73,000 / 250 | Mt / Mt per yr (2025e) | USGS MCS | Feb 2026 | SOURCED |
| 30 | World potash reserves / production | > 5,900 / 49 | Mt K₂O / Mt K₂O per yr (2025e) | USGS MCS | Feb 2026 | SOURCED |
| 31 | Seasonal water need: wheat / maize / potato / tomato | 450–650 / 500–800 / 500–700 / 400–800 | mm | FAO Training Manual 3, Table 5 | 1986 | SOURCED |
| 32 | Consumptive water footprint: wheat / potato / tomato / dry beans | 1,619 / 224 / 171 / 4,070 | m³/t | Mekonnen and Hoekstra, HESS | 2011 | COMPUTED from SOURCED |
| 33 | Drip vs furrow application efficiency | 85–95 vs 45–65 | % | Rudnick and Irmak (Nebraska/Wyoming E3A) | 2015 | SOURCED |
| 34 | Tomato water use: open field / Spanish parral / Dutch closed greenhouse | 100–300 / 40 / 4 | L/kg | Nederhoff and Stanghellini (Van Kooten et al. 2008) | 2010 | SOURCED |
| 35 | Diet land need, US, 10 diets | 0.13–1.08 | ha/person/yr | Peters et al., Elementa | 2016 | SOURCED |
| 36 | Biosphere 2 crop area per person (81% of diet) | 250 | m² | Silverstone | 1997 | SOURCED (÷8 COMPUTED) |
| 37 | BIOS-3 plant area per person at 100% food closure | 56 (8.5 kW PAR/person) | m² | Salisbury, Gitelson and Lisovsky, BioScience Table 2 | 1997 | SOURCED |
| 38 | NASA BLSS crop area per person | 40–50 | m² | Johnson et al., Front. Astron. Space Sci. | 2021 | SOURCED |
| 39 | World cropland per person | 0.194 | ha (2023) | FAO via OWID | 2023 | COMPUTED from SOURCED |

---

## 2. Findings by question

### Q1. Target properties of a productive cropland soil or growing medium

*Finished 2026-10-25. All sources accessed 2026-10-25.*

**Method caveat, learned during this question:** a page-summarizing fetch tool returned "Table 19" values for FAO-56 that were single numbers not present in the original (the original gives ranges). Every FAO-56 figure below was then re-checked against the raw page text downloaded with curl. Treat any number in this file marked SOURCED as checked against the source text, not against a summary.

#### 1a. Texture (USDA / NRCS Soil Survey Manual 2017 classes)

Source: Buness, Schad and Rau, *The Ultimate Soil Texture Flow Chart*, Technical University of Munich, 11 Jan 2022, which reproduces the texture-class table "according to NRCS Soil Survey Manual (2017)". https://wrb.isric.org/files/The_Ultimate_Soil_Texture_Flow_Chart_2022-01-11.pdf — **SOURCED** (secondary reproduction of the NRCS table; the NRCS manual itself was not opened).

| Class | % sand | % silt | % clay |
|---|---|---|---|
| Sand | > 85 | < 15 | < 10 (and silt + 1.5×clay < 15) |
| Loamy sand | > 70 to ≤ 90 | < 30 | < 15 |
| Sandy loam | > 52 to ≤ 85 (or > 43 to ≤ 52 with silt 41–50 and clay < 7) | ≤ 48 | < 20 |
| **Loam** | **> 23 to ≤ 52** | **≥ 28 to < 50** | **≥ 7 to < 27** |
| Silt loam | ≤ 50 | ≥ 50 to < 80 (or ≥ 80 to ≤ 88 with clay 12–20) | < 27 |
| Silt | ≤ 20 | ≥ 80 | < 12 |
| Sandy clay loam | > 45 to ≤ 80 | < 28 | ≥ 20 to < 35 |
| Clay loam | > 20 to ≤ 45 | > 15 to < 53 | ≥ 27 to < 40 |
| Silty clay loam | ≤ 20 | > 40 to ≤ 73 | ≥ 27 to < 40 |
| Sandy clay | > 45 to ≤ 65 | < 20 | ≥ 35 to < 55 |
| Silty clay | ≤ 20 | ≥ 40 to ≤ 60 | ≥ 40 to ≤ 60 |
| Clay | ≤ 45 | < 40 | ≥ 40 |

- Particle-size boundaries in that chart follow **ISO 11277:2009**: clay ≤ 2 µm, silt > 2–63 µm, sand > 63 µm–2 mm (same source). Note: the USDA system puts the silt/sand boundary at 50 µm, not 63 µm — **UNVERIFIED here** (not opened in a USDA document this session).
- No single source found that states "the ideal texture for crop X is Y%". What sources do give, crop by crop, are the *consequences* of texture (water-holding, bulk-density limits, CEC), below. Loam and silt loam carry the highest plant-available water per meter of soil (1d).

#### 1b. Bulk density and porosity

Source: Klopp, H. and Bly, A., "Bulk Density: An Indicator of Soil Health," SDSU Extension, updated 22 Sep 2023, Table 1. https://extension.sdstate.edu/bulk-density-indicator-soil-health — **SOURCED**. The same three-band summary appears on the Illinois Soil Quality site (https://soilquality.nres.illinois.edu/bulk-density/, "Table 1. General relationship of soil bulk density to root growth based on soil texture"), which is the NRCS Soil Quality Indicator table in simplified form.

| Texture | Ideal bulk density (g/cm³) | Restricts root growth (g/cm³) |
|---|---|---|
| Sand, loamy sand | < 1.60 | > 1.80 |
| Sandy loam, loam | < 1.40 | > 1.80 |
| Sandy clay loam, clay loam | < 1.40 | > 1.75 |
| Silt, silt loam | < 1.40 | > 1.75 |
| Silty clay loam | < 1.40 | > 1.65 |
| Sandy clay, silty clay | < 1.10 | > 1.58 |
| Clay | < 1.10 | > 1.47 |

- "Ideal soil porosity is considered to be 50%, which corresponds to a bulk density of about … 1.33 g cm⁻³" (SDSU, same page) — **SOURCED**. Check: (1 − 0.50) × 2.65 g/cm³ (assumed mineral particle density) = 1.325 g/cm³ — **COMPUTED**, consistent.
- **Least Limiting Water Range** critical limits (da Silva, Kay and Perfect 1994, *Soil Sci. Soc. Am. J.* 58:1775, doi:10.2136/sssaj1994.03615995005800060028x, abstract read via OpenAlex): field capacity −0.01 MPa; wilting point −1.5 MPa; **minimum air-filled porosity 10%**; **soil penetration resistance limit 2.0 MPa**. LLWR fell sharply above bulk density **1.36 g/cm³ (silt loam)** and **1.43 g/cm³ (loamy sand)** — **SOURCED**.
- Magdoff and van Es, *Building Soils for Better Crops* 4th ed. (SARE), §6.05: roots need "at least 20% of the pore space (about 10% of the volume of the whole soil) to be air filled" — **SOURCED**.

#### 1c. Container / soilless growing media

- Search-result summaries gave "50–85% total porosity, 10–30% air space, 45–65% container capacity, bulk density 0.19–0.70 g/cm³" as nursery-substrate guidelines — **UNVERIFIED**: three pages that should carry the figures were opened; one (UGA Circular 1292-04, Yu and Gu, 30 Jan 2024, https://fieldreport.caes.uga.edu/publications/C1292-04/) gave only "air space … optimal range (15%–30%)", the Arkansas greenhouse unit returned HTTP 403, and the original attribution was not found.
- pH: "6.2 to 6.8 in soil-based substrate and 5.4 to 6.6 in soilless substrate" for most greenhouse crops — greenhouse-management.com, *Greenhouse Management* ch. 12 (Apex Publishers; no author or date on page) — **SOURCED** (weak source).

#### 1d. Water-holding capacity and rooting depth

FAO Irrigation and Drainage Paper 56 (Allen, Pereira, Raes and Smith 1998), **Table 19**, "Typical soil water characteristics for different soil types". https://www.fao.org/4/x0490e/x0490e0c.htm — **SOURCED** (raw page text).

| Soil type | θFC (m³/m³) | θWP (m³/m³) | Available θFC − θWP (m³/m³) |
|---|---|---|---|
| Sand | 0.07–0.17 | 0.02–0.07 | 0.05–0.11 |
| Loamy sand | 0.11–0.19 | 0.03–0.10 | 0.06–0.12 |
| Sandy loam | 0.18–0.28 | 0.06–0.16 | 0.11–0.15 |
| Loam | 0.20–0.30 | 0.07–0.17 | 0.13–0.18 |
| Silt loam | 0.22–0.36 | 0.09–0.21 | 0.13–0.19 |
| Silt | 0.28–0.36 | 0.12–0.22 | 0.16–0.20 |
| Silty clay loam | 0.30–0.37 | 0.17–0.24 | 0.13–0.18 |
| Silty clay | 0.30–0.42 | 0.17–0.29 | 0.13–0.19 |
| Clay | 0.32–0.40 | 0.20–0.24 | 0.12–0.20 |

- 0.10 m³/m³ available water = 100 mm water per m of soil depth — **COMPUTED** (unit conversion; FAO-56 Example 36 uses the same: 0.15 − 0.06 = 90 mm/m for loamy sand).
- Cross-check in US units: Clark, C.A., "The important role of soil texture on water," UW–Madison Crops and Soils Extension (no date), table citing the USDA-NRCS infiltration guide: coarse sand 0.25–0.75 in/ft; loamy sand 1.1; sandy loam 1.2–1.4; loam 1.95; silt loam 2.00–2.50; silty clay loam 1.8–2.0; clay 1.2–1.5 in/ft. https://cropsandsoils.extension.wisc.edu/articles/the-important-role-of-soil-texture-on-water — **SOURCED**. 1 in/ft = 25.4 mm / 0.3048 m = 83.3 mm/m, so loam 1.95 in/ft ≈ 162 mm/m — **COMPUTED**.

**FAO-56 Table 22**, maximum effective rooting depth Zr (m) and depletion fraction p (for ETc ≈ 5 mm/day). https://www.fao.org/4/x0490e/x0490e0e.htm — **SOURCED** (raw page text). "The larger values for Zr are for soils having no significant layering … The smaller values … may be used for irrigation scheduling."

| Group | Crop: Zr (m), p |
|---|---|
| Cereals | Spring wheat 1.0–1.5, 0.55 · Winter wheat 1.5–1.8, 0.55 · Barley 1.0–1.5, 0.55 · Oats 1.0–1.5, 0.55 · Maize grain 1.0–1.7, 0.55 · Sorghum grain 1.0–2.0, 0.55 · Millet 1.0–2.0, 0.55 · Rice 0.5–1.0, 0.20 (of saturation) |
| Legumes | Beans dry/pulses 0.6–0.9, 0.45 · Beans green 0.5–0.7, 0.45 · Soybeans 0.6–1.3, 0.50 · Chickpea 0.6–1.0, 0.50 · Lentil 0.6–0.8, 0.50 · Peas fresh 0.6–1.0, 0.35 · Groundnut 0.5–1.0, 0.50 · Faba bean 0.5–0.7, 0.45 |
| Roots and tubers | Potato 0.4–0.6, 0.35 · Sweet potato 1.0–1.5, 0.65 · Cassava yr 1 0.5–0.8, 0.35; yr 2 0.7–1.0, 0.40 · Beets 0.6–1.0, 0.50 · Sugar beet 0.7–1.2, 0.55 · Turnip 0.5–1.0, 0.50 · Carrots 0.5–1.0, 0.35 |
| Leafy / small vegetables | Lettuce 0.3–0.5, 0.30 · Spinach 0.3–0.5, 0.20 · Cabbage 0.5–0.8, 0.45 · Broccoli 0.4–0.6, 0.45 · Celery 0.3–0.5, 0.20 · Onion 0.3–0.6, 0.30 · Garlic 0.3–0.5, 0.30 · Radish 0.3–0.5, 0.30 |
| Fruit vegetables | Tomato 0.7–1.5, 0.40 · Sweet pepper 0.5–1.0, 0.30 · Eggplant 0.7–1.2, 0.45 · Cucumber 0.7–1.2, 0.50 · Squash/zucchini 0.6–1.0, 0.50 · Pumpkin 1.0–1.5, 0.35 · Melons 0.8–1.5, 0.40 · Strawberries 0.2–0.3, 0.20 |
| Forages | Alfalfa hay 1.0–2.0, 0.55 · Berseem clover 0.6–0.9, 0.50 · Ryegrass hay 0.6–1.0, 0.60 |

#### 1e. Minimum soil depth

- Soil-depth suitability thresholds as implemented in the R package `soilassessment` v1.3.1 (function `depthSuit`, citing Sys, Van Ranst, Debaveye and Beernaert 1993, *Land Evaluation Part III: Crop Requirements*, and Naidu et al. 2006). Source code read: https://raw.githubusercontent.com/cran/soilassessment/master/R/depthSuit.R and `calcSuit.R`. Cereals, grain legumes, most vegetables, alfalfa and root crops: **> 75 cm highly suitable; 50–75 moderately; 25–50 marginally; < 25 cm currently not suitable**. Fruit trees, oil crops, cotton, sugarcane and similar: > 200 cm highly; 75–200 moderately; 50–75 marginally; < 50 not suitable. — **UNVERIFIED against the original** Sys et al. tables (that book was not found online); recorded as what a published software implementation uses.
- WRB defines a **Leptosol** by continuous rock starting ≤ 25 cm from the surface — see Q2.

#### 1f. Organic matter, organic carbon, C:N

- SOM-to-SOC conversion: "Historically, a factor of 1.724 has been used … based on the assumption that organic matter is 58% carbon"; "a factor of 2 is often more suitable for soil layers rich in organic matter" (citing Pribyl 2010, *Geoderma* 156:75–83, doi:10.1016/j.geoderma.2010.02.003). SoilWise vocabulary, https://voc.soilwise-he.containers.wur.nl/id/https://soilwise-he.github.io/soil-health%23SOCToSOMConversion — **SOURCED** (vocabulary entry; Pribyl abstract not obtainable via OpenAlex or Semantic Scholar).
- "A critical level" of SOM for temperate agricultural soils: Loveland, P. and Webb, J. (2003), *Soil & Tillage Research* 70:1–18. Secondary sources say it discussed an assumed 2% SOC threshold and found weak evidence for any single threshold. **UNVERIFIED** — the abstract was elided by the publisher in Crossref, OpenAlex and Semantic Scholar, and ScienceDirect returned 403.
- **A sourced "typical SOM % for productive cropland" range: NOT FOUND** this session (see §3).
- C:N of soil organic matter: "The C:N ratio in the organic matter of agricultural soils ideally averages about 10:1" — NRCS Illinois, *Soil Tech Note 23A: Carbon:Nitrogen Ratio* (undated). https://nrcs-prod.azureedge.us/state-offices/illinois/soil-tech-note-23a-carbonnitrogen-ratio-cn — **SOURCED**.
- USDA NRCS, *Carbon to Nitrogen Ratios in Cropping Systems* (East National Technology Support Center, Jan 2011; citing Brady and Weil 2002). Mirror: https://sarep.ucdavis.edu/sites/g/files/dgvnsk9171/files/media/documents/NRCS-C_N_ratios_cropping_systems.pdf — **SOURCED**:
  - soil microbes ≈ 8:1; the microbial diet they need ≈ **24:1** (16 parts C for energy, 8 for maintenance);
  - materials above 24:1 cause temporary N immobilization, below 24:1 temporary net mineralization; compost piles aim for about 30:1;
  - Table 1: rye straw 82:1 · wheat straw 80:1 · oat straw 70:1 · corn stover 57:1 · rye cover crop at anthesis 37:1 · pea straw 29:1 · rye vegetative 26:1 · mature alfalfa hay 25:1 · rotted barnyard manure 20:1 · legume hay 17:1 · beef manure 17:1 · young alfalfa hay 13:1 · hairy vetch 11:1.

#### 1g. pH

University of Delaware, Gartley, Shober and Sims, *Measurement and Management of Soil pH for Crop Production in Delaware*, Oct 2024 (citing Shober et al. 2024 and Wyenandt et al. 2024). https://udel.edu/content/dam/udelImages/canr/pdfs/extension/factsheets/Measurement-and-Management-of-Soil-pH-for-Crop-Production.pdf — **SOURCED** (PDF text extracted). Mineral soils, water pH 1:1. "Most plants grow best … when pH values are between 5.5 and 7.0." Critical pH = "the maximum soil pH value at which liming increases crop yield" (Adams 1984).

| Group | Target pH / critical pH |
|---|---|
| Cereals | Barley, corn, oats, rye, sorghum, wheat: 6.0 / 5.5 |
| Legumes | Snap beans 6.2 / 6.0 · Lima beans 6.2 / 6.0 · Peas 6.5 / 6.0 · Alfalfa 6.8 / 6.0 |
| Roots | White potato, non-scab-resistant 5.2 / 5.0 · scab-resistant 6.2 / 5.5 · Sweet potato 6.2 / 5.5 · Carrots 6.0 / 5.5 · Beets 6.5 / 6.2 · Radish 6.5 / 6.2 · Turnip 6.5 / 6.0 |
| Leafy | Lettuce 6.5 / 6.0 · Spinach 6.5 / 6.0 · Cabbage 6.5 / 6.2 · Kale 6.5 / 6.2 · Celery 6.5 / 6.0 · Onions 6.5 / 6.0 |
| Fruit vegetables and fruit | Tomatoes 6.5 / 6.0 · Peppers 6.5 / 6.0 · Cucumbers 6.5 / 6.0 · Squash 6.5 / 6.0 · Strawberries 6.2 / 5.8 · Blueberries 4.8 / 4.2 · Apples 6.5 / 6.0 |

- Acid soils raise Al and Mn toxicity and lower P, Ca and Mg availability; alkaline soils lower Cu, Fe, Mn and Zn availability and P availability (same source) — **SOURCED**.

#### 1h. Salinity — FAO Ayers and Westcot / Maas–Hoffman

FAO Irrigation and Drainage Paper 29 Rev. 1 (Ayers and Westcot 1985), Table 4. https://www.fao.org/4/t0234e/T0234E03.htm — **SOURCED**. Irrigation water ECw restriction: none < 0.7 dS/m; slight to moderate 0.7–3.0; severe > 3.0.

Maas–Hoffman equation: **Yr = 100 − b (ECe − a)**, Yr = relative yield %, a = threshold ECe (dS/m, saturated-paste extract), b = slope (% yield loss per dS/m above threshold). FAO Annex 1, Table A1.1 (FAO Paper 29 rev. updated with Maas and Grattan 1999), https://www.fao.org/4/Y4263E/y4263e0e.htm — **SOURCED**. "In gypsiferous soils, plants will tolerate an ECe about 2 dS/m higher than indicated."

| Crop | Threshold a (dS/m) | Slope b (%/dS/m) | Rating | ECe at 50% yield (Ayers–Westcot Table 4) |
|---|---|---|---|---|
| Barley grain | 8.0 | 5.0 | T | 18 |
| Wheat (bread) | 6.0 | 7.1 | MT | 13 |
| Wheat (durum) | 5.9 | 3.8 | T | — |
| Sorghum | 6.8 | 16 | MT | 9.9 |
| Maize | 1.7 | 12 | MS | 5.9 |
| Rice (paddy) | 3.0 | 12 | S | 7.2 |
| Soybean | 5.0 | 20 | MT | 7.5 |
| Common bean | 1.0 | 19 | S | 3.6 |
| Cowpea | 4.9 | 12 | MT | — |
| Peanut | 3.2 | 29 | MS | — |
| Potato | 1.7 | 12 | MS | 5.9 |
| Sweet potato | 1.5 | 11 | MS | — |
| Sugar beet | 7.0 | 5.9 | T | 15 |
| Carrot | 1.0 | 14 | S | 4.6 |
| Onion | 1.2 | 16 | S | 4.3 |
| Lettuce | 1.3 | 13 | MS | 5.1 |
| Spinach | 2.0 | 7.6 | MS | 8.6 |
| Cabbage | 1.8 | 9.7 | MS | — |
| Tomato | 2.5 | 9.9 | MS | 7.6 |
| Pepper | 1.5 | 14 | MS | 5.1 |
| Cucumber | 2.5 | 13 | MS | 6.3 |
| Alfalfa | 2.0 | 7.3 | MS | 8.8 |
| Cotton | 7.7 | 5.2 | T | 17 |

(S = sensitive, MS = moderately sensitive, MT = moderately tolerant, T = tolerant.)

#### 1i. Cation exchange capacity

University of Georgia Extension Circular 1040, *Cation Exchange Capacity and Base Saturation* (Sonon, Kissel and Saha; reviewed 8 Sep 2022). https://fieldreport.caes.uga.edu/publications/C1040/cation-exchange-capacity-and-base-saturation/ — **SOURCED**.
- By texture (meq/100 g = cmol(+)/kg): sand 1–5 · fine sandy loam 5–10 · loam 5–15 · clay loam 15–30 · clay > 30.
- By component: kaolinite 3–15 · illite 15–40 · montmorillonite 80–100 · **soil organic matter 200–400**.
- Base saturation % = (Ca + Mg + K) / CEC × 100.

#### 1j. Plant-available N, P, K and micronutrients (soil-test sufficiency levels)

- **Nitrogen:** Pre-sidedress nitrate test (Magdoff, Univ. of Vermont): top 12 in (30 cm) sampled when corn is 6–12 in tall; "Concentrations of nitrate-N between 25 and 30 ppm indicate that application of N fertilizer likely will not increase yields." Morris, T., UConn Soil Nutrient Analysis Laboratory (undated). https://plantsoilcenter.cahnr.uconn.edu/soil-testing-to-manage-nitrogen-for-sweet-corn/ — **SOURCED**.
- **Phosphorus and potassium:** 2020 Tri-State Fertilizer Recommendations (Ohio, Indiana, Michigan; Mehlich-3 extractant), as summarized by LaBarge and Culman, Ohio State C.O.R.N. Newsletter 2022-03. https://agcrops.osu.edu/newsletter/corn-newsletter/2022-03/considerations-managing-p-k-2022 — **SOURCED (secondary; the Tri-State PDF itself was blocked at both Purdue and MSU)**. Critical Mehlich-3 P: corn and soybean 20 ppm, wheat and alfalfa 30 ppm (maintenance range for corn 20–40 ppm per search summary, UNVERIFIED). Critical Mehlich-3 K: 100 ppm (CEC < 5) and 120 ppm (CEC > 5).
- **Micronutrients:** Lindsay, W.L. and Norvell, W.A. (1978), "Development of a DTPA Soil Test for Zinc, Iron, Manganese, and Copper," *Soil Sci. Soc. Am. J.* 42:421–428 (abstract read via OpenAlex). Critical levels for corn: **Zn 0.8 ppm, Fe 4.5 ppm, Mn 1.0 ppm (tentative), Cu 0.2 ppm** (DTPA extract, near-neutral and calcareous Colorado soils). "Critical nutrient levels must be determined separately for each crop." — **SOURCED**.

### Q2. Classification of built soils: Technosols, anthropogenic soils, terra preta

*Finished 2026-10-25. Primary source: IUSS Working Group WRB (2022), *World Reference Base for Soil Resources*, 4th edition, IUSS, Vienna (first published 22 July 2022; minor corrections 18 Dec 2022). https://wrb.isric.org/files/WRB_fourth_edition_2022-12-18.pdf — full PDF downloaded and text extracted; every WRB item below is **SOURCED** from that text.*

#### 2a. What counts as a soil (WRB §1.3)

- "the object classified in the WRB is: any material within 2 m of the Earth's surface that is in contact with the atmosphere, excluding living organisms, areas with continuous ice not covered by other material, and water bodies deeper than 2 m."
- "The definition includes continuous rock, paved urban soils, soils of industrial areas, soils on buildings and other (permanent/stable) constructions, cave soils as well as subaqueous soils."
- WRB says it takes this broad approach to "avoid sterile discussion on a universally agreed definition of soil and its required thickness and stability." The traditional meaning cited: "soil is the natural medium for the growth of plants" (Soil Survey Staff 1999).
- **So under WRB, a built mixture on a roof, in a pot or on a rock surface is classifiable as a soil.** The qualifier **Isolatic** exists precisely for "soil material containing fine earth without any contact to other soil material containing fine earth (e.g. soils on roofs or in pots)", above technic hard material, a geomembrane or a continuous layer of artefacts starting ≤ 100 cm deep.

#### 2b. Technosols (WRB key, p. 97)

A soil is a **Technosol** if it has (1) **≥ 20% artefacts** (by volume, weighted average, whole soil) in the upper 100 cm or to a limiting layer, **or** a layer ≥ 10 cm thick starting ≤ 50 cm deep with ≥ 80% artefacts; and does not have an artefact-bearing argic, spodic, vertic etc. horizon starting ≤ 100 cm; and has no limiting layer (unless made of artefacts) starting ≤ 10 cm — **or** (2) a continuous, very slowly permeable to impermeable **constructed geomembrane** of any thickness, or **technic hard material**, starting ≤ 100 cm from the surface.

- **Artefacts** (§3.3.2): substances "created or substantially modified by humans as part of industrial or artisanal manufacturing processes" or brought up by humans from depth into an environment where they do not commonly occur, and still "substantially the same chemical and mineralogical properties as when first manufactured." Examples: "bricks, pottery, glass, crushed or dressed stone, wooden boards, industrial waste, plastic, garbage, processed oil products, bitumen, mine spoil and crude oil."
- **Technic hard material** (§3.3.18): consolidated industrial/artisanal material, continuous or with < 5% free space horizontally — "asphalt, concrete or a continuous layer of worked stones."
- **Black carbon is an artefact "only if it is intentionally manufactured by humans"** (§3.1.31).
- Technosol qualifiers (selected): **Urbic** — layer ≥ 20 cm within 100 cm with ≥ 20% artefacts, ≥ 35% of which are "rubble and refuse of human settlements". **Spolic** — same, ≥ 35% of artefacts "industrial products (e.g. mine spoil, dredgings, slag, ash, rubble)". **Garbic** — same, ≥ 35% of artefacts contain ≥ 20% organic carbon "(e.g. organic waste)". **Hyperartefactic** — ≥ 50% artefacts within 100 cm. **Ekranic** — technic hard material starting ≤ 5 cm. **Linic** — constructed geomembrane starting ≤ 100 cm. **Transportic** — a layer ≥ 20 cm (or ≥ 50% of the soil if a limiting layer is ≤ 40 cm deep) with < 10% artefacts, "moved from a source area outside the immediate vicinity by intentional human activity".
- Organotechnic material: "< 20% soil organic carbon and ≥ 35% (by volume) organic artefacts" (WRB overview table).
- **A key consequence for built soils:** a mixture made of *transported natural material* with < 20% artefacts (crushed rock counts as an artefact; "crushed or dressed stone" is listed) is not a Technosol by the artefact criterion — it would key out elsewhere and could carry the Transportic qualifier. **COMPUTED reading of the key, not a stated WRB example.**

#### 2c. Anthrosols and the human-made diagnostic horizons

**Anthrosols** (WRB key, p. 96): a hortic, irragric, plaggic or terric horizon ≥ 50 cm thick; or an anthraquic plus underlying hydragric horizon with combined thickness ≥ 50 cm (paddy soils); or a pretic horizon whose layers total ≥ 50 cm within 100 cm.

| Horizon | How it forms (WRB description) | Diagnostic thresholds (all also need ≥ 20 cm thickness) |
|---|---|---|
| **Hortic** (§3.1.16) | "deep cultivation, intensive fertilization and/or long-continued application of human and animal wastes and other organic residues (e.g. manures, kitchen refuse, compost and night soil)" | Munsell value and chroma ≤ 3 moist · **≥ 1% SOC** · **≥ 120 mg/kg Mehlich-3 P** in upper 20 cm · base saturation ≥ 50% · ≥ 25% of area showing animal pores, coprolites or other soil-animal traces |
| **Plaggic** (§3.1.29) | NW Central Europe, "from Medieval times until the introduction of mineral fertilizers at the beginning of the 20th century, sod and other topsoil materials were commonly used for bedding livestock… The mixture of sods and excrements was later spread on fields", producing a horizon "in places > 100 cm thick" | sand to loam texture · artefacts < 20%, or ≥ 100 mg/kg Mehlich-3 P, or spade/plow marks · value ≤ 4 moist, chroma ≤ 4 · **≥ 0.6% SOC** · base saturation < 50% unless limed · land surface raised |
| **Terric** (§3.1.36) | "addition of mineral material or a combination of mineral material and organic residues, for example, fertile mineral soil, compost, calcareous beach sands, loess or mud… In most cases, it is built up gradually over a long period of time." | evidence of added foreign material · < 10% artefacts · **≥ 0.6% SOC** · base saturation ≥ 50% · land surface raised |
| **Pretic** (§3.1.31) | "results from human activities with the addition of black carbon, especially charcoal"; Amazonian Dark Earths / Terra Preta de Índio | value ≤ 4, chroma ≤ 3 moist · **≥ 0.6% SOC** (without artefacts) · exchangeable Ca + Mg ≥ 1 cmolc/kg · **≥ 100 mg/kg Mehlich-3 P** · ≥ 1% visible black carbon by area, *or* ≥ 0.3% black-carbon C with black-C/total-OC ≥ 0.15 |

- WRB notes Mehlich-3 P is roughly double Mehlich-1 P; the pretic P threshold was raised in 2022 from 60 to 100 mg/kg (Mehlich-3). 120 mg/kg Mehlich-3 P ≈ 43.6 mg/kg Olsen P ≈ 100 mg/kg Olsen P₂O₅ (Kabała et al. 2018, cited in WRB). "Old charcoal hearths usually fail the P criterion of the pretic horizon" — charcoal alone does not make a pretic horizon.
- **Leptosols** (WRB key): continuous rock starting ≤ 25 cm from the surface, or < 20% fine earth averaged over 75 cm. **Lithic**: rock ≤ 10 cm. **Nudilithic**: rock at the surface. (Bare rock with nothing on it is still a classifiable WRB object.)

#### 2d. Terra preta (Amazonian Dark Earths): how made, properties

**Glaser, Haumaier, Guggenberger and Zech (2001)**, "The 'Terra Preta' phenomenon: a model for sustainable agriculture in the humid tropics," *Naturwissenschaften* 88:37–41, doi:10.1007/s001140000193. Full text read (SSWM mirror). **SOURCED**:
- Sites "usually occur in areas averaging 20 ha", with sites up to 350 ha; > 50,000 ha estimated between the Tapajós and Curuá-Una rivers alone.
- Studied sites had "deep (40–80 cm) black A horizons together with the presence of ceramics and charcoal particles". Texture and mineralogy match surrounding soils, i.e. they were made *from* the surrounding poor soils.
- Black carbon "up to 70 times higher (mean: four times higher)" than adjacent soils down to 60 cm. Black carbon ≈ 20% of SOM down to ~40 cm (≈ 10% in control topsoil).
- 0–30 cm: terra preta held "around 2.7±0.5 times as much OC as corresponding soils (approximately 250 Mg ha⁻¹ m⁻¹)", against ~100 Mg ha⁻¹ m⁻¹ reported for Amazonian Oxisols.
- Black carbon stocks 25 ± 10 Mg/ha (0–30 cm) and 25 ± 9 Mg/ha (30–100 cm): enrichment factors 8 ± 4 and 73 ± 28.
- Radiocarbon ages of charcoal/black carbon 1,775 ± 325 yr BP (60 cm, Santarém), and 740–2,460 yr BP (30–40 cm, cited from Saldarriaga and West 1986).
- **Proposed formation:** "low-heat smouldering domestic fires" for cooking and heating, rather than natural or slash-and-burn fires. Their simulation: pine charred at 300 °C yields ~20% charcoal; ~600 Mg/ha wood would need charring to supply the measured stocks. Nutrients: "It may be speculated that human excrement and biomass accumulated from the surrounding land, together with residues from hunting and fishing, are responsible for the nutrient richness… Proof of this is still lacking."
- Mechanism of fertility: oxidation of black carbon over centuries creates carboxylic groups that raise CEC and nutrient holding.

**Cunha et al. (2009)**, *Revista Brasileira de Ciência do Solo* 33, doi:10.1590/s0100-06832009000100009 (abstract via OpenAlex). **SOURCED** — terra preta vs. adjacent Ferralsols:

| Property | Terra preta | Adjacent Ferralsol |
|---|---|---|
| pH | 5.1–5.4 | 4.4 |
| Sum of bases (cmolc/kg) | 8.93–10.33 | 2.04 |
| CEC (cmolc/kg) | 17.2–17.5 | 9.5 |
| Base saturation | 51–59% | 21% |
| P (mg/kg) | 116–291 | 5 |
| Total C (g/kg) | 44.6–44.7 | 37.9 |

- **Macedo et al. (2017)**, *PLoS ONE* 12:e0178038 (abstract): formation processes identified at Iranduba: "(i) addition of organic residues and ceramic artifacts (cumulization) with the use of fire; (ii) mechanical action of humans, roots and macrofauna (bioturbation); (iii) melanization of deeper horizons as a result of bioturbation; (iv) argilluviation and degradation of iron nodules." Depth of the dark layer results from bioturbation carrying charcoal down. — **SOURCED**.
- **Contested origin:** Silva et al. (2021), *Nature Communications* 12:127, doi:10.1038/s41467-020-20184-2, argued from Nd/Sr isotopes and microcharcoal radiocarbon at one site that the P and Ca came from river (alluvial) deposition and that indigenous people "harnessed natural processes… but were not responsible for their genesis." Rebutted by Lombardo et al. (2022), *Nature Communications*, doi:10.1038/s41467-022-31064-2, "Evidence confirms an anthropic origin of Amazonian Dark Earths": archaeological evidence places widespread ADE formation in the Late Holocene, tracking population growth peaking ~1000 BP. A reply by Silva et al. followed (doi:10.1038/s41467-022-31065-1). Abstracts read via OpenAlex — **SOURCED**. A 2025 spatial study (*J. Archaeol. Sci.*, doi:10.1016/j.jas.2025.106169) also "supports an anthropic origin at the Caldeirão site" (title only — UNVERIFIED beyond title).

#### 2e. Other historical built soils

- **Plaggen soils (NW Europe):** at Braakmankamp (eastern Netherlands), luminescence dating gave land clearance ~900–1000 CE, plaggen accumulation starting ~1200–1300 CE, **average accumulation ≈ 1.14 mm/yr**. Choi et al. (2024), *SOIL* 10:567, doi:10.5194/soil-10-567-2024 (abstract). — **SOURCED**. A 1.14 mm/yr rate over ~700 years ≈ 80 cm — **COMPUTED** (assumes constant rate; consistent with WRB's "in places > 100 cm thick").
- **Dorotsuke (Japan):** alluvial soil carried on horseback up to Andosol fields on the Omiya Upland and matured before application, practiced an estimated 400–600 years until the early twentieth century; produced an anthropogenic horizon **56 ± 12 cm** thick in 54 of 81 fields surveyed; classed as Andic Terric Anthrosols where ≥ 50 cm. The neutral, Ca-rich alluvium later lost Ca²⁺ by leaching and acidified. Wakabayashi and Tamura (2025), *Soil Science and Plant Nutrition*, doi:10.1080/00380768.2025.2576871 (abstract). — **SOURCED**.
- **Chinampas (Aztec, Lake Xochimilco):** raised fields on artificial islands in a freshwater lake, built from "local vegetation and mud", edged with willow (*Salix bonplandiana*); canal water rises by capillarity; "a considerable portion of the fertility… is system-immanent and generated in the aquatic components"; "up to seven harvests per year." Ebel (2019/2020), *HortTechnology* 30(1):13, doi:10.21273/horttech04310-19 (abstract). — **SOURCED**.

#### 2f. Modern constructed Technosols (recipes reported in the literature)

Deeb et al. (2020), "Using constructed soils for green infrastructure – challenges and limitations," *SOIL* 6:413–434, doi:10.5194/soil-6-413-2020 — full text downloaded and read. **SOURCED**:
- Constructed Technosols are "mixtures of organic and mineral waste… designed to meet specific requirements."
- Materials tested in the French SITERRE program: excavated deep-horizon soils (acidic and basic), bricks, concrete and unsorted demolition rubble, track ballast, green wastes, sewage sludge, green-waste compost, sewage-sludge compost, paper-mill sludge, street-sweeping wastes. Others: coffee grounds, backfill, thermally treated industrial soil, recycled ferrihydrites, glass.
- Guidance: generally avoid "more than 30% organic matter" to limit loss by oxidation; mixtures from 20% to 40% compost behaved similarly hydrostructurally; recommendation of "20% to 30% compost for parks and lawns to avoid mineralization and nutrient leaching"; for trees, "10% green waste compost and 70% crushed concrete had the most favorable outcome."
- Rooftop vegetable production on urban-waste Technosols (green-waste compost, crushed wood, spent mushroom substrate; Paris, AgroParisTech, 2013–2015): yields "almost equivalent" to local horticulture; retained 74–84% of rainfall — **UNVERIFIED** (from search summary of Grard et al. 2018, *Agron. Sustain. Dev.* 38:2, doi:10.1007/s13593-017-0474-2; HAL and Springer pages both blocked).

### Q3. Nutrient removal, dietary nutrients, excreta, biosolids; 100,000-person budget

*Finished 2026-10-25. Conversions used throughout (COMPUTED from atomic masses): P₂O₅ = P × 2.291; K₂O = K × 1.205; 1 lb/short ton = 0.5 kg/t; 1 lb/bu ÷ bushel weight (lb) × 1000 = kg/t. Bushel weights assumed at US standards — corn and sorghum 56 lb, wheat and soybean 60 lb, rough rice 45 lb (standard figures, **not re-sourced this session**).*

#### 3a. Nutrients removed per metric ton of harvested product

**Table 3a-1. Grain and seed crops** (three independent sources; agreement between them is the check).

| Crop | IPNI via Univ. of Arkansas FSA2176 (kg/t, COMPUTED from lb/bu) | UK RB209 / PDA 2020 (kg/t fresh) | Swedish Food Authority 2004 via Jönsson et al. 2004 Table 6 (kg/t edible fraction) |
|---|---|---|---|
| Wheat | N 20.0 · P₂O₅ 8.0 · K₂O 4.8 | winter wheat grain: P₂O₅ 6.5 · K₂O 5.5 (grain + straw 7.0 / 10.5); other cereals grain 8.0 / 5.5 | 14% water: N 17.5 · P 3.6 (= 8.2 P₂O₅) · K 3.8 (= 4.6 K₂O) |
| Maize (grain) | N 12.0 · P₂O₅ 6.2 · K₂O 4.5 | — | dry, 10% water: N 15.1 · P 2.1 · K 2.9 |
| Rice | N 12.7 · P₂O₅ 6.7 · K₂O 3.6 (rough rice) | — | unpolished, 12%: N 12.4 · P 3.0 · K 2.3 |
| Sorghum | N 11.8 · P₂O₅ 7.0 · K₂O 4.8 | — | 11%: N 17.6 · P 2.9 · K 3.5 |
| Millet | — | — | 14%: N 16.8 · P 2.4 · K 2.2 |
| Soybean | N 55.0 · P₂O₅ 12.2 · K₂O 20.0 | — | dry, 10%: N 59.5 · P 5.5 · K 17.0 |
| Field beans / dry beans | — | field beans: P₂O₅ 11.0 · K₂O 12.0 | red beans dry: N 35.2 · P 4.1 · K 9.9 |
| Lentils | — | — | dry: N 38.4 · P 3.8 · K 7.9 |
| Peas | — | dried: P₂O₅ 9.0 · K₂O 10.0 | — |
| Oilseed rape | — | seed: P₂O₅ 14.0 · K₂O 11.0 | — |

- IPNI per-bushel values (Roberts, Kirkpatrick, Slaton and Norman, *Estimating Nutrient Removal for Row Crops Grown in Arkansas*, FSA2176, Univ. of Arkansas, Table 1, "Data for nutrient removal obtained from International Plant Nutrition Institute"): corn 0.67 / 0.35 / 0.25; sorghum 0.66 / 0.39 / 0.27; rice 0.57 / 0.30 / 0.16; soybean 3.3 / 0.73 / 1.2; wheat 1.2 / 0.48 / 0.29 lb N / P₂O₅ / K₂O per bushel. https://www.uaex.uada.edu/publications/pdf/FSA-2176.pdf — **SOURCED**; kg/t conversion **COMPUTED**.
- Potash Development Association (UK), *Phosphate and Potash Removal by Crops*, March 2020; values "can also be found in the AHDB Nutrient Management Guide (RB209), 2020"; "per metric ton of fresh material harvested." https://www.pda.org.uk/wp/wp-content/uploads/2020/03/pda-pprc.pdf — **SOURCED**.
- Jönsson, H., Richert Stintzing, A., Vinnerås, B. and Salomon, E. (2004), *Guidelines on the Use of Urine and Feces in Crop Production*, EcoSanRes Publication Series 2004-2, Stockholm Environment Institute, Table 6 (maize dry from USDA 2004). Retrieved from the Internet Archive copy of http://www.ecosanres.org/pdf_files/ESR_Publications_2004/ESR2web.pdf — **SOURCED**. (The table header says "kg/ha" but the rows are per 1,000 kg harvested; read as kg per metric ton.)
- Second check on N: California Crop Fertilization Guidelines (CDFA FREP / UC Davis), wheat (common), weighted average **43.0 lb N/ton at 12% moisture = 21.5 kg N/t** (range 32.1–52.7 lb/ton). https://www.cdfa.ca.gov/is/ffldrs/frep/FertilizationGuidelines/N_Wheat.html — **SOURCED**; conversion COMPUTED.
- Uptake is larger than removal: "an 8 t/ha wheat crop removes only about 45 kg K₂O in the grain, the growing crop can contain 300 kg/ha K₂O" (PDA 2020) — **SOURCED**. Harvest index "for N and P is often quite high with > 75% of the total nutrients taken up removed in the harvested grain…; the nutrient harvest index for K and micronutrients is typically < 50%" (FSA2176) — **SOURCED**.

**Table 3a-2. Potatoes, roots and vegetables** (kg per metric ton fresh weight)

| Crop | N (CDFA weighted average, COMPUTED from lb N/ton) | N, P, K (Jönsson et al. 2004 Table 6) | P₂O₅, K₂O (PDA/RB209 2020) |
|---|---|---|---|
| Potato | 3.12 (range 2.04–4.61) | N 2.9 · P 0.3 · K 4.7 (80% water) | P₂O₅ 1.0 · K₂O 5.8 |
| Carrot | 1.65 (0.86–3.68) | — | 0.7 · 3.0 |
| Onion | 1.97 (0.80–3.15) | N 1.9 · P 0.4 · K 1.9 | bulb 0.7 · 1.8 |
| Tomato (processing) | 1.37 (0.95–1.80) | N 1.4 · P 0.3 · K 2.1 | — |
| Lettuce (iceberg) | 1.32 (0.88–2.37) | — | — |
| Broccoli | 5.6 (3.74–9.51) | — | — |
| Cabbage | — | white: N 2.2 · P 0.3 · K 2.7 | 0.9 · 3.6 |
| Spinach | — | N 3.0 · P 0.3 · K 5.6 | — |
| Green beans | — | N 2.9 · P 0.4 · K 2.4 | French beans 1.0 · 2.4 |
| Pumpkin | — | N 1.6 · P 0.4 · K 3.4 | — |
| Watermelon | — | N 1.0 · P 0.1 · K 1.2 | — |
| Sugar beet (roots) | — | — | 0.8 · 1.7 |

CDFA per-crop pages (https://www.cdfa.ca.gov/is/ffldrs/frep/FertilizationGuidelines/N_Potato.html and N_Carrot, N_Onion, N_Tomato, N_Lettuce, N_Broccoli): weighted averages potato 6.24, carrot 3.29, onion 3.94, processing tomato 2.73, iceberg lettuce 2.63 (romaine higher), broccoli 11.2 lb N per ton fresh weight — **SOURCED** (raw page text); kg/t **COMPUTED**.

#### 3b. Nutrients embodied in an ordinary diet, and nutrients excreted

**Food supply (FAO Food Balances via Our World in Data, CSV downloaded 2026-10-25; OWID cites the FAOSTAT release of 2025-10-28):** world average protein supply **92.2 g/person/day (2023)**, of which animal 38.7 g and plant 53.4 g; world dietary energy supply 3,006 kcal/person/day (2023). Regional 2022: Europe 112.3, Africa 66.3, Asia 93.6 g/day. https://ourworldindata.org/grapher/daily-per-capita-protein-supply · https://ourworldindata.org/grapher/daily-protein-supply-from-animal-and-plant-based-foods — **SOURCED**. Cross-check: FAO *Statistical Yearbook 2024* states "Protein supply was highest in Europe in 2022, with 112 g per person per day compared with 66 g per person per day for Africa" and world DES 2,985 kcal in 2022 (OWID 2022: 2,987) — agrees. https://openknowledge.fao.org/server/api/core/bitstreams/d784864f-7f28-49d2-903e-6680d09a9d97/content/cd2971en.html — **SOURCED**. These are *supply* figures and do not subtract household waste.

- N in supplied protein: 92.2 g × 365 / 6.25 = **5.38 kg N/person/yr** (6.25 = conventional protein-to-N factor) — **COMPUTED**.

**Excretion (Jönsson et al. 2004):**
- Table 1, Swedish default values (Vinnerås 2002), per person per year: urine 550 kg wet, 21 kg dry, **N 4.0 kg, P 0.365 kg**; feces 51 kg wet, 11 kg dry, **N 0.55 kg, P 0.183 kg**; toilet paper 8.9 kg wet; blackwater total 610 kg wet, 40.5 kg dry, **N 4.55 kg, P 0.548 kg** — **SOURCED**.
- Equations from FAO food supply: **N = 0.13 × total food protein; P = 0.011 × (total food protein + vegetal food protein)** — same units in and out — **SOURCED**.
- Applied to the 2023 world figures: N = 0.13 × 92.2 × 365 = **4.37 kg N/person/yr**; P = 0.011 × (92.2 + 53.4) × 365 = **0.58 kg P/person/yr** — **COMPUTED**.
- Table 3 (Jönsson and Vinnerås 2004), kg/person/yr total (urine / feces): China N 4.0 (3.5 / 0.5), P 0.6 (0.4 / 0.2), K 1.8 (1.3 / 0.5); South Africa N 3.4, P 0.5, K 1.6; Uganda N 2.5, P 0.4, K 1.4; India N 2.7, P 0.4, K 1.5; Haiti N 2.1, P 0.3, K 1.2 — **SOURCED**. Measured Chinese total (Gao et al. 2002): 4.4 kg N and 0.5 kg P.
- Partition (Sweden): "approximately 88% of the excreta N and 67% of the excreta P are found in the urine"; less digestible diets put less in urine (China: ~70% of N, 25–60% of P). Feces wet mass: Sweden 51, China 115, Kenya up to 190 kg/person/yr; fecal dry mass Sweden ~11, China ~22 kg. Urine volume default 1.5 L/person/day (550 L/yr); urine N "3–7 g N per liter" — **SOURCED**.
- Excreted organic matter in feces ~10 (Sweden) to 20 (China) kg/person/yr; plus ~8 kg toilet paper; after 40–70% composting loss, ~10 kg organic matter per person per year in fecal compost — **SOURCED**.
- Udert (2002, Eawag): urine "contributes about 80% of nitrogen and 60% of phosphorus" of household wastewater but < 1% of its volume — **SOURCED** (abstract, doi:10.3929/ethz-a-004541820).
- Area fertilized: urine from one person "will suffice to fertilize 300–400 m² of crop per person per year with N at a reasonable rate"; urine P up to 600 m²; fecal P (~0.2 kg) at crop removal rate fertilizes 200–300 m² of wheat at 3 t/ha, or 20–40 m² on P-poor soils needing 5–10× removal (Jönsson et al. 2004) — **SOURCED**.

#### 3c. Recovery in real sanitation and treatment systems

| System | Recovery | Source | Status |
|---|---|---|---|
| Urine-diverting toilet + fecal separation (Aquatron), Swedish household | **60% N, 46% P, 43% K** of household-wastewater nutrients collected; fecal N and P separated 73% and 58% to the dry fraction | Vinnerås and Jönsson (2002), *Bioresource Technology* 84(3):275–282 (SLU abstract page) | SOURCED |
| Passive "Urine Trap" flush toilet, field test by users, shared women's bathrooms, India (841 uses, 50 days) | **36% TN, 18% TP** separated (vs. 70–80% TN in engineering tests); urine *volume* separation 89 ± 2% — users wetting the squat plate degraded performance | Kachoria et al., *Science of the Total Environment* (PMC9742848) | SOURCED |
| P recovery from dissolved flows (e.g. struvite from digester liquor) | maximum **~25%** of WWTP influent P | Egle et al. (2016), *Sci. Total Environ.*, doi:10.1016/j.scitotenv.2016.07.019 (abstract) | SOURCED |
| P recovery from sewage sludge | **~40–50%** of WWTP input | Egle et al. (2016) | SOURCED |
| P recovery from sewage sludge ash | **60–90%** of wastewater P | Egle et al. (2016) | SOURCED |
| Global | humans discharge "a maximum of 3.7 Mt P into wastewater thereby potentially satisfying 20% of the global fertilizer demand"; only ~4% judged recoverable under 2015 market conditions | Kok et al. (2018), *HESS* 22:5781 (abstract) | SOURCED |
| Fraction of influent N retained in sludge at a conventional nitrifying–denitrifying plant | — | — | **NOT FOUND** (see §3) |

#### 3d. Biosolids (sewage sludge) per person

- "Each person discharging human waste to a wastewater treatment system produces approximately 47 dry pounds (21 kilograms) of sewage sludge each year." National Research Council (2002), *Biosolids Applied to Land: Advancing Standards and Practices*, ch. 1. https://www.nationalacademies.org/read/10426/chapter/4 — **SOURCED**. Same report: ~3.4 million dry tons land-applied or distributed, ≈ 68% of sludge from ~5,900 facilities in 37 states (as summarized from the page; first 100,000 characters read) — **SOURCED**.
- European figures from a search summary (22.5 kg DM/capita/yr; > 55 g/person/day; Austria 97 g) — **UNVERIFIED** (source pages not opened).
- Composition, Ontario BMP book *Application of Municipal Sewage Biosolids to Cropland* (PDF dated 2012), table "Characteristics of three types of sewage biosolids" (dry-weight basis): **total N** aerobic liquid 1.6–6.1%, anaerobic liquid 2.8–9.0%, dewatered 3.1–7.0%; **total P** 1.8–4.0%, 1.5–6.3%, 2.2–4.5%; total solids 1–2.4%, 1.7–7.0%, 18–40%. "Fertilizer-equivalent nitrogen equals ammonium-nitrogen plus 30% of the organic nitrogen"; "Fertilizer-equivalent phosphorus equals 40% of the total phosphorus". "Most sewage biosolids are low in potassium (K)." N and P are "about one-quarter to one-fifth" of typical blended fertilizer. https://bmpbooks.com/media/Application-of-Municiple-Sewage-Biosolids-to-Cropland-05-Biosolids-Characteristics-Affecting-Land-Application.pdf — **SOURCED**.

#### 3e. Nutrients needed to feed 100,000 people for a year — COMPUTED

**Assumptions (stated, not sourced as a single method):**
1. Adults are near nutrient balance, so the N, P and K **excreted** per year ≈ the N, P and K **eaten** per year (the basis of the Jönsson–Vinnerås equations, which were fitted from food supply to measured excretion).
2. Two diet cases: (A) Swedish default excretion (high-protein diet: Sweden supply 112.8 g protein/day in 2023, OWID); (B) world-average 2023 food supply through the Jönsson equations.
3. K is not in the Swedish Table 1; use the range of Table 3 national estimates, 1.2–1.8 kg K/person/yr, midpoint 1.5.
4. "Field application" multiplies by the world cereal fertilizer-use efficiencies (difference method): N 35% (Omara et al. 2019, *Agrosyst. Geosci. Environ.*, doi:10.2134/age2018.10.0045, 2015 value; 33% in 1999), P 16% (Dhillon et al. 2017, *Agron. J.*, doi:10.2134/agronj2016.08.0483, 1961–2013), K 19% (Dhillon et al. 2019, *Agron. J.*, doi:10.2134/agronj2018.07.0462). These efficiencies were defined for *cereals*; applying them to a whole diet that includes animal products is a simplification — animal products need feed, which raises the need further, and that is **not** included. Note that the P "balance method" efficiency was 77% (Dhillon 2017): the 16% figure counts soil-supplied P against fertilizer, so it overstates the fresh-P need on a soil already at maintenance level.

| Line | N | P (as P₂O₅) | K (as K₂O) |
|---|---|---|---|
| Per person eaten/excreted, case A (Sweden) | 4.55 kg | 0.548 kg (1.26 kg) | 1.2–1.8 kg (1.4–2.2 kg) |
| Per person, case B (world 2023) | 4.37 kg | 0.584 kg (1.34 kg) | same |
| **100,000 people, nutrients in food eaten** | **437–455 t N** | **55–58 t P (126–134 t P₂O₅)** | **120–180 t K (145–217 t K₂O)** |
| ÷ world cereal use efficiency (N 0.35, P 0.16, K 0.19) — fertilizer-equivalent applied at world-average efficiency | **1,250–1,300 t N** | **343–365 t P** | **630–950 t K** (midpoint 790 t) |
| Recoverable from the same people's excreta with the Swedish urine-diversion + fecal-separation system (60% N, 46% P, 43% K) | 262–273 t N | 25–27 t P | 52–77 t K |
| Same, with the field-tested Urine Trap toilet (36% TN, 18% TP of total excreta) | 157–164 t N | 10–11 t P | — |
| Biosolids from conventional sewers: 21 kg DS/person → **2,100 t dry solids**; at 3.1–7.0% N and 2.2–4.5% P (dewatered) | 65–147 t N in solids (fertilizer-equivalent N lower) | 46–95 t P | low |

- Arithmetic example: 4.37 kg × 100,000 = 437,000 kg = 437 t N; 437 t / 0.35 = 1,249 t N. 0.584 × 100,000 = 58.4 t P; ÷ 0.16 = 365 t P. 1.5 × 100,000 = 150 t K; ÷ 0.19 = 789 t K.
- **Inconsistency, recorded not resolved:** the biosolids P range (46–95 t) overlaps and exceeds the excreted P (55–58 t). Sludge P includes non-excreta sources (e.g. detergents, food waste, industry) and chemical P precipitation; the 21 kg DS and the Ontario composition range come from different countries and decades. They should not be combined into a single closed balance without a plant-level mass balance, which was not found.
- What this does **not** compute: the crop-by-crop harvest needed (that needs a diet composition and yields; see Q6), livestock feed, food waste between supply and plate, and losses after harvest.

### Q4. Nitrogen, phosphorus and potassium supply routes

*Finished 2026-10-25. Conversions: N fraction of NH₃ = 14.007/17.031 = 0.8224; 1 lb/acre = 1.121 kg/ha; 1 MWh = 3.6 GJ (all COMPUTED).*

#### 4a. Biological nitrogen fixation (BNF)

**Global totals — Herridge, Peoples and Boddey (2008)**, "Global inputs of biological nitrogen fixation in agricultural systems," *Plant and Soil* 311:1–18, doi:10.1007/s11104-008-9668-3 (abstract read on the UNE repository, https://rune.une.edu.au/web/handle/1959.11/16181) — **SOURCED**:
- pulses 2.95 Tg N/yr; oilseed legumes 18.5 Tg; **soybean 16.4 Tg** (77% of crop-legume fixation; 50% of crop-legume area); pasture and fodder legumes 12–25 Tg; **rice 5 Tg**; sugar cane 0.5 Tg; non-legume crop lands < 4 Tg; extensive savannas < 14 Tg; **total 50–70 Tg N/yr in agricultural systems**. Below-ground N was included.
- For scale: global ammonia production 185 Mt NH₃ in 2020 (IEA, below) = 152 Tg N — **COMPUTED** (185 × 0.8224).

**Per-hectare rates for forage legumes — Alabama Cooperative Extension ANR-3023, *Forage Legumes and Nitrogen Fixation* (Aug 2023), Table 1 "adapted from Ball et al. (2016)"**, https://www.aces.edu/wp-content/uploads/2023/08/ANR-3023_ForageLegumesAndNitrogenFixation_082223L-G.pdf — **SOURCED** (lb N/acre/yr; kg/ha COMPUTED):

| Legume | lb N/acre/yr | kg N/ha/yr |
|---|---|---|
| Alfalfa | 50–300 | 56–336 |
| Red clover | 50–250 | 56–280 |
| White clover | 30–250 | 34–280 |
| Crimson clover | 30–150 | 34–168 |
| Hairy vetch | 50–150 | 56–168 |
| Soybean (forage type) | 55–160 | 62–179 |
| Cowpea | 30–90 | 34–101 |
| Perennial peanut | 50–250 | 56–280 |
| Sericea lespedeza | 40–100 | 45–112 |

"The lower end of the range… would represent the amount of N fixed when 20 to 30 percent of the stand consists of legumes, whereas the upper end would reflect pure stands of legumes under nearly ideal growing conditions."

- Nitrogen *credits* to a following crop are smaller than fixation: Kansas State L-778 *Using Legumes in Crop Rotations*, Table 1 — alfalfa, excellent stand (> 5 plants/ft²) 120 lb/a, good 80, fair 40, poor 0; sweet clover 60–120; red clover 40–80; **soybeans 40 lb/a** (≈ 45 kg/ha) — https://bookstore.ksre.ksu.edu/pubs/L778.pdf — **SOURCED**.
- Grain soybean per hectare (Salvagiotti et al. 2008, *Field Crops Res.* 108:1–13, doi:10.1016/j.fcr.2008.03.001): **NOT FOUND** — no abstract available via OpenAlex.
- Fixed N tracks shoot N: fixed N = 0.79 × shoot N − 0.49 (forage legumes) and 0.70 × shoot N + 1.01 (grain legumes); in a nine-year organic Paris-basin rotation legumes supplied 86% of N inputs. Anglade, Billen and Garnier (2015), *Ecosphere* 6:37, doi:10.1890/es14-00353.1 (abstract) — **SOURCED**.

**Azolla (with cyanobacterium *Anabaena azollae*)** — secondary review figures only:
- Yang et al. (2025), "Role of Azolla in sustainable agriculture and climate resilience," *Frontiers in Plant Science*, doi:10.3389/fpls.2025.1661720 (full PDF text read): "In flooded rice systems, fixation rates of 2–4 kg N per hectare per day have been reported"; "supplies 40–60 kg N ha⁻¹ per cycle"; "contributes 30–60 kg N ha⁻¹ per season"; *A. filiculoides* "fixing 128 kg N/ha in 50 days"; decomposing mat "supplying 20–40 kg N/ha" — each attributed by the review to earlier primary studies (Pabby, Adhikari, Kollah, Kulasooriya and De Silva 1977, Watanabe, Kumarasinghe and Eskew 1993). **SOURCED to the review; primary studies not opened.**
- Marzouk et al. (2023), *Heliyon* 9:e13040, doi:10.1016/j.heliyon.2023.e13040 (abstract): Azolla "saved the nitrogen requirement of rice up to 60 kg N ha⁻¹" — **SOURCED**.

**Free-living cyanobacteria in flooded rice:** "a moderate potential of about 30 kg N ha⁻¹ crop cycle⁻¹," attributed to Roger and Ladha (1992), *Plant and Soil* 141:41–55 — **UNVERIFIED** (search summary only; the IRD full-text server was in maintenance, no abstract in OpenAlex). Herridge et al.'s global rice figure (5 Tg) is sourced.

**Free-living heterotrophic bacteria (upland):** a per-hectare agricultural rate was **NOT FOUND**. Herridge et al. give < 4 Tg/yr for all non-legume crop lands. Dynarski and Houlton (2017), *New Phytologist*, doi:10.1111/nph.14905 (abstract): free-living fixation "is suppressed by N fertilization and stimulated by Mo fertilization", and by P additions in tropical forests — **SOURCED** (qualitative).

#### 4b. Industrial nitrogen fixation

**Haber–Bosch — IEA (2021), *Ammonia Technology Roadmap*** (PDF via fertilizer.org, text read) — **SOURCED**:
- Global ammonia production **185 Mt in 2020** (182 Mt in 2019); "Around 70% of ammonia is used to make fertilizers."
- "Just over 70% of ammonia production is via natural gas-based steam reforming, while most of the remainder is via coal gasification" (170 bcm of gas, 75 Mtce of coal).
- Energy intensity: global average **~41 GJ/t NH₃ net** (46 gross); best available technology **28 GJ/t net (32 gross) for natural gas**, **36 GJ/t net (37 gross) for coal**; theoretical minimum via pure methane **18.6 GJ/t net (20.9 gross)**.
- **Electrolytic route:** "requiring **36 GJ of electricity per metric ton of ammonia** produced for the process as a whole, with an efficiency of 64% on a lower heating value basis for the electrolyzer. Most of the electricity (95%) is used for hydrogen production, with the remaining 5% used to power the air separation and Haber-Bosch synthesis units."
- Grid electrolysis beats best natural-gas SMR on CO₂ only if grid intensity ≤ 180 g CO₂/kWh (global average then 475 g).
- Royal Society (2020), *Ammonia: zero-carbon fertilizer, fuel and energy store* (policy briefing PDF, read): 176 Mt in 2018; "consuming 8 MWh of energy per metric ton of ammonia"; "most of the energy consumption and around 90% of the carbon emissions are from the production of hydrogen"; ~1.8% of global CO₂ emissions (~500 Mt CO₂). https://royalsociety.org/-/media/policy/projects/green-ammonia/green-ammonia-policy-briefing.pdf — **SOURCED**.

Per metric ton of **nitrogen** (COMPUTED, ÷ 0.8224): BAT natural gas 28 → **34 GJ/t N**; global average 41 → 50 GJ/t N; coal BAT 36 → 44 GJ/t N; **electrolytic 36 GJ electricity/t NH₃ → 43.8 GJ = 12.2 MWh electricity per t N**. Royal Society 8 MWh/t NH₃ = 28.8 GJ/t NH₃ = 35 GJ/t N (consistent with IEA BAT).
- Hydrogen needed: 3 × 1.008 / 17.031 = **0.178 t H₂ per t NH₃**; stoichiometric water for electrolysis 0.178 × 18.015 / 2.016 = **1.59 t water per t NH₃** (process minimum; cooling and purification water excluded) — **COMPUTED**.

**Plasma NOₓ (Birkeland–Eyde and successors) — Rouwenhorst et al. (2021)**, "From the Birkeland–Eyde process towards energy-efficient plasma-based NOx synthesis: a techno-economic analysis," *Energy & Environmental Science* 14:2520, doi:10.1039/d0ee03763j (PMC8133363; **corrected 2023**, *Energy Environ. Sci.* 16:6170, cost conversion error of 13.7×). Read via page-summary fetch, quoted sentences — **SOURCED (summary-tool reading; raw text not extracted)**:
- current best plasma NOx **2.4 MJ/mol N** (thermal arc 2.4–3.1); must fall to ~0.7 MJ/mol N to compete; electrolysis-based Haber–Bosch ~0.5–0.6 MJ/mol N; thermal-plasma theoretical limit 0.72; vibrationally promoted mechanism limit 0.2 MJ/mol N.
- Per metric ton N (COMPUTED, ÷ 14.007 g/mol): **2.4 MJ/mol = 171 GJ/t N**; 0.7 → 50 GJ/t N; 0.5–0.6 → 36–43 GJ/t N (matches the IEA electrolytic figure).

**Electrochemical (ambient) ammonia:** Zhou, Fu, Chorkendorff and Nørskov (2024), "Electrochemical Ammonia Synthesis: The Energy Efficiency Challenge," *ACS Energy Letters*, doi:10.1021/acsenergylett.4c02954 (abstract): "The current Li-mediated process has a theoretical maximum energy efficiency of ~28%" — **SOURCED**. Not commercial.

**Struvite** (MgNH₄PO₄·6H₂O, molar mass 245.4 g/mol): **5.7% N, 12.6% P, 9.9% Mg** by mass — **COMPUTED** from formula. So struvite is a P product that carries little N (about 0.45 t N per t P). Recovery limits are in Q3 (≤ 25% of WWTP influent P from dissolved flows, Egle et al. 2016).

#### 4c. Phosphorus

**Rock phosphate — USGS, *Mineral Commodity Summaries*, February 2026, "Phosphate Rock"** (S. M. Jasinski), https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-phosphate.pdf — **SOURCED**:
- World mine production (marketable rock) **239 Mt (2024), 250 Mt (2025e)**; **world reserves 73,000 Mt** (Morocco 50,000 Mt; China 3,400; Egypt 2,800; Tunisia 2,500; Russia 2,400; Algeria 2,200; Brazil 1,600; South Africa 1,500; USA 1,000; Saudi Arabia 1,000; Finland 1,000). Reserves/2025 production ≈ 292 years — **COMPUTED**.
- "World resources of phosphate rock are more than 300 billion tons. There are no imminent shortages of phosphate rock." "There are no substitutes for phosphorus in agriculture." US recycling: "None."
- World P₂O₅ in fertilizers **47.8 Mt (2025e)**, 47.1 Mt (2024); projected 51.5 Mt by 2029.
- Per person: 47.8 Mt P₂O₅ ÷ 8.09 billion (world population 2023, OWID/UN) = **5.9 kg P₂O₅ = 2.6 kg P per person per year** of fertilizer P — **COMPUTED** (year mismatch 2025 vs. 2023 population noted). Compare excreted P ≈ 0.55–0.58 kg/person/yr (Q3): fertilizer P use is ~4.5× what people excrete, consistent with the low system P efficiency in Q3.

**Recycled P streams compared:**

| Stream | P content / scale | Plant availability | Source | Status |
|---|---|---|---|---|
| Human excreta | 0.55–0.58 kg P/person/yr (67% in urine, Sweden) | urine P soluble | Jönsson et al. 2004 | SOURCED |
| Global wastewater | ≤ 3.7 Mt P/yr (≈ 20% of fertilizer demand); ~4% economically recoverable in 2015 | — | Kok et al. 2018 | SOURCED |
| Struvite from wastewater | 12.6% P | ryegrass field trial: equal to single superphosphate at 20 kg P/ha, better at 80 kg P/ha (yield 23.5 vs 17.4 Mg/ha yr 2); chickpea and wheat pot trial: similar P uptake to KH₂PO₄ at low and medium rates | De Lucca Agrelo et al. 2026, *Nutr. Cycl. Agroecosyst.*, doi:10.1007/s10705-025-10465-x; Sharma et al. 2024, *J. Soil Sci. Plant Nutr.*, doi:10.1007/s42729-024-01727-8 (abstracts) | SOURCED |
| Sewage sludge ash | 60–90% of wastewater P recoverable | depends on process | Egle et al. 2016 | SOURCED |
| Biosolids | 1.5–6.3% P (dry); fertilizer-equivalent P counted as 40% of total | slow | Ontario BMP | SOURCED |
| Animal bone char | "> 30% P₂O₅" when pyrolyzed < 850 °C, 20 min residence | "high mineral phosphate fertilizer replacement value" (authors' claim) | Someus and Pugliese 2018, *Sustainability* 10:2349, doi:10.3390/su10072349 (abstract) | SOURCED |
| Seabird guano (global flux) | seabirds excrete 591 Gg N/yr and 99 Gg P/yr; readily soluble 72.5 Gg N and 21.8 Gg P; Antarctic and Southern coasts receive the highest inputs | — | Otero et al. 2018, *Nature Communications* 9:246, doi:10.1038/s41467-017-02446-8 (abstract) | SOURCED |

Guano scale check: all seabirds' P excretion (99 Gg = 0.099 Mt P/yr) is ~0.5% of fertilizer P use (47.8 Mt P₂O₅ = 20.9 Mt P) — **COMPUTED**.

#### 4d. Potassium

**USGS, *Mineral Commodity Summaries*, February 2026, "Potash"**, https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-potash.pdf — **SOURCED**:
- World mine production **46.7 Mt K₂O (2024), 49 Mt (2025e)**; leading producers Canada 15.0, Russia 10.0, China 6.3, Belarus 6.0 Mt (2025e).
- **World reserves > 5,900 Mt K₂O equivalent** (Russia 2,000; Canada 1,100; Laos 1,000; Belarus 750); Israel and Jordan "Large" (Dead Sea brines). Reserves/2025 production > 120 years — **COMPUTED**.
- World potash fertilizer consumption **41.6 Mt K₂O (2025e)**; capacity 66.1 Mt K₂O (2025).
- Forms: muriate of potash (KCl, ≥ 95% pure), sulfate of potash, potassium magnesium sulfate (langbeinite); production by underground mining, solution mining and solar evaporation of brines (including Great Salt Lake).
- Per person: 41.6 Mt K₂O ÷ 8.09 billion = **5.1 kg K₂O = 4.3 kg K per person per year** — **COMPUTED**.
- Dhillon et al. (2019): "At current consumption rates, existing K reserves as K₂O are estimated to last 100 yr"; 71% of cereal K estimated to come from the soil — **SOURCED** (abstract).
- Recycled K: urine carries most excreted K (China 1.3 of 1.8 kg/person/yr, Jönsson et al. 2004 Table 3); biosolids are "low in potassium" (Ontario BMP) — **SOURCED**.

#### 4e. Quantities per person per year (summary)

| Route | Per person per year | Status |
|---|---|---|
| N excreted (= eaten) | 4.4–4.6 kg N | SOURCED/COMPUTED (Q3) |
| World ammonia N | 185 Mt NH₃ (2020) ÷ 7.89 billion = 19.3 kg N total, ~13.5 kg N in fertilizer (70%) | COMPUTED |
| Energy to fix the eaten N by Haber–Bosch | 4.37 kg × 34 GJ/t = 0.15 GJ (gas, BAT); electrolytic 4.37 kg × 12.2 MWh/t = 53 kWh electricity | COMPUTED |
| Energy at world-average N efficiency (12.5 kg N applied, Q3) | 0.43 GJ (gas BAT); 152 kWh electricity (electrolytic) | COMPUTED |
| Same for 100,000 people | 437–1,300 t N → 14,900–44,300 GJ (gas BAT) or **5.3–15.8 GWh electricity** (electrolytic) | COMPUTED |
| P fertilizer use (world average) | 2.6 kg P | COMPUTED |
| K fertilizer use (world average) | 4.3 kg K | COMPUTED |

### Q5. Water: crop water requirements, irrigation efficiency, field vs. protected

*Finished 2026-10-25. Unit note: 1 mm of water over 1 ha = 10 m³ (COMPUTED).*

#### 5a. Seasonal crop water need (mm per growing period)

Brouwer, C. and Heibloem, M. (1986), *Irrigation Water Management: Irrigation Water Needs*, FAO Training Manual No. 3, Part I ch. 2, **Table 5 "Approximate values of seasonal crop water needs"** and **Table 4 "Indicative values of the total growing period"**. https://www.fao.org/4/s2022e/s2022e02.htm — **SOURCED** (raw page text). These are crop evapotranspiration over the season under standard conditions; FAO says "it is much better to obtain the values locally."

| Crop | Water need (mm/season) | ≈ m³/ha (COMPUTED) | Growing period (days) |
|---|---|---|---|
| Barley / oats / wheat | 450–650 | 4,500–6,500 | 120–150 |
| Maize (grain) | 500–800 | 5,000–8,000 | 125–180 |
| Rice (paddy) | 450–700 | 4,500–7,000 | 90–150 |
| Sorghum / millet | 450–650 | 4,500–6,500 | sorghum 120–130; millet 105–140 |
| Soybean | 450–700 | 4,500–7,000 | 135–150 |
| Bean | 300–500 | 3,000–5,000 | dry 95–110; green 75–90 |
| Pea | 350–500 | 3,500–5,000 | 90–100 |
| Peanut | 500–700 | 5,000–7,000 | 130–140 |
| Potato | 500–700 | 5,000–7,000 | 105–145 |
| Sugar beet | 550–750 | 5,500–7,500 | 160–230 |
| Cabbage | 350–500 | 3,500–5,000 | 120–140 |
| Onion | 350–550 | 3,500–5,500 | dry 150–210; green 70–95 |
| Tomato | 400–800 | 4,000–8,000 | 135–180 |
| Pepper | 600–900 | 6,000–9,000 | 120–210 |
| Melon | 400–600 | 4,000–6,000 | 120–160 |
| Alfalfa | 800–1,600 | 8,000–16,000 | 100–365 |
| Sunflower | 600–1,000 | 6,000–10,000 | 125–130 |
| Cotton | 700–1,300 | 7,000–13,000 | 180–195 |
| Banana | 1,200–2,200 | 12,000–22,000 | 300–365 |
| Sugarcane | 1,500–2,500 | 15,000–25,000 | 270–365 |

- Reference-grass ET (same manual, Table 2), mm/day: desert/arid 4–6 (< 15 °C), 7–8 (15–25 °C), 9–10 (> 25 °C); humid 1–2, 3–4, 5–6 — the climate scaling behind the crop figures — **SOURCED**.
- Paddy-rice figure excludes water for land preparation, percolation and standing water — this exclusion is **UNVERIFIED** here (stated in FAO's text on rice in other chapters, not checked this session).

#### 5b. Water per metric ton of product (field crops, global averages)

Mekonnen, M.M. and Hoekstra, A.Y. (2011), "The green, blue and gray water footprint of crops and derived crop products," *Hydrology and Earth System Sciences* 15:1577–1600, doi:10.5194/hess-15-1577-2011, **Table 3**, global averages 1996–2005 (m³ per metric ton). Full PDF read — **SOURCED**. Green = rain water consumed; blue = irrigation water consumed; gray = water notionally needed to dilute N pollution (not physically consumed). "Consumptive" = green + blue — **COMPUTED**.

| Crop | Green | Blue | Gray | Total | Consumptive (green + blue) |
|---|---|---|---|---|---|
| Wheat | 1,277 | 342 | 207 | 1,827 | 1,619 |
| Rice, paddy | 1,146 | 341 | 187 | 1,673 | 1,487 |
| Maize | 947 | 81 | 194 | 1,222 | 1,028 |
| Barley | 1,213 | 79 | 131 | 1,423 | 1,292 |
| Sorghum | 2,857 | 103 | 87 | 3,048 | 2,960 |
| Millet | 4,306 | 57 | 115 | 4,478 | 4,363 |
| Potatoes | 191 | 33 | 63 | 287 | 224 |
| Sweet potatoes | 324 | 5 | 53 | 383 | 329 |
| Cassava | 550 | 0 | 13 | 564 | 550 |
| Soybeans | 2,037 | 70 | 37 | 2,145 | 2,107 |
| Beans, dry | 3,945 | 125 | 983 | 5,053 | 4,070 |
| Peas, dry | 1,453 | 33 | 493 | 1,979 | 1,486 |
| Lentils | 4,324 | 489 | 1,060 | 5,874 | 4,813 |
| Chickpeas | 2,972 | 224 | 981 | 4,177 | 3,196 |
| Groundnuts (in shell) | 2,469 | 150 | 163 | 2,782 | 2,619 |
| Cabbages | 181 | 26 | 73 | 280 | 207 |
| Lettuce | 133 | 28 | 77 | 237 | 161 |
| Spinach | 118 | 14 | 160 | 292 | 132 |
| Tomatoes | 108 | 63 | 43 | 214 | 171 |
| Cucumbers | 206 | 42 | 105 | 353 | 248 |
| Green peppers | 240 | 42 | 97 | 379 | 282 |
| Onions, dry | 192 | 88 | 65 | 345 | 280 |
| Carrots and turnips | 106 | 28 | 61 | 195 | 134 |
| Pumpkins, squash | 228 | 24 | 84 | 336 | 252 |
| Sugar beet | 82 | 26 | 25 | 132 | 108 |

- Category averages (abstract): sugar crops ~200, vegetables ~300, roots and tubers ~400, fruits ~1,000, cereals ~1,600, oil crops ~2,400, **pulses ~4,000 m³/t**. Global crop water footprint 7,404 billion m³/yr (78% green, 12% blue, 10% gray); rain-fed 5,173 Gm³, irrigated 2,230 Gm³ — **SOURCED**.

#### 5c. Irrigation efficiency

Rudnick, D.R. and Irmak, S., *E3A: System Performance and Efficiency* (Univ. of Nebraska–Lincoln; edited by M. Geiger, Univ. of Wyoming), ©2015, Table 6 "Potential water application efficiencies (Ea, %) for well-designed and managed irrigation systems. Adapted from Irmak et al. (2011)." https://www.wyoextension.org/agpubs/pubs/B-1264-step4.pdf — **SOURCED**.

| System | Potential application efficiency |
|---|---|
| Sprinkler: LEPA | 80–90% |
| Linear move / center pivot | 75–85% |
| Solid set | 70–85% |
| Side roll / hand move | 65–85% |
| Traveling gun | 65–75% |
| Furrow, conventional | 45–65% |
| Furrow, surge | 55–75% |
| Furrow with tailwater reuse | 60–80% |
| Basin | 60–75% |
| Basin (paddy) | 40–60% |
| Precision level basin | 65–80% |
| Bubbler / micro-spray / micro-point / micro-line | 80–90% / 85–90% / 85–90% / 85–90% |
| Surface drip | 85–95% |
| Subsurface drip | > 95% |

- Overall irrigation efficiency = application efficiency × conveyance efficiency (Ec can approach 100% for a pivot on a well) — same source, **SOURCED**.
- Gross irrigation need = net need ÷ efficiency: e.g. 500 mm net at 60% (furrow) = 833 mm gross; at 90% (drip) = 556 mm — **COMPUTED**.

#### 5d. Field vs. protected cultivation, water per kg

**Tomato** — Nederhoff, E. and Stanghellini, C. (2010), "Water use efficiency of tomatoes in greenhouses and hydroponics," *Practical Hydroponics & Greenhouses*, Nov/Dec 2010, starting p. 52 (Wageningen UR), https://edepot.wur.nl/156932 — **SOURCED**. Table 2 (source: Van Kooten et al. 2008), liters of water per kg fresh tomato:

| Production method | Country | L/kg |
|---|---|---|
| Open field, general | Israel, Spain, Turkey | 100–300 |
| Open field, drip irrigation | Israel | 60 |
| Unheated plastic greenhouse ("parral") | Spain | 40 |
| Unheated glasshouse | Israel | 30 |
| Unheated parral with regulated ventilation | Spain | 27 |
| Advanced controlled glasshouse with CO₂ | Netherlands | 22 |
| Same, closed (recirculating) hydroponics | Netherlands | 15 |
| Same, closed greenhouse | Netherlands | **4** |
| Greenhouse with evaporative cooling | Mexico | est. 100 (anecdotal "over 60 or even more than 90") |

- Their arithmetic: field ~300 L/m² per season ÷ 5 kg/m² = 60 L/kg; greenhouse ~1,000 L/m²/yr ÷ 50–80 kg/m²/yr = 12.5–20 L/kg, "on average… about 15 liters/kg." Field yields "3–8 kg/m²/year", greenhouse "50–80 kg/m²/year (even 100…)". Transpiration "often it is 90% of water uptake." University of Córdoba data (Table 3): field 210 (excellent management) to 693 L/kg (poor); greenhouse 53–122 L/kg — **SOURCED**.
- The Mekonnen–Hoekstra global tomato footprint (171 m³/t consumptive = 171 L/kg) sits inside the open-field range — **COMPUTED** comparison.
- Passive desert greenhouses, Central Arava (Israel), 10 farms: **94 m³/t (94 L/kg) water footprint** and **72 m²/t land footprint** per metric ton of tomatoes, whole chain to export. Ravitz Wyngaard and Kissinger (2022), *Front. Sustain. Food Syst.* 6:994920, doi:10.3389/fsufs.2022.994920 (abstract) — **SOURCED**. (Includes water for production of inputs; not directly comparable with the farm-gate L/kg above.)

**Lettuce** — Barbosa et al. (2015), *Int. J. Environ. Res. Public Health* 12:6879, doi:10.3390/ijerph120606879 (abstract), Yuma, Arizona: hydroponic greenhouse **41 ± 6.1 kg/m²/yr, 20 ± 3.8 L/kg, 90,000 ± 11,000 kJ/kg** energy; conventional field **3.9 ± 0.21 kg/m²/yr, 250 ± 25 L/kg, 1,100 ± 75 kJ/kg**. Hydroponics: 11× yield, 82× energy. The hydroponic figures were *modeled* from engineering equations, the field figures from crop budgets — **SOURCED**.

### Q6. Minimum cropland area per person vs. closed-system figures

*Finished 2026-10-25. 1 ha = 10,000 m²; 1 sq ft = 0.0929 m² (COMPUTED conversions).*

#### 6a. What the world actually uses

- World cropland **1,571 million ha (2023)**; world arable land **0.172 ha per person (2023)** — FAO data via Our World in Data CSVs (`cropland-area`, `arable-land-use-per-person`), downloaded 2026-10-25 — **SOURCED**.
- Cropland per person: 1,571 Mha ÷ 8.09 billion = **0.194 ha ≈ 1,940 m² per person (2023)** — **COMPUTED**. This includes land for feed, fiber, biofuel, export and waste, so it is an upper envelope for a real diet at today's average yields, not a minimum.
- World average yields 2023 (t/ha; FAO via OWID): wheat 3.63, maize 5.87, rice 4.76, soybeans 2.70, potatoes 22.8. Spread between farming systems, 2023: wheat 8.47 (Netherlands), 8.13 (UK) vs 2.81 (Ethiopia); potatoes 51.4 (USA), 41.8 (Netherlands) vs 12.8 (Ethiopia); maize 11.1 (USA) vs 1.41 (Niger) — **SOURCED**. These yield gaps between high- and low-input farming (roughly 3–8× for the same crop) drive area per person — ratio **COMPUTED**.

#### 6b. Published diet-based land requirements (soil-based)

| Study | Area per person per year | What it covers | Status |
|---|---|---|---|
| Peters, Wilkins and Fick (2007), *Renewable Agriculture and Food Systems*, doi:10.1017/s1742170507001767 — New York State, 42 diets (0–381 g/day meat and eggs; 20–45% calories from fat) | **0.18–0.86 ha** (1,800–8,600 m²) | complete diet incl. livestock feed and pasture; "Increasing meat in the diet increased per capita land requirements" | SOURCED (abstract) |
| Peters et al. (2016), "Carrying capacity of U.S. agricultural land: Ten diet scenarios," *Elementa* 4:000116, doi:10.12952/journal.elementa.000116 | **0.13–1.08 ha** (1,300–10,800 m²) | 10 diets incl. losses, processing, feed, land suitability; carrying capacity highest for the **lacto-vegetarian** diet; the vegan diet supported fewer people than two healthy omnivore diets | SOURCED (abstract) |
| Ecology Action / GROW BIOINTENSIVE (J. Jeavons), FAQ — hand-dug, compost-crop-heavy garden | **4,000 sq ft ≈ 372 m²** "when grown at GROW BIOINTENSIVE intermediate yields"; layout 60% compost and grain crops, 30% special root crops, 10% soft fruits and vegetables (tropics 50/30/20); salad vegetables and soft fruits alone ≈ 200 sq ft (19 m²), not a complete diet | SOURCED — **advocacy organization's claim, not peer-reviewed**; https://www.growbiointensive.org/FAQ/FAQ_RawFood.html |

- A published FAO figure for **minimum m² per person at low vs. high input** was **NOT FOUND**. The FAO/IIASA/UNFPA (1982) *Potential population-supporting capacities of lands in the developing world* reports results by country: by 2000, countries unable to feed their own populations = **65 at low inputs, 36 at intermediate, 19 at high** (FAO AEZ applications page, https://www.fao.org/4/t8300e/t8300e0b.htm; also https://www.fao.org/4/u8480e/U8480E0e.htm) — **SOURCED** for counts. Input levels as described there: low = traditional subsistence; intermediate = some fertilizer and improved varieties; high ≈ Western European farming.

#### 6c. Closed and semi-closed systems

| System | Area | Food from inside, notes | Source | Status |
|---|---|---|---|---|
| **Biosphere 2** (Arizona), first closure Sept 1991–Sept 1993, 8 crew, **soil-based** agriculture with goats, pigs, chickens; all wastes returned to soil | **2,000 m² cropping area = 250 m²/person** | "approximately **81%** of the overall nutritional needs"; diet averaged **2,200 kcal, 73 g protein, 32 g fat** per person per day; crew lost 10–20% body weight, mostly in the first 6 months; "light to be the main limiting factor"; agriculture took **25% of crew time**, animals 9%, food preparation 12% | Silverstone, S.E. (1997), "Food production and nutrition for the crew during the first 2-year closure of Biosphere 2" (PubMed abstract via OpenAlex); see also Silverstone and Nelson (1996), *Adv. Space Res.*, doi:10.1016/0273-1177(95)00861-8 | SOURCED |
| Biosphere 2 scaled to 100% (linear) | 250 ÷ 0.81 ≈ **309 m²/person** | — | — | COMPUTED (assumes linear scaling) |
| **BIOS-3** (Krasnoyarsk), 3 crew, electric light (xenon lamps, ~400 kW total), wheat, chufa and vegetables | total growing area **63 m²** for 3 people = 21 m²/person (animal products, ~25% of food mass, supplied from outside) | Table 2, parameters by degree of closure: **85% closure → 35% of food regenerated, 13 m² of plants per person, 2.0 kW PAR per person; 95% → 80%, 30 m², 4.6 kW; 99% → 100%, 56 m², 8.5 kW** (relative system size 1.0 / 2.3 / 4.0). "Recycling reduced the crew requirements to only 4.6% of the requirements without recycling." Mineral closure in the third experiment only ~20%, nitrogen ~40% | Salisbury, Gitelson and Lisovsky (1997), "Bios-3: Siberian Experiments in Bioregenerative Life Support," *BioScience* 47(9), from p. 575, doi:10.2307/1313164; PDF (SIMOC mirror) read; Table 2 read from the rendered page image | SOURCED |
| **NASA** bioregenerative life support studies | "estimates ranging from about **40 to 50 m²** (or more) of crop growing area needed per person" | — | Johnson et al. (2021), *Front. Astron. Space Sci.* 8:734343, doi:10.3389/fspas.2021.734343 (abstract) | SOURCED |
| **Lunar Palace 1** (Beijing), "Lunar Palace 365", 370 days, 8 crew in rotating groups | plant area **NOT FOUND** | "The efficiency of plant production completely met the crew's need of plant-based food"; material closure 98.2%; urine recovery 99.7%; solid waste 67% | Fu et al. (2021), bioRxiv doi:10.1101/2021.01.12.426282 (abstract) | SOURCED (area NOT FOUND) |

#### 6d. Comparison (COMPUTED from the rows above)

| Basis | m² per person | Multiple of NASA's 40–50 m² |
|---|---|---|
| BIOS-3 design, 100% plant food, electric light 8.5 kW PAR/person | 56 | ~1.1–1.4× |
| NASA BLSS estimates | 40–50 | 1× |
| Biosphere 2, soil-based, sunlight, 81% of needs (incl. small livestock) | 250 (309 scaled to 100%) | ~5–8× |
| GROW BIOINTENSIVE claim, hand garden, intermediate yields, includes compost crops | 372 | ~7–9× |
| Lacto-vegetarian, US agricultural land incl. losses (Peters 2016, low end) | 1,300 | ~26–33× |
| New York State diets (Peters 2007) | 1,800–8,600 | ~36–215× |
| World cropland per person, 2023 (all uses) | 1,940 | ~39–49× |

- What separates the closed-system and field numbers, as the sources state them: continuous electric light (BIOS-3 ~400 kW for 63 m²; 2.0–8.5 kW of photosynthetically active radiation per person), year-round cropping, high-yield cultivars and no fallow or feed crops; Biosphere 2 used sunlight and soil and found light the main limit.

---

## 3. NOT FOUND / open threads

**NOT FOUND (searched; where):**
1. **A sourced target SOM % / SOC % range for productive cropland.** Searched for Loveland and Webb (2003), whose abstract was elided at Crossref, OpenAlex and Semantic Scholar, with ScienceDirect returning 403. The Oklahoma State factsheet returned 403. NRCS pages gave the C:N ratio but no SOM range.
2. **Original Sys et al. (1993) crop-requirement tables** (soil depth, texture by crop). Library catalog records only; the depth thresholds come from a software implementation (UNVERIFIED).
3. **Fraction of influent N retained in sludge at a conventional nitrifying–denitrifying WWTP.** Two WebSearches died at the query; OpenAlex searches returned no usable abstract; the Sengupta et al. 2015 review has no abstract.
4. **Grain-soybean N fixation per hectare** (Salvagiotti et al. 2008 meta-analysis): no abstract available.
5. **Free-living cyanobacteria N fixation in rice per crop** (Roger and Ladha 1992): the IRD server was in maintenance and no abstract was available. The ~30 kg N/ha/crop figure is UNVERIFIED.
6. **Upland free-living bacterial N fixation, kg N/ha/yr, in cropland.** Only the global total (< 4 Tg) and qualitative controls were found.
7. **Historical guano N/P analyses** (e.g. Peruvian guano grades): died at the query.
8. **An FAO per-person cropland area at low vs. high input:** the FAO 1982 study pages give country counts only.
9. **Lunar Palace 1 plant-growing area:** bioRxiv returned HTTP 429.
10. **Food energy (kcal/kg) values for a calorie-only area calculation:** the USDA FoodData Central API was rate-limited, so the calculation was **deliberately not done** rather than done with recalled values.
11. **The original attribution of the container-substrate ranges** (50–85% total porosity, 10–30% air space, 45–65% container capacity): only search summaries carried them, and three candidate pages lacked them or were blocked (UNVERIFIED).
12. **Tri-State 2020 Fertilizer Recommendations PDF itself:** blocked at Purdue (404/HTML) and MSU (HTML/empty). Values were taken from the OSU newsletter summary.

**Open threads (for a later pass):**
- Rouwenhorst et al. 2021 plasma figures were read through a page-summary tool, not the raw text. Re-check against the PMC full text, and against the 2023 correction (EES 16:6170), which changed costs, not energy, per the notice.
- Recalculate the 100,000-person budget with a defined diet (crop list and yields) once food-composition data can be fetched, so it rests on crop removals (Q3a) rather than excretion.
- Biosolids P (46–95 t per 100,000 people) exceeds excreted P (55–58 t). This needs a plant-level mass balance to reconcile (non-excreta P, chemical precipitation, differing countries and dates).
- Bushel weights (56 / 60 / 45 lb) were used from standard practice and not re-sourced this session.
- USDA vs ISO silt/sand boundary (50 vs 63 µm): the USDA side was not opened.
- The Brattleboro / Massachusetts urine-diversion program reports (US field data) surfaced but were not opened.
- Wheeler's primary NASA papers (source of the 40–50 m² figure) were not opened. The figure comes from a 2021 NASA-authored review.

---

## 4. Full search log

*Spelling note: per the house American-English rule, British spellings inside quoted titles and inside the logged search strings were normalized after the fact (the queries as typed used "tonne" in four places and "fertiliser" in one; titles originally read "Faeces", "fertiliser", "grey"). Everything else in each logged string is verbatim.*

*Format: `query` (tool) → result · whether it found something · if a dead end, whether it died at the query (no relevant hits) or at the sources (hits existed but could not be opened or did not contain the claim).*

### Q1 search log

1. Fetched `https://www.fao.org/4/t0234e/T0234E03.htm` (FAO 29 Table 4) → found. 
2. `Maas Hoffman 1977 salt tolerance threshold slope percent yield decrease per dS/m table wheat barley maize bean` (WebSearch) → found FAO Annex 1 link (Y4263E). `fao.org/3/...` redirected to `fao.org/4/...`; fetched → found Table A1.1.
3. `NRCS soil quality indicator bulk density ideal bulk density restrict root growth by texture table g/cm3` (WebSearch) → found. NRCS PDF `Soil%20Quality-Indicators-Bulk%20Density.pdf` → **dead at the source** (socket hang up). Illinois page and SDSU page opened → found.
4. `optimum soil pH range for crops table alfalfa soybean wheat corn potato blueberry extension publication` (WebSearch) → found UDel factsheet; WebFetch could not parse PDF; text extracted locally with pdftotext → found.
5. `available water holding capacity by soil texture inches per foot table sand loam silt loam clay extension` (WebSearch) → found; Wisconsin page opened → found.
6. FAO-56 ch. 8 `x0490e0e.htm`: first WebFetch refused to reproduce; second gave Table 19 single values **not present in the original** (summary error, caught). Downloaded raw HTML with curl: Table 22 in `x0490e0e.htm`, Table 19 in `x0490e0c.htm` → found. Note: the original prints silty clay θFC as "0-30 - 0.42"; read as 0.30–0.42.
7. `Sys Van Ranst Debaveye 1993 land evaluation crop requirements soil depth cm S1 S2 S3 wheat maize` (WebSearch) → original book **dead at the query** (catalog records only). R package `soilassessment` doc page had no numbers; source code read from GitHub CRAN mirror → found thresholds (secondary).
8. `typical cation exchange capacity range by soil texture meq/100g sand loam clay organic matter CEC extension fact sheet` (WebSearch) → found; UGA C1040 opened → found.
9. `Loveland Webb 2003 "critical threshold" soil organic carbon 2% temperate agricultural soils review` (WebSearch) → only secondary mentions. ScienceDirect 403; Crossref, OpenAlex, Semantic Scholar: abstract elided → **dead at the sources**.
10. NRCS C:N sheet `nrcs142p2_052823.pdf` → **dead at the source** (socket hang up; curl failed). `NRCS "Carbon to Nitrogen Ratios in Cropping Systems" 24:1 microbes soil C:N residue table` (WebSearch) → UC Davis mirror; downloaded and read → found.
11. Pribyl 2010 via OpenAlex → no abstract. `Pribyl 2010 critical review SOC to SOM conversion factor 1.724 van Bemmelen factor of 2 abstract` (WebSearch) → search summary contained a garbled "1.24" figure (discarded); SoilWise vocabulary page opened → found.
12. `"C:N ratio" of soil organic matter typically 10:1 to 12:1 agricultural topsoil extension` (WebSearch) → NRCS Illinois tech note opened → found (10:1). Oklahoma State factsheet → **dead at the source** (403). The "8:1 to 15:1, average 10–12:1" figure in the search summary was not traced to an opened page → not used.
13. `Lindsay Norvell 1978 DTPA soil test critical levels zinc 0.8 iron 4.5 manganese copper 0.2 mg/kg` (WebSearch) → no page with values; abstract via OpenAlex → found.
14. `Tri-State Fertilizer Recommendations 2020 Mehlich-3 phosphorus critical level corn soybean wheat ppm potassium critical level CEC` (WebSearch) → Purdue PDF (curl returned HTML, WebFetch 404) and MSU PDF (HTML / empty) → **dead at the sources**; OSU newsletter summary opened → found.
15. `pre-sidedress nitrate test PSNT 25 ppm nitrate-N critical level corn Magdoff 12 inch sample extension` (WebSearch) → UConn page (redirect) opened → found.
16. `air-filled porosity 10% critical limit root growth aeration "least limiting water range" da Silva Kay Perfect 1994 penetration resistance 2 MPa` (WebSearch) → found; Magdoff and van Es LibreTexts page opened → found; da Silva et al. abstract via OpenAlex → found.
17. `recommended physical properties container growing substrate total porosity 50-85% air space 10-30% water holding capacity 45-65% bulk density extension` (WebSearch) → figures only in the search summary. UGA field report p=4977 (no ranges), UGA C1292-04 (15–30% air space only), Arkansas greenhouse unit (403), greenhouse-management.com (pH only) → original attribution **dead at the sources**; kept as UNVERIFIED.
18. `"7 to 27 percent clay, 28 to 50 percent silt, and" loam definition Soil Survey Manual NRCS` (WebSearch) → UW library page opened, empty → dead at the source; TUM/ISRIC texture flow chart PDF downloaded and read → found (NRCS 2017 table reproduced).

### Q2 search log

1. Downloaded `https://wrb.isric.org/files/WRB_fourth_edition_2022-12-18.pdf` (236 pp.) with curl; text extracted; read §1.3, key to RSGs (Histosols–Technosols, Leptosols), §3.1.16, 3.1.29, 3.1.31, 3.1.36, 3.3.2, 3.3.18, qualifier list → found.
2. OpenAlex search `terra preta Glaser phenomenon model sustainable agriculture humid tropics` → found Cunha 2009 (abstract) and Glaser 2001 (no abstract in OpenAlex).
3. OpenAlex search `Anthropogenic Dark Earths Central Amazonia properties genesis state of scientific knowledge` → found Glaser and Birk 2012 (doi:10.1016/j.gca.2010.11.029) but **no abstract** (dead at the source); Macedo 2017, Silva 2021 abstracts found.
4. `Glaser 2001 Naturwissenschaften "Terra Preta" phenomenon abstract black carbon 70 times organic matter 250 Mg ha` (WebSearch) → SSWM mirror PDF; downloaded, read in full → found.
5. OpenAlex search `Evidence confirms an anthropic origin of Amazonian Dark Earths` → Lombardo 2022 abstract found.
6. OpenAlex search `plaggen soils Europe formation sod manure thickness rate` → Choi 2024 (abstract, rate) and Dorotsuke 2025 (abstract) found.
7. OpenAlex search `constructed Technosols soil construction ecological reclamation derelict lands Séré` → Fabbri 2021 abstract; Séré 2008 itself not surfaced (query near-miss).
8. OpenAlex search `Using constructed soils for green infrastructure challenges and limitations Deeb` → found; full PDF from Copernicus read → found.
9. Grard et al. 2018: OpenAlex no abstract; Springer PDF returned HTML (paywall redirect); `"Rooftop farming on urban waste provides many ecosystem services" Grard hal yields kg m-2 green waste compost wood chips spent mushroom` (WebSearch) → HAL page "Access Denied" → **dead at the sources**; only search-summary figures, kept UNVERIFIED.
10. OpenAlex search `chinampa soils Xochimilco properties organic matter construction` → Ebel 2019 abstract found. No quantitative chinampa soil-property paper with abstract surfaced (near-dead at the query; one microbiology paper on "high humus, alkaline-saline chinampa soils" noted, not opened).

### Q3 search log

1. `IPNI nutrient removal per metric ton harvested product kg N P2O5 K2O wheat maize rice potato soybean table` (WebSearch) → links found; **the search tool's own "metric values" (e.g. "soybeans remove roughly 2.5 kg N … per metric ton") were wrong by ~20× and were discarded**. PDA 2020 PDF and Arkansas FSA2176 PDF downloaded and read → found. Manitoba poster → **dead at the source** (HTML returned).
2. `nutrient removal vegetable crops lb N P K per ton harvested tomato lettuce potato broccoli Hartz University of California table` (WebSearch) → CDFA guideline pages; CDFA project PDF 11-0558 was the wrong document (irrigation). Raw HTML of CDFA pages N_Tomato, N_Lettuce, N_Broccoli, N_Potato, N_Carrot, N_Onion, N_Wheat read → found. N_Corn, N_Rice, N_Bean, N_Cabbage, N_Spinach, N_Pepper, N_Melon, N_Alfalfa → **dead at the source** (pages under those names return a stub; actual page names not found).
3. `Geisseler 2016 "Nitrogen concentration in harvested plant parts" literature overview UC Davis pdf` (WebSearch) → apps1.cdfa.ca.gov PDF returned HTML → **dead at the source**; 2021 FREP report downloaded but covers perennial crops only (not used).
4. `Jönsson Richert Vinnerås Salomon 2004 Guidelines on the Use of Urine and Feces in Crop Production EcoSanRes pdf …` (WebSearch) → SuSanA PDF was a slide deck (not the guideline); SuSanA resource page gave a Portuguese download. `"Guidelines on the use of urine and feces in crop production" EcoSanRes 2004-2 pdf english table …` (WebSearch) → SSWM page held the original ecosanres.org link (dead); **Internet Archive copy** downloaded (43 pp.) and read → found Tables 1, 3, 6 and text.
5. `sewage sludge production per person per year kg dry solids population equivalent g DS/PE/day digested sludge statistics` (WebSearch) → NRC 2002 chapter opened → found 21 kg. European per-capita figures not opened (UNVERIFIED).
6. OpenAlex `Egle phosphorus recovery municipal wastewater integrated comparative …` → abstract found. `nitrogen phosphorus mass balance wastewater treatment plant fate sludge effluent percent influent` → Kok 2018 and Udert 2002 abstracts found.
7. `fraction of influent nitrogen recovered in sewage sludge conventional wastewater treatment plant percent denitrification lost as N2 nitrogen mass balance study` (WebSearch) → patents and generic text → **dead at the query**. Extended-mode near-duplicate `"of the nitrogen" influent ends up in sludge … "biological nutrient removal" …` → **dead at the query**. OpenAlex `substance flow analysis nitrogen phosphorus municipal wastewater treatment plant sludge effluent gaseous` and `nitrogen recovery from wastewater potential review ammonia stripping urine source separation percent recovery` → no usable N-fate abstract; Sengupta et al. 2015 has no abstract (dead at the source).
8. `typical nutrient content of biosolids percent dry weight total nitrogen phosphorus potassium anaerobically digested extension table` (WebSearch) → Oklahoma State PDF failed to download (dead at the source); Ontario BMP chapter PDF downloaded and read → found.
9. `FAO Statistical Yearbook 2024 world average protein supply g per capita per day dietary energy supply kcal 2022` (WebSearch) → FAO highlights page (kcal only); Yearbook HTML downloaded (regional protein, no world figure in text); FAOSTAT API → **dead at the source** (error 521); Food Systems Dashboard → 429; OWID CSV downloads → found world series.
10. `urine diversion toilets field study fraction of excreted urine collected percent capture efficiency nitrogen recovery real system` (WebSearch) → SLU abstract page (Vinnerås and Jönsson 2002) and PMC article (Kachoria et al.) opened → found. Brattleboro / Massachusetts urine-diversion reports surfaced but not opened.
11. OpenAlex DOIs 10.1038/nature15743 (Zhang 2015; no abstract), 10.2134/agronj2016.08.0483, 10.2134/age2018.10.0045, 10.2134/agronj2018.07.0462 → efficiency abstracts found.

### Q4 search log

1. OpenAlex DOI 10.1007/s11104-008-9668-3 (Herridge 2008) → no abstract. `Herridge Peoples Boddey 2008 "Global inputs of biological nitrogen fixation in agricultural systems" abstract Tg soybean 16.4 free-living cyanobacteria rice` (WebSearch) → UNE repository; raw HTML read → found.
2. OpenAlex `Peoples biological nitrogen fixation agricultural legumes global estimates kg N per ha review 2009 symbiotic` → Peoples 2009 (no abstract, dead at the source); Anglade 2015 abstract found; Kebede 2021 abstract (qualitative).
3. `extension table nitrogen fixed by legumes pounds per acre per year alfalfa red clover white clover soybean hairy vetch field pea` (WebSearch) → Alabama ANR-3023 and Kansas L-778 PDFs downloaded and read → found. Field pea rate not found in these.
4. OpenAlex DOI 10.1016/j.fcr.2008.03.001 (Salvagiotti 2008, grain soybean) → no abstract → **dead at the source**.
5. OpenAlex `Azolla nitrogen fixation rice kg N ha biofertilizer review` and `Azolla nitrogen fixation rate kg N per hectare per year doubling time Anabaena azollae review Wagner` → Yang 2025 (full PDF read), Marzouk 2023 abstract; Wagner 1997 not surfaced (near-miss at the query).
6. OpenAlex `Roger Ladha biological N2 fixation wetland rice fields estimation contribution nitrogen balance` and title search → records found, no abstracts. `blue-green algae cyanobacteria nitrogen fixation flooded rice field average kg N per hectare per crop Roger Ladha 1992 estimate` (WebSearch) → IRD PDF link; curl returned a script page; WebFetch redirected to maintenance.ird.fr → **dead at the source**. Ladha et al. 2022 (*Field Crops Res.*): ScienceDirect PDF and HTML both 403 → **dead at the source**.
7. OpenAlex `heterotrophic free-living nitrogen fixation rates terrestrial kg N ha yr review Reed Cleveland` → Dynarski and Houlton 2017 (qualitative only); no agricultural per-hectare rate → **dead at the query**.
8. OpenAlex DOI 10.1039/c9ee02873k (Smith 2020) → one-line abstract; RSC PDF returned HTML and RSC HTML 403 → **dead at the source**.
9. `Royal Society 2020 "Ammonia: zero-carbon fertilizer, fuel and energy store" pdf energy GJ per metric ton ammonia steam methane reforming` (WebSearch) → PDF downloaded and read → found.
10. `electrolysis-based ammonia electricity consumption MWh per metric ton NH3 IEA Ammonia Technology Roadmap 2021 natural gas share coal share hydrogen feedstock` (WebSearch) → IEA roadmap PDF (fertilizer.org) downloaded and read → found. The search summary's "12 MWh/t" and "10.02 MWh/t" figures were not traced to opened pages → not used.
11. OpenAlex `plasma nitrogen fixation energy efficiency GJ per metric ton review comparison Haber-Bosch` and `plasma-based nitrogen fixation NOx energy cost MJ per mol Birkeland Eyde comparison review` → Rouwenhorst 2020/2021 (abstracts without numbers). `Rouwenhorst 2021 Birkeland–Eyde plasma NOx synthesis energy cost MJ/mol N 2.4 MJ/mol Haber-Bosch 0.48 MJ/mol comparison` (WebSearch) → PMC8133363; curl returned a 167-character stub; WebFetch summary read → found (and the 2023 correction notice).
12. OpenAlex `electrochemical ammonia synthesis lithium mediated energy efficiency review` → Zhou et al. 2024 abstract found.
13. USGS MCS 2026 phosphate rock and potash PDFs downloaded (also 2025 editions downloaded, not needed) → found.
14. OWID population CSV → world 2020 and 2023 found.
15. OpenAlex `meta-analysis struvite phosphorus fertilizer effectiveness compared soluble`, `bone char bone meal phosphorus fertilizer content P2O5 plant availability`, `seabird guano phosphorus nitrogen content fertilizer history Peru` → abstracts for De Lucca Agrelo 2026, Sharma 2024, Someus 2018, Otero 2018 found. Historical guano N/P content (e.g. Peruvian guano analyses) **not found** (dead at the query). A 2026 struvite meta-analysis surfaced in a low-visibility journal; not opened.

### Q5 search log

1. FAO Training Manual 3 (Brouwer and Heibloem 1986) chapters `s2022e02`–`s2022e0b.htm` downloaded with curl; Table 4 and Table 5 found in `s2022e02.htm` → found. Irrigation efficiency not in these chapters (searched s04, s08, s09) → dead at the source for that item.
2. `FAO irrigation field application efficiency surface irrigation 60% sprinkler 75% drip 90% table "field application efficiency"` (WebSearch) → search summary gave unattributed ranges (not used). Howell and Evett CPIA 2005 paper downloaded → no percentage table. Howell 2002 "Irrigation system efficiencies" PDF → HTML returned at both irrigationtoolbox URLs (**dead at the source**). USDA-ARS eprint 1136 → download failed. Wyoming/Nebraska E3A Step 4 PDF downloaded and read → found Table 6.
3. OpenAlex DOIs 10.5194/hess-15-1577-2011 and 10.3390/ijerph120606879 → abstracts; Mekonnen and Hoekstra full PDF downloaded, Table 3 read → found.
4. OpenAlex `greenhouse tomato water use efficiency Almeria kg per m3 crop water productivity open field comparison` and `irrigation water productivity greenhouse tomato Almeria open field kg m-3 comparison Thompson Gallardo` and `water use efficiency closed soilless greenhouse tomato recirculation liters per kg Netherlands` → Ravitz Wyngaard 2022 abstract found; other abstracts qualitative (Nikolaou 2019, D'Amico 2023). An Almería-specific farm-gate L/kg study was not opened (the 2010 "water footprint and virtual water exports of Spanish tomatoes" has no abstract).
5. `tomato water use liters per kilogram open field vs plastic greenhouse Almería vs Dutch glasshouse closed system 15 L/kg comparison study` (WebSearch) → WUR edepot 156932 (article) and 385636 (Stanghellini 2015 slides) downloaded and read → found.

### Q6 search log

1. OpenAlex `Carrying capacity of U.S. agricultural land ten diet scenarios Peters` → near-miss (not in top results); DOI 10.12952/journal.elementa.000116 fetched directly → abstract found. `Testing a complete-diet model land resource requirements food consumption New York State` → Peters 2007 abstract found.
2. OpenAlex `Biosphere 2 agriculture food production yields intensive agricultural biome Silverstone Nelson` → Nelson 2021 (abstract qualitative); SPJ PDF returned HTML and HTML 403 → **dead at the source**. `Food production and nutrition in Biosphere 2 results from the first mission` → Silverstone 1997 PubMed record with abstract → found (2,000 m², 81%).
3. OpenAlex `Bios-3 Siberian experiments bioregenerative life support Salisbury Gitelson` → record, no usable abstract; OUP PDF returned HTML (**dead at the source**). `BIOS-3 Krasnoyarsk phytotron area square meters per person wheat chufa crew of three 180 days percent food regenerated Salisbury Gitelson 1997` (WebSearch) → SIMOC mirror PDF downloaded; OCR text garbled for Table 2; page rendered with pdftoppm and read as an image → found.
4. OpenAlex `NASA bioregenerative life support crop area per person 40 m2 Wheeler candidate crops` → Johnson et al. 2021 abstract → found. Wheeler's own primary papers not opened.
5. OpenAlex `Lunar Palace 1 365 day closed experiment plant cultivation area crew` → Fu et al. 2021 abstract; bioRxiv PDF returned text stub and full-text page HTTP 429 → plant area **dead at the source**.
6. OWID CSVs `cropland-area`, `arable-land-use-per-person`, `wheat-yields`, `potato-yields`, `rice-yields`, `maize-yields`, `soybean-yields` → found. `cropland-use-per-person` and `land-use-per-capita-for-cropland` → 404 (dead at the source; per-person value computed instead).
7. USDA FoodData Central API (to compute calorie-only area from yields) → **OVER_RATE_LIMIT** on DEMO_KEY → dead at the source; calorie-only area computation was therefore **not done** rather than done with recalled kcal values.
8. `FAO 1982 "Potential population supporting capacities of lands in the developing world" low input intermediate high input persons per hectare results` (WebSearch) → FAO pages t8300e0b and u8480e0e read → country counts found; per-person area **not in these pages** (dead at the sources).
9. `Ecology Action biointensive minimum area to grow complete diet one person square feet 4,000 Jeavons` (WebSearch) → growbiointensive.org FAQ opened → found.
