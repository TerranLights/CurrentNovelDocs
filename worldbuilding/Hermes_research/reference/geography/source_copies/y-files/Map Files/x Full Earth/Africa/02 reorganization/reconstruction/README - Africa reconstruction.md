# Africa (full continent) — the reconstruction (2026-10-04)

**For consideration.** One composite map of all Africa with the country borders as the author decided them in the six subsections (all decided 2026-10-03 and 2026-10-04): 52 countries as decided and **no border changes anywhere**.

## What is here
| File | What it is |
|---|---|
| `map-1-africa-country-borders.png` | The composite map (48 x 30 in, 110 dpi, LAEA centered on 16 E, 1.5 N, house style). Countries as decided; red hatching for Western Sahara and the Moroccan-administered units ("as administered, sovereignty open"); blue crosshatching for Somalia and Somaliland ("volatile territory"); red dashed arrows for the three trade arrangements (Senegal-Gambia, Togo-Ghana, Gabon-Equatorial Guinea-Republic of the Congo); pale dots for the four island states not yet mapped or decided (the Comoros, Mauritius, the Seychelles, Sao Tome and Principe). The sidebar summarizes each subsection and what is still open. |
| `africa-reconstruction-base.gpkg` | Geometry: `units` (873, with `new_country`, `ckey`, `zone`, `status`, `arrangement`), `countries`, `lakes`, `rivers`, `places`. |
| `map-data/country-assignment.csv` | The 873 units: zone, country today, region, country as decided, status mark (`open`, `volatile` or blank), political arrangement, the author's note. |
| `map-data/countries.csv` | One row per country as decided: zone, units, decision, arrangement. |
| `build_reconstruction.py` | Reads the six folders in `../basis files/` and writes the gpkg and the two CSVs. |
| `render_reconstruction.py` | Draws the map from the gpkg. |

## How it was built
`python3 build_reconstruction.py` reads each subsection's `africa-*-base.gpkg` and `map-data/new-country-assignment.csv` from `../basis files/Africa (<zone>)/` (873 units, every `new_country` filled; nothing in the basis files is edited), merges them, and writes the files above. `python3 render_reconstruction.py` then draws the map. A country is the union of its first-order units (Natural Earth 10m admin-1, an older vintage), so a border follows unit edges. Names were normalized (Ivory Coast to Côte d'Ivoire, Swaziland to Eswatini, S. Sudan to South Sudan, "Morocco (as administered today)" to Morocco with a status mark). Needs geopandas, matplotlib, shapely, pandas; fonts are in `fonts/`.

## Choices made (the author can reverse any of them)
- **Colors** are assigned by adjacency (no two neighbors share a color) and carry no meaning; the colors differ from the subsection maps.
- **The island states** are shown from the basis files' country layers as pale dots with "not yet decided" labels, not as decided countries.
- **The Moroccan-administered units** (Laâyoune-Boujdour-Sakia El Hamra and Oued el Dahab) are drawn as part of Morocco with the red hatch, as in the Northwest-North map.
- **Somaliland** is its own polygon, hatched like Somalia (volatile territory).

## Still open
The African Union (details to be worked out later) and the island states.
