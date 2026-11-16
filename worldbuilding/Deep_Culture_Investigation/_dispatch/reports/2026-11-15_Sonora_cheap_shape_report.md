# Sonora springboards, cheap shape: run report (2026-11-15)

One sub-agent per nation-sign, writing the domain and every concept of that sign one sheet at a time; Sonora, all twelve signs, Aries to Pisces, chained by one run agent. Scouting only: no web, no research. The prompt added three things to the Alaska pilot's: use the brief's missing-scope-file rule, vary the source rows between sheets, and aim for 10 or more distinct pointers per sheet.

## Per-sign table
Words are `wc -w` per file. Tokens are the sub-agent's own reported usage (the run agent's own overhead is not included). Minutes are the sub-agent's reported duration.

| Sign | Sheets | Agents | Relaunches | QA problems | Avg words | Max words | Tokens | Minutes |
|---|---|---|---|---|---|---|---|---|
| 1 Aries | 11 | 1 | 0 | 0 | 769 | 793 (Beginning) | 115,717 | 4.9 |
| 2 Taurus | 11 | 1 | 0 | 1 (real, fixed) | 823 | 881 (Domain) | 138,438 | 5.5 |
| 3 Gemini | 10 | 1 | 0 | 0 | 722 | 745 (Siblings) | 111,388 | 3.8 |
| 4 Cancer | 10 | 1 | 0 | 0 | 759 | 810 (Domain) | 104,015 | 3.8 |
| 5 Leo | 13 | 1 | 0 | 0 | 757 | 816 (Domain) | 146,954 | 4.7 |
| 6 Virgo | 10 | 1 | 0 | 2 (false positives) | 784 | 807 (Health) | 129,850 | 5.3 |
| 7 Libra | 11 | 1 | 0 | 0 | 773 | 833 (Domain) | 115,849 | 4.9 |
| 8 Scorpio | 11 | 1 | 0 | 1 (false positive) | 779 | 803 (Rebirth) | 123,477 | 4.8 |
| 9 Sagittarius | 11 | 1 | 0 | 2 (false positives) | 784 | 889 (Domain) | 167,707 | 7.9 |
| 10 Capricorn | 10 | 1 | 0 | 2 (false positives) | 792 | 839 (Domain) | 142,746 | 4.2 |
| 11 Aquarius | 10 | 1 | 0 | 0 | 791 | 831 (Hope) | 147,106 | 4.0 |
| 12 Pisces | 12 | 1 | 0 | 2 (false positives) | 765 | 809 (Surrender) | 131,682 | 5.1 |
| **Total** | **130** | **12** | **0** | **10 flagged (1 real)** | **775** | **889** | **1,574,929** | **about 59** |

## Totals
- 130 of 130 sheets `STATUS: done`; 12 agents; no relaunches; no sheet over 1,000 words (longest 889). Total 100,771 words, average 775 (Alaska 776, Cascadia 851).
- **Tokens:** 1,574,929 from the sub-agents: about 12,100 per sheet and about 131,000 per nation-sign (Alaska: 1,455,853, about 11,200 per sheet; Cascadia per-concept: about 61,000 per sheet). So Sonora cost about 8 percent more than Alaska, and about one fifth of the per-concept shape. The weekly-allotment reading is the author's (before 22%, started 15:31; the after reading is to be recorded in the checklist).
- **Wall-clock:** first launch 15:32, Pisces finished and checked 16:33, about 61 minutes for the nation (Alaska: 66). Sub-agent runs 3.8 to 7.9 minutes. It ran after 15:00 as planned, with the ULM idle.

