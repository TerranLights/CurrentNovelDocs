# East Asia (region key `east-asia`) - final-state nation polygons

Deliverable: `nations.gpkg` with two layers, `nations` (9 rows) and `subdivisions` (the nine Han states, 9 rows). Rebuild with `build_east-asia.py` (reads the source zip and `/tmp/ne_test` read-only); `make_preview.py` renders `preview.png`.

## What was used
- Source folder `x Full Earth/Asia/Asia (East)/`: `README.md`, `Native_Names.md`, `Timeline_Reasoning.md`, and `asia-east-current.zip` (read in place by the build script; holds `ea_series.py`, `data/polities.csv`, `data/province_assignments.csv`, `data/native_labels.csv`). [read]
- Which unit belongs to which nation: the region's own `owner_map_f` column in `province_assignments.csv` (the renderer writes it; not re-derived). Unit geometry: Natural Earth 10m admin-0/admin-1 geojson in `/tmp/ne_test/` with the same keys `ea_series.py` uses (`a1:China:<name>`, `a0:<ADMIN>`, `South Korea MINUS Jeju`). [computed]
- Colors: `color_hex` in `polities.csv` (the same fills `ea_series.py` draws). Native names: `native_labels.csv` / `Native_Names.md`. No capitals are defined in the source, so `capital*` columns are empty.

## Final state chosen
**Map F, 2267 to present** (the last of the six maps, A to F, in the README timeline; `maps.csv` lists nine sovereign ids for F: SIN, MAN, MON, ETK, TIB, TWN, KOR, JPN, JEJ). Eight sovereign powers plus the neutral Jeju-do. No competing later dated source exists in the folder.

## Nations (units = Natural Earth units dissolved)
| nation | native | kind | units | color |
|---|---|---|---|---|
| Sinian Federation | 震旦联邦 | nation | 27 | #3FA9C9 |
| Manchuria | 满洲 | nation | 3 (Liaoning, Jilin, Heilongjiang) | #4C9A5A |
| Mongolia | Монгол Улс | nation | 2 (Mongolia + Inner Mongol) | #E8963C |
| East Turkestan | شەرقىي تۈركىستان | nation | 1 (Xinjiang) | #A8C84A |
| Tibet | བོད | nation | 1 (Xizang) | #E8A0C4 |
| Taiwan | 臺灣 | nation | 1 | #3E9E9E |
| Korea | 한국 | nation | 2 (North Korea + South Korea minus Jeju) | #8E6FB8 |
| Japan | 日本 | nation | 1 | #D4527D |
| Jeju-do | 제주도 | neutral zone | 1 | #F5C518 |

Sinian Federation units: 25 provinces/municipalities + Hong Kong + Macau (Hainan sits in Min; Qinghai in Qin). Subdivision layer (`parent`, `name`, `native`, `units`, plus `unit_names`, `color`, `group` = `Sinian Federation`, `group_role` = `member`): Zhongyuan 中原 (5), Qin 秦 (4, with Qinghai), Bashu 巴蜀 (5), Jin 晋 (1), Wu 吴 (4), Gan 赣 (1), Xiang 湘 (1), Min 闽 (2, with Hainan), Yue 粤 (4, with Hong Kong and Macau). Their union equals the Federation row exactly (27 units). Hakka (non-territorial, no ground) is deliberately not a row.

## Verification
- All geometries valid, EPSG:4326, longitudes 73.6 to 154.0 (nothing crosses the antimeridian). No overlaps between rows (computed, 0 area); no interior holes; the only gaps between rows are coastal inlets. [computed]
- `preview.png` compared with `asia-east-F-post-court.png`: shapes and unit membership match nation by nation (Manchuria/Mongolia boundary along the Inner Mongolia line, Qinghai in the Federation, Tibet = Xizang only, Hainan, Hong Kong, Taiwan, Korea with Jeju cut out, whole Japanese chain). No mismatches found. Native text is not drawn on the preview (no CJK font in the atlas fonts folder).

## Seams and neighbors (nothing from these is included)
- Russia package: Outer Manchuria (Primorye, Khabarovsk, Amur, Jewish AO), Sakhalin, the Kurils, Buryatia, Tuva. The source draws these white ("unclaimed seams"); this layer leaves them empty, so the Russia region must supply them. Source open question Q7: Khabarovsk is drawn whole although it runs to about 62.6 N.
- West Asia: Central Asia and Afghanistan border East Turkestan, Mongolia's west and Tibet/Xinjiang; out of scope here.
- South Asia / Southeast Asia: Xizang and Xinjiang borders follow Natural Earth's China-side admin-1 outlines (including whatever disputed ground NE assigns to them, such as Aksai Chin in the Xinjiang/Xizang units); the neighbor regions' India, Bhutan, Nepal, Myanmar, Laos and Vietnam borders may therefore show small overlaps or gaps at the merge. The Paracel Islands (an admin-1 unit of China in NE) and the Spratly Islands are not assigned by the region's data and are excluded; Southeast Asia should decide them.
- Natural Earth admin-0 Mongolia/North Korea/South Korea/Japan/Taiwan versus admin-1 China outlines can differ by a few hundred meters along shared borders; measured overlap in this region is zero and no land gaps were found.

## Notes and caveats
- Names follow the map F legend: `Sinian Federation` (legend writes "The Sinian Federation", the atlas spec writes `Sinian Federation`), `Jeju-do` (map label JEJU-DO; Native_Names writes Jeju-do). `Korea` is the unified nation. Pre-unification North/South Korea are not separate rows.
- Jeju-do kind is `neutral zone` (the source calls it a condominium / "not a nation"); `group` is empty because the three powers share it rather than it being a member of any bloc.
- Included as the data assigns them: Hainan, Hong Kong, Macau, Taiwan with Penghu/Kinmen/Matsu (NE admin-0 Taiwan), Dokdo (inside NE South Korea, so it sits in Korea), the Ryukyus including Okinawa (inside NE Japan).
- Source data quirk (open question Q4): Wu and Korea share the hex #8E6FB8. The Han states are not drawn in the source's F map (one Federation color), and the main layer uses #3FA9C9 for the Federation, so this causes no clash in the nations layer; it only matters if the subdivision colors are drawn next to Korea.
- Open author decisions inherited from the source: Q9/Q10 are cosmetic; none changes the polygons.
- Natural Earth geometry vintage is whatever is in `/tmp/ne_test/` (not independently dated). All figures above are computed unless marked.
