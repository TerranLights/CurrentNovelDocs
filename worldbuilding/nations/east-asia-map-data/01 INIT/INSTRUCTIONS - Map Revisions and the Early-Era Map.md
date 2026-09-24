# East Asia — Map Revisions and the New Early-Era Map

> ⚠️ **PARTLY SUPERSEDED, 2026-09-23.** Any instruction below to hatch the six southern subdivisions or
> to cross-hatch Qinghai is **out of date** — both questions are settled and **nothing on these maps is
> hatched any more.** See `UPDATE 03 - Qinghai Settled.md` and `UPDATE 04 - Southern Border Settled.md`.
> Everything else in this file still stands.

**Hand this file to the map-generating pass along with the four CSVs in this folder and `README.md`.**
It supersedes the earlier prompt set for everything it covers.

2026-09-23. Written against the first generation in
`y-files/Map Files/Asia (East)/01 initial generations/` — `asia-east-nations.png`,
`asia-east-sinian-federation.png` and `ea_nations.py`.

---

## What This Round Produces

**Three maps, not two.** The first pass was very good; keep its visual language entirely — same projection,
same palette, same typography, same legend structure, same hatching conventions.

| Map | Status | What to do |
|---|---|---|
| **A — the nations map**, post-unification / pre-Court | **built and correct** | Leave alone unless the domain/sphere note is taken up |
| **B — the Sinian Federation inside** | **built and correct** | Leave alone, same caveat |
| **C — the EARLY-ERA nations map**, the broken century | **built and correct** | Leave alone, same caveat |
| **D — the POST-COURT nations map** | **does not exist** | **Build it.** This is the new work — see Part 3 |

Maps A, C and B were built and verified in the 2026-09-23 follow-up round. **Map D is new**, and it is a small
change to Map A rather than a fresh construction.

---

## Why There Is Now an Early Era — Read This First

**Author, 2026-09-23:**

> What displays as "The Sinian Federation" was initially a smattering of multiple countries, who then unified
> into one federated country. A similar thing happened where, in the early era, there was Mongolia and Inner
> Mongolia, which later unified into simply "Mongolia" — similarly, though not identically, to how there
> became one single Korea.
>
> It just becomes the Sinian Federation some generations after the first war — the one in 2083.
>
> This means that there would be **multiple maps for the landmasses**, in order to track the progression of
> how these various landmasses developed over time.

**So East Asia is a map series.** The 2083 war fragments the region; the centuries after it are a story of
things coming back together at different speeds. At roughly 25 years to a generation, "some generations
after 2083" puts the Federation's founding somewhere in the **mid-2100s to early 2200s** — a range to work
inside, **never a date to print on the map.**

**The key consequence, and the thing most likely to be got wrong:** in the early era, **three separate
unifications have not happened yet.** China is many states, Mongolia is two states, and Korea is two states.

---

# PART 1 — Map A: One Optional Refinement

**Map A needs no correction.** Two defects reported in an earlier draft of this sheet were checked against the
rendered output pixel by pixel and **neither is real**: the Korea/Manchuria boundary follows the Yalu and Tumen
correctly, and Russia is already out-of-scope grey with only the three named seams in white. Map A does not
need regenerating.

## 1.1 Two color collisions on Map C — minor

Map C draws two pairs of regions in identical hex values, because the palettes were assigned per file and
Map C is the first map to show both files at once:

- **Jin `#E8963C` and Mongolia `#E8963C`** — separated only by Inner Mongolia's lighter orange.
- **Wu `#8E6FB8` and Korea `#8E6FB8`** — separated by the Yellow Sea.

Both read acceptably at full size because of the distance between them, so this is a refinement rather than a
defect. If corrected, shift **Jin** and **Wu** rather than Mongolia or Korea — those two are canon nations
whose colors are reused on Maps A and D, whereas Jin and Wu appear only on Map C and inside Map B.

## 1.2 The domain/sphere distinction was never rendered — lower priority

Every region is drawn as flat `core` fill. The spec asks for `domain_territory` at reduced opacity and
`sphere_territory` as a dotted outline. As it stands it is impossible to see that Manchuria's domain reaches
into eastern Inner Mongolia, or that Tibet's sphere covers Kham. **Optional this round**, but if taken up,
apply it to Map C as well.

## 1.4 What was right — do not touch

