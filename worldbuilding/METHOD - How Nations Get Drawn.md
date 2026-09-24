# Method — How Nations Get Drawn

2026-09-23. **Reverse-engineered, not dictated.** This is my reading of how the New North America map was
produced, derived from three artifacts the author placed together: Colin Woodard's *American Nations* data,
the "Largest Ancestry by County, 2010" census map, and the author's own finished map. Written so the same
method can be applied to Latin America.

⚠️ **This is an inference and should be corrected where wrong.** I did not watch the map being made. Where I
am guessing at intent rather than observing a pattern, I say so.

---

## The Three Inputs

| Input | What it supplies | Status |
|---|---|---|
| **Woodard's *American Nations*** | The *concept* — eleven regional cultures defined by founding population, and the Doctrine of First Effective Settlement that explains why they persist | Extracted to `extractions/American_Nations_Extraction.md` |
| **"Largest Ancestry by County, 2010"** | Present-day demographic evidence at county resolution | Third-party map, `nations/latin-america-map-data/` |
| **A blank base map** | Whole states and provinces as the drawing units | `nations/latin-america-map-data/North America with tentative labels.jpg` is the finished product |

---

## The Central Tension — and What It Reveals

**Woodard's own doctrine forbids using the ancestry map the obvious way.** The extraction states it plainly:

> Whichever group is the first to establish a viable, self-perpetuating society in a given territory sets that
> territory's lasting cultural character — **regardless of how many later immigrants of other backgrounds
> arrive.** [...] This could be a genuinely small founding population, and **it will very often *not* be
> whichever group later became numerically dominant.**

So present-day ancestry is explicitly *not* the determinant. Yet the ancestry map is in the source folder.

**My reading: the ancestry map is used as corroboration, not as a border source.** Where founding culture and
present ancestry agree, a region is solid and can be drawn confidently. Where they disagree, that is a signal
to think rather than a rule to follow. The evidence supports this:

**Where the two agree, the author's regions are cleanest:**

| Region | Founding population (Woodard) | Present ancestry (census map) | Result |
|---|---|---|---|
| **Sonora** | El Norte — Hispanic borderlands | Solid **Mexican** across AZ, NM | Drawn tightly, borders obvious |
| **Alaska** | Outside Woodard's scope | Overwhelmingly **Local Native** | Extended across the whole Canadian north on the same logic |
| **The CSA** | Deep South — plantation, enslaved Africans | Solid **African American** through the Black Belt | Core is unambiguous |
| **Utah** *(inside Colorado)* | Mormon settlement | Solid **English** — the Mormon corridor | A visible block inside a larger region |

**Where they disagree, the author departed from Woodard — which is the interesting part:**

- **Midwestland.** Woodard's Midlands is a Quaker-founded corridor running the Ohio Valley. The author's
  Midwestland is the **trans-Mississippi plains** — the Dakotas, Minnesota, Nebraska, Iowa, Kansas, Missouri —
  which is exactly the solid **German and Norwegian** block on the ancestry map. *Here the author followed the
  demographic evidence over Woodard's founding-population analysis.*
- **Appalachia.** The author's version absorbs Wisconsin, Michigan, Illinois, Indiana and Ohio — the industrial
  Great Lakes belt, which is German on the ancestry map and Midlands/Yankeedom on Woodard's. Neither source
  produces this bundle on its own. *Here the author followed something else — most likely industrial and
  geographic coherence.*

---

## The Refinement — the "Settling Population" Is an Ethnic Identity, Tiered

**Stated by the author, 2026-09-23:**

> So far as "settling populations", what they would realistically be is **ethnic identities** (first grouped
> into major categories, then subdivided into more "personalized" categories).

**This names something the method was already doing.** Everything above is inference; this is not. And it
retroactively explains the ancestry map's presence in the source folder, which the section above had to reason
its way toward: *"Largest Ancestry by County"* **is an ethnic-identity map.** German, Irish, English,
Norwegian, African American, Mexican — those are not census artifacts, they are the second tier of exactly the
scheme the author describes.

### Why this is a genuine improvement, not a relabeling

**Woodard's Doctrine of First Effective Settlement only works on settler colonies.** It describes an arriving
population founding a self-perpetuating society in territory that was, from the colonizing power's point of
view, open. That is a real and specific historical situation, and it covers North America, Australia, and much
of Latin America.

**It does not survive contact with East Asia.** China, Japan and Korea have continuous civilizations millennia
old. There is no founding-settler moment to point at, no first effective settlement, no arriving group whose
institutions set the lasting character. Applied literally, the doctrine returns nothing.

**Ethnic identity is what survives the translation.** It asks the question the doctrine was really asking —
*who are these people and why do they stay distinct?* — without requiring a colonization event to answer it.
A method that works on both the Alaska Panhandle and the Tarim Basin is more useful than one that works on
only half the world.

### The two tiers, worked

