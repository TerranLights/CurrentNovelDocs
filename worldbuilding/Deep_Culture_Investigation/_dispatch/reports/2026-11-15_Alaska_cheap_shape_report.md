# Alaska springboards, cheap shape: run report (2026-11-15)

One sub-agent per nation-sign, writing the domain and every concept of that sign one sheet at a time. Alaska, all twelve signs, Aries to Pisces, run by one run agent. Scouting only: no web, no research.

## Per-sign table
Words are `wc -w` per file. Tokens are the sub-agent's own reported usage (the run agent's own usage is not included). Time is the sub-agent's reported duration.

| Sign | Sheets | Agents | Relaunches | QA problems | Avg words | Max words | Tokens | Minutes |
|---|---|---|---|---|---|---|---|---|
| 1 Aries | 11 | 1 | 0 | 0 | 740 | 790 (Identity) | 90,740 | 3.9 |
| 2 Taurus | 11 | 1 | 0 | 0 | 660 | 763 (Domain) | 104,402 | 4.1 |
| 3 Gemini | 10 | 1 | 0 | 0 | 748 | 785 (Duality) | 131,519 | 5.1 |
| 4 Cancer | 10 | 1 | 0 | 0 | 819 | 867 (Domain) | 115,664 | 5.2 |
| 5 Leo | 13 | 1 | 0 | 1 (false positive, see below) | 839 | 951 (Domain) | 127,310 | 5.6 |
| 6 Virgo | 10 | 1 | 0 | 0 | 805 | 881 (Domain) | 130,261 | 4.7 |
| 7 Libra | 11 | 1 | 0 | 0 | 797 | 861 (Projection) | 149,151 | 4.9 |
| 8 Scorpio | 11 | 1 | 0 | 0 | 791 | 843 (Secrecy) | 117,027 | 4.8 |
| 9 Sagittarius | 11 | 1 | 0 | 0 | 756 | 786 (Travel) | 100,461 | 4.6 |
| 10 Capricorn | 10 | 1 | 0 | 0 | 832 | 905 (Domain) | 110,326 | 4.8 |
| 11 Aquarius | 10 | 1 | 0 | 0 | 811 | 905 (Domain) | 160,049 | 6.6 |
| 12 Pisces | 12 | 1 | 0 | 0 | 722 | 801 (Crime) | 118,943 | 5.3 |
| **Total** | **130** | **12** | **0** | **1 (false positive)** | **777** | **951** | **1,455,853** | **about 61** |

## Totals
- 130 of 130 sheets `STATUS: done`; 12 agents; no relaunches; no sheet over 1,000 words (longest 951, Leo Domain).
- **Tokens:** 1,455,853 from the sub-agents, about 11,200 per sheet and about 121,000 per nation-sign. The Cascadia per-concept run cost about 61,000 per sheet, so the cheap shape is about 5.4 times cheaper per sheet (about 18 percent of the cost). The run agent's own overhead is small (status, QA and log calls) and is not in the figure. The meter was not read by this agent.
- **Wall-clock:** first launch 09:14, last sign finished about 10:20 (all on 2026-11-15), so about 66 minutes for the whole nation, sub-agent runs 4 to 7 minutes each. Note this ran in the morning, not after 15:00 as the plan said, so the shared meter was not clean for a before and after reading.
- Total length 100,963 words, average 777 (Cascadia: 851 average).

## Rule breaks and how fixed
- **QA flags: one.** Leo, `00 - Domain and folkways.md`, line 29: the event's own published name, World Eskimo-Indian Olympics. A false positive. Kept as published and set in quotation marks, per the run instruction; no rewrite. The QA script still flags it on every run.
- Other "Indian" occurrences are inside published book or program titles (for example the Federal Indian Boarding School Initiative, and two books in Aquarius) and are allowlisted; QA reports 0 problems for those signs.
- No South Asian pointers outside the "Held for review" line, no zodiac pointers, no law outside Libra and Capricorn, no URLs flagged. No sheet needed a hand rewrite.
- Several agents reported sheets over the brief's 750 target (up to 951); none over the 1,000 cap.

