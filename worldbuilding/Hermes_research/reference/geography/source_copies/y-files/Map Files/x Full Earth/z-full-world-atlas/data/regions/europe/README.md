# Region `europe`: final-state nation polygons (map C-15)

**Deliverable:** `nations.gpkg`, layer `nations` (EPSG:4326, 51 rows: 49 nations, 1 autonomous zone, 1 disputed area). **Rebuild:** `build_europe.py` (reads `../../../../Europe/` read-only, or the folder in env `EUROPE_SRC`; imports the Europe project's own `render_europe_init.py` and `render_europe_series.py`, so no borders are re-derived). **Preview:** `preview.png` (2400 px; each nation in the INIT map's own color; gray hatch = left to the Russia extraction). All counts and areas below are computed by the build unless flagged.

## Final state chosen, and why
Map **C-15** (`europe-C-15-wave-15-skoprodija.png`), the last of the series (computed from the script's stage list: INIT, B, C-00 to C-15; README of the Europe folder states C-15 is the last and the only one that resolves Karelia). Used, as C-15 draws them:
- Scandinavian Trade Union (from map B, persists on all C maps): Norway, Sweden, Finland, Denmark, Iceland, Faroe Islands, `group_role` = `member`.
- Confederacy of Intermarium Nations at C-15: **members** (17): Poland, Lithuania, Kaliningrad, Czechia, Slovakia, Latvia, Estonia, Ukraine, Hungary, Romania, Moldova, Bulgaria, Croatia, Slovenia, Serbia, Montenegro, Greece. **Observers** (3): Belarus (admitted "restricted", drawn hatched like an observer; the note says so), Bosnia and Herzegovina, Skoprodija. **Barred**: Albania.
- `color` is the color C-15 draws (teal `#62b3a8` for Union members, crimson `#b83b4d` for Confederacy members, light crimson `#e9b4bc` for observers, `#5a5650` for Albania, the INIT palette color for the rest).
- `native` holds the native names the Europe script documents (Ukraine, Belarus, Bulgaria, Serbia, Montenegro, Greece, Cyprus, Bosnia and Herzegovina; Cyrillic or Greek). The Europe data documents none for the Latin-script nations.

## Left to the Russia agent (NOT in this file)
Russia (core, **including the eastern-Ukraine slice**: Luhansk, Donetsk, Kharkiv, Dnipropetrovsk, Zaporizhzhia and Kherson east of the Dnieper, `Europe/data/eastern-ukraine-east-side.geojson`), Idelsk-Uralia (**with Murmansk Oblast** at C-15), Donska-Kubania (**with Crimea and Sevastopol**), Karelia (**the Republic, which at C-15 joins Finland**; the Russia agent must hand it to `Finland`), Chechnya, Dagestan, Ingushetia, Kabardino-Balkaria, Karachay-Cherkessia, North Ossetia-Alania. Siberia, Kunnarantaiga and Tuva are in Russia's csv but not drawn by the Europe maps.
- **My `Finland` excludes the Republic of Karelia** (it keeps the Finnish regions called North and South Karelia, and Aland). **My `Ukraine` excludes the eastern slice and Crimea** (the Ukraine row is the 25 Ukraine units with `east_ua` cut away; the Russia agent should use the same `eastern-ukraine-east-side.geojson` so the seam closes).
- **Kaliningrad is mine**: it is a Confederacy member nation here (source unit `Russia/Kaliningrad` in `europe-base.gpkg`), and is not in Russia's `subdivisions.csv`.
- Seams: Finland/Karelia, Estonia and Latvia/Russia, Belarus/Russia and Ukraine/Russia join Natural Earth admin-0 (mine) with Natural Earth admin-1 (`ne-russia-admin1.geojson`, Russia agent's); expect slivers or small overlaps at those borders (not checked, the other extraction does not exist yet).

## Nations (49) with unit counts
Scandinavian Trade Union: Norway 19, Sweden 21, Finland 29 (18 + 11 Aland), Denmark 5, Iceland 9, Faroe Islands 1.
British Isles: United Kingdom 209 (England, Scotland, Wales units + Gibraltar, Akrotiri, Dhekelia), Northern Ireland 26, Ireland 34, Crown Dependencies 3 (Isle of Man, Jersey, Guernsey).
West and Alps: France 105 (with Wallonia 5, Brussels 1, Luxembourg 3), Netherlands 17 (with Flanders 5), Germany 15 (no Bavaria), Austro-Bavaria 10, Switzerland 26, Liechtenstein 11, Monaco 1.
Iberia: Spain 44, Catalonia 4, Basque Country 6 (4 provinces + the Trevino and Villaverde enclave parts), Portugal 20, Andorra 7.
Italy and Malta: Magna Lombardia 64, Meridia 37 (without Sicilia), San Marino 9, Vatican City 1, Malta 68.
Confederacy: Poland 16, Lithuania 10, Kaliningrad 1, Latvia 119, Estonia 15, Belarus 7 (observer), Ukraine 25, Czechia 14, Slovakia 8, Hungary 48 (43 + 5 Romanian counties), Romania 37, Moldova 40, Bulgaria 29 (with Kirklareli), Slovenia 193, Croatia 21, Serbia 55 (with Kosovo), Montenegro 21, Bosnia and Herzegovina 18 (observer), Skoprodija 72 (observer; North Macedonia without the 12-municipality Albanian belt), Albania 24 (barred; with the belt), Greece 16 (with Edirne and Tekirdag).
Mediterranean: Cyprus 6 (whole island with Northern Cyprus; the Green Line is a dashed line on the maps, not a boundary here).
Special rows: **Sicilia** (`autonomous zone`, 9 units; cut out of Meridia) and **Transnistria** (`disputed`, 2 geoBoundaries units; cut out of Moldova), because the Europe maps hatch them as separate overlays. Their `group` is empty and their color is the parent's.

## Special areas kept only as notes
Gibraltar and the Akrotiri/Dhekelia base areas (inside `United Kingdom`, not drawn separately); Trevino and Villaverde (inside `Basque Country`, cut out of `Spain`); the Albanian belt (inside `Albania`); the Partium counties (inside `Hungary`); East Thrace (inside Greece and Bulgaria); Brussels and the German-speaking Community (drawn French by default, under review in the source); Kosovo (inside Serbia). Crimea as an Autonomous Zone belongs to the Russia extraction (Donska-Kubania).

## Greenland, Svalbard, others
- **Greenland**: the Europe data holds it only as a Natural Earth country polygon in the `countries` layer, drawn hatched and labeled "Greenland (Danish; honorary in the Union)", off the frame. It is not a nation in the Europe data, so it is **not output** (note on `Denmark`). The author/atlas must decide who draws it.
- **Svalbard and Jan Mayen**: not in the Europe data (Norway has 19 mainland county units); not output.
- Not in the Europe data: the Canary Islands, Madeira, the Azores (the README says so); Turkey, the Caucasus, North Africa, Central Asia and the Middle East are gray "out of scope" (other regions).

## Checks
Compared `preview.png` with `europe-C-15-wave-15-skoprodija.png` nation by nation: shapes and unit membership match (Finland without Karelia, Ukraine without the east, Hungary with the Partium, Skoprodija and Albania with the belt split, Greece and Bulgaria with Thrace, Kaliningrad, Cyprus whole). No overlaps above 0.01 km2 between rows (computed). All geometries valid, longitudes within -180..180, no antimeridian cases.

## Caveats
- Geometry is built in the Europe project's Lambert azimuthal frame and reprojected to EPSG:4326; vertices round-trip exactly, but expect hairline gaps of a few meters where the source itself leaves them (for example the 5 m cut around the Spanish enclaves).
- Small overlaps resolved the way the source draws them (later drawn on top): the Cyprus units overlap the UK base-area polygons by about 1.5 km2 (removed from `United Kingdom`); Vatican City is cut out of Meridia. Vatican City is only about 0.01 km2 in the source data and Monaco about 19 km2 (Natural Earth shapes, computed), so they will look tiny or oversized.
- Moldova minus Transnistria and Meridia minus Sicilia drop slivers under 0.1 km2.
- Natural Earth geometry is the 10m vintage the source used; some unit names in `units` (Latvia 119, Slovenia 193, Malta 68) are municipalities, so the unit counts are not comparable across nations.
- Open in the source (author decisions, not mine): when Karelia/Murmansk change hands, Bosnia's timing, the Brussels split, Belarus's "restricted" status mapped here to `observer`.
