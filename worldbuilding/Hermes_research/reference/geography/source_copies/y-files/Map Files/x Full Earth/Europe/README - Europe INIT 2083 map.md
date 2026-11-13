# Europe INIT 2083: the starting map

**Made 2026-09-30.** One map of Europe at the outset of 2083 with every land separated into its own nation, in the style of East Asia's first map (`Asia (East)/04 timeline staging/Asia_East/asia-east-A-fragmented.png`): a title box, a right-hand legend grouped by region (a color swatch, the nation's name and its native name where it uses another script), and special areas marked in the legend.

**Output:** `europe-init-2083.png` (3640 × 1885). **Script:** `render_europe_init.py` (reads only `./data/`). **Inputs copied into `data/`:** `europe-base.gpkg`, `fonts/`, the Natural Earth subsets for Russia, Italy, Iberia, the British Isles and the Nordic countries, `eastern-ukraine-east-side.geojson`, `moldova-geoboundaries-adm1.geojson`, `russia-subdivisions-round2.csv`. The working files (decision log, open-questions note, earlier maps, research) are in `archive 01/`, which is the source of truth for every decision below.

## The 59 nations on the map
- **The Nordic countries (6):** Norway, Sweden, Finland (with Åland), Denmark, Iceland, the Faroe Islands. Greenland (honorary) is in the legend but lies off the map.
- **The British Isles (4):** the United Kingdom (England, Scotland, Wales, with Gibraltar and the Cyprus base areas), Northern Ireland, Ireland, the Crown Dependencies.
- **The West and the Alps (7):** France (with Wallonia, Brussels and Luxembourg), the Netherlands (with Flanders), Germany (without Bavaria), Austro-Bavaria (Bavaria and Austria), Switzerland, Liechtenstein, Monaco.
- **Iberia (5):** Spain (without Catalonia and the Basque country), Catalonia, the Basque Country (Biscay, Gipuzkoa, Álava, Navarre, plus the Treviño and Villaverde enclaves), Portugal, Andorra.
- **Italy and Malta (5):** Magna Lombardia, Meridia (Sicilia is an Autonomous Zone), San Marino, Vatican City, Malta.
- **The Confederacy of Intermarium Nations (21):** Poland, Lithuania, Kaliningrad, Latvia, Estonia, Belarus, Ukraine (without the eastern slice), Czechia, Slovakia, Hungary (with five Romanian counties), Romania, Moldova (Transnistria disputed), Bulgaria (with Kırklareli), Slovenia, Croatia, Serbia (with Kosovo), Montenegro, Bosnia and Herzegovina, Skoprodija, Albania (with the Albanian belt), Greece (with Edirne and Tekirdağ). The map shows them as separate nations at the start; their later accession order is on `archive 01/confederacy-accession-order.png`.
- **The East (10):** Russia (core, with the eastern-Ukraine slice), Idelsk-Uralia, Donska-Kubania (Crimea an Autonomous Zone), Karelia (with Murmansk, as the proto-country), and the North Caucasus republics Chechnya, Dagestan, Ingushetia, Kabardino-Balkaria, Karachay-Cherkessia, North Ossetia-Alania.
- **The Mediterranean (1):** Cyprus (the Green Line dashed).

## Drawn as at the start (the INIT state)
Karelia and Murmansk are still the proto-country, **not yet part of Finland**; Murmansk later joins Idelsk-Uralia. Brussels (a French exclave with a corridor and a French/Dutch split under review) and the German-speaking Community are drawn as French by default. Switzerland and the small states are as today (changes deferred to later timeline stages).

## Not on this map
Siberia and the Far East (beyond the frame), Turkey, the Caucasus, North Africa, Central Asia and the Middle East (gray, "out of scope", see their own maps), Greenland and Svalbard (off the frame), the Canary Islands, Madeira and the Azores. Colors are assigned by a script so that neighbors differ; the Russian nations keep the colors from the Russia maps.

## The series after INIT (made 2026-09-30; script `render_europe_series.py`, which imports `render_europe_init.py`)
Each map repeats the INIT frame and style, with a "Map" tag at the top right (as East Asia's Map A to Map F) and a gold outline on the nations that change on that map. **No years are implied.**

| Map | File | What changes |
|---|---|---|
| INIT | `europe-init-2083.png` | The starting map: every land its own nation; the Nordic countries are not yet in a union |
| B | `europe-B-scandinavian-trade-union.png` | The Scandinavian Trade Union forms: Finland (with Åland), Sweden, Denmark, Norway, the Faroes and Iceland share one color; borders between them are dotted red (expedited crossings); Greenland honorary |
| C-00 | `europe-C-00-core-poland.png` | Poland as the core of the Confederacy; Albania barred (black cross-hatch) from here on |
| C-01 | `europe-C-01-wave-01-lithuania-kaliningrad.png` | Lithuania and Kaliningrad join |
| C-02 | `europe-C-02-wave-02-czechia-slovakia.png` | Czechia and Slovakia |
| C-03, C-04 | `...wave-03-latvia.png`, `...wave-04-estonia.png` | Latvia, then Estonia |
| C-05 | `...wave-05-belarus.png` | Belarus, restricted (hatched: closer to an observer) |
| C-06 | `...wave-06-ukraine.png` | Ukraine |
| C-07 to C-09 | `...wave-07-hungary.png`, `...wave-08-romania.png`, `...wave-09-moldova.png` | Hungary, Romania, Moldova |
| C-10 | `...wave-10-bulgaria.png` | Bulgaria |
| C-11 | `...wave-11-croatia-slovenia.png` | Croatia and Slovenia (voting) |
| C-12, C-13 | `...wave-12-serbia.png`, `...wave-13-montenegro-bosnia.png` | Serbia; then Montenegro, with Bosnia and Herzegovina an observer (hatched; timing open) |
| C-14, C-15 | `...wave-14-greece.png`, `...wave-15-skoprodija.png` | Greece; then Skoprodija, last, beginning as an observer. **C-15 also shows Karelia (the Republic) as part of Finland and Murmansk Oblast as part of Idelsk-Uralia** (author, 2026-09-30: "by the very end ... Karelia is definitely part of Finland"); Map B and C-00 to C-14 still show Karelia (with Murmansk) as the proto-country |

**Rules used.** The Confederacy is a confederation, not a unification: members stay separate countries, drawn in one crimson color with dashed gold lines between them; observers are a lighter crimson with hatching; Albania is blocked throughout. The order is the author's (2026-09-30), from `archive 01/DECISION LOG - Confederacy of Intermarium Nations (membership order).md`. The Scandinavian Trade Union persists on every C map. **Open:** *when* Karelia becomes part of Finland and Murmansk part of Idelsk-Uralia (the author will decide which map shows the change; until then it appears only on C-15). **Not built yet:** other later-stage maps ( any change to Switzerland and the small states; the UK/Ireland and Brussels details), and any maps for the Russian, West Asian or other regions' own progressions.
