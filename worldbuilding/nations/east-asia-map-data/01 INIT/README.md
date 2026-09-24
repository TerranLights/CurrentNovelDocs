# East Asia Map Data — for Image Generation

2026-09-23. Machine-readable datasheets derived from
`../../extractions/East Asia - Frontiers, Civilizational Spheres and the Han Core (survey).md`,
`../material-base/East Asia - Material and Economic Base (survey).md` and
`../China - Ethnolinguistic Map (read from reference).md`, formatted so they can be handed to an
image-generating model to draw approximate regional maps.

**These are FOR CONSIDERATION ONLY.** Three of the twelve regions are settled canon; the rest are a first-pass
division offered to be argued with. Every row names its own merge candidate so rejecting one is an informed
choice rather than a guess.

## The Files

| File | Rows | What it is |
|---|---|---|
| `regions-main.csv` | 12 | The nations layer — East Asia's candidate polities |
| `regions-sinitic.csv` | 10 | **The internal divisions of region 1 only.** Not nations. See the warning below |
| `regions-mandarin-split.csv` | 4 | **Early era only.** Mandarin itself breaking into separate states before the Federation forms — three, plus an optional fourth |
| `regions-optional.csv` | 7 | Candidates deliberately excluded from the 12, listed so they can be drawn if wanted |

---

## ⚠️ READ THIS FIRST — The Two Errors This Map Invites

**Error 1: not saying which map in the series you are drawing.** Whether the ten in `regions-sinitic.csv` are
countries or internal divisions depends on *when* the map is set — and **neither answer is wrong**. Early on
they are **sovereign states with their own external borders**. Later they are **internal lines inside one
Sinian government**, drawn the way US state boundaries are drawn inside the United States. Same ten shapes,
different border weight. See "The Map Series" below, and always state the era in the prompt.

**Error 2: producing a culture-area map instead of a nations map.** The Latin America pass returned a map of
overlapping cultural zones when what was needed was a map of countries with borders. **This is a nations map.**
Every region is a polity with a hard external boundary. `sphere_territory` is the *only* column that may
overlap or fade, and it is decoration, not a border.

---

## The Map Series — These Files Describe Two Eras, Not One

**Author, 2026-09-23:**

> What displays as "The Sinian Federation" was initially a smattering of multiple countries, who then unified
> into one federated country. A similar thing happened where, in the early era, there was Mongolia and Inner
> Mongolia, which later unified into simply "Mongolia" — similarly, though not identically, to how there
> became one single Korea.
>
> This means that there would be **multiple maps for the landmasses**, in order to track the progression of
> how these various landmasses developed over time.

**So East Asia is a map *series*, not a map.** The post-2083 collapse fragmented the region; the centuries
after it are a story of things coming back together, at different speeds and by different routes. The
`early_era_status` column in both CSVs carries what is known.

### What unifies, and into what

| Early era | → | Late era |
|---|---|---|
| A smattering of separate **Sinitic countries** — draw `regions-sinitic.csv` as sovereign states | → | **The Sinian Federation**, one government, those same lines now internal |
| **Mongolia** and **Inner Mongolia**, two states | → | **Mongolia**, one state. *Not a merge candidate — a timeline event* |
| **Two Korean states** | → | **One Korea** |

**This is why `regions-sinitic.csv` does double duty**, and why it is worth having as its own file: the same
ten rows are the early era's nations and the late era's internal divisions. Nothing needs redrawing between
the two maps — only the borders' *weight* changes, from external to internal.

### The one timing anchor there is

**Author, 2026-09-23:** the territory *"becomes the Sinian Federation some generations after the first war —
the one in 2083."*

So the sequence is: **the 2083 war → fragmentation into separate Sinitic states → unification some generations
later.** At roughly 25 years to a generation that puts the Federation's formation somewhere in the **mid-2100s
to early 2200s** — which is a range to work inside, **not a date to quote.** The fragmented map is therefore
not a brief interlude; it is the state of the region for something like a century, long enough that people
live and die inside it.

