# west-asia atlas data

Output: `nations.gpkg` (layer `nations`, 30 rows, EPSG:4326). Reproduce with `build_west-asia.py` (reads the source folder and the author's repo CSVs read-only; env vars `WA_SRC`, `NE_DIR`, `DATA_ROOT`, `OUT_DIR`), preview with `preview_west-asia.py` -> `preview.png`.

## Final state used
The `08 follow-up` state in `Asia/Asia (West)/` (`CHANGES.md`, 2026-09-30): the three East Thrace provinces (Edirne, Kirklareli, Tekirdag) are removed from Turkey and NOT in this package (Europe: Edirne and Tekirdag to Greece, Kirklareli to Bulgaria). Istanbul Province stays Turkish. This is the latest dated state; the composite map (`west-asia-composite-map.png`, 2026-09-30) is the authority. The CSVs in the repo (`middle-east-map-data/regions.csv` and `subdivisions.csv`, edited 2026-09-30) are the data the scripts read.

## What a "nation" is here
The composite map does not draw the present-day countries; it draws the author's regions (one `region_id` per legend entry), some of which split or join real countries. Each row of `nations` is one such legend entry, dissolved from Natural Earth 1:10m admin-1 units. The assignment logic is not re-derived: the Central Asia crosswalk (`CA_ASSIGN`, `CA_NE2CSV`) and the Middle East/South Caucasus name matching are copied verbatim from `west-asia-composite-render.py` (marked BEGIN/END in the build script), and `classify()`, `REGIONS` and `OVERRIDES` are imported from the source folder's `middle_east_classify.py` and `middle_east_name_map.py`. `nation` is the composite legend name exactly (including parentheticals such as `Abkhazia (contested)`).

## Nations (units = Natural Earth units dissolved)
Central Asia: Kazakhstan 16; Kyrgyzstan 5 (without Batken, Jalal-Abad, Osh); Turkmenistan 5; Uzbekistan 10; Karakalpakstan 1 (autonomous zone inside Uzbekistan); Tajikistan 5; Fergana Valley (Uncertain Territory) 6 (Uzbekistan's Fergana/Andijan/Namangan + Kyrgyzstan's Batken/Jalal-Abad/Osh, cross-border).
Middle East: Kurdistan 21 (cross-border: Iraq's KRI + Kurdish-flagged Turkey, Iran, Syria provinces); Turkey 65; Syria 13; Jordan 12; Lebanon 9; Palestine 21 (Palestinian Territories plus all former Israel except Jerusalem); Jerusalem (Neutral City) 2; Iraq 15; Kingdom of Nejd and Hejaz 23 (Saudi Arabia + Kuwait + Bahrain); Qatar 7; Oman 11; United Arab Emirates 7; North Yemen 13; South Yemen 6 (includes the Socotra archipelago, which NE carries inside the Hadramawt polygon); Dhale (Disputed Territory) 1; Persia 26 (Iran, with Ilam); Khuzestan (Unstable Territory) 1; Afghanistan 33 (without Nimruz); Balochistan 3 (Iran's Sistan and Baluchestan + Pakistan's Baluchistan province + Afghanistan's Nimruz).
South Caucasus: Georgia 11; Abkhazia (contested) 1; Azerbaijan 14 (14 economic regions dissolved from 78 NE rayons); Armenia 11.

`kind`: `nation` for most; `autonomous zone` (Karakalpakstan), `neutral zone` (Jerusalem), `disputed` (Fergana Valley, Dhale, Khuzestan, Abkhazia). `group`/`group_role` are empty: the data defines no unions or blocs. `native` is empty (the data documents no native names). `color` = the composite's region color (hex from the scripts' REGIONS tables). Capitals = the national-capital markers the composite draws (CAPS dict); Palestine's marker is Ramallah, Kurdistan's is Erbil, Kingdom of Nejd and Hejaz's is Riyadh. No capital is drawn for Karakalpakstan, Fergana, South Yemen, Dhale, Khuzestan, Balochistan, Abkhazia (left empty, not invented).

## Verification
Rendered `preview.png` and compared it nation by nation with `west-asia-composite-map.png`: every region's shape and colors match, East Thrace is absent, Istanbul remains. Computed: geometries valid, no overlaps above 1e-4 sq deg between rows, longitudes inside -180..180 (min 25.7, max 87.3). Jerusalem was cut out of Palestine where the Israel/West Bank units overlapped it (Jerusalem wins).

## Caveats and gaps
- **South Ossetia (contested) is a legend entry with no geometry**: Natural Earth has no admin-1 polygon for it, so the source map does not draw it either. It is missing from `nations.gpkg`; its area is most likely already inside the Georgia polygon (NE Shida Kartli; the Tskhinvali unit was unmatched, not checked). The author must decide whether to supply a polygon.
- Unmatched units in the source (computed): Yemen/Socotra (covered inside Hadramawt, so South Yemen has the island), Qatar/Al Sheehaniya (folded into a parent unit), Georgia/South Ossetia. Kazakhstan has 16 NE units against the data's 21 (Abai, Jetisu, Ulytau, Shymkent and Baikonur are not separate in NE; Baikonur is unioned into Kyzylorda); the land is complete.
- Admin-1 geometry is 1:10m generalized; small slivers or gaps at coasts and between units are possible. No Caspian or Persian Gulf water is drawn.
- Borders of the data follow present-day provinces; the author's scenario regions (Kurdistan, Balochistan, Nejd and Hejaz, Palestine) are provisional per the source ("For consideration only").

## Seams with other regions
- **Europe**: East Thrace (Edirne, Kirklareli, Tekirdag) is excluded; Europe must supply Greece's and Bulgaria's extension to the Turkish border. Cyprus and Northern Cyprus are not here (Europe's). Turkey's other European-side land is only Istanbul Province.
- **Russia**: the Kazakhstan/Russia border and the Caucasus (Georgia, Abkhazia, Azerbaijan northern border with Dagestan) meet Russia's data; no overlap here, gaps possible from different geometry vintages.
- **South Asia**: Pakistan is out of this region except its Baluchistan province, which is part of Balochistan here; South Asia's package must exclude that province (or the merge must take this one). Afghanistan is drawn here (33 units, Nimruz excluded), so South Asia's package might also define Afghanistan; treat this one as authoritative unless South Asia includes it, then drop it from one side and keep Nimruz in Balochistan. Check the Kashmir/Gilgit and Wakhan boundaries against South Asia.
- **East Asia**: Kazakhstan, Kyrgyzstan, Tajikistan and Afghanistan border China (Xinjiang is drawn gray out of scope in the source).
- **Africa**: Egypt, Sinai and Sudan/Eritrea/Djibouti/Somalia are not here (Africa's). Sinai borders Palestine (former Israel/Gaza) and the Kingdom of Nejd and Hejaz (Tiran/Aqaba); the Gulf of Aqaba seam was not checked. Socotra's Somali-side islands are Africa's.
