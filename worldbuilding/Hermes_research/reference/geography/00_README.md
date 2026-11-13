STATUS: ready (2026-11-12). Written by Claude.

# Geography folder for Hermes (read only)

**What this is.** The geographic information Hermes needs to know **which real-world places each post-war nation covers**: a compiled table, and copies of the source files it was built from. The compiled table and these copies are Claude's. **The Lead Developer's note (2026-11-12) makes this folder a write location as well:** relevant results go here, organized to match the source folder structure, so that Claude can see what each piece of data is relevant to and where the conclusions that use it belong. Where to put a new geography result is in the section below.

**Start with** `01_territories_by_target.md`: one file, one entry per target, built from the sources below. Use `source_copies/` to check a detail.

**These are snapshots.** The copies were made on 2026-11-12 from the map-data folders (`y-files/Map Files/x Full Earth/` and the CurrentNovelDocs `worldbuilding/nations/` notes). The originals keep changing; they are the authority. Each copy's original path is in the table below.

**Superseded or stale files were left out on purpose:** the older numbered "follow-up" and archive folders, the early-state `worldbuilding/nations/russia-map-data/` (it mirrors the old 20-nation Russia), and the roster `World-Nations-Roster.md` (stale for Europe).

**Left out:** South Asia (no South Asian population came to Tepenia), and the map images and geometry files (`.png`, `.gpkg`, `.geojson`), which Hermes cannot use as text.

## How `source_copies/` is organized

Each copy sits at the **same path as its original, counted from the `media/` folder** (`/home/kuroskalacs/Documents/Doll-Fi/media/`). For example, the original `y-files/Map Files/x Full Earth/North America/north-america-nations/reference/nations-assignment.csv` is copied to `source_copies/y-files/Map Files/x Full Earth/North America/north-america-nations/reference/nations-assignment.csv`. A file extracted from a zip sits in a folder named after the zip. New geography results follow the same rule: put each one at the path of the source folder it bears on.

## Where each copy came from

