# southeast-asia: nations.gpkg

Output: `nations.gpkg`, layer `nations`, 14 rows, EPSG:4326, valid, no overlaps between rows (computed, build script checks pairwise). Reproduce with `build_southeast-asia.py` (reads the source read-only; env vars `SEA_SRC`, `NE_DIR`, `OUT_DIR`). `preview.png` is rendered by the same script.

## What was used as the final state
Source folder: `Asia/Asia (Southeast)/` (top level). Final state = the two **national maps** (`mainland_sea_map_national.png`, `maritime_sea_map_national.png`), built by `render_map_national.py` and `render_map_maritime_national.py` with `subdivisions.csv` and `subdivisions_maritime.csv`. `CHANGES.md` (round 3, 2026-09-26) is the latest dated change and touches only two mainland label positions, so geometry is unaffected. The two zips (`files.zip`, `southeast_asia_national_v04.zip`) were unpacked in scratch: the scripts and CSVs inside are byte-identical (md5, computed) to the top-level ones; the zip PNGs differ only in the older-round label placement. No conflict between candidates. Because Natural Earth admin-1 predates some real-world changes, the scripts' own corrections (Vietnam merges, Philippine NIR/BARMM, Indonesia keyword blocs) are what define units.

## Nations (units = rows in the source tables)
| nation | kind | units | capital |
|---|---|---|---|
| Myanmar | nation | 15 | Nay Pyi Taw |
| Thailand | nation | 74 | Bangkok |
| Laos | nation | 18 | Vientiane |
| Cambodia | nation | 25 | Phnom Penh |
| Vietnam | nation | 34 | Hanoi |
| Deep South | nation | 3 | none in source |
| Indonesia | nation | 31 | Nusantara (116.8, -0.9) |
| Aceh | autonomous zone | 1 | none in source |
| West Papua | nation | 6 | none in source |
| Philippines | nation | 18 | Manila |
| Malaysia | nation | 16 | Kuala Lumpur |
| Brunei | nation | 4 | Bandar Seri Begawan |
| Singapore | nation | 1 | Singapore |
| Timor-Leste | nation | 14 | Dili |

Colors are the CSV `color_hex` of each nation (what the maps fill, lightened 15 percent on the map itself). `group` and `group_role` are empty: neither script nor tables define a union or bloc for these nations (the "spheres" in the scripts, such as the Tai Continuum or the Maritime Mandala, are cultural overlays, not memberships, and are not recorded).

## How the tables split the countries
- Thailand: Pattani, Yala and Narathiwat become the independent **Deep South** after the 2083 war; Thailand is the rest.
- Indonesia: six former blocs (Sumatra, Java, Kalimantan, Sulawesi, Maluku, Nusa Tenggara and Bali) form ONE nation, **Indonesia**. Aceh is split off as an **Autonomous Zone** drawn with its own hard border (a nation-tier polygon). **West Papua** is the whole six-province Papua region (Papua, West Papua, Central, Highland, South, Southwest). The split uses the script's `bloc_of` keyword classifier on NE admin-1.
- Malaysia stays one country. Sarawak is a sub-country Autonomous Zone (dashed internal border on the map) and is NOT split into its own row; Sabah and Peninsular Malaysia are ordinary.
- Philippines stays one nation (18 regions; BARMM is an ordinary region, Sulu moved to Zamboanga Peninsula, Negros Island Region created); Myanmar stays one nation (no split in the national maps).
- Timor-Leste includes the Oecusse exclave.

## Geometry method (deviation from the scripts, deliberate)
The scripts draw mainland nations from dissolved admin-1 units and the five single-country maritime nations from admin-0. For a gap-free atlas layer this build uses Natural Earth **admin-0** outlines for Myanmar, Laos, Cambodia, Vietnam, Thailand, Philippines, Malaysia, Brunei, Singapore and Timor-Leste, and cuts the Deep South out of Thailand using the three admin-1 provinces (the same carve-out as the script). Indonesia, Aceh and West Papua come from admin-1 via `bloc_of`, with any sliver between them and Indonesia's admin-0 outline absorbed into Indonesia (as the script does). Overlaps from the two Natural Earth layers are resolved in a fixed priority (carve-outs first); computed: the overlap area cut was below 0.00001 square degrees for every nation, i.e. none of substance. All islands are kept.

## Visual check
`preview.png` compared with both national maps: all shapes and unit assignments match (Deep South at the Thai-Malay border, Aceh at Sumatra's north tip, West Papua east of Halmahera including Bird's Head and the Raja Ampat islands, Oecusse, Brunei's two parts, Singapore). No mismatches remain.

## Caveats and seams
- **Papua New Guinea** lies east of West Papua (straight border near 141 E): belongs to Oceania. West Papua's east edge must meet Oceania's PNG polygon; both come from Natural Earth, so they should agree.
- **Bangladesh and India** (west of Myanmar), **China** (north of Myanmar, Laos, Vietnam) are not in this layer; Myanmar's NE and the Vietnam-China border seams are Natural Earth lines.
- **Malaysia/Thailand and Brunei/Malaysia** land borders come from Natural Earth admin-0; the Deep South polygon is from admin-1, so a thin sliver between Deep South and Malaysia may differ from the exact border (cut by priority, no overlap, a tiny gap is possible).
- **Singapore, Brunei and Sabah/Sarawak/Kalimantan** borders are at Natural Earth's best line; the source notes the Sabah/Sarawak-Kalimantan border is not fully demarcated in reality.
- **Cocos/Christmas Island, Palau, Taiwan** are not part of this region. Australia's Ashmore and Cartier and Christmas Island are outside the layer.
- Capitals for the Deep South, Aceh and West Papua are not given in the source (Pattani, Banda Aceh and Jayapura appear only as city markers), so they are empty; the author may want to decide them.
- Myanmar's capital Nay Pyi Taw, Xaisomboun (Laos) and Tboung Khmum (Cambodia) are newer than Natural Earth; they are inside the parent geometry, not separate.
- `native` is empty everywhere: the source gives no native names.
- Maps are Lambert azimuthal equal-area; polygons here are plain lon/lat from Natural Earth, no antimeridian crossing (max longitude about 141 E).
