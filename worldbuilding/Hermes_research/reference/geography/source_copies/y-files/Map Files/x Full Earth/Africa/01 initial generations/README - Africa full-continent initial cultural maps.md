# Africa (full continent) — initial Woodard-style cultural, realm, language and religion maps (first pass, 2026-10-03)

**For consideration only. No nations are named, no borders are settled.** These maps join the six subsection map sets in `../../subsections/` (Northwest-North, Northwest-South, North-Center, Northeast, Central, South) into one continental series. **Nothing in the subsection notes, tables or maps was edited**: every unit keeps the region, tier, languages, religions and overlays its own subsection gave it. Research proposes, the author disposes.

## What is in the series
| File | What it shows |
|---|---|
| `map-1-cultural-regions.png` | **267 regions** in ten realms (A 28, B 16, C 41, D 40, E 29, F 17, G 19, H 32, I 32, J 13), Woodard-style: **core** (solid, 639 units), **domain** (light, 234 units) and **sphere** (hatching and dotted edge: the 58 overlays that some unit draws, up to two per unit). Regions carry their continental number, and a name where it fits. Cabo Verde is an inset. |
| `map-1b-region-index.png` | The index of the 267 numbered regions by realm, with each region's subsection key and confidence. Regions too small for a number at this scale are listed here only. |
| `map-2-realms.png` | The ten realms of the continental framework (Tier 1). Realm J, Indian Ocean Islands, holds only Madagascar so far. |
| `map-3-languages.png` | **Plurality home language** per unit: 226 languages are a plurality somewhere (39 more appear only as a hatched second language), colored by one of 34 language groups, with hatching where a second language reaches about 20%. |
| `map-4-religion.png` | **Plurality affiliation** per unit: Islam 378 units, other Christianity 480, Oriental Orthodox Christianity 5, African traditional religions 10; hatching where a second religion reaches about 20% (178 units). |

House style follows the subsection maps (flat fills, whole first-order units, warm sidebar, Crimson Text and Lato, Lambert azimuthal equal-area, here centered on 17 E, 1.5 N). Latin script only, American English.

## Regenerating
`python3 merge_subsections.py [NE_DIR]` reads the six subsections' `01 initial generations/map-data/` folders and geometry (`../../subsections/`) plus Natural Earth 10m (`NE_DIR`, default `/tmp/ne_test`: `ne_10m_admin_0_countries`, `admin_1_states_provinces`, `lakes`, `rivers_lake_centerlines`, `populated_places_simple` as `.geojson`) and writes everything the renderer needs into this folder (`africa-continent-base.gpkg` and `map-data/`). It stops with an error if a unit is missing or duplicated, a language code has no group, an overlay code is unknown or a religion code is outside the vocabulary. Then `python3 render_continent.py` makes the five PNGs (or `render_continent.py regions | index | realms | language | religion`; a full run takes several minutes). Needs geopandas, matplotlib, shapely, pandas; fonts are in `fonts/`. **After the merge, this folder is self-contained**: the renderer reads only `map-data/` and the local gpkg, so a copy in `02 reorganization/01 follow-up/` runs as is (copy the whole folder contents there, edit the CSVs, re-render).

