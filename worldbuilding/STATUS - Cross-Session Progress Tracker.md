# STATUS — Cross-Session Progress Tracker

**Read this first in any new session that touches worldbuilding or maps.** Last updated **2026-09-29 —
**South Asia opened as a new region; Stage 1 (frameworks) is DONE for all of it — seven files — and the dividing
line with India is pinned to coordinates.** See §4.9 — read it before doing anything else in this region; it
has an exact scope definition that is easy to get wrong by inference, and a list of author decisions now open. West Asia (Central
Asia + Middle East/Turkey/Afghanistan + South Caucasus) is officially DONE, author-confirmed, immediately
before South Asia was opened. All five pipeline stages complete for all three West Asia sub-packages; two
extensive follow-up rounds (divisions review — dozens of real border/naming/demographic decisions — then
label/legend polish) both closed out. See §4.8 for the full write-up. Previously, as of 2026-09-26, author
confirmed FIVE regions officially done: North America, Latin America (Central + South America), East Asia,
Southeast Asia, and Oceania. Hawaii's North America map inset (corner-box, Pacific Ocean) is also done,
closing out the last open item from the Oceania/Hawaii work. **Still fully untouched:** Russia (Stage 1 done,
see §4.5), Europe, and Africa (which will be "a vastly
enormous undertaking," the author's own words). See §2's table and §7.

BOTH Southeast Asia maps are now ✅ COMPLETE, with TWO official map pairs, matching the East Asia / North
America / Latin America pattern. After the `02 reorganization` round-trip (WebUI render + review, several
fix passes, a WebUI polish pass, and a local geopandas/matplotlib clean-room verification that caught one
real regression a WebUI-only round-trip never surfaced), the region produced **two distinct official
deliverables**, both author-confirmed as intentional, not a false start:
1. **The sphere/mandala version** (hard borders + the Tai Continuum / Isan / Zomia / Khmer Krom / Patani
   Malay World / Maritime Mandala / Overseas Chinese / Linguistic Wallacea overlay) — the thematic version,
   built first. **Its package now lives at `y-files/Map Files/Asia (Southeast)/02 reorganization/04
   follow-up/southeast-asia-nations/`** (plus `southeast-asia-nations.zip`, the two rendered PNGs, and a
   `clean test-run (no context)/` verification record in that same `04 follow-up/` folder) — moved there
   during the national-borders work below; author-confirmed 2026-09-26 this is fine as its resting place,
   already redundantly backed up (also mirrored in `01 initial generations/render_map.py` /
   `render_map_maritime.py`, kept in sync throughout). **Not** sitting in `03 official timeline years/`
   any more — don't go looking for it there.
2. **The national-borders version** (hard borders, nation colors, capitals — no sphere overlay), built as
   the planned public-facing counterpart, arrived sooner than expected. **This is now the one sitting at
   `y-files/Map Files/Asia (Southeast)/03 official timeline years/`** — `mainland_sea_map_national.png` /
   `maritime_sea_map_national.png` at the top level, with the reproducible package (`render_map_national.py`,
   `render_map_maritime_national.py`, both CSV pairs, fonts) in `archive 01/`. Went through several rounds of
   label-position polish (`02 reorganization/06–09 follow-up/`, each with its own `CHANGES.md`) — Thailand,
   Laos, Myanmar, Indonesia and West Papua's name-label positions/sizes were all tuned against real renders
   (including one case, West Papua, where the requested direction was tried, rendered, found to make its
   border clash worse, and reversed) before landing in their final spots.

Indonesia: six-bloc core incl. Maluku, capital Nusantara, West Papua independent, Aceh an Autonomous Zone.
Malaysia stays intact, Sarawak an Autonomous Zone (Sabah ordinary). Thailand's Deep South
(Pattani/Yala/Narathiwat) is its own independent nation after 2083 — the mainland map's first-ever partition
decision — connected to Malaysia's Kelantan/Terengganu via the cross-map sphere "The Patani Malay World" (the
sphere-version map only). **Only the Deep South's final name is still open (Stage 5)** — every other nation on
both maps keeps its real-world name. See §4.3 and §4.4.**

This is the handoff document. It records where every region stands, what is settled, what is open, and the
traps that have already cost time once.

---

## 0. Six things to know before doing anything

1. **⚠️ The web-search budget is PER SESSION, not per day.** 200 `WebSearch` calls. Once exhausted it does
   **not** reset overnight — only a **fresh session** resets it. `WebFetch` is a separate path and keeps
   working; most of the Southeast Asia research was done that way. **If a session will need research, do it
   early.**
2. **⚠️ NEVER write to `TepenianUniverseTimeline` without an explicit instruction naming it.** Standing,
   absolute. Everything staged here migrates there only when conclusively settled, and only when asked.
3. **Whole first-order subdivisions only.** Never split a province, state, region or prefecture. This rule is
   absolute and has shaped every map decision in the project.
4. **The map generation happens in the web UI**, not here. This repo holds the **data and instruction sheets**;
   the rendered output lives outside it at `Doll-Fi/media/y-files/Map Files/<Region>/NN follow-up/`.
5. **Flag uncertainty loudly.** Files here feed a zero-error canon repo. An unflagged guess reads as settled
   fact later. ⚠️ markers are the mechanism, not a stylistic tic.
6. **Research proposes, the author disposes.** Surveys never name nations or draw borders. They set out
   options with costs and mark the decision.

---

## 1. The pipeline

Every region moves through the same five stages.

| Stage | Output | Lives in |
|---|---|---|
| **1. Frameworks survey** | The analytical layer — what replaces first effective settlement | `worldbuilding/extractions/` |
| **2. Material survey** | What the ground holds, and what survives a collapse | `worldbuilding/nations/material-base/` |
| **3. Map data** | CSVs + a README the web UI can act on | `worldbuilding/nations/<region>-map-data/` |
| **4. Generation** | Rendered PNGs + renderer script | `y-files/Map Files/<Region>/` *(outside the repo)* |
| **5. Naming** | Placeholders → canon names | — **not yet done anywhere** |

---

## 2. Status by region

| Region | Frameworks | Material | Map data | Generated | Named |
|---|---|---|---|---|---|
| **North America** ✅ DONE | ✅ *(Woodard)* | ✅ 9 nation files | ✅ | ✅ (incl. Hawaii inset, 2026-09-26) | ✅ canon |
| **East Asia** ✅ DONE | ✅ ~23,700 w | ✅ ~21,600 w | ✅ 6-map series | ✅ **all 6, with dates/native text/epoch headers** | ✅ **fully named — MIGRATED TO CANON** |
| **Latin America** ✅ DONE *(Central + South America)* | ✅ | ✅ | ✅ 3 CSVs | ✅ **COMPLETE — rendered and author-verified 2026-09-25** | ✅ Keeps real-world country names throughout; **Amazonia, La República de Yucatán, Saint Martin, and (2026-09-28) the Araucanía-Patagonia Autonomous Zone [APAZ] / La Zona Autónoma de Patagonia y Araucanía [ZAPA] are final, settled names**; ⚠️ **Virgin Islands and French Antilles/Aruba-Curaçao still working names** |
| **Mainland SE Asia** ✅ DONE | ⚠️ ~4,582 w | ⚠️ ~5,668 w | ✅ built 2026-09-26 | ✅ **TWO official pairs** — national-borders in `03 official timeline years/`; sphere version in `02 reorg/04 follow-up/southeast-asia-nations/` | ⚠️ Deep South unnamed |
| **Maritime SE Asia** ✅ DONE | ⚠️ ~5,875 w | ⚠️ ~5,276 w | ✅ 91 rows, Indonesia unified | ✅ **TWO official pairs** — national-borders in `03 official timeline years/`; sphere version in `02 reorg/04 follow-up/southeast-asia-nations/` | ✅ real names |
| **Oceania** ✅ DONE | ⚠️ first pass 2026-09-26 | ❌ | ✅ **built + rendered 2026-09-26** (167 rows, 23 nations) | ✅ **two companion maps, WebUI-confirmed across 3 rounds** (framing fix, flat-color pass) | ❌ Hawaii only (North America canon) |
| **West Asia** ✅ DONE — author's framing: Kazakhstan, the rest of the "-stans," and the Middle East | ✅ Stage 1 done 2026-09-27 for Central Asia + Middle East/Turkey/Afghanistan; ✅ South Caucasus (Georgia/Azerbaijan/Armenia) added 2026-09-28 | ✅ Stage 2 done for all three sub-packages | ✅ Stage 3 done for all three (`central-asia-map-data/`, `middle-east-map-data/`, `south-caucasus-map-data/`) | ✅ Stage 4 done 2026-09-28 for all three, then two full follow-up rounds 2026-09-29 (divisions review §4.8; label/legend polish, `05`–`07 follow-up` folders) — **author-confirmed officially done, 2026-09-29** | ✅ Kurdistan, Persia, Kingdom of Nejd and Hejaz, United Arab Emirates, and every Central Asia country carry final real/historical names; Fergana Valley (Uncertain Territory), Khuzestan (Unstable Territory) and Dhale (Disputed Territory) are deliberately-named unresolved statuses, not placeholders |
| **Russia** — IN PROGRESS | ✅ Stage 1 done 2026-09-27, 3 East Asia seams resolved (§4.5) | ❌ Stage 2 not started — flagged as more load-bearing than usual (Rosstat 12-region breakdown needed) | ✅ **built + rendered locally 2026-09-27** (83 rows, 20 nations, 4 maps — built ahead of Stage 2, 6 nations flagged provisional) | ✅ 4 maps rendered, label collisions fixed round 2 — not yet through WebUI review | ❌ |
| **South Asia** — IN PROGRESS — Pakistan, Nepal, Bangladesh, Bhutan, Sri Lanka (full scope) + one precisely-bounded slice of Northeast India (the rest of India explicitly out of scope) | ✅ Stage 1 done 2026-09-29: six long surveys (Pakistan; Nepal+Bhutan; Bangladesh; Sri Lanka; Northeast India ×2) plus the Siliguri-line scoping file; ⚠️ each carries open author decisions, none chosen | ❌ | ✅ **final country maps 2026-09-29** (`04 follow-up - final maps/`: whole region, Pakistan, Northeast/Madhyama, Sri Lanka) plus first-pass Woodard-style cultural maps: 🟡 **first-pass Woodard-style maps rendered 2026-09-29** — 8 maps (cultural regions, languages, religion, structural tiers, + 4 zooms) in `y-files/Map Files/Asia (South-Central)/01 initial generations/`; staging data in `nations/south-asia-map-data/` (39 regions, 15 spheres, 460 classified district units); not yet reviewed by the author | ❌ |
| **Europe** — Intermarium + Woodard-style cultural research | ✅ Stage 1 done 2026-09-29 (14 notes, now in `y-files/Map Files/Europe/01 initial generations/research/`); Priority 1 current-events check done 2026-09-30 | ❌ | ✅ built 2026-09-30: 1,600 units, 41 regions (40 from the framework + Corsica, added by the author), plus per-unit language and religion classifications, staged next to the renderer in `01 initial generations/map-data/` (not in the repo) | 🟡 **first-pass maps rendered 2026-09-30** — cultural regions (41), seven realms, languages and religion, in `y-files/Map Files/Europe/01 initial generations/`; not yet reviewed by the author | ❌ |
| **Africa** — author's own flag: "will be a vastly enormous undertaking". Split into six folders (2026-10-01): Northwest was split by the author into **Northwest-North** (Morocco, Algeria, Tunisia, Western Sahara, Mauritania, Mali) and **Northwest-South** (Senegal, Gambia, Guinea-Bissau, Guinea, Sierra Leone, Liberia, Burkina Faso, Cote d'Ivoire, Ghana, Togo, Benin, Cabo Verde); Tunisia and Cabo Verde were added to those lists. **Northwest-North started first.** | 🟡 Northwest-North only: continental framework + 3 regional notes (~61,000 words), 2026-10-01, in `y-files/Map Files/Africa/Africa (Northwest-North)/01 initial generations/research/`; the other four sections untouched | ❌ | ✅ Northwest-North: 43 regions, 110 units, staged next to the renderer (not in the repo) | 🟡 Northwest-North first-pass maps rendered 2026-10-01 (regions, 3 realms, languages, religion); not yet reviewed by the author | ❌ |

---

## 3. What is settled — decisions that must not be relitigated

