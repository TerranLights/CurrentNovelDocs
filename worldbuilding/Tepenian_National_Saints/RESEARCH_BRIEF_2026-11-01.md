# Research brief, 2026-11-01: second round of the saints survey

**Done 2026-11-01.** All five jobs finished. A1, A2, B and C are merged into `Historical_Figures_Survey.md` (now 110 figures), and their part files are deleted; Job D is `The_Seven_Saints_in_the_Record.md`.

The author asked for research into real historical figures directly relevant to Antarctica, as part of the basis of reference for the Tepenian national Saints. The first round (`Historical_Figures_Survey.md`, 53 figures) is done. This round covers the figures that round listed for later, the companions of the existing Saints, the founders and firsts of the station era, the namesakes of major places, the gaps the first round left, and the historical record behind the seven existing Saints.

Canon framing (DerivationMechanisms `Glossary/T.md`, "Tepenian Saints"): the civic veneration of pre-2083 Antarctic explorers as Saints who unknowingly prepared the home the exiles would later need; the honorific uses the first name. The roster is St. Robert (Scott), St. Ernest (Shackleton), St. Roald (Amundsen), St. Douglas (Mawson) and St. Richard (Byrd); city files add St. Carsten (Borchgrevink) and St. Jules (Dumont d'Urville).

## Rules for every job
- **Facts only.** No patronages, Saints' days, virtues, iconography or other assignments. That is later creative work for the author.
- **Real-world history is wanted here.** Record what the sources say; where accounts differ, give both and name the sources. Where a popular story is doubtful (a misattributed quote, an apocryphal advertisement), say so.
- **Sources:** prefer national biographies, polar institutes and heritage trusts, museums, Britannica and expedition accounts; Wikipedia is fine as a supplement. Two or three per figure, as links. No South Asian figures and no South Asian sources (the author's No Subcontinentals law).
- **Quotations:** short ones only, with their source.
- **Style:** American English, American dates ("June 6, 1868"). Plain, short sentences.
- **Tepenian place line:** check the DerivationMechanisms Glossary (`/home/kuroskalacs/Documents/Doll-Fi/media/Reference/DerivationMechanisms/Glossary/`, one file per letter) for a city or place tied to the figure. Write "none in canon found" when there is none. Do not read or write anything in the InnerTepeniaGDD or TepenianUniverseTimeline repos.
- **Write only your own output file.** No git commits.
- **Checkpoint:** the first line of the output file is `STATUS: n of N surveyed`, updated after each figure is written, so a cut-off run can resume.

## Entry format for jobs A1, A2, B and C
```
### Full Name (birth year-death year)
- **Life and origin:** birth date and place; background and training.
- **Antarctic role:** what they did there, with dates.
- **Tie to an existing Saint:** (jobs A1 and A2 only) how their journey connects to the Saint's.
- **Deeds and character in the record:** what they are remembered for, and how sources judge them.
- **What they left behind:** huts, graves, maps, stations, discoveries or methods that outlasted them.
- **Death:** date, place and cause.
- **Tepenian place:** from the Glossary check.
- **Sources:**
  - [Title](URL)
```

## Job A1: companions of St. Roald, St. Robert, St. Richard and St. Jules
Output: `_part_A1_companions.md`. 17 figures.
- **Amundsen's polar party and ship:** Olav Bjaaland, Helmer Hanssen, Sverre Hassel, Oscar Wisting, Hjalmar Johansen (dropped from the polar party), Thorvald Nilsen (captain of *Fram*).
- **The *Belgica*, Amundsen's first Antarctic voyage:** Frederick Cook, Henryk Arctowski, Emil Racoviță, Émile Danco, Carl August Wiencke.
- **Scott's *Terra Nova* expedition:** William Lashly, Edward "Teddy" Evans, Edward Atkinson (led the search party that found the tent), Tryggve Gran.
- **Byrd's South Pole flight:** Bernt Balchen, with Harold June and Ashley McKinley inside his entry.
- **Dumont d'Urville's voyage:** Charles Hector Jacquinot.

## Job A2: companions of St. Douglas, St. Carsten and St. Ernest
Output: `_part_A2_companions.md`. 14 figures.
- **Mawson:** Xavier Mertz, Belgrave Ninnis, Frank Hurley, Edgeworth David, Alistair Mackay (the last two from the 1909 South Magnetic Pole journey).
- **Borchgrevink's *Southern Cross* expedition:** Nicolai Hanson (the first person buried on the Antarctic continent), Louis Bernacchi.
- **Shackleton:** the Ross Sea party (Aeneas Mackintosh, Ernest Joyce, Arnold Spencer-Smith, Victor Hayward, Ernest Wild), Harry McNish (the *James Caird*'s carpenter), Luis Pardo (captain of the *Yelcho*).

## Job B: founders and firsts of the station era
Output: `_part_B_stations_and_firsts.md`. 17 figures.
- **Station founders and expedition leaders:** Mikhail Somov, Aleksey Treshnikov, Hernán Pujato, George Dufek, Paul-Émile Victor, Takesi Nagata, Gaston de Gerlache, John Rymill.
- **Early Argentine Antarctic figures:** José María Sobral, Julián Irízar, Hugo Alberto Acuña.
- **Firsts:** Caroline Mikkelsen (with her husband Klarius Mikkelsen inside her entry), Ingrid Christensen, Edith "Jackie" Ronne, Jennie Darlington, Gabriel González Videla (the first head of state to visit Antarctica).
- **Science and treaty:** Lloyd Berkner (the International Geophysical Year).

## Job C: place namesakes, organizers and the first round's gaps
Output: `_part_C_namesakes_and_gaps.md`. 9 figures plus the gaps.
- **Figures:** Francis Crozier, Samuel Knox, William Smith (the South Shetlands), John Davis (the American sealer of 1821), Clements Markham, Fridtjof Nansen, Macpherson Robertson, Adèle Dumont d'Urville, and Queen Maud with Princess Martha of Sweden as one short entry. For anyone who never went south, the Antarctic role line says so and gives the tie.
- **Gaps from the first round**, as a separate section "Gaps filled", one short paragraph each with sources, or "still not found":
  - John M. Rothera: later life and death.
  - David E. Bunger: life dates, origin and later career.
  - Mario Zucchelli: exact death date and cause.
  - Causes of death of Carsten Borchgrevink, Archibald McMurdo, Georg von Neumayer and Petter Sørlle.

## Job D: the seven Saints in the record
Output: `The_Seven_Saints_in_the_Record.md`. 7 figures: Scott, Shackleton, Amundsen, Mawson, Byrd, Borchgrevink, Dumont d'Urville.

The first round already has their biographies; do not repeat them. For each Saint, under `### St. <Name> (Full Name)`:
- **Their own words:** well-sourced lines from journals, letters, speeches or books, with the source; doubtful or misattributed quotes, marked as such.
- **Faith and outlook:** what the record says about their religious belief or practice, if anything.
- **Graves, memorials and sites:** graves, memorial crosses, plaques and huts, in Antarctica and elsewhere, with dates and inscriptions where recorded. Note sites at or near the places Tepenian cities stand on: Hut Point and Cape Evans (Scott), the South Pole (Amundsen Station), Cape Denison and Mawson Station (Denison, Mawson), Cape Adare, Little America and Byrd Station (Byrd), Pointe Géologie (Dumont d'Urville).
- **Objects:** surviving objects tied to them (boats, sledges, flags, huts, letters) and where they are kept.
- **Accounts beyond the ordinary:** reports such as the "fourth presence" felt on the South Georgia crossing, with who reported them and where.
- **Key dates:** a short dated list of the deeds the record treats as defining (landings, farthest-souths, the Pole, rescues, deaths).
- **How they are remembered today:** existing commemorations, anniversaries, place names, institutions and traditions (for example, the toast at Shackleton's grave), and how reputations have shifted.
- **Sources:** as links.

## Resume procedure
1. Read each output file's `STATUS` line. A job whose count is below its total is unfinished.
2. Resume the job with this brief, starting at the first figure missing from its file. Do not rewrite finished entries.
3. When all five jobs are done, merge A1, A2, B and C into `Historical_Figures_Survey.md` as new sections, update its STATUS line and its "Not yet surveyed" section, then delete the four part files. `The_Seven_Saints_in_the_Record.md` stays a file of its own.
