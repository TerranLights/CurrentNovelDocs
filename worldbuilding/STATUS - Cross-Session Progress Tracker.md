# STATUS — Cross-Session Progress Tracker

**Read this first in any new session that touches worldbuilding or maps.** Last updated **2026-09-24**.

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
| **North America** | ✅ *(Woodard)* | ✅ 9 nation files | ✅ | ✅ | ✅ canon |
| **East Asia** | ✅ ~23,700 w | ✅ ~21,600 w | ✅ 8-map series | ✅ **all 8** — *visual tweaks pending* | ❌ **4 placeholders** |
| **Latin America** | ✅ | ✅ | ✅ 3 CSVs | ⚠️ draft nations map | ❌ **placement under author review** |
| **Mainland SE Asia** | ⚠️ ~3,500 w | ⚠️ ~3,100 w | ❌ | ❌ | ❌ |
| **Maritime SE Asia** | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Russia** | ❌ | ❌ | ❌ | ⚠️ folders exist, empty | ❌ |
| **South / Central / West Asia** | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Africa, Europe, Oceania** | ❌ | ❌ | ❌ | ❌ | ❌ |

---

## 3. What is settled — decisions that must not be relitigated

**East Asia**

- **The Sinian Federation is the Han core**, not PRC borders. Xinjiang, Tibet, Inner Mongolia and Manchuria
  are separate polities.
- **The southern border is Option A** — Yunnan, Guizhou, Guangxi, Gansu, Hainan and Ningxia are **all**
  Federation territory. *Nothing is hatched any more.* Region 10 "Yungui" **never forms.**
- **Qinghai** joins **The Northwest** in the early era and passes into the Federation at unification. It is
  **not** Tibetan and **not** its own region.
- **Tibet is the TAR and nothing else**, on every map.
- **Manchuria, East Turkestan, Tibet and Taiwan never join the Federation.**
- **Mandarin splits three ways** in the early era — North China Plain, The Northwest, Bashu — with Jianghuai
  folded into Wu.
- **Hakka has no territory in any era.** Drawn as hatched pockets, never a border.
- **Jeju-do** becomes a three-power condominium (Korea, Japan, the Sinian Federation) on Map F, with **Korean
  taking precedence in any conflict-in-translation.**
- **The map series is eight maps with two branch points:** `A → B1|B2 → B3 → C|D → E → F`.

**Mainland Southeast Asia**

- **Mainland first, maritime later.** Indonesia is to get its **own internal division** when maritime is done.
- **The mandala is carried natively** — cores get hard borders, **spheres overlap and the overlaps are
  correct.** This is the one region where `sphere_territory` does real work.

**Universe-wide**

- **Melinda Barlow** begins the commensal relationship that makes bats semi-tame "wild pets" centuries later.
  A ~20-minute **short film**. Canon in `history/Bat Semi-Domestication - the Commensal Pathway.md`.

---

## 4. Open work, in priority order

### 4.1 East Asia — closest to finished, three items left

**All three are settled in the handoff package at**
`y-files/Map Files/Asia (East)/05 follow-up - sem-finalized [not all permanently named]/`
which contains `ea_series.py`, an enriched `data/polities.csv`, `naming_worksheet.csv`, `series_graph.csv`
and `open_questions.csv`. **That package supersedes every earlier East Asia output.**

1. **⚠️ NAMING — two parts, both author-led.**

   **(a) The four placeholders must be named:** `NCP` (The North China Plain), `NW` (The Northwest), `NKO`
   (Northern Korea), `SKO` (Southern Korea). **The Koreas must not use present-day state names.**

   **(b) ⚠️ Slight adjustments to the naming more broadly** — author-stated 2026-09-24, specifics not yet
   given. **This is not limited to the four placeholders**; names already marked `WORKING` or `ESTABLISHED`
   may also be tweaked. **Ask which ones before changing anything.**

   **Mechanically, both are the same edit:** fill `final_name` / `final_map_label` in `naming_worksheet.csv`,
   copy into `polities.csv`, re-run the renderer. Every map updates because every map reads the same row.
   *The package carries `precedent_names_from_notes` — Qin, Shu, Wuyue, Chu and others already cited in our
   own notes — so this is a choosing problem, not a research problem.*
2. **⚠️ DECIDE THE TWO BRANCH ORDERS**, or confirm they stay parallel: **B1 or B2 first** (Qinghai, or the
   Mongolias) and **C or D first** (Korea, or the Federation).
3. **⚠️ MINOR VISUAL ADJUSTMENTS to the rendered maps** — author-stated 2026-09-24, specifics not yet given.
   **Ask what they are before re-rendering.** Because `ea_series.py` reads only `data/`, most visual changes
   are a data edit plus one re-run rather than a rebuild.

### 4.2 Latin America — the surveys are done; the borders are not

**⚠️ NOT FINISHED. Author-stated 2026-09-24: the placement of the new countries needs reviewing — where the
nations would actually be drawn.**