## Rule breaks and how fixed
- **Real break, one:** Taurus, Self-worth: "2022 U.S. Interior report on Indian boarding schools" (a descriptive phrase, not the published title). Rewritten by hand to "investigative report on federal boarding schools"; QA clean after.
- **False positives, nine (still flagged by the QA script; kept as published, in quotation marks, no rewrite, per the instruction):** the historical "Phoenix Indian School" (Virgo Improvement x2, Capricorn Discipline x2, Pisces Domain x1), the "Phoenix Indian School Visitor Center" and "Steele Indian School Park" (Sagittarius Education x2), the "Gila River Indian Community" (Scorpio Power x1), and the archive's own historical search term "Indian school" (Pisces Domain, glossed as the archive's historical term). Other "Indian" occurrences are in published titles or agency names and are allowlisted (for example Underhill's *Papago Indians* in Libra, the Bureau of Indian Affairs).
- No South Asian pointers outside the "Held for review" line, no zodiac pointers, no law outside Libra and Capricorn, no URLs flagged. Eleven of the twelve Pisces sheets write "Held for review: none." in place of the category line (a minor deviation; nothing South Asian is named; not rewritten).
- One watch item: Gemini Mediation lists Mexican state alternative-justice centers (an institution pointer; borderline against the no-law rule, left in place).
- Sheets over the brief's 750 target are most of them (up to 889); none over 1,000.

## Pointers and repetition, against Alaska and Cascadia
Recomputed for all three nations with one script, so the figures are comparable (the pointer count is the rows of "Where to look first"; terms are the rows of "Search terms").

| | Sonora | Alaska | Cascadia |
|---|---|---|---|
| Pointers per sheet | 12.3 | 9.4 | 10.6 |
| Search-term rows per sheet | 7.5 | 6.5 | 7.2 |
| Distinct pointer names (all sheets) | 1,574 | 1,073 | 1,336 |
| Pointer names recurring in 3 or more sheets of one sign | 1 | 34 | 7 |
| Substantive shared identical lines (excluding status, headings, table headers, the held-for-review line) | 19 | 8 | 0 |
| Of those, "Languages needed" lines | 17 | 5 | 0 |
| Near-identical lines (same first 50 characters, long lines, same exclusions) | 47 | 112 | 70 |

- **Pointers per sheet** went up 31 percent over Alaska (the added "10 or more distinct" instruction held) and beat Cascadia's per-concept sheets.
- **Recurring source pool, the Alaska weakness, is fixed:** one pointer (Paz, *El laberinto de la soledad*, in 3 Leo sheets) against Alaska's 34 (Project Jukebox in 10 Leo sheets and 10 Aquarius sheets, the Native Language Center in 8 Aries sheets, and so on).
- **Identical lines are slightly more than Alaska's, and they are the same kind:** 17 of 19 are the "Languages needed" line (phrases such as "Spanish and English." repeated in 2 to 8 sheets of a sign; Cascadia varies the line). The other two: Aquarius's "Law: no law here; see Libra and Capricorn" line plus the lands hedge, identical in 9 sheets, and one Libra line in 2 sheets. These are low-value lines, not copied content. No paragraph-level copying found.
- **The lands hedge** ("the nation's exact lands are still to be settled; written for the Sonoran Desert core") appears in 129 of 130 sheets, once per sheet, inside the Flags or header line and worded differently across sheets, so it is rarely an identical line (Aquarius's is). It does not run through every section as Alaska's did, but it is still a sentence on every sheet; a scope file for Sonora would remove it. Alaska's report counted 97 hedge lines; the wording here is more varied, so the identical-line count stays low.

## Where the sheets read thinner, more repetitive or less specific
Overall Sonora is the strongest of the three in specificity and variety. Honest weak spots:
- **"Languages needed" lines**, as above: the most repeated line type, across all twelve signs.
- **Gemini (avg 722; Siblings 745 max, Domain about 690)** is the shortest sign and the lightest sheets; still 10 or more pointers each.
- **Indigenous-language search terms stay thin** in most sheets: usually one row ("Indigenous languages" or a single O'odham row with "ask speakers' glossaries; check") because the agent's knowledge of O'odham, Yoeme, Comcaac and Cucapá vocabulary is limited. Spanish rows carry the load. Cascadia has the same gap in its Native-language rows.
- **A few finding-leaning phrases** survive in Flags (for example Scorpio Trust: "distrust of researchers is itself a finding to respect"); minor, in notes about sensitivity, not in the pointers.
- **Taurus and Sagittarius sheets run longest** (Taurus avg 823, Sagittarius Domain 889). Not a quality problem, but the length drifts up from the 750 target.
- No sheet read as generic filler. A spot read of Taurus Possession and Scorpio Trust found real, well-known sources with *check* on each (INEGI ENVIPE, AmericasBarometer, Arizona State Museum, Saxton's O'odham dictionary, De León, Urrea, Alianza Hispano-Americana), a recognizable frame per concept, and no invented-looking names. I did not verify any name.

## Do the two cultures stay distinct?
Yes, mostly. Treating the two as the Mexican-Sonoran side and the Arizona and border-American side (with the Indigenous nations as a third strand crossing both), the sheets keep them apart in three ways. Pointers split into parallel sides: a keyword tally of "Where to look first" rows gives about 690 rows with a Mexico-side marker (INEGI, Archivo Histórico del Estado de Sonora, UNAM, UABC, Latinobarómetro) and about 687 with a U.S.-side marker (Arizona State Museum, Gallup, Pew, GSS, Morrison Institute), plus about 226 with Indigenous-nation markers; first queries often name both sides ("Pull Sonora and Arizona census tables... note the differing questions"). Search terms are Spanish (with Sonoran and border slang such as *tiliches*, *yonke*, *pollero*) and English (Arizona usage) in separate rows. "Who to compare" lists contrast border pairs (Nogales and its Arizona twin), kin-based Mexican American families against Anglo retirees and Latter-day Saint colonists, and the Indigenous nations (O'odham, Yaqui, Mayo, Comcaac, Cocopah, Apache) are named as separate units in nearly every sheet (129 of 130 sheets mention one). The risk is blur at the border: the sheets treat the border pairing as a unit, which is right for a target built from both sides, but the tally shows no sign where one side was dropped. The keyword counts are crude; no sheet was audited row by row.

## Verdict
The cheap shape held on a mid-size, two-culture nation: about 12,100 tokens per sheet, 0 relaunches, one real rule break (fixed), more pointers per sheet than Alaska or Cascadia, and a recurring-source problem that the "vary the source rows" instruction fixed. Remaining weaknesses are small and mechanical (the "Languages needed" line, the lands hedge, thin Indigenous-language rows). A Sonora scope file would remove the hedge; the "Languages needed" line could be dropped from the template or required to be concept-specific. No sign called for the middle shape.