**East Asia — ✅ COMPLETE, migrated to canon 2026-09-24.** Final maps live at
`Doll-Fi/media/Reference/TepenianUniverseTimeline/Worldspace/Locations/Earth/Upper_Earth/Asia_East/`
(author-copied — **that repo is still never to be edited by an agent without an explicit instruction naming
it**, this is just a pointer to where the finished output now lives). The full working package (CSVs, the
renderer, every decision's provenance) stays at
`y-files/Map Files/Asia (East)/08 follow-up - all visuals fully updated/instruction set/` for anyone who needs
to regenerate or further modify the maps later.

- **The Sinian Federation is the Han core**, not PRC borders. Xinjiang, Tibet, Inner Mongolia and Manchuria
  are separate polities.
- **The southern border is Option A** — Yunnan, Guizhou, Guangxi, Gansu, Hainan and Ningxia are **all**
  Federation territory. *Nothing is hatched any more.* Region 10 "Yungui" **never forms.**
- **Qinghai** joins **Qin** in the early era and passes into the Federation at unification. It is **not**
  Tibetan and **not** its own region. **The merged state keeps the name Qin** — territorial absorption doesn't
  require a rename, matching how historical Chinese states (Qin, Han, Tang) grew into the Gansu-Qinghai
  frontier without renaming themselves.
- **Tibet is the TAR and nothing else**, on every map.
- **Manchuria, East Turkestan, Tibet and Taiwan never join the Federation.**
- **Mandarin splits three ways** in the early era — Zhongyuan, Qin, Bashu — with Jianghuai folded into Wu.
- **Hakka has no territory in any era.** Drawn as hatched pockets, never a border.
- **Jeju-do** becomes a three-power condominium (Korea, Japan, the Sinian Federation) on Map F, with **Korean
  taking precedence in any conflict-in-translation.**
- **The map series is a six-map linear sequence, no branches:** `A → B → C → D → E → F` — Mongolia unites →
  Korea unites → Qinghai joins Qin → the Sinian Federation founds → the Court/Jeju-do. The earlier eight-map
  branch structure (`B1`/`B2`, parallel `C`/`D`) is retired; the resolved chronological order made two of
  those eight states never actually occur.
- **All naming is settled**: `NCP` → Zhongyuan, `NW` → Qin, `NKO` → North Korea, `SKO` → South Korea, and
  every polity has a researched native-language name (`震旦联邦` for the Sinian Federation, `한국` for unified
  Korea, etc. — see `Native Names - East Asia Polities.md` in the package folder).
- **Every map now carries its real in-universe years and an epoch name/summary**, overlaid on the map itself —
  the full timeline (2083 war → 2094 → 2098 → 2111 → 2131 → 2179 → 2267 → 2318) is in
  `10 follow-up - timeline years/TIMELINE - East Asia Map Series.md`. This reverses the project's earlier
  "no dates on maps" convention now that the years are genuinely researched rather than guessed.

**Latin America — South America ✅ ACCEPTED AND RENDERED 2026-09-24; Central America/Caribbean not yet
reviewed.** The political-nations map (`map-7-nations.png`) and its `nations-assignment.csv` are filed at
`y-files/Map Files/Latin America/02 reorganization/06 follow-up/` — rendered in the Claude.ai analysis tool
from round 07's `nations.py`, and machine-verified against a hand-built reference CSV: **394/394 rows match
exactly, zero mismatches.** Author confirmed on sight: "South America looks exactly as I envisioned it." The
working package (script, dependencies, instructions) is at `05 follow-up/`, with round 05's and round 06's
own packages preserved inside it as `archive 01/` and `archive 02/`.

- **Argentina survives intact** — roughly its real-world territory, minus whatever the Autonomous Zone below
  takes. Does **not** merge with Uruguay/Paraguay/Central Chile into a "Southern Cone" bloc, reversing that
  part of the draft 12-nation map. Grounded in the survey's own §5.4, which already paired Argentina and
  Chile on "mutual isolation from everyone north of them."
- **Chile survives intact** — its own nation, separate from the Autonomous Zone it co-guarantees. Matches the
  survey's own §12 case: "the most geographically bounded society in the hemisphere," unusually continuous
  state capacity.
- **The Autonomous Zone — borders walked and confirmed 2026-09-24, matching the draft's Region 13 footprint
  exactly (whole first-order subdivisions, per the nations-map rule).** Becomes **one unified autonomous
  zone**, not split between Chile and Argentina. **Jointly recognized and guaranteed by Argentina and
  Chile** — demilitarized (no standing military), otherwise self-governing — echoing the Jeju-do condominium
  model from East Asia. **Takes 1–2 generations after the war to fully form**, not immediate.
  - **Chile contributes:** La Araucanía, Los Ríos, Los Lagos, Aisén del General Carlos Ibáñez del Campo,
    Magallanes y Antártica Chilena.
  - **Argentina contributes:** Neuquén, Río Negro, Chubut, Santa Cruz, Tierra del Fuego.
  - **Dimensions:** roughly **1.13 million km²** (Chile ≈ 339,600 km² + Argentina ≈ 786,000 km²) and roughly
    **5.14 million people** (Chile ≈ 2.57M + Argentina ≈ 2.58M, current real-world census figures used as a
    stand-in). For scale: larger in area than France, with a population in the range of Norway or Costa
    Rica — big enough to be a real polity, not a rump territory.
  - **Real-world grounding, in two distinct layers that justify different halves of the footprint.** The
    **northern half** (La Araucanía, Los Ríos, Neuquén, Río Negro) is grounded in the Mapuche's own
    transnational homeland concept, **Wallmapu**, which already splits the same way across the Andes
    (Gulumapu in Chile, Pwelmapu in Argentina) — an ethnic-homeland argument. The **southern half** (Los
    Lagos, Aisén, Magallanes, Chubut, Santa Cruz, Tierra del Fuego) is grounded instead in geography and
    connectivity: Chilean Patagonia (Aisén, Magallanes) has **no land route to central Chile that doesn't
    cross Argentina**, a real structural reason that periphery drifts out of either state's sole orbit. **Not
    revisited as two separate zones** — kept as one, on the judgment that a single joint condominium is
    simpler to write and administer than two overlapping ones, but the two-different-justifications point is
    worth remembering if the border is ever pressured in-story (the Wallmapu core has an ethnic-homeland case
    for independence the southern periphery does not).
- **Hispaniola is entirely the Dominican Republic**, including its small surrounding islands. **Haiti's
  population effectively went extinct post-war**; the Dominican population expanded to fill the whole island.
  Resolves a tension the survey's own region-5 notes flagged and left open ("Haiti in particular is arguably
  its own object") — not "its own object" any more, just gone. **Not yet applied to
  `nations-assignment.csv`** — apply when the Antilles & Guianas (region 5+6) merger itself gets reviewed, so
  Haiti and the Dominican Republic render as one polity rather than two.
- **Uruguay and Paraguay both stay independent, distinct nations** — settled, consistent with the pattern set
  by Argentina, Chile, the five Caribbean islands, and the Guianas trio.
  - **Paraguay** — the survey's own top candidate for a standalone nation on cultural grounds
    (Guaraní-speaking, Jesuit-mission founding institution, a *Povo Novo* rather than *Povo Transplantado* —
    the opposite tier from every neighbor), reinforced economically: co-owns **Itaipu** (14 GW, shared with
    Brazil, ten of its twenty units run at 50 Hz specifically for Paraguay) and **Yacyretá** (shared with
    Argentina); electricity is Paraguay's **second-largest export** (12.3%, $1.52B) — a position the survey
    notes no other country in the region holds.
  - **Uruguay** — a weaker cultural case (Ribeiro groups it with Argentina in the exact same founding-society
    tier, no real seam), but a strong outcome-based one: called "the Pampas in miniature" in the survey, with
    an unusually well-balanced export base (wood pulp, frozen beef, rice, dairy) and flagged as the one
    country in the whole survey whose Economic Complexity Index runs higher than its size would predict —
    genuinely self-sufficient, food-secure, with its own river frontage and port.
- **Amazonia is a new, trans-national country, capital Manaus — fully settled, walked border by border.**
  Replaces the old draft's region-9-based "Amazonia," and is a genuine break from Brazil rather than a
  Brazil-internal Ribeiro region.
  - **From Brazil (whole states, all seven; this replaces the old Ribeiro four-way Brazil split's
    "Amazônia/Caboclo" entry — Mato Grosso in, Tocantins out):** Roraima, Amazonas, Amapá, Acre, Rondônia,
    Pará, Mato Grosso.
  - **From Peru:** Loreto only. **Ucayali and Madre de Dios stay with Peru** — both are road-connected to the
    rest of the country (the Federico Basadre and Interoceanic highways), unlike Loreto.
  - **From Colombia:** Amazonas, Vaupés, Guainía. **Caquetá, Putumayo, and Guaviare stay with Colombia** — all
    three are road-connected; the other three are not.
  - **From Bolivia:** Pando only. **Beni and Santa Cruz stay with Bolivia.**
  - **From Venezuela:** Amazonas **and** Bolívar. Bolívar is a deliberate exception to the pattern below — an
    industrial, populous, well-connected state (Ciudad Guayana's steel/aluminum, Angel Falls/Canaima), not an
    isolated one, added by explicit author choice rather than the connectivity logic that decided everything
    else.
  - **Ecuador contributes nothing** — none of its Oriente provinces (Sucumbíos, Orellana, Napo, Pastaza,
    Morona Santiago, Zamora Chinchipe) are isolated; Ecuador is small and road-networked even across the
    Andes, so the logic that pulled in Loreto/Leticia/Cobija doesn't apply.
  - **Guyana, Suriname, and French Guiana contribute nothing** — consistent with those three staying fully
    intact as the Guianas trade-union trio (above); none of their sphere-tier interior provinces were ceded.
  - **The governing logic, applied consistently except for the one flagged Bolívar exception:** road isolation
    from the rest of the home country — Iquitos (Loreto) and Leticia (Colombia's Amazonas) have **zero** road
    connection to the rest of their countries; Cobija (Pando) is seasonally impassable by road (30+ hours even
    in the dry season) with a permanent bridge straight to Brazil instead; Vaupés and Guainía's capitals
    (Mitú, Puerto Inírida) are air/river-only. Venezuela's Amazonas (Puerto Ayacucho) is the soft case — one
    paved road to the capital since 1980, but almost the entire rest of the state beyond that is roadless.
  - **Rendered and verified 2026-09-24** — see the round-07 pointer above. Territory unchanged since round
    06's walk; only the surrounding countries' own borders changed shape around it (below).
- **Venezuela survives intact as its own country**, minus Bolívar and Amazonas (both ceded to Amazonia,
  above) — keeps Caracas, Zulia/Maracaibo (its historic oil heartland), the vast majority of the Orinoco Belt
  (the world's largest heavy-oil accumulation, ~20% of proven reserves — Guárico, Anzoátegui, Monagas, Delta
  Amacuro all stay with Venezuela; only a strip of northern Bolívar is lost), the Andes, and ~92% of its
  population. **Deliberate structural consequence, kept rather than fixed:** the Guri Dam (Bolívar state)
  supplied 60–80% of all of Venezuela's electricity pre-collapse — truncated Venezuela is **oil-rich and
  power-poor**, and **negotiates a power trade agreement with Amazonia** to cover the gap, using the same
  cross-border transmission infrastructure that historically already exported Guri's power to Brazil,
  Colombia, and Margarita Island. A real point of post-war leverage/dependency between the two countries, not
  a problem written around.
- **The draft's "Antilles & Guianas" merger (regions 5+6) is dissolved.** It collapsed today's five-plus
  island nations and all three Guianas into one post-war polity; none of that consolidation stands.
  - **Guyana, Suriname, and French Guiana stay three distinct sovereign nations**, bound together by a
    **NAFTA-style trade union**, not merged into one country. **A later evolution into a single unified
    country is left open** as a possible development in the *later* First Interwar Period — explicitly **not**
    the case early on. Grounding: the same offshore oil basin (Guyana's Stabroek Block, Suriname's GranMorgu/
    Block 58), the real, current Guiana Shield Strategic Dialogue among the three, and the Aluku Maroon nation
    already living on both sides of the Suriname/French Guiana border. Case against, noted honestly: three
    different colonial languages (English/Dutch/French) and a genuine Guyana/Suriname border dispute
    (Corentyne River/New River Triangle).
  - **Cuba, the Dominican Republic (all of Hispaniola), Jamaica, Puerto Rico, and Trinidad & Tobago all stay
    separate, distinct nations** in the early First Interwar Period — essentially their real-world borders
    today, not consolidated. **Later mergers among them are left open** as a possible later-period
    development, same caveat as the Guianas.
  - **Partially applied to `nations-assignment.csv` 2026-09-24, South America only** — Guyana, Suriname and
    French Guiana are split out of "ANT" into their own nation codes in `05 follow-up/`. **Cuba, Hispaniola/
    DR, Jamaica, Puerto Rico, Trinidad & Tobago and the rest of the small islands are deliberately left merged
    under "The Antilles"** — that dissolution is Central America/Caribbean-phase work, scoped for later by the
    author, not a gap.
- **The Southern Cone (SCN) is dissolved into four sovereign nations — Argentina, Chile, Uruguay,
  Paraguay.** No territory changed hands beyond what's described above; this is purely re-labeling four
  already-distinct blocks of the old merged draft.
- **⚠️ GOVERNING RULE for South America, settled 2026-09-24 (round 07): a country keeps its own territory
  unless there's a specific, settled reason a piece of it changed hands.** The merged culture-area nations
  that the original Ribeiro-derived draft (and rounds 05/06) still carried — **The Central Andes, The
  Altiplano, Nordeste, Brasil Sudeste, The Sul** — are **retired as political entities.** They remain useful
  as the *analytical* layer that reasoned out where borders might plausibly move (that's what they were always
  for), but they are not nations on the map. As a result:
  - **Ecuador, Peru, Bolivia and Colombia are sovereign again**, each missing only the specific territory
    already settled above as ceded to Amazonia (Ecuador cedes nothing and is untouched).
  - **Brazil is one sovereign nation again**, not three — it keeps every state the old Nordeste/Sudeste/Sul
    split it between, minus the seven whole states already settled above as ceded to Amazonia.
  - **Argentina and Chile each grow back** the provinces the old Altiplano had pulled from them: Argentina
    regains Jujuy, Salta, Tucumán, Catamarca, Santiago del Estero and La Rioja; Chile regains Arica y
    Parinacota and Tarapacá.
  - **Colombia is pulled out of Circum-Caribbean**, closing the "Colombian Andes → Circum-Caribbean" open
    question below — Colombia keeps everything it had, including Nariño, minus only what's ceded to Amazonia.
    *(Circum-Caribbean itself is fully retired as of round 08 — see the Central America block below.)*
- **One question the draft answered by default, not by decision, remains open**: the "Antilles & Guianas"
  dissolution for the Caribbean islands proper (Cuba, Hispaniola, Jamaica, Puerto Rico, Trinidad & Tobago),
  still merged under "The Antilles" on purpose. The other two open questions from this list — Coahuila/Nuevo
  León/Tamaulipas, and the Ladino Corridor — are closed; see the Central America block below.

**Central America — ✅ decided 2026-09-25, round 08 built, not yet rendered.** Package at `y-files/Map Files/
Latin America/02 reorganization/07 follow-up/` (`nations.py`, `regions_geo.py`, `render.py`, a hand-verified
`nations-assignment.csv` transformed from round 06's confirmed output — 394/394 rows, no gaps or duplicates).
Same governing rule as South America: a country keeps its own territory unless there's a specific, settled
reason a piece of it changed hands. **Retires the last three merged culture-area nations on the whole map:
Mesoamerica (for Guatemala's former share), The Ladino Corridor, and Circum-Caribbean** — all three remain
useful as the analytical layer, not as political entities.

- **La República de Yucatán is new, and its name is final/settled** — Chiapas, Tabasco, Campeche, Yucatán and
  Quintana Roo (all five Mexican estados) plus Petén (Guatemala). Eastern border: the Hondo River. Belize stays
  fully intact.
  - *Petén's case*: its entire international border runs against exactly Campeche, Tabasco and Chiapas, not
    the Guatemalan highlands. Its road connection to Guatemala City was worse than its proximity to the
    peninsula until very recently (no road before 1970; unpaved until 1997–99). Last part of the Maya world
    conquered (1697).
  - *Quintana Roo's case*: closes the loop the real 1841–48 Republic of Yucatán already drew — that republic's
    actual territory was exactly Yucatán, Campeche and Quintana Roo.
  - *Chiapas and Tabasco* are the author's own addition to that historical footprint.
  - *Belize's case against*: Corozal and Orange Walk were seriously considered (both were founded by Yucatec
    Maya/Mestizo refugees of the Caste War of Yucatán, 1847–1901), but the author's call is that all of Belize
    stays with Belize.
  - **✅ Native-language name adopted 2026-09-28: "U Kuchkabal Mayab"** (Yucatec Maya). Real linguistic research
    behind it: Yucatec Maya is the peninsula's dominant indigenous language (750,000+ speakers across exactly
    the three Mexican states — Yucatán, Campeche, Quintana Roo — this nation is built from), though under real
    intergenerational-transmission pressure (~60% of children of Maya-speaking mothers no longer learn it).
    **"Mayab" is the real native regional name for the peninsula**, attested from the 16th century — distinct
    from and older than "Yucatán" itself, which is *not* a native Maya word at all (best-supported etymology:
    an original Maya "Yucal Petén," altered by Nahuatl speakers to "Yucaltlan," shortened by the Spanish to
    "Yucatán"). **"Kuchkabal" is the real pre-colonial Maya political term** for an independent province/state/
    polity — the word the Maya themselves used for their own 16-24 independent domains before Spanish
    conquest, a more authentic choice than borrowing "república." The compound uses Yucatec Maya's real
    possessive construction (*u* + possessed noun + possessor, e.g. "u p'ok le paalo'," "that boy's hat") to
    produce "U Kuchkabal Mayab" — "The State/Province of Mayab." **Flagged the same way as Künnarantaiga**:
    built from real, attested vocabulary and grammar, but not itself a historically attested phrase — nobody
    has ever actually called Yucatán this. Applied to `nations.py`'s own YUC entry as documentation.
  - **✅ Map label updated 2026-09-28 — now trilingual (English/Spanish/Maya).** First pass added English
    alongside the already-shown Spanish name; author then asked for the Maya name added too, on both the full
    map and the Mexico/Central America/Caribbean crop. Since Yucatán renders small at this zoomed-out scale,
    the label is floating text over the Gulf of Mexico with a leader line to the peninsula, the same technique
    already used for Guyana/Suriname/French Guiana — "THE REPUBLIC OF YUCATÁN" bold on top, "LA REPÚBLICA DE
    YUCATÁN" smaller italic underneath, "U KUCHKABAL MAYAB" at the same smaller size underneath that,
    matching the APAZ/ZAPA precedent for the top two lines. Both maps genuinely re-rendered (not just
    source-edited) each pass, using the same reconstructed local render environment built for the APAZ fix.
    Two spacing bugs caught and fixed along the way: the English/Spanish lines touched on the first bilingual
    attempt, and the leader line's own start point needed moving down twice (once when Spanish was added,
    again when Maya was) so it always originates below the full label stack rather than cutting through it.
    Old outputs archived (not deleted) at `08 follow-up/archive 08 - pre-Yucatan-bilingual-label/` and
    `archive 09 - bilingual before Maya added/`.
  - **✅ Detail-map-only spacing, finalized 2026-09-28**: author confirmed the full Latin America map's label
    was correct as-is and untouched. On the Mexico/Central America/Caribbean crop specifically, Spanish and
    Maya's positions were confirmed correct first; English was then walked down in four small increments
    (`py + 60000` → `45000` → `35000` → `25000`) until the author confirmed the final spacing — close to the
    practical minimum gap before touching Spanish, but clean. **Final, settled offsets on this map**: English
    `py + 25000`, Spanish `py - 115000`, Maya `py - 204000` (fixed throughout). Old intermediate crops archived
    at `archive 10` through `archive 13` (not deleted) — `archive 13 - pre-third-English-nudge/` holds the
    last pre-final version.
- **Post-war México** keeps everything Mesoamerica had except the five estados above. **Closes the Coahuila/
  Nuevo León/Tamaulipas question** left open in `nations/New North America - Territory Definitions (read from
  map).md` — all three stay with México, no Monterrey-anchored breakaway, no CSA annexation.
  - **La República de Sonora** (Sonora + Chihuahua + Arizona + New Mexico) and **Cascadia** (Baja California +
    Baja California Sur + California) both already had their Mexican shares settled before this round — see
    `nations/México (post-war) - Territory and Open Research.md` for the full partition and the open Jalisco-
    vs-Nuevo-León economic research that came out of it (not settled, parked for later).
- **Guatemala, Belize, El Salvador, Honduras, Nicaragua, Costa Rica and Panama are each sovereign again**, at
  their real-world borders except where noted above (Guatemala loses only Petén). This dissolves The Ladino
  Corridor and Circum-Caribbean completely — no territory anywhere on the map still carries either label.
- **The Miskito Kingdom / Río Coco question was raised and explicitly declined as a border.** The historical
  Miskito Kingdom (1687–1894), split by the Río Coco/Wangks — today's actual Nicaragua/Honduras border — and
  Nicaragua's real autonomous regions (RACCN/RACCS) were seriously considered as a trans-national polity, the
  same tier of case as Amazonia. **Author's explicit call: it becomes a connected Semi-Autonomous Zone in
  character/culture terms, but stays official Nicaraguan and Honduran territory — not a border on this map.**
  Parked for later character work.
- **Not yet rendered.** Needs the same Claude.ai analysis-tool pass South America got — see `INSTRUCTIONS - Run
  in Claude.ai to Render the Map.md` in the round-08 folder.
- **New reference tool**: `map-8-reference-overlay.png` at `y-files/Map Files/Latin America/
  02 reorganization/03 follow-up - reference overlay/` — the same 18-region culture-area layer as `map-1`,
  with modern national borders and names drawn bold on top, for comparing culture areas against today's
  countries while deciding post-war borders.

**The Caribbean islands — ✅ decided 2026-09-25, round 09 built, not yet rendered.** Package at `y-files/Map
Files/Latin America/02 reorganization/08 follow-up/`. **This closes Latin America end to end** — every
first-order subdivision on the whole map, from the US/Mexico border to Cape Horn plus every Caribbean island,
now belongs to a specific nation. Retires the last placeholder bloc anywhere on the map, "The Antilles."
Eighteen nations replace it:

- **Cuba** gains US Naval Base Guantánamo Bay back — a lease reverts once no coherent leasing power stands
  behind it.
- **Dominican Republic** absorbs Haiti — already settled 2026-09-24 (§3 above), applied to the CSV for the
  first time this round.
- **Jamaica** reabsorbs the Cayman Islands and Turks and Caicos — both were literal Jamaican dependencies
  until Jamaica's 1962 independence, when each specifically chose to stay British rather than go independent
  with Jamaica.
- **Antigua and Barbuda** reabsorbs Montserrat — administered as one unit ("Antigua, Barbuda and Montserrat")
  under a single governor, 1816–1871.
- **Anguilla stays independent** rather than rejoining Saint Kitts & Nevis — the deliberate exception to the
  pattern above. Its 1967 split (police evicted, 99.7% referendum for separation) was a revolt against exactly
  that union, not a quiet colonial-era administrative line; undoing it would run against the actual history.
- **"Virgin Islands"** *(working name)* is new — reunifies the US and British Virgin Islands, literally the
  same archipelago (the Danish West Indies) until the US bought only the Danish-held three islands from
  Denmark in 1917.
- **Saint Martin is new, and its name is final.** Reunifies the whole island (divided since the 1648 Treaty of
  Concordia between France and the Netherlands, still functionally borderless today) plus Saint Barthélemy,
  its administrative partner in the same arrondissement of Guadeloupe until 2007. **Official bilingual nation,
  French and Dutch, on the Canadian model** — author-specified 2026-09-25, a character note beyond the border.
- **"French Antilles"** *(working name)* is new — Guadeloupe and Martinique only, once Saint Martin and Saint
  Barthélemy split off on their own.
- **"Aruba-Curaçao"** *(working name)* is new — reunifies two of the three pieces of the old Netherlands
  Antilles federation (dissolved 2010) on shared Papiamento/"ABC islands" identity. Sint Maarten, the
  federation's third piece, went to Saint Martin instead — the single-island case there is stronger.
- **Puerto Rico, Trinidad and Tobago, The Bahamas, Barbados, Dominica, Grenada, Saint Kitts and Nevis, Saint
  Lucia, Saint Vincent and the Grenadines** — no change, already-sovereign real-world nations, applied to the
  CSV for the first time this round (previously decided 2026-09-24 but never actually applied — see §5.1).
- **Not yet rendered, and neither is round 08** — this is the first Claude.ai pass that will test two rounds'
  worth of changes at once. See `INSTRUCTIONS - Run in Claude.ai to Render the Map.md` in the round-09 folder.
- **A second, dedicated map was added this round**, author-requested: `map-mexico-central-america-caribbean.png`
  crops the same data down to just Mexico, Central America and the Caribbean, since that sub-region
  necessarily renders small on the full Latin America map. Same underlying data, no new decisions.

**Mainland Southeast Asia — map data built 2026-09-26, not yet rendered.** Package at
`worldbuilding/nations/mainland-southeast-asia-map-data/` (`subdivisions.csv`, `spheres.csv`, `README.md`).
Unlike North America or Latin America, **this map makes no partition/nation-naming decisions** — Myanmar,
Thailand, Vietnam, Laos and Cambodia are already five real, present-day sovereign countries, and every
subdivision belongs to the country it already belongs to. The only original content is the mandala overlay.

- **Mainland first, maritime later.** Indonesia is to get its **own internal division** when maritime is done.
- **The mandala is carried natively** — cores get hard borders, **spheres overlap and the overlaps are
  correct.** This is the one region where `sphere_territory` does real work.
- **169 first-order subdivisions across the five countries**, all whole units, no splits: Myanmar 15 (7 States
  + 7 Regions + Nay Pyi Taw, fully sourced from the frameworks survey), Thailand 77 (76 provinces + Bangkok),
  Vietnam 34 (28 provinces + 6 centrally-run cities, the 2025-reform list), Laos 18 (17 provinces + Vientiane
  Prefecture), Cambodia 25 (24 provinces + Phnom Penh — **note this corrects the material survey's own "26
  units" arithmetic**, see the map-data README).
- **Four cross-border spheres, not five nations' worth of borders redrawn:** the Tai Continuum (S1, the
  broadest ethnolinguistic layer), Isan/the Lao nation cut by the Thai border (S2 — **flagged as needing a
  real design decision**, since Isan's ~22M ethnic Lao outnumber Laos's own population roughly 3:1, and a flat
  core/domain treatment would bury that finding), Zomia/the Massif (S3, and Laos *is* this sphere rather than
  merely containing it), and the Khmer Krom (S4, Cambodia plus three specific Vietnamese provinces that
  absorbed the historically Khmer-majority delta areas in the 2025 reform).
- **The Wa gets the same treatment East Asia's Hakka already established**: hatched, unbordered, leader-lined,
  its own legend entry — never drawn as its own bordered territory, since it's a second-order subdivision
  inside Shan State and the whole-first-order-subdivision rule is absolute.
- **A Myanmar-specific civil-war control snapshot (mid-2026) exists in the frameworks survey (§3.1) but was
  deliberately not built into the main map** — flagged as dated and fast-changing; left as an author-decidable
  optional second map, not built.
- **Not yet rendered.** Needs the same Claude.ai analysis-tool pass the other regions got.
- **⚠️ Evidence pass, 2026-09-26 — `spheres.csv`'s S3 (Zomia) confidence upgraded on real data, not decided.**
  Vietnam's seven-province list and Thailand's Upper North list both moved from low/medium to high confidence
  against real per-province ethnic-minority census figures (and the 2025-merger provinces, Lào Cai and Tuyên
  Quang, check out on both halves of their mergers). **Tak, Thailand was added** to the Upper North list
  (18–24% hill-tribe population, second only to Mae Hong Son); Lampang and Phrae are flagged as the list's
  weakest members (≤2%). Myanmar's Shan-only Zomia scope now has real evidence for extending to Kachin, Chin,
  Kayah and Kayin too (Scott's own stated scope names Burma generally, not Shan specifically) — **not applied
  to the CSV, left as a strengthened option for the author**; see the frameworks survey's new §2.4.

**Maritime Southeast Asia — frameworks survey built 2026-09-26.** File:
`worldbuilding/extractions/Maritime Southeast Asia - the Austronesian Tier, the Melaka Diaspora and the
Colonial Line (survey).md` (~5,875 words). First-pass reconnaissance, same tier as the mainland survey's own
first pass — **not** a finished analysis. Material survey (Stage 2) and map-data (Stage 3) are separate,
not-yet-started follow-ups.

- **The mandala transfers cleanly** — two of the mainland survey's own seven named mandala examples
  (Srivijaya, Majapahit) were already maritime thalassocracies, so the core/domain/sphere vocabulary needs no
  adaptation to reach this region.
- **Tier-1/tier-2 ethnic identity works almost everywhere** (Austronesian dominates every country in the set),
  **with one total exception: West Papua is ethnically Melanesian**, not Austronesian — a different tier-1
  world sitting inside Indonesia's borders, structurally closer to Tibet's relationship to the Sinian
  Federation than to any border-splitting case in the mainland survey.
- **Java is this survey's Hu Line, but internal rather than border-crossing**: ~56% of Indonesia's population
  on ~7% of its land area. Flagged as the load-bearing fact for how Indonesia's internal division should be
  drawn.
- **⚠️ Recommended (not decided) approach to Indonesia's internal division**, per the author's already-settled
  premise that Indonesia gets one: group the 38 provinces into island-group blocs (Sumatra, Java, Kalimantan,
  Sulawesi, Maluku, Nusa Tenggara+Bali, Papua) rather than the 31-ethnicity tier-2 map, building directly on
  Indonesia's own real 2022 reform that split Papua into four provinces. Aceh and West Papua's cases for
  special treatment within their blocs are real and documented in the survey but left open — sphere overlay,
  hatched autonomous pocket (the Wa/Hakka treatment), or full separate block are all live options.
- **The Philippines' Bangsamoro Autonomous Region in Muslim Mindanao (BARMM)** is this region's "the lines
  already exist" case, the maritime equivalent of Myanmar's ethnic states — five provinces plus Cotabato City,
  already a real, current, first-order-subdivision-respecting autonomous region.
- **Sabah and Sarawak (East Malaysia) carry a documented, current MA63 revenue-sharing grievance** against
  Peninsular Malaysia — the maritime equivalent of Isan, though political/economic rather than a full
  ethnic-nationhood case.
- **Brunei, Singapore and Timor-Leste all need little to no redrawing**: Brunei is a shrunk survivor of a real
  precolonial sultanate (the one place in the region a modern border isn't simply an inherited colonial
  administrative unit); Singapore is a city-state that stays itself; Timor-Leste is already fully and cleanly
  sovereign since 2002, with one geographic curiosity (the Oecusse-Ambeno exclave, inside Indonesian
  territory) worth marking on a future map.
- **✅ RESOLVED, evidence pass 2026-09-26 — the Wallace Line question.** "Linguistic Wallacea" (Schapper, 2015,
  2017) is a real, peer-reviewed ethnolinguistic transition zone, not a loose analogy — but it does **not**
  coincide with biological Wallacea: it's shifted east, excluding Lombok/Sulawesi and reaching further into
  New Guinea's Bird's Head/Cenderawasih Bay. See the frameworks survey's updated §2.2.
- **Evidence pass 2026-09-26 — Aceh/West Papua data added, decision still open.** Aceh is ~70% Acehnese of 5.4M
  (2020 census) — an Austronesian, tier-2 case, not tier-1. West Papua is now roughly 50/50 indigenous
  Melanesian vs. Indonesian-migrant-descended (2.7M total) — real demographic complication for whatever
  overlay treatment gets chosen. See survey §3.1.5's new addendum.
- **⚠️ Still not verified**: the overseas-Chinese population's internal dialect/regional composition per
  country.

**Maritime Southeast Asia — material survey built 2026-09-26.** File:
`worldbuilding/nations/material-base/Maritime Southeast Asia - Material and Economic Base (survey).md`
(~5,276 words). Companion to the frameworks survey above; does not relitigate its ethnic/political analysis.

- **The organizing fact is a strait, not a river**: the **Strait of Malacca** carries an estimated 22–30% of
  world trade and ~29% of global maritime oil trade (~23.2 million barrels/day, H1 2025); China alone routes
  ~80% of its oil imports through it. Singapore's entire economy — the world's 2nd-busiest container port
  (44.66M TEU, 2025), its largest bunkering port, and a top-three global refining center — sits downstream of
  this one fact and has almost no resources of its own. The Sunda and Lombok/Makassar Straits are the only
  alternates, both materially worse (shallow/unsuitable for large ships, or 1,000–2,500 nautical miles longer).
- **Java is confirmed as the load-bearing post-collapse fact for Indonesia's internal division** (per the
  frameworks survey's own recommendation): ~158M people (56% of Indonesia) on ~7% of its land, holding the
  national capital, most of the food/industrial base, and — via the pinisi/Bugis inter-island sailing
  tradition, still a **live commercial freight system today, not a heritage relic** — a working pre-industrial
  fallback for archipelago-wide connectivity that no mainland-country rail network has an equivalent of.
- **Indonesia is a near-monopoly nickel supplier (~67% of world output, 2025)**, the world's largest coal
  exporter by volume, and (via Bangka-Belitung) the tin belt's southern anchor — closing the loop the mainland
  survey left open on where the Southeast Asian tin belt actually ends. **Grasberg (Central Papua)** does for
  West Papua exactly what the Guri Dam does for Bolívar in the Latin America survey: gives the core an
  overwhelming material reason not to let a culturally distinct periphery go.
- **Sabah/Sarawak's MA63 grievance (frameworks survey §3.3) is now quantified**: Sarawak alone holds 60%+ of
  Malaysia's gas reserves and receives a renegotiated ~20% royalty; Sabah receives 5%. East Malaysia holds
  ~60% of the country's land and a small fraction of its population — the demographic mirror of the revenue
  asymmetry.
- **Palm oil (Indonesia + Malaysia, ~85% of world supply) is this region's most infrastructure-fragile major
  export** — unlike rice or fish, it requires centralized milling within 24–48 hours of harvest and an export
  logistics chain to realize any value, with no smallholder/subsistence fallback. Contrasted directly with the
  mainland's uniform rice-surplus picture: **the Philippines is a genuine, structural rice-deficit country**
  (78.1% self-sufficient in 2025, targeting 84% by 2026), an asymmetry the mainland region does not have.
- **Timor-Leste's Bayu-Undan gas field — its original post-independence revenue source, ~$25B in lifetime
  revenue — ceased production in mid-2025.** The country now lives off Petroleum Fund withdrawals (~$18.95B,
  funding 70%+ of the budget) while trying to develop Greater Sunrise (~$50B+ potential). **Not a hypothetical
  post-collapse scenario — this is Timor-Leste's actual current fiscal position.**
- **⚠️ Open items carried forward**: Indonesia's/Malaysia's current rice self-sufficiency ratios (not sourced
  this pass, unlike the Philippines'); Brunei's and Timor-Leste's ECI scores; a depth-comparable treatment of
  the Philippines' own inter-island shipping network versus Indonesia's pinisi tradition; Indonesia's total
  geothermal resource potential beyond installed capacity.

**Maritime Southeast Asia — map-data (Stage 3) built 2026-09-26.** Package at
`worldbuilding/nations/maritime-southeast-asia-map-data/` (`subdivisions.csv`, 90 rows; `spheres.csv`, 3 rows;
`README.md`). Two author decisions unblocked this stage and are applied exactly: Indonesia's internal division
is **island-group blocs** (frameworks survey's own recommendation, confirmed), and **Aceh and West Papua both
get full separate hard-bordered blocks**, not a sphere/overlay treatment.

- **Indonesia is now 8 polities, not 1, on this map**: Sumatra (9 provinces), **Aceh** (1, carved out), Java
  (6), Kalimantan (5), Sulawesi (6), Maluku (2), Nusa Tenggara & Bali (3), **West Papua** (6, carved out) — all
  38 provinces accounted for, none split.
- **West Papua boundary resolved as a judgment call, not asked of the author directly**: the frameworks
  survey uses "West Papua" both as the name of one administrative province (*Papua Barat*) and as shorthand for
  the whole Melanesian Papua-island territory. Resolution: **the entire Papua bloc — all six current
  provinces — is "West Papua"** for this map; there is no separate "Papua bloc minus West Papua" remainder.
  Also corrects the frameworks survey's own undercount there (it named "four provinces post-2022, plus West
  Papua province" — five; the real, current total after the second 2022-23 split is **six**, including
  Southwest Papua). **✅ Author-confirmed 2026-09-26 — see §4.4.**
- **Bangsamoro (BARMM) was NOT one of the author's two decisions** — the map-data package's own judgment
  call, by analogy to Myanmar's ethnic-state treatment on the mainland map: BARMM is drawn as an ordinary
  Philippines region (its own row, ordinary subdivision tier), **not** promoted to a full separate block like
  Aceh/West Papua and **not** given a sphere overlay, since it already respects whole-province lines and sits
  entirely inside one country. **✅ Author-confirmed 2026-09-26 — see §4.4.**
- **A real data discrepancy surfaced**: the frameworks survey cites BARMM's population as 5.69 million (2024),
  which turns out to be the **pre**-exclusion figure — a Philippine Supreme Court ruling, final November 2024,
  excludes the province of **Sulu** from BARMM. The map-data package uses a separate, post-exclusion regional
  dataset (4,545,486) instead, with Sulu's population folding back into the Zamboanga Peninsula region row.
  **✅ Resolved 2026-09-26** — Executive Order No. 91 (30 July 2025) confirms the transfer; the ~1.1M gap
  between the two figures is exactly Sulu's population moving to Zamboanga Peninsula, not an error.
- **Three spheres, not the mainland's four**: the Maritime Mandala (Srivijaya/Majapahit — this file's own
  reasoned geometry, since the frameworks survey explicitly declined to propose one), the Overseas Chinese
  Commercial Diaspora, and Linguistic Wallacea (the one sphere with real, peer-reviewed-sourced geography —
  Schapper 2015/2017 — explicitly **not** the same footprint as the 1859 biogeographic Wallace Line).
- **Not yet rendered.** Stage 4 (generation) happens later in the Claude.ai web UI, same as every other
  region's map-data package.

**Universe-wide**

- **Melinda Barlow** begins the commensal relationship that makes bats semi-tame "wild pets" centuries later.
  A ~20-minute **short film**. Canon in `history/Bat Semi-Domestication - the Commensal Pathway.md`.

---

## 4. Open work, in priority order

### 4.1 East Asia — ✅ COMPLETE, no open items

Everything that used to be tracked here (naming, branch order, visual adjustments, native-language text,
timeline years) is resolved and migrated to canon. See §3 above for the settled-decisions summary and the
canon/working-package paths. Nothing left to do unless the author opens something new.

### 4.2 Latin America — ✅ COMPLETE, rendered and author-verified 2026-09-25

**The entire Latin America map is done.** South America, Central America and the Caribbean islands have all
been through the region-by-region "a country keeps its own territory unless there's a specific, settled
reason otherwise" review, rendered in the Claude.ai analysis tool, and author-confirmed against the actual
images — "everything checks out." Both outputs are final: the full map (`map-7-nations.png`) and the dedicated
Mexico/Central America/Caribbean crop (`map-mexico-central-america-caribbean.png`), both in `y-files/Map
Files/Latin America/02 reorganization/08 follow-up/`. That folder's `nations.py` is the authoritative,
fully-tuned script — label positions and two colors (Dominican Republic, the Araucánia–Patagonia Zone) went
through several rounds of author-reviewed adjustment after the initial render. Nothing left to do here unless
the author reopens something.

**✅ NAMED AND FULLY PROPAGATED 2026-09-28**: the Araucánia–Patagonia Autonomous Zone's working name is now
final — **Araucanía-Patagonia Autonomous Zone [APAZ]** in English, **La Zona Autónoma de Patagonia y
Araucanía [ZAPA]** in Spanish, both author-supplied with their own abbreviations. This closes the last
working-name item on the entire South America map. "Virgin Islands," "French Antilles" and "Aruba-Curaçao"
(Caribbean islands, §5.1 below) remain working names, not raised as active items this session.

**Applied everywhere, including an actual re-render** — `nations.py`'s name dict, on-map label text, and
`nations-assignment.csv` (10 rows) all updated; **`map-7-nations.png` was genuinely re-rendered**, not just
source-edited, by reconstructing a local-session-compatible copy of the render environment (the script's own
Natural Earth data normally lives only in the Claude.ai analysis-tool sandbox at `/home/claude/ne/`; this
session substituted already-cached local Natural Earth shapefiles, converted the admin-1 layer to the
`adm1.gpkg` format the script expects, and redirected its hardcoded `/mnt/user-data/...` upload/output paths).
**Author-specified label treatment applied**: the zone's name renders as two stacked text blocks — the English
name bold on top, the Spanish name in smaller italic type directly underneath, since a single text call can't
mix font sizes. Old pre-naming outputs archived (not deleted) to `08 follow-up/archive 06 - pre-APAZ-naming/`.
One incidental fix made along the way: the legend's own new note originally used a ✅ emoji character the
render's font doesn't support (showed as a missing-glyph box) — replaced with plain text.

**Roster note, also done**: `nations/World-Nations-Roster.md`'s South America section no longer says "no
nations named yet" — brought fully current 2026-09-28, including APAZ/ZAPA. That fix also surfaced staleness
well beyond South America (East Asia, Southeast Asia, Oceania, Russia/West Asia sections were all out of date
relative to this tracker) — a full sync pass was done across the whole roster the same session, see that
file directly for the corrected Asia/Oceania/Russia sections and a rewritten Running Tally.

### 4.3 Mainland Southeast Asia — ✅ COMPLETE, official package verified 2026-09-26

**⚠️ UPDATED 2026-09-26: this region's core premise — "no partition decisions, just the mandala overlay" — is
no longer fully true.** Author-settled: Thailand's **Pattani, Yala and Narathiwat** provinces (the "Deep
South") become their **own independent nation** after the 2083 war. This came out of research into the
author's initial proposal that the Deep South joins Malaysia outright — checked and not well-supported (the
actual insurgency, BRN, wants independence, not annexation; Malaysia's government explicitly rules out any
territorial claim) — same finding pattern as West Papua/PNG on the Maritime map, and settled the same way:
separates on its own merits, later Malaysia union left open, not asserted. **The independence-vs-autonomy
sub-question is also now settled, and runs opposite to Aceh's finding**: Thailand has never granted an ethnic
minority region real autonomy anywhere in its modern history (its only two special administrative regions,
Bangkok and Pattaya, are geographic, not ethnic), the current peace process is fragile and unproven (a missed
2024 deadline, a year-long suspension, talks only resuming 8 December 2025), and Deep South security sits
under direct military — not civilian — control since 2005, a structural veto Aceh's case never had. Full
detail in `mainland-southeast-asia-map-data/README.md`'s "The Deep South / Patani Question" section and the
frameworks survey's §3.2 addendum.

**A new sphere, S5 "The Patani Malay World," is the first-ever connection built between the Mainland and
Maritime Southeast Asia maps.** Core here: Pattani/Yala/Narathiwat. The matching Maritime-side sphere (S4)
covers Malaysia's Kelantan and Terengganu — the real, named "Kelantan-Pattani Malay" dialect classification
spans both, tracing to the precolonial Sultanate of Patani. Each map labels the other's portion as continuing
onto its companion rather than drawing it. See `spheres.csv` on both packages.

**✅ `subdivisions.csv`, `spheres.csv` and `render_map.py` are all rebuilt** to reflect the Deep South's
independence and the new S5 sphere — packaged as `instructions-mainland-v02.zip` in `y-files/Map Files/Asia
(Southeast)/01 initial generations/`. Syntax-checked clean; **not yet actually rendered** in the web UI, so
treat the first real render as a verification pass, same as every other script built this way in this project.

**Frameworks and material surveys are otherwise done (below); the map-data stage is now also done** —
`worldbuilding/nations/mainland-southeast-asia-map-data/` (`subdivisions.csv`, `spheres.csv`, `README.md`). See
§3 above for the summary and the package's own README for full detail, sourcing, and the design flags (most
importantly S2/Isan, which needs an author decision on visual treatment, not just a fill color).

**What's left before this region is done:** Stage 4 (generation, in the Claude.ai web UI — not yet run) and
Stage 5 (naming — not applicable here the way it was for North America/Latin America, since these five
countries keep their real names; nothing to name). **Two small open items carried from the map-data build
itself:** whether the author wants the optional Myanmar civil-war-snapshot second map (see §3), and whether to
correct the material survey's Cambodia unit-count arithmetic (24 provinces, not 25 — 25 total with Phnom Penh,
not 26) now that the map-data package has flagged the discrepancy.