| | Tier 1 — major grouping | Tier 2 — individual identity |
|---|---|---|
| **Sets** | which polity the territory belongs to | the internal divisions inside it |
| **North America** | European settler / African American / Indigenous / Hispanic | German, Irish, English, Norwegian, Mexican — the ancestry map's own labels |
| **East Asia** | Han / Turkic / Mongolic / Tibetic / Tungusic / Japonic / Koreanic | within Han: Mandarin, Wu, Yue, Min, Hakka, Xiang, Gan, Jin. Within Turkic: Uygur, Kazakh, Kyrgyz |

**Tier 1 draws the borders. Tier 2 draws what is inside them.** That is the whole of it, and it is what makes
the Sinian Federation legible: one Han polity at tier 1, eight-plus linguistic divisions under it at tier 2.
See `nations/China - Ethnolinguistic Map (read from reference).md`, which supplies both tiers directly.

### Two cautions this creates

1. **⚠️ Tier 2 routinely has more resolution than the nations layer can carry.** The China language map splits
   Min into five; Ribeiro splits Brazil into five Brasis that cut across state lines. Both exceed what a map of
   ten-to-fourteen countries can show. **Tier 2 is evidence to be compressed, not a list to be honored** — the
   same relationship rule 1 already has with county-level data.
2. **Tier 1 groupings are contestable, and the contest is usually the interesting part.** Whether Zhuang is a
   tier-1 grouping of its own or a tier-2 division inside a Han polity is precisely the open southern-border
   question for the Sinian Federation. **The method does not settle it. It makes the question askable**, which
   is what a method is for.

### The core/domain/sphere vocabulary is older than Woodard, and not his

Worth recording, because this project's map data already uses those three words as column names.
**Owen Lattimore's *Inner Asian Frontiers of China* (1940) draws the same distinction seventy-one years
earlier and independently** — his frontier/boundary analysis is core, domain and sphere under other names,
and his definition of a frontier as *"the limit of diminishing returns"* is the sharpest statement of the idea
anywhere in the corpus.

**Two consequences.** The vocabulary is not borrowed from one book and stretched over the world; it is a thing
two scholars reached separately from opposite hemispheres, which is the same independent-convergence test this
project already applied to Ribeiro/Wagley and to Lattimore/Hu. And Lattimore's **"reservoir"** — the frontier
belt as the recruiting ground of whoever rules the core — is a mechanism Woodard has no equivalent for, and it
is directly useful for any frontier polity in this setting.

---

## The Rules I Can Actually Observe

Stated in descending order of confidence.

### 1. Whole states and provinces only — never split one

**Settled as an absolute rule, 2026-09-23.** Woodard splits states constantly and by design; his whole
argument is that culture follows county lines rather than political ones. This project does not.

This is not a failure to apply the method. It is a deliberate translation: **county-level truth is the
*evidence*; state-level borders are the *output*.** A reader can hold "Missouri is Midwestland" in their head.
They cannot hold "the northern two-thirds of Missouri above a line through Boone County."

**The one historical exception, now being removed.** The original map *did* split **Washington and Oregon**
along roughly the Cascade crest, assigning the coastal halves to Cascadia and the interior halves to the
Colorado Republic. The author is redrawing to make both states wholly Cascadian.

That exception is worth recording rather than erasing, because of *where* it fell: **it was the one place
Woodard's own boundary is most famously a within-state line.** His Left Coast is a coastal ribbon never more
than a county or two deep; his Far West is the dry interior behind it, and he treats the two as culturally
opposed. So the split was not arbitrary — it followed the source at exactly the point where the source is
most insistent. Splitting states is what the method *would* do if legibility were not a constraint.

**And there is an independent argument that removing it is correct**, which comes out of the material
research rather than the cultural analysis. The **Columbia Gorge** is the only sea-level route through the
Cascades, carrying I-84, US-30, SR-14, both the UP and BNSF mainlines, and the barge channel in one 80-mile
canyon. A Cascade-crest border cuts that corridor in two, putting an international frontier through the single
most important transport chokepoint in the country — and the Columbia is also the Washington/Oregon line for
much of its length. **Whole states keep the Gorge intact and inside one nation.** See
`nations/material-base/Cascadia - Industry, Ports and Transport (supplement).md`.

The cultural observation survives the border change: Cascadia still contains two of Woodard's nations, and the
east-west seam between them is still the country's real structural weakness — the "ladder, not a chain"
finding. **The seam is now internal rather than international**, which is a more interesting problem than a
border would have been.

### 2. Regions are sized to be countries, not culture areas

Woodard has **eleven nations for the United States alone.** The author has **twelve for the whole
continent** — including Canada, Alaska, Greenland and a DMZ. The author's regions are therefore substantially
larger and fewer relative to territory.

The target appears to be roughly ten to twelve polities: enough for a varied political map, few enough to
remain legible in fiction. **This constraint does real work** — it forces merges that Woodard would not make,
and it is the reason Cascadia swallows both the Left Coast and the Far West.

### 3. Each region must be geographically coherent as a state

Every region has a physical logic a reader could describe in a sentence: a coastal strip, a high plain, a
mountain block, a river basin, a northern shield. Contiguity is absolute — no enclaves, no exclaves.