### Mandarin itself splits — RESEARCHED AND CONFIRMED, 2026-09-23

The author asked whether Mandarin might break into two or three states before the Federation forms. **The
evidence says yes, and that the number is closer to four or five than two.**

**Mandarin is not one thing.** The *Language Atlas of China* (1987) divides it into eight subgroups, and the
largest is not the one around Beijing:

| Subgroup | L1 speakers | Where |
|---|---|---|
| **Southwestern** | **260 million** | Hubei, Sichuan, Guizhou, Yunnan |
| **Central Plains** | **186 million** | Henan, central Shaanxi, eastern Gansu |
| Northeastern | 98 million | The Northeast — *already drawn separately as region 4, Manchuria* |
| Jilu | 89 million | Hebei and Shandong |
| Jianghuai | 86 million | Jiangsu and Anhui along the Yangtze |
| Jiaoliao | 35 million | The Shandong and Liaodong peninsulas |
| Beijing | 27 million | Beijing, Chengde, northern Hebei |
| Lanyin | 17 million | Central and western Gansu, Ningxia |

**Southwestern Mandarin alone has more speakers than the capital core's three subgroups combined.**

**Two independent historical fragmentations, a thousand years apart, produced substantially the same units.**
This is the same convergence test the project already applied to Ribeiro/Wagley and to Lattimore/Hu, and here
it runs three ways — 10th century, 20th century, and the dialect map:

| Linguistic nation | Ten Kingdoms (907–979) | Warlord Era (1916–1928) |
|---|---|---|
| **Jin** | **Northern Han**, capital Taiyuan — Shanxi | **Shanxi clique** — Yan Xishan held Shanxi alone, on a deliberately different railroad gauge from the rest of China |
| **Min** | **Min**, capital Fuzhou — Fujian | — |
| **Yue** | **Southern Han**, capital Guangzhou — Guangdong, Guangxi, Hainan | Guangdong warlords; Old and New Guangxi cliques |
| **Xiang** | **Chu**, capital Changsha — Hunan | Hunan warlords |
| **Wu** | **Wuyue**, capital Hangzhou — Zhejiang, southern Jiangsu | — |
| **Southwestern Mandarin** | **Former Shu** *and* **Later Shu**, both capital Chengdu, plus **Jingnan** in Hubei | Sichuan clique; Yunnan clique |
| **Jianghuai** | **Yang Wu** and **Southern Tang**, capital Nanjing | Anhui clique |
| **Northeastern Mandarin** | — | **Fengtian clique** — 3% of China's population, 90% of its heavy industry |
| **Lanyin Mandarin** | — | **Ma clique**, 1919–1928 — Gansu, Ningxia, Qinghai |

**Seven of the Ten Kingdoms correspond to a linguistic nation on the map.** That is not a coincidence anyone
arranged; it is the same terrain producing the same units twice.

**And one of those units solves a problem the survey called unsolvable.** The Hui — 11.4 million people, no
non-Sinitic language, dispersed everywhere, territorialized nowhere — are stranded by all three
southern-border options. But the **Ma clique was an explicitly Hui Muslim regime that held exactly Gansu,
Ningxia and Qinghai for a decade**, and Lattimore independently named a *"Muslim pale of Gansu and Ningxia"*
as the inner frontier zone. Region **13B** gives the Hui a state without inventing one.

#### The cultural evidence — which consolidates rather than splits

Language alone suggested five Mandarin successors. **Culture cuts it to three, with an optional fourth**, and
the correction came from opera:

- **Qinqiang spans Shaanxi, Gansu *and* Ningxia** as a single tradition. An earlier pass had split Shaanxi
  from Gansu on dialect lines; **one opera tradition across all three says they are one cultural region**, so
  13B is now drawn as one state rather than two.
