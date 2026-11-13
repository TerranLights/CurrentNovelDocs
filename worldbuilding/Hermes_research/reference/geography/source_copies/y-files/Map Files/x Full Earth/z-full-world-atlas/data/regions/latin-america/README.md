# latin-america: region data for the world atlas

Output: `nations.gpkg` (layer `nations`, EPSG:4326, 43 rows = 42 nations + 1 unclaimed territory), `build_latin-america.py`, `render_preview.py`, `preview.png`.

## What was used
- Authoritative script: `Latin America/nations.py` (top level, last written 2026-09-28 18:26). Its tables (`N`, `DEFAULT`, `EXCEPT`, `BRAZIL`, `ISLAND_NATION`, `UNCLAIMED`) are read directly by the build script (parsed, not re-derived), plus `OUT_OF_SCOPE` from `latin-america-nations/regions_geo.py`.
- Geometry: Natural Earth 10m admin-1 and admin-0 geojson from `/tmp/ne_test/`, clipped to the source's own clip box (lon -130..-20, lat -60..40). The package's pinned shapefile download was not used (computed check: all 394 CSV subdivision names matched the geojson exactly).
- Verification (computed): the build asserts that every one of the 394 rows of `nations-assignment.csv` is present with the same nation, with none missing and none extra (394 of 394 matched, 0 wrong). Also compared by eye against `map-7-nations.png` and the detail map; shapes and colors agree.
- Overlaps between nations inside the region: none found (computed, 0 km2). The merge step should still check seams against neighboring regions.

## Which state is final
The top-level `nations.py` and `nations-assignment.csv` (2026-09-28), not the `latin-america-nations/` package. The package README says it reproduces round 09 (2026-09-25), but its `nations.py` predates the 2026-09-28 changes: the top-level script renames the zone to "Araucanía-Patagonia Autonomous Zone" (author-supplied, bilingual with ZAPA) and adds the English / Spanish / Maya label for Yucatán. Assignments are identical between the two; only names and labels differ. The `archive NN` folders and `clean test-run` were ignored.