This is what overrides the sources when they conflict. Cascadia merges two culturally opposed Woodard nations
because **a Pacific coastal strip is a plausible country and a discontinuous culture area is not.**

### 4. Canada is filled in by province, on the same logic

Woodard barely covers Canada. The author extends the method rather than leaving a blank: the prairie provinces
become one polity, Quebec plus the Atlantic provinces another, the northern territories join Alaska on an
Indigenous-majority reading consistent with the ancestry map's treatment of Alaska.

### 5. Names come from the culture, not the geography

*Sonora*, *Cascadia*, *Appalachia*, *Midwestland*, *the CSA*. Several are taken from Woodard directly. None is
a compass direction or an invented word. **A name should tell the reader what kind of people live there.**

### 6. Seams get marked, not resolved

The **DMZ** is the tell. It sits on the Great Lakes/Ontario tangle, placed — per the roster's own note — with
no stated reasoning. That is precisely where Woodard's map is most contested: Michigan splits three ways, Ohio
splits three ways, and Yankeedom's two lobes are separated by the Midlands wedge running through the same
zone.

**The author drew a demilitarized zone on the most culturally incoherent ground on the continent, apparently
by instinct.** Whatever the conscious process, the judgment tracked the sources. Worth trusting on future maps.

---

## The Pattern, Compressed

1. **Read the source analysis** for where the real cultural seams are and why they persist.
2. **Cross-check against demographic evidence.** Agreement means a confident border. Disagreement means a
   decision to make, not a rule to obey.
3. **Draw whole administrative units** — states, provinces, departments. Never split one.
4. **Merge until the count is right** — roughly ten to twelve polities for a continent.
5. **Require geographic coherence.** If it would not work as a country, it is not a region.
6. **Name it after its people.**
7. **Where the ground is genuinely incoherent, mark it** — a contested zone, a DMZ, an unclaimed gap — rather
   than forcing a border through it.

---

## Applying This to Latin America

The two surveys supply step 1. The step-2 evidence is thinner and differently shaped, and that changes things:

- **There is no Latin American equivalent of the county ancestry map** in hand. The closest available
  substitutes are the Indigenous-share figures already collected (Bolivia 62%, Guatemala 43.43% nationally with
  four departments above 89%, Chile's 1.6 million Mapuche) and the Engerman & Sokoloff population-composition
  series. ⚠️ **A Latin American ancestry or ethnicity map at first-order-subdivision level would be the single
  most useful thing to obtain**, and I have not looked for one.

  **Updated 2026-09-23: this is now a gap to close, not a limitation to work around.** East Asia turned out to
  *have* its tier-2 map all along — see `nations/China - Ethnolinguistic Map (read from reference).md`, found
  sitting unreferenced in the same folder as the original ancestry map. Two of three regions now have one.
  **The Latin American gap is "not yet looked for," not "does not exist,"** and closing it would do more for
  the Latin America map than any further reading.
- **The drawing unit is the first-order subdivision** — Mexican and Brazilian *estados*, Argentine and Chilean
  *provincias* and *regiones*, Peruvian and Bolivian *departamentos*. Same rule: never split one.
- **The count should land around ten to fourteen** for everything south of Sonora, not the thirteen-plus-five
  the survey currently proposes. Some merging is expected — the survey names each region's merge candidate for
  exactly this reason.
- **Brazil is the hard case**, because Ribeiro's five Brasis deliberately cut *across* state lines — which
  collides head-on with rule 1. Either the five get rounded to state groupings, or Brazil becomes the one place
  the rule bends.

---

## Open Questions for the Author

1. **Is my reading of the ancestry map right** — corroboration rather than border-source? Or does present-day
   demography carry more weight than Woodard's doctrine allows?
2. **Midwestland followed ancestry over Woodard.** Was that deliberate, or did the German plains block simply
   look more like a country than the Ohio corridor did?
3. **What produced Appalachia's bundle** of the Irish belt plus the industrial Great Lakes? Neither source
   gives it directly.
4. **Was the DMZ placed knowingly** on Woodard's most contested ground, or independently?
5. **Is ten-to-twelve a real target**, or just where the North American map happened to land?

---

## A Housekeeping Note

`nations/latin-america-map-data/` now holds two images. **`North America with tentative labels.jpg` is the
author's own work** and belongs in the repo. **`United States county map by largest ancestry.jpg` was pulled
from the internet** and is third-party material — by the convention already applied to the Google Maps
screenshots in `reference/`, it would normally be gitignored with its content described in text instead. Both
are currently tracked. Flagged rather than changed, since they were placed there deliberately.

A **third** tier-2 map is now in use and needed no such decision: the China language map lives at
`Doll-Fi/New World/maps/`, **outside this repo entirely**, so there was never anything to track or ignore. Its
written extraction — `nations/China - Ethnolinguistic Map (read from reference).md` — is the tracked artifact,
which is the arrangement the convention is reaching for anyway. **Worth treating as the pattern for future
third-party maps:** leave the image where it sits, track the reading.