- **Ping opera** covers Hebei, Beijing and Tianjin; **Yuju** covers Henan. Two traditions, but one wheat-eating
  plain — so they are drawn as one state with an internal seam noted.
- **Sichuan opera** is its own tradition, and *Bashu* / Sichuanese is a **recognized Han cultural subgroup in
  its own right**, not merely a dialect zone.

**The Qing-era Four Great Cuisines are a four-way cultural division of China**, and three of the four fall
inside the Mandarin zone: **Lu** (Shandong, the north), **Chuan** (Sichuan, the west) and **Huaiyang**
(Jiangsu, the east) — with **Yue** (Guangdong) the southern one, already its own nation. Shandong being *the*
representative northern cuisine matters: the north's culinary center is Qilu, not Beijing.

**Everything also agrees on the Qinling–Huaihe line**, which the survey had already established as a measured
discontinuity. Bashu sits on the southern, rice-growing side of it; the North China Plain and the Northwest
sit on the northern, wheat side. **A Mandarin that splits along that line is splitting along the same line
that shows a 5.5-year life-expectancy gap.**

**Recommendation — three states, optionally four:**

| | State | Provinces | Why it holds together |
|---|---|---|---|
| **13A** | **The North China Plain** | Beijing, Tianjin, Hebei, Shandong, Henan | Wheat, the Confucian heartland, Lu cuisine, one continuous plain |
| **13B** | **The Northwest** | Shaanxi, Gansu, Ningxia | One opera tradition (Qinqiang), the loess plateau, the Hui pale, the Hexi Corridor |
| **13C** | **Bashu / the Upper Yangtze** | Sichuan, Chongqing, Hubei *(+Yunnan, Guizhou if in)* | Rice, a mountain-ringed basin, its own cuisine and opera, and the most persistent breakaway in Chinese history |
| **13D** | *Jianghuai / Huaiyang* | Jiangsu, Anhui | **Optional.** Real cultural standing, but a transition zone Skinner groups with Wu |

That gives a fragmented Han world of roughly **nine or ten states**. ⚠️ **A recommendation, not a decision** —
and the single most likely point of disagreement is whether **Shandong (Qilu)** should break out of 13A as a
fourth northern state, which the cuisine evidence would support.

### ⚠️ What is NOT established — do not invent it

- **No dates for any of the three unifications**, beyond the anchor above. The Mongol and Korean unifications
  have no timing at all, and the maps should not imply one.
- **The order is unknown.** Which unification happened first is open, and it matters: a Sinian Federation that
  forms *before* Mongolia unifies is a different neighborhood from one that forms after.
- **Whether all ten Sinitic states were separate**, or whether some were already clustered, is open. Hakka is
  the one member that **cannot** have been a state, since it has no territory in either era.
- **Manchuria, East Turkestan, Tibet and Taiwan have no established early-era status**, and — separately —
  whether any of them *later joined* the Federation is open. The late map draws them outside it.
- **Japan** — the author has indicated no Japanese fragmentation, so it is drawn unchanged in both eras.

### This applies to the whole project, not just East Asia

The same logic reaches **North America** and **Latin America**, whose map data currently describes a single
undated snapshot. The New North America map is presumably a late-era map; what preceded it is undrawn.
**Flagged here rather than acted on** — it is a project-level decision.

---

## Column Reference

