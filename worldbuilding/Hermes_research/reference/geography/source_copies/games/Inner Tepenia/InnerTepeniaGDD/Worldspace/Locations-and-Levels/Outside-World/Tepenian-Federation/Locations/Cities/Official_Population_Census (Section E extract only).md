# Official Population Census: Section E (extract)

Extracted 2026-11-12 from the original at the path below (Section E only: the census names of each old country's successor states). Read-only copy.

## Section E — Successor-country names in the per-nation tables (added 2026-11-02, `DR-85`)

*The per-nation tables in the Specs files and the national totals above write every country in its latest-period form (the world atlas's latest period). A country that split is written as its successor states, each taking its share of the old country's people (headcount; the pools already carry the income adjustment). A country that was renamed is written under its new name. Rows under 0.10% of a city are listed individually in the Specs files.*

| Old name or place | Rows that carry its people now |
|---|---|
| China | East Turkestan, Manchuria, Mongolia, Sinian Federation, Tibet |
| Hong Kong | Sinian Federation |
| Macau | Sinian Federation |
| Mongolia | Mongolia |
| Taiwan | Taiwan |
| South Korea | Korea |
| North Korea | Korea |
| Jeju-do | Korea |
| USA | Alaska, Appalachia, CSA, Cascadia, Colorado, Hawaii, Midwest Republic, New England, Sonora |
| Canada | Alaska, Cascadia, Demilitarized Zone (s. Ontario; not a nation), Prairie Federation, Quebec |
| Mexico | Cascadia, México, Sonora, Yucatán |
| Petén | Yucatán |
| Russia | Chechnya, Dagestan, Donska-Kubania, Finland, Idelsk-Uralia, Ingushetia, Kabardino-Balkaria, Karachay-Cherkessia, Künnarantaiga, North Ossetia-Alania, Russia (core state), Siberia, Tuva |
| Ukraine | Russia (core state) |
| Argentina | Araucanía-Patagonia, Argentina (without Patagonia) |
| Chile | Araucanía-Patagonia |
| Italy | Magna Lombardia, Meridia, Sicilia (autonomous zone within Meridia) |
| Germany | Austro-Bavaria, Germany |
| Austria | Austro-Bavaria |
| Belgium | France, Netherlands |
| Luxembourg | France |
| UK | Northern Ireland, United Kingdom |
| Spain | Basque Country, Catalonia |
| Brazil | Amazonia |
| Indonesia | Aceh, West Papua |
| Thailand | Patani |
| Romania | Hungary |
| Kosovo | Serbia |
| Czech Republic | Czechia |
| Kazakhstan | Kazakhstan |

**Notes on specific rows:**
- **Sinian Federation:** China's nine Han states, with Hong Kong and Macau; it is the same row the old "China" held, in the cities that listed one. Manchuria, Mongolia (with Inner Mongolia), East Turkestan and Tibet are placed only in the cities inside their time-zone windows; elsewhere their share stays with the Sinian Federation. Manchuria's share was then reduced the same way the Sinian Federation's was (a draw from 0.55 to 0.65 in each of its 15 cities, `DR-94`); Mongolia, East Turkestan, Tibet and Taiwan were not reduced. Taiwan is a separate nation.
- **Korea:** South Korea and North Korea. Jeju-do is the International Court of Diplomacy's neutral ground and nobody comes from it (developer, 2026-11-02): its people count as Korea's.
- **Demilitarized Zone (s. Ontario; not a nation):** Canada's former southern-Ontario territory. Its treatment is **still open** (developer, 2026-11-02: to be decided).
- **Sicilia (autonomous zone within Meridia):** listed on its own as the atlas lists it.
- **Kazakhstan** (added 2026-11-02, `DR-93`): a nation never counted before; its pool (4.13 million, estimated from Romania, Serbia and Russia on income and inequality) is placed at 1.45% in the 13 cities within three zones of UTC+5, and it is a founder at Temirötkel and Mawson (boosted there).
- **Neutral Scientific Territory:** no one is from it, so it has no row (developer, 2026-11-01).
- **Kunlun's heritage rows** (given today's names 2026-11-02, `DR-94`; shares and counts unchanged): USA is CSA, Russia is Russia (core state), Canada is Quebec, UK is the United Kingdom, South Korea is Korea, Argentina is Argentina (without Patagonia), Italy is split equally between Meridia and Magna Lombardia, and Germany is split 70% Germany and 30% Austro-Bavaria. The rows follow space-program heritage and not headcount: the Italian space agency is in Rome (Meridia) and its industry in Turin and Milan (Magna Lombardia); Germany's astronaut corps, agency headquarters and module builders are in Cologne and Bremen, while Bavaria holds the mission-control center at Oberpfaffenhofen, the European Southern Observatory's headquarters at Garching and Airbus's satellite works at Ottobrunn (about 30% of German aerospace employment), and Austria adds its space-instrument institute at Graz. Intermarium/Intermaria is unchanged.
- **Where the numbers come from:** `Sinian_Federation_Split_Scratch_2026-11-01/` (file `12_Rebalance_Run4.md`, the research in `Run4_Research/`, and `apply_final.py` for the last changes).