## Brazil
The final map does NOT cut Brazil geometrically. `regions_geo.py::brazil_pieces` (Ribeiro's five "Brasis") belongs to the earlier culture-region maps; the final nations use whole states: seven (Acre, Amazonas, Amapá, Pará, Rondônia, Roraima, Mato Grosso) go to Amazonia, the other 20 units (19 states plus the Distrito Federal) stay Brazil. Brazil = 20 units, Amazonia = 14 units (7 Brazilian states + Pando, Amazonas/Vaupés/Guainía of Colombia, Amazonas and Bolívar of Venezuela, Loreto of Peru).

## Names
`nation` is the legend name on `map-7-nations.png`: "México", "La República de Yucatán" (the map label also gives English "The Republic of Yucatán" and Maya "U Kuchkabal Mayab"; these go in `native`), "Araucanía-Patagonia Autonomous Zone", "Virgin Islands", "French Antilles" and "Aruba-Curaçao" (these three are working names in the source), "Saint Martin" (final name; bilingual French/Dutch). Brazil's, Guyana's etc. names are the plain ones. The `nation_key` column (extra, after the contract columns) holds the source's three-letter key (MEX, YUC, AMZ, ...).

## Nations (units dissolved; area computed on an equal-area projection)
- Aruba-Curaçao: 2 unit(s); 633 km2; Aruba + Curaçao (working name)
- Anguilla: 1 unit(s); 87 km2; stays independent of Saint Kitts and Nevis
- Amazonia: 14 unit(s); 5,556,030 km2; trans-national basin: Pando, Amazonas/Vaupés/Guainía (CO), Amazonas/Bolívar (VE), Loreto + seven whole Brazilian states
- Argentina: 19 unit(s); 1,996,543 km2
- Antigua and Barbuda: 2 unit(s); 551 km2; includes Montserrat
- The Bahamas: 1 unit(s); 12,604 km2
- Belize: 6 unit(s); 22,299 km2
- Bolivia: 8 unit(s); 1,023,109 km2
- Brazil: 20 unit(s); 4,017,495 km2; all Brazil except the seven states in Amazonia
- Barbados: 1 unit(s); 444 km2
- Chile: 11 unit(s); 413,380 km2
- Colombia: 30 unit(s); 902,797 km2
- Costa Rica: 7 unit(s); 51,151 km2
- Cuba: 2 unit(s); 109,995 km2; includes Guantánamo Bay naval base
- Dominica: 1 unit(s); 730 km2
- Dominican Republic: 2 unit(s); 75,331 km2; whole island of Hispaniola (Haiti absorbed)
- Ecuador: 24 unit(s); 255,026 km2
- El Salvador: 14 unit(s); 20,539 km2
- French Antilles: 2 unit(s); 2,755 km2; Guadeloupe and Martinique (working name)
- French Guiana: 1 unit(s); 83,184 km2; Guyane française, sovereign in this setting
- Grenada: 1 unit(s); 347 km2
- Guatemala: 21 unit(s); 72,751 km2
- Guyana: 10 unit(s); 211,214 km2
- Honduras: 18 unit(s); 112,236 km2
- Jamaica: 3 unit(s); 11,787 km2; includes the Cayman Islands and Turks and Caicos Islands
- Saint Kitts and Nevis: 1 unit(s); 264 km2
- Saint Lucia: 1 unit(s); 605 km2
- México: 23 unit(s); 1,148,673 km2; Mexico minus the five Yucatán-bloc estados; Sonora, Chihuahua and both Bajas are out of scope (North America region)
- Nicaragua: 17 unit(s); 128,684 km2
- Panama: 12 unit(s); 74,531 km2
- Paraguay: 18 unit(s); 399,901 km2
- Araucanía-Patagonia Autonomous Zone: 10 unit(s); 1,109,568 km2; demilitarized Argentina-Chile condominium: 5 Chilean regions + 5 Argentine provinces
- Peru: 25 unit(s); 916,090 km2
- Puerto Rico: 1 unit(s); 9,006 km2
- Saint Martin: 3 unit(s); 116 km2; whole island (French + Dutch halves) + Saint Barthélemy; bilingual French/Dutch
- Suriname: 10 unit(s); 145,123 km2
- Trinidad and Tobago: 1 unit(s); 5,123 km2
- Uruguay: 19 unit(s); 177,342 km2
- Saint Vincent and the Grenadines: 1 unit(s); 368 km2
- Venezuela: 23 unit(s); 481,607 km2
- Virgin Islands: 2 unit(s); 500 km2; US + British Virgin Islands (working name)
- La República de Yucatán: 6 unit(s); 272,903 km2; Chiapas, Tabasco, Campeche, Yucatán, Quintana Roo (Mexico) + Petén (Guatemala)
- Falkland Islands: 1 unit(s); 11,597 km2; deliberately unclaimed in the source (drawn pale, outlined); not one of the 42 nations

## Extras and deliberate choices
- Capital: the source gives one only for Amazonia ("capital Manaus", in `nations.py`); coordinates are from Natural Earth populated places (fetched from the local geojson). All other `capital` fields are empty. The source maps plot reference cities (Mexico City, Bogotá, Caracas, ...) but never call them capitals.
- Group: Guyana, Suriname and French Guiana are tied by a "NAFTA-style trade union" that the source does not name; the `group` cell says so (`Guianas trade union (NAFTA-style, unnamed in source)`, role member). No other bloc is named in the source.
- Falkland Islands: the source draws them pale and outlined, "deliberately unclaimed" (not gray out-of-scope), so they are kept as a 43rd row with `kind = unclaimed territory`. Drop this row if the atlas should leave them to another layer; it is not one of the 42 nations.
- Left out as out of scope (the source's gray hatched areas, covered by the North America region): Sonora, Chihuahua (La República de Sonora) and Baja California / Baja California Sur (Cascadia). The United States is not included; Hawaii is outside the clip box.

## Caveats and seams
- Caribbean: Haiti is absorbed into the Dominican Republic (whole of Hispaniola, one nation); Jamaica = Jamaica + Cayman Islands + Turks and Caicos (three separate pieces, one row); Antigua and Barbuda includes Montserrat; Virgin Islands = US + British; Saint Martin = both halves + Saint Barthélemy; Anguilla is its own nation; Cuba includes the Guantánamo base polygon.
- French Guiana is a sovereign nation here (Natural Earth admin-1 "Guyane française"); Guadeloupe and Martinique form French Antilles. These are the only parts of France in the region; any other French overseas piece in another region's data (for example Réunion) is not touched.
- Puerto Rico is its own nation (not US territory); the merge with North America should not also claim it. Natural Earth admin-0 "United States Virgin Islands" is in Virgin Islands here, not in North America.
- Islands inside the clip box that the source does NOT assign to any nation (so they are gaps in this region): Bermuda; Clipperton Island; Bonaire, Saba and Sint Eustatius (Natural Earth lists them under "Netherlands"); Bajo Nuevo Bank and Serranilla Bank; the Uruguay River islet "Brazilian Island"; "South Georgia and the Islands" (outside the source map frame); the Southern Patagonian Ice Field polygon. Pitcairn (Oceania) and the Azores/Cabo Verde (Europe/Africa) fall inside the clip box but belong to other regions and are not included. These are candidates for the author to decide.
- Clipping: the source clips at 60 S, so Chile's and Argentina's Antarctic claims are cut off at 60 S (Tepenia/Antarctica region covers that).
- Seams: Mexico meets North America at the Sonora/Chihuahua and Baja borders, which come from Natural Earth admin-1 lines (no overlap or gap computed against the North America output, which was not available). Border seams between different countries' admin-1 polygons come from separate Natural Earth country shapes; none of them overlap, but thin slivers can exist.
- Author decisions pending in the source: three working names (Virgin Islands, French Antilles, Aruba-Curaçao); maps are labeled "working names, not final".