**✅ Scoping question resolved 2026-09-26: single present-day map, Woodard-style — not a timeline series.**
Author's own words: "basically just a Colin Woodard-style map, as derived from the information we have
available from real-world research." This settles it the same direction as North America (a single map of
present-day/post-collapse nations derived from real cultural-geography research), not East Asia's dated
multi-era political-history sequence. The map-data package already built (single snapshot) is therefore the
right shape and needs no rework on this point. `y-files/Map Files/Asia (Southeast)/`'s `03 official timeline
years/` and `04 timeline staging/` folders turned out to be standard scaffolding rather than a signal a
timeline was wanted here specifically.

**Frameworks ~4,582 words, material ~5,668 words** — up from ~6,600 words combined, via a targeted
gap-filling pass. Treat both files as substantially deepened, **not** as a finished analysis — real gaps
remain (below).

**✅ Vietnam's first-order subdivision count is resolved: 34 provincial-level units (28 provinces + 6
centrally-run cities), effective 1 July 2025 under National Assembly Resolution 202/2025/QH15.** This is what
unblocked the map-data stage built above.

**Closed this session:**

- **Myanmar's conflict map** (state-by-state control, dated as a mid-2026 snapshot) and the **Wa's status**
  (de facto self-governing, China-protected, not separatist — it recognizes Myanmar's sovereignty and has not
  sought formal independence).
- **ECI for all five countries** (consistent ordering: Thailand > Vietnam > Cambodia ≈ Laos > Myanmar).
- **The Southeast Asian tin belt**, plus **Vietnam's minerals** (world's 3rd-largest bauxite reserve,
  2nd-largest rare-earth reserve, barely mined) and **Cambodia's minerals** (latent, undeveloped).
- **The five ports** — Haiphong, Laem Chabang, Yangon, Sihanoukville, Da Nang.
- **Myanmar's teak and rare-earth figures** (the rare-earth finding ties directly to the KIA's October 2024
  territorial gains in the new conflict map). Gas volume/routing updated; no current dollar figure found
  (see "Still open").
- **Thailand's "never colonized" claim** — confirmed, with the nuance kept: independence was bought with
  coerced territorial cessions to France (Laos 1893, western Cambodia 1907) and Britain (four Malay
  sultanates, 1909), not free diplomacy.
- **Laos**, all four residuals: PPA/contract terms for electricity exports; the 38% coal / 34% hydro /
  80%-of-generation contradiction (genuinely resolved — different denominators, primary energy vs. electricity
  generation, confirming the file's own hypothesis); Lan Xang's 1707 three-way split; population shares across
  the Lao Loum/Theung/Sung elevation tiers (~50% of Laos sits in the Theung/Sung tiers).
- **The Zomia seam with East Asia** — checked. No factual contradiction found; one framing nuance flagged (the
  "Zhuang" ethnonym is substantially a 1950s PRC administrative category, in tension with using it as a clean
  label for an 8th–10th-century migrating population; the settled southern-border decision — Yunnan, Guizhou
  **and** Guangxi as Federation territory — is now named explicitly in the file). See frameworks survey §2.3.

**Still open:**

- Exact dollar figures for Myanmar's gas exports and Laos's electricity revenue — ranges found, not single
  sourced numbers.
- Thailand's non-tin minerals — unresearched.
- The ECI cross-source score discrepancy — ordering is consistent across sources, absolute scores are not.

**Not a research gap:** whether a dam-failure scenario is in play is an author decision, not something a
research pass resolves.

### 4.4 Maritime Southeast Asia — ✅ COMPLETE, official package verified 2026-09-26

**Stage 1 (frameworks), Stage 2 (material) and Stage 3 (map-data) are all built. Stage 4 (rendering) has
happened once already**, against the now-superseded eight-blocs-as-eight-nations shape
(`maritime_sea_map.png`, in `y-files/Map Files/Asia (Southeast)/01 initial generations/`). **The renderer
itself is now rebuilt to v4** to reflect the settled shape below and packaged as
`instructions-maritime-v04.zip` in the same folder — syntax-checked clean, **not yet run** against the new
shape. Package at `worldbuilding/nations/maritime-southeast-asia-map-data/`.

**✅ THE FINAL SETTLED SHAPE, after a multi-pass research arc this session** (full detail and sourcing in
`DESIGNATIONS - What Each Region on the Map Actually Is.md`, which also specifies exactly what the map redraw
needs):
- **A six-bloc unified core** — Sumatra, Java, Kalimantan, Sulawesi, Nusa Tenggara & Bali, and **Maluku** (the
  last confirmed) — stays one successor state, capital **Nusantara**.
- **West Papua** secedes and starts fully independent at 2083 (the strongest popular-support evidence in this
  whole research pass); a later merger with Papua New Guinea by the Falkland Treaty (2564) is left open.
- **Aceh** becomes an **Autonomous Zone**, not fully independent, forming gradually after 2083.
- **This also ties Maritime SE Asia to the shared universe timeline for the first time**: 2083 is the same war
  East Asia's own canon already uses.
- **Philippines**: settled definitively, stays whole, no further research needed.
- **Malaysia**: settled — stays intact as a sovereign country, with **Sarawak** specifically gaining
  Autonomous Zone status (same designation as Aceh) — **Sabah stays an ordinary state**, unpromoted, its own
  case being less organized/documented. Same research rigor as Aceh/Maluku: real grievance (5% oil royalty vs.
  the bulk of national gas reserves), but secession is an explicit minority position and Putrajaya has been
  defusing pressure through concession rather than losing control — no war, unlike Aceh's history.
- **A new sphere, S4 "The Patani Malay World," connects this map to the Mainland Southeast Asia map for the
  first time** — Kelantan and Terengganu specifically (not Kedah/Perlis, a separate connection), sharing the
  real "Kelantan-Pattani Malay" dialect classification with Thailand's Deep South. This also surfaced a
  decision about the Deep South itself: the author's initial proposal that it simply joins Malaysia was
  checked and found not well-supported (same pattern as West Papua/PNG) — see §4.3 for the full Deep South
  finding, which is this map's own first-ever partition decision as a knock-on effect.

**Do not treat the current eight-nation render (`maritime_sea_map.png`) as final** — it is superseded by v4 of
the renderer, which has not been run yet. See `DESIGNATIONS.md`'s "What the Map Redraw Needs" section for the
built-vs-untested distinction.

**How this was reached, condensed** (originally "eight blocs = eight nations," reopened, then resolved bloc by
bloc): Sumatra/Java/Kalimantan/Sulawesi/Nusa Tenggara & Bali had no separatist case in either survey from the
start. Aceh and West Papua were the two strongest independence cases (real precolonial sultanate/1976–2005 war;
tier-1 Melanesian exception/ongoing insurgency, respectively). Maluku's case looked real-but-failed (1950 RMS)
until deeper research — see below — pointed it toward the core instead.

**⚠️ A fourth factor added to that research, 2026-09-26 (author-requested): Java is physically sinking.** Not
a separatism argument like the other three, but a real, current, sourced one — Java's north coast (Jakarta,
Pekalongan, Semarang, Demak) subsides up to 1.5m/decade, ~9x faster than sea-level rise, mostly from
groundwater extraction, and it's the actual reason Indonesia is relocating its capital to Kalimantan
(Nusantara). Sumatra has its own smaller, separate exposure (24 islands already lost off Aceh/North
Sumatra/Riau's coasts). Full detail in the material survey's new §9 and `DESIGNATIONS.md`'s Java/Sumatra
sections. Practical upshot for the partition question: Java's 56%-of-population weight may not be a durable
long-term anchor for a unified successor state, independent of whether Aceh/West Papua/Maluku secede.

**Follow-up, same day: Nusantara profiled in full, and a reasoned (flagged-speculative) Java trajectory
built.** `DESIGNATIONS.md` now has real Nusantara specifics (site, size, construction status, the real 85%
funding cut, its 2028 downgrade to "political capital only" with Jakarta keeping economic dominance) plus
three offered in-world scenarios for what that becomes post-collapse, and a full "Java's realistic
post-collapse trajectory" projection reasoning from the real subsidence data to a genuinely well-grounded
hypothesis: **a Kalimantan/Nusantara-anchored successor state surviving Java's coastal collapse better than a
Jakarta-anchored one would, for structural (not just demographic) reasons.** All explicitly flagged as
reasoned speculation for the author to react to, not decided fact — read `DESIGNATIONS.md` directly for the
full reasoning chain before treating any of it as settled.

**✅ SETTLED, same day: the five-bloc core, and the region's first confirmed link to the shared universe
timeline.** Author-confirmed: **Sumatra, Java, Kalimantan, Sulawesi, and Nusa Tenggara & Bali all stay one
unified successor state** — none of the five has any separatist basis (ethnic, religious, linguistic,
economic, industrial, or societal) for splitting from the others, confirmed bloc by bloc. **The capital, as of
the 2083 war, is Nusantara** — certain given the real-world timeline (a troubled, underfunded transition still
completes well within 60 years of 2022's groundbreaking). **This is also the first time Maritime Southeast
Asia has been tied to the project's shared universe timeline**: 2083 is the same war East Asia's own canon
already uses (§3's East Asia entry above) — this region's collapse is not a separate event. The eight-blocs-
as-eight-nations premise the rendered `maritime_sea_map.png` was built under is now **superseded**; that
render will need redrawing once the remaining question resolves.

**✅ SETTLED, same day: West Papua secedes.** Author-confirmed, backed by the strongest popular-support
evidence in this research pass: the 2017 West Papuan People's Petition (1.8M signatures, 95.77% indigenous,
representing over 70% of the whole indigenous population, collected under real threat of arrest) and the
1969 "Act of Free Choice"'s well-documented illegitimacy (~1,000 hand-picked voters). Caveat: this is
specifically about indigenous sentiment — roughly half the territory is settler-descended, with no evidenced
independence sentiment. **West Papua starts as its own independent nation at the 2083 war.** Whether it later
merges with Papua New Guinea by the Falkland Treaty (2564) is a separate, deliberately left-open question —
real precedent exists for gradual economic-integration-then-merger (Yemen, 1990) but failure is arguably the
more common historical pattern (Mali Federation, UAR, Senegambia all collapsed within 2 months to 7 years);
Korea's 75+ year unbroken partition despite shared kinship is the sobering counter-case. None of that
precedent covers a 500-year timescale, so this stays a creative call. Full detail and sourcing in
`DESIGNATIONS.md`'s West Papua section.

**✅ SETTLED, same day: Aceh becomes an Autonomous Zone, not a fully independent nation.** Author-confirmed,
forming gradually after the 2083 war as a secondary consequence of Indonesia's post-war weakening (the capital
move, the loss of West Papua and possibly Maluku), not a clean immediate break — consistent with Aceh staying
physically attached to Sumatra, unlike West Papua's or Maluku's island geography. Grounded in real evidence:
**Aceh already has almost exactly this status today** (the 2005 Helsinki Agreement — own regional Islamic law,
resource control, local political parties — has held for 20 years, with real but non-fatal implementation
gaps), and neither of the two obvious cautionary analogies actually applies: **Crimea**'s 1991–2014 Autonomous
Republic status ended via *external annexation* by an ethnic-kin power (Russia) exploiting Ukrainian
weakness — Aceh has no equivalent external claimant; **Hong Kong**'s "one country, two systems" was eroded by
a *central state growing stronger* over time (the 2020 National Security Law, 23 years into a 50-year
promise) — the author's own premise is a *weakening* post-war Indonesia, the opposite condition. **Structurally
distinct from the Araucanía–Patagonia Autonomous Zone** (Latin America), which is jointly guaranteed by two
neighboring sovereign states and takes 1–2 generations to form — Aceh's arrangement has no second
co-guaranteeing country, closer to the real Crimea/Hong Kong/actual-Aceh single-central-state model.

**✅ SETTLED, same day: Maluku stays part of the core, as its sixth bloc — the last open question, now
closed.** Author-requested deeper research (culture, economy, current politics) found a meaningfully weaker
case for secession than "real but historically failed" suggested: **pela gandong**, Maluku's own deepest
cultural institution, is a still-living system of cross-religious village alliance oaths built specifically
around social harmony and reconciliation, not division — it's explicitly credited with helping Maluku recover
from the 1999–2002 conflict. The RMS government-in-exile (Netherlands since 1966) is still active as of
September 2025, but reads as a diaspora-symbolic movement, not an on-the-ground insurgency — no OPM-style
armed movement, no West-Papua-2017-petition-scale mobilization found. And economically, North Maluku is
currently **the fastest-growing province in Indonesia** (34.17% growth in 2025, the national high, driven by
nickel-downstream investment) — a live, material reason for Maluku itself to want to stay integrated, not
just a reason for Jakarta to keep it. **This closes the entire Indonesia partition question.** Full sourcing
in `DESIGNATIONS.md`'s Maluku section, which is now the authoritative, complete, current state of every bloc.

**Both design questions that blocked Stage 3 are now resolved by the author:** Indonesia's internal division is
island-group blocs (confirmed, as recommended), and Aceh/West Papua both get full separate hard-bordered
blocks (not a sphere/overlay treatment) — see §3 above for the full breakdown, including the West Papua
boundary judgment call and the BARMM/Sulu items this unblocking surfaced.

**Open items carried forward, not resolved in this pass:**

- **✅ The West Papua boundary resolution (whole Papua bloc) and BARMM's ordinary-subdivision treatment are
  now author-confirmed (2026-09-26)** — both were this file's own judgment calls, flagged for review, and the
  author has since endorsed both as-built. No longer open.
- **✅ The BARMM/Sulu population-figure discrepancy is now reconciled (2026-09-26)** — see the render-review
  entry below; the ~1.1M gap is Sulu's population moving to Zamboanga Peninsula, confirmed via EO 91.
- Sphere S1's entire geometry (the Maritime Mandala) is this map-data file's own reasoned construction, since
  neither survey proposes specific geometry — lowest-confidence content in the package, worth a look before
  treating it as settled.
- The overseas-Chinese population's internal dialect/regional composition, by country — still open, not needed
  for this map.
- Indonesia's/Malaysia's rice self-sufficiency ratios; Brunei's/Timor-Leste's ECI scores; the Philippines'
  inter-island shipping network in comparable depth to Indonesia's pinisi tradition (all from the material
  survey's own §8) — none block Stage 4.

**First WebUI render pass (2026-09-26): script bugs found and fixed, five factual corrections made.** The
author took `render_map_maritime.py` (v1, built directly in this session rather than by the web UI from
scratch, unlike the mainland script) to the Claude.ai web UI for Stage 4. That session's review found real
bugs and real factual errors, none caught locally since this session has no geopandas access to test against.
**All fixed in a v2 script** (`y-files/Map Files/Asia (Southeast)/01 initial generations/render_map_maritime.py`)
and in the canon docs (not just the web UI's own copy):

- **Script bugs fixed**: the Indonesia keyword-classifier crashed on Jambi/Lampung/Bengkulu (no "Sumatra"
  substring — added as explicit keywords); the "other countries" context layer wasn't clipped to a bounding
  box before reprojecting, so a country near the antipode (almost certainly Antarctica) blew up to cover the
  whole frame under the Lambert azimuthal projection; the legend covered Aceh, Peninsular Malaysia, Kuala
  Lumpur, Singapore and the Mandala label (moved to a dedicated side panel, same fix pattern as the North
  America scripts use); several sea/label positions sat on land or collided (Java Sea was on Bali, Banda Sea on
  Halmahera, Strait of Malacca on Sumatra, Timor-Leste's label on Dili's own marker); the Bird's Head sphere
  patch was a schematic ellipse that cut through province lines and undershot Cenderawasih Bay — now uses the
  real old-vintage "Papua Barat"/"West Papua" province polygon where Natural Earth carries it, falling back to
  the ellipse only if that specific province isn't found; the Overseas Chinese sphere's Singapore buffer
  spilled ~15km into Johor and Batam (removed — no buffer); S2's core and domain hatches were identical
  density, copied from the mainland's deliberate Isan equal-weight choice but meaningless here (differentiated).
  **Not fixed, left for the web UI's next pass**: the Philippines' internal subdivision lines draw from
  Natural Earth's ~118-province admin-1 data, not the 18-region level this map's own data is keyed to — the web
  UI's review already identified that Natural Earth carries a region-grouping attribute to dissolve by, but
  this session has no way to confirm its exact field name without live data access.
- **Five factual corrections, applied to the frameworks survey, the material survey, and `subdivisions.csv`/
  `spheres.csv` alike, not just the render script**: (1) the Sabah cession direction was backwards — **Brunei
  ceded North Borneo to Sulu** in the 17th century in return for military help in a Brunei civil war, not Sulu
  ceding to Brunei in the 15th; (2) **Malaysia's ethnic-Chinese share is ~23% (2020 census), not ~34%** (that
  figure was roughly the 1960s share); (3) **both Sabah and Sarawak receive a 5% oil royalty** — Sarawak's real,
  separate win was a 5% state sales tax on petroleum products, not a 20% royalty (20% is what both states have
  been *demanding*); (4) **Timor-Leste has 14 municipalities, not 13** — Atauro split from Dili in 2022, and
  Oecusse-Ambeno is formally a Special Administrative Region, not an ordinary municipality; (5) the BARMM/Sulu
  population discrepancy is **resolved**, not just flagged — Executive Order No. 91 (30 July 2025) confirms
  Sulu's transfer to Zamboanga Peninsula, and the ~1.1M gap between BARMM's two cited figures is that transfer.
- **Three sphere-design questions raised by the review, all now author-decided (2026-09-26) and applied**:
  **Aceh and Bali both join the Maritime Mandala's domain** (Aceh: a central Malacca Strait trade node in its
  own right, previously in no sphere at all; Bali: Majapahit's living cultural heir); **Linguistic Wallacea's
  core includes Sumbawa but excludes Lombok**, via a schematic sub-province patch rather than a whole-province
  swap — Sumbawa and Lombok share one province (West Nusa Tenggara), so the whole-first-order-subdivision rule
  (which governs hard borders, not sphere overlays) would otherwise force an all-or-nothing choice that the
  survey's own "east of Lombok" finding doesn't support either way.

### 4.5 Russia — Stage 1 frameworks survey done, 2026-09-27; the three East Asia seams resolved

**📍 For current map state (nation names, capitals, open items), read
`y-files/Map Files/Russia/PROGRESS TRACKER - Read This First.md` — that file is now the authoritative,
actively-maintained handoff doc for Russia's ongoing reorganization work (round 2 as of 2026-09-27: 20
nations → 13, Idelsk-Uralia/Donska-Kubania named, capitals set for four nations, Country A still unnamed).
The section below is historical record of Stage 1 and is not being kept in sync turn-by-turn — don't treat it
as current for anything past the Stage 1 survey itself.**

Deliberately excluded from East Asia, with **three seams left white and unclaimed**: Outer Manchuria,
Sakhalin/the Kurils, and Buryatia/Tuva. Every East Asia map has a blank northern edge because of this.
**Chosen 2026-09-26 as the region after Oceania, not before it** — see §4.6. `y-files/Map Files/Russia/` used
to have a batch of stray Latin America files misplaced in it (`nations.py`, `map-7-nations.png`, etc.,
left over from before Latin America had its own folder) — **the author cleaned this up 2026-09-27**; the
folder is now a genuine empty scaffold, confirmed no real Russia content was lost.

**✅ Stage 1 frameworks survey built 2026-09-27**:
`worldbuilding/extractions/Russia - Federal Fractures and the Far Eastern Question (survey).md`. Headline
finding: Russia's fragmentation logic is mostly **economic/regional, not ethnic** — only 5 of ~85 federal
subjects (the oil/gas okrugs Khanty-Mansi and Yamalo-Nenets, Moscow, St. Petersburg, Tatarstan) produce over
70% of federal budget revenue; 72 of 85 are net recipients. Uses tiered ethnic identity (same method as East
Asia, not Woodard's settler-doctrine) since Russia's expansion is imperial-annexation-shaped, not
settlement-shaped.

**The three seams — resolved, recommendations not assertions**:
1. **Outer Manchuria** → its own **Russian Far Eastern successor state**. No ethnic case (Russian-majority,
   same Tier 1 as Moscow), but a real historical precedent exists: the actual **Far Eastern Republic
   (1920-22)**, a buffer state covering almost this exact territory (Amur, Transbaikal, Kamchatka, Sakhalin,
   Primorye). Stays a hard border against East Asia's Manchuria/Chuang Guandong along the existing
   Aigun (1858) / Peking (1860) treaty line already drawn on that map.
2. **Sakhalin and the Kurils** → folds into that same Far Eastern polity (the real 1920-22 Far Eastern
   Republic already included Sakhalin). The live real-world Japan-Russia dispute over the four southern Kurils
   is flagged as optional East Asia-side texture (a sphere-style tension marker on Japan's entry), not a
   redraw — **author's call, not resolved by this survey**.
3. **Buryatia and Tuva** → split. **Tuva gets its own polity** (88.7% ethnic Tuvan, a real 1993 constitutional
   secession clause) — this is the pan-Mongolic sphere's "northern dimension" East Asia's survey flagged as
   undefined. **Buryatia is a genuine open judgment call**, structurally identical to East Asia's own
   unresolved Inner Mongolia case (Mongolic but only ~30% Buryat in its own republic) — deliberately left
   open, mirroring East Asia's own non-resolution there.

**Biggest gap flagged for Stage 2**: Rosstat's own 12-economic-region framework wasn't pulled into this pass —
it's Russia's official government framework for regional economic analysis and would upgrade "5 donors, 72
recipients" into an actual drawable regional skeleton, the way Skinner's macroregions anchored East Asia's Han
core. Also flagged, not yet researched: Kaliningrad (a genuine exclave, cut off from any Russian successor
state's contiguous territory — will almost certainly need its own seam-style treatment), North
Ossetia/Kabardino-Balkaria/Karachay-Cherkessia, and Kalmykia (Europe's only Buddhist-majority republic,
Mongolic Tier 1 but geographically separated from Buryatia/Tuva by the width of Russia).

**✅ Stage 3 map-data package built and rendered locally, 2026-09-27**: one full-Russia overview + three
regional close-ups (west, central, east) — the first region in this project split into four maps rather than
one or two. Delivered to `y-files/Map Files/Russia/01 initial generations/` and mirrored to
`worldbuilding/nations/russia-map-data/`. Built ahead of the usual pipeline order (Stage 2 material survey
still hasn't happened for Russia) on direct author instruction — the package is explicitly flagged throughout
as a rougher first pass than Oceania's or Southeast Asia's Stage 3 work.

**20 nations, 83 subdivisions** (Crimea/Sevastopol excluded — coded as Ukrainian in Natural Earth, not
asserted as Russian). Well-grounded in the Stage 1 survey: core Russia, Tatarstan, Kalmykia, Tuva, Chechnya,
Ingushetia, Kaliningrad (a genuine exclave, drawn in true position rather than an inset — it sits only a few
hundred km from the rest of Russia, comfortably inside the West close-up's own frame, unlike Hawaii's case on
the North America map). **⚠️ Six flagged author-review judgment calls**: the Russian Far East's inclusion of
Buryatia (the single biggest open item on the whole map — mirrors East Asia's own unresolved Inner Mongolia
case), Sakha drawn as its own nation (a deliberate divergence from the Rosstat grouping), Bashkortostan, North
Ossetia-Alania, Kabardino-Balkaria, and Karachay-Cherkessia (none of the last four researched in the Stage 1
pass). Least-researched tier, Rosstat-skeleton defaults not individually researched: The Northern Republic,
The Volga Republic, The Urals Republic, Western Siberia, Eastern Siberia, Southern Russia.

Antimeridian handling (the `shift_lon`/`antimeridian_fix` technique Oceania established first) reused for the
East close-up — confirmed working, Chukotka renders as one contiguous shape near the Bering Strait. **Label
collisions found and fixed 2026-09-27** (round 2, after the fork's own initial build flagged one as unfixed):
the North Caucasus capital cluster (Grozny/Magas/Vladikavkaz/Nalchik/Cherkessk/Makhachkala, six capitals
within ~150km of each other) on both the West close-up and the full overview, plus Yekaterinburg/"The Urals
Republic" and Kyzyl/"TUVA" on the Central close-up — see that folder's `CHANGES.md`. Not yet through a
Claude.ai web-UI round-trip — treat as a solid first pass, not a fully polished final render, same caveat
every other region's first Stage 3 pass carried.

### 4.6 Oceania — chosen as the next region, 2026-09-26; Stage 1 done, Stage 3 map data built + rendered

**Author's call, made explicit 2026-09-26**: Oceania goes before Russia. Reasoning at the time — Oceania has
a head start (Hawaii is already a named, canon North America nation) and is self-contained, with no shared
border waiting on another unfinished region; Russia is bigger, has zero groundwork, and also patches three
border seams East Asia left open (§4.5), a bigger lift for later. West Asia (Kazakhstan + the "-stans" + the
Middle East, referenced by both the Sinian Federation and Russia) is the region planned after both of these,
not started.

**Hawaii's own National Character Profile, added 2026-09-26**:
`nations/Sovereign Republic of Hawaii - National Character Profile.md`. Author-requested specifically —
Hawaii ties into two load-bearing pieces of existing canon (U.R.U.K./En.Ki.Du, the robot birthplace; Doris
Morikawa's Hall of Archives, the pre-war human-knowledge repository) worth developing even though Hawaii's
Assembly-member status was already settled. Real-world material research found a sharp tension worth
preserving, not resolving: Hawaii is severely food-import-dependent (85-90% imported, as low as 11.6%
true self-sufficiency) and fuel-import-dependent (80%+, uses ~16x more energy than it produces) — one of the
most materially fragile places in this project's worldbuilding so far, in direct tension with its declared
identity as neutral, self-sufficient-seeming safe haven for civilization's most important institutions. Two
dramatic questions already flagged as deliberately open in existing canon (`Writers-Room-Hooks.md`) were
preserved, not resolved: whether the Hall of Archives survived the wars, and whether Hawaii's neutrality
protected it or endangered it. The single biggest open research question this file surfaced: who supplies
Hawaii's post-collapse shipping lifeline — needs cross-checking against Cascadia's own material-base research
once that connection is worth making.

**Frameworks survey, first pass (the rest of Oceania)**: `worldbuilding/extractions/Oceania - Coastal
Cohesion and the Import Lifeline (survey).md`. Covers Australia, New Zealand and the Pacific Islands — Hawaii
is covered separately, above. Author supplied four working hypotheses up front to steer the research (not to
be treated as settled): Australia won't fracture (coastal settlement pattern argument); Oceania likely sees no
direct
attacks in the war; NZ likely stays independent rather than being absorbed into Australia; NZ's North/South
Islands likely don't split. **Research so far supports all four, with nuance**:
- Australia's 87-95% coastal population concentration is real and strongly supports the cohesion argument,
  but WA actually voted 66% to secede in 1933 (blocked only by the Constitution's "indissoluble" clause and a
  refused British petition) — real historical secessionism exists, so the "won't fracture" case rests on
  *post-collapse survivability*, an argument this survey extends past what the historical record itself
  tested, not one the historical record settles outright. Flagged as the author's own reasoned extrapolation.
- NZ's 1901 non-federation was a deliberate, considered choice (Seddon wanted an independent country, not
  an Australian state) — solid precedent for staying independent.
- NZ's "South Island nationalism" is a real, named, 160-year-old movement (traced to 1860s gold-rush wealth
  vs. North Island war costs; nearly caused a colonial split in 1865; had a minor political party as recently
  as 1997) — genuine grievance, never serious secession traction. Matches "possible but unlikely" well.
- **The real finding, matching the author's own instinct that supply lines are the crux**: Australia is
  food-secure (200%+ self-sufficiency, major net exporter) and raw-energy-rich (top-tier LNG/coal exporter),
  but severely import-dependent on two specific things — **refined fuel** (80-90% import-reliant; only 2 of 4
  refineries left; exports 75% of its own crude rather than refining it) and **pharmaceuticals** (~90%
  imported, mostly China/India, with almost no domestic manufacturing capacity even for raw ingredients). The
  Pacific Islands proper (not Australia/NZ) are a completely different, far more fragile case — already
  described in real-world sources as facing "existential threats" from import dependency (80% of food
  imported on Tuvalu's main island) — flagged as needing its own separate treatment, not folded into
  Australia/NZ's relative resilience.

**✅ RESOLVED, author-confirmed 2026-09-26**: "Upper Earth" is just this setting's standing term for
"everywhere on the planet that isn't Antarctica" (Tepenia) — not a pointer to the later, separate War of
Upper Earth (~2563-2564, `history/World-History-Excerpt.md`). Oceania's map work is keyed to the **2083 war**,
matching every sibling region. No longer open.

**Cross-repo connection found 2026-09-26**: a parallel Claude Code session in the `Inner Tepenia` GDD repo
independently researched Australia's material profile for a different purpose — Australia is established
canon there as Tepenia's single biggest Upper Earth trading partner across two of Tepenia's three coastal
regions, and that session compiled real-world-grounded candidate exports each direction (Australia's
pharma/fuel/phosphate/rare-earth/semiconductor import dependency; Tepenia's Antarctic-advantaged
astrophysics/paleoclimate/cryogenic research and on-site 3D-print manufacturing). Independently corroborates
this survey's own Section 3 food/fuel/pharma numbers. Full candidate list (no decisions made) at
`games/Inner Tepenia/InnerTepeniaGDD/Worldspace/.../Research_Logs/Upper_Earth_Trade_Research_Log.md`; this
project's own cross-reference and the author's own candidate new-port-site analysis (Bunbury/Perth, Adelaide's
Outer Harbor, and Jan Juc/Torquay/Flinders near Melbourne, chosen to sit outside Port Phillip Bay's narrow
entrance) are in the Oceania survey's own new §4. **§4.1, added same day: shipping-time estimates for the two
routes tying these ports to Dumont d'Urville and Casey** (both already-developed Tepenian subnet cities),
calculated from real-world great-circle distance calibrated against RSV Nuyina's and L'Astrolabe's actual
Hobart transit data (validated to <1% distance error). **✅ SETTLED, author-confirmed: use "about a week and a
half" (~10-11 days) each way as the single working figure for all three routes** — sits in the upper-middle of
the calculated per-route ranges (6.5-12.3 days depending on route); the full per-route ranges stay on record
in §4.1 if more precision is ever needed.

**§4.2, added same day: which real countries Australia critically depends on, and how far each one is.**
Identified 11 countries covering Australia's "can't do it ourselves" categories (pharma, fuel, phosphate,
semiconductors, rare-earth processing, vehicles, heavy machinery) with real 2024 trade data, then calculated
each one's shipping time using the same great-circle method, re-calibrated this time against three real
commercial container-shipping benchmarks (Shanghai↔Sydney, LA↔Sydney, Rotterdam↔Melbourne-via-Cape).
Closest critical suppliers (Singapore, Malaysia, Thailand — 7-14 days) carry the most acute single-point
goods (fuel, semiconductors, the one non-Chinese rare-earth processor); the most distant (Morocco, 30-45
days, no substitute source) carries phosphate — already flagged elsewhere as paralleling Tepenian canon's own
phosphorus chokepoint. Full table and method in the survey's own §4.2.

**Stage 3 map-data package built and rendered locally, 2026-09-26**:
`worldbuilding/nations/oceania-map-data/` — `subdivisions.csv` (167 rows, real Natural Earth admin-1 data
across 26 countries/territories resolved to 23 nations), `spheres.csv` (Melanesia/Micronesia/Polynesia, the
standard real ethnographic three-region model, not this project's own construction), `render_map_oceania.py`,
`fonts/`, and a `README.md`. Australia and New Zealand drawn per the Stage 1 findings above (both unified);
the other 14 sovereign Pacific nations drawn at their real-world borders (no partition decisions needed,
unlike Indonesia on the Maritime SE Asia map); nine pre-war French/US/UK/NZ-associated territories (New
Caledonia, French Polynesia, Wallis and Futuna, Guam, Northern Mariana Islands, American Samoa, Pitcairn
Islands, Cook Islands, Niue) drawn as their own provisional nations, each flagged ⚠️ for author review since
none of their pre-war metropoles has an established successor-state in this project yet — **Guam is the
highest-priority flag**, given its real strategic significance (Andersen AFB, Naval Base Guam). Norfolk
Island and the uninhabited Ashmore & Cartier/Coral Sea Islands folded into Australia. **First region in this
project whose real extent crosses the antimeridian** (Fiji, Tonga, Kiribati, NZ's outer islands, most of
Polynesia) — solved with a longitude-shift-before-reprojection step, verified against a standalone test
render; documented prominently in the script and README so it isn't accidentally removed later. Rendered and
visually reviewed locally (five label collisions found and fixed: Guam/Hagåtña, French
Polynesia/Papeete, Palau/Ngerulmud, New Zealand/Wellington, Solomon Islands/Honiara), **then confirmed
through one real Claude.ai web-UI render** (`y-files/Map Files/Oceania/01 initial generations/`) — matched
the local render pixel-for-pixel in every check performed.

**✅ Split into two companion maps, 2026-09-26, author-requested**: `render_map_oceania_continental.py`
(Australia, New Zealand, Papua New Guinea) and `render_map_oceania_islands.py` (the other 20
nations/territories) — matching the Southeast Asia region's own Mainland/Maritime split. Spheres are now
genuinely cross-map (PNG's Melanesia slice and NZ's Polynesia slice on the continental map; the rest of each
sphere on the islands map), the same convention as the Patani Malay World sphere between the Mainland and
Maritime Southeast Asia maps. Both scripts verified locally, packaged for the next WebUI round at
`y-files/Map Files/Oceania/02 reorganization/01 follow-up/`. The original single-map `render_map_oceania.py`
is kept as a reference copy, not part of the two-map delivery.

**✅ Continental map framing fixed, 2026-09-26, author-requested (round 2)**: author reviewed the WebUI
render and asked to "move the camera POV further west" so Australia reads as the clear object of attention,
without New Zealand ending up jammed against the frame's edge. Root cause: the crop window's bounds were
computed from *every* drawn New Zealand subdivision, including remote sub-antarctic/equatorial dependencies
(Chatham Islands, Kermadec Islands, Tokelau, Auckland/Campbell/Antipodes Islands, the Snares, Three Kings
Islands) — Tokelau alone sits ~2,000 km north of NZ's main islands, near Samoa, which forced the frame
thousands of km past what a viewer actually expects to see as "New Zealand," stranding Australia in the
left third of the map. Fix: the crop-bounds calculation now excludes those eight outlier subdivisions (they
still draw wherever they fall — nothing removed from the map itself, only from what sizes the frame).
Australia's centroid now lands at roughly 44-45% of the map width, with New Zealand's main islands keeping
the same 350 km margin every other nation on the map gets. Verified locally, re-delivered to
`y-files/Map Files/Oceania/02 reorganization/01 follow-up/` (see that folder's `CHANGES.md`).

**✅ Both maps switched to flat, plain colors, 2026-09-26, author-requested (round 3)**: author asked for
"clean, flat, plain colors" across both companion maps. The only non-flat element on either map was the
crosshatch/dot pattern filled across each sphere's territory (Melanesia, Micronesia, Polynesia); that fill
layer is removed from both scripts. Each sphere still shows its colored dashed/dotted boundary line around
its extent (a thin outline, not a texture) — spheres are still visually identifiable, just without the
patterned fill. The legend's separate hatch-swatch row per sphere was folded into its line-swatch row
(same description text, one row instead of two). National fill colors were already flat solid tints and
are unchanged. Verified locally, delivered to
`y-files/Map Files/Oceania/02 reorganization/03 follow-up/` (see that folder's `CHANGES.md`).

**Not yet done**: Stage 2 material survey (beyond Australia, which got that depth inside the Stage 1 survey
itself); NZ-Australia integration depth (CER, Trans-Tasman Travel Arrangement, ANZUS) needed to actually
settle the absorption question rather than just lean on 1901 precedent; a dedicated Pacific Islands pass (PNG,
Fiji, Solomons, Vanuatu, Samoa, Tonga, Micronesia/Polynesia individually — their import-dependency profiles
likely vary hugely by scale); Australia's uranium/critical-minerals export position; verifying the three
candidate port sites above against real feasibility factors; whether an east-coast (Sydney/Brisbane) port
candidate is also needed; author review of the nine provisional-nation flags; per-subdivision population data
(currently blank throughout); a WebUI render/review pass.
`y-files/Map Files/Oceania/` has the standard four-stage folder scaffolding, empty.

### 4.8 West Asia — ✅ OFFICIALLY DONE, author-confirmed 2026-09-29

**Scope, author-confirmed**: Central Asia (Kazakhstan, Uzbekistan, Turkmenistan, Kyrgyzstan, Tajikistan) +
Middle East core + Turkey + Afghanistan. South Asia and Egypt/North Africa explicitly excluded.

**Stage 1 (frameworks), both files built 2026-09-27:**
- `worldbuilding/extractions/Central Asia - Steppe, Oasis and the Fergana Tangle (survey).md`
- `worldbuilding/extractions/Middle East - Sykes-Picot, Sect and the Kurdish Question (survey).md` — later
  filled in with two research gaps the author asked for by name: Jordan (§5.3) and Israel/Palestine (§2,
  2.1–2.6), grown from ~6,200 to ~8,600 words.

**Stage 2 (material survey), both files built 2026-09-28, via parallel research passes:**
- `worldbuilding/nations/material-base/Central Asia - Steppe, Oasis and Aquifer - Material and Economic Base
  (survey).md` — 5,399 words. Organizing fact: a **closed drainage basin** (Syr Darya + Amu Darya feeding the
  now-mostly-gone Aral Sea) — unlike every other region's river so far, this one's entire catchment sits
  inside the same countries it serves, so there's no external actor to blame and no external fix to import.
  Also surfaces a new Tuva/Karakalpakstan-tier open case: Uzbekistan's autonomous Republic of
  Karakalpakstan, sitting on the Aral's shore with a dormant constitutional secession clause (2022 protests).
  Kazakhstan's fiscal base runs 80%+ through the Russian-transit CPC pipeline while Kazakhstan simultaneously
  funds the Russia-bypassing Middle Corridor — a single point of failure the country is actively hedging
  against.
- `worldbuilding/nations/material-base/Middle East - Material and Economic Base (survey).md` — 6,207 words.
  Organizing fact: **two master resources running in opposite directions** — hydrocarbons radiate outward from
  the Gulf (Ghawar; the shared Qatar/Iran North Field–South Pars gas field, the world's largest, a live 2026
  war target), while water flows downstream *into* the region from Turkey, whose GAP/Southeastern Anatolia
  dams have cut Iraq's water ~80% since 1975 — no single actor holds both levers. The Mesopotamian Marshes are
  a genuine Tonlé-Sap-tier case (fully recovered twice after upstream damming, proving the damage is
  reversible). Gulf desalination (up to 100% of potable water in Kuwait/Qatar), food imports (85–90%), and oil
  exports all converge on the single Strait of Hormuz chokepoint. Afghanistan's famous "$1 trillion in
  minerals" claim is flagged as real geology but not a realistic near-term economy — the sourcing itself calls
  it "flawed and farfetched."

**⚠️ Explicit folder instruction, author-stated 2026-09-28 — do not infer a different location later**: the
Woodard-style (Stage 4 generation) rendered-map output for this region goes in `y-files/Map Files/
Asia (West)/01 initial generations/`. Reference for what "Woodard-style" means: `y-files/Map Files/
Latin America/01 initial generations/` (culture-region maps, core/domain/sphere shading, confidence markers,
existing out-of-scope nations cross-hatched gray, present-day borders as dashed reference lines, "first-pass,
for consideration only" framing).

**Stage 3 (map data), both packages built 2026-09-28:**
- `worldbuilding/nations/central-asia-map-data/` — 55 subdivision rows across all 5 countries, 2 spheres
  (Fergana Valley Mosaic + point-marker enclaves; Uyghur Diaspora). Karakalpakstan kept as an ordinary Uzbek
  subdivision but flagged as this region's own Tuva-tier open case (constitutional autonomy, dormant secession
  clause). Turkmenistan has zero sourced sub-national population data anywhere — genuinely unpublished, not a
  research gap.
- `worldbuilding/nations/middle-east-map-data/` — 293 subdivision rows across all 16 countries/territories
  (Turkey, Syria, Lebanon, Israel, Palestinian Territories, Jordan, Iraq, Iran, Saudi Arabia, Yemen, Oman,
  UAE, Qatar, Bahrain, Kuwait, Afghanistan), 4 spheres: **S1 The Kurdish Nation** (~45M people, Iraq's KRI the
  only settled case — the frameworks survey itself declines to propose a treatment, flagged as this package's
  most structurally complex sphere); **S2 Sunni-Shia Sectarian Geography** (a demographic layer only, not a
  political bloc — explicitly the most sensitive judgment call in the package); **S3 The Pan-Turkic Sphere**
  and **S4 The Persianate/Central Asian Bridge** — the project's first author-survey-flagged (not
  independently-discovered) cross-map connectors, both reaching into `central-asia-map-data/` via Turkey and
  Afghanistan respectively. Live disputes recorded as flags, not resolved: Israel/Palestine's overlapping
  Jerusalem/West Bank administrative claims, Iraq's Kirkuk (Article 140), the Golan Heights, and Yemen's live
  (Sept. 2026) Houthi/PLC civil-war control split by governorate — the last one flagged as a candidate
  optional dated second map, same treatment Myanmar's civil-war snapshot got in the Southeast Asia package.
  One color collision fixed during the merge (Iraq's original hex was nearly identical to Syria's — both
  share a long border; Iraq reassigned to a distinguishable burnt orange).

**Stage 4 (generation), first cut, both halves, 2026-09-28** — rendered to
`y-files/Map Files/Asia (West)/01 initial generations/` via the same local geopandas/matplotlib + Natural
Earth pipeline established for Russia. **⚠️ First attempt at both maps was built as ordinary political maps
(real country borders as the primary colored layer, culture only as a thin overlay) and was rejected by the
author**: "The Woodard-style maps are maps of cultures, languages, and people, not political borders." One
render was stopped mid-flight; the wrong Central Asia attempt was archived (not deleted) to `02
reorganization/archive 00 - wrong-style political-border first attempt/`. See
[[feedback_woodard_style_means_culture_not_political]] — this lesson must be checked before Stage 4 work on
any future region.

**Corrected versions, both self-verified by viewing the actual rendered PNG:**
- **`central-asia-map.png`** — seven named cultural regions as the primary layer (The Kazakh Steppe, The
  Kyrgyz Highlands, The Turkmen Desert-Oasis, The Uzbek Oasis Civilization, Karakalpakstan, The Persianate
  Tajik Highlands, The Fergana Valley Tangle — the last one given a distinct hatch texture rather than a flat
  color, and drawn as one continuous region across three countries' real borders, matching how the Latin
  America reference map draws Amazonia). Gorno-Badakhshan renders as a lighter Pamiri "domain" variant within
  the Tajik Highlands; Samarkand and Bukhara carry a distinct marker for their historic Tajik/Persian
  character despite sitting in Uzbek-core territory. Modern political borders are thin dashed-gray reference
  lines; Russia and China/Xinjiang are cross-hatched gray, "existing region — out of scope." Design record:
  `worldbuilding/nations/central-asia-map-data/regions.csv`.
- **`middle-east-map.png`** — eleven named cultural/ethnic/sectarian regions (The Kurdish Nation, Anatolia,
  The Levant, Lebanon, Israel, Palestine, Mesopotamia, Arabia, Yemen, Persia, Afghanistan). The Kurdish Nation
  is drawn as one continuous region spanning Turkey/Iraq/Iran/Syria (Iraq's KRI as solid core, the rest as
  lighter domain), the same Amazonia-style cross-border treatment. Israel and Palestine's overlapping
  Jerusalem/West Bank claims are drawn as literal overlapping/cross-hatched "contested" geometry, resolving
  nothing; Iraq's Kirkuk is marked contested rather than assigned to either Mesopotamia or the Kurdish Nation;
  Yemen's cultural fill uses the real historical Zaydi/Shafi'i split, explicitly distinguished in the map's own
  caption from the live 2026 war's separate control lines (which stay in `subdivisions.csv`, not drawn as the
  base layer). **Self-caught mid-build**: an attempted internal Maronite/Sunni/Shia hatch for Lebanon was
  found misleading (Natural Earth's coarse pre-2003/2017 Lebanon geometry merges several governorates into one
  polygon) and was simplified to one solid region rather than shipped looking more resolved than the data
  supports — flagged as a named future-polish item in `regions.csv`, not silently smoothed over. Design record:
  `worldbuilding/nations/middle-east-map-data/regions.csv`.
- **Geometry gaps, logged not faked**: Central Asia — Baikonur (no NE polygon, city marker only), Kazakhstan's
  2018-22 splits (Abai/Jetisu/Ulytau/Shymkent), Kyrgyzstan's Osh City, Turkmenistan's Ashgabat (all render as
  part of their pre-split parent unit, capital still marked). Middle East — Socotra, Qatar's Al Sheehaniya,
  Afghanistan's Panjshir have no Natural Earth polygon at all; Lebanon's 2003/2017 splits and Iraq's Halabja
  render at their pre-split geometry.

**Stage 4 polish round 1, 2026-09-28** — `02 reorganization/01 follow-up/` (explicit author folder
instruction). Two changes:
1. **First-order subdivision (province/governorate/oblast) boundaries added as a visible thin-line layer**
   within every cultural region's fill on both standalone maps, distinct from the bold region border and the
   dashed country-reference line — the author wanted the granular administrative units visible for later
   border decisions, not just the dissolved region blob. `central-asia-map.png`/`.py` and
   `middle-east-map.png`/`.py` updated in place. **Caught and fixed a latent bug along the way**:
   `middle-east-render.py`'s output path was hardcoded to `01 initial generations/` — would have silently
   overwritten the pristine folder on a future run; repointed to write next to the script.
2. **New composite `west-asia-composite-map.png`** — merges both packages' 18 regions (7 Central Asia + 11
   Middle East/Turkey/Afghanistan) onto one canvas, Kazakhstan/Turkey to Yemen/Afghanistan. Same subdivision-
   line treatment. **S3 (Pan-Turkic) and S4 (Persianate/Central Asian Bridge)**, previously label-only on the
   standalone Middle East map since the two halves weren't on one canvas, now render as real dashed connector
   arcs (Anatolia to the four Turkic Central Asian regions; Afghanistan to the Persianate Tajik Highlands,
   Uzbek Oasis Civilization, and Persia). Edge distortion (NW Kazakhstan, S Yemen, E Afghanistan) is visibly
   greater than either standalone map, disclosed honestly in the map's own footer rather than hidden. One
   rough edge for a future pass: the Levant/Israel/Palestine/Lebanon corner is cramped at this zoomed-out
   scale — legible but tight, handled better on the standalone Middle East map.

All three outputs self-verified by viewing the actual rendered PNGs.

**Not yet done**: further Stage 4 polish (the Levant-corner crowding on the composite) and Stage 5 (naming).

**South Caucasus (Georgia, Azerbaijan, Armenia) added to West Asia's scope, 2026-09-28** — author's explicit
instruction while developing the Kurdish Nation region, after asking where these three fit and being told they
were previously unmapped (out of Central Asia's scope by that survey's own words — "Azerbaijan is Caucasus/
Europe side" — out of the Middle East package's scope, never covered by Russia's own survey, and Europe hasn't
started). Stages 1-3 done in one pass, matching the Central Asia/Middle East packages' rigor exactly:
- **Stage 1**: `worldbuilding/extractions/South Caucasus - Three Churches, Two Pipelines and a Closed Border
  (survey).md` (4,259 words). Headline finding: **three old, self-contained civilizations that predate every
  empire that's since claimed them** — Armenia was the first state on Earth to adopt Christianity officially
  (301 CE), the Georgian Orthodox Church traces to the 4th century — Azerbaijan is the opposite case, a modern
  Turkic/Shia-Muslim state whose founding identity is explicitly bound to Turkey ("one nation, two states,"
  the 2021 Shusha Declaration). **Nagorno-Karabakh/Artsakh is this project's most violently resolved
  territorial question anywhere** — Azerbaijan's September 2023 offensive displaced ~100,000+ ethnic Armenians
  (99% of the territory) within days; treated like Syria's AANES dissolution (a dated, real resolution, not an
  open question). **Abkhazia and South Ossetia are the genuinely unresolved cases** — Kirkuk/Israel-Palestine
  tier, flagged not resolved, both de facto independent and Russian-garrisoned since the 1990s/2008 war.
- **Stage 2**: `worldbuilding/nations/material-base/South Caucasus - Material and Economic Base (survey).md`
  (2,268 words). Organizing fact: **a land bridge, not a river or strait** — the Baku-Tbilisi-Ceyhan pipeline
  and Baku-Tbilisi-Kars railway physically route landlocked, oil/gas-rich Azerbaijan's exports through Georgia
  to Turkey and world markets, explicitly bypassing both Russia and Armenia. A newer piece, the **Zangezur
  Corridor/TRIPP**, would connect Azerbaijan's mainland to its Nakhchivan exclave through a 43km strip of
  Armenia's own Syunik province — construction began but full ratification needs a 2027 Armenian
  constitutional referendum, not yet finalized.
- **Stage 3**: `worldbuilding/nations/south-caucasus-map-data/` — `subdivisions.csv` (38 rows: Georgia 13,
  Azerbaijan 14, Armenia 11), `regions.csv` (5 Woodard-style regions — Georgia, **Abkhazia and South Ossetia
  split out as their own regions rather than shades of Georgia**, since Abkhaz/Northwest Caucasian and
  Ossetian/Iranic are genuinely separate language families from Kartvelian, the same logic that kept
  Karakalpakstan separate from Uzbek territory in the Central Asia package; Azerbaijan; Armenia — Nagorno-
  Karabakh deliberately does **not** get its own region, reflected instead in two of Azerbaijan's own
  2021-created economic-region names), `spheres.csv` (2 rows — see below), `README.md`. All CSVs validated
  clean.

**⚠️ Two direct, load-bearing ties to the already-built Middle East package, flagged for the author's decision,
not yet applied to that package's own files:**
1. **The Pan-Turkic sphere (Middle East `spheres.csv` S3) now has the concrete anchor it was missing** —
   Azerbaijan-Turkey's "one nation, two states" relationship is exactly the grounding fact that sphere's
   Azerbaijan mention needed (previously named but explicitly out of scope). Recorded as this package's own S1
   row, recommending S3's extension into real Azerbaijani territory rather than staying label-only.
2. **Armenia's Yazidi population (31,079 census, community estimates 50,000+) is the largest Yazidi population
   by share anywhere outside Iraq** — a real, direct tie to the Kurdish Nation region (Middle East S1) that
   project data didn't previously carry. Recorded as this package's own S2 row, but **deliberately flagged at
   low confidence** — unlike the Pan-Turkic case, whether Armenian Yazidis belong in a pan-Kurdish sphere at
   all is a live, unsettled identity question, not just a sourcing gap.

**Stage 4 done, 2026-09-28** — folded directly into the existing Middle East and composite maps rather than
built as its own standalone map, per the author's own instruction: "include it with West Asia/Middle East. It
might be useful to consider them in the context of their neighbors." Working folder:
`02 reorganization/02 follow-up - divisions - initial stages/`.

- **`middle-east-map.png`** and **`west-asia-composite-map.png`** both updated in place — 5 new regions
  (Georgia, Abkhazia, South Ossetia, Azerbaijan, Armenia) render as real colored/hatched territory alongside
  Turkey/Iran/the Kurdish Nation, not gray out-of-scope hatch. Abkhazia and South Ossetia get their own
  distinguishable contested-hatch treatment (circle-hatch, distinct from each other and from Kirkuk/Israel-
  Palestine's "+"-hatch). Nagorno-Karabakh stays unrendered as its own case, reflected only in two of
  Azerbaijan's own 2021-created economic-region names — consistent with the source survey's own "resolved by
  force" finding.
- **Two flagged cross-region ties now actually drawn**, not just recorded as a recommendation: the Pan-Turkic
  sphere (S3) extended into real Azerbaijani territory plus a drawn connector arc to Anatolia ("one nation,
  two states," 2021 Shusha Declaration); Armenia's Yazidi population tied to the Kurdish Nation region via a
  deliberately light, low-confidence dotted-circle marker (not solid domain fill, since the survey itself
  flags this as an unsettled identity question, not just a sourcing gap).
- **A real geometry problem solved, not worked around**: Natural Earth only carries Azerbaijan at rayon/
  district level (78 features), not this project's 14-economic-region level. Fixed with a real, sourced
  rayon-to-economic-region mapping (Wikipedia's "Economic regions of Azerbaijan," cross-checked against every
  NE feature name) dissolved per region at render time — not a fallback or an approximation. One real gap
  remains: Lachin district (part of East Zangezur since 2021) has no Natural Earth polygon at all, flagged not
  fabricated, so that region renders very slightly incomplete on its western edge.
- **South Ossetia has no Natural Earth polygon at all** (confirmed by direct inspection of every Georgia-admin
  NE feature) — appears in both legends with its own color/confidence entry but is not visually drawn on
  either map this pass, disclosed in both footers rather than hidden.
- **Two real rendering bugs caught and fixed in this round**: the standalone Middle East map's legend/footer
  text collided after adding the 5 new regions (fixed by making the footer's y-position computed from where
  the legend content actually ends, rather than a hardcoded value — the same category of bug a prior round
  already hit once for the same reason); the new Pan-Turkic/Yazidi annotation labels initially overlapped
  other map content and were repositioned with backing boxes for legibility.

Georgia's and Armenia's own material resource bases beyond the transit-corridor/closed-border findings remain
flagged as real gaps, not researched further this pass.

**Divisions review, round 1, 2026-09-28** — `02 reorganization/03 follow-up - divisions - initial stages/`.
Author beginning to walk the Central Asia map region by region deciding what stays as-is vs. gets
repartitioned for the eventual nations layer.

- **✅ Kazakhstan — confirmed whole**, no changes. Matches "The Kazakh Steppe" region exactly (all 21
  subdivisions).
- **✅ Kyrgyzstan's south (Osh Region, Jalal-Abad Region, Batken) — confirmed staying in the Fergana Valley
  Tangle**, not repartitioned to either Kyrgyzstan or Uzbekistan wholesale. This came after a real research
  detour worth preserving: the author first floated "repartition it to Uzbekistan, since the USSR/Russian
  Federation that assigned it to Kyrgyzstan in 1924 won't exist by the First Interwar Period anyway." Real,
  sourced research (added to the frameworks survey as new §2.1) found the 1924 assignment genuinely was a
  bureaucratic override of ethnic demographics — Osh was 94% Uzbek by the 1923 census, but Kyrgyz negotiators
  won the territory on a stated economic-viability argument ("infringement of national arithmetic... reasons
  of economic character alone," 3rd Plenary Session, CC CPT, 14 Sept 1924), since the otherwise all-mountain
  Kyrgyz ASSR needed Osh/Jalal-Abad's urban and agricultural base to function. **But current whole-oblast
  demographics (2009 census, the finest grain this project's whole-subdivision rule allows) don't support the
  repartition-to-Uzbekistan case**: Osh Region is 68.6% Kyrgyz/28.0% Uzbek, Jalal-Abad 71.8%/24.8%, Batken
  mostly Kyrgyz with 14.7% Uzbek/6.9% Tajik — only Osh **city** itself is genuinely near-even (43%/48%, 2009).
  A 1924 bureaucratic land-grab, entirely by accident, now lines up with the actual oblast-level demographic
  majority a century later — likely via Kyrgyz internal migration and Uzbek emigration (especially post-2010
  Osh riots). **Settled 2026-09-28: leave the current Fergana Tangle treatment as-is** — not a full handover to
  either side, matching how genuinely split the ground truth actually is at the city/valley-floor level even
  though the surrounding countryside isn't.
  - **⚠️ Open item, explicitly parked by the author for a later session, not decided**: whether Osh specifically
    should additionally be classified as a "Disputed Territory." Author's own comparison was Transnistria —
    flagged as not quite a factual match as-is (Transnistria is a genuine functioning unrecognized breakaway
    state with its own government/currency/military and a Russian garrison; Osh Region today is ordinary,
    fully-administered Kyrgyz territory with a real history of ethnic violence, 1990 and 2010, but no
    breakaway government). Two options recorded as theoretically possible, neither chosen:
    1. Apply this project's existing Kirkuk/Israel-Palestine-style "contested" cross-hatch designation to Osh
       specifically — a flagged, unresolved status between claimant states, no breakaway government implied.
    2. Actually invent a Transnistria-style outcome for the setting — a real, functioning, unrecognized
       breakaway quasi-state emerging in Osh sometime before/during the First Interwar Period, the same shape
       of extrapolation Thailand's Deep South got (a real ongoing tension escalated into a new, designed
       post-collapse political fact) — this would need its own reasoning (who backs it, why it survives) built
       out before it's usable, not just a label.
    **Come back to this explicitly** — do not resolve it by default in either direction in a future session.
- **✅ Turkmenistan — confirmed whole**, no changes. Matches "The Turkmen Desert-Oasis" exactly (all 6
  subdivisions).
- **✅ Tajikistan's Sughd region — settled as core Tajik territory, moved OUT of the Fergana Valley Tangle**,
  the opposite call from Kyrgyzstan's south. Same research rigor applied: Sughd sits geographically inside the
  Fergana Valley system like Osh/Jalal-Abad/Batken did, but unlike them it's **84% Tajik / 14.8% Uzbek (2010
  census)** — a decisive majority, not a close call. It's also Tajikistan's economic engine (~60.8% of
  national industrial output, ~two-thirds of GDP) and was specifically transferred from the Uzbek SSR to the
  Tajik SSR in 1929 for the same economic-viability logic that gave Kyrgyzstan Osh/Jalal-Abad in 1924 — except
  here the demographic majority actually supports the assignment rather than overriding it. Real ongoing
  internal friction noted but not treated as grounds for a different territorial call: a substantial Uzbek
  minority, and the Khujand/"Leninabadi" elite that ran Tajikistan's government for nearly 40 years (WWII to
  the 1992-97 civil war) was deliberately excluded from power by the postwar settlement. Author's own words:
  "conclusively part of Tajikistan... There may be an Uzbek minority, and the two experience friction, but the
  country itself is fundamentally Tajik." New sourcing added to the frameworks survey's own §2.1 (alongside
  the Osh finding) and §3.5. **Applied to `central-asia-map-data/regions.csv` and both the standalone Central
  Asia map and the composite, re-rendered and self-verified 2026-09-28** — the Fergana Tangle now spans only
  Uzbekistan and Kyrgyzstan; the Vorukh/Kairagach point-enclaves (a separate, sub-subdivision-level fact) still
  render regardless. Working folder: `02 reorganization/03 follow-up - divisions - initial stages/`.
- **✅ Karakalpakstan — settled as an officially recognized Autonomous Zone within Uzbekistan**, not
  independent, not ordinary undifferentiated territory — closes out this project's own Tuva/BARMM-tier open
  case for Central Asia. Real historical grounding walked through before the decision: created 1925 inside
  *Kazakh* jurisdiction (not Uzbek), only transferred to the Uzbek SSR in 1936 as a late, somewhat arbitrary
  Soviet delimitation move; declared "sovereignty" in 1990 at the Soviet collapse, traded that year for an
  unfulfilled 1993 promise of a 20-year independence referendum; ~30 years of quiet compliance followed, but
  propped up by elite continuity and the total absence of any outside patron (unlike Russia's backing of
  Transnistria/Abkhazia) rather than by genuine settled harmony; ruptured once, badly, in 2022 when Tashkent
  tried to formally strip the dormant secession clause — the largest unrest in its post-Soviet history
  (~18-21 dead by the Uzbek government's own count). Author's reasoning: no active conflict or separatist
  movement at present, so the already-functioning autonomous arrangement stays as-is rather than being changed
  pre-emptively. **Applied to `central-asia-map-data/regions.csv`** — no re-render needed, since the region
  was already drawn as its own distinct color; just documented as settled rather than an open flag.
- **✅ Uzbekistan (Samarkand/Bukhara/Surxondaryo/Qashqadaryo regions) — stays as current whole territory for
  now**, but with a real future-development flag attached, not a closed question. The existing "Samarkand and
  Bukhara are historically Tajik/Persian centers" flag turned out to understate a much bigger, well-documented,
  currently live dispute: a real historical paper trail of deliberate census reclassification (Samarkand city,
  1920 census 44,758 Tajiks/3,301 Uzbeks → 1926 census 43,364 Uzbeks/10,716 Tajiks, the same population
  relabeled within six years), a huge current gap between official (4.8% national Tajik share) and
  Tajik-advocate (25-30%) population estimates, and specific claims that Samarkand city is ~70% and Bukhara
  city ~90%+ ethnically Tajik despite official statistics. **But at the whole-region level our map actually
  operates at, the disputed population is a city-core phenomenon, not a regional majority** — Bukhara Region's
  official Tajik population is ~60,898 of ~2 million; Samarkand Region is 63% rural with Tajik concentration
  confined to the city's historic core — the same shape as Osh city sitting inside majority-Kyrgyz Osh Region.
  Surxondaryo has an above-average but still clearly minority Tajik share (12.5% vs. 83% Uzbek); Qashqadaryo's
  own figure is an open gap. **Author's explicit future-development flag, not built or dated**: once Moscow's
  influence is gone, roughly the first half of the First Interwar Period could plausibly see this same
  grievance escalate into severe Tajik/Uzbek violence, potentially producing partial district-level breakaways
  from Uzbekistan to Tajikistan (most plausibly Samarkand/Bukhara city-adjacent districts specifically, not
  whole regions) — a real, sourced premise for a later session to design out properly, the same way Thailand's
  Deep South insurgency became a designed post-2083 independence outcome, not something to default into.
  Applied to `central-asia-map-data/regions.csv` and the frameworks survey's own §3.2 (new sourced subsection).
  No re-render needed — the map's existing treatment doesn't change, only the documentation behind it.

**Divisions review, Middle East/Caucasus side, round 1, 2026-09-28** — same working folder. Kurdish Nation
groundwork from the earlier round (Erbil settled KRI core; Kirkuk parked with two theoretical options, not
decided; Mosul/Nineveh flagged as under-researched at the sub-governorate level; Tikrit/Salah Al-Din a clean
non-Kurdish "no") carries forward unchanged.

- **✅ Afghanistan — confirmed whole territorially, no partition**, but with an important distinction drawn and
  recorded, not just a blanket "stays as-is." The author's own framing, precisely stated: Afghanistan's
  well-documented immunity to conquest (three failed Anglo-Afghan wars, the USSR 1979-89, NATO/US 2001-2021)
  is an immunity to **outside** conquest specifically — "any successful assault upon the country would come
  from inside, not from anybody looking to try and conquer." Real, precedented grounding for that distinction:
  the 1992-2001 civil war's Northern Alliance was a coherent, ethnically-organized coalition along almost
  exactly this map's own internal Tier-2 lines — Tajiks under Massoud, Uzbeks under Dostum, Hazara Shias under
  Khalili/Mohaqiq — fighting the Pashtun-dominated Taliban, each side with its own foreign backer (Iran vs.
  Pakistan). **The current Taliban government is actively re-priming that same fracture**: per the Middle East
  Institute's own May 2026 tracker, 90% of senior/mid-level Taliban figures are Pashtun against just 5.2%
  Tajik and ~3% Uzbek, despite Pashtuns being only 40-45% of the population; the 49-member cabinet has 2
  Tajiks, 2 Uzbeks, 2 Baloch, 1 Nuristani and essentially no Hazara or Shia representation; real power is
  reported concentrated in a narrow circle of Kandahari Pashtuns, with non-Pashtun officials reportedly being
  actively removed via arrests, dismissals, and in some cases killings. **Flagged for future development, not
  built or dated**: a real, sourced-enough premise for a later session to design a Northern-Alliance-style
  internal breakaway/civil-war outcome — the same category of parked item as Uzbekistan's Samarkand/Bukhara
  scenario and Osh's disputed-territory question. Applied to `middle-east-map-data/regions.csv`. No re-render
  needed — the map's existing territory/treatment doesn't change, only the documentation behind it.
- **⚠️ Nakhchivan (Azerbaijan) and Syunik (Armenia) — real, symmetric population history added, flagged as
  UNCERTAIN TERRITORY, explicitly parked for a later session, not resolved.** Author asked directly who lives
  on each end of the already-flagged Zangezur Corridor question. Both territories are today close to
  ethnically homogeneous, but arrived there by opposite mechanisms on very different timescales: **Nakhchivan**
  was 59%/40% Azerbaijani/Armenian as recently as 1916, declining under Soviet policy (15% Armenian in 1926 →
  1.4% in 1979) to today's effectively-zero Armenian population, capped by the deliberate destruction of the
  Julfa/Jugha khachkar cemetery (once possibly 10,000+ carved Armenian cross-stones), finally leveled entirely
  in December 2005. **Syunik** is the mirror image compressed into a few years instead of a century —
  Azerbaijanis were the single largest minority in Armenia as a whole across the entire 1831-1989 census
  record, until most fled or were forced out during the First Nagorno-Karabakh War (concentrated 1988-91);
  Syunik's own older Turkic name, **Zangezur**, is the direct namesake of the corridor dispute itself. Added to
  the frameworks survey's own new §3.1 and both subdivisions' notes in `south-caucasus-map-data/
  subdivisions.csv`. **Explicitly not resolved into any map treatment** — recorded as history only, come back
  to it deliberately in a future session, same as the Osh disputed-territory and Uzbekistan Samarkand/Bukhara
  items above.
- **✅ Iranian/"South" Azerbaijan (East Azerbaijan, Ardabil, West Azerbaijan's Azeri portion) — settled as
  staying part of Iran/Persia, not a live partition question the way the Kurdish Nation is.** Researched to
  the same depth as the Kurdish question, per the author's explicit request (new frameworks survey §3.8).
  Population scale rivals or exceeds the Kurdish case (16-24% of Iran's population by some estimates, Tabriz
  96.5% Azeri) and a real Soviet-backed secessionist state (the Azerbaijan People's Government) actually
  existed here in 1945-46 — but it collapsed within a year the moment Soviet troops withdrew, unlike Kurdish
  nationalism's real patron-independent institutional depth (the KRG, Peshmerga, PKK all persist regardless of
  any one foreign backer). **The load-bearing finding on why Tehran holds this region**: genuine Shia-identity
  elite integration, not coercion — Supreme Leader Khamenei and President Pezeshkian are both of Azerbaijani
  origin — the structural opposite of how Iran treats its Sunni Kurdish and Baloch minorities (the gozinesh
  loyalty-vetting system, documented employment/political exclusion, disproportionate death-penalty
  application). **Author's own settled read, following directly from this research**: without a
  Moscow-equivalent external patron providing the state apparatus itself (not just moral/financial backing,
  which is what 1945-46 actually depended on), this region's bargaining position against Tehran is
  structurally weak — one of the weakest separatist cases anywhere in the Middle East package. Real cultural
  grievances (no Azeri-language public education, limited media) persist and are flagged as a possible
  non-territorial story for later, not a territorial one. Applied to `middle-east-map-data/regions.csv`. No
  re-render needed.
- **✅ Yemen — settled as TWO states, North Yemen and South Yemen, not one.** Author asked what Yemen's history
  has "generally been" — the finding reframes the question: unification (only since 22 May 1990, and unstable
  every decade since — the 1994 civil war, the 2014 Houthi takeover, the STC's rival administration 2018 to
  its contested January 2026 dissolution, the live September 2026 Houthi offensive) is the young anomaly;
  division is the deep historical default. North Yemen's predecessor, a Zaydi Imamate, ruled the highlands
  continuously for roughly a millennium (until 1962); South Yemen had a completely separate 128-year British
  colonial trajectory (Aden captured 1839, independence 1967) producing the only Marxist state the Arab world
  ever had. **The split follows the real pre-1990 YAR/PDRY political border**, not the Zaydi-highland/
  Shafi'i-lowland religious split this file previously used as a proxy for it (the two overlap substantially
  but aren't identical — Ibb and Ta'izz are Shafi'i-majority religiously but were politically North Yemen).
  **One governorate doesn't divide cleanly: Dhale, created post-1990/1998 by stitching together 5 South
  Yemen/Lahij districts and 4 North Yemen/Ibb-Ta'izz districts, plus a pre-state identity of its own as the
  historic Emirate of Dhala — settled as officially recognized Disputed Territory between the two new states**,
  the same Kirkuk-style treatment, and the same structural case as Kaliningrad or the Fergana enclaves. New
  frameworks survey §5.5; applied to `middle-east-map-data/regions.csv` (Yemen's single region replaced by
  `north_yemen`, `south_yemen`, and `dhale_disputed`). **Re-render needed** — this changes the actual drawn
  regions on both the standalone Middle East map and the composite, unlike the Afghanistan/Azerbaijan items
  above which only changed documentation. **✅ Re-rendered and self-verified 2026-09-28** — North Yemen
  (`#7A9B4E`, olive) and South Yemen (`#3D7A6E`, teal) render as two clearly distinct regions along the correct
  real historical line (Ibb and Ta'izz correctly land in North Yemen, the one place the old religious-cultural
  line would have gotten it wrong); Dhale renders as its own small cross-hatched "DHALE (DISPUTED TERRITORY)"
  patch sitting exactly on the seam; Socotra still reads as its own flagged case within South Yemen. **Real risk
  caught and fixed during the render**: `middle-east-render.py` was auto-regenerating `regions.csv` from its
  own hardcoded per-region notes at the end of every run, which would have silently destroyed every
  hand-authored note in that file (the Iranian Azerbaijan §3.8 writeup, this very Yemen-partition reasoning,
  etc.) the next time the script ran — that auto-write block has been disabled, and `regions.csv`'s integrity
  was confirmed intact afterward.
