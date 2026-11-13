# North America: atlas region data

Files: `nations.gpkg` (layer `nations`, 14 rows, EPSG:4326), `build_north_america.py` (reproducible build), `make_preview.py` and `preview.png` (check render). Run: `python build_north_america.py && python make_preview.py` (Natural Earth 10m `.geojson` files in `NE_DIR`, default `/tmp/ne_test`; nothing was downloaded).

## What was used and which state is final
Source (read-only): `x Full Earth/North America/`. Final state = the **eighth round, 2026-09-26** (`CHANGES.md`: dedicated Hawaii map on top of the seventh-round Hawaii inset). Evidence (computed): the loose `north-america-nations/` folder, `files.zip` and `north-america-nations-with-hawaii.zip` hold byte-identical `na_nations.py` and `hawaii_nation.py`, and `nations/north-america-nations.png` equals the top-level PNG. The `nations/na-states-*.png` files are older per-nation images (2026-09-25/26) and were not used. No conflict between candidates. Unit assignments are copied verbatim from `na_nations.py` (`NATIONS` table) and `reference/nations-assignment.csv` (72 rows); the Hawaii definition is from `hawaii_nation.py`.

## Nations (14 rows)
| nation | kind | units | color | capital |
|---|---|---|---|---|
| Alaska | nation | 4 (Alaska minus Panhandle, Yukon, NWT, Nunavut minus the Arctic exceptions) | #5A8BD0 | Whitehorse |
| The People's Democratic Republic of Cascadia | nation | 7 (WA, OR, CA, BC, Baja California, Baja California Sur, Alaska Panhandle) | #7CC9AA | open |
| Colorado | nation | 6 (ID, MT, WY, NV, UT, CO) | #2B4F86 | open |
| La República de Sonora | nation | 4 (AZ, NM, Sonora, Chihuahua) | #B59A45 | Tucson |
| The Prairie Federation | nation | 4 (AB, SK, MB, Ontario north of the DMZ line, incl. Manitoulin) | #E6D46A | open |
| The Midwest Republic | nation | 7 (ND, SD, NE, KS, MN, IA, MO; "Midwestland") | #52AE84 | leaning Omaha, not settled (left empty) |
| Appalachia | nation | 11 (WI, MI, IL, IN, OH, KY, WV, VA, MD, DE, DC) | #2F6A3E | Cincinnati |
| New England | nation | 9 (NY, PA, NJ, CT, RI, MA, VT, NH, ME) | #8660B4 | open |
| The CSA | nation | 11 (TX, OK, AR, LA, MS, AL, GA, FL, SC, NC, TN) | #DD7F3E | narrowed to Texas, city open |
| Quebec | nation | 5 (Québec, NL, NB, NS, PEI) | #6BC3D8 | Quebec City |
| Greenland | nation | 2 (Greenland admin-0 + Queen Elizabeth Islands) | #C166AE | Nuuk |
| The Sovereign Republic of Hawaii | nation | 1 (whole admin-1 Hawaii, Ni'ihau to Kure Atoll) | #1E8A8A | Honolulu is only an unasserted default; left empty |
| Demilitarized Zone | special area | 1 (Ontario south of the cut) | #C9413B | none |
| Neutral Scientific Territory | neutral zone | 1 (Baffin Island and satellites) | #FFFFFF | none |

No `group` / `group_role` values: the source defines no unions or blocs. The Neutral Scientific Territory is shared among Alaska, Greenland, the Prairie Federation and Quebec (stated in its note), not a member of any group.

## Special areas as the script treats them
- **Arctic archipelago** (Nunavut + NWT split island by island, classified by each island's representative point as in the script): north of 74.7N goes to Greenland (Queen Elizabeth Islands); east of 82W and north of 61.5N is the Neutral Scientific Territory; the rest stays Alaska.
- **DMZ**: Ontario south of the Mattawa River - Lake Nipissing - French River line, then south of Manitoulin (waypoints in the script). Manitoulin and Fitzwilliam Island stay Prairie Federation.
- **Alaska Panhandle**: Alaska south and east of the Jetté-Cook cut goes to Cascadia (the script's three-piece cut polygon, 85,000 km2 approx per its README).
- Cut polygons are built in the source's projection (Lambert azimuthal equal-area, 47N 96W), as the source builds them, densified to 1.5 km, then converted back to lon/lat so they reproduce the source's actual line (including the due-south-from-Mount-Cook edge noted in the source README).

## Checks (computed)
- All 14 geometries valid; zero pairwise overlaps (> 0.01 km2) in an equal-area projection; no overlap resolution was needed.
- Hawaii measures 16,848 km2, matching the figure in the source README. Midway Atoll is not inside the Hawaii polygon (distance about 0.9 degrees from it).
- Preview compared nation by nation with `north-america-nations.png`: shapes, the Panhandle, Baffin, the Queen Elizabeth Islands and the DMZ match; every unit sits in the same nation.

## Caveats and decisions
1. **Aleutians kept.** The source clips to longitudes -179.9..-10 (its map crop), which drops Alaska's islands west of the antimeridian. Here the full Natural Earth geometry is kept: Alaska has 9 parts at positive longitudes (east of 0, up to 179.8E), already split at 180 by Natural Earth, so the polygon is valid in -180..180. The source map does not show them.
2. **Great Lakes water is inside the polygons.** Natural Earth admin-1 polygons for Michigan, Wisconsin, Ontario, Ohio and the like include Great Lakes water; the source draws `ne_10m_lakes` (scalerank <= 3) on top. The atlas should draw lakes above the nations the same way. Hudson Bay and James Bay are not included (sea).
3. **Natural Earth version.** The source pins `natural-earth-vector` commit ca96624 (shapefiles). This build used the `.geojson` files in `/tmp/ne_test/` (same layers, version not recorded). All unit names resolved. A few boundary vertices may differ slightly from the source's pinned data; no visible difference in the preview.
4. **Capitals.** The map source (`na_nations.py`, README) gives none. The capitals in the table are the *settled* ones from the worldbuilding note `worldbuilding/nations/New North America - Territory Definitions (read from map).md` (Alaska 2026-09-22; Sonora, Appalachia, Quebec, Greenland 2026-09-26), with coordinates from Natural Earth populated places (Whitehorse, Tucson, Cincinnati, Québec, Nuuk; fetched from the local file). Unsettled ones are left empty (source: note, outside the map source folder).
5. **Out of scope on the source map, left out:** Saint-Pierre and Miquelon (a French territory, drawn as plain gray land), Bermuda, and all of Mexico except Baja California, Baja California Sur, Sonora and Chihuahua, plus Central America and the Caribbean.
6. **Hawaii is drawn as an inset on the source map** (not in true position). The polygons here are in true geographic position (-178.3 to -154.8 longitude).
7. **Midway Atoll** is deliberately outside the Republic in the source (it belongs to Natural Earth's "United States Minor Outlying Islands"); the source flags it as an open author question. Not included here. Other US Minor Outlying Islands (Wake, Johnston, Palmyra and others) are not in the source and not included; the whole-world atlas may need a decision.
8. Source open items inherited: where the Panhandle line meets the sea near Yakutat Bay (source README, "Open question"), and the label "LATIN AMERICA / unpartitioned" mismatch (label only).

## Seams with neighboring regions
- **Latin America (Mexico, Central America, Caribbean):** this region includes Mexico's Baja California, Baja California Sur (in Cascadia) and Sonora, Chihuahua (in La República de Sonora). The Latin America extraction must not also claim these four states. Mexico's other states (Coahuila, Nuevo León, Tamaulipas and the rest) belong to Latin America; the seam is the US-Mexico line from Texas to Chihuahua/Sonora plus the Sonora/Chihuahua southern borders and the Cascadia/Sonora seam through the Gulf of California. The Bahamas, Cuba and so on are Latin America (source legend).
- **Russia (Chukotka) and the Aleutians:** the Aleutians cross 180 degrees; Chukotka lies west of them.
- **Oceania:** Hawaii sits in North America by author decision (2026-09-26), not Oceania; the Oceania extraction should not include it. The Northwestern Hawaiian Islands to Kure Atoll are included here.
- Quebec and Greenland stay in North America's lineage; Greenland's polygon is the Natural Earth admin-0 outline plus the Queen Elizabeth Islands.
