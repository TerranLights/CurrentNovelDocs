# Worldbuilding

Universe-wide worldbuilding — **deliberately not bound to any single novel.** Every book in this line shares
one universe, so the nations, the history, and the analytical frameworks behind them live here rather than
inside whichever book happened to need them first.

If a piece of material would still be true and still be useful with a given book deleted, it belongs here.
If it only makes sense in the context of one book, it belongs in that book's own folder.

## Layout

| Folder | Contents | Git |
|---|---|---|
| `extractions/` | Our own distilled analysis of source works — currently Colin Woodard's *American Nations*: the regional-culture framework, the map descriptions, and the cross-reference against this universe's own map. | **tracked** |
| `nations/` | Per-nation reference: the world nations roster, the New North America territory definitions read from the map, the fillable nation profile template, and per-nation material-base research. | **tracked** |
| `history/` | Events and chronology that span books — the Falkland Treaty material, the world history excerpt. | **tracked** |
| `data/` | Bulk third-party datasets (USGS, FAOSTAT, EIA, Statistics Canada, INEGI, OEC and similar). Large, freely re-downloadable, not ours to redistribute. | *ignored* |
| `source-books/` | Copyrighted source texts used as reference. | *ignored* |

The split follows the same principle already used for `reference/character-methodology/`: **what we write is
tracked; what we merely downloaded is not.** Anything worth keeping from a dataset gets written up into
`extractions/` or `nations/` and tracked there.

## Start Here

- **`nations/New North America - Territory Definitions (read from map).md`** — the precise state-by-state and
  province-by-province reading of the New North America map. The single most useful entry point, since almost
  everything else depends on knowing which territory belongs to which nation.
- **`nations/World-Nations-Roster.md`** — every nation confirmed or documented so far, worldwide, with the
  running tally against the 30+ target.
- **`nations/z-template - Nation Character Profile.md`** — copy per nation and fill in.
- **`extractions/American_Nations_Extraction.md`** — the analytical method underneath all of the above.
- **`extractions/Latin America - Regional Frameworks and Colonial Origins (survey).md`** and
  **`nations/material-base/Latin America - Material and Economic Base (survey).md`** — the same two layers for
  everything south of Sonora. **No nations named yet**; these are the groundwork for deriving them.
- **`OPEN RESEARCH ITEMS - recheck list.md`** — everything that failed, could not be verified, or rests on
  something weaker than a source, consolidated from all nine nation files. **This is the list that has to
  reach zero before any of this can be promoted to the Timeline repo.** It also records which domains refuse
  requests and which research methods actually work, so a retry does not rediscover the same walls.

## This Folder Is a Staging Area, Not a Permanent Home

**Eventually all of this migrates to the `TepenianUniverseTimeline` repo** — the authoritative parent for the
entire shared universe, from which every project (novels, games, the TV series) inherits its baseline canon.
At that point the material gets reorganized into its final shape: **by country, and into timelines with actual
dates and times**, rather than the research-oriented layout it has here.

**That migration is explicitly for later.** It happens only once the worldbuilding is conclusively and
permanently settled, and settling it is expected to take a long time and a great deal of research. Until then
this folder is a working research space, and nothing in it should be treated as final.

### Why the separation exists

**Everything in `TepenianUniverseTimeline` must be perfect.** It is the authoritative parent canon that every
project in the universe — novels, games, the TV series — inherits from. A mistake there does not stay there;
it propagates into every downstream work that trusted it, and gets discovered later, embedded in finished
material. So the standard for that repo is absolute: anything in it must be thoroughly and conclusively
determined to be factually true within the Tepenian Universe. No mistakes. None.

That standard is impossible to work under while actually figuring things out. Research requires proposing,
being wrong, and revising. So the two activities are deliberately split across two places:

| | `worldbuilding/` (here) | `TepenianUniverseTimeline` |
|---|---|---|
| **Purpose** | figuring things out | recording what is settled |
| **Speculation** | expected, welcome | forbidden |
| **Uncertainty** | flagged and kept visible | must not exist |
| **Being wrong** | normal, the point of the process | unacceptable |
| **Revision** | constant | rare and deliberate |

**The consequence: promotion is a verification gate, not a file move.** Material does not graduate to the
Timeline repo by being finished-looking. It graduates by having every open question closed, every "proposed"
resolved, every unverified claim either confirmed or cut. Anything still carrying a hedge is by definition not
ready.

This is also why files here should flag uncertainty loudly rather than smoothing it over. An unflagged guess
reads as settled fact later, and settled fact is what gets promoted. **Marking what is not yet known is the
mechanism that makes the eventual promotion safe** — it is not a stylistic preference.

Practical consequences while that remains true:

- **Don't migrate piecemeal.** Material moves when the whole picture is settled, not file by file as
  individual pieces start to look finished.
- **Don't over-format for a destination that doesn't exist yet.** Optimize for research legibility now;
  the country/timeline reorganization is its own later pass.
- **Expect churn.** Borders, nation names, dates, and material assumptions are all still moving. Files here
  should say what is settled and what is not, rather than presenting everything with equal confidence.

There is precedent for how this goes: the Falkland Treaty material and the world history reference were
previously migrated out of `InnerTepeniaGDD` into `TepenianUniverseTimeline`, with pointer stubs left behind
in the original location. The same pattern applies here when the time comes.

## Related, Held Elsewhere on Purpose

- `reference/story-structure-definitions.md` — story structure, not worldbuilding.
- `reference/character-methodology/` — the character-development pipeline.
- `reference/Reference/Images/Maps/` — the map images themselves, including
  `North America with tentative labels.jpg`, which `nations/` reads from.
- The Tepenian Universe Timeline repo — canonical cross-project chronology.