- **✅ Kurdish Nation/Anatolia border redrawn along the Taurus-Zagros mountain belt** — the first actual
  border-cleanup pass on this map, following directly from the Taurus-Zagros overlay work above. Author
  identified the border as "oddly-shaped" and, after checking whether any natural feature could clean it up
  (rivers, mountain ranges, Turkey's own official geographic regions — none of which worked cleanly on their
  own), landed on the real Taurus-Zagros mountain belt as the dividing logic. **Tunceli, Bingöl and Muş move
  from the Kurdish Nation's domain into Anatolia's core** — a real geological case (Muş's plain is explicitly
  bounded south by the Bitlis Mountains, part of the actual suture zone; Tunceli sits in its own separate
  highland basin, the Munzur Mountains) traded openly against a real demographic one (Bingöl and Muş are both
  recorded elsewhere in this file as straightforwardly Kurdish-majority, same tier as the provinces that stay
  in the domain) — the same "clean shape over perfect fidelity" tradeoff this project's North America map
  already makes (Cascadia and the CSA both collapse multiple Woodard regions). **A standing expectation of
  ethnic/sectarian violence along this exact seam is now recorded explicitly** (new frameworks survey
  addendum after §3.7) — not a specific predicted event, but a flagged structural premise for a later session,
  the same category as Uzbekistan's Samarkand/Bukhara scenario or Afghanistan's Northern-Alliance premise.
  Applied to `middle-east-map-data/regions.csv`. **✅ Re-rendered and rigorously self-verified 2026-09-28** —
  after an initial visual check looked ambiguous given how busy this area of the map is, verification was
  redone by plotting actual markers at Tunceli/Bingöl/Muş/Diyarbakır's real centroids using the render
  script's own coordinate pipeline: all three moved provinces landed cleanly inside Anatolia, the Diyarbakır
  control point stayed correctly inside Kurdish Nation domain, confirmed on both the standalone map and the
  composite. `regions.csv` confirmed untouched by the render run (same MD5 before and after).