## Honest quality comparison with Cascadia
Overall the sheets are good and specific. A spot read of Taurus Possession and Pisces Crime found real, well-known Alaska sources (Alaska Native Language Center, Sealaska Heritage Institute, Alutiiq Museum, UAA Justice Center, Dauenhauer and Dauenhauer, Fienup-Riordan, Exxon Valdez Trustee Council), all marked *check*, no findings, and good local detail (Bush order, caches, village versus road system). It is not generic filler. The differences against Cascadia:

**Thinner**
- **Taurus, all eleven sheets** (avg 660; the eight shortest sheets in the nation are all Taurus: Possession 610, Self-worth 630, Security 638, Stubbornness 642, Stability 644, Possessiveness 645, Ownership 666, Values 669). Fewer search-term rows and pointers than the Cascadia Taurus sheets, and no scholarly frames (Cascadia's Possession sheet cites Belk, Weiner, Menzel and national household surveys; Alaska's has none of these, only Alaska-specific archives and museums).
- **Scorpio concept sheets** (Purging, Betrayal, Control, Trust, Revenge, Secrecy): the lowest pointer counts in the nation (7 each).
- On average Alaska has 9.4 pointers per sheet against Cascadia's 10.6, and 6.4 search-term rows against 7.2. The language rows are fewer because Alaska's list is Native languages, Russian, Tagalog, Korean and Spanish, with less in the way of large-language vocabulary (Cascadia has Chinese, Japanese and rich Spanish slang).

**More repetitive**
- The same Alaska source pool recurs across sheets: Alaska Native Language Center dictionaries, Project Jukebox, Alaska Native Knowledge Network, Alaska Native Commission final report (1994), Fienup-Riordan, Dauenhauer, ADF&G Subsistence, ANCSA corporation reports. This is the nature of a thin-documentation nation, not copy-paste, but a reader meets the same rows often. Worst: **Capricorn** (27 sheet pairs sharing a 50-character row opening, including the *yuuyaraq* row in 8 sheets, the *Iñupiat Ilitqusiat* row in 9, and the Alaska Native Commission report in 4 to 5), **Taurus** (17), **Libra** (13), **Scorpio** (13).
- Many "Languages needed" lines are one of two or three set phrases (for example "English; Native-language dictionaries; Russian for some communities").

**Less specific / a defect**
- The first-query lists in **Aquarius** (sheets 00, 03, 04, 06, 07, 09; six sheets) and several others (11 sheets in all) begin "Read the scope file", but Alaska has no `00 - Scope.md` yet, so that step points at nothing.
- A hedge line about Canadian lands ("Canadian lands, if held", Yukon) appears in 97 of 130 sheets. The tracker header gives no territory file for Alaska ("pre-war lands carried: USA, Canada"), so each sub-agent hedged. Agents said they did not read the territory file. If the author settles Alaska's lands (does it hold Yukon?), these lines should be cleaned or confirmed. This is the one systematic cost of the cheap shape on a nation whose territory is unset.

## Identical and near-identical lines shared between sheets within a sign
Counted from the files (lines of 25 or more characters that appear in two or more sheets of one sign; "near" means the first 50 characters of a long line match).

| | Alaska | Cascadia |
|---|---|---|
| Identical lines shared (all signs, includes 3 boilerplate lines per sign: banner, two table headers) | 45 | 36 |
| Excess over boilerplate | 9 | 0 |
| Near-identical (50-character prefix) | 137 | 96 |

The 9 excess identical lines are: "Canadian lands, if held" (Aries, 7 sheets), "Languages needed" phrases (Aries x2, Taurus, Libra x2), "Read the scope file" first queries (Aquarius x2), and one table row (Capricorn, *Iñupiat Ilitqusiat*). The near-identical difference is dominated by recurring source rows, as above. No paragraph-level copying was found; sheets are written from scratch.

## Verdict for the shape decision
The cheap shape held on a thin-documentation nation: about 5 times cheaper, same QA record (0 relaunches, no rule breaks), and sheets are specific and usable. Cost: slightly fewer pointers and terms per sheet, a recurring source pool, and the territory/scope hedge. Alaska under-measures a typical nation (few units, thin documentation, little scholarship to cite), so the second pilot on a mid-size nation (Sonora or Korea) should confirm whether sheets blur when there is more to say. If they do, the middle shape (two or three concepts per agent) is the fallback. Two cheap improvements before the next nation: give the agents the territory (or a scope file) so they stop hedging, and tell them not to point first queries at a scope file that does not exist.