The hatch covers exactly the six undecided subdivisions and **stops cleanly at the Guangdong line**. The Tian Shan is an internal dashed line inside East Turkestan, not a border.
Hainan is hatched; Taiwan is separate; Hokkaido and Okinawa sit inside Japan. On Map B: Mandarin is at true
size, **Hakka is drawn as hatched circles labeled "no territory,"** and Huizhou and Ping are marked as
non-federal points. All of that is exactly right and should carry over unchanged.

---

# PART 2 — Map C: The Early-Era Nations Map

**Title it as the early era. Put no date on it.**

Build it from Map A's code and styling. Same projection, same extent, same legend layout, same fonts, same
hatch conventions, same city set. **Four things change.**

## 2.1 There is no Sinian Federation — draw nine Han states

Replace the single cyan Federation with the following. **Sources: `regions-mandarin-split.csv` for 13A–13C,
`regions-sinitic.csv` for the rest.** All get full external borders at the same weight as Korea's or Japan's.

| # | State | Provinces (whole, no splitting) | Color |
|---|---|---|---|
| 13A | **The North China Plain** | Beijing, Tianjin, Hebei, Shandong, Henan | `#4FC3D9` |
| 13B | **The Northwest** | Shaanxi, **Gansu**, **Ningxia** | `#2E8CA8` |
| 13C | **Bashu** | Sichuan, Chongqing, Hubei, **Yunnan**, **Guizhou** | `#7FD8E8` |
| 14 | **Jin** | Shanxi | `#E8963C` |
| 15 | **Wu** | Shanghai, Zhejiang, **Jiangsu, Anhui** | `#8E6FB8` |
| 16 | **Gan** | Jiangxi | `#5B8DD6` |
| 17 | **Xiang** | Hunan | `#9AA5B1` |
| 19 | **Min** | Fujian, **Hainan** | `#D4A017` |
| 20 | **Yue** | Guangdong, **Guangxi** | `#E8B44F` |

Plus **Hong Kong and Macau** inside Yue, as on Map A.

**Three notes on that table:**

- **Jiangsu and Anhui go to Wu.** They are Jianghuai — Mandarin-speaking ground that Skinner places in the
  same macroregion as Wu. `regions-mandarin-split.csv` carries them as an optional fourth Mandarin state
  (13D); **the recommendation is to fold them into Wu**, and that is what this table does. If the author
  later wants 13D drawn separately, it is ready.
- **The three Mandarin successors are deliberately one color family.** Cyan shades, so a reader sees at a
  glance that they were one thing and will be again. Every other state gets its own distinct hue.
- **The six undecided subdivisions are still hatched**, exactly as on Map A — now distributed across four
  different states (Gansu and Ningxia in 13B; Yunnan and Guizhou in 13C; Guangxi in Yue; Hainan in Min). The
  hatch travels with the province, not with the nation.

## 2.2 Hakka still has no territory

Keep it exactly as Map B drew it: **scattered hatched circles** in the Guangdong–Fujian–Jiangxi borderlands,
labeled **"Hakka (no territory)"**, with the same legend entry. **It is the one nation that was never a
state in either era** — it has no ground to be sovereign over. Do not give it a border.

## 2.3 Mongolia has not unified — draw two Mongol states

**Mongolia** (region 5) and **Inner Mongolia** (region 6) are **two separate sovereign states**, each with a
full external border at the same weight as every other nation. Keep their existing colors — `#E8963C` and
`#F0B860` — which are deliberately close, so the reader can see they belong together before they are together.

**This is a timeline event, not a merge candidate.** Region 6's `merge_candidate` field says "5 or 4"; on this
map ignore that and draw it as its own country.

## 2.4 Korea has not unified — draw two Korean states

Draw the peninsula as **two states divided on the present-day line**, both in the Korean purple `#8E6FB8`,
separated by a full international border.

⚠️ **Label them neutrally** — "Northern Korea" and "Southern Korea," or leave them unlabeled with a single
bracketed "Korea (divided)" annotation. **Do not use present-day state names.** The author's note was that
Korea *probably* had not unified yet, so this is the working assumption and not settled canon.

## 2.5 What stays identical to Map A

Change nothing else. Specifically, all of these carry over exactly:

- **Manchuria, East Turkestan, Tibet, Taiwan** — same borders, same colors, same labels.
- **Japan** — unchanged, including Hokkaido and Okinawa inside it.
- **Qinghai** — settled Federation territory, drawn solid. No cross-hatch.
- **The Tian Shan** — internal dashed line inside East Turkestan.
- **The three unclaimed seams** — Outer Manchuria, Sakhalin/the Kurils, Buryatia/Tuva, in white.
- **Out of scope** — Southeast, South and Central Asia, and Russia, in grey.
- The legend's structure, the graticule, the city dots, and the footer note.