| Column | Meaning |
|---|---|
| `region_id` | Stable ID. 1–12 main, 13–22 Sinitic, O1–O7 optional. |
| `region_name` | Display label. |
| `tier1_identity` | The major ethnic grouping. **This is the layer that draws borders.** |
| `lattimore_zone` | Position relative to the Great Wall frontier — core, frontier, or beyond. Use for a simplified map. |
| `status` | `CANON` (settled, do not redraw), `PROPOSED` (argue with it), `CONTINGENT` (exists only on a condition). |
| `modern_territory` | Present-day provinces or countries. **The primary key for placing it.** |
| `core_territory` | Where identity is strongest. **Draw this as solid fill.** |
| `domain_territory` | Clear but lesser control. **Draw as lighter fill.** |
| `sphere_territory` | Wide, mild, overlapping. **Draw as a dotted outline — overlaps here are correct, not errors.** |
| `anchor_cities` | Specific places to hang the shape on. **Most useful single column for accuracy.** |
| `lat_north`, `lat_south`, `lon_west`, `lon_east` | Approximate bounding box, decimal degrees. **Rough guides, not boundaries.** |
| `color_hex`, `color_name` | Suggested palette. **Chosen to match the author's own reference language map** where the groups correspond. |
| `founding_population` | Who set the character, per the tiered-identity method. |
| `characteristic_institution` | The institution that defined it. |
| `confidence` | `high` / `medium` / `low` — how solid the case for this being its own region is. |
| `merge_candidate` | Which region it folds into if simplified. |
| `notes` | Anything a map-maker should know. |
| *Sinitic only:* `norman_zone` | Jerry Norman's three-way grouping — Northern, Central, Southern. |
| *Sinitic only:* `federal_member` | Whether it carries federal weight. Three do not. |
| *Sinitic only:* `skinner_macroregion` | G. William Skinner's physiographic macroregion, for cross-checking. |

## The Coarse Grouping

If twelve regions is too many, `lattimore_zone` collapses them into three, following Owen Lattimore (1940):

- **Core — inside the Wall.** Region 1.
- **Frontier — the contested belt.** Regions 4, 6, 11, and arguably 10.
- **Beyond the frontier.** Regions 5, 7, 8.
- **Outside the Sinic world / Sinosphere.** Regions 2, 3, 9, 12.

**Why this grouping and not another:** the Great Wall, the **Hu Line** (1935), Lattimore's frontier and the
**400 mm rainfall isohyet** are four independent descriptions of one line. East of it, 43% of the territory
holds 94% of the people, and the 2002 and 2015 measurements are essentially identical. **Ninety years, a
revolution and the largest internal migration in human history did not move it.**

---

## Four Hard Constraints

These are settled and must not be redrawn:

1. **The Sinian Federation is the Han core only** — roughly the Eighteen Provinces, inside the Wall. It does
   **not** extend past it. Manchuria, Inner Mongolia, Xinjiang and Tibet are separate regions on this map even
   though all four are inside modern PRC borders.
2. **Whole first-order subdivisions only.** Never split a province, autonomous region, municipality or
   prefecture. This rule is absolute and it is why regions O6 and O7 exist as exclusions.
3. **Russia is deferred entirely.** Three seams touch this map and all three are **blank, unclaimed ground** —
   not Russian, not anyone's:
   - **Outer Manchuria**, north of the Amur and east of the Ussuri. Region 4 stops at the modern Heilongjiang
     and Jilin provincial line.
   - **Sakhalin and the Kurils.** Region 11 stops at the Hokkaido prefectural boundary.
   - **Buryatia and Tuva**, on Mongolia's northern flank. Regions 5 and 6 stop at the modern border.
4. **Scope is East Asia only.** Southeast Asia, South Asia, Central Asia and the Middle East are **out of
   scope** — leave them unshaded and label them as belonging to other nations not yet drawn. Vietnam in
   particular is out of scope, though note the Zhuang/Nùng are the same Tai people under two names across that
   border, together over 15 million.

---

## ✅ The Southern Border — SETTLED 2026-09-23 as Option A

**Author's decision: all six first-order subdivisions — Yunnan, Guizhou, Guangxi, Gansu, Hainan and Ningxia —
are Sinian Federation territory.** Nothing on these maps is hatched any more. Qinghai is settled too, and is
Federation ground by way of The Northwest. **There is no undecided border left in East Asia.**

### Why, in one table

The case for exclusion rested on the language map, which shows those provinces as a shatter zone of roughly
twenty-five peoples. **That reading is right about territory and wrong about population.**

