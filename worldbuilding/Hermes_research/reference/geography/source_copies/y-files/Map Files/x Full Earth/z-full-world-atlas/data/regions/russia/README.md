# World atlas data: Russia

`nations.gpkg` (layers `nations`, `units`, `autonomous_zones`), built by `build_russia.py`, previewed in `preview.png`. Follows `../../../ATLAS SPEC - region data format.md`.

## What was used (all read-only)
- `x Full Earth/Russia/subdivisions.csv` (90 rows; the CSV header text still says 82, the 09 follow-up grew it) for the nation of every unit; `cyrillic_names.py` for native names; `kherson_left_bank.geojson` for Kherson east of the Dnieper (computed by the Europe project from the Natural Earth Dnieper centerline).
- Natural Earth 10m admin-1 (`/tmp/ne_test/`; a 92-feature subset is kept in `cache/ne-admin1-russia-ukraine-subset.geojson` so the build is reproducible; source URL pattern `https://naciscdn.org/naturalearth/10m/cultural/ne_10m_admin_1_states_provinces.zip`).
- Capitals and coordinates: `render_map_russia_full.py` (CAPS and CAPS_LATIN_ONLY, author-confirmed 2026-09-27 per CHANGES.md and the capital-candidate notes). Europe README for naming and the C-15 ruling.

## Final state chosen and why
The `09 follow-up` state of the Russia package (the latest, 2026-09-30: Crimea and Sevastopol as an Autonomous Zone of Donska-Kubania; Luhansk, Donetsk, Kharkiv, Dnipropetrovsk, Zaporizhzhia in full and Kherson east of the Dnieper in the Russia nation), PLUS Europe's final map C-15 (author, 2026-09-30): the Republic of Karelia is part of Finland and Murmansk Oblast is part of Idelsk-Uralia. The package's own maps and CSV still show the proto-country "Karelia" (Karelia plus Murmansk); that nation does not exist here.

## Nations (13; units dissolved)
| nation | units | capital | note |
|---|---|---|---|
| Russia | 24 | Moscow | 18 core + 6 eastern-Ukraine units (Kherson left bank only) |
| Idelsk-Uralia | 26 | Nizhny Novgorod | includes Murmansk (C-15) |
| Donska-Kubania | 9 | Rostov-on-Don | includes Crimea + Sevastopol as an Autonomous Zone (also layer `autonomous_zones`) |
| Künnarantaiga | 12 | Vladivostok | Sakha, Irkutsk, Buryatia, Chukotka, Sakhalin with the Kurils, etc. |
| Siberia | 11 | Novosibirsk | |
| Tuva | 1 | Kyzyl | |
| Chechnya, Ingushetia, Dagestan, North Ossetia-Alania, Kabardino-Balkaria, Karachay-Cherkessia | 1 each | Grozny, Magas, Makhachkala, Vladikavkaz, Nalchik, Cherkessk | |
| Finland | 1 | (none) | the Republic of Karelia only; `group` Scandinavian Trade Union, `member` (from the Europe README; Europe's Finland row should win on conflict); color empty |

`kind` is `nation` for every row (the package calls them nations; the Autonomous Zone is a layer, not a separate row, so the merge by name stays clean). `color` is the package hex; native names from `cyrillic_names.py` (not set for the Finland row). Dagestan, Donska-Kubania and Finland are multipart; Künnarantaiga, Siberia and Idelsk-Uralia carry many island parts (Arctic archipelagos, Kurils, Sakhalin).

## Checks
- Valid geometry, longitudes within -180..180 (Natural Earth already cuts Chukotka and Wrangel at the antimeridian; checked: no polygon spans it), no overlaps between rows (computed).
- 73 sub-1e-3 deg2 sliver holes (the Kherson left-bank cut does not meet Zaporizhzhia and Crimea exactly, computed) were filled into the neighbor with the longest shared border; the `units` layer keeps the unfilled shapes.
- Visual: `preview.png` against `x Full Earth/Russia/russia_reference_map.png`: all nation shapes and unit assignments match; the only differences are the intended ones (Karelia gold is now Finland, Murmansk is in Idelsk-Uralia, the eastern-Ukraine slice and Crimea are added). The reference PNG on disk (dated 09-27) predates the slice, so the slice was checked against the CSV/CHANGES and the script logic instead.

## Caveats and seams
- **Kaliningrad is NOT in `subdivisions.csv`** (the package draws it as neutral background); it is not in this file. The Europe region supplies it (Confederacy member, per C-15).
- **Ukraine seam with Europe:** Europe supplies Ukraine without the eastern slice. The slice's western edge is Natural Earth's oblast borders (Kharkiv, Dnipropetrovsk, Zaporizhzhia) and the Kherson left-bank line; Europe's `eastern-ukraine-east-side.geojson` and Europe's own base may be cut slightly differently, so expect slivers or overlaps along that edge (not compared). The Kherson raion-level cut is unsettled per the package. Crimea touches Kherson at the isthmus.
- **Finland seam:** Karelia's western edge is the Natural Earth Russia-Finland border; Europe's Finland polygon may differ by a few km.
- **Karelia/Murmansk:** the Karelia-Murmansk and Karelia-Arkhangelsk internal borders are unit borders and exact.
- **East Asia seam:** the southern borders (China, Mongolia, Kazakhstan, North Korea) and the Kuril/Sakhalin edge are Natural Earth admin-1 outlines; the East Asia region may use a different vintage, so small slivers are possible. Not compared. Russia (NE admin-0) minus this file is only Kaliningrad; this file minus admin-0 Russia is only the Ukrainian slice and Crimea (computed).
- One unnamed Natural Earth islet (about lon 67.3, lat 68.8, "RUS-99 minor island") is dropped, as in the package's own scripts.
- Capitals not decided in the package: Crimea Autonomous Zone (Simferopol only an obvious candidate), Finland's Karelia piece; left empty. Idelsk-Uralia and Donska-Kubania names are still placeholders per the package; Cyrillic forms are letter-for-letter transliterations.
- Natural Earth borders on the Caucasus (Dagestan, Chechnya and so on) are those of present-day republics.