## Files
- `map-data/regions.csv` — the 267 regions: continental number (`region_num`, 1 to 267, ordered by realm, then subsection, then the subsection's own id), `region_key` (subsection and its own id, e.g. `NC-27`), realm, name, map label, confidence, institution, reset type. Names, labels, institutions and reset codes are the subsections' (working labels).
- `map-data/classification.csv` — **873 drawing units**: unit id, country, unit, subsection, `region_num`, `region_key`, tier, `sphere_1` and `sphere_2` (the overlays actually drawn, after the subsection's own rules), `sphere_all` (every overlay the note lists), `judgment_call` (597 of 873), language and religion columns, confidence (132 units rest on a unit-level figure, 366 on solid qualitative evidence or a national figure, 375 are inferred or from memory), one-clause evidence.
- `map-data/spheres.csv` — the 100 overlay layers recorded, 59 drawn in at least one subsection (58 appear on units). `map-data/lang-religion/languages.csv`, `language_groups.csv`, `religions.csv` — 318 languages in 34 groups and six religions.
- `map-data/zone-seams.csv` — the 88 pairs of adjacent regions that come from different subsections, with each side's main language and shared overlays; 14 pairs share a main language. **Candidate merges for the author; none is applied.**
- `map-data/coverage.csv` — Natural Earth units of African countries that no subsection covers (now only the Comoros, 3 units).
- `merge_subsections.py`, `render_continent.py`, `africa-continent-base.gpkg`, `fonts/`.

## How the merge was done (the only changes made to the subsection data)
- **Realms** are the framework's letters, which the subsections already shared (A Maghreb and Libyan Coast; B Sahara; C Sahel and Sudanian West; D Guinea Coast and Middle Belt; E Central African Forest and Savanna; F Nile Valley and Red Sea; G Horn of Africa; H East Africa and the Great Lakes; I Southern Africa). Cabo Verde stays in D as in the Northwest-South subsection (it has no realm in the framework).
- **Region numbers** are new and continental; every region keeps its subsection key.
- **Language codes:** nine clashes where one code meant two languages, and one older code, were renamed (Northwest-North `kab` Kabyle to `kby`, `shi` Tashelhit to `shl`, `bam` Bambara to `bmb`, `son` Songhay to `sng`, `fr` to `fra`; Northwest-South `som` Somba to `sbd`; North-Center `mas` Masa to `msa`; Northeast `mas` Masalit to `mls`; South `lom` Lomwe to `lmw`, `nwg` Namwanga to `nmw`). Codes that meant the same language in several subsections (`ful`, `orm`, `sar`, `gba`, `bem`, `mnk` and others) were merged. **The 32 language groups are mine** (the subsections' own family headings differ), assigned code by code in `merge_subsections.py`.
- **Overlay codes:** the same codes were used for the same worlds across subsections (FUL, AMZ, SAR, BTI, SOM, ORM, SWA, KNG and others merge); the one clash, `NUB` (Nubian world in the Northeast, Nubi Muslim communities in Central), became `NBI` in Central. **Which overlays a unit draws follows its own subsection's rule** (drawn set, and the rule that a core unit does not hatch for its own region's group, with the Central, Northeast and South `HOME_ALL` extension): a world that one subsection records without drawing is still not drawn on its units. Hatches and colors were reassigned so that no two overlays repeat.
- **Religion:** the Northwest-North subsection used `sunni` and `ibadi`; both became `isl`, and its single Ibadi second-religion cell is dropped as a second religion (it stays in the subsection data). Northeast's `ort` stays a separate category.
- Nothing else was changed (Madagascar's overlay `SWA` is built as `IOM` inside the South subsection itself, not here): no unit was moved, no tier edited, no region merged or renamed.

## Choices made in this first pass (the author can reverse any of them)
- **Zone seams are not merged.** Where one culture runs across a subsection line, the two halves remain separate regions: the Yoruba (Benin's Porto-Novo region and Nigeria's Lagos and Yoruba Heartland), the Kongo (Congo's Kongo regions and Angola's north), the Beti-Pahuin (Cameroon's Beti-Bulu forest and Gabon's Fang Country), the Zaghawa (Chad's Dar Zaghawa and Darfur), the Somali (Ethiopia's Ogaden and Jubaland against Kenya's Somali region), the Fulbe of the Senegal valley, and the Tuareg (Kidal and Aïr). They are listed in `map-data/zone-seams.csv`.
- **Units: the Natural Earth vintage, with no rebuilding**, so the unit vintage differs by country (see each subsection's README).
- **Madagascar** was added to the South subsection on 2026-10-03 (13 regions, realm J, numbers 255 to 267); **the other island states** (the Comoros, Mauritius, the Seychelles, Sao Tome and Principe) are not yet mapped and are gray. Madagascar's languages are 13 Malagasy dialect codes (the group "Malagasy dialects (Austronesian)") plus Comorian; its drawn overlays are the Merina kingdom, the Sakalava dynasties and the Indian Ocean Muslim and Comorian coast.
- **Language map color:** one hue per language group (hues chosen so that touching groups are far apart on the wheel) and one lightness step per language; labels are placed only where a language's area is large enough to carry one.
- **Labels on map 1:** each region carries its continental number, plus its name where the name fits inside the region; very small regions are unlabeled and appear in the index only.

## Highest-priority things to check
- The **weakest cells** are those of the subsections (see each README): Guinea-Bissau, Togo and Burkina Faso; all DRC language and religion; all Chad religion; Nigeria's state religion; nearly all Sudan language and religion; Angola outside Luanda; Tanzania by region.
- **Language groups** and the **seam list** are new and mine: please check the groupings (for example, Swahili sits with the Kenya and Tanzania Bantu, Ateker with the Nilotic group) and which seams you want merged.
- **Subsection vintage mismatches** meet at the lines: for example, Natural Earth's Libya (2007 shabiyat) against Niger and Chad, and the Northwest-North Algeria and Mali divisions against newer ones elsewhere.
- **The Northwest-North data is the oldest style** (18 broader language codes, one religion category, fewer overlay codes): its languages are coarser than the rest of the continent's.

## Author decisions open
- Which of the 14 same-language seams to merge into continental regions (and whether other cross-line cultures should be merged); which island states to add to realm J beside Madagascar.
- The island states (the Comoros, Mauritius, the Seychelles, Sao Tome and Principe); Cabo Verde's realm.
- Everything listed in the six subsection READMEs ("Author decisions open") still stands.