| | Population | Han | Non-Han |
|---|---|---|---|
| Guangxi | 50,126,804 | **62.5%** | 18,807,577 |
| Yunnan | 47,209,277 | **67.0%** | 15,579,061 |
| Guizhou | 38,562,148 | **62.0%** | 14,653,616 |
| **Total** | **135,898,229** | **63.9%** | 49,040,255 |

**All three are Han-majority.** So the trade was never a Han federation against a non-Han one. It was:
**expel 86,857,974 Han to avoid absorbing 49,040,255 non-Han — 1.77 Han lost per non-Han avoided.**

**The Zhuang, specifically.** 15,721,956 people, over 90% of them in Guangxi, China's largest minority and a
real nation by any measure. But a Zhuang state in Guangxi would be **31% Zhuang and 62% Han**. Against Tibet's
TAR at 86% Tibetan or the Tarim at ~95% non-Han, Guangxi is not an ethnic territory in the same sense.

**Gansu and Ningxia were settled separately and earlier**, by the decision placing them in The Northwest
alongside Shaanxi and Qinghai — a state that then unifies into the Federation. **Hainan sits inside Min.**

### What the decision closes

- **Region 10 (Yungui) never forms.** A Yungui state would have been **64.8% Han** across 85.8 million people —
  not a non-Han polity at all. The survey's "Far West case" therefore has **no East Asian instance**, which is
  itself a finding: East Asia has frontier peoples beyond an ecological boundary, not a terrain-defined
  interior nobody could settle.
- **The Federation keeps its material base** — Gansu's nickel, Yunnan's aluminum/lead/zinc/tin, Guizhou's
  phosphate, Guangxi's tin and manganese.
- ⚠️ **The chromium gap survives the decision and still matters.** Chinese chromium was never verified, and
  **without chromium there is no stainless steel regardless of nickel.** It no longer bears on the border, but
  it bears on what the Federation can actually make. Still on the recheck list.

**What the Federation is now:** a Han federation that permanently contains ~72 million non-Han, including the
Zhuang entire and two first-order autonomous regions named for minorities it absorbed. **That is deliberate.**
A monoculture would have no internal politics; this has them built in.

---

## Suggested Prompts

**For the main nations map:**

> Draw a **political map of East Asia** showing 12 countries. This is a map of **nations with hard borders**,
> not a map of cultural zones. Use `core_territory` as solid fill in `color_hex`, `domain_territory` as the
> same color at reduced opacity, and `sphere_territory` as a dotted outline only — spheres may overlap between
> regions and that is correct, do not resolve them. Label each region with `region_name`.
>
> Leave **unshaded and labeled as out of scope**: Southeast Asia, South Asia, Central Asia, and all Russian
> territory. Leave **blank and unlabeled** three unclaimed seams: Outer Manchuria north of the Amur, Sakhalin
> and the Kurils, and Buryatia/Tuva.
>
> Draw Yunnan, Guizhou, Guangxi, Gansu, Hainan and Ningxia **solid** — they are settled Federation
> territory. **Nothing on this map is hatched.**

**For the simplified map:** same, but color by `lattimore_zone` instead — four colors, not twelve — and draw
the Great Wall / Hu Line / 400 mm isohyet as a single heavy line, because they nearly coincide.

**For the EARLY-ERA map — the fragmented century after 2083:**

> Draw a political map of East Asia **set in the generations between the 2083 war and the founding of the
> Sinian Federation**. Same base, same colors, same projection as the main nations map, with four differences:
>
> 1. **There is no Sinian Federation.** In its place draw the rows of `regions-sinitic.csv` as **sovereign
>    states with full external borders** — same weight as Korea's or Japan's. **But do not draw Mandarin as
>    one country:** replace row 13 with the three states **13A, 13B and 13C** from
>    `regions-mandarin-split.csv` (the rows marked `draw_in_three_way = YES`), and fold **13D (Jianghuai)**
>    into Wu. That gives roughly nine or ten Han states in place of the Federation.
> 2. **Mongolia and Inner Mongolia are two separate sovereign states**, both with full external borders.
> 3. **Korea is two states**, divided. Draw the division line but do not label the two halves with
>    present-day names.
> 4. **Hakka still has no territory** — keep it as scattered hatched pockets with the same "no territory"
>    label. It is the one member that was never a state.
>
> Keep the three unclaimed seams and the out-of-scope shading exactly as on the main map. **Nothing is
> hatched.** Title it as the early era and **do not put a date on it.**

