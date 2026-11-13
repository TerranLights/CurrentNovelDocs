# World atlas (built 2026-10-04)

Two 16:9 pages at 3840 x 2160 (4K), plus a PDF of both:

| File | What it is |
|---|---|
| `out/01_cover_and_index.png` | Page 1: cover and index. Title, how to read the atlas, the state shown for each region, a small copy of the world map, and the index of all 272 entries (number, map color, name, status marks, capital), grouped by region and, inside a region, by union (the Confederacy of Intermarium Nations, the Scandinavian Trade Union, the three Oceania spheres, Madhyama and its zones, the Guianas trade union). |
| `out/02_world_map.png` | Page 2: the world map (Equal Earth projection cut in the Bering Strait so Chukotka and the Aleutians stay whole). 161 nations are named on the map (a thin line joins a name that sits outside its nation); 111 nations too small to name carry a numbered circle keyed to the index. Hatching marks disputed or unclaimed territory (red), volatile territory (blue crosshatch) and neutral zones (white dots); gray dots mark land no region has worked out yet. |
| `out/world_atlas.pdf` | Both pages as a 2-page PDF. |
| `out/03_world_map_with_CIN.png` | An additional (not a page) 3840 x 2160 copy of the world map that draws the Confederacy of Intermarium Nations as one bloc, as the Europe series draws it: members in one crimson color with dashed gold lines between them, the three observers (Belarus, Bosnia and Herzegovina, Skoprodija) in pale crimson with hatching, and Albania, barred, in dark cross-hatching. Everything else matches page 2. Made by `render_world_map.py --cin`. |

## How it was built
Each region's final state was turned into one GeoPackage of nation polygons (`data/regions/<region>/nations.gpkg`, format in `ATLAS SPEC - region data format.md`, with its own `build_*.py`, `preview.png` and `README.md` listing sources, the state treated as final, caveats and seams). `scripts/merge_world.py` then joins them (rows with the same name are merged: Finland = Europe's Finland plus the Karelia piece from the Russia package), resolves seam overlaps by region priority (South Asia's district-level lines win over the Natural Earth outlines used by East Asia, Southeast Asia and West Asia), and fills land no region covers: slivers go to the neighbor with the longest shared border, islands go to the nation of the same name where one exists (Svalbard to Norway, Heard Island to Australia, and so on), and everything else becomes a gray "not yet worked out" row named after its present-day country. `scripts/render_world_map.py` draws page 2 and `scripts/render_cover.py` draws page 1. Everything is in `data/world/` (`nations_world.gpkg`, `numbering.csv`, `labels.csv`, `merge_report.md`).

**Rebuild:** `python3 scripts/build_atlas.py` (about 8 minutes, including the CIN map; needs geopandas, shapely, matplotlib, pandas, numpy, pyproj and Pillow; Natural Earth 10m in `NE_DIR`, default `/tmp/ne_test`).

## When Tepenia changes (expected soon)
Tepenia's nation polygon and its 38 cities are read straight from the Tepenia project's own data (`Tepenia (Antarctica)/tentative_rudimentary/data/`: `base/land.geojson`, `base/ice_shelves.geojson`, `cities.csv`). After an update there, run `python3 scripts/build_atlas.py --tepenia`. If Tepenia gains sub-regions or other nations inside Antarctica, edit `data/regions/tepenia/build_tepenia.py` to emit more rows (the merge, the map colors and the index pick them up by themselves).

## When another region changes
Edit that region's source folder, then `python3 scripts/build_atlas.py --regions <region_key>` (keys: `europe`, `russia`, `east-asia`, `south-asia`, `southeast-asia`, `west-asia`, `oceania`, `north-america`, `latin-america`); Africa is `--africa` (it reads the copy in `x Full Earth/Africa/`). `--all-regions` reruns everything.

## What the author may want to decide
- **Not yet worked out (13 gray rows):** India, the Maldives, the Caribbean Netherlands, Bermuda, Saint Pierre and Miquelon, South Georgia, Saint Helena, the Chagos islands, the French Southern and Antarctic Lands, and the four undecided African island states (the Comoros, Mauritius, the Seychelles, Sao Tome and Principe). They are present-day outlines.
- **Provisional territories** in the Oceania data (New Caledonia, Guam, the Northern Marianas, American Samoa, the Cook Islands, Niue, French Polynesia, Wallis and Futuna, Pitcairn) are drawn as the nations the Oceania source makes them; Midway is outside Hawaii in that source.
- **Capitals:** only the capitals the sources state are in the index (116); many nations have none.
- **Patani (marked for review):** the Southeast Asia source calls Thailand's three southern provinces "Deep South" (a placeholder). On 2026-10-04 the author asked the atlas to rename it **Patani** for now and to mark it for review; it prints as "Patani*" on the map with "name under review" in the index. The rename and the review note live in `scripts/merge_world.py` (`RENAMES`, `REVIEW`); the source files still say "Deep South". To give it its final name, change `RENAMES` and delete its `REVIEW` entry.
- **Placeholder names** inherited from the sources (Idelsk-Uralia, Donska-Kubania, Virgin Islands, French Antilles, Aruba-Curaçao, Madhyama, Skoprodija, and the unnamed Guianas trade union) are printed as written.
- **Native names** (Cyrillic, Greek, CJK, Arabic, Hangul) are in `nations_world.gpkg` but not printed: the house fonts (Crimson Text, Lato) lack those scripts.
- **Seams:** where two regions' data overlap (Nepal and Tibet, Pakistan and East Turkestan, the Indian zones and Myanmar) the overlap goes to the higher-priority region; the full list with areas is in `data/world/merge_report.md`.
- A zoom inset for Europe or the Caribbean was not made (the regional maps cover them); the numbered circles stand in.
