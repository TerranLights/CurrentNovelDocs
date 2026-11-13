# Asia (East)

**Status:** Confirmed — core geography, chronology, and naming settled. Per-country deep-dive files (see
`Countries/` once populated) are TBD.
**Region:** Upper Earth (non-Antarctic Earth) — East Asia
**Governing map series:** six maps, `A` through `F`, in this folder — the authoritative territorial and
chronological reference for the region across the First Interwar Period (2083–2564)
**Source project:** CurrentNovelDocs (`worldbuilding/`), migrated 2026-09-24

This file governs everything under `Asia_East/`. Per-country detail (the Sinian Federation, Unified Korea,
Mongolia, and the other polities named below) belongs in its own subfolder once written; this file is the
region-level overview and the timeline those subfolders all answer to.

---

## The six maps

| Map | Years | Event |
|---|---|---|
| `A` — Post-War Ruins and Rebuilding | 2094–2097 | The war's immediate aftermath. Nineteen sovereign polities across East Asia, none yet reunified: nine Han successor states, Qinghai (its own country), Inner Mongolia and Mongolia (separate), and a divided Korea. |
| `B` — Mongolian Unification | 2098–2110 | Inner Mongolia and Mongolia reunite — the first post-war consolidation in the region, completed in under five years once conditions allowed. Qinghai and the two Koreas remain separate. |
| `C` — Korean Unification | 2111–2130 | North and South Korea reunify. Qinghai and the nine Han states remain apart. |
| `D` — West-Sinian Consolidation | 2131–2178 | Qinghai merges into Qin — the last of the three bilateral post-war mergers. Every division in the region except the Han states' own is now resolved. |
| `E` — Full Sinian Consolidation | 2179–2266 | The nine Han states — Zhongyuan, Qin, Bashu, Jin, Wu, Gan, Xiang, Min, and Yue — federate as **the Sinian Federation**. East Asia's post-war consolidation is complete: eight sovereign powers remain (the Federation, Mongolia, Manchuria, East Turkestan, Tibet, Taiwan, Korea, and Japan). |
| `F` — Neutral Jeju-Do and the Court | 2267–present | Establishment of the International Court of Diplomacy at Jeju-Do — neutral ground shared by Korea, Japan, and the Sinian Federation, submitted by Korea under carefully negotiated stipulations. |

Every map's own header carries its year range and a one-sentence summary of the era, in-image. Full
per-decision reasoning (why each merger happened when it did, real-world precedents consulted) lives in
`Timeline_Reasoning.md` in this folder.

**The nuclear war of September 26, 2083** — already established, universe-wide, before this region's own
timeline work began — is the anchor every year above is measured from.

---

## Reconciling this region's dates with existing Timeline canon

**This needs a maintainer's attention before or alongside posting — flagging it explicitly rather than letting
it sit as a silent contradiction.**