**For the Sinian Federation's internal map — the LATE era, after unification:**

> Draw **one country**, the Sinian Federation, with **ten internal divisions** from `regions-sinitic.csv` —
> the way US states are drawn inside the United States. **One external border, ten internal lines.** Do not
> give the divisions separate national borders.
>
> Draw **Mandarin at its true size** — roughly two-thirds to three-quarters of the whole. Do not balance it.
> The lopsidedness is the point.
>
> Draw **Hakka as scattered hatched pockets, not a solid region** — it has no contiguous territory. If
> possible, show Skinner's nine macroregions as thin gray lines underneath, since **the mismatch between the
> two schemes is the point.**

---

## Corrections to the First Generation (2026-09-23)

All three maps are now built and verified —
`y-files/Map Files/Asia (East)/02 follow-up/`. **One outstanding item, and it is optional.**

### 1. The domain/sphere distinction was not rendered

Every region is drawn as flat `core` fill. The spec asks for `domain_territory` at reduced opacity and
`sphere_territory` as a dotted outline. **Lower priority than the Korea fix**, but it is currently impossible
to see, for example, that Manchuria's domain reaches into eastern Inner Mongolia, or that Tibet's sphere
covers Kham. With the southern border and Qinghai both settled, **there are no hatched fills left at all**.

### What was right and should not be touched

The hatch, while it existed, covered exactly the six subdivisions and stopped cleanly at the Guangdong line — it is now removed, the question having been settled as Option A. The Tian Shan is an internal dashed line inside East Turkestan, not a border.
Hainan is hatched; Taiwan is separate; Hokkaido and Okinawa are inside Japan. On the Federation map: Mandarin
is at true size, **Hakka is drawn as hatched circles labeled "no territory"**, and Huizhou and Ping are marked
as non-federal points. All of that is exactly right.

---

## Caveats

- Bounding boxes are **approximate**, derived from described geography. They are guides for placement, not
  borders to trace. `anchor_cities` is more reliable.
- ⚠️ **Region 10 (Yungui) exists only under Option C-strong.** Under the default Option A, do not draw it.
- ✅ **Region O4 (Qinghai) is SETTLED, 2026-09-23.** It joins **The Northwest (13B)** in the early era and
  passes with it into the **Sinian Federation** at unification. **Never cross-hatch it again.** It is not
  Tibetan and it is not its own region — the census settled that: Qinghai is 50.5–54% Han and only 20.7–21%
  Tibetan, and giving it to Tibet would have cut Tibet from 86.0% to 45.6% Tibetan.
- ⚠️ **Region 21 (Hakka) cannot be drawn as a territory at all.** 44 million people with no macroregion,
  occupying the seams between three provinces. This is Woodard's Greater Appalachia exactly. The author must
  choose between a non-territorial federal member and absorption into its neighbors.
- ⚠️ **Region 7 (East Turkestan) contains two countries and the rule forbids separating them.** The Tarim is
  95% non-Han; Dzungaria is Han- and Kazakh-majority. Draw the Tian Shan as an internal dashed line to show the
  problem without resolving it.
- ⚠️ **Region 19 (Min) is five languages compressed into one.** The finer resolution is recorded in the survey
  and deliberately not used for drawing — the same resolution applied to Ribeiro's five Brasis.
- The three **CONTINGENT** entries (10, 11, 12) and everything in `regions-optional.csv` are **off by default**.
  Draw them only if asked.
