# Brief: identifying low-level concepts per sign (2026-10-30)

## The project
The author is building a system of **fundamental robot concepts**.
- **The starting frame:** the zodiac's twelve signs, used only as research classifiers for twelve meta-categories of human understanding. This is not astrology.
- **The eventual goal:** collect every **low-level concept**, then sort them into general categories and tag each with symbols from several systems. That sorting is NOT part of this pass.
- **What a low-level concept is:** anything at all. The author's examples are hope, joy, faith, fear, anger, justice, duty and honor.

**This pass:** read the documentation we already have for your signs, and identify **every low-level concept** it shows belongs to that sign's area of human life.
- **Research only.** No robot understanding, no proposals for the author's world. Do not sort the concepts into categories.

## Read
Base folder: `/home/kuroskalacs/Documents/Doll-Fi/media/Literature/books/CurrentNovelDocs/worldbuilding/Robot_Fundamental_Concepts/`
- **For each of your signs, read the whole notes file:** `01 - The twelve meta-categories/<NN - Sign (label)>/1 - Human understanding (research)/Notes - GDD zodiac documentation.md`. These files are 7,500 to 12,500 words; read them in full with offset-based reads.
  - Every section counts, not just section 10 ("Topics in this area"). Concepts are often named in passing: in a shadow pattern, a myth's point, or an axis.
- **If a note is unclear,** check the GDD sign file it cites (`/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Concordia-City/Districts/Zodiac_Personality_Substrate/`). Don't re-read it wholesale.

## What counts, and how to name it
- **A concept is a single idea of human life:** an emotion (fear, joy), a virtue or value (loyalty, fairness), a vice or failing (possessiveness, arrogance), a relationship or social act (betrayal, gossip, patronage), a practice or institution (marriage, contract, ritual), a state or condition (belonging, isolation, stagnation), a faculty (discernment, memory), a life event (birth, death, inheritance), and so on.
- **Name it with the plainest common English noun,** lowercase and singular where natural: `betrayal`, `self-worth`, `revenge`, `nostalgia`.
  - Use the author's own words where they fit: justice, crime, trust, care, honor, duty, hope, joy, faith, fear, anger.
  - Prefer the common name over a coined or astrological one: `stubbornness`, not "fixity".
  - **Keep the name to the concept itself.** Put this sign's angle on it in the gloss. For example, the concept is `abandonment` and the gloss says "the core fear: being left; ..."
  - Use a two-word name only when no single word carries the idea (`peace at any price`, `help nobody asked for`). Keep these rare.
- **Opposites and near-synonyms are separate concepts** when the material treats them separately (`loyalty` and `betrayal`; `pride` and `humiliation`).
- **Leave out:** body parts, colors, stones, metals, plants, tarot and chakra (correspondences, not concepts); proper names of myths or people (but do take the concept a myth illustrates); and anything that only describes astrology's mechanics (element, modality, decan as terms).
- **Be complete.** Expect roughly 50 to 120 concepts per sign. Better a long list with honest glosses than a short one.

## Output
For each sign, write `Low-level concepts (2026-10-30).md` in that sign's `1 - Human understanding (research)/` folder.

1. **First line:** `STATUS: IN PROGRESS (next: <section of the notes being read>)`, updated as you go, then `STATUS: COMPLETE`.
2. **Then:**
   - the title `# <Sign>: low-level concepts identified so far`;
   - the line "Identified 2026-10-30 from `Notes - GDD zodiac documentation.md` in this folder. Research only; not categorized; not robot understanding.";
   - a count line: "N concepts."
3. **ONE markdown table**, sorted alphabetically by concept, with exactly these columns:

   `| Concept | How this sign's material frames it | Notes § |`

   - **Concept:** the lowercase name only, with no bold or links. A script will merge all twelve tables, so the same idea must have the same spelling in every file.
   - **Gloss:** one line, at most about 25 words, in our own words.
   - **Notes §:** the section number(s) of the notes file, for example `3, 10`.
4. **After the table:** a short "Borderline" list of candidates you weren't sure count as concepts, each with a reason.

**Also update the folder's `README.md`:** add a bullet under "## Sources added" naming the new concepts file. Leave the STATUS line alone.

## Rules
- **Write only your assigned files.** Run no git commands that change anything.
- **American English.** Paraphrase in our own words, with no quotations; the repo is public.
- **Resumable:** create each file early and update its STATUS line. If you are resumed, or are a replacement agent, read your files' STATUS lines and continue; never restart a completed file.
- **Finish one sign completely before starting the next.**

## When done, reply with
- your files, with their STATUS and concept counts;
- the ten concepts per sign you judge most central to its area;
- naming choices other agents might make differently (for example, whether you used `envy` or `jealousy`), so the merge can reconcile them.