A draft exists: `y-files/Map Files/Latin America/03 follow-up/` holds `nations-assignment.csv` (**394 rows**,
named nations such as Amazonia mapped onto first-order subdivisions), `map-7-nations.png`, and the render
scripts. **Treat it as a proposal to argue with, not an accepted map.**

**What it needs:** the author to walk the assignment region by region and accept, reject or redraw — the same
"research proposes, author disposes" step East Asia went through for its southern border and Qinghai. **This
is a review, not new research.**

**And it is the reason the roster still says no nations are named** — the names exist in a draft nobody has
signed off. See §5.1.

### 4.3 Mainland Southeast Asia — surveys are a frame, not a finished pass

**~6,600 words against East Asia's ~45,000.** Written under an exhausted search budget.

**Blocking the map stage:**

- **⚠️ Vietnam's first-order subdivision count.** It reorganized its provinces in **2025** and the current
  count is unknown. **Every other country is established** — Myanmar 14 + Nay Pyi Taw, Cambodia 26, Laos 17 +
  Vientiane, Thailand 77. **This one gap blocks the CSVs.**

**Largest analytical holes:**

- **⚠️ Myanmar's conflict map** — which armed groups hold which ground. Named in both files as the single most
  important gap. Also: whether the **Wa** are a de facto state.
- **⚠️ No ECI data for any of the five.** Both other regional surveys use economic complexity as their
  quantified backbone; this one has no equivalent.
- **⚠️ The Southeast Asian tin belt** — spans Thailand, Myanmar and Malaysia. Historically world-significant,
  entirely absent.
- **⚠️ Ports** — Haiphong, Laem Chabang, Yangon, Sihanoukville, Da Nang. None covered.

**Per country:**

| | Outstanding |
|---|---|
| **Vietnam** | Least researched. Only Kinh 85.32% known; no minority figures, no minerals, no ports, province count unresolved |
| **Myanmar** | Conflict map; Wa status; gas figures are 2012, teak is colonial; **rare earths uncovered** despite being a major supplier |
| **Thailand** | "Never colonized" unverified and load-bearing; minerals; Laem Chabang |
| **Laos** | Dollar revenue + contract terms; the **38% coal vs 34% hydro vs 80%-of-generation contradiction**; Lan Xang's 1707 three-way split; population shares for the three elevation tiers |
| **Cambodia** | Minerals; Sihanoukville. Otherwise in reasonable shape |

**Also:** the **Zomia seam** with the East Asia survey needs a consistency read. The massif does not stop at
the Chinese border and the two surveys were written separately.

### 4.4 Maritime Southeast Asia — not started

Indonesia, the Philippines, Malaysia, Brunei, Singapore, Timor-Leste. **A full two-survey pass**, larger than
everything in 4.2 combined. **Indonesia gets its own internal division** — decided.

### 4.5 Russia — deferred, and it is now the conspicuous hole

Deliberately excluded from East Asia, with **three seams left white and unclaimed**: Outer Manchuria,
Sakhalin/the Kurils, and Buryatia/Tuva. `y-files/Map Files/Russia/` has folders but **no output**. Every East
Asia map has a blank northern edge because of this.

### 4.6 Everything else

South, Central and West Asia; Africa; Europe beyond the Intermarium; Oceania beyond Hawaii.

---

## 5. ⚠️ Known inconsistencies — fix these

1. **`nations/World-Nations-Roster.md` says Latin America has "no nations named yet."** **Strictly that is
   still correct** — the 394-row `nations-assignment.csv` is a *draft awaiting author review* (§4.2), not
   accepted canon. But the roster should say so explicitly, because a draft that detailed reads as settled to
   anyone who finds it first. **The assignment file should also be brought into the repo as map-data** rather
   than living only in the output folder.
2. **The roster's Asia section and running tally** predate the eight-map series and the Qinghai/southern-border
   decisions. **Re-read against §3 above.**
3. **`TepenianUniverseTimeline/Reference/World_History_Reference.md`** still records Qinghai as *"unresolved
   and drawn hatched/unassigned."* **Now settled** — but that repo is not to be edited without an explicit
   instruction. Flagged, not fixed.
4. **`east-asia-map-data/01 INIT/`** holds superseded instruction sheets, several already banner-flagged as
   partly out of date. **`02 maps/` is the live set.**

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

1. **Name the four East Asia placeholders and settle the branch orders.** It is the closest thing to finished
   and it is a decision, not research.
2. **Resolve Vietnam's province count.** One search, unblocks the whole Southeast Asia map stage.
3. **Then either:** review the Latin America nations placement (§4.2 — a decision, not research), deepen mainland SE Asia (Myanmar's conflict map, ECI, the tin belt, ports) — **or** start
   maritime SE Asia, which is a blank page and a bigger prize.
4. **Fix the roster inconsistencies in §5** whenever convenient; they are cheap and they mislead.

**Do the searching early in the session.**