---

# PART 3 — Map D: After the Court

**This is Map A with one island recolored.** Copy Map A exactly — same projection, same borders, same palette,
same legend, same cities — and make the single change below.

## 3.1 The canon

**Author, 2026-09-23:** upon the founding and establishment of the **International Court of Diplomacy at
Jeju-do**, Korea delegated Jeju-do as **neutral ground, to be legally shared among itself, Japan, and the
Sinian Federation.**

A stipulation of that arrangement: **Korean, Japanese and Mandarin are equally valid before the Law**, but
**where a conflict-in-translation arises, the Korean text takes precedence** — the role English plays in
present-day international instruments.

## 3.2 The change

**Draw Jeju-do in its own color, distinct from all three of its parents** — Korea's purple `#8E6FB8`, Japan's
rose `#D4527D`, and the Sinian cyan `#3FA9C9`. Use **`#F5C518` (bright gold)**, and give the island a
**magnified inset** — it renders at only ~13 × 8 px, so color alone cannot carry it. See
`UPDATE 02 - Jeju-do Legibility.md` for the full specification.

Give it its own legend entry, below the nations block and above the hatching block:

> **Jeju-do — neutral ground**
> *International Court of Diplomacy · shared by Korea, Japan and the Sinian Federation*

**The whole-subdivision rule is not broken by this.** Jeju is **Jeju Special Self-Governing Province**, a
first-order subdivision of Korea, so drawing it out is legal under the same rule that forbids splitting
Xinjiang. Source row: **`2J`** in `regions-main.csv`.

## 3.3 Why Map A stays as it is

The two maps are both correct, for different moments:

| | Korea | The Federation | The Court | Jeju |
|---|---|---|---|---|
| **Map C** | two states | does not exist | — | ordinary Korean ground, inside the southern state |
| **Map A** | unified | exists | not yet founded | ordinary Korean ground |
| **Map D** | unified | exists | founded | **neutral, shared three ways** |

**There is a real window between A and D**, and it is roughly two generations wide. Korea's reunification and
the Federation's founding both happened **at least three and possibly four generations before** the Court's
April 27, 2318 ruling; the Court itself was already established **at least one full generation before** that
ruling. So the unified map is correct for a meaningful stretch during which Jeju is still simply Korean.

⚠️ **Put no dates on either map.** The bounds above explain why two maps exist; they are not captions.

## 3.4 Suggested caption for Map D

> **ASIA (EAST) — the Court years**
> *After the founding of the International Court of Diplomacy at Jeju-do*
>
> Jeju-do is neutral ground, submitted by Korea and legally shared with Japan and the Sinian Federation.
> Whole first-order subdivisions only. Hatching marks an undecided border. No dates are implied.

---

# PART 4 — Constraints That Never Change

1. **Whole first-order subdivisions only.** Never split a province, autonomous region or municipality.
2. **Russia is deferred.** Three seams are blank and unclaimed — not Russian, not anyone's.
3. **Scope is East Asia only.** Southeast, South, Central Asia and the Middle East stay unshaded and labeled
   out of scope.
4. **Option A is the default southern border**, with the six subdivisions hatched to show the question is
   open. Do not silently resolve it.
5. **These are nations maps.** Every region has a hard external boundary. `sphere_territory` is the only thing
   permitted to overlap or fade.

---

# PART 5 — Do Not Invent These

Flag them on the map only as described; otherwise leave them alone.

- **No dates.** Not for the Federation's founding, not for the Mongol or Korean unifications. The only anchor
  is "some generations after 2083," and it stays off the map.
- **The order of the three unifications is unknown.** Do not imply a sequence.
- **Manchuria, East Turkestan, Tibet and Taiwan have no established early-era status.** They are drawn as on
  Map A because that is the only information available — not because it is settled. Do not add or remove them.
- **Whether any of those four later joined the Federation is open.**
- **Shandong (Qilu) may belong outside 13A** as a fourth northern state; the cuisine evidence would support it.
  Not drawn that way here. Do not act on it unless the author asks.
- **Japan** — no Japanese fragmentation has been indicated, so it is unchanged in both eras.

---

# PART 6 — A Suggested Caption for Map C

> **ASIA (EAST) — the broken century**
> *After the war of 2083, before the Federation*
>
> China is nine states. Mongolia is two. Korea is two. Whole first-order subdivisions only; dashed lines
> inside a nation mark unresolved seams, not borders. Hatching marks an undecided border. No dates are
> implied.
