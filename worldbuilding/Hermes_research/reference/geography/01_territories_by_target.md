STATUS: draft v1 (2026-11-12). Compiled by Claude from the source copies in `source_copies/`. For Hermes to read.

# Territories by target: which real-world places each post-war nation consists of

**What this is.** For each post-war nation (a target on `DCI countries _ cultures checklist [Hermes].md`), the pre-war first-order subdivisions (states, provinces, regions, oblasts, prefectures and so on) it consists of, what the old countries lost and to whom, and where the sources are unsure. The post-war world is not the pre-war one: for example, Baja California and Baja California Sur are part of Cascadia, and Sonora and Chihuahua are part of La República de Sonora. **Research a nation's culture by the places listed here, not by the old country.**

**How to use it.**
1. Find the target in the contents below. Read its entry: **Consists of**, **Left out**, **Notes**, **Confidence**.
2. Research the places listed. Where an entry says a subdivision is only *part* of a nation, research only that part, and say so.
3. If an entry says a source is silent, or the confidence is low, write that in your file's *Open threads*. Do not fill a gap yourself.
4. The original files are in `source_copies/`, with `00_README.md` listing where each came from. If this table and a source copy disagree, the source copy is nearer the source; write both and write `NEEDS CLAUDE:` at the top.

**Greenland** is one of New North America's twelve regions and is relevant, though it has no Census I exiles.

**This table is a snapshot of 2026-11-12.** The map work continues; some items are open (listed at the end of each part). Claude refreshes the copies when the source changes.

## Contents
- Part 1: North America and Latin America (Alaska, Cascadia, Colorado, Sonora, Prairie Federation, Midwest Republic, New England, Appalachia, CSA, Quebec, DMZ, Greenland, Hawaii, México, Yucatán, Brazil, Amazonia, Argentina, Araucanía-Patagonia, Chile, Uruguay)
- Part 2: Europe and South Africa (31 European targets, plus the rest of the Europe map)
- Part 3: Russia, East Asia, Southeast Asia, Central Asia and Oceania

---


# Part 1: North America and Latin America

## Territory table: North America and Latin America (post-war nations)

Compiled 2026-11-12 from the project files. Read-only research; no repo file was edited.

## Sources used (and which is authoritative)

Abbreviations used in each nation's Source line:

- **NA-CSV** = `y-files/Map Files/x Full Earth/North America/north-america-nations/reference/nations-assignment.csv` (72 rows, rendered 2026-09-26, eighth round). Authoritative for North America. It is the output of `na_nations.py`; the atlas build (`z-full-world-atlas/data/regions/north-america/README.md`) confirms it is the final state and that the loose folder, `files.zip` and the Hawaii zip are byte-identical.
- **NA-README** = `.../North America/north-america-nations/README.md` (nations table, the three exceptions, decisions) and **NA-CHANGES** = `.../North America/CHANGES.md` (seventh and eighth rounds, Hawaii).
- **LA-CSV** = `y-files/Map Files/x Full Earth/Latin America/nations-assignment.csv` (top-level, written 2026-09-28; 394 rows). Authoritative for Latin America; `nations.py` beside it (tables `N`, `DEFAULT`, `EXCEPT`, `BRAZIL`) agrees with it. The `archive NN` folders and `latin-america-nations/` are older (assignments identical; only names and labels differ, per the atlas README).
- **LA-ATLAS** = `z-full-world-atlas/data/regions/latin-america/README.md` (2026-10-04, verified 394 of 394 rows).
- **TD** = `worldbuilding/nations/New North America - Territory Definitions (read from map).md` (2026-09-22/23; an early reading of the hand-drawn map; superseded where it differs from NA-CSV).
- **MEX** = `worldbuilding/nations/México (post-war) - Territory and Open Research.md` (2026-09-25, "settled").
- **ROSTER** = `worldbuilding/nations/World-Nations-Roster.md` (as synced 2026-09-28).
- **HAW** = `worldbuilding/nations/Sovereign Republic of Hawaii - National Character Profile.md` (2026-09-26).
- **SCOPE** = `worldbuilding/Deep_Culture_Investigation/Targets/Cascadia/00 - Scope.md` (2026-11-02) and `Deep_Culture_Investigation/Data/Unit_Territories.md` (2026-11-03).
- **CENSUS-E** = Inner Tepenia GDD `.../Cities/Official_Population_Census.md`, Section E, "Successor-country names" (2026-11-02). This is the source of the census names and of which old countries "carry" which nations.

Rule applied: later-dated and more specific source wins. NA-CSV (09-26) and LA-CSV (09-28) outrank TD (09-22) and the older Latin America survey files. Disagreements are listed under each nation and again at the end.

Census-name convention: the census writes "Argentina (without Patagonia)", "Araucanía-Patagonia", "Yucatán", "México", "Sonora", "Hawaii", "CSA", "Demilitarized Zone (s. Ontario; not a nation)". The formal names below come from NA-CSV and LA-CSV.

---

## North America

### Alaska (census: Alaska; formal: Republic of Alaska; capital Whitehorse)
- **Consists of:**
  - United States: Alaska (part: north and west of the Jetté-Cook line, i.e., all of Alaska except the Panhandle)
  - Canada: Yukon (whole); Northwest Territories and Nunavut (part: the mainland and most islands, after the Queen Elizabeth Islands and Baffin cuts below)
- **Left out / lost by old countries:** United States: the Alaska Panhandle (south and east of the Jetté-Cook line) went to Cascadia. Canada: Nunavut/NWT islands north of 74.7N (Queen Elizabeth Islands) went to Greenland; Baffin Island and satellites (east of 82W, north of 61.5N) are the Neutral Scientific Territory.
- **Notes:** The Arctic archipelago is split island by island by each island's representative point (NA-README exception 1). The atlas build keeps the Aleutians west of the antimeridian as Alaska (LA/NA atlas README caveat 1). Where the Jetté-Cook line meets the sea near Yakutat Bay is an open author question (NA-README, "Open question"): as rendered, the strip between 139.98W and Yakutat Bay goes to Cascadia.
- **Source:** NA-CSV rows ALA (3 rows); NA-README nations table and exception 1 and 3; TD "Twelve Regions" table (older wording: "Alaska minus the Panhandle, plus Yukon, NWT, Nunavut, and the Arctic Archipelago").
- **Confidence:** high (whole-subdivision list is explicit; the island split rule is stated with coordinates).

### Cascadia (census: Cascadia; formal: The People's Democratic Republic of Cascadia; earlier the Republic of Cascadia)
- **Consists of:**
  - United States: Washington, Oregon, California (all whole); Alaska (part: the Panhandle, south and east of the Jetté-Cook line)
  - Canada: British Columbia (whole)
  - Mexico: Baja California, Baja California Sur (whole)
- **Left out / lost by old countries:** United States lost WA, OR, CA and the Panhandle to Cascadia; Canada lost British Columbia; Mexico lost both Bajas. Sonora (the Mexican state) and the rest of Mexico did not go to Cascadia.
- **Notes:** Washington and Oregon are wholly Cascadian (the earlier hand-drawn split along the Cascades was removed, settled 2026-09-23). California is the whole state by the whole-subdivision rule (TD flags that the map alone cannot settle it; SCOPE decision 13 uses the whole state). The Panhandle has two statements: NA-CSV and NA-README define it by the Jetté-Cook geometric cut (about 85,000 km2, Yakutat to Ketchikan); SCOPE and Unit_Territories (2026-11-02/03) list ten boroughs and census areas: Haines, Hoonah-Angoon, Juneau, Ketchikan Gateway, Petersburg, Prince of Wales-Hyder, Sitka, Skagway, Wrangell, Yakutat (Yakutat inside, decision 12). The two are consistent in spirit; the borough list is the later statement.
- **Source:** NA-CSV rows CAS (7 rows); NA-README exception 3; TD ("Settled 2026-09-23" and Finding 1); MEX section 1 (Bajas); SCOPE section 1 territory table; Unit_Territories.
- **Confidence:** high for the seven-unit membership; medium for the exact Panhandle limit (two formulations, Yakutat strip flagged open).

### Colorado (census: Colorado; formal: Colorado Republic)
- **Consists of:** United States: Colorado, Idaho, Montana, Nevada, Utah, Wyoming (all whole).
- **Left out / lost by old countries:** Only the United States lost territory to it. Washington and Oregon (interior halves were once drawn here on the hand-drawn map) stay wholly Cascadia.
- **Notes:** None beyond the Washington/Oregon ruling.
- **Source:** NA-CSV rows COL (6 rows); NA-README; TD.
- **Confidence:** high.

### Sonora (census: Sonora; formal: La República de Sonora; capital Tucson)
- **Consists of:**
  - United States: Arizona, New Mexico (whole)
  - Mexico: Sonora, Chihuahua (whole)
- **Left out / lost by old countries:** The United States lost AZ and NM; Mexico lost Sonora and Chihuahua. Coahuila, Nuevo León and Tamaulipas are not Sonora (an interim version wrongly included them; corrected 2026-09-23) and stay with México.
- **Notes:** None beyond the correction.
- **Source:** NA-CSV rows SON (4 rows); NA-README "Decisions made along the way"; TD correction 2026-09-23; MEX section 1; Sonora National Character Profile territory line (confirms four states).
- **Confidence:** high.

### Prairie Federation (census: Prairie Federation; formal: The Prairie Federation)
- **Consists of:** Canada: Alberta, Saskatchewan, Manitoba (whole); Ontario (part: north of the DMZ line, including Manitoulin Island and Fitzwilliam Island).
- **Left out / lost by old countries:** Only Canada lost territory to it. Southern Ontario (south of the line) is the DMZ, not Prairie.
- **Notes:** The DMZ line follows the Mattawa River mouth (46.320N, 78.707W), west just north of North Bay, across Lake Nipissing, down the French River to its mouth (45.941N, 80.902W), then south through open water past Manitoulin's southern shore and western end into Lake Huron. Manitoulin stays Prairie (settled 2026-09-25). Prairie Federation is one of four nations sharing the Neutral Scientific Territory (Baffin) as a research partner; it holds none of it.
- **Source:** NA-CSV rows PRA (4 rows); NA-README exception 2 and "Settled: Manitoulin Island". TD says only "western Ontario" and is superseded.
- **Confidence:** high (coordinates stated).

### Midwest Republic (census: Midwest Republic; formal: The Midwest Republic, colloquially "Midwestland")
- **Consists of:** United States: Iowa, Kansas, Minnesota, Missouri, Nebraska, North Dakota, South Dakota (all whole).
- **Left out / lost by old countries:** Only the United States lost territory to it. Illinois (Chicago) is Appalachia, not Midwestland (TD Finding 3).
- **Notes:** None.
- **Source:** NA-CSV rows MID (7 rows); NA-README; TD.
- **Confidence:** high.

### New England (census: New England; formal: People's Democratic Republic of New England per ROSTER; the CSV legend name is "New England")
- **Consists of:** United States: Connecticut, Maine, Massachusetts, New Hampshire, New Jersey, New York, Pennsylvania, Rhode Island, Vermont (all whole).
- **Left out / lost by old countries:** Only the United States lost territory to it. Delaware and Maryland went to Appalachia.
- **Notes:** The formal "People's Democratic Republic" name appears only in ROSTER; NA-CSV and NA-README use "New England".
- **Source:** NA-CSV rows NEN (9 rows); NA-README; TD; ROSTER (formal name).
- **Confidence:** high for territory; medium for the formal name (one source).

### Appalachia (census: Appalachia; formal: Appalachia Republic; capital Cincinnati)
- **Consists of:** United States: Delaware, District of Columbia, Illinois, Indiana, Kentucky, Maryland, Michigan, Ohio, Virginia, West Virginia, Wisconsin (all whole; 10 states plus D.C.).
- **Left out / lost by old countries:** Only the United States lost territory to it. Tennessee went to the CSA.
- **Notes:** Source disagreement: TD (2026-09-22) lists Tennessee under Appalachia and describes "Maryland/Delaware area"; NA-CSV (2026-09-26), NA-README and the atlas build put Tennessee in the CSA and list Delaware, D.C. and Maryland explicitly. NA-CSV used. TD itself flagged the Maryland/Delaware/D.C. corner as ambiguous.
- **Source:** NA-CSV rows APP (11 rows); NA-README; TD (older, disagrees on Tennessee).
- **Confidence:** high for the 11 units; the Tennessee disagreement is resolved in favor of the later source.

### CSA (census: CSA; formal: The CSA)
- **Consists of:** United States: Alabama, Arkansas, Florida, Georgia, Louisiana, Mississippi, North Carolina, Oklahoma, South Carolina, Tennessee, Texas (all whole).
- **Left out / lost by old countries:** Only the United States lost territory to it. No Mexican state: Coahuila, Nuevo León and Tamaulipas stay with México, so the CSA's southern border faces Sonora (Chihuahua) on the upper Rio Grande and México below it.
- **Notes:** National capital Houston (author, 2026-10-12); Texas state capital stays Austin.
- **Source:** NA-CSV rows CSA (11 rows); NA-README; TD Finding 5 (Texas wholly CSA; its "unclaimed" Mexican border is superseded by MEX).
- **Confidence:** high.

### Quebec (census: Quebec; formal: Quebec)
- **Consists of:** Canada: Québec, Newfoundland and Labrador, New Brunswick, Nova Scotia, Prince Edward Island (all whole).
- **Left out / lost by old countries:** Only Canada lost territory to it. Ontario's east (Ottawa Valley, Ottawa) is the DMZ, not Quebec. Saint-Pierre and Miquelon (France) is drawn as plain gray land and assigned to no nation.
- **Notes:** Quebec is one of four nations sharing the Neutral Scientific Territory as research partner; it holds none of it. TD says "Quebec and the Atlantic provinces; eastern Ontario"; the eastern Ontario part is superseded by the DMZ cut.
- **Source:** NA-CSV rows QUE (5 rows); NA-README; atlas NA README caveat 5 (Saint-Pierre and Miquelon).
- **Confidence:** high.

### Demilitarized Zone (census: Demilitarized Zone (s. Ontario; not a nation))
- **Consists of:** Canada: Ontario (part: everything south of the DMZ line described under the Prairie Federation: the Ottawa Valley and Ottawa, the Windsor tip, the whole Bruce Peninsula down to Cove Island off Tobermory, and the rest of southern Ontario).
- **Left out / lost by old countries:** Canada lost this part of Ontario to the DMZ. Northern Ontario, including Manitoulin and Fitzwilliam Islands, went to the Prairie Federation.
- **Notes:** Not a nation, drawn hatched red. CENSUS-E (2026-11-02) says its treatment is "still open (developer: to be decided)". It carries the people counted as Canadians from southern Ontario.
- **Source:** NA-CSV row DMZ; NA-README exception 2 and "Fixes made while packaging" 1; CENSUS-E notes.
- **Confidence:** high for the territory; the status is open by the author's own note.

### Greenland (a New North America region; not in the census list)
- **Consists of:**
  - Greenland (the old territory of that name): the whole island
  - Canada: Nunavut and Northwest Territories (part: the Queen Elizabeth Islands, islands centered north of 74.7N)
- **Left out / lost by old countries:** Canada lost the Queen Elizabeth Islands to Greenland. Greenland's pre-war sovereign (Denmark) is not named in the sources; the CSV lists the country as "Greenland".
- **Notes:** Capital Nuuk (settled 2026-09-26). TD says "Greenland, plus some of the high Arctic islands". No census row ("no one is from it" is stated only for the Neutral Scientific Territory; Greenland simply does not appear in CENSUS-E).
- **Source:** NA-CSV rows GRE (2 rows); NA-README nations table and exception 1; atlas NA README (Greenland polygon = admin-0 outline plus QEI).
- **Confidence:** high.

### Neutral Scientific Territory (not a nation; listed for completeness)
- **Consists of:** Canada: Nunavut and Northwest Territories (part: Baffin Island and its satellites, east of 82W and north of 61.5N).
- **Notes:** Held open for shared research among Alaska, Greenland, the Prairie Federation and Quebec (author, 2026-09-25). Not in CENSUS-E (no people come from it).
- **Source:** NA-CSV unnumbered row; NA-README.
- **Confidence:** high.