- **⚠️ Flagged future border seam, 2026-09-28, explicitly not resolved**: the author is considering the real
  Tekirdağ/Istanbul provincial border in East Thrace (near Tekirdağ's Çorlu/Çerkezköy vs. Istanbul Province's
  Silivri/Büyükkılıçlı-Küçükkılıçlı) as Anatolia's own eventual western edge once this project's Europe region
  exists — Tekirdağ, Kırklareli and Edirne (all of Turkey's European territory outside Istanbul Province
  itself) would sit on the far side of it. **Explicitly not decided or applied now** — author's own words:
  "it's not necessary to start thinking about Greece and/or Bulgaria... we'll get to that once we start doing
  Europe." Anatolia keeps all of East Thrace for now. Same category as Russia's own once-deferred Outer
  Manchuria/Sakhalin/Buryatia-Tuva seams before East Asia existed to resolve them. New frameworks survey note
  after §7.1; applied to `middle-east-map-data/regions.csv`'s Anatolia note. No map change, no re-render.
  **✅ RESOLVED 2026-09-30 (author, Europe session):** Tekirdağ, Kırklareli and Edirne **leave Turkey**: **Edirne and Tekirdağ go to Greece, Kırklareli to Bulgaria** (Turkey's western edge is now the Tekirdağ/Istanbul provincial line; Istanbul Province stays Turkish). Applied in `y-files/Map Files/Asia (West)/02 reorganization/08 follow-up/` (the middle-east and composite maps re-rendered, the three provinces drawn as gray out-of-scope territory; Central Asia's map unchanged; see that folder's CHANGES.md) and in `middle-east-map-data/regions.csv` (turkey row: 68 to 65 member provinces) and `subdivisions.csv` (the three rows marked MOVED). Decision record: Europe `02 follow-up/DECISION LOG - Confederacy of Intermarium Nations (membership order).md` §6c.

**Divisions review, round 2, 2026-09-28** — `02 reorganization/04 follow-up - further borders/`.

- **✅ Afghanistan — confirmed as-is, divisions review closed.** Author explicitly reviewed both Afghanistan's
  overall territorial extent and its internal Pashtun/Tajik/Hazara/Uzbek Tier-2 sub-zone borders and found no
  reason to change either: "we can pretty much leave its borders as-is." Applied to
  `middle-east-map-data/regions.csv`. No map change.
- **✅ Halabja (Iraq) — confirmed as-is, sub-question closed.** Author asked about the skinny governorate-shaped
  strip along the Iranian border containing Halabja/Ababayle/Pshta. Researched to the same depth as the other
  border cases: unlike the Turkish/Iranian domain provinces under review this round, Halabja isn't a flagged
  minority province of a non-Kurdish state — it split from Sulaymaniyah in 2014 as the KRI's own 4th governorate
  (Iraq's 19th nationally as of April 2025), already on the same uncontested core footing as Erbil/Duhok/
  Sulaymaniyah, and it's the site of the March 1988 Halabja chemical attack (the defining atrocity of Saddam's
  Anfal campaign against the Kurds) — among the least ambiguous Kurdish territory on the map. Its narrow shape
  reflects real terrain (a valley corridor to within ~14 km of Iran), not a classification artifact. Applied to
  `middle-east-map-data/regions.csv`'s `kurdish_nation`/core note. No map change.
- **✅ Khanaqin/Diyala (Iraq) — settled, marked Disputed Territory.** Author spotted a real, odd "stick" shape —
  Diyala Governorate's actual northeastern panhandle — wedged between Iraqi and Iranian Kurdish territory on the
  render and asked about it. Researched: that panhandle is Khanaqin District, formally listed among the
  "disputed territories of Northern Iraq" under Article 140 of the Iraqi Constitution — the identical legal
  status Kirkuk holds — de facto split between Diyala and Sulaymaniyah/KRG administration, genuinely mixed
  Kurdish/Arab/Turkmen (frameworks survey §3.9). Since this project has no admin-2 (district-level) Iraq geometry
  to carve Khanaqin out precisely, the author chose to mark **all of Diyala** contested (same tier/hatch as
  Kirkuk) rather than leave it disclosed-but-invisible the way Lebanon's confessional mosaic was — a disclosed
  tradeoff that overstates the dispute's true extent in exchange for actually showing it. Applied to
  `middle_east_classify.py` (`IRAQ_CONTESTED` now `{"Kirkuk", "Diyala"}`) and `regions.csv`'s `mesopotamia`
  contested/sunni_mixed rows. **Re-rendered and rigorously re-verified** — `regions.csv` confirmed untouched by
  MD5 before/after, and the Diyala panhandle confirmed showing Kirkuk-style cross-hatch on the actual output PNG.
- **✅ Raqqa (Syria) — settled, moved from Kurdish Nation's domain to Levant's core.** Author asked about the
  area between Ayn Issa and Lake Assad (i.e. Raqqa Governorate, including Raqqa city). Researched: Raqqa is
  ~90% Sunni Arab overall, and still ~70% Arab even in its most-Kurdish district (Tell Abyad, home to Ayn Issa),
  where Kurds are only ~25% and concentrated in the district's western part — the weakest demographic case for
  Kurdish Nation domain status anywhere on this map. Its old placement tracked SDF/AANES political and military
  control (Raqqa served as a DAANES administrative center), not the population living there, which runs against
  this map's own stated method of drawing culture/ethnicity as the primary layer. Al-Hasakah, Raqqa's former
  domain-mate and Syria's actual historic Kurdish heartland (the Jazira region), is unaffected and stays.
  Applied to `middle_east_classify.py` (`SYRIA_KURDISH` now just `{"Al-Hasakah"}`) and `regions.csv`'s
  `kurdish_nation`/domain and `levant`/core rows. **Re-rendered and rigorously re-verified** via the render
  script's own live coordinate transform (debug star markers at Raqqa's and a Aleppo control's real centroids
  both landed in solid Levant territory; an Al-Hasakah control star correctly stayed in Kurdish Nation domain) —
  `regions.csv` confirmed untouched by MD5 before/after.
- **✅ Nineveh (Mosul) — real disputed periphery found, deliberately left unrendered.** Author asked whether
  Nineveh deserved the same Disputed Territory treatment just given to Diyala/Khanaqin. Researched: Sinjar
  District (majority Yazidi, ~249,000 people), the Nineveh Plains (Tel Kaif/Hamdaniya/Shekhan — Shabak/Assyrian-
  Chaldean Christian/Yazidi/Kurdish/Turkmen mix), and parts of Tel Afar are all real, sourced Article 140
  disputed territories, same legal list as Khanaqin. But unlike Diyala, Nineveh's capital IS Mosul — a massive,
  unambiguously Sunni Arab city never seriously part of the KRG's claims — so governorate-level contested status
  here would overstate the dispute far more than it did for Diyala. Author's own call after that tradeoff was
  laid out: "if that's the case, then it makes sense for it to stay part of Iraq." Nineveh stays plain
  `mesopotamia`/`sunni_mixed`, unchanged. Full sourcing recorded in frameworks survey §3.11 and `regions.csv`'s
  sunni_mixed note — flagged, not hidden, same posture as Lebanon's dropped confessional mosaic — but
  intentionally NOT rendered. No map change, no re-render needed.
- **✅ "The Levant" split into Syria and Jordan, each its own named region.** Author's own words: "the remaining
  area of Syria that hasn't been partitioned away, that area, we can recognize as Syria." The old `levant`
  region combined Syria's core territory (minus its Kurdish/Alawite/Druze flags) with Jordan under one generic
  label — inconsistent with how every other real, sovereign country on this map (Lebanon, Israel, Palestine)
  already gets its own name. Author confirmed splitting Jordan out too, for the same consistency reason, when
  asked. Applied: `middle_east_classify.py`'s `REGIONS` dict (`levant` → `syria` keeping its old maroon
  `#8A3E2E`, plus new `jordan` in sage-olive `#7D8C6E`) and `classify()`'s Syria/Jordan branches;
  `regions.csv`'s three former `levant` rows re-tagged `syria` (alawite/core/druze) plus a new `jordan`/core
  row; both render scripts' legends, confidence dicts, and (in the composite) label positions and legend-order
  lists updated to match. **Re-rendered both maps and visually confirmed** — the standalone map's legend now
  lists Syria and Jordan separately with Jordan's new color visible on the map itself, and the composite map's
  region labels now read "SYRIA" and "JORDAN" as separate names. `regions.csv` confirmed untouched by MD5
  before/after both render runs.
- **✅ "Anatolia," "Mesopotamia," and "Persia" renamed to Turkey, Iraq, and Iran.** Author's own words: "what
  hasn't been partitioned away from Anatolia, Mesopotamia, and Persia, we can settle those as Turkey, Iraq, and
  Iran" — the same consistency logic as the Levant → Syria/Jordan split just above, closing out the last three
  generic cultural-region labels standing in for real, still-sovereign countries with nothing left to partition.
  Applied: `middle_east_classify.py`'s `REGIONS` dict (colors kept identical for continuity) and `classify()`'s
  Turkey/Iraq/Iran branches; `regions.csv`'s `anatolia`/`mesopotamia`/`persia` rows re-tagged `turkey`/`iraq`/
  `iran` (tiers and member subdivisions unchanged); both render scripts' confidence dicts, connector code (S3
  Pan-Turkic, S4 Persianate Bridge), and — in the composite — label positions and legend-order lists updated to
  match. **Re-rendered both maps and visually confirmed** — the standalone map's legend now reads Turkey/Iraq/
  Iran, and the composite map's own region labels now read "TURKEY," "IRAQ," and "IRAN" directly on the canvas.
  `regions.csv` confirmed untouched by MD5 before/after both render runs.
- **✅ "The Kurdish Nation" renamed to Kurdistan.** Author's own words: "the territories that are now marked as
  decidedly in Kurdish Nation, we can go ahead and call that Kurdistan." Applied: `middle_east_classify.py`'s
  `REGIONS` dict (`kurdish_nation` → `kurdistan`, color unchanged) and `classify()`'s four Kurdistan-returning
  branches; `regions.csv`'s two `kurdish_nation` rows (core/domain) re-tagged `kurdistan`; both render scripts'
  confidence dicts, connector/centroid lookups, legend-order lists, and every on-map caption/annotation/legend
  line mentioning "the Kurdish Nation" (including the small Armenia-Yazidi-tie annotation, caught on a second
  pass since it wrapped across lines) updated to "Kurdistan." **Re-rendered both maps and visually confirmed** —
  `regions.csv` confirmed untouched by MD5 before/after.
- **✅ "Iran" renamed to Persia, 2026-09-29 (one day after Iran was settled) — an in-world naming choice, not a
  reversal.** Author's instinct: post-war Iran is "finally a secular society, and they would identify themselves
  by their historical name." Real nuance researched and disclosed before applying: "Iran" is actually the
  ancient native endonym (Sassanid-era, 1,700+ years), while "Persia" is the Greek exonym the outside world used
  instead — so this isn't "restoring an older name," it's the post-war citizenry deliberately adopting a name
  that carries real symbolic charge today (Iranian monarchists, diaspora, and secular nationalists favor
  "Persia" specifically to signal a break from the "Islamic Republic of Iran" era and evoke pre-Islamic
  heritage) — exactly the in-world logic here. Applied: `middle_east_classify.py`'s `REGIONS` dict (`iran` →
  `persia`, color unchanged) and `classify()`'s four Persia-returning branches (nation-string checks against
  real-world "Iran" in Natural Earth data are untouched — only the map-facing region_id/name changed);
  `regions.csv`'s four `iran` rows (core/azeri/arab/baloch) re-tagged `persia`; both render scripts' confidence
  dicts, connector code (S4 Persianate Bridge), label positions, and legend-order lists updated to match.
  **Re-rendered both maps and visually confirmed** — the composite map's own region label now reads "PERSIA"
  directly on the canvas. `regions.csv` confirmed untouched by MD5 before/after both render runs.
- **🔄 Ilam (Iran) — open, not yet settled.** Author proposed the same "keep in Iran" treatment for Ilam,
  Kurdish Nation's southernmost Iranian domain province, paralleling the Tunceli/Bingöl/Muş redraw. Unlike that
  case, the parallel doesn't hold cleanly: Ilam's Kurdish/Lak population offers a weaker identity-ambiguity case
  than Tunceli's Zaza/Alevi question, and geologically Ilam itself straddles both sides of the Zagros divide
  (real highland terrain in its north/east, a Mesopotamian-lowland-extension plain in its southwest bordering
  Iraq) rather than sitting cleanly on one side the way Muş's plain did. Presented to the author with this
  tension disclosed; awaiting their call before any edit to `regions.csv` or a re-render.