`Reference/World_History_Reference.md` already carries entries for Unified Korea and the Sinian Federation,
with a developer ruling dated 2026-09-23 (one day before this region's dates were locked) stating both
polities formed "at an absolute minimum three generations, possibly four" before the April 27, 2318 Jeju-do
ruling, "closer to the early/mid-2200s than to 2318."

**This region's dates are earlier than that guidance anticipated, by deliberate author choice, confirmed
2026-09-24:**

- Unified Korea (`C`): **2111** — roughly 8.3 generations before 2318, not the ~3-4 the existing ruling
  described.
- The Sinian Federation (`E`): **2179** — roughly 5.6 generations before 2318, comfortably clearing the
  existing ruling's floor but landing just short of "early 2200s."

**The author's reasoning:** by the time of the Jeju-do ruling, all three powers with a stake in it — Korea,
the Sinian Federation, and Japan — should already have a well-established sense of cultural identity, rather
than reading as newly-formed countries still finding their footing. A ruling of that magnitude, made at a
neutral venue three sovereign powers agreed to respect, carries more weight coming from mature, settled
nations than from countries barely a lifetime old. The earlier dates were chosen specifically to support that.

**This does not violate the existing ruling's hard floor** (both dates clear "at least 3-4 generations before
2318" easily) — it only departs from the ruling's softer, more specific expectation of where in that window
the dates would land. **Proposed resolution:** update `World_History_Reference.md`'s Unified Korea and Sinian
Federation entries to reflect these confirmed dates in place of the "closer to the early/mid-2200s" language,
which this region's own research has now superseded with an actual confirmed date rather than an estimate. A
suggested replacement passage for each entry is in `Proposed_World_History_Reference_Updates.md` in this
folder — **not applied to the live Timeline repo by this staging pass**, per this project's standing rule that
an agent never writes to that repo without an explicit instruction naming it. Apply by hand, or explicitly
instruct an agent to apply it, when ready.

---

## Settled facts (do not relitigate)

- **The Sinian Federation is the Han core**, not the old PRC's borders. Xinjiang (East Turkestan), Tibet,
  Inner Mongolia (absorbed into Mongolia), and Manchuria are separate polities and never join the Federation.
- **The nine Han states**, in the Federation from its founding: Zhongyuan (中原, the Central Plain), Qin (秦),
  Bashu (巴蜀), Jin (晋), Wu (吴), Gan (赣), Xiang (湘), Min (闽), and Yue (粤).
- **Qinghai merges into Qin**, not Tibet and not its own region — resolves the "hatched/unassigned" status
  the existing `World_History_Reference.md` Sinian Federation entry still records as open (see below).
- **Qin keeps its name after absorbing Qinghai.** Territorial growth doesn't require a rename, matching how
  historical Chinese states (Qin, Han, Tang) expanded into the same Gansu-Qinghai frontier without renaming
  themselves.
- **Whole first-order subdivisions only** — no province, state, or prefecture is ever split by a border.
- **Jeju-do becomes a three-power condominium** (Korea, Japan, the Sinian Federation) on Map `F`, submitted by
  Korea under negotiated stipulations, home to the International Court of Diplomacy. Korean takes precedence
  in any conflict-in-translation.
- **Mongolia and Japan keep their real-world present-day names** throughout — the project's earlier
  "no present-day names" naming rule for the two Koreas was explicitly overridden on the same reasoning.
- **Every polity has a researched native-language name**, not just an English one — see `Native_Names.md` in
  this folder. Notably: "Sinian" traces to Sanskrit *Cīna* via 震旦 (Zhèndàn), a real historical Chinese term
  for China, not an invented gloss — complementary to, not a contradiction of, the existing
  `World_History_Reference.md` note that "Sinian" derives from the classical Sinae/Sino root. Unified Korea's
  native name, `한국` (Hanguk), was derived by dropping the directional prefix shared by pre-unification North
  Korea (`북한`) and South Korea (`남한`), not by picking between the two states' own self-designations.
  The Sinian Federation's own colloquial nickname, established in `World_History_Reference.md`, is
  **the Iron Federation** — not contradicted by anything here.

## Stale references in existing canon (flagged, not fixed)

- `World_History_Reference.md`'s Sinian Federation entry still cites `y-files/Map Files/Asia (East)/
  02 follow-up/asia-east-nations.png` as its supporting visual and still describes Qinghai as "drawn hatched/
  unassigned pending further research." Both are superseded by this region's finished six-map series and the
  settled Qinghai-into-Qin decision above.

## Character & Culture

Not yet established here, beyond the settled geopolitical facts above. Per this repo's own precedent
(`Worldspace/Locations/Juan_Carlos.md`), this section stays deliberately minimal rather than inventing
cultural detail — if developed later, it should build from each polity's own post-war circumstances, not be
transplanted from real-world national stereotypes.

## Open Questions

- Per-polity deep-dive files (Sinian Federation, Unified Korea, Mongolia, Manchuria, East Turkestan, Tibet,
  Taiwan) — not yet written; folders TBD under `Asia_East/`.
- The exact founding date of the International Court of Diplomacy is set at **2267** (see
  `Timeline_Reasoning.md`) — satisfies the existing ruling's "at least one full generation before the 2318
  ruling" floor exactly, no conflict there.
- Unified Korea's and the Sinian Federation's political systems, internal structure, and roles (if any) in the
  later War of Upper Earth (~2563–2564) are all still open, matching `World_History_Reference.md`'s own
  existing TBD notes.
- Whether any of these six maps' years, or this region's timeline generally, ever get referenced directly in
  a story set here — not decided.

## Canonical Appearances

- **CurrentNovelDocs** — origin. Full working package (source CSVs, the map renderer, every decision's
  provenance) at `y-files/Map Files/Asia (East)/08 follow-up - all visuals fully updated/instruction set/` in
  that project's own repo.