### Hawaii (census: Hawaii; formal: The Sovereign Republic of Hawaii)
- **Consists of:** United States: Hawaii (the whole state, including the uninhabited Northwestern Hawaiian Islands chain to Kure Atoll).
- **Left out / lost by old countries:** The United States lost the state of Hawaii. Midway Atoll is outside the Republic (never part of the state; it belongs to Natural Earth's "United States Minor Outlying Islands"); the author has not decided whether it should join (NA-CHANGES eighth round, open question). Other US Minor Outlying Islands (Wake, Johnston, Palmyra and others) are not assigned in these sources.
- **Notes:** Stays part of North America rather than Oceania (author, 2026-09-26). Drawn as a corner-box inset, not in true position. HAW lists the eight main islands as core and says the Northwestern Hawaiian Islands' status as domain is "TBD", while NA-CSV and the map include them; map used.
- **Source:** NA-CSV row HAW; NA-CHANGES (seventh, eighth rounds); NA-README; HAW "Core territory" and "Domain" lines; atlas NA README caveats 6 and 7.
- **Confidence:** high for the main islands and the state boundary; medium for the Northwestern Hawaiian Islands (HAW leaves them TBD) and Midway (open).

---

## Latin America

### México, post-war (census: México; formal: México)
- **Consists of:** Mexico: Aguascalientes, Coahuila, Colima, Distrito Federal (Ciudad de México), Durango, Guanajuato, Guerrero, Hidalgo, Jalisco, México (state), Michoacán, Morelos, Nayarit, Nuevo León, Oaxaca, Puebla, Querétaro, San Luis Potosí, Sinaloa, Tamaulipas, Tlaxcala, Veracruz, Zacatecas (all whole; 23 of 32 entities).
- **Left out / lost by old countries:** Mexico lost Baja California and Baja California Sur to Cascadia; Sonora and Chihuahua to Sonora; Chiapas, Tabasco, Campeche, Yucatán and Quintana Roo to Yucatán.
- **Notes:** "Smaller than the México we know, but the same country, not a rename" (MEX). Coahuila, Nuevo León and Tamaulipas were once unclaimed on the hand-drawn map; MEX (2026-09-25) closed this: all three stay with México. LA-CSV writes the capital entity as "Distrito Federal"; MEX writes "Ciudad de México".
- **Source:** LA-CSV rows MEX (23 rows); MEX section 1; LA-ATLAS (23 units; Sonora, Chihuahua and both Bajas out of scope).
- **Confidence:** high.

### Yucatán (census: Yucatán; formal: La República de Yucatán; English "The Republic of Yucatán"; Maya "U Kuchkabal Mayab")
- **Consists of:**
  - Mexico: Campeche, Chiapas, Quintana Roo, Tabasco, Yucatán (all whole)
  - Guatemala: Petén (whole department)
- **Left out / lost by old countries:** Mexico lost five estados to it; Guatemala lost Petén. Belize stays fully intact, including Corozal and Orange Walk; the eastern border is the Hondo River.
- **Notes:** The 1841-48 Republic of Yucatán held only Yucatán, Campeche and Quintana Roo; Chiapas, Tabasco and Petén join on connectivity grounds. Capital, government and economy not yet worked out (MEX section 3).
- **Source:** LA-CSV rows YUC (6 rows); MEX section 1 and 3; `nations.py` table N.
- **Confidence:** high.

### Brazil (census: Brazil; formal: Brazil)
- **Consists of:** Brazil: Alagoas, Bahia, Ceará, Distrito Federal, Espírito Santo, Goiás, Maranhão, Mato Grosso do Sul, Minas Gerais, Paraná, Paraíba, Pernambuco, Piauí, Rio Grande do Norte, Rio Grande do Sul, Rio de Janeiro, Santa Catarina, Sergipe, São Paulo, Tocantins (all whole; 19 states plus the Distrito Federal).
- **Left out / lost by old countries:** Brazil lost seven whole states to Amazonia: Acre, Amapá, Amazonas, Mato Grosso, Pará, Rondônia, Roraima.
- **Notes:** The final map does not cut Brazil geometrically; Ribeiro's five "Brasis" belong to the earlier culture-region maps. Brazil gains nothing from any neighbor.
- **Source:** LA-CSV rows BRA (20 rows); `nations.py` BRAZIL table; LA-ATLAS "Brazil"; CENSUS-E ("Brazil: Amazonia").
- **Confidence:** high.

### Amazonia (census: Amazonia; capital Manaus)
- **Consists of:**
  - Brazil: Acre, Amapá, Amazonas, Mato Grosso, Pará, Rondônia, Roraima (whole)
  - Bolivia: Pando (whole)
  - Colombia: Amazonas, Guainía, Vaupés (whole)
  - Peru: Loreto (whole)
  - Venezuela: Amazonas, Bolívar (whole)
- **Left out / lost by old countries:** Brazil lost seven states; Bolivia lost Pando only; Colombia lost three departments (it keeps Caquetá, Putumayo, Guaviare, Vichada and Nariño); Peru lost Loreto only (it keeps Ucayali, Madre de Dios and Puno); Venezuela lost Amazonas and Bolívar. Ecuador contributes nothing.
- **Notes:** 14 units, about 5.56 million km2. Walked border by border 2026-09-24 on a road-isolation and connectivity logic; Venezuela's Bolívar (with the Guri Dam) is the one deliberate exception to that logic.
- **Source:** LA-CSV rows AMZ (14 rows, source regions 9 + 15); `nations.py` N and EXCEPT; LA-ATLAS; ROSTER (South America).
- **Confidence:** high.

### Argentina (census: Argentina (without Patagonia); formal: Argentina)
- **Consists of:** Argentina: Buenos Aires, Catamarca, Chaco, Ciudad de Buenos Aires, Corrientes, Córdoba, Entre Ríos, Formosa, Jujuy, La Pampa, La Rioja, Mendoza, Misiones, Salta, San Juan, San Luis, Santa Fe, Santiago del Estero, Tucumán (all whole; 19 of 24 units).
- **Left out / lost by old countries:** Argentina lost Chubut, Neuquén, Río Negro, Santa Cruz and Tierra del Fuego to the Araucanía-Patagonia Autonomous Zone.
- **Notes:** "Survives intact on its pampas core; also keeps Jujuy, Salta, Tucumán, Catamarca, Santiago del Estero and La Rioja" (`nations.py`). La Pampa and Mendoza stay Argentine (not in the list of five provinces going to the Zone). The sources do not address Argentina's South Atlantic island claims or Antarctic claim.
- **Source:** LA-CSV rows ARG (19 rows); `nations.py` N and EXCEPT; CENSUS-E ("Argentina: Araucanía-Patagonia, Argentina (without Patagonia)").
- **Confidence:** high.

### Araucanía-Patagonia (census: Araucanía-Patagonia; formal: Araucanía-Patagonia Autonomous Zone [APAZ]; Spanish: La Zona Autónoma de Patagonia y Araucanía [ZAPA])
- **Consists of:**
  - Argentina: Chubut, Neuquén, Río Negro, Santa Cruz, Tierra del Fuego (whole)
  - Chile: Aisén del General Carlos Ibáñez del Campo, La Araucanía, Los Lagos, Los Ríos, Magallanes y Antártica Chilena (whole regions)
- **Left out / lost by old countries:** Argentina lost five provinces; Chile lost five regions. The rest of both stays with Argentina and Chile.
- **Notes:** A demilitarized joint condominium of Argentina and Chile (named 2026-09-28, author-supplied); takes 1-2 generations after the war to fully form. Mapuche Wallmapu in the north, geographically isolated Patagonia in the south; area about 1.11 million km2. The atlas clips Chile's and Argentina's Antarctic claims at 60 S (Magallanes y Antártica Chilena as a region includes the Chilean Antarctic claim; the Tepenia/Antarctica region covers it).
- **Source:** LA-CSV rows PAT (10 rows, source region 13); `nations.py` N and EXCEPT; STATUS tracker lines 160-168; LA-ATLAS.
- **Confidence:** high.

### Chile (census: Chile; formal: Chile)
- **Consists of:** Chile: Antofagasta, Arica y Parinacota, Atacama, Bío-Bío, Coquimbo, Libertador General Bernardo O'Higgins, Maule, Región Metropolitana de Santiago, Tarapacá, Valparaíso, Ñuble (whole regions; 11 of 16).
- **Left out / lost by old countries:** Chile lost La Araucanía, Los Ríos, Los Lagos, Aisén del General Carlos Ibáñez del Campo and Magallanes y Antártica Chilena to the Araucanía-Patagonia Autonomous Zone.
- **Notes:** "Survives intact" on the northern and central regions; also keeps Arica y Parinacota and Tarapacá (the old Altiplano merger was retired). The sources are silent on Chile's Pacific islands (for example Easter Island, which sits inside Valparaíso under the whole-region rule); not stated.
- **Source:** LA-CSV rows CHL (11 rows); `nations.py` N and EXCEPT.
- **Confidence:** high.

### Uruguay (census: Uruguay; formal: Uruguay)
- **Consists of:** Uruguay: Artigas, Canelones, Cerro Largo, Colonia, Durazno, Flores, Florida, Lavalleja, Maldonado, Montevideo, Paysandú, Rivera, Rocha, Río Negro, Salto, San José, Soriano, Tacuarembó, Treinta y Tres (all 19 departments).
- **Left out / lost by old countries:** None; no old country lost territory to it and it lost none ("Stays independent", `nations.py`).
- **Notes:** The atlas lists the Uruguay River islet "Brazilian Island" as unassigned (a gap, not a decision).
- **Source:** LA-CSV rows URU (19 rows); `nations.py` N; LA-ATLAS caveats.
- **Confidence:** high.

---

## Pre-war countries, where each part went

### United States (50 states and D.C.)
| Nation | Subdivisions |
|---|---|
| Alaska | Alaska (part: north and west of the Jetté-Cook line) |
| Cascadia | Washington, Oregon, California; Alaska (part: the Panhandle, south and east of the Jetté-Cook line) |
| Colorado | Colorado, Idaho, Montana, Nevada, Utah, Wyoming |
| Sonora | Arizona, New Mexico |
| Midwest Republic | Iowa, Kansas, Minnesota, Missouri, Nebraska, North Dakota, South Dakota |
| Appalachia | Delaware, District of Columbia, Illinois, Indiana, Kentucky, Maryland, Michigan, Ohio, Virginia, West Virginia, Wisconsin |
| New England | Connecticut, Maine, Massachusetts, New Hampshire, New Jersey, New York, Pennsylvania, Rhode Island, Vermont |
| CSA | Alabama, Arkansas, Florida, Georgia, Louisiana, Mississippi, North Carolina, Oklahoma, South Carolina, Tennessee, Texas |
| Hawaii | Hawaii (whole state, to Kure Atoll) |
| Outside the sources | Midway Atoll and other US Minor Outlying Islands (unassigned); Guam, American Samoa and Northern Mariana Islands (not covered by the North or Latin America sources). In the Caribbean: Puerto Rico is its own nation; the US Virgin Islands joined the Virgin Islands nation (with the British Virgin Islands, working name); the Guantánamo Bay naval base went to Cuba (LA-CSV). |

All 50 states and D.C. are accounted for (Alaska is split between two nations).

### Canada (10 provinces, 3 territories)
| Nation | Subdivisions |
|---|---|
| Alaska | Yukon; Northwest Territories and Nunavut (part: mainland and most islands) |
| Cascadia | British Columbia |
| Prairie Federation | Alberta, Saskatchewan, Manitoba; Ontario (part: north of the DMZ line, incl. Manitoulin) |
| Demilitarized Zone (not a nation) | Ontario (part: south of the DMZ line) |
| Quebec | Québec, New Brunswick, Nova Scotia, Prince Edward Island, Newfoundland and Labrador |
| Greenland | Nunavut and Northwest Territories (part: Queen Elizabeth Islands, north of 74.7N) |
| Neutral Scientific Territory (not a nation) | Nunavut and Northwest Territories (part: Baffin Island and satellites) |

### Mexico (32 federal entities)
| Nation | Entities |
|---|---|
| Cascadia | Baja California, Baja California Sur |
| Sonora | Sonora, Chihuahua |
| Yucatán | Campeche, Chiapas, Quintana Roo, Tabasco, Yucatán |
| México | Aguascalientes, Coahuila, Colima, Distrito Federal (Ciudad de México), Durango, Guanajuato, Guerrero, Hidalgo, Jalisco, México, Michoacán, Morelos, Nayarit, Nuevo León, Oaxaca, Puebla, Querétaro, San Luis Potosí, Sinaloa, Tamaulipas, Tlaxcala, Veracruz, Zacatecas |

### Guatemala
Yucatán: Petén. Guatemala (unchanged, sovereign again): the other 21 departments (Alta Verapaz, Baja Verapaz, Chimaltenango, Chiquimula, El Progreso, Escuintla, Guatemala, Huehuetenango, Izabal, Jalapa, Jutiapa, Quezaltenango, Quiché, Retalhuleu, Sacatepéquez, San Marcos, Santa Rosa, Sololá, Suchitepéquez, Totonicapán, Zacapa).

### Brazil (26 states and the Federal District)
Amazonia: Acre, Amapá, Amazonas, Mato Grosso, Pará, Rondônia, Roraima. Brazil: the other 19 states and the Distrito Federal (listed under Brazil above).

### Bolivia
Amazonia: Pando. Bolivia: Chuquisaca, Cochabamba, El Beni, La Paz, Oruro, Potosí, Santa Cruz, Tarija.

### Argentina
Araucanía-Patagonia: Chubut, Neuquén, Río Negro, Santa Cruz, Tierra del Fuego. Argentina (without Patagonia): the other 19 units (listed under Argentina above).

### Chile
Araucanía-Patagonia: La Araucanía, Los Lagos, Los Ríos, Aisén del General Carlos Ibáñez del Campo, Magallanes y Antártica Chilena. Chile: the other 11 regions (listed under Chile above).

### Uruguay
All 19 departments stay Uruguay.

### Other countries met
- **Colombia:** Amazonia: Amazonas, Guainía, Vaupés. Colombia keeps the rest (30 units incl. Nariño, Caquetá, Putumayo, Guaviare, Vichada).
- **Peru:** Amazonia: Loreto. Peru keeps the other 25 units.
- **Venezuela:** Amazonia: Amazonas, Bolívar. Venezuela keeps the other 23 units.
- **Ecuador, Paraguay, Belize, Guyana, Suriname, Honduras, El Salvador, Nicaragua, Costa Rica, Panama:** unchanged (Belize explicitly kept whole against a Yucatán claim; Ecuador contributes nothing to Amazonia).
- **Greenland (Denmark):** the whole island is the nation Greenland (LA/NA CSV country "Greenland").
- **France:** Saint-Pierre and Miquelon is assigned to no nation (NA atlas caveat 5); Guadeloupe and Martinique form French Antilles; Guyane française is the sovereign nation French Guiana (LA-CSV).
- **Caribbean (outside the assigned list, for orientation):** Haiti was absorbed into the Dominican Republic (whole of Hispaniola); the Cayman Islands and Turks and Caicos joined Jamaica; Montserrat joined Antigua and Barbuda; Sint Maarten, Saint Martin and Saint Barthélemy form Saint Martin; Aruba and Curaçao form Aruba-Curaçao (LA-CSV).

---

## Flags, gaps and unresolved items

1. **Tennessee.** TD (2026-09-22) puts it in Appalachia; NA-CSV (2026-09-26), NA-README and the atlas put it in the CSA. NA-CSV used.
2. **Ontario.** TD says "western Ontario" to the Prairie Federation, "eastern Ontario" to Quebec and a "narrow band" for the DMZ; the later NA-CSV and README put all of Ontario north of the DMZ line in the Prairie Federation, and all south of it (including the east) in the DMZ. Later used. The DMZ's treatment is still open by the author (CENSUS-E, 2026-11-02).
3. **Alaska Panhandle limit.** The map rule (Jetté-Cook geometric cut; Yakutat Bay strip open) and the Cascadia scope (ten boroughs and census areas, Yakutat inside) are two formulations of the same territory; the sources do not state whether they match to the kilometer.
4. **Hawaii.** Midway Atoll is outside (open author question); the Northwestern Hawaiian Islands are in on the map but "TBD" as domain in HAW; other US Minor Outlying Islands (Wake, Johnston, Palmyra) are unassigned.
5. **Greenland.** Not in the census list (CENSUS-E has no row for it); the sources name no pre-war sovereign for it.
6. **Neutral Scientific Territory and the DMZ** are not nations and carry no census row of their own (the DMZ has a census row as a placeholder; the Neutral Territory has none).
7. **Unassigned in the Latin America data:** Falkland Islands (deliberately unclaimed), Bermuda, Clipperton Island, Bonaire, Saba and Sint Eustatius, Bajo Nuevo and Serranilla Banks, the "Brazilian Island" islet, South Georgia, and the Southern Patagonian Ice Field polygon (LA-ATLAS). Antarctic claims are cut at 60 S.
8. **Argentina and Chile.** The sources do not say how Argentina's South Atlantic and Antarctic claims or Chile's Pacific islands and Antarctic claim are divided; whole-subdivision logic (above) is the only rule stated.
9. **Working names.** Virgin Islands, French Antilles and Aruba-Curaçao are working names (not in the requested list).
10. **Formal names.** "People's Democratic Republic of New England" appears only in ROSTER. Capitals for Colorado, the Prairie Federation, New England, Hawaii and Yucatán are open (not needed for territory).
11. **Distrito Federal / Ciudad de México.** LA-CSV and MEX write the same entity differently; one entity either way.
12. **Natural Earth vintage.** Both CSVs use Natural Earth names (for example "Bío-Bío" and "Ñuble" for Chile, "Distrito Federal" for Mexico City); the entity set is a snapshot of that data, not a statement that no later entity changed.

---


# Part 2: Europe and South Africa

## Territory table: Europe and South Africa (post-war nations)

Read-only research, compiled 2026-11-12. No repo file was edited.

## Source key (the short names used below)
All paths are under `/home/kuroskalacs/Documents/Doll-Fi/media/`.
- **ATLAS-EU-README** = `y-files/Map Files/x Full Earth/z-full-world-atlas/data/regions/europe/README.md` (2026-10-04; the latest build, "final state" = map C-15).
- **ATLAS-EU-BUILD** = `.../z-full-world-atlas/data/regions/europe/build_europe.py` (the unit-to-nation logic) and `nations.gpkg` (51 rows; unit counts read from it).
- **INIT** = `y-files/Map Files/x Full Earth/Europe/render_europe_init.py` (builds every nation's geometry; byte-identical to the copy in `y-files/Map Files/Europe/02 reorganization/04 follow-up - final map INIT 2083/`), with `render_europe_series.py` and `README - Europe INIT 2083 map.md` (identical in both places; no CHANGES.md exists in either).
- **DATA** = `.../x Full Earth/Europe/data/` (`europe-base.gpkg` units layer; `italy-provinces.geojson`, `iberia-provinces.geojson`, `british-isles-units.geojson`, `eastern-ukraine-east-side.geojson`, `moldova-geoboundaries-adm1.geojson`). Unit names below are read from these files.
- **DL-CIN** = `y-files/Map Files/Europe/02 reorganization/03 follow-up - determining Western Europe/DECISION LOG - Confederacy of Intermarium Nations (membership order).md` (file last edited 2026-10-23; the decisions inside are dated 2026-09-30). Section numbers are cited.
- **DL-UKR** = same folder, `DECISION LOG - Eastern Ukraine and Crimea.md` (2026-09-30).
- **OQ-WE** = same folder, `OPEN QUESTIONS - Western Europe (for the later European worldbuilding pass).md` (2026-09-30).
- **INTAKE** = `Literature/books/CurrentNovelDocs/worldbuilding/nations/Europe - GDD hand-over intake (Santa Luce, the two Italys, the CIN; 2026-10-23).md`.
- **CENSUS-E** = `games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Official_Population_Census.md`, Section E (2026-11-02, DR-85), the successor-country table.
- **ATLAS-RU-README** = `.../z-full-world-atlas/data/regions/russia/README.md` (Karelia, Murmansk, the eastern-Ukraine slice, Crimea).
- **ATLAS-WORLD** = `.../z-full-world-atlas/README.md` and `data/world/merge_report.md` (the world merge).
- **AF-ATLAS** = `.../z-full-world-atlas/data/regions/africa/build_africa.py` and `nations.gpkg` (there is no README in the Africa folder).
- **AF-LOG** = `y-files/Map Files/x Full Earth/Africa/country-borders decision log.md` (identical to the copy in `Map Files/Africa/full-continent_map/`).
- **AF-RECON** = `y-files/Map Files/x Full Earth/Africa/02 reorganization/reconstruction/africa-reconstruction-base.gpkg` (units layer) and its `README - Africa reconstruction.md`.
- The World-Nations-Roster (`worldbuilding/nations/World-Nations-Roster.md`) was read; its Europe section is stale (it lists only the Intermarium and calls the rest "undocumented"), so it was not used for territory.

**Unit level.** The Europe data uses "first-order units" in the project's sense: counties, provinces, regions, voivodeships, Natural Earth admin-1. A few countries are stored at a finer level (Latvia 119 and Slovenia 193 municipalities, Malta 68 local councils, Liechtenstein 11 municipalities, Kosovo 30 municipalities, the UK at local-authority level, Hungary with county-rank cities). Those are noted where they occur. Where a nation is "whole", every unit of the old country is in it.

**Which state is described.** The nation polygons follow map C-15, the last map of the Europe series (the start-of-2083 INIT state plus the Scandinavian Trade Union, the Confederacy waves, and, at C-15 only, Karelia in Finland and Murmansk in Idelsk-Uralia). Territory is the same on every map except where noted (Karelia/Murmansk).

---

## Nations asked for

### United Kingdom (census name: United Kingdom; formal name not recorded in the sources)
- **Consists of:** United Kingdom: England (whole; nine regions in the source: North West, West Midlands, South West, North East, Yorkshire and the Humber, East Midlands, East, South East, Greater London), Scotland (whole; source regions Eastern, South Western, Highlands and Islands, North Eastern, including Orkney, Shetland and Eilean Siar), Wales (whole; West Wales and the Valleys, East Wales). Also folded in: Gibraltar and the Akrotiri and Dhekelia Sovereign Base Areas (on Cyprus). 209 source units (206 + 3).
- **Left out / lost by old countries:** the old UK lost Northern Ireland (to Northern Ireland). Scotland and Wales stay (DL-CIN 4l). The Crown Dependencies (Isle of Man, Jersey, Guernsey) are a separate row, not in this one.
- **Notes:** the base-area polygons overlap the Cyprus polygon by about 1.5 km2, which is cut from the UK row. Gibraltar and the bases are not drawn separately.
- **Source:** ATLAS-EU-README ("British Isles"), ATLAS-EU-BUILD NOTE["United Kingdom"] and UNITS, INIT (`G["United Kingdom"]`), DATA `british-isles-units.geojson`, DL-CIN 4l and 4k, CENSUS-E ("UK").
- **Confidence:** high (consistent across README, build and decision log).

### Northern Ireland (census name: Northern Ireland)
- **Consists of:** United Kingdom: Northern Ireland (whole; 26 local-government districts in the source, for example Derry, Strabane, Fermanagh, Dungannon, Armagh, Newry and Mourne, Belfast, Antrim, Down).
- **Left out / lost by old countries:** the UK lost it. Ireland (the state) gave nothing and gained nothing; the two "always remained two separate countries" (DL-CIN 4l).
- **Notes:** keeps its name and gets its own government (form open).
- **Source:** ATLAS-EU-BUILD, INIT, DL-CIN 4l, CENSUS-E.
- **Confidence:** high.

### France (census name: France)
- **Consists of:** France: all 96 metropolitan departments in the source (including Paris and the inner suburbs, Corsica as Haute-Corse and Corse-du-Sud, Alsace as Bas-Rhin and Haut-Rhin, the Pyrenees departments, and the French Basque districts, which stay French) (whole). Belgium: Wallonia's five provinces (Hainaut, Liege, Luxembourg, Namur, Walloon Brabant) plus the Brussels-Capital Region (whole of both). Luxembourg: the whole country (Diekirch, Grevenmacher, Luxembourg). 105 source units (96 + 5 + 1 + 3).
- **Left out / lost by old countries:** Belgium (Wallonia and Brussels to France; Flanders to the Netherlands) and Luxembourg (whole) lost territory to France. France itself loses nothing: the French Basque districts, Northern Catalonia and Corsica stay French (DL-CIN 4h, 4k).
- **Notes:** Brussels is a French exclave inside the Netherlands' Flemish Brabant; the source draws it French by default and marks it "under review". The German-speaking Community (Eupen and Sankt Vith, inside the province of Liege) is drawn French by default, also under review (alternative: Germany). The French overseas departments are not in the Europe data. Whether Luxembourg is an autonomous zone is undecided.
- **Source:** ATLAS-EU-README, ATLAS-EU-BUILD (`France: cu("France") + 5 + 1 + cu("Luxembourg")`), INIT, DATA `europe-base.gpkg` (France 96, Luxembourg 3, Belgium 11 units), DL-CIN 4g and 4h, OQ-WE, CENSUS-E ("Belgium", "Luxembourg").
- **Confidence:** high for the unit list; medium for Brussels and the German-speaking Community (see Flags).

### Germany (census name: Germany)
- **Consists of:** Germany: 15 Laender: Baden-Wurttemberg, Brandenburg, Bremen, Hamburg, Hessen, Mecklenburg-Vorpommern, Niedersachsen, Nordrhein-Westfalen, Rheinland-Pfalz, Saarland, Sachsen, Sachsen-Anhalt, Schleswig-Holstein, Thuringen, Berlin (all whole). Germany without Bavaria.
- **Left out / lost by old countries:** Germany lost Bayern (to Austro-Bavaria). Baden-Wurttemberg stays German; the rest of Germany stays unified (DL-CIN 4e).
- **Notes:** the German-speaking Community of Belgium is drawn French, not German (under review).
- **Source:** ATLAS-EU-README, INIT (`G["Germany"]`), DL-CIN 4e, CENSUS-E ("Germany").
- **Confidence:** high.

### Austro-Bavaria (census name: Austro-Bavaria; "Republic of Austro-Bavaria" in DL-CIN 4e)
- **Consists of:** Austria: all nine Bundeslaender (Burgenland, Karnten, Niederosterreich, Oberosterreich, Salzburg, Steiermark, Tirol, Vorarlberg, Wien) (whole). Germany: Bayern (whole, including Franconia and Bavarian Swabia). 10 source units.
- **Left out / lost by old countries:** Austria (whole) and Germany (Bayern only) lost territory to it. South Tyrol (Bozen) is in Magna Lombardia, not here.
- **Notes:** two constituent states with twin capitals Munchen and Wien; independent, not in the Confederacy. Whether all of Bavaria goes is listed as "not yet decided" in DL-CIN 4e, but the build and the map take the whole of present-day Bavaria.
- **Source:** ATLAS-EU-README, ATLAS-EU-BUILD NOTE, INIT, DL-CIN 4e, OQ-WE, CENSUS-E ("Germany", "Austria").
- **Confidence:** high for the units used; the "whole Bavaria" question is flagged.

### Netherlands (census name: Netherlands)
- **Consists of:** Netherlands: the 12 provinces (Groningen, Friesland, Drenthe, Overijssel, Flevoland, Gelderland, Utrecht, Noord-Holland, Zuid-Holland, Zeeland, Noord-Brabant, Limburg) (whole). Belgium: Flanders' five provinces (Antwerp, East Flanders, Flemish Brabant, Limburg, West Flanders) (whole). 17 source units.
- **Left out / lost by old countries:** Belgium lost Flanders to it (and Wallonia and Brussels to France).
- **Notes:** Brussels (French) is an exclave inside Flemish Brabant. The Caribbean Netherlands are not in the Europe data.
- **Source:** ATLAS-EU-README, ATLAS-EU-BUILD (`FL` list), INIT, DL-CIN 4g, CENSUS-E ("Belgium").
- **Confidence:** high; medium on the Brussels corridor (see Flags).

### Magna Lombardia (census name: Magna Lombardia)
- **Consists of:** Italy: 11 regions (whole): Piemonte, Valle d'Aosta, Liguria, Lombardia, Trentino-Alto Adige (including South Tyrol), Veneto, Friuli-Venezia Giulia, Emilia-Romagna, Toscana, Umbria, Marche. 64 source provinces.
- **Left out / lost by old countries:** Italy lost these regions to it (and the rest to Meridia and Sicilia). San Marino and the Vatican are not in it.
- **Notes:** "Border B" (Toscana, Umbria, Marche and everything above). Capital Bologna (political); Milano the economic capital. About 33.6 million people in the log.
- **Source:** ATLAS-EU-README, INIT (`NORTH_REG`), DATA `italy-provinces.geojson`, DL-CIN 4f, OQ-WE (South Tyrol inside Magna Lombardia), CENSUS-E ("Italy").
- **Confidence:** high.

### Meridia (census name: Meridia)
- **Consists of:** Italy: Lazio, Abruzzo, Molise, Campania, Apulia (Puglia), Basilicata, Calabria, Sardegna (all whole). 37 source provinces. Sicilia is cut out as a separate row (below) and the Vatican is cut out.
- **Left out / lost by old countries:** Italy lost these regions to it. San Marino is separate.
- **Notes:** capital Roma, with the Vatican inside it, 52 km from the border. Sardinia is in the Meridia polygon (see Flags: the 2026-10-23 "Autonomous Zone" yes is unresolved).
- **Source:** ATLAS-EU-README, ATLAS-EU-BUILD (`Meridia`: not NORTH_REG and not Sicily), INIT, DL-CIN 4f, INTAKE section 6 item 4, CENSUS-E.
- **Confidence:** high for the region list; medium for Sardinia's status.

### Sicilia (autonomous zone within Meridia; census: "Sicilia (autonomous zone within Meridia)")
- **Consists of:** Italy: Sicily (the island's 9 provinces; whole).
- **Left out / lost by old countries:** Italy lost it (to Meridia, as an Autonomous Zone).
- **Notes:** in the atlas it is its own row (`autonomous zone`), cut out of Meridia, drawn hatched; its color is Meridia's.
- **Source:** ATLAS-EU-README ("Special rows"), ATLAS-EU-BUILD, INIT, DL-CIN 4f.
- **Confidence:** high.

### Spain (census name: Spain)
- **Consists of:** Spain: every autonomous community except Catalonia and the Basque Country and Navarre: Andalucia (Almeria, Cadiz, Cordoba, Granada, Huelva, Jaen, Malaga, Sevilla), Aragon (Huesca, Teruel, Zaragoza), Asturias, Cantabria (except the Villaverde enclave), Castilla y Leon (Avila, Burgos except the Trevino enclave, Leon, Palencia, Salamanca, Segovia, Soria, Valladolid, Zamora), Castilla-La Mancha (Albacete, Ciudad Real, Cuenca, Guadalajara, Toledo), Extremadura (Badajoz, Caceres), Galicia (La Coruna, Lugo, Orense, Pontevedra), La Rioja, Madrid, Murcia, Valencian Community (Alicante, Castellon, Valencia), the Balearic Islands, Ceuta, Melilla. The Canary Islands (Las Palmas, Santa Cruz de Tenerife) are in the source geometry and in the 44-unit count. 44 source units.
- **Left out / lost by old countries:** Spain lost Catalonia (4 provinces), the Basque Country (Biscay, Gipuzkoa, Alava) and Navarre, and the Trevino and Villaverde enclaves, to Catalonia and the Basque Country.
- **Notes:** Galicia, Valencia and the Balearics stay Spanish (DL-CIN 4h). The Trevino and Villaverde enclaves are cut out of Spain. Olivenza stays Spanish-administered.
- **Source:** ATLAS-EU-README, ATLAS-EU-BUILD (`Spain`: not Pais Vasco, Foral de Navarra, Cataluna), INIT, DATA `iberia-provinces.geojson`, DL-CIN 4h and 4k.
- **Confidence:** high for the cut; medium for the Canary Islands (README says they are not in the Europe data, but the geometry is; see Flags). CENSUS-E lists Spain's successors as only "Basque Country, Catalonia" (the remainder row "Spain" is not written there).

### Catalonia (census name: Catalonia)
- **Consists of:** Spain: Barcelona, Girona (Gerona), Lleida (Lerida), Tarragona (all whole; the four provinces of the autonomous community, about 8.0 million). 4 source units.
- **Left out / lost by old countries:** Spain lost them. French Northern Catalonia stays French; Valencia and the Balearics stay Spanish. Andorra is separate.
- **Notes:** extent "taken as the four provinces unless the author says otherwise" (DL-CIN 4h); the wider Catalan lands are listed as open in OQ-WE.
- **Source:** ATLAS-EU-README, ATLAS-EU-BUILD, INIT, DL-CIN 4h, OQ-WE, CENSUS-E.
- **Confidence:** high (extent flagged as the working default).

### Basque Country (census name: Basque Country)
- **Consists of:** Spain: Biscay (Bizkaia), Gipuzkoa, Alava, Navarre (Navarra) (whole), plus the Trevino enclave (a Burgos exclave inside Alava, about 290 km2) and the Valle de Villaverde enclave (a Cantabria exclave inside Biscay, about 10 km2). 6 source units (4 provinces + 2 enclave parts); about 2.9 million people.
- **Left out / lost by old countries:** Spain lost them (Castile and Leon lost Trevino, Cantabria lost Villaverde). France loses nothing: the French Basque districts (Labourd, Lower Navarre, Soule) stay French.
- **Notes:** Navarre's inclusion is the log's own reading, marked "to be confirmed"; the build includes it.
- **Source:** ATLAS-EU-README, ATLAS-EU-BUILD, INIT (`BASQ_MAIN`, `ENCL`), DL-CIN 4h, CENSUS-E.
- **Confidence:** high for the build; medium for Navarre (the log's confirmation line says "four Spanish Basque provinces: Biscay, Gipuzkoa, Alava and Navarre", while a later sentence still marks Navarre "to be confirmed").

### Poland (census name: Poland)
- **Consists of:** Poland: all 16 voivodeships (Silesian, Lesser Poland, Subcarpathian, Lower Silesian, Opole, Podlachian, Warmian-Masurian, Lubusz, West Pomeranian, Lublin, Pomeranian, Masovian, Lodz, Kuyavian-Pomeranian, Greater Poland, Swietokrzyskie) (whole).
- **Left out / lost by old countries:** none; present-day borders, no transfers (DL-CIN section 1, the "ULB doctrine").
- **Notes:** the core of the Confederacy; capital Lublin, later Katowice (DL-CIN preamble).
- **Source:** ATLAS-EU-README, INIT, DL-CIN section 1.
- **Confidence:** high.

### Czechia (census name: Czechia; pre-war "Czech Republic")
- **Consists of:** Czech Republic: all 14 regions (Prague, Stredocesky, Jihocesky, Plzensky, Karlovarsky, Ustecky, Liberecky, Kralovehradecky, Pardubicky, Vysocina, Jihomoravsky, Olomoucky, Zlinsky, Moravskoslezsky) (whole).
- **Left out / lost by old countries:** none; present-day borders (DL-CIN 4a2).
- **Notes:** the census row is a rename of the pre-war name.
- **Source:** ATLAS-EU-README, INIT, DL-CIN 4a2, CENSUS-E ("Czech Republic").
- **Confidence:** high.

### Slovakia (census name: Slovakia)
- **Consists of:** Slovakia: all 8 regions (Bratislavsky, Trnavsky, Trenciansky, Nitriansky, Zilinsky, Banskobystricky, Presov, Kosicky) (whole).
- **Left out / lost by old countries:** none. The Hungarian-majority districts of Dunajska Streda and Komarno stay Slovak (DL-CIN 4a2).
- **Notes:** none beyond the above.
- **Source:** ATLAS-EU-README, INIT, DL-CIN 4a2.
- **Confidence:** high.

### Hungary (census name: Hungary)
- **Consists of:** Hungary: whole (19 counties and Budapest; the source lists 43 units, adding county-rank cities such as Szeged, Pecs, Debrecen and Gyor). Romania: five counties, Satu Mare, Bihor, Salaj, Maramures, Arad (all whole; about 30,400 km2). 48 source units (43 + 5).
- **Left out / lost by old countries:** Romania lost the five counties to Hungary. Slovakia, Ukraine (Transcarpathia), Serbia (Vojvodina) and Austria lost nothing to Hungary. Cluj is not taken; Szekely Land (Harghita, Covasna) and Mures stay Romanian (DL-CIN 4b).
- **Notes:** the "repatriation" rules for ethnic Romanians in the five counties (six-generation proof, joint commission) are in DL-CIN 4b. No Szekely Autonomous Zone.
- **Source:** ATLAS-EU-README, ATLAS-EU-BUILD (`PARTIUM`), INIT, DL-CIN section 1 and 4b, CENSUS-E ("Romania").
- **Confidence:** high.

### Romania (census name: Romania)
- **Consists of:** Romania: 37 units: Bucharest and Ilfov, plus the counties Alba, Arges, Bacau, Bistrita-Nasaud, Botosani, Braila, Brasov, Buzau, Calarasi, Caras-Severin, Cluj, Constanta, Covasna, Dambovita, Dolj, Galati, Giurgiu, Gorj, Harghita, Hunedoara, Ialomita, Iasi, Mehedinti, Mures, Neamt, Olt, Prahova, Sibiu, Suceava, Teleorman, Timis, Tulcea, Valcea, Vaslui, Vrancea (all whole). That is Romania minus the five counties given to Hungary.
- **Left out / lost by old countries:** Romania lost Satu Mare, Bihor, Salaj, Maramures and Arad to Hungary.
- **Notes:** Moldova is a separate nation; a Moldova-Romania union is undecided.
- **Source:** ATLAS-EU-README, ATLAS-EU-BUILD (`cu("Romania") - 5`), INIT, DL-CIN 4b.
- **Confidence:** high.

### Serbia (census name: Serbia)
- **Consists of:** Serbia: all 25 districts in the source (Belgrade; the seven Vojvodina districts: North Backa, West Backa, South Backa, North Banat, Central Banat, South Banat, Srem; and central Serbia's districts) (whole). Kosovo: the whole territory (30 municipalities in the source, about 10,900 km2). 55 source units.
- **Left out / lost by old countries:** Kosovo (as a pre-war state) lost all of itself to Serbia. Serbia itself loses nothing.
- **Notes:** Kosovo is not a separate country in the setting (DL-CIN section 1). Whether the Albania block applies to Albanian-majority areas inside Serbia is open.
- **Source:** ATLAS-EU-README, ATLAS-EU-BUILD (`cu("Serbia") + cu("Kosovo")`), INIT, DL-CIN section 1 and 3, CENSUS-E ("Kosovo").
- **Confidence:** high.

### Slovenia (census name: Slovenia)
- **Consists of:** Slovenia: whole (193 municipalities in the source; the source has no coarser level).
- **Left out / lost by old countries:** none.
- **Notes:** joins the Confederacy on a voting basis in wave 11 with Croatia.
- **Source:** ATLAS-EU-README, INIT, DL-CIN section 1.
- **Confidence:** high.

### Croatia (census name: Croatia)
- **Consists of:** Croatia: whole (20 counties plus Grad Zagreb; the source holds 21 units, one county listed twice).
- **Left out / lost by old countries:** none.
- **Notes:** wave 11 with Slovenia, voting basis.
- **Source:** ATLAS-EU-README, INIT, DL-CIN section 1.
- **Confidence:** high.

### Bulgaria (census name: Bulgaria)
- **Consists of:** Bulgaria: whole (28 oblasts in the source, including Sofia city and Sofia province). Turkey: Kirklareli Province (whole; East Thrace, 6,889 km2). 29 source units.
- **Left out / lost by old countries:** Turkey lost Kirklareli to Bulgaria (and Edirne and Tekirdag to Greece). Istanbul Province stays Turkish.
- **Notes:** a Muslim, Turkish-speaking population comes with Kirklareli (DL-CIN 6c, as the log's own consequence note).
- **Source:** ATLAS-EU-README, ATLAS-EU-BUILD (`cu("Bulgaria") + 1`), INIT (`turkey_thrace` layer), DL-CIN 6c.
- **Confidence:** high.

### Lithuania (census name: Lithuania)
- **Consists of:** Lithuania: all 10 counties (Alytus, Kaunas, Klaipeda, Marijampole, Panevezys, Siauliai, Taurage, Telsiai, Utena, Vilnius) (whole).
- **Left out / lost by old countries:** none. The Curonian Spit stays split with Kaliningrad as today (DL-CIN 4 item 4).
- **Notes:** none.
- **Source:** ATLAS-EU-README, INIT, DL-CIN section 1 and 4.
- **Confidence:** high.

### Latvia (census name: Latvia)
- **Consists of:** Latvia: whole (119 municipalities in the source).
- **Left out / lost by old countries:** none; Latgale stays Latvian (DL-CIN 4a3).
- **Notes:** none.
- **Source:** ATLAS-EU-README, INIT, DL-CIN 4a3.
- **Confidence:** high.

### Estonia (census name: Estonia)
- **Consists of:** Estonia: all 15 counties (Harju, Hiiu, Ida-Viru, Jogeva, Jarva, Laane, Laane-Viru, Polva, Parnu, Rapla, Saare, Tartu, Valga, Viljandi, Voru) (whole).
- **Left out / lost by old countries:** none; Ida-Viru stays Estonian (DL-CIN 4a3).
- **Notes:** none.
- **Source:** ATLAS-EU-README, INIT, DL-CIN 4a3.
- **Confidence:** high.

### Belarus (census name: Belarus)
- **Consists of:** Belarus: Brest, Gomel, Grodno, Minsk, Mogilev, Vitebsk oblasts and the City of Minsk (7 units; whole).
- **Left out / lost by old countries:** none; Grodno Oblast and its Polish minority stay (DL-CIN 4a4).
- **Notes:** Confederacy observer ("restricted", drawn hatched).
- **Source:** ATLAS-EU-README, INIT, DL-CIN 4a4.
- **Confidence:** high.

### Ukraine (census name: Ukraine)
- **Consists of:** Ukraine: whole except the eastern slice and Crimea. In (whole): Chernihiv, Volyn, Rivne, Zhytomyr, Kyiv Oblast, Kyiv City, Transcarpathia, Chernivtsi, Ivano-Frankivsk, Odesa, Vinnytsia, Lviv, Sumy, Mykolaiv, Poltava, Khmelnytskyi, Ternopil, Cherkasy, Kirovohrad. Kherson Oblast: the part west of the Dnieper only (about 25% of the oblast). 25 source units (the polygon is the 25 units with the eastern side cut away).
- **Left out / lost by old countries:** Ukraine lost Luhansk, Donetsk, Kharkiv, Dnipropetrovsk and Zaporizhzhia oblasts (whole) and the east (left) bank of Kherson Oblast to Russia (core state), and Crimea and Sevastopol to Donska-Kubania (an Autonomous Zone).
- **Notes:** Zaporizhzhia's right-bank corner is left with the oblast, and the Kherson left bank at raion level is "deferred" (DL-UKR 3). Zakarpattia, Chernivtsi and Budjak stay Ukrainian.
- **Source:** ATLAS-EU-README ("Left to the Russia agent"), ATLAS-EU-BUILD, INIT (`east_ua`), DL-UKR sections 1 and 3, DL-CIN 4a5, ATLAS-RU-README, CENSUS-E ("Ukraine" carries into "Russia (core state)").
- **Confidence:** high for oblast level; medium for the Kherson line (DL-UKR 3, raion-level cut unsettled).

### Norway (census name: Norway)
- **Consists of:** Norway: all 19 counties as the source stores them (Troms, Nordland, Nord-Trondelag, Sor-Trondelag, Hedmark, Akershus, Ostfold, Finnmark, Oslo, Buskerud, Vestfold, Telemark, Aust-Agder, Vest-Agder, Rogaland, Hordaland, Sogn og Fjordane, More og Romsdal, Oppland) (whole).
- **Left out / lost by old countries:** none.
- **Notes:** Svalbard and Jan Mayen are not in the Europe data; the world merge adds them to Norway as a gap fill (ATLAS-WORLD, "20 pieces (62,090 km2) added to Norway"; the README names Svalbard to Norway). Scandinavian Trade Union member.
- **Source:** ATLAS-EU-README, ATLAS-EU-BUILD, INIT, ATLAS-WORLD.
- **Confidence:** high (Svalbard: medium, inferred from the README and merge report wording).

### Sweden (census name: Sweden)
- **Consists of:** Sweden: all 21 counties (Norrbotten, Vasterbotten, Jamtland, Dalarna, Varmland, Vastra Gotaland, Vasternorrland, Gavleborg, Uppsala, Stockholm, Sodermanland, Ostergotland, Kalmar, Blekinge, Skane, Halland, Gotland, Vastmanland, Jonkoping, Orebro, Kronoberg) (whole).
- **Left out / lost by old countries:** none.
- **Notes:** Scandinavian Trade Union member.
- **Source:** ATLAS-EU-README, INIT, DL-CIN 4j.
- **Confidence:** high.

### Denmark (census name: Denmark)
- **Consists of:** Denmark: the 5 regions (Hovedstaden, Sjaelland, Syddanmark, Midtjylland, Nordjylland) (whole). Greenland is not in this row.
- **Left out / lost by old countries:** none. The Faroe Islands are their own row.
- **Notes:** Greenland has "honorary status" in the Union and is not a Europe-data nation. In the North America data Greenland is its own nation (Natural Earth admin-0 plus the Queen Elizabeth Islands). Scandinavian Trade Union member.
- **Source:** ATLAS-EU-README ("Greenland, Svalbard, others"), INIT, DL-CIN 4j, `.../data/regions/north-america/README.md`.
- **Confidence:** high for the Europe row; medium for how Greenland and Denmark relate in the atlas (see Flags).

### Finland (census name: Finland)
- **Consists of:** Finland: all 18 regions (Lapland, Northern Ostrobothnia, Kainuu, North Karelia, South Karelia, Kymenlaakso, Uusimaa, Finland Proper, Satakunta, Ostrobothnia, Central Ostrobothnia, Northern Savonia, Southern Savonia, Central Finland, Southern Ostrobothnia, Pirkanmaa, Tavastia Proper, Paijat-Hame) (whole). Aland Islands (11 municipalities; whole). Russia: the Republic of Karelia (whole; about 174,000 km2). Europe's own Finland row has 29 units and excludes the Republic; the atlas merge adds the Karelia piece from the Russia package.
- **Left out / lost by old countries:** Russia lost the Republic of Karelia to Finland. Murmansk Oblast does not go to Finland (to Idelsk-Uralia). The Karelian Isthmus and Vyborg (Leningrad Oblast) are not part of the plan.
- **Notes:** the Karelia transfer is a later-stage change: shown only at map C-15 (before that, "Karelia" is a proto-country with Murmansk). The ethnic-Russian population transfer is not built. Scandinavian Trade Union member.
- **Source:** ATLAS-EU-README ("Left to the Russia agent"), ATLAS-RU-README (Finland row), ATLAS-WORLD ("joined 2 rows named 'Finland'"), DL-CIN 4i, OQ-WE ("Finland and Karelia"), CENSUS-E ("Russia" carries into Finland).
- **Confidence:** high that the Republic of Karelia is included; medium on timing and on the Isthmus (open).

### Iceland (census name: Iceland)
- **Consists of:** Iceland: whole (9 regions in the source: Austurland, Sudurland, Sudurnes, Reykjavik, Hofudborgarsvaedi, Vesturland, Vestfirdir, Nordurland vestra, Nordurland eystra).
- **Left out / lost by old countries:** none.
- **Notes:** Scandinavian Trade Union member.
- **Source:** ATLAS-EU-README, INIT, DL-CIN 4j.
- **Confidence:** high.

### South Africa (census name: not listed in CENSUS-E Section E; the Africa data row is "South Africa")
- **Consists of:** South Africa: all nine provinces (Eastern Cape, Free State, Gauteng, KwaZulu-Natal, Limpopo, Mpumalanga, North West, Northern Cape, Western Cape) (whole). 9 source units.
- **Left out / lost by old countries:** none. South Africa is the pre-war state, unchanged.
- **Notes:** Lesotho and Eswatini stay separate countries. The Western Cape and KwaZulu-Natal were weighed for splitting and left as they are. The Southern African Customs Union, the Common Monetary Area and SADC already link several of the eleven southern countries; no new arrangement.
- **Source:** AF-LOG ("South: all eleven countries stay as they are", 2026-10-04), AF-ATLAS (`africa/nations.gpkg`, South Africa kind "nation", note "stays as it is"), AF-RECON (units layer, nine rows, all marked "Stays as it is (author, 2026-10-04)").
- **Confidence:** high.

---

## The rest of the map (one line each)
Europe data defines these other rows (ATLAS-EU-README, ATLAS-EU-BUILD, INIT). Unit counts are from `nations.gpkg`.

- **Ireland** (34 units): the island of Ireland south of Northern Ireland; unchanged.
- **Crown Dependencies** (3): Isle of Man, Jersey, Guernsey (with Sark) as one small nation.
- **Faroe Islands** (1): Scandinavian Trade Union member, its own row.
- **Switzerland** (26 cantons), **Liechtenstein** (11), **Monaco** (1), **Andorra** (7), **San Marino** (9), **Vatican City** (1, cut out of Meridia), **Malta** (68 councils): as today (DL-CIN 4k: changes deferred to later timeline stages).
- **Portugal** (20 units, as listed: 18 districts plus Madeira and the Azores): as today (DL-CIN 4h); Olivenza stays Spanish-administered.
- **Kaliningrad** (1): the entire former Russian oblast as a Confederacy member nation (wave 1); not in Russia's csv.
- **Moldova** (40 units, with the Transnistria and Bender area cut out as a separate geometry): Confederacy wave 9; Gagauzia stays inside.
- **Transnistria** (disputed, 2 geoBoundaries units: Transnistria and Bender): cut out of Moldova; status unsettled.
- **Montenegro** (21 municipalities): Confederacy wave 13. **Bosnia and Herzegovina** (18 units): strictly an observer.
- **Skoprodija** (formerly North Macedonia; 72 of its 84 municipalities): observer, joins last; the 12 western municipalities (Struga, Centar Zupa, Debar, Mavrovo and Rostusa, Gostivar, Vrapciste, Bogovinje, Tetovo, Tearce, Zelino, Brvenica, Vevcani) go to Albania.
- **Albania** (24 = 12 counties + the 12-municipality belt): barred from the Confederacy.
- **Greece** (16 = 14 regions incl. Mount Athos + Edirne and Tekirdag from Turkey): Confederacy wave 14.
- **Cyprus** (6): the whole island including Northern Cyprus (the Green Line is only drawn dashed); the Akrotiri and Dhekelia base areas belong to the UK row.
- **Russia group (supplied by the Russia package, not Europe's file):** Russia (core, including the eastern-Ukraine slice), Idelsk-Uralia (with Murmansk Oblast at C-15), Donska-Kubania (with Crimea and Sevastopol as an Autonomous Zone), Karelia (to Finland at C-15), Chechnya, Dagestan, Ingushetia, Kabardino-Balkaria, Karachay-Cherkessia, North Ossetia-Alania. (Siberia, Kunnarantaiga and Tuva are in the Russia csv but not drawn by Europe.)
- **Groupings:** the Scandinavian Trade Union = Norway, Sweden, Finland (with Aland), Denmark, Iceland, Faroe Islands (Greenland honorary). The Confederacy of Intermarium Nations at C-15: members (17) Poland, Lithuania, Kaliningrad, Czechia, Slovakia, Latvia, Estonia, Ukraine, Hungary, Romania, Moldova, Bulgaria, Croatia, Slovenia, Serbia, Montenegro, Greece; observers (3) Belarus, Bosnia and Herzegovina, Skoprodija; barred Albania. Austro-Bavaria is outside it.

---

## Pre-war countries, where each part went
(Pre-war country in scope: every old country that changed, plus those the nations above draw on. Unchanged countries are in the last line.)

- **Belgium** (dissolved): Hainaut, Liege, Luxembourg, Namur, Walloon Brabant and Brussels to **France**; Antwerp, East Flanders, Flemish Brabant, Limburg and West Flanders to the **Netherlands**. The German-speaking Community (inside Liege) is drawn French, under review.
- **Luxembourg:** whole to **France**.
- **Germany:** Bayern to **Austro-Bavaria**; the other 15 Laender stay in **Germany**.
- **Austria:** whole to **Austro-Bavaria**.
- **United Kingdom:** England, Scotland, Wales (with Gibraltar and the Cyprus base areas) stay as **United Kingdom**; Northern Ireland to **Northern Ireland**; the Crown Dependencies are their own row.
- **Ireland:** unchanged, **Ireland**.
- **Spain:** Catalonia (4 provinces) to **Catalonia**; Biscay, Gipuzkoa, Alava, Navarre, plus Trevino (Burgos) and Villaverde (Cantabria), to the **Basque Country**; the rest remains **Spain**.
- **Italy:** Piemonte, Valle d'Aosta, Liguria, Lombardia, Trentino-Alto Adige, Veneto, Friuli-Venezia Giulia, Emilia-Romagna, Toscana, Umbria, Marche to **Magna Lombardia**; Lazio, Abruzzo, Molise, Campania, Apulia, Basilicata, Calabria, Sardegna to **Meridia**; Sicily to **Sicilia** (autonomous zone in Meridia).
- **Romania:** Satu Mare, Bihor, Salaj, Maramures, Arad to **Hungary**; the other 37 units stay **Romania**.
- **Kosovo:** whole to **Serbia**.
- **North Macedonia:** 72 municipalities to **Skoprodija** (renamed); 12 western municipalities to **Albania**.
- **Turkey:** Kirklareli Province to **Bulgaria**; Edirne and Tekirdag Provinces to **Greece**.
- **Russia:** the Republic of Karelia to **Finland**; Kaliningrad Oblast to **Kaliningrad**; Murmansk Oblast to Idelsk-Uralia; Crimea and Sevastopol to Donska-Kubania (Autonomous Zone).
- **Ukraine:** Luhansk, Donetsk, Kharkiv, Dnipropetrovsk, Zaporizhzhia (whole) and the east bank of Kherson to **Russia (core state)**; Crimea and Sevastopol (already counted under Russia in the data) to Donska-Kubania; the remainder stays **Ukraine**.
- **Moldova:** stays **Moldova**, with Transnistria and Bender marked disputed.
- **Cyprus:** whole island (with Northern Cyprus) stays **Cyprus**; the two British base areas go to the **United Kingdom** row.
- **Czech Republic:** whole, renamed **Czechia**.
- **South Africa:** whole, unchanged, **South Africa**.
- **Unchanged and whole in their own rows:** Poland, Slovakia, Slovenia, Croatia, Bulgaria (plus Kirklareli), Lithuania, Latvia, Estonia, Belarus, Hungary (plus the five counties), France (plus Belgium's French parts and Luxembourg), Netherlands (plus Flanders), Norway, Sweden, Denmark, Finland (plus Karelia), Iceland, Portugal, Switzerland, Liechtenstein, Monaco, Andorra, San Marino, Vatican City, Malta, Montenegro, Bosnia and Herzegovina, Albania (plus the belt), Greece (plus East Thrace), Faroe Islands.

---

## Checks against CENSUS-E Section E
All the splits the brief names agree with the build: Belgium to France and the Netherlands; Luxembourg to France; Austria and part of Germany (Bayern) to Austro-Bavaria; Italy to Magna Lombardia, Meridia and Sicilia; Romania's part to Hungary; Kosovo to Serbia; the UK to Northern Ireland and the United Kingdom; Spain to Basque Country, Catalonia (and Spain); Russia carries into Finland (the Republic of Karelia); Ukraine carries into Russia (core state); the Czech Republic is renamed Czechia.

## Flags, gaps and unresolved items
1. **Sardinia.** The atlas and build put Sardegna inside Meridia (no separate Autonomous Zone). DL-CIN 4f (2026-09-30) says Sardinia is "fully part of the South, not an Autonomous Zone" (keeps its existing special statute). INTAKE section 6 item 4 (2026-10-23) records the author's "yes" to an Autonomous Zone hosted by Meridia and flags the conflict as OPEN; the DM Glossary `OPEN CONFLICTS (2026-10-30).md` lists it still open. The later date favors "Autonomous Zone", but it is not applied anywhere in the data. The territory (Sardegna in Meridia) is the same either way. Separately, GDD notes give Meridia "about 23.8 million without Sardinia", while the log's 25.4 million figure includes Sardinia.
2. **Brussels.** DL-CIN 4g has four successive entries (solid French, then an enclave without a corridor, then, last, "REVISED: Brussels gets the corridor after all and the city is divided French/Dutch, with Sint-Genesius-Rode joining France"), and marks the whole arrangement "for review". The build draws Brussels whole as French with no corridor, and Sint-Genesius-Rode stays in Flemish Brabant (Netherlands). The Netherlands row and the France row would change if the last entry is applied. Unresolved.
3. **German-speaking Community** (Eupen, Sankt Vith; inside Liege). Drawn French by default; the alternative is Germany (OQ-WE). Unresolved.
4. **Luxembourg autonomous-zone status** undecided; the Belgian province of Luxembourg goes with Wallonia to France by default (OQ-WE).
5. **Canary Islands, Madeira, Azores.** ATLAS-EU-README says they are "not in the Europe data", but the data does contain them: the Canary Islands (two provinces) are in `iberia-provinces.geojson` and in Spain's 44-unit count, and Madeira and the Azores are in the 20 Portugal units. They are off the map frame. Treat as part of Spain and Portugal; the README line is out of line with the data.
6. **Greenland and Svalbard.** Greenland is a separate "nation" in the North America data (Natural Earth outline plus the Queen Elizabeth Islands) while the Europe notes call it "Danish; honorary in the Union". The two statements are not reconciled in the sources. Svalbard and Jan Mayen are not in Europe's Norway row; the world merge adds them to Norway.
7. **Karelia and Murmansk timing.** The territory is fixed (Karelia Republic to Finland, Murmansk to Idelsk-Uralia) but "which map shows the change" is open; only C-15 shows it. The Karelian Isthmus and Vyborg are not in the plan, and the Russian-population transfer is not built. The Russia package's own CSV still shows the proto-country "Karelia" with Murmansk (ATLAS-RU-README).
8. **Eastern Ukraine.** The Kherson left-bank cut at raion level is deferred; Zaporizhzhia's right-bank corner is left with the oblast; whether the slice is one unit, an autonomous zone or goes to Donska-Kubania is listed open (DL-UKR 3 and 4). The slice borders may leave slivers against the Russia polygons.
9. **Navarre in the Basque Country** is both confirmed ("four Spanish Basque provinces ... Navarre") and marked "to be confirmed" in DL-CIN 4h. The build includes it.
10. **Skoprodija / Albania belt.** DL-CIN section 1 names Plasnica in the 12-municipality belt in one paragraph, and Vevcani (not Plasnica) in the pocket-rule paragraph; the build and the atlas use Vevcani (Plasnica stays in Skoprodija). Other Albanian-plurality municipalities (Lipkovo, Saraj, Aracinovo, Zajas, Oslomej, Studenicani, Cair) are not cut.
11. **Austro-Bavaria.** DL-CIN 4e lists "whether the whole of present-day Bavaria goes" as not yet decided, but build, README and map use all of Bayern. The log also says Baden-Wurttemberg stays German.
12. **Census Section E gaps.** Section E lists Spain's carrying rows as "Basque Country, Catalonia" only (no "Spain" row), has no row for Kaliningrad (a nation in the Europe data), and does not mention Ireland, Crown Dependencies or the other unchanged countries (expected, since their names do not change). South Africa is not in Section E at all.
13. **Spelling and unit-level caveats.** Unit names above are the source's, in ASCII for diacritics (the data has Polish, Czech, Hungarian, Romanian and Slovene diacritics; Romanian names in the data lack some of them). The source data has some typos ("Seien-et-Marne", "Haute-Rhin", "Sjaelland" as "Sjaaelland"). Counts for Latvia, Slovenia, Malta, Liechtenstein, Kosovo, the UK and Hungary are at municipality or local-authority level, not first-order.
14. **Sources not found.** No CHANGES.md in the Europe folders; no nation profile for Magna Lombardia, Meridia, the CIN or any Europe nation (INTAKE section 3); no README in the atlas Africa folder. The World-Nations-Roster is stale for Europe and was not used. The two merge-report gap fills "2 pieces (2,964 km2) added to France" and "1 piece (1 km2) to Crown Dependencies" are not identified in the report, so the table does not name them. French overseas departments, the Caribbean Netherlands and other overseas territories are not in the Europe data; the sources are silent on them.
15. **Unverified items from memory in the sources** (marked as such in DL-CIN): many figures (populations, areas, the Brussels and Luxembourg facts). None of those figures were used above except the areas the log gives for Hungary's gain (about 30,400 km2) and Kosovo (about 10,900 km2).

---


# Part 3: Russia, Asia and Oceania

## Territory table: Russia, Asia (except South Asia) and Oceania

Read-only research, compiled 2026-11-12. Nothing in any repo was edited.

## Sources used, and how they rank

Path shorthands used below:
- **ATLAS** = `y-files/Map Files/x Full Earth/z-full-world-atlas/data/regions/<region>/` (README.md and build_<region>.py), built 2026-10-04. Its READMEs name the "final state" each region uses.
- **XFE** = `y-files/Map Files/x Full Earth/` (the source folders the atlas builds read: `Russia/`, `Asia/Asia (East)/`, `Asia/Asia (Southeast)/`, `Asia/Asia (West)/`, `Oceania/`). Files under `y-files/Map Files/Asia/` and `Oceania/` (without "x Full Earth") were checked and are identical or older.
- **NATIONS** = `Literature/books/CurrentNovelDocs/worldbuilding/nations/` (`central-asia-map-data/`, `east-asia-map-data/`, `mainland-` and `maritime-southeast-asia-map-data/`, `oceania-map-data/`, `World-Nations-Roster.md`). Used as background only. `russia-map-data/` there mirrors the ORIGINAL 20-nation state and is superseded, so it was not used for the territory lists.
- **CENSUS** = `games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Official_Population_Census.md`, Section E (added 2026-11-02, DR-85), used as the check on successor names. It is the latest-dated source and wins on NAMES; it says nothing about subdivisions, so the atlas and XFE data win on TERRITORY.

Final states used (latest in each source):
- Russia: XFE `Russia/` = the `09 follow-up` of 2026-09-30 (subdivisions.csv, 90 rows; CHANGES.md; `PROGRESS TRACKER - Read This First.md`), plus Europe map C-15 (author, 2026-09-30): Republic of Karelia to Finland, Murmansk Oblast to Idelsk-Uralia (applied in ATLAS `russia/build_russia.py`, which overrides the CSV's proto-nation "Karelia").
- East Asia: XFE `Asia/Asia (East)/` map F (2267 to present), read from `asia-east-current.zip` (`data/province_assignments.csv`, column `owner_map_f`; `data/polities.csv`), as used by ATLAS `east-asia/`.
- Southeast Asia: XFE `Asia/Asia (Southeast)/subdivisions.csv` and `subdivisions_maritime.csv` (round 3, 2026-09-26; byte-identical to the `09 follow-up - usable-ready form` copy), as used by ATLAS `southeast-asia/`.
- Central Asia: NATIONS `central-asia-map-data/regions.csv` (2026-09-29) and ATLAS `west-asia/build_west-asia.py` (`CA_ASSIGN`), XFE `Asia/Asia (West)/` `08 follow-up` (2026-09-30).
- Oceania: XFE `Oceania/subdivisions.csv` (flat-color pass, round 3, 2026-09-26; identical to `04 follow-up - map-ready`), as used by ATLAS `oceania/`.
- Names: ATLAS world merge (`z-full-world-atlas/README.md`, `scripts/merge_world.py`) renames the source's "Deep South" to **Patani** (author, 2026-10-04, marked for review); the CENSUS also writes Patani.

Unit names are written as the source files spell them. For Russia the sources use Natural Earth spellings; the standard name is added in brackets where it differs.

---

## RUSSIA (pre-war Russia becomes 13 successor rows; Ukraine's east and Crimea join them)

Unit counts check: Russia 24 + Idelsk-Uralia 25 (+ Murmansk) + Donska-Kubania 9 + Künnarantaiga 12 + Siberia 11 + Tuva 1 + six Caucasus republics 6 + Karelia 1 = 90 rows in subdivisions.csv (84 Russian units, 6 Ukrainian). Kaliningrad is not in the CSV.

### Russia (core state) (census "Russia (core state)"; native Россия; capital Moscow)
- **Consists of:**
  - Russia (pre-war), 18 whole units: Belgorod, Bryansk, City of St. Petersburg (federal city), Kaluga, Kursk, Leningrad, Lipetsk, Moscow Oblast [source "Moskovskaya"], Moscow (federal city) [source "Moskva"], Novgorod, Oryol [source "Orel"], Pskov, Ryazan, Smolensk, Tambov, Tula, Tver, Voronezh (all whole).
  - Ukraine (pre-war), 6 units: Luhansk Oblast, Donetsk Oblast, Kharkiv Oblast, Dnipropetrovsk Oblast, Zaporizhzhia Oblast (all whole) and Kherson Oblast (part: east of the Dnieper only, about 75% of the oblast by area; Kherson city and the right bank stay Ukrainian).
- **Left out / lost by old countries:** Ukraine loses the five whole oblasts and the Kherson left bank to this nation (author, 2026-09-30); Ukraine also loses Crimea and Sevastopol, but to Donska-Kubania (below). Pre-war Russia's other units went to the 12 other successors, to Finland (Karelia) and to Kaliningrad.
- **Notes:** Kherson is the only district-level exception to the whole-first-order-unit rule (geometry from `kherson_left_bank.geojson`); the raion-level cut is flagged unsettled in CHANGES.md. Whether the eastern-Ukraine slice keeps ordinary oblast status or gets its own designation is open. The CENSUS table lists "Ukraine -> Russia (core state)" only.
- **Source:** XFE `Russia/subdivisions.csv` (nation = Russia, 24 rows); `Russia/CHANGES.md` (top entries, 2026-09-30); ATLAS `russia/README.md` table; ATLAS `russia/build_russia.py` (EAST_UKRAINE, Kherson handling); CENSUS Section E.
- **Confidence:** high for the unit list; medium for the Kherson line.

### Idelsk-Uralia (census "Idelsk-Uralia"; native Иделск-Уралия, letter-for-letter transliteration; capital Nizhny Novgorod; placeholder name, from the 1918 Idel-Ural project, gloss "Volga-Uralia")
- **Consists of:**
  - Russia (pre-war), 26 whole units. Volga-Urals core: Bashkortostan, Tatarstan, Udmurtia [source "Udmurt"], Chuvashia [source "Chuvash"], Mari El [source "Mariy-El"], Mordovia, Kirov, Nizhny Novgorod [source "Nizhegorod"], Penza, Samara, Saratov, Ulyanovsk, Orenburg, Perm Krai, Sverdlovsk, Chelyabinsk, Kurgan. Four ex-Russia-core oblasts: Ivanovo, Kostroma, Vladimir, Yaroslavl. North: Arkhangelsk, Nenets Autonomous Okrug, Komi, Vologda. Final addition (Europe C-15, 2026-09-30): Murmansk Oblast (exclave, reached across the White Sea throat).
- **Left out / lost by old countries:** pre-war Russia loses these 26 units to this nation.
- **Notes:** Murmansk was a separate proto-nation "Karelia" (with Karelia Republic) in the CSV and the PROGRESS TRACKER; C-15 sent Murmansk here. The tracker's "27 subdivisions" figure is stale; the CSV has 25 plus Murmansk = 26 (ATLAS counts 26). Nenets AO is geographically inside Arkhangelsk but is its own listed unit.
- **Source:** XFE `Russia/subdivisions.csv` (nation = Idelsk-Uralia, 25 rows); ATLAS `russia/build_russia.py` (`final_nation`: Murmansk) and README; `Russia/PROGRESS TRACKER` (tracker note on Europe C-15).
- **Confidence:** high.

### Donska-Kubania (census "Donska-Kubania"; native Донска-Кубания; capital Rostov-on-Don; placeholder name, from the 1918 Don Republic and Kuban People's Republic)
- **Consists of:**
  - Russia (pre-war), 7 whole units: Krasnodar Krai, Adygea [source "Adygey"], Rostov, Stavropol Krai, Kalmykia [source "Kalmyk"], Astrakhan, Volgograd.
  - Ukraine (pre-war), 2 units: Crimea (Autonomous Republic of Crimea) and Sevastopol (city), both whole, as an Autonomous Zone inside Donska-Kubania.
- **Left out / lost by old countries:** Russia loses 7 units; Ukraine loses Crimea and Sevastopol (author, 2026-09-30; reason: Crimea was an autonomous unit for nearly all of the Ukrainian period).
- **Notes:** The Crimea Autonomous Zone is the only autonomous zone in the Russia data; its name, capital, powers and Crimean Tatar representation are open, and Sevastopol going with Crimea is an assumption (the author spoke of Crimea only). The nation is multipart (the Crimean Peninsula is separated from the mainland by the Kherson left bank, which is Russia core's, touching at the isthmus).
- **Source:** XFE `Russia/subdivisions.csv` (nation = Donska-Kubania, 9 rows); `Russia/CHANGES.md` (Crimea entry, 2026-09-30); ATLAS `russia/README.md` and `build_russia.py` (`autonomous_zones` layer).
- **Confidence:** high; medium for Sevastopol.

### Künnarantaiga (census "Künnarantaiga"; native Күннарантайга; ASCII form Kunnarantaiga; capital Vladivostok; "Land of the Sunlit Taiga", author-invented compound of Yakut and Buryat words; formerly "Country A")
- **Consists of:** Russia (pre-war), 12 whole units: Sakha (Yakutia), Amur, Buryatia [source "Buryat"], Zabaykalsky Krai [source "Chita"], Chukotka Autonomous Okrug [source "Chukchi Autonomous Okrug"], Kamchatka, Khabarovsk Krai, Magadan [source "Maga Buryatdan"], Primorsky Krai [source "Primor'ye"], Sakhalin (with the Kuril Islands, as Natural Earth carries it), Jewish Autonomous Oblast [source "Yevrey"], Irkutsk.
- **Left out / lost by old countries:** pre-war Russia loses these 12 units. China's "Outer Manchuria" question (Primorye, Khabarovsk, Amur, Jewish AO) is settled here: Russian territory, not Manchuria's.
- **Notes:** Spans Lake Baikal to the Bering Strait; Chukotka crosses the antimeridian. The Baikal-partition idea (splitting off Irkutsk, Buryatia, Zabaykalsky) was researched and rejected; the nation stays whole. Sakhalin and the Kurils were a seam the East Asia data left empty (it does not claim them for Japan).
- **Source:** XFE `Russia/subdivisions.csv` (nation = Künnarantaiga, 12 rows); `Russia/PROGRESS TRACKER` (Baikal item); `Asia/Asia (East)/README.md` (seams); ATLAS `russia/README.md`.
- **Confidence:** high.

### Siberia (census "Siberia"; native Сибирь; capital Novosibirsk)
- **Consists of:** Russia (pre-war), 11 whole units: Khakassia [source "Khakass"], Krasnoyarsk Krai, Altai Krai [source "Altay"], Altai Republic [source "Gorno-Altay"], Kemerovo, Khanty-Mansi Autonomous Okrug [source "Khanty-Mansiy"], Novosibirsk, Omsk, Tomsk, Tyumen, Yamalo-Nenets Autonomous Okrug [source "Yamal-Nenets"].
- **Left out / lost by old countries:** pre-war Russia loses these 11 units; Tuva (inside the old Siberian Federal District) is a separate nation, and Irkutsk went to Künnarantaiga.
- **Notes:** Western Siberia plus Eastern Siberia minus Irkutsk and Tuva. The world-atlas merge also adds a 38 km2 sliver to Siberia (geometry only).
- **Source:** XFE `Russia/subdivisions.csv` (nation = Siberia, 11 rows); `Russia/PROGRESS TRACKER` table; ATLAS `russia/README.md`.
- **Confidence:** high.

### Chechnya (census "Chechnya"; native Чечня; capital Grozny)
- **Consists of:** Russia (pre-war): Chechen Republic [source "Chechnya"] (whole).
- **Left out / lost by old countries:** pre-war Russia loses this one unit.
- **Notes:** Independent, unchanged from the original 20-nation map.
- **Source:** XFE `Russia/subdivisions.csv` (1 row); ATLAS `russia/build_russia.py` NOTE.
- **Confidence:** high.

### Dagestan (census "Dagestan"; native Дагестан; capital Makhachkala)
- **Consists of:** Russia (pre-war): Republic of Dagestan (whole).
- **Left out / lost by old countries:** pre-war Russia loses this one unit.
- **Notes:** ~30 recognized peoples and no ethnic majority, kept whole under the whole-first-order-unit rule. Drawn as a multipart polygon in the atlas.
- **Source:** XFE `Russia/subdivisions.csv` (1 row, note column); ATLAS `russia/README.md`.
- **Confidence:** high.

### Ingushetia (census "Ingushetia"; native Ингушетия; capital Magas; largest city Nazran)
- **Consists of:** Russia (pre-war): Republic of Ingushetia [source "Ingush"] (whole).
- **Left out / lost by old countries:** pre-war Russia loses this one unit.
- **Notes:** Independent, unchanged.
- **Source:** XFE `Russia/subdivisions.csv` (1 row); `Russia/PROGRESS TRACKER`.
- **Confidence:** high.

### Kabardino-Balkaria (census "Kabardino-Balkaria"; native Кабардино-Балкария; capital Nalchik)
- **Consists of:** Russia (pre-war): Kabardino-Balkar Republic [source "Kabardin-Balkar"] (whole).
- **Left out / lost by old countries:** pre-war Russia loses this one unit.
- **Notes:** Independent; the provisional "[P]" marker was removed (confirmed independent).
- **Source:** XFE `Russia/subdivisions.csv` (1 row); `Russia/PROGRESS TRACKER`.
- **Confidence:** high.

### North Ossetia-Alania (census "North Ossetia-Alania"; native Северная Осетия — Алания; capital Vladikavkaz)
- **Consists of:** Russia (pre-war): Republic of North Ossetia-Alania [source "North Ossetia"] (whole).
- **Left out / lost by old countries:** pre-war Russia loses this one unit. (South Ossetia is a separate "contested" entry in the West Asia/South Caucasus data, a Georgian-side region; it is not part of this nation.)
- **Notes:** Independent; "[P]" removed.
- **Source:** XFE `Russia/subdivisions.csv` (1 row); `Russia/PROGRESS TRACKER`; ATLAS `west-asia/README.md` (South Ossetia).
- **Confidence:** high.

### Karachay-Cherkessia (census "Karachay-Cherkessia"; native Карачаево-Черкесия; capital Cherkessk)
- **Consists of:** Russia (pre-war): Karachay-Cherkess Republic [source "Karachay-Cherkess"] (whole).
- **Left out / lost by old countries:** pre-war Russia loses this one unit. Adygea (a neighboring Circassian republic) went to Donska-Kubania, not here.
- **Notes:** Independent; confirmed in a follow-up message after being left off the author's first list.
- **Source:** XFE `Russia/subdivisions.csv` (1 row); `Russia/PROGRESS TRACKER`.
- **Confidence:** high.

### Tuva (census "Tuva"; native Тыва; capital Kyzyl)
- **Consists of:** Russia (pre-war): Tuva Republic (whole).
- **Left out / lost by old countries:** pre-war Russia loses this one unit (it does not go to Mongolia or Siberia).
- **Notes:** 88.7% Tuvan; canon economic agreement with Mongolia, no border change (narrative only).
- **Source:** XFE `Russia/subdivisions.csv` (1 row); ATLAS `russia/build_russia.py` NOTE; `Russia/PROGRESS TRACKER`.
- **Confidence:** high.

### Other nations the Russia data define
- **Finland (Karelia piece):** the Republic of Karelia (whole), joined to Finland at Europe map C-15 (2026-09-30); the CSV's proto-nation "Karelia" no longer exists. The rest of Finland is in the Europe region. CENSUS lists Finland among Russia's successors.
- **Kaliningrad:** not in the Russia CSV. The Europe region draws it as its own country (the former oblast, majority Russian, a founding Confederacy of Intermarium Nations member with Lithuania). The CENSUS Russia row does not name it (gap, see end).
- **Ukraine (remainder):** the Europe region keeps Ukraine without the eastern slice and Crimea (a Confederacy member).

---

## CENTRAL ASIA (only Kazakhstan was asked for; its neighbors listed at the end of this section)

### Kazakhstan (census "Kazakhstan"; native name not in the sources; capital Astana)
- **Consists of:** Kazakhstan (pre-war), 21 first-order units, all whole: Akmola, Aktobe, Almaty Region, Atyrau, East Kazakhstan, Jambyl, Karaganda, Kostanay, Kyzylorda, Mangystau, North Kazakhstan, Pavlodar, Turkistan, Abai, Jetisu, Ulytau, West Kazakhstan, plus the cities of republican significance Astana, Almaty City, Shymkent, and Baikonur (Russian-leased cosmodrome enclave, through 2050).
- **Left out / lost by old countries:** nothing is lost or gained: Kazakhstan keeps its whole territory. No Russian unit goes to Kazakhstan.
- **Notes:** The 2022 region split (Abai, Jetisu, Ulytau) is counted; Baikonur is Kazakh sovereign territory under foreign administration (not a lost unit). Natural Earth carries only 16 of the 21 units; the land is complete (Baikonur is folded into Kyzylorda in the atlas geometry). Renamed in the data from "The Kazakh Steppe" to Kazakhstan.
- **Source:** NATIONS `central-asia-map-data/regions.csv` (row `kazakhstan`, 2026-09-29) and README; ATLAS `west-asia/README.md` and `build_west-asia.py` (`CA_ASSIGN`); CENSUS Section E (Kazakhstan added 2026-11-02).
- **Confidence:** high.

### Other nations the Central Asia data define (one line each)
- **Kyrgyzstan:** Chuy, Naryn, Talas, Issyk-Kul, Bishkek (Batken, Jalal-Abad, Osh Region and Osh City go to the Fergana Valley region).
- **Uzbekistan:** Bukhara, Jizzakh, Navoiy, Qashqadaryo, Samarkand, Sirdaryo, Surxondaryo, Tashkent Region, Khorazm, Tashkent City (minus Karakalpakstan and the three Fergana units).
- **Karakalpakstan:** Uzbekistan's Karakalpakstan as an Autonomous Zone that stays part of Uzbekistan (settled 2026-09-28).
- **Fergana Valley (Uncertain Territory):** cross-border region of Uzbekistan's Fergana, Andijan, Namangan plus Kyrgyzstan's Batken, Jalal-Abad, Osh Region/Osh City, with eight named point enclaves.
- **Tajikistan:** whole (Khatlon, Districts of Republican Subordination, Sughd, Dushanbe, Gorno-Badakhshan as Pamiri "domain").
- **Turkmenistan:** whole (Ahal, Balkan, Dashoguz, Lebap, Mary, Ashgabat).
- **Rest of West Asia (data in ATLAS `west-asia/`, not asked for):** Afghanistan (minus Nimruz), Balochistan (Iran's Sistan and Baluchestan, Pakistan's Baluchistan province, Afghanistan's Nimruz), Persia (Iran), Kurdistan (cross-border), Turkey (without East Thrace), Syria, Lebanon, Jordan, Palestine, Jerusalem (neutral city), Iraq, Kingdom of Nejd and Hejaz (Saudi Arabia + Kuwait + Bahrain), Qatar, Oman, United Arab Emirates, North Yemen, South Yemen (with Socotra), Dhale and Khuzestan (disputed), Georgia, Abkhazia (contested), South Ossetia (contested, no polygon), Azerbaijan, Armenia.

---

## EAST ASIA (final state = map F, 2267 to present: eight sovereign nations plus the neutral Jeju-do)

Pre-war China's 34 provincial-level units (31 mainland plus Hong Kong and Macau, with Taiwan separate in the data) are assigned as follows. The data keeps whole first-order units only; no province is split.

### Sinian Federation (census "Sinian Federation"; native 震旦联邦 Zhendan Lianbang; colloquial "the Iron Federation"; formed 2179)
- **Consists of:** China (pre-war), 27 units, all whole: 25 provinces and province-level municipalities plus Hong Kong and Macau, grouped in the nine Han member states:
  - Zhongyuan 中原 (5): Beijing, Tianjin, Hebei, Shandong, Henan.
  - Qin 秦 (4): Shaanxi, Gansu, Ningxia, Qinghai (Qinghai merged into Qin in 2131).
  - Bashu 巴蜀 (5): Sichuan, Chongqing, Hubei, Yunnan, Guizhou.
  - Jin 晋 (1): Shanxi.
  - Wu 吴 (4): Shanghai, Zhejiang, Jiangsu, Anhui.
  - Gan 赣 (1): Jiangxi.
  - Xiang 湘 (1): Hunan.
  - Min 闽 (2): Fujian, Hainan.
  - Yue 粤 (4): Guangdong, Guangxi, Hong Kong (S.A.R.), Macau (S.A.R.).
- **Left out / lost by old countries:** China loses Liaoning, Jilin, Heilongjiang (to Manchuria), Inner Mongol (to Mongolia), Xinjiang (to East Turkestan), Xizang (to Tibet). Taiwan is a separate polity (Natural Earth admin-0 "Taiwan"), not taken from China in the data.
- **Notes:** Hong Kong and Macau are in Yue (CENSUS confirms both go to the Sinian Federation). Hainan is in Min and Qinghai in Qin, not in Tibet. The southern-border question was settled by the author on 2026-09-23 (Option A: Yunnan, Guizhou, Guangxi, Gansu, Hainan, Ningxia are all in). Hakka (44 million people) are non-territorial and have no unit. The Paracel and Spratly islands are NOT assigned by the data (see gaps).
- **Source:** XFE `Asia/Asia (East)/asia-east-current.zip` -> `data/province_assignments.csv` (`owner_map_f` = SIN, 27 rows) and `data/polities.csv`; `Asia/Asia (East)/README.md` (settled facts) and `Timeline_Reasoning.md`; ATLAS `east-asia/README.md` and `build_east-asia.py` (HAN list); NATIONS `east-asia-map-data/01 INIT/UPDATE 03` and `UPDATE 04`; CENSUS Section E.
- **Confidence:** high.

### Manchuria (census "Manchuria"; native 满洲 Manzhou; never joins the Federation)
- **Consists of:** China (pre-war): Liaoning, Jilin, Heilongjiang (all whole).
- **Left out / lost by old countries:** China loses these three provinces. Outer Manchuria (Primorye, Khabarovsk, Amur, Jewish AO) is Russian (Künnarantaiga), not Manchuria. An early INIT proposal (2026-09-23) listed five eastern Inner Mongolian prefectures (Hulunbuir, Hinggan, Tongliao, Chifeng, Xilin Gol) as a Manchurian "domain"; the later final data puts all of Inner Mongol in Mongolia, so they are not Manchuria's.
- **Notes:** The Korean-majority Yanbian area is inside Jilin and so stays in Manchuria. The CENSUS says Manchuria's population share was reduced in the census draw (DR-94); that is a census matter, not a territory change.
- **Source:** XFE `Asia/Asia (East)/asia-east-current.zip` -> `province_assignments.csv` (MAN, 3 rows); ATLAS `east-asia/README.md`; NATIONS `east-asia-map-data/01 INIT/regions-main.csv` (proposal, superseded); CENSUS Section E.
- **Confidence:** high.

### Mongolia (with Inner Mongolia) (census "Mongolia"; native Монгол Улс Mongol Uls)
- **Consists of:** Mongolia (pre-war): the whole state. China (pre-war): Inner Mongol (the Inner Mongolia Autonomous Region, whole).
- **Left out / lost by old countries:** China loses Inner Mongolia to Mongolia (the two merged 2098-2110). Mongolia loses nothing. Buryatia (Russian) and Tuva stay outside.
- **Notes:** The data cuts at the Inner Mongolia boundary, so it is whole-region, not a culture-area line (Mongol populations of Xinjiang and Qinghai are not included). The CENSUS note says "Mongolia (with Inner Mongolia)".
- **Source:** XFE `Asia/Asia (East)/asia-east-current.zip` -> `province_assignments.csv` (MON: `a0:Mongolia`, `a1:China:Inner Mongol`); ATLAS `east-asia/README.md`; CENSUS Section E notes.
- **Confidence:** high.

### East Turkestan (census "East Turkestan"; native شەرقىي تۈركىستان Sherqiy Turkistan; script unverified)
- **Consists of:** China (pre-war): Xinjiang Uyghur Autonomous Region (whole).
- **Left out / lost by old countries:** China loses Xinjiang. The Uyghur diaspora in Kazakhstan, Uzbekistan and Kyrgyzstan is a sphere overlay (S2) in the Central Asia data; no territory moves.
- **Notes:** Never joins the Federation. The Tian Shan is drawn as an internal dashed line in the source maps. Geometry includes whatever Aksai Chin ground Natural Earth gives the Xinjiang unit; the atlas merge hands 1,689 km2 of East Turkestan overlap to Pakistan.
- **Source:** XFE `Asia/Asia (East)/asia-east-current.zip` -> `province_assignments.csv` (ETK, 1 row); ATLAS `east-asia/README.md`; ATLAS `data/world/merge_report.md`.
- **Confidence:** high.

### Tibet (census "Tibet"; native བོད Bod)
- **Consists of:** China (pre-war): Xizang (the Tibet Autonomous Region, whole).
- **Left out / lost by old countries:** China loses Xizang. Qinghai and Tibetan-area counties in Sichuan, Yunnan and Gansu are NOT Tibet's (whole-province rule; Qinghai is in Qin).
- **Notes:** "The Tibet Autonomous Region and nothing else", on all maps. 86% Tibetan. Atlas-merge seam overlaps with South Asian neighbors go to those neighbors (Nepal 4,138 km2, Madhyama 347 km2, Bhutan 208 km2, Arunachal AZ 891 km2).
- **Source:** XFE `Asia/Asia (East)/asia-east-current.zip` -> `province_assignments.csv` (TIB, 1 row); NATIONS `east-asia-map-data/01 INIT/UPDATE 03 - Qinghai Settled.md`; ATLAS `east-asia/README.md`.
- **Confidence:** high.

### Taiwan (census "Taiwan"; native 臺灣 in Traditional characters)
- **Consists of:** Taiwan (pre-war, Natural Earth admin-0 "Taiwan"): the main island with Penghu, Kinmen and Matsu (whole).
- **Left out / lost by old countries:** none; Taiwan is not carved from China in the data and is a separate nation throughout.
- **Notes:** Sovereign on all eight maps. Pratas (Dongsha) and Taiping Island are not mentioned by the sources.
- **Source:** XFE `Asia/Asia (East)/asia-east-current.zip` -> `province_assignments.csv` (TWN: `a0:Taiwan`); ATLAS `east-asia/README.md`; CENSUS Section E.
- **Confidence:** high.

### Korea (census "Korea"; native 한국 Hanguk, unified 2111-2130)
- **Consists of:** North Korea (pre-war): the whole state. South Korea (pre-war): the whole state minus Jeju-do (Jeju Special Self-Governing Province), including Dokdo (Liancourt Rocks).
- **Left out / lost by old countries:** South Korea loses Jeju-do to the neutral zone below. North Korea loses nothing.
- **Notes:** Pre-unification North and South are not separate rows. CONFLICT (flagged): the CENSUS (2026-11-02) assigns Jeju-do's people to Korea ("its people count as Korea's"), while the territory data (map F, ATLAS) makes Jeju-do a neutral zone shared by Korea, Japan and the Sinian Federation, cut out of Korea. The census sentence is about headcount, so both can hold; the territory is not Korea's in the atlas.
- **Source:** XFE `Asia/Asia (East)/asia-east-current.zip` -> `province_assignments.csv` (KOR: `a0:North Korea`; `a0:South Korea MINUS a1:South Korea:Jeju`); ATLAS `east-asia/README.md`; CENSUS Section E notes.
- **Confidence:** high for the land; medium on how Jeju-do should be counted.

### Japan (census names it only as an old country; native 日本 Nihon/Nippon)
- **Consists of:** Japan (pre-war): the whole island chain (Hokkaido, Honshu, Shikoku, Kyushu, the Ryukyus including Okinawa, the Ogasawara and Izu islands), as Natural Earth admin-0 draws it.
- **Left out / lost by old countries:** none. Sakhalin and the Kurils are Russian (Künnarantaiga), not Japan's; the data is silent on any Japanese claim to the southern Kurils.
- **Notes:** No Japanese fragmentation is indicated. Ainu-homeland (Hokkaido) was only ever a "contingent" idea in the early INIT file.
- **Source:** XFE `Asia/Asia (East)/asia-east-current.zip` -> `province_assignments.csv` (JPN: `a0:Japan`); ATLAS `east-asia/build_east-asia.py` NOTE; `Asia/Asia (East)/README.md`.
- **Confidence:** high.

### Other nations the East Asia data define
- **Jeju-do:** neutral zone and three-power condominium (Korea, Japan, Sinian Federation), seat of the International Court of Diplomacy (founded 2267); the single unit Jeju, cut out of South Korea.
- **Zhongyuan, Qin, Bashu, Jin, Wu, Gan, Xiang, Min, Yue:** the nine Han member states of the Sinian Federation (listed above); sovereign states from 2094 to 2178 on earlier maps. Qinghai was a sovereign state until it merged into Qin.
- **Inner Mongolia:** a sovereign state until 2098, then part of Mongolia.
- **Hakka:** non-territorial; no ground.

---

## SOUTHEAST ASIA

### Vietnam (census: not listed as changed; native name not in sources; capital Hanoi)
- **Consists of:** Vietnam (pre-war), 34 units under the post-2025 provincial mergers, all whole: Hà Nội, Huế, Hải Phòng, Đà Nẵng, Hồ Chí Minh City, Cần Thơ, Lai Châu, Điện Biên, Sơn La, Cao Bằng, Lạng Sơn, Quảng Ninh, Thanh Hóa, Nghệ An, Hà Tĩnh, Tuyên Quang, Lào Cai, Thái Nguyên, Phú Thọ, Bắc Ninh, Hưng Yên, Ninh Bình, Quảng Trị, Quảng Ngãi, Gia Lai, Khánh Hòa, Lâm Đồng, Đắk Lắk, Đồng Nai, Tây Ninh, Vĩnh Long, Đồng Tháp, Cà Mau, An Giang.
- **Left out / lost by old countries:** nothing lost or gained.
- **Notes:** Geometry in the atlas is Natural Earth admin-0 Vietnam; the Paracel Islands (disputed with China) are not assigned (see gaps).
- **Source:** XFE `Asia/Asia (Southeast)/subdivisions.csv` (Vietnam, 34 rows); ATLAS `southeast-asia/README.md`.
- **Confidence:** high.

### Thailand (census "Thailand" row; native name not in sources; capital Bangkok)
- **Consists of:** Thailand (pre-war), 74 units (Bangkok plus 73 provinces), all whole: Bangkok, Amnat Charoen, Ang Thong, Bueng Kan, Buriram, Chachoengsao, Chai Nat, Chaiyaphum, Chanthaburi, Chiang Mai, Chiang Rai, Chonburi, Chumphon, Kalasin, Kamphaeng Phet, Kanchanaburi, Khon Kaen, Krabi, Lampang, Lamphun, Loei, Lopburi, Mae Hong Son, Maha Sarakham, Mukdahan, Nakhon Nayok, Nakhon Pathom, Nakhon Phanom, Nakhon Ratchasima, Nakhon Sawan, Nakhon Si Thammarat, Nan, Nong Bua Lamphu, Nong Khai, Nonthaburi, Pathum Thani, Phang Nga, Phatthalung, Phayao, Phetchabun, Phetchaburi, Phichit, Phitsanulok, Phra Nakhon Si Ayutthaya, Phrae, Phuket, Prachinburi, Prachuap Khiri Khan, Ranong, Ratchaburi, Rayong, Roi Et, Sa Kaeo, Sakon Nakhon, Samut Prakan, Samut Sakhon, Samut Songkhram, Saraburi, Satun, Sing Buri, Sisaket, Songkhla, Sukhothai, Suphan Buri, Surat Thani, Surin, Tak, Trang, Trat, Ubon Ratchathani, Udon Thani, Uthai Thani, Uttaradit, Yasothon.
- **Left out / lost by old countries:** Thailand loses Pattani, Yala, Narathiwat to Patani (below).
- **Notes:** Everything else about Thailand is unchanged. Isan is a sphere overlay only (not a border).
- **Source:** XFE `Asia/Asia (Southeast)/subdivisions.csv` (Thailand, 74 rows); ATLAS `southeast-asia/README.md`; NATIONS `mainland-southeast-asia-map-data/README.md` ("The Deep South / Patani Question").
- **Confidence:** high.

### Patani (census "Patani"; source and the Southeast Asia files call it "Deep South"; world atlas renames it "Patani", working name marked for review, author 2026-10-04)
- **Consists of:** Thailand (pre-war): Pattani, Yala, Narathiwat provinces (all whole).
- **Left out / lost by old countries:** Thailand loses these three provinces (separation after the 2083 war, author decision 2026-09-26; independence, not autonomy). Songkhla and Satun stay in Thailand; Malay-majority Kelantan and Terengganu stay in Malaysia (linked only by the cross-map "Patani Malay World" sphere).
- **Notes:** No capital in the source. A later union with Malaysia was left open as an unbuilt possibility. Final name still open.
- **Source:** XFE `Asia/Asia (Southeast)/subdivisions.csv` (nation = "Deep South", 3 rows, notes on Narathiwat); ATLAS `southeast-asia/README.md`; ATLAS `z-full-world-atlas/README.md` (Patani rename) and `scripts/merge_world.py`; CENSUS Section E.
- **Confidence:** high for the land; the name is a working name.

### Indonesia (census "Indonesia" row; native name not in sources; capital Nusantara, East Kalimantan, per the maritime DESIGNATIONS file)
- **Consists of:** Indonesia (pre-war), 31 provinces, all whole: North Sumatra, West Sumatra, Riau, Jambi, South Sumatra, Bengkulu, Lampung, Bangka Belitung Islands, Riau Islands, Special Capital Region of Jakarta, West Java, Central Java, Special Region of Yogyakarta, East Java, Banten, West Kalimantan, Central Kalimantan, South Kalimantan, East Kalimantan, North Kalimantan, North Sulawesi, Central Sulawesi, South Sulawesi, Southeast Sulawesi, Gorontalo, West Sulawesi, Maluku, North Maluku, Bali, West Nusa Tenggara, East Nusa Tenggara. (Island blocs: Sumatra 9 (without Aceh), Java 6, Kalimantan 5, Sulawesi 6, Maluku 2, Nusa Tenggara and Bali 3.)
- **Left out / lost by old countries:** Indonesia loses Aceh (1 province, to Aceh) and the six Papua-region provinces (to West Papua); the 38 provinces are all accounted for (31 + 1 + 6).
- **Notes:** Timor-Leste's Oecusse-Ambeno exclave sits inside Indonesian West Timor (East Nusa Tenggara). North Kalimantan and the 2022-23 Papua splits are counted as currently in force.
- **Source:** XFE `Asia/Asia (Southeast)/subdivisions_maritime.csv` (Indonesia, 31 rows); NATIONS `maritime-southeast-asia-map-data/README.md` (bloc table) and DESIGNATIONS; ATLAS `southeast-asia/README.md` and `build_southeast-asia.py` (`bloc_of`).
- **Confidence:** high.

### Aceh (census "Aceh"; native name not in sources; capital not stated, Banda Aceh is a city marker only)
- **Consists of:** Indonesia (pre-war): Aceh Province (whole).
- **Left out / lost by old countries:** Indonesia loses Aceh (author decision 2026-09-26).
- **Notes:** Called an Autonomous Zone in the source (drawn as its own hard-bordered nation-tier polygon, with a hatch overlay, the same tier as Latin America's Araucanía-Patagonia Autonomous Zone); the CENSUS lists it as a successor row of Indonesia. Whether it is a full nation or an Autonomous Zone inside a larger frame is a naming-tier question the sources leave as "Autonomous Zone, drawn as a nation".
- **Source:** XFE `Asia/Asia (Southeast)/subdivisions_maritime.csv` (Aceh, 1 row + note); ATLAS `southeast-asia/README.md` (kind = autonomous zone); CENSUS Section E.
- **Confidence:** high for the land; medium for the tier label.

### West Papua (census "West Papua"; native name not in sources; capital not stated, Jayapura is a city marker)
- **Consists of:** Indonesia (pre-war), 6 provinces, all whole: Papua, West Papua [Papua Barat], Central Papua, Highland Papua, South Papua, Southwest Papua.
- **Left out / lost by old countries:** Indonesia loses all six Papua-region provinces. Papua New Guinea (east of the 141st meridian) is separate and unchanged (Oceania).
- **Notes:** "West Papua" here is the whole six-province bloc, not only the administrative province Papua Barat. Home of the Grasberg mine (Central Papua).
- **Source:** XFE `Asia/Asia (Southeast)/subdivisions_maritime.csv` (West Papua, 6 rows + notes); NATIONS `maritime-southeast-asia-map-data/README.md`; ATLAS `southeast-asia/README.md`.
- **Confidence:** high.

### Malaysia (census "Malaysia" not in the successor table; native name not in sources; capital Kuala Lumpur)
- **Consists of:** Malaysia (pre-war), 16 units, all whole: Johor, Kedah, Kelantan, Malacca, Negeri Sembilan, Pahang, Penang, Perak, Perlis, Selangor, Terengganu, Sabah, Sarawak, Kuala Lumpur, Labuan, Putrajaya.
- **Left out / lost by old countries:** nothing lost or gained.
- **Notes:** Sarawak is a sub-country Autonomous Zone inside Malaysia (author decision 2026-09-26; dashed border, NOT a separate row). Sabah stays an ordinary state (settled 2026-09-26). The Philippines' claim to Sabah (via Sulu) is a live dispute the data does not resolve. Labuan, Kuala Lumpur and Putrajaya are Federal Territories.
- **Source:** XFE `Asia/Asia (Southeast)/subdivisions_maritime.csv` (Malaysia, 16 rows + notes); ATLAS `southeast-asia/README.md` ("How the tables split the countries").
- **Confidence:** high.

### Philippines (census: not listed as changed; native name not in sources; capital Manila)
- **Consists of:** Philippines (pre-war), 18 regions, all whole: National Capital Region (NCR), Cordillera Administrative Region (CAR), Ilocos Region (I), Cagayan Valley (II), Central Luzon (III), Calabarzon (IV-A), Mimaropa, Bicol Region (V), Western Visayas (VI), Negros Island Region (NIR), Central Visayas (VII), Eastern Visayas (VIII), Zamboanga Peninsula (IX), Northern Mindanao (X), Davao Region (XI), Soccsksargen (XII), Caraga (XIII), Bangsamoro Autonomous Region in Muslim Mindanao (BARMM).
- **Left out / lost by old countries:** nothing lost or gained.
- **Notes:** BARMM is an ordinary autonomous region (Basilan, Lanao del Sur, Maguindanao del Norte, Maguindanao del Sur, Tawi-Tawi, plus Cotabato City); Sulu is excluded from it and sits in Zamboanga Peninsula (Executive Order No. 91, 2025). The Negros Island Region (2024) is counted. Natural Earth admin-1 is older; the scripts' own corrections define the units.
- **Source:** XFE `Asia/Asia (Southeast)/subdivisions_maritime.csv` (Philippines, 18 rows + notes); ATLAS `southeast-asia/README.md`.
- **Confidence:** high.

### Other nations the Southeast Asia data define
- **Myanmar (15 whole units, no split):** Shan, Rakhine, Kachin, Mon, Kayin, Chin, Kayah, Yangon, Mandalay, Sagaing, Ayeyarwady, Bago, Magway, Tanintharyi, Nay Pyi Taw.
- **Laos (18):** Vientiane Prefecture, Attapeu, Bokeo, Bolikhamxai, Champasak, Houaphanh, Khammouane, Luang Namtha, Luang Prabang, Oudomxay, Phongsaly, Sainyabuli, Salavan, Savannakhet, Sekong, Vientiane, Xaisomboun, Xiangkhouang.
- **Cambodia (25):** Phnom Penh, Banteay Meanchey, Battambang, Kampong Cham, Kampong Chhnang, Kampong Speu, Kampong Thom, Kampot, Kandal, Kep, Koh Kong, Kratié, Mondulkiri, Oddar Meanchey, Pailin, Preah Sihanouk, Preah Vihear, Prey Veng, Pursat, Ratanakiri, Siem Reap, Stung Treng, Svay Rieng, Takéo, Tboung Khmum.
- **Singapore:** one unit, whole city-state.
- **Brunei (4 districts):** Brunei-Muara, Belait, Temburong, Tutong (Temburong is separated from the rest by Sarawak territory).
- **Timor-Leste (14, including the Oecusse-Ambeno exclave and Atauro):** Aileu, Ainaro, Atauro, Baucau, Bobonaro, Covalima, Dili, Ermera, Lautém, Liquiçá, Manatuto, Manufahi, Oecusse-Ambeno, Viqueque.

---

## OCEANIA

### Australia (census: not listed as changed; native name not in sources; capital Canberra)
- **Consists of:** Australia (pre-war), 14 units, all whole: Australian Capital Territory, Jervis Bay Territory, Lord Howe Island, Macquarie Island, New South Wales, Northern Territory, Queensland, South Australia, Tasmania, Victoria, Western Australia, Ashmore and Cartier Islands, Coral Sea Islands, Norfolk Island.
- **Left out / lost by old countries:** nothing lost or gained.
- **Notes:** Australia stays unified (author's hypothesis supported by research: coastal settlement pattern; Western Australia's 1933 secession vote flagged as the strongest counter-case). Norfolk Island is folded in at lower confidence than Ashmore and Cartier and the Coral Sea Islands. The Australian Antarctic claim is not drawn in this region. The world-atlas merge also gives Australia Heard Island and small unassigned slivers (494 km2) by name match.
- **Source:** XFE `Oceania/subdivisions.csv` (Australia, 14 rows + notes); NATIONS `oceania-map-data/README.md`; ATLAS `oceania/README.md`; `z-full-world-atlas/README.md` (Heard Island).
- **Confidence:** high.

### New Zealand (census: not listed as changed; native name not in sources; capital Wellington)
- **Consists of:** New Zealand (pre-war), 24 units, all whole: Antipodes Islands, Auckland, Auckland Islands, Bay of Plenty, Campbell Islands, Canterbury, Chatham Islands Territory, Gisborne District, Hawke's Bay, Kermadec Islands, Manawatu-Wanganui, Marlborough District, Nelson City, Northland, Otago, Southland, Taranaki, Tasman District, The Snares, Three Kings Islands, Tokelau, Waikato, Wellington, West Coast.
- **Left out / lost by old countries:** nothing lost or gained.
- **Notes:** New Zealand stays independent and unified (declined the 1901 Australian federation). Tokelau (a pre-war territory) is included as a region. Cook Islands and Niue (free-association states) and Pitcairn (UK) are separate provisional nations in the data, with the author free to fold the Cook Islands and Niue into New Zealand or tie Pitcairn to it (open). The Ross Dependency is not drawn here.
- **Source:** XFE `Oceania/subdivisions.csv` (New Zealand, 24 rows); ATLAS `oceania/README.md` (caveats); NATIONS `oceania-map-data/README.md`.
- **Confidence:** high.

### Other nations the Oceania data define (one line each; 23 rows in total)
- **Papua New Guinea (20 provinces, with Bougainville as North Solomons):** Central, Chimbu, East New Britain, East Sepik, Eastern Highlands, Enga, Gulf, Madang, Manus, Milne Bay, Morobe, National Capital District, New Ireland, North Solomons, Northern, Sandaun, Southern Highlands, West New Britain, Western, Western Highlands.
- **Melanesia:** Fiji (5 divisions incl. Rotuma), Solomon Islands (10), Vanuatu (6), New Caledonia (3; provisional, pre-war French).
- **Micronesia:** Micronesia (Chuuk, Kosrae, Pohnpei, Yap), Marshall Islands (Ratak and Railik chains), Palau (16 states), Nauru (14 districts), Kiribati (whole, with the Phoenix and Line Islands), Guam (provisional), Northern Mariana Islands (provisional; Northern Islands, Rota, Saipan, Tinian).
- **Polynesia:** Samoa (11 districts), American Samoa (provisional; may reunify with Samoa), Tonga (5), Tuvalu, Cook Islands (provisional), Niue (provisional), French Polynesia (provisional; 5 island groups), Wallis and Futuna (provisional), Pitcairn Islands (provisional).
- **Not in this region:** Hawaii (North America data; Midway is outside Hawaii in the Oceania source).

---

## Pre-war countries, where each part went

| Pre-war country | Where each part went |
|---|---|
| **China** (34 provincial-level units, mainland 31 plus HK and Macau) | Sinian Federation: Beijing, Tianjin, Hebei, Shandong, Henan (Zhongyuan); Shaanxi, Gansu, Ningxia, Qinghai (Qin); Sichuan, Chongqing, Hubei, Yunnan, Guizhou (Bashu); Shanxi (Jin); Shanghai, Zhejiang, Jiangsu, Anhui (Wu); Jiangxi (Gan); Hunan (Xiang); Fujian, Hainan (Min); Guangdong, Guangxi, Hong Kong, Macau (Yue). Manchuria: Liaoning, Jilin, Heilongjiang. Mongolia: Inner Mongol. East Turkestan: Xinjiang. Tibet: Xizang. (Paracel and Spratly islands: unassigned.) |
| **Hong Kong / Macau** | Sinian Federation (Yue). |
| **Taiwan** | Taiwan (separate throughout). |
| **Mongolia** | Mongolia (whole; gains Inner Mongolia). |
| **Japan** | Japan (whole chain). |
| **South Korea** | Korea, except Jeju-do (neutral zone; people counted as Korea's in the census). Dokdo is in Korea. |
| **North Korea** | Korea (whole). |
| **Russia** (about 85 federal subjects) | Russia (core): 18 units listed above. Idelsk-Uralia: 25 units plus Murmansk. Donska-Kubania: 7 units. Künnarantaiga: 12. Siberia: 11. Tuva: 1. Chechnya, Dagestan, Ingushetia, Kabardino-Balkaria, North Ossetia-Alania, Karachay-Cherkessia: 1 each. Finland: Republic of Karelia. Kaliningrad: its own country in the Europe region (Confederacy of Intermarium Nations member). Crimea and Sevastopol (carried as Russian admin-1 units by Natural Earth; treated by the author as Ukraine's former autonomous unit) are in Donska-Kubania as an Autonomous Zone. |
| **Ukraine** | Russia (core): Luhansk, Donetsk, Kharkiv, Dnipropetrovsk, Zaporizhzhia (whole), Kherson (east of the Dnieper only). Donska-Kubania: Crimea and Sevastopol (Autonomous Zone). The rest of Ukraine stays Ukraine (Europe region). |
| **Kazakhstan** | Kazakhstan (whole, 21 units incl. Baikonur lease). |
| **Indonesia** (38 provinces) | Indonesia: 31 provinces. Aceh: Aceh. West Papua: Papua, West Papua, Central Papua, Highland Papua, South Papua, Southwest Papua. |
| **Thailand** | Thailand: 74 units. Patani: Pattani, Yala, Narathiwat. |
| **Malaysia** | Malaysia (whole, 16 units; Sarawak an Autonomous Zone inside). |
| **Philippines, Vietnam, Myanmar, Laos, Cambodia, Brunei, Singapore, Timor-Leste** | Each whole and unchanged under its own name. |
| **Uzbekistan** | Uzbekistan (10 units), Karakalpakstan (Autonomous Zone inside), Fergana Valley (Fergana, Andijan, Namangan, shared with Kyrgyzstan). |
| **Kyrgyzstan** | Kyrgyzstan (Chuy, Naryn, Talas, Issyk-Kul, Bishkek); Fergana Valley (Batken, Jalal-Abad, Osh). |
| **Tajikistan, Turkmenistan** | Each whole and unchanged. |
| **Australia, New Zealand, Papua New Guinea, Fiji and the other Pacific states** | Each whole under its own name (Pacific territories provisional). |

## Flags, gaps and unresolved items

1. **Patani naming:** the Southeast Asia source files still say "Deep South" (a placeholder). The census and the world atlas say Patani (atlas rename 2026-10-04, marked for review). This table uses Patani with the source name noted.
2. **Jeju-do:** census (2026-11-02) counts its people as Korea's; the territory data (map F) makes it a neutral zone cut out of Korea. Both stated; no ruling found that merges them.
3. **Kaliningrad:** missing from the CENSUS Section E Russia row (which lists Finland, Russia core and eleven others). The Europe data makes it its own country; confirm which census row carries Kaliningrad's people.
4. **Census Ukraine row:** Section E says "Ukraine -> Russia (core state)" only. By the territory data, Crimea and Sevastopol (Donska-Kubania) and the unchanged rest of Ukraine (Europe) are not Russia (core state).
5. **Paracel and Spratly Islands (and Scarborough Shoal):** assigned by neither the East Asia data nor the Southeast Asia data (each says the other should decide). Unresolved.
6. **Kherson left bank:** raion-level cut unsettled; Kherson is the one non-whole first-order unit in the Russia data.
7. **Crimea Autonomous Zone and Sevastopol:** name, capital, powers open; Sevastopol's inclusion assumed.
8. **Russia sub-lists differ by source age:** the PROGRESS TRACKER says Idelsk-Uralia has 27 subdivisions and calls the Russia core "minus 4 oblasts moved to Idelsk-Uralia"; the CSV count is 25 plus Murmansk (the later C-15 change). The XFE CSV header text still says 82 rows (it has 90). The older `NATIONS/russia-map-data/` (original 20 nations) was not used.
9. **Placeholder names:** Idelsk-Uralia and Donska-Kubania are placeholders per the sources; native forms are transliterations.
10. **Native names:** the sources give none for Kazakhstan, the Southeast Asian nations, Oceania nations, Aceh, West Papua, Australia or New Zealand (marked "not in sources" above).
11. **Japan and the Kurils:** data is silent on Japan's claim to the southern Kurils; they ride with Sakhalin in Künnarantaiga because Natural Earth carries them in that unit.
12. **Cook Islands, Niue, Pitcairn, other Pacific territories:** provisional; the author may fold Cook Islands and Niue into New Zealand, tie Pitcairn to it, or reunify American Samoa with Samoa (open).
13. **Aceh tier:** called an Autonomous Zone in the source but listed as a successor country row in the census; the hard-border treatment is intentional per the author.
14. **Hakka and Hui:** non-territorial or dispersed peoples with no unit of their own (the Hui are concentrated in Qin, which holds about 43% of them).
15. **Not covered (out of scope):** South Asia (skipped as instructed), Hawaii, Antarctic claims of Australia and New Zealand (the Tepenia region), Europe except as it touches Russia.

---