| Copy (under `source_copies/`) | Original (under `media/`) | What it holds |
|---|---|---|
| `y-files/Map Files/x Full Earth/North America/north-america-nations/reference/nations-assignment.csv` | `y-files/Map Files/x Full Earth/North America/north-america-nations/reference/nations-assignment.csv` | the final subdivision-to-nation table (one row per state, province or part) |
| `y-files/Map Files/x Full Earth/North America/north-america-nations/README.md` | `y-files/Map Files/x Full Earth/North America/north-america-nations/README.md` |  |
| `y-files/Map Files/x Full Earth/North America/CHANGES.md` | `y-files/Map Files/x Full Earth/North America/CHANGES.md` |  |
| `y-files/Map Files/x Full Earth/z-full-world-atlas/data/regions/north-america/README.md` | `y-files/Map Files/x Full Earth/z-full-world-atlas/data/regions/north-america/README.md` |  |
| `Literature/books/CurrentNovelDocs/worldbuilding/nations/New North America - Territory Definitions (read from map).md` | `Literature/books/CurrentNovelDocs/worldbuilding/nations/New North America - Territory Definitions (read from map).md` | older (2026-09-22); superseded in places by the CSV (for example Tennessee) |
| `Literature/books/CurrentNovelDocs/worldbuilding/nations/México (post-war) - Territory and Open Research.md` | `Literature/books/CurrentNovelDocs/worldbuilding/nations/México (post-war) - Territory and Open Research.md` |  |
| `Literature/books/CurrentNovelDocs/worldbuilding/nations/Sovereign Republic of Hawaii - National Character Profile.md` | `Literature/books/CurrentNovelDocs/worldbuilding/nations/Sovereign Republic of Hawaii - National Character Profile.md` | Hawaii's territory is stated in the profile |
| `Literature/books/CurrentNovelDocs/worldbuilding/Deep_Culture_Investigation/Targets/Cascadia/00 - Scope.md` | `Literature/books/CurrentNovelDocs/worldbuilding/Deep_Culture_Investigation/Targets/Cascadia/00 - Scope.md` | the model Stage 0 scope: territory and units |
| `Literature/books/CurrentNovelDocs/worldbuilding/Deep_Culture_Investigation/Data/Unit_Territories.md` | `Literature/books/CurrentNovelDocs/worldbuilding/Deep_Culture_Investigation/Data/Unit_Territories.md` | each unit's counties, census divisions or municipios (Cascadia) |
| `y-files/Map Files/x Full Earth/Latin America/nations-assignment.csv` | `y-files/Map Files/x Full Earth/Latin America/nations-assignment.csv` | the final subdivision-to-nation table |
| `y-files/Map Files/x Full Earth/z-full-world-atlas/data/regions/latin-america/README.md` | `y-files/Map Files/x Full Earth/z-full-world-atlas/data/regions/latin-america/README.md` |  |
| `y-files/Map Files/x Full Earth/Europe/README - Europe INIT 2083 map.md` | `y-files/Map Files/x Full Earth/Europe/README - Europe INIT 2083 map.md` |  |
| `y-files/Map Files/x Full Earth/z-full-world-atlas/data/regions/europe/README.md` | `y-files/Map Files/x Full Earth/z-full-world-atlas/data/regions/europe/README.md` | the final Europe state (map C-15) and its nation list with unit counts |
| `y-files/Map Files/x Full Earth/Europe/archive 01/OPEN QUESTIONS - Western Europe (for the later European worldbuilding pass).md` | `y-files/Map Files/x Full Earth/Europe/archive 01/OPEN QUESTIONS - Western Europe (for the later European worldbuilding pass).md` |  |
| `y-files/Map Files/x Full Earth/Europe/archive 01/DECISION LOG - Eastern Ukraine and Crimea.md` | `y-files/Map Files/x Full Earth/Europe/archive 01/DECISION LOG - Eastern Ukraine and Crimea.md` |  |
| `y-files/Map Files/x Full Earth/Europe/archive 01/DECISION LOG - Confederacy of Intermarium Nations (membership order).md` | `y-files/Map Files/x Full Earth/Europe/archive 01/DECISION LOG - Confederacy of Intermarium Nations (membership order).md` |  |
| `y-files/Map Files/x Full Earth/Europe/archive 01/Eastern Ukraine - Candidate Border Lines (working).md` | `y-files/Map Files/x Full Earth/Europe/archive 01/Eastern Ukraine - Candidate Border Lines (working).md` |  |
| `Literature/books/CurrentNovelDocs/worldbuilding/nations/Europe - GDD hand-over intake (Santa Luce, the two Italys, the CIN; 2026-10-23).md` | `Literature/books/CurrentNovelDocs/worldbuilding/nations/Europe - GDD hand-over intake (Santa Luce, the two Italys, the CIN; 2026-10-23).md` |  |
| `y-files/Map Files/x Full Earth/Africa/country-borders decision log.md` | `y-files/Map Files/x Full Earth/Africa/country-borders decision log.md` |  |
| `y-files/Map Files/x Full Earth/Africa/02 reorganization/reconstruction/README - Africa reconstruction.md` | `y-files/Map Files/x Full Earth/Africa/02 reorganization/reconstruction/README - Africa reconstruction.md` |  |
| `y-files/Map Files/x Full Earth/Africa/01 initial generations/README - Africa full-continent initial cultural maps.md` | `y-files/Map Files/x Full Earth/Africa/01 initial generations/README - Africa full-continent initial cultural maps.md` |  |
| `y-files/Map Files/x Full Earth/Russia/subdivisions.csv` | `y-files/Map Files/x Full Earth/Russia/subdivisions.csv` | the 09 follow-up (2026-09-30): subdivision to nation |
| `y-files/Map Files/x Full Earth/Russia/CHANGES.md` | `y-files/Map Files/x Full Earth/Russia/CHANGES.md` |  |
| `y-files/Map Files/x Full Earth/z-full-world-atlas/data/regions/russia/README.md` | `y-files/Map Files/x Full Earth/z-full-world-atlas/data/regions/russia/README.md` | includes the Europe C-15 changes (Karelia to Finland, Murmansk to Idelsk-Uralia) |
| `y-files/Map Files/x Full Earth/Asia/Asia (East)/asia-east-current/CURRENT STATE - East Asia Map Series.md` | `y-files/Map Files/x Full Earth/Asia/Asia (East)/asia-east-current.zip::asia-east-current/CURRENT STATE - East Asia Map Series.md` | extracted from the zip (map F state) |
| `y-files/Map Files/x Full Earth/Asia/Asia (East)/asia-east-current/Native Names - East Asia Polities.md` | `y-files/Map Files/x Full Earth/Asia/Asia (East)/asia-east-current.zip::asia-east-current/Native Names - East Asia Polities.md` | extracted from the zip (map F state) |
| `y-files/Map Files/x Full Earth/Asia/Asia (East)/asia-east-current/data/maps.csv` | `y-files/Map Files/x Full Earth/Asia/Asia (East)/asia-east-current.zip::asia-east-current/data/maps.csv` | extracted from the zip (map F state) |
| `y-files/Map Files/x Full Earth/Asia/Asia (East)/asia-east-current/data/polities.csv` | `y-files/Map Files/x Full Earth/Asia/Asia (East)/asia-east-current.zip::asia-east-current/data/polities.csv` | extracted from the zip (map F state) |
| `y-files/Map Files/x Full Earth/Asia/Asia (East)/asia-east-current/data/province_assignments.csv` | `y-files/Map Files/x Full Earth/Asia/Asia (East)/asia-east-current.zip::asia-east-current/data/province_assignments.csv` | extracted from the zip (map F state) |
| `y-files/Map Files/x Full Earth/Asia/Asia (East)/README.md` | `y-files/Map Files/x Full Earth/Asia/Asia (East)/README.md` |  |
| `y-files/Map Files/x Full Earth/z-full-world-atlas/data/regions/east-asia/README.md` | `y-files/Map Files/x Full Earth/z-full-world-atlas/data/regions/east-asia/README.md` |  |
| `y-files/Map Files/x Full Earth/Asia/Asia (Southeast)/subdivisions.csv` | `y-files/Map Files/x Full Earth/Asia/Asia (Southeast)/subdivisions.csv` |  |
| `y-files/Map Files/x Full Earth/Asia/Asia (Southeast)/subdivisions_maritime.csv` | `y-files/Map Files/x Full Earth/Asia/Asia (Southeast)/subdivisions_maritime.csv` |  |
| `y-files/Map Files/x Full Earth/z-full-world-atlas/data/regions/southeast-asia/README.md` | `y-files/Map Files/x Full Earth/z-full-world-atlas/data/regions/southeast-asia/README.md` |  |
| `Literature/books/CurrentNovelDocs/worldbuilding/nations/central-asia-map-data/regions.csv` | `Literature/books/CurrentNovelDocs/worldbuilding/nations/central-asia-map-data/regions.csv` |  |
| `Literature/books/CurrentNovelDocs/worldbuilding/nations/central-asia-map-data/subdivisions.csv` | `Literature/books/CurrentNovelDocs/worldbuilding/nations/central-asia-map-data/subdivisions.csv` |  |
| `y-files/Map Files/x Full Earth/z-full-world-atlas/data/regions/west-asia/README.md` | `y-files/Map Files/x Full Earth/z-full-world-atlas/data/regions/west-asia/README.md` | covers Central Asia, the Middle East and the South Caucasus |
| `y-files/Map Files/x Full Earth/Oceania/subdivisions.csv` | `y-files/Map Files/x Full Earth/Oceania/subdivisions.csv` |  |
| `y-files/Map Files/x Full Earth/z-full-world-atlas/data/regions/oceania/README.md` | `y-files/Map Files/x Full Earth/z-full-world-atlas/data/regions/oceania/README.md` |  |
| `y-files/Map Files/x Full Earth/z-full-world-atlas/README.md` | `y-files/Map Files/x Full Earth/z-full-world-atlas/README.md` |  |
| `y-files/Map Files/x Full Earth/z-full-world-atlas/data/world/merge_report.md` | `y-files/Map Files/x Full Earth/z-full-world-atlas/data/world/merge_report.md` |  |
| `games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Official_Population_Census (Section E extract only).md` | `games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Official_Population_Census.md, Section E` | extract |

## Known gaps (also at the end of each part of the table)

- Greenland has no census row and no source names its pre-war sovereign.
- Brussels, the German-speaking Community of Belgium, Navarre, Sardinia's status and the Karelia timing are open in the Europe sources.
- Jeju-do, Kaliningrad, Crimea and Sevastopol, Kherson (left bank), the Paracel and Spratly islands, and the Pacific territories are open or provisional.
- The census (Section E) has no row for Kaliningrad or South Africa, and lists Spain's carrying rows as only Basque Country and Catalonia.
- Territory below the first-order subdivision (counties, municipalities) is in Cascadia's `Unit_Territories.md` only.