- **✅ New cross-border region: Balochistan, 2026-09-29 — reaches outside this project's normal scope.**
  Author's own scenario, following a demographic/social/geological research pass on Persia's Sistan and
  Baluchestan: "The Balochi areas of Persia, Afghanistan, and Pakistan successfully unite and gain control over
  a seaport." Real anchors, not invention: Baloch separatists already declared a "Republic of Balochistan" from
  Pakistan in May 2025 (not recognized by Islamabad, which still fights the insurgency); Chabahar, Iran's only
  oceanic port, already sits inside Sistan and Baluchestan, so the seaport goal needs no reach beyond Persia's
  own territory. Author explicitly directed that Pakistan's Balochistan province be drawn on the map despite
  Pakistan/South Asia being out of this project's scope — "since what had previously been part of Pakistan is
  now part of this map scope anyway" — and that Afghanistan's already-flagged Nimruz (Baloch-majority ~60%) be
  folded in too. Checked and ruled out Helmand (92% Pashtun) and Farah (80% Pashtun) as alternative Afghan
  pieces — Nimruz alone is correct.
  - Applied: new `PAKISTAN_BALOCHISTAN` handling and a new `balochistan` region in `middle_east_classify.py`
    (core = Iran's Sistan and Baluchestan + Pakistan's Baluchistan; domain = Afghanistan's Nimruz, moved out of
    `persia`/baloch and `afghanistan`/baloch_mix respectively); one new row added to `subdivisions.csv`
    (Pakistan/Baluchistan, population 14,894,402 per Pakistan's 2023 census) plus updated notes on the Iran and
    Afghanistan rows; `regions.csv`'s `persia`/baloch and `afghanistan`/baloch_mix rows removed, two new
    `balochistan` rows added (the displaced general-Afghanistan note relocated to the `afghanistan`/pashtun
    row rather than lost); both render scripts' confidence dicts, and — in the composite — label position and
    legend-order list, updated to match. New frameworks survey §9 with full sourcing.
  - **Geometry confirmed available before committing**: Natural Earth's admin-1 dataset carries Pakistan's
    "Baluchistan" province (PAK-1108) directly — no fabrication needed. The rest of Pakistan remains an
    ordinary out-of-scope gray neighbor on both maps (already in both scripts' `neighbors`/`OTHER_NEIGHBORS`
    lists), confirmed unaffected by this one province's addition.
  - **Re-rendered both maps and rigorously verified**: matched subdivisions rose from 327/331 to 328/332 (the
    expected +1, no new errors); a direct crop of the standalone map's render confirmed Iran's and Pakistan's
    Balochistan pieces render as one continuous solid-red core territory across the (invisible) international
    border, with Nimruz's lighter dotted-red domain tier correctly bridging to Afghanistan, and the rest of
    Pakistan still correctly gray-hatched "out of scope." The composite map's own region label now reads
    "BALOCHISTAN" directly on the canvas. Both `regions.csv` and `subdivisions.csv` confirmed untouched by MD5
    before/after both render runs.
- **✅ Nimruz upgraded from domain to core tier within Balochistan, same day.** Author's follow-up instruction:
  "that slice of Afghanistan that's designated as majority Balochi should also be included." Nimruz now renders
  with the same solid fill as Iran's Sistan and Baluchestan and Pakistan's Baluchistan — full, equal inclusion
  rather than a lighter tie. Applied to `middle_east_classify.py` (Nimruz's branch now returns
  `("balochistan", "core")`) and `regions.csv` (the domain row merged into the core row's member list and
  note). Re-rendered both maps and visually confirmed — Nimruz is now visually indistinguishable in tier from
  the rest of Balochistan's territory. Both CSVs confirmed untouched by MD5 before/after.
- **✅ Afghanistan's remaining territory confirmed conclusively Afghanistan, same day.** With Nimruz's carve-out
  to Balochistan applied, author explicitly reaffirmed everything else — Pashtun, Tajik, Hazara, Uzbek/Turkmen,
  Nuristani, and the mixed_sourced/mixed_extrapolated provinces — as settled: "the rest of what we understand
  to be Afghanistan (that hasn't been partitioned away), mark as conclusively Afghanistan." Applied to
  `regions.csv`'s `afghanistan`/pashtun row. No map/data change — Afghanistan's territory and tiers were
  already correct; this closes the loop opened by the Nimruz carve-out. No re-render needed.
- **Panjshir's map gap explained, not a bug**: author asked about a blank white patch on the render near Kabul.
  It's Panjshir Province — Afghanistan's newest province (split from Parwan in 2004), which has no Natural
  Earth polygon at all and has been flagged as unmatched in every render this session ("Afghanistan / Panjshir"
  in the unmatched list). Sits correctly in the Hindu Kush foothills northeast of Kabul, surrounded by the
  dotted Tajik-tier territory — Panjshir itself is overwhelmingly Tajik and was Ahmad Shah Massoud's stronghold
  against both the Soviets and the Taliban. No action taken; this is a known, disclosed geometry gap (see the
  map's own footer), not something to fix by fabricating a boundary.
- **✅ Panjshir's gap actually fixed, same day — real sourced geometry found, not fabricated.** Author asked
  directly whether the gap could be colored in. Investigation found Natural Earth actually does carry Panjshir's
  real shape — it just carries it as a SECOND feature both named/woe_named "Parwan" (adm1_code AFG-1769 and
  AFG-1772), a duplicate-name artifact from Panjshir's 2004 split off from Parwan that NE never fully relabeled.
  NE's own `gn_name` (GeoNames) field disambiguates the two correctly (AFG-1769=Panjshir, AFG-1772=Parwan),
  confirmed by plotting both against Panjshir's and Parwan's real capitals (Bazarak vs. Charikar) — a clean
  bbox/centroid match for each. **A real latent bug was also caught in the process**: the pre-fix ambiguous
  name-match could have been silently drawing either ("Parwan"'s own subdivisions.csv row) with Panjshir's
  shape instead of its own, non-deterministically, in every prior render — this is the same class of duplicate-
  name mislabeling already known and worked around for Daykundi/Uruzgan, just not previously noticed here.
  Applied: explicit `gn_name`-based matching for both "Panjshir" and "Parwan" added to both render scripts'
  `match_geometry()`/`me_match_geometry()` functions; `subdivisions.csv`'s Panjshir and Parwan rows both updated
  with the finding. **Re-rendered both maps and visually confirmed** — matched subdivisions rose from 328/332 to
  329/332 (Panjshir no longer in the unmatched list), and a direct crop of the Kabul-area gap shows Panjshir now
  filled with its correct dotted Tajik-tier texture, matching its neighbors. Both CSVs confirmed untouched by
  MD5 before/after both render runs.
- **✅ Remaining Turkey/Kurdistan border officially settled, closing out the last un-reviewed segment.** With
  Tunceli, Bingöl and Muş already redrawn via the Taurus-Zagros logic, the author explicitly confirmed the
  other 13 Turkish domain provinces (Adıyaman, Ağrı, Bitlis, Diyarbakır, Hakkâri, Mardin, Siirt, Batman,
  Şırnak, Van, Şanlıurfa, Kars, Iğdır) as officially drawn: "so far as the border between Turkey and Kurdistan,
  we can settle the currently-drawn border as official." Applied to `regions.csv`'s `kurdistan`/domain row. No
  map change, no re-render — this only closes out documentation for a border that isn't changing.
- **✅ Khuzestan marked "Unstable Territory" — new region, deliberately not resolved between two real paths.**
  Author asked for the case on Khuzestan; research found a much richer history than the existing internal-
  minority flag captured — the real pre-1925 Emirate of Muhammara ("Arabistan"), suppressed by Reza Shah and
  its name erased by 1936, plus a real continuous separatist history (1979 APCO uprising, the 1980 Iranian
  Embassy siege in London by the "Arab Popular Movement in Arabistan," a 2018 Ahvaz military-parade attack and
  subsequent crackdown). Key nuance found: Saddam Hussein's 1980 invasion expected Khuzestan's Shia Arabs to
  welcome union with Iraq — they didn't, staying loyal to Tehran's Islamic Republic on sectarian grounds. But
  this project's own settled decision that post-war Persia turns secular removes exactly that religious tie,
  reopening a real "reunify with Iraq's Shia south" path alongside the better-precedented "independent
  Arabistan" path. Author's own call: "for now, let's mark it as unstable territory," rather than choosing
  between them. Applied: new `khuzestan_unstable` region in `middle_east_classify.py` (contested tier, same
  "+++" hatch as Kirkuk/Dhale) and `regions.csv` (moved out of Persia's own internal `arab` flag, which no
  longer exists as a separate row); `subdivisions.csv`'s Khuzestan note updated; both render scripts' confidence
  dicts, and — in the composite — label position and legend-order list (including the hatch-assignment list),
  updated to match. New frameworks survey §10 with full sourcing. **Re-rendered both maps and rigorously
  verified** — matched-subdivision count unchanged (329/332, as expected for a pure reclassification with no
  geometry change), and a debug-marker check (Khuzestan's real centroid plotted via the render script's own
  live coordinate transform, a Tehran control point plotted alongside it) confirmed Khuzestan lands correctly
  in the new cross-hatched `khuzestan_unstable` territory while Tehran stays correctly in plain Persia core.
  Both CSVs confirmed untouched by MD5 before/after both render runs.
- **✅ Lebanon's confessional hatch, dropped entirely at Stage 4, partially restored.** Author picked Lebanon
  as the next region to develop. Investigation found the original "overlapping, misleading hatching" note
  overstated the problem — checked Natural Earth's actual 6-polygon geometry against the OVERRIDES mapping
  (`middle_east_name_map.py`) governorate-by-governorate: South and Nabatieh each have their own clean,
  unshared polygon (Shia, no conflict); Mount Lebanon and Keserwan-Jbeil share one polygon but both are
  genuinely Maronite-heavy (flagging the shared shape is accurate); only Baalbek-Hermel/Beqaa is a real,
  unresolvable conflict (Beqaa proper isn't Shia-majority), so that one flag was dropped and disclosed instead
  of rendered. Applied: `LEBANON_SHIA`/`LEBANON_MARONITE` sets updated and activated in `classify()`
  (`middle_east_classify.py`); `regions.csv`'s single `lebanon`/core row split into core/shia/maronite rows;
  `subdivisions.csv`'s Baalbek-Hermel note updated with the geometry-conflict disclosure; composite script's
  `ME_TIER_HATCH` gained the missing `maronite` entry. **Re-rendered both maps and rigorously verified** — a
  debug-marker pass confirmed no tier conflicts on any shared geometry (Mount Lebanon/Keserwan-Jbeil both
  `maronite`; Baalbek-Hermel/Beqaa both `core`; Akkar/North both `core`), and — since Lebanon is tiny enough
  that oversized debug markers obscured the whole country at first — a pixel-color scan located Lebanon's
  actual fill precisely, and a zoomed crop confirmed the north renders plain, the coastal Mount Lebanon belt
  renders cross-hatched, and the south renders diagonal-hatched, exactly as intended. Frameworks survey §4.3
  updated. Both CSVs confirmed untouched by MD5 before/after both render runs.
- **✅ Iraq confirmed as-is — the broader Sunni/Shia split closed out, no map change.** Author walked through
  Iraq's full internal treatment (Kirkuk/Diyala contested, the Sunni-mixed north/center, the Shia south) and
  confirmed it stands as officially depicted: "let's just leave Iraq as-is, as it's currently depicted on the
  map." Along the way, verified a few points of confusion directly against the render rather than assuming:
  confirmed Kirkuk and Diyala render identically (same grid cross-hatch, both "contested" tier — Kirkuk sits
  further north adjacent to Kurdistan's core, Diyala is more central-east between Baghdad and Iran, neither is
  in the southern Shia bloc); confirmed the "diagonal hatching" the author had in mind is actually the
  separate Shia tier (Wasit, visible just south of Diyala), not a different treatment of Kirkuk/Diyala
  themselves. Researched Wasit specifically as a representative case of the Shia south (capital Al-Kut, ~1.64M
  people per 2024 census, genuinely Shia-majority with small Marsh Arab/Feyli Kurd pockets, real Iran-Iraq War
  and 2004 Mahdi Army history). Applied: a full geographic-composition writeup for future reference (frameworks
  survey's new §4.4, covering the contested pair, the Sunni-mixed north/center including Baghdad's own
  disclosed default-bucket status, and the Shia south) plus a confirmation note on `regions.csv`'s `iraq`/
  sunni_mixed row. No map change, no re-render — this closes out documentation only.
- **✅ Syria's Alawite/Druze flags confirmed staying part of Syria, no partition.** Author's words: "those
  Alawite/Druze areas can be officially recognized as part of Syria." Applied to `regions.csv`'s `syria`/
  alawite and `syria`/druze rows. Both remain flagged minority-population hatches within Syria's own core
  territory, unchanged visually — this only closes the open question of whether either might separate. No map
  change, no re-render.
- **✅ Azraq/Ruwaished repartition-to-Arabia considered, declined.** Author asked about the demographics of
  these two eastern-desert Jordanian border towns as part of developing Jordan. Research found both are real
  exceptions to their governorate's assumed character — Azraq (Zarqa Governorate) has a documented Druze
  community, distinct from Zarqa city's own Palestinian-refugee-descended urban core; Ruwaished (Mafraq
  Governorate, the farthest-east Jordanian settlement, on the Iraq border) showed only 67.5% Jordanian
  citizens, unusually low, likely reflecting Iraqi refugee/migrant presence. Author considered repartitioning
  this area to Arabia but declined once both figures confirmed real Jordanian-citizen majorities (67.5% and
  84.5% respectively): "if they're majority Jordanian, just leave it as-is." Applied to `subdivisions.csv`'s
  Mafraq and Zarqa rows. No map change, no re-render.
- **🔄 Israel/Palestine post-collapse scenario — in active development, one piece settled.** Author is building
  a mutual-nuclear-exchange scenario growing out of this project's already-established "2026 Iran war" (§6),
  not a single-actor collapse. Grounded in real facts researched this session: Israel's own undeclared nuclear
  arsenal (~90-100 warheads, Dimona), its population/state apparatus concentration in identifiable strategic
  nodes (Tel Aviv/Gush Dan, Haifa, Beer Sheva/Dimona), and its real layered missile defense (Iron Dome, David's
  Sling, Arrow 2/3) — meaning the mechanism collapses the *state* without implying total population loss, and a
  real, dispersed surviving population is expected. **✅ Settled piece: Jerusalem takes no damage at all** and
  becomes a neutral city under mutually shared international administration — author's own words, "nobody
  anywhere wants to cause harm to it because everybody has a vested-interest stake in its existence." This
  connects to a real precedent already in the frameworks survey: the 1947 UN Partition Plan's own proposed
  Jerusalem corpus separatum (international administration), never implemented before the 1948 war overtook
  it. **Update, same session — governance and territory also now settled**: Hamas does not survive as a
  governing force (author's explicit call, "I really really don't like the idea of Hamas being allowed to
  exist," grounded in Hamas losing its Iranian patron in the same war plus Israel's own already-ongoing
  campaign against it); the Palestinian Authority becomes the official government; all of former Israel's
  territory becomes Palestine except Jerusalem. **This has now been applied to the map** — see the fuller entry
  below (search "Hamas does not survive") for the full implementation and verification detail. Frameworks
  survey §2.7 documents the complete scenario. **Still explicitly open**: the specific status of Israel's
  surviving dispersed population within Palestine, and the West Bank settler population's own status.
- **✅ Hamas does not survive as a governing force; the Palestinian Authority absorbs all of former Israel's
  territory as Palestine — applied to the map.** Following directly from the Jerusalem-spared decision above:
  author's explicit call on Hamas specifically ("I really really don't like the idea of Hamas being allowed to
  exist"), grounded in a real mechanism rather than fiat — Hamas is part of Iran's "Axis of Resistance" network,
  dependent on it for funding/arms/training; with Iran devastated in the same mutual nuclear exchange, combined
  with Israel's own already-documented ongoing campaign against it (§2.5's "de facto limited war"), Hamas loses
  its patron at the moment it's already being ground down militarily. The Palestinian Authority is left as the
  sole functioning government and absorbs the territory: "The Palestinian Authority becomes the official
  government, and all that land becomes Palestine." Not a negotiated transfer — a one-state outcome arrived at
  by state collapse, the same way this project's other "government left standing" scenarios work. Real
  precedent within this project: Jordan's own history (§5.3) of naturalizing ~1 million Palestinian refugees as
  full citizens after 1948.
  - **Applied**: `middle_east_classify.py`'s `REGIONS` dict retired "israel" entirely, added new "jerusalem"
    region (`#D9C08A`, Jerusalem-stone limestone color); `classify()`'s Israel branch now returns
    `jerusalem`/core for Jerusalem District, `palestine`/core for every other former Israeli district
    (including Judea and Samaria Area — no longer a separate contested claim); Palestinian Territories' own
    Jerusalem (al-Quds) also now returns `jerusalem`/core. `regions.csv`'s old `israel`/core and
    `israel`/contested rows removed; `palestine`/core expanded to absorb all six former Israeli districts; new
    `jerusalem`/core row added. Both render scripts' now-obsolete Israel/Palestine contested-overlap drawing
    code removed (would have crashed on the retired `REGIONS["israel"]` lookup in the standalone script, since
    it referenced that color directly). Caption/footer text in both scripts updated. `subdivisions.csv`'s
    Israel and Palestinian Territories Jerusalem-related rows fully annotated with the settled reasoning.
  - **Re-rendered both maps and rigorously verified**: matched-subdivision count unchanged (329/332, a pure
    reclassification, no geometry change); a debug-marker pass confirmed Jerusalem District, Jerusalem
    al-Quds, Tel Aviv, Gaza, and Judea and Samaria Area all classify correctly (`jerusalem`/core vs.
    `palestine`/core as expected); a zoomed crop of the actual composite-map output confirmed Jerusalem renders
    as its own distinct, solid tan-colored neutral region, clearly bordered off from the now-expanded purple
    Palestine (which was confirmed reaching Tel Aviv). `regions.csv` confirmed byte-identical (same MD5) across
    the final subdivisions.csv-note-only re-render pass.
  - **Explicitly still open**, not decided: the specific status of Israel's surviving dispersed population
    within the new Palestinian state (full equal citizenship vs. a "domain"/flagged-minority model like Adjara
    or Iranian Azerbaijan elsewhere on this map — raised, not chosen), and the West Bank settler population's
    own specific status given the occupation history behind it.
  - **Note for future reference** (author's own stated goal, this session: building toward a wiki-style
    reference site from this project's accumulated notes): frameworks survey §2.7 is written as the single
    complete account of this whole scenario — mechanism, Jerusalem, governance, territory, and the two
    remaining open questions — specifically so it can be pulled forward into that future site directly.
- **✅ Jordan's proposed Palestinian-population flag declined — resolved via return migration, not left open.**
  Following directly from the Israel/Palestine settlement above: author's own words, "Jordan's Palestinian
  refugees are able to return to Palestine, thus making Jordan unquestionably Jordanian-majority." This
  resolves the flag proposed earlier this session (Amman/Zarqa/Irbid/Jerash/Balqa, the real geographic
  concentration of Jordan's Palestinian-descended population) — rather than applying it, it's declined for a
  specific in-world reason: with Palestine now holding vastly more territory following Israel's collapse, the
  population that had been displaced there for decades is framed as returning rather than permanently settled.
  This also resolves the Azraq/Ruwaished repartition question in the same direction it was already trending.
  Applied to frameworks survey §5.3 (full reasoning) and `subdivisions.csv`'s Amman, Zarqa, Irbid, Jerash, and
  Balqa rows (cross-referenced notes). No map change — Jordan was never given the flag in the first place, so
  nothing to undo visually; this only closes the open question. No re-render needed.
- **⚠️ The surviving Israeli population's fate AND the West Bank settlers' status — both explicitly parked,
  not defaulted into an answer.** Asked directly about the surviving Israeli population, author's own words:
  "I honestly have no idea... There are so many variables involved that are all stacked onto each other, I
  don't have the brain power to imagine what that would be like." Asked separately about the West Bank
  settlers specifically, same answer: "I really don't think I'm capable of figuring out the West Bank
  settlers' status." Both treated the same as this project's other genuinely hard, deliberately parked
  questions (Osh, Uzbekistan's Samarkand/Bukhara, Tekirdağ/Istanbul) — real open premises for a later session,
  not quietly resolved in the meantime. Neither borrows from or is implied by Jordan's own settled return-
  migration answer above, which is a separate question. Applied to frameworks survey §2.7 as parked items.
- **✅ Afghanistan's "stays whole" call re-confirmed via real economic/geographic viability research, not
  reversed.** Author's hypothesis: if the ethnic Tier-2 zones actually separated (not merely contested control
  of the whole country, the existing Northern Alliance premise), none could survive independently, so the land
  stays whole either way. Tested rather than assumed — evidence is real but mixed: **Hazara (Bamyan/Daykundi)
  confirms it strongly** (entirely landlocked within Afghanistan's own other provinces, no international border
  at all, no significant documented resources); but **Tajik north (Badakhshan touches three international
  borders — Tajikistan, China via the Wakhan Corridor, Pakistan) and Uzbek/Turkmen north (real natural gas/oil
  fields, direct Uzbekistan/Turkmenistan borders) are stronger independent-viability cases than the hypothesis
  assumed.** What holds regardless: every piece shares Afghanistan's own acute two-neighbor trade dependency
  (Pakistan 42%, India 40% of exports). Author's own call: keep the stays-whole conclusion, now grounded in
  this research alongside the existing outside-conquest-immunity reasoning. Applied to frameworks survey's new
  §7.5 and `regions.csv`'s `afghanistan`/pashtun row. No map change — Afghanistan's territory was already
  correct; this only strengthens the documentation behind it. No re-render needed.
- **✅ Ilam — the longest-open item of this whole session, finally settled: moved from Kurdistan's domain to
  Persia's core.** Author asked for a refresher on what/where Ilam is, then a deeper look at its geological
  composition; research confirmed the province genuinely straddles both sides of its own internal divide — the
  Kabir Kouh range (up to 2,775m at Kan Seifi peak) with real intermontane valley-plains in the north/east, a
  real Mesopotamian-lowland-extension desert plain (Dehloran/Musian/Dasht Abbas, 50-300m) in the southwest, and
  a real river system (the Seymareh feeding the Karkheh, Iran's third-longest river) draining the whole
  province toward Iraq. Author's own call: "I would say tie it in with Persia." Disclosed tradeoff, not a clean
  parallel to Tunceli/Bingöl/Muş: this is not a whole-province-on-one-side-of-the-divide case the way that
  precedent was, and Ilam's Kurdish/Lak population is less identity-ambiguous than Tunceli's — both facts made
  this a weaker case for the move than it first appeared, but the author settled it anyway, grounded in the
  province's own hydrology tying it to Persia rather than Kurdistan.
  - Applied: `IRAN_KURDISH` in `middle_east_classify.py` no longer includes Ilam (now `{"Kurdistan",
    "Kermanshah", "West Azerbaijan"}`); `regions.csv`'s `kurdistan`/domain row lost Ilam, `persia`/core row
    gained it, both with full reasoning notes; `subdivisions.csv`'s Ilam row updated to match.
  - **Re-rendered both maps and rigorously verified**: matched-subdivision count unchanged (329/332, a pure
    reclassification); a debug-marker pass confirmed Ilam now classifies `persia`/core while Kermanshah and
    Iran's own Kurdistan province stay correctly `kurdistan`/domain; a zoomed crop of the actual output
    confirmed Ilam renders as solid magenta Persia territory, cleanly separated from the pale dotted-mint
    Kurdistan domain to its north. Both CSVs confirmed untouched by MD5 before/after both render runs.
- **✅ Socotra researched properly for the first time, confirmed staying part of South Yemen.** Author asked
  what/where it was, then its size, then who it has closest ties to. Research found: genuinely small (main
  island ~3,665 km², ~60,000 people — about Long Island-sized); two real ties pointing different directions —
  ethnically/linguistically Mahra people speaking Soqotri, closely related to Mehri (spoken in Al Mahrah, an
  actual mainland South Yemen governorate), but politically currently controlled by the UAE (troops seized the
  airport/seaport in 2018; the UAE-backed STC staged an actual coup in June 2020, with documented repression
  since). Author's own resolving principle, matching this map's own culture-over-control method (the same
  logic that already corrected Raqqa's placement, §3.10): "if the people consider themselves Yemenis, then it
  makes sense that it would be part of Yemen" — supported by the population's own documented resistance to the
  UAE-backed coup, not welcoming it. Applied to frameworks survey's new §5.6 and `regions.csv`'s
  `south_yemen`/socotra row (confidence upgraded medium→high). No map change — Socotra was already correctly
  placed; this only closes out under-researched documentation. No re-render needed.
- **✅ Georgia's Adjara researched further and confirmed as its long-term Autonomous Zone, current treatment
  kept as-is.** Research found: capital Batumi (Georgia's 2nd-largest city); religious distinctness traces to
  the 1614 Ottoman conquest and ~200 years of Islamization, but the current 2024 census shows Adjara Orthodox-
  majority again (59.5% Orthodox, 33.9% Muslim), with real internal variation (mountainous Khulo ~95.3% Muslim
  vs. coastal Kobuleti ~71% Orthodox) this map's whole-governorate resolution can't further resolve. Most
  load-bearing fact: Adjara is the ONLY autonomous region in the whole South Caucasus with no secessionist
  conflict since Soviet dissolution, maintaining strong Georgian national identity even under a genuinely
  authoritarian local strongman (Abashidze, 1991-2004) despite real Turkish/Russian geopolitical interest.
  Author's own call: "if its long-term status is as an Autonomous Zone, then let's just go ahead and keep it
  that way." Applied to the South Caucasus survey's own §2.3 and `regions.csv`'s `georgia`/adjara_muslim row.
  No map change — already correctly a flagged religious minority within Georgia's core. No re-render needed.
- **✅ Nakhchivan's own independence question researched and closed — stays Azerbaijan's Autonomous Republic.**
  Author asked how it would fare as a fully independent country, separate from both Armenia and Azerbaijan.
  Research found no plausible basis for it: formally the Nakhchivan Autonomous Republic (same formal category
  as Adjara, settled the same session); population ~459,600, 99.7% Azerbaijani, with no separatist identity
  basis (its one "independence" declaration, Jan. 1990, was solidarity with Azerbaijan's own anti-Soviet
  movement, not separatism from it); economically fragile (real unemployment, mass emigration to Turkey — an
  entire Istanbul district, Besler, is now mostly Nakhchivanis) and totally geography-dependent (landlocked,
  decades of Armenian/Turkish blockade). Author's own call: "keep it as an Azerbaijani Autonomous Republic."
  Applied to the South Caucasus survey's §3.1 and `regions.csv`'s `azerbaijan`/core row. Explicitly resolves
  only Nakhchivan's own status — Syunik's status, the Zangezur Corridor/TRIPP question, and the deeper
  population-history "uncertain territory" flag all remain parked as before. No map change, no re-render.
- **✅ "Arabia" split into named countries — the last generic multi-country bloc label on the map, closed out
  the same way Levant→Syria/Jordan and Anatolia/Mesopotamia/Persia→Turkey/Iraq/Iran were.** Author weighed each
  of the six GCC monarchies' real independence case directly (population/citizenship base, economic
  diversification, security guarantees, historical precedent) rather than splitting by default:
  - **Qatar and Oman settled staying independent** — Qatar on its world-highest GDP per capita and demonstrated
    resistance to the 2017-2021 Saudi-led blockade; Oman on its genuinely distinct Ibadi-Muslim identity (~45%
    of its Muslim population, a real third branch of Islam), former-maritime-empire history, and control of
    the Musandam Peninsula overlooking the Strait of Hormuz.
  - **Kuwait and Bahrain settled absorbed into a Saudi successor state** — Kuwait's case is built on negative
    evidence (Iraq's 1990 invasion fully occupied it, restored only by international coalition); Bahrain is
    close to a de facto Saudi dependency already (the King Fahd Causeway, and the 2011 Saudi/UAE Peninsula
    Shield Force intervention that helped suppress its own Shia-majority uprising).
  - **The successor state's name is settled: the Kingdom of Nejd and Hejaz.** Real precedent found for
    renaming at all: the current kingdom is the *Third* Saudi State (the First, the Emirate of Diriyah, was
    destroyed by Ottoman-Egyptian forces in 1818; the Second, the Emirate of Nejd, was defeated by the rival
    Rashidi dynasty in 1891). Rather than picking just **Nejd** (the historical core region across all three
    Saudi states) or just **Hejaz** (the separate Hashemite-ruled western region with Mecca/Medina until
    1925/26), the author settled on the combined form — not invented, but the dynasty's own real 1926-1932
    historical name for the state it ruled between uniting the two regions and rebranding as "Saudi Arabia" in
    1932. Two follow-up questions settled directly: (1) the name doesn't need to cover 100% of the successor
    state's actual territory (Kuwait/Bahrain/Eastern Province included) any more than the real 1926-1932
    kingdom, "Persia," or the real "Saudi Arabia" do; (2) "Kingdom" as a governmental *form* is characteristically
    consistent for this region regardless of which bloodline ends up ruling — every real Gulf state today is a
    monarchy, and both prior Saudi-state collapses were followed by continued dynastic/tribal rule (once under a
    *different* house, the Rashidis) rather than any republican turn, so the specific ruling family is
    deliberately left open, not assumed to be the same Al Saud line as the real world's Saudi Arabia.
  - **UAE settled staying fully independent, 2026-09-29 — the strongest independence case of the whole former
    bloc, stronger even than Qatar's.** A real, current (2025-2026) rupture with the Nejd/Hejaz successor state
    specifically: the Yemen war split them once already (UAE forces withdrew 2019 over strategy; by December
    2025 UAE-backed southern separatists seized territory in southern Yemen outright, prompting a Saudi demand
    for full Emirati withdrawal), real 2021/2023 OPEC+ quota disputes bitter enough the Saudi crown prince
    reportedly accused the UAE of "stabbing us in the back," a planned 2026 UAE departure from OPEC, and the two
    backing opposite sides of Sudan's civil war (Saudi backs the SAF, UAE backs the rival RSF) — observers call
    it a "rupture." Also weighed: independent military/foreign policy already exercised (own bases in Libya and
    Eritrea, a 1994 US Defense Cooperation Agreement, its own unilateral 2020 Abraham Accords normalization with
    Israel ahead of Saudi Arabia), and 50+ years as its own successful federation (formed 1971 after Bahrain and
    Qatar each walked away from the same union talks). Real vulnerabilities disclosed: only ~12% native Emirati
    citizens (same issue already disclosed for Qatar); Abu Dhabi dominates the internal federation (~95% of oil,
    ~92% of gas, ~2/3 of the economy, permanent federal presidency); Dubai's 2009 Dubai World debt crisis ($59B
    debt, $10B Abu Dhabi bailout kept explicitly "case-by-case"); and a real historical Saudi territorial claim
    on Abu Dhabi itself on the eve of 1971 independence, resolved by a 1974 agreement (left resolved, not
    reopened). **Author's own addition: Abu Dhabi's capital city hosts a small, fully neutral diplomatic
    district** — below this map's rendering resolution (sub-city, not a whole emirate), so documented as lore in
    `subdivisions.csv`'s own "Abu Dhabi" note rather than drawn as its own map region, paralleling Jerusalem's
    own neutral-city status at region scale.
  - **Applied**: `middle_east_classify.py`'s `REGIONS` dict and `classify()` (new `qatar` and `oman` regions;
    Kuwait/Saudi Arabia/Bahrain all now route to `nejd_hejaz` — renamed from the working placeholder
    `saudi_arabia` — carrying Bahrain's real shia_majority flag and Saudi's own Eastern Province shia_flag
    forward intact); `regions.csv`'s old 3-row `arabia` block renamed/reduced to a single `uae` core row (the
    UAE's own settled independence case), plus the renamed 3-row `nejd_hejaz` block (core/shia_flag/shia_majority)
    with updated notes; `subdivisions.csv`'s "Abu Dhabi" row carries the new neutral-district note. Both
    `middle-east-render.py` and `west-asia-composite-render.py` updated (legend confidence dicts, label
    positions, legend-order lists) for both the `saudi_arabia` → `nejd_hejaz` and `arabia` → `uae` region_id
    renames.
  - **Re-rendered both maps and rigorously verified**: matched-subdivision count unchanged (329/332, a pure
    reclassification); a six-way debug-marker pass (Riyadh, Kuwait City, Manama, Doha, Abu Dhabi, Muscat) confirmed
    every country classifies correctly; a zoomed crop of the actual output confirmed Qatar renders as its own
    distinct maroon peninsula, Bahrain's diagonal shia_majority hatch carried over correctly into the Saudi
    successor region, and UAE/Oman both render as their own distinct colors. `regions.csv` confirmed untouched
    by MD5 before/after both render runs. New frameworks survey §5.2.1/§5.2.2 documents the full reasoning.

**Finalized maps, 2026-09-29** — `02 reorganization/05 follow-up - finalized maps/`. The author moved active
work into this new folder (a full mirror of `04 follow-up - further borders/`, carrying that folder's latest
UAE-decision renders forward). All three render scripts (`middle-east-render.py`, `west-asia-composite-render.py`,
`central-asia-render.py`) live here now; this is the current working folder going forward, not `04`.

- **✅ Solid-color cleanup, 2026-09-29 — every region on all three maps now renders as one flat solid color,
  no exceptions.** Author's instruction: "clean up the maps so that the countries are all solid colors,"
  clarified on request to mean removing BOTH hatching AND tier-based shade variation (not just hatching alone),
  across all three maps (Middle East standalone, West Asia composite, and Central Asia standalone — not just
  the two West Asia maps this session had been focused on).
  - **Removed from `middle-east-render.py`**: `TIER_HATCH` and `CONTESTED_REGION_HATCH` dicts, the `lighten()`
    tint helper, the per-tier fill/hatch branching in the main region-fill loop (now one `facecolor=base` pass
    per region_id), and the Abkhazia/South Ossetia contested-hatch overlay pass. Legend's "How to read it"
    block simplified to drop the now-false core/domain/hatch/contested-hatch/circle-hatch explanation lines.
  - **Removed from `west-asia-composite-render.py`**: `ME_TIER_HATCH`, `CONTESTED_REGION_HATCH`, `CA_SPECIAL_HATCH`
    dicts, `lighten()`, `HATCH_GRAY` (dead), the Fergana Tangle/GBAO/Samarkand-Bukhara/Abkhazia/South-Ossetia
    special-case overlay passes, and every corresponding `hatch=` legend-patch argument.
  - **Removed from `central-asia-render.py`**: `SPECIAL_HATCH_UNITS` and `DOMAIN_UNITS` dicts, `lighten()`,
    `HATCH_GRAY` (dead), the GBAO lighter-shade overlay and Samarkand/Bukhara dot-hatch overlay passes, and
    their legend-patch entries.
  - **Kept, deliberately**: the gray cross-hatch treatment for out-of-scope real-world neighboring countries
    (Russia, China, Egypt, Pakistan, etc.) on all three maps — that hatch marks "not part of this project's
    classification," not a country's own color, so it's a different visual language from the tier hatching
    that was removed. Confirmed with the author as in-scope for a *future* ask, not assumed silently.
  - **Underlying data preserved, not deleted**: `tier` values still get computed and stored in each script's
    working dataframe (harmless, unused by rendering); `regions.csv`/`subdivisions.csv`'s own tier rows and
    prose notes (Iraq's Shia/Sunni/contested split, Lebanon's confessional zones, Khuzestan's unstable-territory
    status, Abkhazia/South Ossetia's disputed marks, Samarkand/Bukhara's Tajik-minority flag, GBAO's Pamiri
    distinctness, etc.) are all untouched — this was a rendering-only cleanup for the eventual wiki's sake, not
    a reversal of any prior research or classification decision. Two regions.csv notes that specifically
    claimed a still-existing map hatch (Uzbek Oasis's Samarkand/Bukhara note, Persianate Tajik's GBAO note) were
    reworded to say the distinction is documented but no longer drawn, not deleted. Matching addenda added to
    all three README.md files (middle-east-map-data, south-caucasus-map-data, central-asia-map-data).
  - **Re-rendered all three maps and verified**: identical match/unmatched counts on every map, confirming this
    was a pure visual cleanup with no geometry or classification regression (Middle East 329/332 — same 3
    unmatched; composite 329/332 Middle East + 48/48 Central Asia; Central Asia standalone 48 polygons/5
    countries, same 7 folded-in subdivisions).

- **✅ Extra annotation-line cleanup, 2026-09-29 — removed the Taurus-Zagros tectonic overlay and every
  cross-region tie/sphere connector line, keeping present-day national border reference lines.** Author's
  instruction: "remove the 'hashed' tectonic faultline... Same with the other dotted lines," clarified on
  request to mean the sphere/tie connectors specifically (Pan-Turkic tie, Yazidi tie, S3/S4 composite
  connectors, Central Asia's S1/S2 markers) — NOT the dashed-gray present-day-border reference lines, which
  stay on all three maps.
  - **Removed from `middle-east-render.py`**: the Pan-Turkic tie arc (Turkey↔Azerbaijan), the Yazidi-tie
    circle (Armenia↔Kurdistan), and the Taurus-Zagros Catmull-Rom curve overlay, plus their "How to read it"
    legend lines. Dead imports cleaned up (`matplotlib.patheffects`, `numpy`, `shapely.geometry.LineString`).
  - **Removed from `west-asia-composite-render.py`**: the `draw_connector()`/`region_centroid()` helpers and
    the S3 Pan-Turkic fan, S4 Persianate/Central Asian Bridge connectors, Yazidi-tie circle, and Taurus-Zagros
    overlay they supported, plus their legend lines and stale header/footer text. Dead imports cleaned up
    (`FancyArrowPatch`, `numpy`).
  - **Removed from `central-asia-render.py`**: the S1 Isfara/Konibodom sub-marker and S2 Uyghur-diaspora
    circle, plus their legend lines. Dead `numpy` import cleaned up. The separate Fergana Valley enclave
    point-markers (diamonds with leader lines) were NOT touched — a different feature, not a tie/sphere line.
  - **Kept, deliberately**: present-day national border dashed-gray reference lines on all three maps (a
    different visual language — "here's today's real border" — not a sphere/tie annotation); the gray
    cross-hatch for out-of-scope neighboring countries (already confirmed in-scope for the earlier solid-color
    cleanup, unrelated to this ask).
  - **Underlying research untouched**: the Pan-Turkic sphere, the Persianate/Central Asian Bridge, Armenia's
    Yazidi population, and the Taurus-Zagros geological rationale for Kurdistan's cross-border shape all stay
    fully documented in `spheres.csv` and the frameworks surveys — only the drawn map annotation was removed.
  - **Re-rendered all three maps and verified**: identical match/unmatched counts on every map (same as the
    prior solid-color cleanup pass), confirming this was a pure visual cleanup with no regression.

- **✅ Central Asia region renaming, 2026-09-29 — five of the package's seven regions renamed to their real,
  current country names.** Author asked whether Turkmenistan/Uzbekistan/Kyrgyzstan/Tajikistan (and, by the same
  logic, Kazakhstan) had been addressed yet, then asked to "name all those countries to their current names" —
  the same generic-cultural-label-vs-real-name fix already applied to the Middle East map (Levant→Syria/Jordan,
  Kurdish Nation→Kurdistan, "Arabia"→United Arab Emirates, "Saudi Arabia"→Kingdom of Nejd and Hejaz).
  - **Renamed**: `kazakh_steppe`/"The Kazakh Steppe" → `kazakhstan`/"Kazakhstan"; `kyrgyz_highlands`/"The
    Kyrgyz Highlands" → `kyrgyzstan`/"Kyrgyzstan"; `turkmen_desert_oasis`/"The Turkmen Desert-Oasis" →
    `turkmenistan`/"Turkmenistan"; `uzbek_oasis`/"The Uzbek Oasis Civilization" → `uzbekistan`/"Uzbekistan";
    `persianate_tajik`/"The Persianate Tajik Highlands" → `tajikistan`/"Tajikistan." Colors and member
    subdivisions unchanged for all five — this was a pure naming change.
  - **NOT renamed, deliberately**: `karakalpakstan` (already carries its own real, current name — an
    autonomous republic, not a sovereign country needing this fix) and `fergana_tangle` (a genuinely
    cross-border mosaic spanning Uzbekistan and Kyrgyzstan that doesn't correspond to any single country, the
    same reason "Kurdistan" and "Balochistan" keep their own descriptive names on the Middle East map rather
    than being forced into one nation's name).
  - **Applied**: `central-asia-render.py`'s `REGIONS`/`ASSIGN`/`REGION_LABEL_POS`/`ORDER` and
    `west-asia-composite-render.py`'s `CA_REGIONS`/`CA_ASSIGN`/`REGION_LABEL_POS`/legend-order list all updated
    (mechanical identifier rename plus the five display-name changes); stale footer-text mentions of the old
    display names fixed in both scripts. `central-asia-map-data/regions.csv` fully rewritten with the new
    region_ids/names and a rename note on each changed row; matching addendum added to
    `central-asia-map-data/README.md`. `subdivisions.csv` and `spheres.csv` needed no changes — both already
    key by real nation name, not region_id, same pattern as the Middle East package.
  - **Re-rendered both the Central Asia standalone and composite maps and verified**: identical match counts
    (48 polygons/5 countries standalone; 48/48 Central Asia + 329/332 Middle East on the composite) and a
    visual check confirming the map now labels "KAZAKHSTAN," "KYRGYZSTAN," "TURKMENISTAN," "UZBEKISTAN," and
    "TAJIKISTAN" directly, with "Karakalpakstan" unchanged (see below for the Fergana Valley Tangle's own,
    separate rename the same day).

- **✅ Three more naming/visual decisions, 2026-09-29, same session as the Central Asia country renames above.**
  - **Fergana Valley Tangle marked "Uncertain Territory."** Author: "mark that as 'uncertain territory'."
    `fergana_tangle`/"The Fergana Valley Tangle" renamed to `fergana_uncertain`/"Fergana Valley (Uncertain
    Territory)" — matching the exact naming convention already used for Khuzestan ("Khuzestan (Unstable
    Territory)") and Dhale ("Dhale (Disputed Territory)"). Not renamed to a country name like its five
    neighbors, since it's deliberately cross-border and doesn't correspond to any single country. Color and
    member subdivisions unchanged. Applied to both `central-asia-render.py` and `west-asia-composite-render.py`
    (identifier + display name + footer text) and `central-asia-map-data/regions.csv`/README.md.
  - **Georgia, Armenia, and Azerbaijan's parenthetical descriptors dropped.** Author: "just call them 'Georgia',
    'Armenia', and 'Azerbaijan'." "Georgia (Kartvelian/Orthodox)," "Armenia (Apostolic)," and "Azerbaijan
    (Turkic/Shia)" simplified to plain "Georgia," "Armenia," "Azerbaijan" in `middle_east_classify.py`'s
    `REGIONS` dict (the composite map imports this directly, so no separate edit needed there) and
    `middle-east-map-data/regions.csv`. The dropped parentheticals stay fully documented in each row's own
    notes and the South Caucasus frameworks survey — only the display label changed.
  - **Khuzestan recolored to Persia's color, with a hatch overlay — the one deliberate exception to the
    solid-color cleanup.** Author: "make Khuzestan the same color as Persia, but with hatch marks to illustrate
    the fact that it's not cleanly-settled (i.e., 'unstable territory')." `khuzestan_unstable`'s color changed
    from a distinct gray-brown (`#8F8570`) to Persia's own `#A8456B` in `middle_east_classify.py`; a narrow,
    single-purpose hatch-overlay pass (diagonal `///`, no fill, drawn on top of the flat color fill) added back
    to both `middle-east-render.py` and `west-asia-composite-render.py` — scoped to this one region only, not a
    reversal of the general solid-color cleanup. Legend swatches for Khuzestan updated to show the same hatch
    on both maps, and both "How to read it" lists updated with a line explaining it. Applied to
    `middle-east-map-data/regions.csv` and the frameworks survey's own §10.
  - **Re-rendered all affected maps and verified**: identical match/unmatched counts on every map (no geometry
    or classification regression); visual checks confirmed Khuzestan's hatch renders correctly over Persia's
    color on both the standalone Middle East map and the composite, and Fergana Valley (Uncertain Territory)
    and the simplified Georgia/Armenia/Azerbaijan labels render correctly on the Central Asia and composite maps.

**Label fixes, 2026-09-29** — `02 reorganization/06 follow-up - label fixes/`. Author moved work into this new
folder (mirrors `05`'s latest state). Pure rendering fixes this round, no research/classification changes.

- **✅ Fergana Valley (Uncertain Territory) and Palestine labels moved outside their own cramped shapes,** with
  a leader line pointing back to the actual land — both regions are too small for their name to fit inline at
  any readable size. Fergana's label is two lines ("FERGANA VALLEY" / "(UNCERTAIN TERRITORY)") per the author's
  own requested line break; Palestine stays one line, matching this map's existing all-caps label convention.
  Applied to `central-asia-render.py` (Fergana only — Palestine isn't on this map) and
  `west-asia-composite-render.py` (both). The standalone `middle-east-render.py` was untouched — it turns out
  that map never draws region names on the land at all, only in its side legend, so Palestine's own cramped
  label only existed on the composite map.
- **✅ Fixed a real rendering bug: an unexplained white/cream circle inside Kazakhstan, at Baikonur.** Root
  cause tracked down properly, not papered over: Natural Earth carries "Baykonur Cosmodrome" as its own
  separate admin-0 entity (SOVEREIGNT=Kazakhstan, TYPE=Lease) — a literal circular hole carved out of
  Kyzylorda's own admin-1 polygon. That hole was falling into the maps' generic "out-of-scope neighboring
  country" bucket (a plain cream fill, no hatch, since it isn't Russia/China), which is what rendered as an
  unexplained circle; the first fix attempt (excluding it from that bucket and painting a matching-color patch
  on top) still left a visible ring, because the underlying province-border layer was separately tracing the
  real interior-ring hole in Kyzylorda's own polygon regardless of what got drawn on top. Properly fixed by
  unioning the Baikonur polygon directly into Kyzylorda's geometry before any dissolve or boundary-tracing
  happens, in both `central-asia-render.py` and `west-asia-composite-render.py` — Baikonur is real Kazakh
  territory (just operationally leased to Russia), so this is the geographically correct fix, not a workaround.
  Re-rendered and verified: identical match counts on both maps, hole/ring fully gone on close inspection.

- **✅ Large-scale label repositioning pass, 2026-09-29, from author-supplied hand-annotated reference images**
  (`06 follow-up - label fixes/reference/`). Author drew ovals/arrows directly on copies of both rendered maps
  to show exactly where each on-map region label should move. Interpretation rule, confirmed by the author's
  own framing: a plain oval = relocate the label there; an arrow with no separate destination oval = a small,
  delicate nudge in that direction only; a dashed circle + arrow + solid destination oval, or a curved arrow
  into a solid oval = full relocation with a leader line back to the actual land (this map's existing pattern
  for cramped small regions). Reference-image pixel positions were converted to precise lon/lat coordinates
  using the render scripts' own actual projection math (xlim/ylim/dpi/figure size extracted via a temporary
  debug print, removed after use) rather than eyeballed, then verified visually against the reference crops.
  - **Two-line label, Khuzestan**: "Khuzestan (Unstable Territory)" split into "KHUZESTAN" / "(UNSTABLE
    TERRITORY)" on two lines, matching the same wording/break the author requested for Fergana Valley earlier
    the same day. Only the on-map composite label changed — the side-legend entries (both maps) stay one line,
    since a compact legend row was never the "ultra-cramped" problem being solved.
  - **Relocated within their own territory, no leader line needed** (Central Asia map): Kazakhstan, Turkmenistan,
    Uzbekistan, Tajikistan. (Composite map): the same four, plus Kurdistan, Afghanistan, Persia, Kingdom of Nejd
    and Hejaz, North Yemen, South Yemen.
  - **Delicate nudge only** (composite map): Turkey (nudged right/east), Karakalpakstan (nudged left/west), UAE
    (nudged down/southwest) — each just a few tenths of a degree, per the author's explicit "very very
    delicately, very slightly" instruction.
  - **Moved to a new callout position with a leader line** (composite map): Fergana Valley (Uncertain Territory)
    and Palestine had their existing leader-line destinations updated to the author's newly-specified spots;
    Khuzestan (Unstable Territory), Armenia, Lebanon, Dhale (Disputed Territory), and Qatar all gained a brand
    new leader-line callout for the first time (previously drawn inline on their own territory, which the
    author's reference showed as too cramped/cluttered by nearby city labels).
  - **Applied to `central-asia-render.py` and `west-asia-composite-render.py`** — `REGION_LABEL_POS` dict entries
    updated/removed as appropriate, nudge deltas applied inline with a comment, and the callout-label block
    (already established for Fergana/Palestine) extended with the five new entries plus Khuzestan and Fergana's
    updated destinations.
  - **Re-rendered both maps and verified visually against every one of the author's own reference-image
    annotations** (side-by-side crops of each repositioned label) — all matched cleanly, no new overlaps
    introduced, identical subdivision match counts on both maps (no geometry regression).

- **✅ Follow-up label tweaks, same day.** Four more small fixes, all in `06 follow-up - label fixes/`:
  - **Kyrgyzstan nudged again, opposite directions per map**: up-and-right (delicately) on the Central Asia
    standalone map; down-and-right (delicately) on the composite map — the author gave each map its own
    separate, opposite-vertical-direction instruction.
  - **All country and city name labels on the composite map enlarged 30%** — the dynamic region-label font-size
    formula, the seven callout-label font sizes (Fergana/Palestine/Khuzestan/Armenia/Lebanon/Dhale/Qatar), and
    the capital/city marker labels all multiplied by 1.3. Sea labels (Caspian Sea, Persian Gulf, etc.) and the
    small sub-region flags (Gorno-Badakhshan, out-of-scope Russia/China annotations) were deliberately left
    alone — the author's own wording was "countries and cities" specifically. Scoped to the composite map only,
    matching how the message was structured (Central Asia map's own text sizes are unchanged).
  - **Fixed a real bug: Dhale's leader line was landing on the coast near Aden, not on the actual Dhale
    (Disputed Territory) patch.** The gray patch itself sits a bit north/inland of where the old xy coordinate
    (44.7, 13.5) pointed. Found the patch's real rendered centroid by color-matching its exact fill color
    (`#8A8070`) in the output PNG and measuring its pixel centroid directly, then converted that pixel position
    to the correct lon/lat (44.79, 13.891) using the render script's own actual projection math — the same
    verification-over-guessing approach used throughout this map project.
  - **Re-rendered both maps and verified visually**: Kyrgyzstan's new position confirmed on each map, the
    30% size increase confirmed across region and city labels on the composite map, and Dhale's leader line
    confirmed landing squarely on the real gray patch. Identical subdivision match counts, no regression.

- **✅ Second follow-up pass, same day.** Kyrgyzstan nudged again on both maps — further right only this time
  (same delicate touch) — and the composite map's country/city label text enlarged a further 70% on top of the
  prior 30% (stacked multiplicatively, ×1.3×1.7 ≈ ×2.21 of the original size), per the author's own "still hard
  to read" follow-up. Same three spots updated as before (region-label font formula, the seven callout labels,
  capital/city markers) — sea labels and small sub-region flags still deliberately excluded. Re-rendered and
  confirmed: text is now much more legible, though the already-dense Levant cluster (Palestine/Lebanon/Syria/
  Jordan/Jerusalem) and the Yemen cluster now show more visible label overlap as a direct consequence of the
  larger text in already-tight space — flagged here, not silently fixed, since resolving it would mean
  repositioning several more labels beyond what was asked this round.

- **✅ Third follow-up pass, same day.** Two changes: Kyrgyzstan's own label position confirmed final by the
  author ("ideally repositioned... can be left alone") — no further change on either map. And the composite
  map's +70% country-label size increase was judged too large ("I misjudged, and +70% was too huge") — dialed
  back 30% from where it stood, explicitly for country-level labels only, with city/capital labels left exactly
  as they were. Net effect on country labels: ×1.3 × ×1.7 × ×0.7 ≈ ×1.55 of the original pre-2026-09-29 size
  (cities remain at ×1.3 × ×1.7 ≈ ×2.21). Applied to the same two country-label spots (region-label font
  formula, the seven callout labels) — the city/capital marker fontsize line was left untouched. Re-rendered
  and confirmed: country labels visibly smaller than the prior pass, the Levant/Yemen overlap from the +70%
  pass eased somewhat, city labels unchanged.

- **✅ Fourth follow-up pass, same day.** With country labels dialed back, the author noted city and country
  labels had ended up "about comparably sized, which is unfortunate," and asked for city labels specifically
  reduced 20% from where they stood. Applied only to the city/capital marker fontsize line (the one spot left
  untouched in the prior pass) — net effect on cities: ×1.3 × ×1.7 × ×0.8 ≈ ×1.77 of the original pre-2026-09-29
  size (countries stay at ≈×1.55 from the pass above). Re-rendered and confirmed: cities now read clearly
  smaller than country names again, restoring a sensible label hierarchy, and the Levant cluster's crowding
  eased further as a side effect.

- **✅ Fifth follow-up pass, same day — the Palestine/Jordan cluster's real crowding problem, fixed properly.**
  Author: "in the region of Palestine and Jordan, the names of places are squished together... find a way to
  distribute them comfortably." This was the composite map's worst remaining cluster: Ramallah, Amman, and
  Jerusalem (all real cities within ~70km of each other) were rendering as an unreadable jumble ("RamAllah" /
  "Amman" / "erusalem" running together), worsened by every font-size increase this session, and the
  "JERUSALEM (NEUTRAL CITY)" region label was sitting right on top of that same jumble.
  - **Jerusalem (Neutral City) given its own leader-line callout** — the last of this map's on-territory region
    labels still lacking one, moved into Jordan's own open desert interior (clear of Palestine's and Lebanon's
    own leader lines out over the sea).
  - **Ramallah, Amman, and Jerusalem's city-marker labels given individual offset overrides** — a new
    `CITY_LABEL_OVERRIDE` dict (checked per-city, falling back to the existing default 18km/2.2pt offset for
    every other city on the map) with custom horizontal distance and vertical placement for just these three:
    Ramallah flipped to extend its text left (toward open Palestine/sea space, away from Amman) instead of
    right; Jerusalem pushed further left and placed below its marker instead of above; Amman pushed further
    right into Jordan's own clear territory.
  - **Jordan's own country label nudged into its own open desert interior**, since its old position (still
    inside the same crowded cluster) needed to get out of the way for the new Jerusalem callout and the
    now-more-spread-out city labels.
  - **Re-rendered and verified visually**: every one of Ramallah/Amman/Jerusalem/Jordan/Jerusalem (Neutral City)
    now reads cleanly with no overlap, the new leader line lands correctly on Jerusalem's real location, and
    nothing else on the map was disturbed (identical subdivision match count).

- **✅ Sixth follow-up pass, same day.** Georgia nudged up, Azerbaijan nudged down (both delicately). Jerusalem
  (Neutral City)'s brand-new leader line from the pass above turned out to cut straight through Jordan's own
  country label — moved further left/south (destination changed from (38.8, 29.4) to (36.5, 28.8)) so the line
  path never crosses Jordan's label position at all, verified by checking the line's own parametrization doesn't
  pass near (37.4, 30.6). Also split into two lines per the author's own requested wording/break: "JERUSALEM" /
  "(NEUTRAL CITY)", matching the same all-caps two-line convention as Fergana and Khuzestan. Re-rendered and
  confirmed: the leader line now clears "JORDAN" with visible room to spare, Georgia/Azerbaijan both read
  cleanly against their neighboring city labels (Tbilisi/Baku), no regressions.

- **✅ Seventh follow-up pass, same day.** Georgia nudged further up, Azerbaijan further down again (both still
  delicate). Also: Georgia and Azerbaijan's country-label font sizes were still visibly smaller than Turkey,
  Kurdistan, and the other larger countries — root cause found, not just patched: this map's country-label
  formula scales font size by each region's own real land *area* (`9 + area_frac * 340`, clamped to 19 before
  the session's stacked size multipliers), and every one of the map's bigger countries (Turkey, Kurdistan,
  Kazakhstan, Persia, Afghanistan, Balochistan, Nejd/Hejaz, Iraq, Turkmenistan — confirmed via a temporary debug
  print of each region's actual computed size, removed after use) already sits at that same 19-point clamp
  ceiling, while Georgia (16.8) and Azerbaijan (18.0) fell just under it purely because they're smaller
  countries by area. Added an explicit override for these two region_ids to use the same clamp-ceiling value
  as every large country, rather than their own area-scaled size — author's own framing: match the size other
  countries already use, not just "make it bigger" by an arbitrary amount. Re-rendered and confirmed: Georgia
  and Azerbaijan now read at the same size as Kurdistan/Turkey, with the two labels also spread further apart
  and no new overlaps.

- **✅ Eighth follow-up pass, same day.** Author extended the same "match the other countries' size" treatment
  to seven more: Kyrgyzstan, Tajikistan, North Yemen, Jordan, and Syria (added to the same override list as
  Georgia/Azerbaijan, since they render through the same area-scaled on-territory label loop) plus Armenia,
  Palestine, and Lebanon (which don't go through that loop at all — they're in the separate leader-line callout
  block, and had each been given their own smaller, arbitrarily-chosen base size, 11-13, when they were first
  added; changed all three to the same 19-point base the on-territory labels clamp to).
  - **Fallout caught and fixed**: enlarging Lebanon's callout to match immediately collided it with Syria's own
    label (they sit close enough that both being large text ran them together into "LEBANON SYRIA"). Moved
    Lebanon's leader-line destination further out over the Mediterranean (from (34.548, 34.607) to
    (32.4, 35.9)) to clear it — this is the same "check the actual render, don't just trust the formula"
    discipline this project uses throughout; the fix was caught by looking at the output, not assumed safe.
  - **Re-rendered and verified visually across the whole map**, not just the changed labels — confirmed Lebanon/
    Syria/Palestine all read cleanly with clear separation, the other six enlarged labels (Kyrgyzstan, Tajikistan,
    North Yemen, Jordan, Armenia) show no new collisions anywhere else on the map, and the subdivision match
    count is unchanged.

- **✅ Ninth follow-up pass, same day.** UAE's own label was colliding with Muscat's city label (Oman's
  capital) — nudged further down into UAE's own territory (lat 23.7 → 22.9) to clear it, and given a UAE-only
  +10% size bump (its own small real land area otherwise clamps it well under the size the bigger-country
  override list uses, and the author asked for a specific +10% here rather than the full match-the-others
  treatment). Re-rendered and confirmed: UAE's label no longer touches Muscat's, reads visibly larger, and nothing
  else nearby (Qatar, Abu Dhabi, Doha) was disturbed.

- **✅ Tenth follow-up pass, same day.** Qatar's callout-label size increased +20% (its own base multiplier went
  from 11 to 11×1.2). UAE nudged a tiny bit back up (lat 22.9 → 23.05) — still clear of Muscat, just less far
  down than the prior pass. Re-rendered and confirmed: Qatar reads visibly larger, UAE still doesn't touch
  Muscat's label, no other labels in the Gulf cluster (Abu Dhabi, Doha, Manama) disturbed.

**Sidebar adjustments, 2026-09-29** — `02 reorganization/07 follow-up - sidebar adjustments/`. Author moved work
into this new folder (mirrors `06`'s latest state; new `reference/` subfolder present but its two images turned
out to be stale copies from the prior label-fix round with no new annotations on them, so this round worked
from the author's own written instruction instead).

- **✅ Sidebar legend text and swatches enlarged on both maps — was "close-to-impossible to read."** The legend
  (built via `fig.legend()`) was still sized for this map's original, much-smaller overall text scale from
  before this session's several rounds of label/font-size increases, so it had fallen far behind everything
  else on the page. Central Asia standalone: `fontsize`/`prop size` 7.5→13, `handlelength` 2.0→3.2,
  `handleheight` 1.05→1.7, `labelspacing` 0.5→0.7. Composite (much denser — ~30 region rows plus headers and
  a ~9-item "how to read it" key, so grown more conservatively to avoid overflowing into the footer):
  `fontsize`/`prop size` 6.9→10, `handlelength` 1.8→2.6, `handleheight` 1.0→1.35, `labelspacing` 0.42→0.5.
  Scope was exactly what the author named — legend text and color-swatch/line/marker indicators only; the
  title, subtitle, description paragraph, and footer text sizes were left untouched since they weren't part of
  the ask. Re-rendered both maps and confirmed visually: both legends are now clearly legible with plenty of
  blank space left below them before the footer begins — no overflow or collision on either map.

- **✅ Composite map legend enlarged a second time, same day — the first pass had been too conservative.**
  Author: still "close-to-impossible to read." The first pass (6.9→10) had been sized cautiously to guard
  against overflowing into the footer, but that render confirmed a large amount of blank space was left below
  the legend — room the first pass left unused. Pushed further this time: `fontsize`/`prop size` 10→14,
  `handlelength` 2.6→3.4, `handleheight` 1.35→1.8, `labelspacing` 0.5→0.65 (now matching, not just approaching,
  the standalone Central Asia map's own legend size).
  - **Caught and fixed a real overflow this increase caused**: the Khuzestan hatch explainer line ("Diagonal
    hatch over Persia's color — Khuzestan, not cleanly settled (Unstable Territory)") ran off the right edge of
    the sidebar at the new size — the longest line in the whole legend, and the one row that didn't survive the
    jump. Split it across two lines with an explicit `\n` and trimmed the redundant trailing "(Unstable
    Territory)" (Khuzestan's own line above already states this), rather than shrinking the font back down.
  - **Re-rendered and verified visually**: confirmed the whole legend, cross-referenced row by row, fits
    cleanly with clear margin before the footer, the fixed Khuzestan line now wraps correctly with no clipping,
    and no other row overflowed at the new size.

---

**✅ WEST ASIA OFFICIALLY DONE — author-confirmed 2026-09-29.** All five pipeline stages complete for all three
sub-packages (Central Asia, Middle East/Turkey/Afghanistan, South Caucasus), sharing one composite map plus a
standalone Central Asia map and a standalone Middle East map. Closing state:
- **Divisions review** (two rounds, `02 reorganization/02–04 follow-up` folders): dozens of real border,
  naming, and demographic decisions closed out one at a time, each backed by actual research (Kurdish Nation→
  Kurdistan, Levant→Syria/Jordan, Iran→Persia, the Israel/Palestine post-collapse scenario, the Arabia bloc
  split into Qatar/Oman/UAE/the Kingdom of Nejd and Hejaz, Balochistan, Khuzestan, Karakalpakstan, Adjara,
  Nakhchivan, and the Central Asia country renames, among many others) — see the section above in full for
  every individual call and its sourcing.
- **Rendering/polish rounds** (`05`–`07 follow-up` folders): a full solid-color cleanup, removal of every
  cross-region tie/sphere annotation line, a large-scale author-directed label repositioning pass (from
  hand-annotated reference images), several rounds of font-size tuning across region/city/legend text, and a
  real rendering bug fixed properly (the Baikonur "white circle," fixed by unioning geometry rather than
  papering over the symptom).
- **All three maps** (`central-asia-map.png`/`.svg`, `middle-east-map.png`/`.svg`, `west-asia-composite-map.png`/
  `.svg`) live in `y-files/Map Files/Asia (West)/02 reorganization/07 follow-up - sidebar adjustments/` as the
  current, final versions.
- **No open items remain** from this region's own divisions-review list. Long-parked cross-project-scope
  questions (Israel's surviving population status, West Bank settlers, Syunik/Zangezur Corridor, Osh's
  disputed-territory status, Uzbekistan's Samarkand/Bukhara scenario) stay explicitly parked, not resolved by
  default — see their own notes above if picked back up later.

### 4.9 South Asia — Stage 1 DONE 2026-09-29; author decisions open, read this before anything else

**⚠️ READ THE FULL SURVEY FILE FIRST**: `worldbuilding/extractions/South Asia - The Siliguri Line and the
Nagalim Question (survey).md`. This section is a summary; that file has the full sourcing and reasoning.
Working folder: `y-files/Map Files/Asia (South-Central)/01 initial generations/` (the region's folder
scaffold — `02 reorganization/`, `03 official timeline years/`, `04 timeline staging/` — already exists,
pre-created, entirely empty; treat it the same way West Asia's own numbered `follow-up` folders were used).

**Session ended abruptly**: the author reported the terminal display was becoming garbled, likely triggered by
Bengali-script glyphs (জিরো পয়েন্ট আমগাছ তলা) copy-pasted from Google Maps into a message, and asked to save
everything and start a fresh session rather than keep debugging display corruption mid-task. Nothing was lost —
this section and the survey file above are the complete, deliberate handoff, not a reconstruction from
fragments. A copy-paste-ready resume prompt for the author's own use also lives at
`y-files/Map Files/Asia (South-Central)/01 initial generations/post-garble_restart_instructions.md`.

**Exact scope, author-settled — do not infer a different boundary from convenience or symmetry with other
regions:**
- **Pakistan, Nepal, Bangladesh, Bhutan, Sri Lanka**: full deep-research treatment, same rigor as every other
  country this project has built out. **Stage 1 done 2026-09-29** (see the Stage 1 block below);
  Stage 2 onward still ahead.
- **India**: explicitly **zero research** on the country as a whole, per the author's own direct words
  ("I require you to do exactly zero `[0]` research on India. Totally unnecessary."). The *only* India-related
  work is figuring out where a specific "slicing disconnect" line runs and what becomes of the land on its far
  side.
- **The India slice**: a real, precisely-specified dividing line — starting at the Nepal–Bihar–West Bengal
  tripoint, following the real Bihar/West Bengal state border to the Mahananda River, then following that
  river to the India–Bangladesh border (exact crossing point between two named Google Maps landmarks, "East
  Bandarjhuli" and "জিরো পয়েন্ট আমগাছ তলা" / "Zero Point Amgachh Tola") — author-drawn from direct Google Maps
  inspection, not this project's own invention. Everything south/west of that line (the rest of West Bengal,
  all of Bihar, the rest of India) is permanently out of scope. Everything north/east of it — Darjeeling,
  Kalimpong, Jalpaiguri, Alipurduar, Cooch Behar, Sikkim, Assam,
  Meghalaya, Nagaland, Manipur, Tripura, Mizoram, and **all of Arunachal Pradesh** (author explicitly confirmed
  the whole state, not just a piece of it) — breaks away into one or more new countries.

**Research completed this pass, real and sourced (see the survey file for full citations)**:
- The real Siliguri Corridor's exact geography (20–22 km at its narrowest; the real 1962-war and 2017-Doklam
  strategic-vulnerability precedent) and the real, century-old Gorkhaland separatist movement (Darjeeling +
  Kalimpong's own distinct Nepali/Gorkha identity, independently corroborating the author's own drawn line).
- A two-tier answer to "one country or several" (the author's own question) — **real evidence points clearly
  to several, not one**:
  - **Tier 1 (strong, active, real fracture lines)**: Sikkim (a real 1642–1975 independent kingdom, a
    restoration case not a secession case); "Nagalim"/Greater Nagaland (Nagaland + Naga-inhabited Manipur hill
    districts + Naga-inhabited eastern Arunachal Pradesh districts — a real, current NSCN unification claim,
    not invented); Meitei Manipur (the valley core); the Kuki-Zo bloc (southern Manipur hills — sharpened by
    the real, ongoing 2023–24 Manipur ethnic war, 175+ dead, ~60,000 displaced); Mizoram (unified, a real
    resolved 1986 peace accord to build from); Meghalaya (three historically separate tribal kingdoms welded
    in 1972, but genuinely no active internal fracture movement today — stays whole).
  - **Tier 2 (real evidence, but how far the fracture goes is a genuinely open call)**: Assam's Barak Valley
    (constitutionally already Bengali-majority/distinct from the Assamese Brahmaputra Valley); Bodoland (a
    real, active Bodo tribal autonomy demand); Tripura (the real demographic mirror-image of Assam's
    problem — tribal-majority before 1947, flipped Bengali-majority by two refugee waves, with a real
    decades-long insurgency resolved only in 2024); the rest of Arunachal Pradesh (23 tribes, no strong
    internal-fracture case beyond the Naga claim already carved out — but China's real "South Tibet" claim on
    the *entire* state, centered on Tawang Monastery, is a live external complication worth a deliberate
    decision); Darjeeling/Kalimpong themselves (merge into Sikkim, given the shared Nepali/Gorkha identity and
    direct geographic adjacency, or stand alone).

**Not yet decided — the author's own explicit next call, do not default to an answer**: how granular to make
the breakaway split. Tier 1 alone is six countries; adding some or all of Tier 2 could reach ten or more.

**The line is pinned to coordinates (2026-09-29) — see the survey file's "The line, pinned to coordinates"
section**: (1) Nepal–Bihar–West Bengal tripoint ≈ 88.102°E, 26.542°N; (2) Bihar/West Bengal border meets the
Mahananda ≈ 88.242°E, 26.449°N; (3) Mahananda reaches the Bangladesh border ≈ 88.3327°E, 26.4962°N
(Tentulia Upazila), author-verified against the two Google Maps landmarks. The line is made entirely of whole
district boundaries (Kishanganj/Darjeeling, then Darjeeling/Uttar Dinajpur), so there is no river-precision
tradeoff. **No part of Uttar Dinajpur or Kishanganj breaks away.** A check map is at `y-files/Map Files/Asia
(South-Central)/01 initial generations/siliguri_line_check.png`.

**Stage 1 completed 2026-09-29 (a second session, after the display-corruption interruption)** — six new
surveys in `worldbuilding/extractions/`, all Latin-script only, all ⚠️-flagged, none choosing for the author.
Each is 9,000–13,000 words; the two Northeast surveys replace the Wikipedia-only first pass with district-level
census data and correct it (see the scoping file). Files, one line of headline each:
- **Pakistan** (`Pakistan - The Indus Plain, the Pashtun and Baloch Rim, and Five Live Fracture Lines`) —
  Plain / Rim / Roof framework; 27th Amendment (13 Nov 2025) made the army constitutional; Karachi is
  city-state scale (20.4M, 11.1% Sindhi-speaking); four whole-province rule breaks.
- **Nepal and Bhutan** (`Nepal and Bhutan - The Three Belts, the Madhesh Line and the Southern Bhutan Exodus`)
  — the Terai is 53.6% of Nepal but Madhesh Province is only ~39% of it; under the pinned line Bhutan borders
  only breakaway-slice territory, and the Duars Bhutan lost in 1864-65 lie inside it.
- **Bangladesh** (`Bangladesh - The Delta, the Double Partition and the Hill Frontier`) — the only real internal
  territorial fracture is the Chittagong Hill Tracts (3 districts, 1.84M, 49.94% indigenous); the Teesta's whole
  Indian course is in the breakaway slice; the Ganges treaty expires December 2026.
- **Sri Lanka** (`Sri Lanka - Chronicle, Census and the Eastern Three-Way`) — built on the final 2024 census;
  Eastern Province has no majority (Moor 39.5 / Tamil 38.1 / Sinhalese 22.1); nine options A-I.
- **Northeast India, hills** (`Northeast India (Naga-Manipur-Mizoram hills) - Excluded Areas, Valley and Hill,
  and the Three-Way Fault`) — Nagaland has 17 districts; a Naga-Kuki front opened February 2026; five mixed
  Manipur districts (Kangpokpi, Chandel, Tengnoupal, Noney, Jiribam); Frontier Nagaland Territorial Authority
  signed February 2026; the published Nagalim map is mostly not Naga on census figures.
- **Northeast India, rest** (`Northeast India (Assam-Tripura-Sikkim-Gorkha hills) - Valleys, Hills and the
  Citizenship Ledger`) — the line takes 8.54M people in northern Bengal, only ~10% in the Gorkha hill core;
  Assam is 64% of the scope; three drawing-rule breaks (Bodoland Territorial Region, Darjeeling hills vs
  Siliguri, TTAADC).

**Initial cultural maps generated 2026-09-29 (Stage 3 staging + first Stage 4 pass)**: `nations/south-asia-map-data/`
holds `regions.csv` (39 working cultural regions in six structural tiers), `spheres.csv` (15 overlays),
`languages.csv`, `units/` (district drawing units) and `classification/` (six CSVs, one row per unit, every row
tracing to a survey table). The eight rendered maps and the reproducible renderer (`render.py`,
`south-asia-base.gpkg`) are in `y-files/Map Files/Asia (South-Central)/01 initial generations/` with a README that
lists the known limits and the scheme gaps to fix in the next revision. **Unreviewed by the author.** The maps use
**districts**, not whole first-order subdivisions — a flagged exception decision (see the README).
**Follow-up 2026-09-29** (`y-files/Map Files/Asia (South-Central)/02 reorganization/01 follow-up/`, with `CHANGES.md`):
Pakistan's whole Baluchistan province is cut out as already-mapped Balochistan (West Asia package); R20 Pashtun Rim is
now KP and ex-FATA only. `01 initial generations/` is the unchanged first-pass archive; further rounds go in the next
numbered `02 reorganization/NN follow-up/` folder.
**Follow-up 2026-09-29 (second round)** (`02 reorganization/02 follow-up - initial maps/`, with `README.md`): tentative-country
maps of what is settled (Pakistan minus Balochistan, Nepal, Bhutan, Sri Lanka, Bangladesh) plus **each of the seven
Northeast states (Sikkim, Meghalaya, Assam, Nagaland, Manipur, Mizoram, Tripura) drawn as its own reference country**,
so the author can judge how the Northeast would divide; Arunachal Pradesh and North Bengal are shown as undecided.
Key geometry fact from that round: among Sikkim, Meghalaya, Tripura and Mizoram only Tripura and Mizoram touch
(Meghalaya is ~61-67 km from them, Sikkim 188-478 km); Assam touches every other Northeast state.
**Northeast groupings floated by the author (2026-09-29, tentative, NOT decided; `map-11` and `map-12` in that folder):** (A) Sikkim,
Meghalaya, Assam, Mizoram, Tripura and North Bengal (Darjeeling, Kalimpong, Jalpaiguri, Alipurduar, Cooch Behar) unified into one
country, Nagaland and Manipur each their own country; (B) all eight in one country with Nagaland and Manipur as Autonomous Zones
inside it. Geometry checked: the six are contiguous (one 153,155 km2 polygon, ~48.1 M people, Assam 64.9%); Arunachal Pradesh is
unassigned in both. An earlier four-way union (Sikkim+Meghalaya+Tripura+Mizoram) was ruled out on the data: non-contiguous.
**Author's strong preference, 2026-09-29: proposal B** ("I really, really like the idea of the one single country with two
Autonomous Zones") — one country of the eight units, Nagaland and Manipur as Autonomous Zones. Not yet declared settled; still to
resolve: Arunachal Pradesh's placement, each zone's powers (defense, police, taxes, the Myanmar border), whether the zones are
demilitarized, whether Manipur's Naga districts join the Nagaland zone, and the union's name.
**Author's answers, 2026-09-29 (working folder now `02 reorganization/03 follow-up - decisions/`):** (1) **Arunachal Pradesh joins as a
third Autonomous Zone**; (2) zone powers: undecided; (3) **each zone has a standing military** (size and equipment undecided);
(4) **Manipur's Naga districts are proposed as "disputed"** (Senapati, Ukhrul, Kamjong, Tamenglong, Noney); (5) the union's name is
undecided, with the author leaning toward a Buddhism-related name. Map: `map-13-proposal-B-revised-three-autonomous-zones.png`.
Note for the name: with Arunachal the union has nine units, not eight (six core units plus three zones).
**Name leaning (author, 2026-09-29):** some variation of **"Madhyama"** (Sanskrit, "middle"; the Buddhist Middle Way / Madhyamaka)
was the leaning; **the author then chose "Madhyama" as the cleanest and most fitting name** (it does not lean hard into Buddhism at the expense of the
Christian and Muslim populations). Exact form (Madhyama, Madhyamaka, ...) not fixed.
**Zone bargain (author's direction, 2026-09-29):** in exchange for serving in the armed forces and training the rest of the country, the
Naga and Manipur people are free to run their own societies inside their Autonomous Zones with minimal (possibly no) taxation and
minimal government interference. Open: whether one union army or three zone armies; whether Arunachal's zone gets the same deal;
how the zones are funded; civilian control of the military; how factional militias become zone forces.
**2026-09-29: the whole internal military structure is deferred** (the author is not knowledgeable about military life). The full record of
decisions and open items is `worldbuilding/nations/Madhyama and the Northeast - Decision Log and Open Items (working).md` (copy in the
`03 follow-up - decisions/` folder). Madhyama = the six core units plus three Autonomous Zones, adopted as the working structure, not yet formally declared settled.
**2026-09-29, end of the South Asia country decisions:** the author called South Asia "fully settled" and asked for the final country maps —
done: `y-files/Map Files/Asia (South-Central)/02 reorganization/04 follow-up - final maps/` (whole region, Pakistan, the Northeast/Madhyama, Sri Lanka).
Economic work (Stage 2) is deferred to future sessions. Madhyama's internal military structure, zone powers and the disputed-district mechanics
remain deferred (see the decision log).
**Official maps (2026-09-29):** the four final maps redrawn with plain solid colors, national borders only and capitals marked, in
`y-files/Map Files/Asia (South-Central)/02 reorganization/05 follow-up - official maps/` (whole region, Pakistan, Madhyama, Sri Lanka).
**Madhyama's capital: Guwahati (author, 2026-09-29, settled)**; marked on the official maps. (Candidates weighed: Shillong, a planned capital near Nagaon, a split capital; Siliguri ruled out as too exposed.)
**Refined 2026-09-29:** instead of minimal or no taxation, the zones pay **extended military service** (about twice the length, plus extra
responsibilities, compared with the rest of the country), and **the rest of the country's taxes pay for what the zone peoples would
otherwise have paid taxes for.** Arithmetic: the three zones hold ~6.22 M people (2011) against ~48.1 M in the six core units, i.e.
about 11.5% of the nine-unit population of ~54.3 M. Open: quota vs universal service, funding formula, civilian control.

**Author decisions SETTLED so far in South Asia (2026-09-29):** (1) the India dividing line, pinned to coordinates
(above); (2) Pakistan's whole Baluchistan province is Balochistan, already mapped in the West Asia package — not
re-cut here; (3) **the Pashtun portion of Pakistan (Khyber Pakhtunkhwa and the ex-FATA districts) stays part of
Pakistan**, decided after the geology/hydrology and public-opinion/retake-cost notes in the Pakistan survey
§7.2b-7.2d; (4) **Pakistan is settled: everything except the Baloch portion stays one Pakistan** (Punjab, Sindh
incl. Karachi, the Saraiki belt, Khyber Pakhtunkhwa and the ex-FATA, Gilgit-Baltistan, Azad Kashmir and Islamabad all
remain Pakistani; the Pakistan survey §11.2 records it). **No Pakistan partition decisions remain open**; the South Asia
maps' Pakistani regions are cultural, not political. (5) **Sri Lanka does not split — it stays one country** (Sri Lanka survey §10 records it; the Eastern
Province and up-country Tamil territorial questions are closed, the cultural regions stay descriptive). (6) **Nepal and Bhutan both stay intact, exactly at their current borders** (Nepal and Bhutan survey §11:
Nepal option 1, Bhutan option 6; the Madhesh, Tharuhat and Limbuwan claims are carried as internal tensions, not
partitions). **Their inter-country relationship (trade, cultural ties, the Lhotshampa rift) is deferred to a later
session**; only the sphere-layer question stays open for these two. (7) **Bangladesh stays its own country at its current borders** (Bangladesh survey §6.5 and §9.2; the
Chittagong Hill Tracts do not break away and Sylhet does not split; only the CHT's *internal* treatment — no recognition,
sphere overlay, or a bounded autonomous zone — remains open, and it changes no border).

**Author decisions now open (each is set out as an options menu in its survey)**: the breakaway split's
granularity (the headline decision); the Chittagong Hill Tracts' internal treatment within Bangladesh; the Barak
Valley's fate (Sylhet stays in Bangladesh); Teesta ownership; whether sphere layers are added; whether a separate Tibet inherits the PRC's Bhutan/Arunachal claims;
the exception rule for the five mixed Manipur districts; and the three Northeast drawing-rule breaks.

**⚠️ Cross-file inconsistencies this pass surfaced (also §5)**: (a) the West Asia map already draws Pakistan's
Balochistan as a Baloch-majority core region, but the 2023 census gives Balochi 39.9 / Pashto 34.0 / Brahui
17.2, Quetta District 60% Pashto, ten northern districts 86-99.9% Pashto; (b) the Mainland Southeast Asia survey
does not mention that the Arakan Army has held Myanmar's entire Bangladesh border since 9 Dec 2024.

**⚠️ Unverified items flagged for a check before they harden into canon**: Sri Lanka's inflation-peak figure (a
17.5% figure appears in the survey and looks far too low for 2022), the Rohingya count (1.17M vs 1.3M),
post-February-2026 Bangladesh events, Gilgit-Baltistan 2026 status, the Assam post-2021 district list in the
boundary dataset, and the 2026 Naga-Kuki and Manipur displacement figures.

**Immediate next steps, in order**: (1) author works through the open decisions above, starting with the
breakaway split's granularity; (2) Stage 2 material surveys for the five countries and every candidate
entity that survives that decision; (3) Stage 3 map data — the line itself needs no precision tradeoff, but
confirm the boundary dataset carries Assam's post-2021 districts; (4) Stage 4/5 as normal.

### 4.10 Europe — Intermarium research done 2026-09-29 (Stage 1 begun; nothing decided)

**Canon:** the roster's line "The Intermarium, later renamed Intermarija — a unification covering much of Eastern Europe" (author, 2026-09-18). **New premise (author, 2026-09-29):** about a
generation after the 2083 war the Eastern European countries form the **Confederacy of Intermarium Nations**. Six files in `y-files/Map Files/Europe/01 initial generations/`
(five research notes plus `Intermarium - Overview and Synthesis (survey).md`, which is the one to read first): history of the idea; the modern initiatives (Three Seas etc.); the northern and
eastern tier incl. Kaliningrad; the central European and Balkan tier; confederal precedents and design options. **Open (all the author's):** which countries (four options A-D in the synthesis);
Kaliningrad's status (the Russia notes deferred it to Europe); the fate of NATO, the EU and Germany in the fiction; the form (confederacy vs unification; whether "Intermarija" is a later rename);
the seat, language/script, religion, defense, veto rules; and the rest of Europe (Western and Southern Europe, Scandinavia, UK and Ireland) is still undocumented. The web-search budget ran out
during the research, so 2025-26 items are flagged for re-checking.
**Author's answers 2026-09-29:** the Confederacy is "more than a Union, but less than a Federation" (sovereign national cultures; a confederacy, definitively); NATO and the EU have both collapsed
(Russia and the USA already known from earlier work; Germany undecided); membership starts skeletal and absorbs countries over time (which countries: undecided); Kaliningrad stays "independent" within the
confederacy (majority Russian, capital Kaliningrad); the confederacy's capital **begins in Lublin and later relocates to Katowice** (author, 2026-09-29; the trigger and timing of the move are open).
**Europe cultural research launched 2026-09-29** (Woodard-style): seven research notes `Europe - 0 ... 6 ...` in `y-files/Map Files/Europe/01 initial generations/` (framework and tiers; British Isles and Iceland;
France, Benelux and the Alpine states; Iberia, Italy and the Mediterranean islands; Germany, Austria and the Nordics; the Baltic-Poland-Ukraine-Carpathian states; the Balkans and Greece). The author also says part of eastern Ukraine becomes
Russian in the setting; the border is to be worked out later with the researcher's help (evidence in the eastern Ukraine section of note 5). The capital's relocation trigger: the author is not sure yet.
**Europe cultural research DONE 2026-09-29** (seven notes plus `Europe - Overview and Synthesis (survey).md`, which is the one to read first): a continental framework (a three-tier scheme, Realm/Region/Identity, replacing
first effective settlement with the "last effective reset"; 40 continental regions, about 28 merged) and six regional notes proposing about 205 fine regions; the whole-subdivision rule breaks in about 30 places; French départements are
recommended as units. Open decisions are the synthesis §7. The eastern-Ukraine border has an evidence base (Europe 5 §7, nine cut-line options) but no proposal.

**Europe first-pass Woodard-style maps rendered 2026-09-30** (author asked for "a Woodard-style map of Europe"; East Asia named as the better house-style model than South Asia): `map-1-cultural-regions.png` (40 regions, core/domain/sphere) and
`map-2-seven-realms.png`, and (author-requested, same day) `map-3-languages.png` and `map-4-religion.png`, with `render.py`, `build_data.py`, `map-data/` (incl. `lang-religion/` with six per-region classification files and notes) and a README listing the judgment calls, in `y-files/Map Files/Europe/01 initial generations/`. Chosen resolution: the framework's 40 regions with Natural Earth admin-1 units
(French départements). **Author decisions 2026-09-30:** Poitou-Charentes homed in region 16 (domain); Corsica gets its own designation, region 41. The eastern Ukraine border is **not** drawn; **three whole-oblast candidate packages (A core: Crimea, Sevastopol, Donetsk, Luhansk; B plus Zaporizhzhia and Kherson; C the language belt) and a recommendation (start from A; treat the Azov land bridge as a separate contiguity decision, drawn at raion level) were drafted 2026-09-30 in `Europe/02 reorganization/01 follow-up/` (`Eastern Ukraine - Candidate Border Lines (working).md`, `eastern-ukraine-candidate-lines.png`); the author then proposed their own line (Black Sea up the Dnieper past Dnipro, then north along the western edge of Kharkiv Oblast to the Russian border; Crimea to Donska-Kubania), clarified 2026-09-30 (version 2, `eastern-ukraine-proposed-line-v2.png`): **Luhansk, Donetsk, Kharkiv, Dnipropetrovsk and Zaporizhzhia whole; Kherson only east of the Dnieper (about 75% by area); Crimea goes to Donska-Kubania as an Autonomous Zone (author, 2026-09-30: it was autonomous through almost the whole Ukrainian period; Sevastopol assumed to go with it)**; decisions logged in `Europe/02 reorganization/01 follow-up/DECISION LOG - Eastern Ukraine and Crimea.md` and `map-data/designations.csv`; **Crimea and Sevastopol applied to the Russia project 2026-09-30 in `Russia/02 reorganization/08 follow-up - including Crimea/`** (full/West/reference/Woodard re-rendered, Center/East unchanged; see its CHANGES.md); **then the author confirmed the mainland slice goes to the Russia nation (2026-09-30) and it was applied in `Russia/02 reorganization/09 follow-up/` (now the authoritative Russia folder; six Russia rows, Kherson left bank as a district-level exception, same four maps re-rendered)**; the author's villages all lie within 10 km of existing oblast borders, so the trace is the oblast border; about 16 million people on the mainland plus about 2.4 million in Crimea and Sevastopol at the 2001 baseline (about 38% of Ukraine); cities added on the Russia maps (Kharkiv, Dnipro, Donetsk; Zaporizhzhia and Luhansk on the West close-up); open: the Kherson left bank at raion level, the name forms; **the Europe cultural maps 1 to 4 are deliberately NOT reduced (author, 2026-09-30): they carry a red reference border for the proposed Russia–Ukraine line instead**. Language/religion rows: 52 confidence 3, 1,285 confidence 2, 263 confidence 1; the weakest layers are Germany's religion, Belgium/France/Switzerland religion (surveys), Latvia and the Balkans (no unit-level census in the notes). Still open: the framework's §7 decisions, regional zooms, the Part 4 sphere overlay, re-checking confidence-1 rows against primary census tables.

**Confederacy membership order (author, 2026-09-30)**, logged in `Europe/02 reorganization/01 follow-up/DECISION LOG - Confederacy of Intermarium Nations (membership order).md` and drawn in `confederacy-accession-order.png`: Poland the core at present-day borders (ULB doctrine); then Lithuania and Kaliningrad (now a country), Czechia and Slovakia, Latvia, Estonia, Belarus on a restricted observer basis (Poland's mistrust of Russians), Ukraine, Hungary, Romania, Bulgaria, the Balkans on a partial basis; **Albania forbidden by unanimous decision, a hard block**. **Hungary takes Satu Mare and Bihor from Romania** (the Partium); Székely Land stays Romanian and **Romania would never grant it autonomy** (author). Open: Moldova (author forgot it; to be placed), which Balkan countries count, whether the Albania block covers Albanian-majority territory elsewhere, the rest of Europe.

### 4.7 Everything else

South Asia, Egypt/North Africa (both explicitly out of West Asia's scope); Africa generally; Europe beyond the
Intermarium.

**Africa (Northwest-North) — Stage 1 research and first-pass maps done 2026-10-01.** Read `y-files/Map Files/Africa/Africa (Northwest-North)/01 initial generations/README - Africa NW-N initial cultural maps.md`
first. Open author decisions: how to present Western Sahara (five options in note 1 §10); keep the Natural Earth units (Algeria 48 wilayas, Mali 9 regions, Morocco's old 16) or rebuild on current divisions (Algeria 58, 69 from 2027; Mali about 20);
Kabylie and the Aurès as one region, two or a sphere; the Rif; Timbuktu; Tindouf; the MAK proclamation; the Haratin overlay. Ariana is merged into the "Manubah" polygon (confirmed against the data). Next: the author reviews the four maps, then
Northwest-South (including Cabo Verde), then North-Center, Northeast, Central and South.

---

## 5. ⚠️ Known inconsistencies — fix these

1. **`nations/World-Nations-Roster.md` says Latin America has "no nations named yet."** **Now stale for all of
   Latin America** — South America (accepted canon 2026-09-24, rendered and author-confirmed), Central America
   (decided 2026-09-25, real-world names throughout plus the finalized "La República de Yucatán"), and the
   Caribbean islands (decided 2026-09-25, real-world names throughout plus Saint Martin, final and bilingual)
   are all fully decided now — the only thing outstanding anywhere in Latin America is rendering Central
   America and the Caribbean, not naming. The roster should say so. **The accepted `nations-assignment.csv`
   should also be brought into the repo as map-data** rather than living only in the output folder.
2. **The roster's Asia section and running tally** predate the eight-map series and the Qinghai/southern-border
   decisions. **Re-read against §3 above.**
3. **`TepenianUniverseTimeline/Reference/World_History_Reference.md`** still records Qinghai as *"unresolved
   and drawn hatched/unassigned."* **Now settled** — but that repo is not to be edited without an explicit
   instruction. Flagged, not fixed.
4. **`east-asia-map-data/01 INIT/`** holds superseded instruction sheets, several already banner-flagged as
   partly out of date. **`02 maps/` is the live set.**
5. **Balochistan's "Baloch-majority" premise** (Middle East survey §9 and `middle-east-map-data/regions.csv`
   `balochistan` rows) does not survive Pakistan's 2023 census for the province as a whole: Balochi 39.9%,
   Pashto 34.0%, Brahui 17.2%. The author-settled cross-border Balochistan region stands (the whole Baluchistan
   province, as drawn in West Asia) and **the South Asia maps now cut along that province line** (2026-09-29,
   `02 reorganization/01 follow-up/`); the premise wording needs a note. See the Pakistan survey.
6. **The Mainland Southeast Asia survey** omits that the Arakan Army has held Myanmar's whole border with
   Bangladesh since 9 Dec 2024 (found by the Bangladesh survey).

---

## 6. Character and story work in flight

- **Melinda Barlow** — a **prefilled seed block** is staged in `character_seed-input.txt` with origin,
  timeframe and backstory filled. **Needs from the author:** Type (robot or human — *not stated*), the
  Personal Vision, Enneagram + Undercurrent, personality, weakness, goal. Then → Stage 1 Derived Sheet.
- **⚠️ The author has handwritten notes for roughly 90% of all stories**, not yet transcribed. Process:
  photograph the pages, give the folder path, transcription follows the Streetside Harmonies convention —
  flag uncertain words inline, preserve table structure, flag stray personal content.
- **Her project folder does not exist yet.** `y-template/` is novel-shaped (`text/`, "stanza scene and chapter
  breakdowns"); a 20-minute short film wants different scaffolding. Decide when standing it up.

---

## 7. Suggested order for the next session

**Six regions officially done, author-confirmed**: North America (incl. Hawaii's corner-box inset), Latin
America (Central + South America), East Asia, both Southeast Asia maps, Oceania (both companion maps, through
three WebUI-confirmed rounds — framing fix, flat-color pass), and, as of 2026-09-29, **West Asia** (Central
Asia + Middle East/Turkey/Afghanistan + South Caucasus — see §4.8's own closing summary for the full picture).
Nothing to pick up in any of these six unless the author opens something new. Small carried-forward items, not
blocking, listed below.

**South Asia opened 2026-09-29, immediately after West Asia's completion, IN PROGRESS — see §4.9 for the full
handoff, read it before doing anything else here.** Scope: Pakistan, Nepal, Bangladesh, Bhutan, Sri Lanka plus
one precisely-bounded breakaway slice of Northeast India (India itself otherwise explicitly out of scope — zero
research). **Stage 1 is done for all of it (seven files) and the India dividing line is pinned to coordinates;
the next step is the author working through the open decisions listed in §4.9, starting with the breakaway
split's granularity, then Stage 2 material surveys.**
**This is the active region — pick this up next, not Russia/Europe/Africa below**, unless the author redirects.

**Three regions remain after South Asia, none started — the author's own inventory, 2026-09-26**: Russia,
Europe, and Africa (which will be "a vastly enormous undertaking," the author's own words). West Asia —
originally named as the region after Russia, since it borders both the Sinian Federation and Russia and would
have benefited from Russia's borders existing first — was instead picked up and fully completed out of that
original order, and South Asia was opened right after it, also out of the original order. Russia's own Stage 1
frameworks work (§4.5) still needs Stage 2 material survey before its map data can be built. Standing order
once South Asia is done, unless the author redirects: **Russia → Europe / Africa** (Europe vs. Africa order not
yet discussed). Africa is explicitly flagged by the author as the biggest lift of the three.

**Small carried-forward items, not blocking, pick up whenever convenient:**
- **✅ DONE 2026-09-28, fully closed**: the Araucánia–Patagonia Autonomous Zone is named (APAZ / ZAPA, see
  §4.2), propagated to `nations.py`/`nations-assignment.csv`, genuinely re-rendered into `map-7-nations.png`
  with the author's own bilingual label treatment, and synced to `World-Nations-Roster.md` (which also got a
  full staleness fix across every other region while in there).
- The Southeast Asia Deep South still needs its final name (Patani is the obvious candidate, not yet
  asserted) — Stage 5, same as every other region's placeholder-named nations.
- The optional Myanmar conflict-snapshot map, and the Southeast Asia material survey's Cambodia count
  correction (both §4.3).
- **Fix the roster inconsistencies in §5.** `nations/World-Nations-Roster.md` still says Southeast Asia is
  "entirely undocumented" (line ~108) — stale, now that both SE Asia maps are done.

**Do the searching early in the session** — still true for whichever of Russia/West Asia/Europe/Africa gets
picked up next; every region so far has needed a real-world material/frameworks research pass before map data
could be built.
