# Korea springboards, cheap shape: run report (2026-11-15)

One sub-agent per nation-sign, writing the domain and every concept of that sign one sheet at a time; Korea, all twelve signs, Aries to Pisces, chained by one run agent. Scouting only: no web, no research. The prompt was Sonora's, plus a request for Korean-language terms (hangul and romanization) and for period- and region-specific pointers. This was the test of a history-rich, culturally dense nation (one culture, North, South and Jeju-do inside it).

## Per-sign table
Words are `wc -w` per file. Tokens are the sub-agent's own reported usage (the run agent's overhead is not included). Minutes are the sub-agent's reported duration.

| Sign | Sheets | Agents | Relaunches | QA problems | Avg words | Max words | Tokens | Minutes |
|---|---|---|---|---|---|---|---|---|
| 1 Aries | 11 | 1 | 0 | 0 | 769 | 794 (Anger) | 109,540 | 5.1 |
| 2 Taurus | 11 | 1 | 0 | 0 | 796 | 851 (Domain) | 114,298 | 4.9 |
| 3 Gemini | 10 | 1 | 0 | 0 | 808 | 835 (Domain) | 118,094 | 5.8 |
| 4 Cancer | 10 | 1 | 0 | 0 | 811 | 838 (Motherhood) | 118,103 | 5.0 |
| 5 Leo | 13 | 1 | 0 | 0 | 772 | 834 (Domain) | 157,380 | 9.5 |
| 6 Virgo | 10 | 1 | 0 | 0 | 824 | 848 (Usefulness) | 123,393 | 5.5 |
| 7 Libra | 11 | 1 | 0 | 0 | 715 | 756 (Projection) | 121,200 | 5.8 |
| 8 Scorpio | 11 | 1 | 0 | 0 | 816 | 858 (Domain) | 141,534 | 7.6 |
| 9 Sagittarius | 11 | 1 | 0 | 0 | 796 | 838 (Truth) | 120,839 | 5.9 |
| 10 Capricorn | 10 | 1 | 0 | 0 | 790 | 864 (Domain) | 91,860 | 4.3 |
| 11 Aquarius | 10 | 1 | 0 | 0 | 775 | 808 (Nonconformity) | 111,390 | 4.5 |
| 12 Pisces | 12 | 1 | 0 | 0 | 761 | 789 (Boundary) | 123,055 | 7.2 |
| **Total** | **130** | **12** | **0** | **0** | **785** | **864** | **1,450,686** | **about 71 (sum of runs)** |

## Totals
- 130 of 130 sheets `STATUS: done`; 12 agents; no relaunches; QA over all of Korea: 130 sheets scanned, 0 problems. No sheet over 1,000 words (longest 864); total 102,066 words, average 785 (Sonora 775, Alaska 777, Cascadia 851).
- **Tokens:** 1,450,686 from the sub-agents: about 11,200 per sheet and about 120,900 per nation-sign. That is level with Alaska (1,455,853) and about 8 percent below Sonora (1,574,929), so the richer nation cost no more. Cascadia per-concept was about 61,000 per sheet.
- **Wall-clock:** first launch 16:44, Pisces finished and checked 17:57, so about 73 minutes for the nation (Alaska 66, Sonora 61). Sub-agent runs 4.3 to 9.5 minutes (Leo longest, 13 sheets). It ran after 15:00, so the ULM was idle. The meter reading is the author's.

## Rule breaks and how fixed
- **QA flags: none** (no "Indian", no South Asian outside the "Held for review" line, no zodiac, no URL, no law outside Libra and Capricorn). Nothing needed a hand edit; I touched no sheet.
- **Process deviations, self-reported by sub-agents, not fixed:** Virgo read concepts 3 to 9 through `head -c` cutoffs of the concept block (later sections not read) and chained some `concept_block.py` calls with the previous sheet's write; Libra ran `concept_block.py` for all concepts at once in setup before the per-sheet calls; Aries dumped the whole tracker once. The sheets themselves pass QA and read as specific, so I did not relaunch them. The Virgo sheets are the ones to re-read if the author wants a strict per-concept audit.
- **Not a break but a systematic line:** Korea has no `00 - Scope.md` (the tracker names South Korea, North Korea and Jeju-do as lands carried), so most sheets carry one hedge sentence "the nation's exact lands are still to be settled" (119 of 130 sheets carry it; the 11 Libra sheets carry no hedge at all). It sits once in Flags, not in every section. A Korea scope file would remove it.
- The sheets run over the 750 target (average 785, 715 to 864), none over the cap.

## Pointers and repetition, against Sonora, Alaska and Cascadia
Recomputed for all four with one script (pointers are the rows of "Where to look first"; terms are the rows of "Search terms"; identical lines are lines of 25 or more characters in 2 or more sheets of one sign, excluding status, headings, table headers and the held-for-review line; near-identical means the same first 50 characters). The figures differ slightly from the Sonora report's own because the row normalization differs; read across, not against the old report.

| | Korea | Sonora | Alaska | Cascadia |
|---|---|---|---|---|
| Pointers per sheet | 12.5 | 12.3 | 9.4 | 10.6 |
| Search-term rows per sheet | 10.6 | 7.5 | 6.5 | 7.2 |
| Distinct pointer names (all sheets) | 1,520 | 1,517 | 1,030 | 1,294 |
| Pointer names recurring in 3 or more sheets of one sign | 1 | 0 | 27 | 1 |
| Identical lines shared between sheets of a sign | 6 | 19 | 8 | 0 |
| Of those, "Languages needed" lines | 4 | 17 | 5 | 0 |
| Near-identical lines (50-character prefix) | 39 | 56 | 113 | 70 |

- Korea's search-term section is the richest of the four (10.6 rows per sheet against 7.5 for Sonora): every one of the 130 sheets has hangul terms, usually with romanization and a gloss. Pointer count per sheet ranges from 10 to 16 (every sheet met the "10 or more" target); signs average 10.9 (Leo) to 15.1 (Scorpio), the thin end being Leo and Capricorn.
- The six shared lines: four "Languages needed" lines (Aries "Korean." in 3 sheets, Scorpio two variants in 4 and 2, Capricorn in 3), one table row (the identity term 정체성 in 2 Aries sheets) and the hedge sentence repeated word for word in all 10 Virgo sheets. No paragraph-level copying found.
- Alaska's recurring-source-pool weakness is absent: one pointer name recurs three or more times inside a sign. Across the whole nation, *Annals of the Joseon Dynasty* is named in 13 sheets, spread over different signs, which is natural for the one great source.

## Taurus, and the pilots' known weaknesses
- **Thin Taurus (Alaska's weakness): not repeated.** Korea Taurus averages 12.2 pointers per sheet (Alaska Taurus was the thinnest sign of that nation) and 796 words; the sample read (Possession) has 13 search-term rows and 12 pointers, from museum and ritual-text sources (National Folk Museum, Jujagarye, Jeju 4.3 Peace Park, Daangn Market) down to a clinical-literature row.
- **Repeated lands hedge:** present as a single Flags sentence on 119 of 130 sheets (see above), the one systematic repetition.
- **One-row Indigenous-language terms:** not applicable; Korea is one language, with Jeju-eo named as a separate language in "Languages for searching" on the sheets I read.
- **"Languages needed" boilerplate:** down to four repeated lines (Sonora had 17), and the line is concept-specific in most sheets (for example "Korean; Hanja for Joseon; English for external guides" in Libra Diplomacy).

## Where Korea reads thinner, more repetitive or less specific
Overall Korea is the strongest of the four in search terms and level with Sonora in pointers. Honest weak spots:
- **Leo (avg 10.9 pointers; four concept sheets at the 10-pointer floor: Self-expression, Being seen, Dignity, Honor)** and **Cancer (Protection, Abandonment at 10)** are the thinnest. Capricorn averages 11.1. These are still specific (the Abandonment sheet names the Truth and Reconciliation Commission adoption investigations, TRACK, Trenka, Hubinette, and a lonely-deaths survey), just fewer.
- **Libra is the shortest sign** (avg 715, Diplomacy 671 words) though its pointer count is high (13.1): rows are terse and its "Who to compare" lists are bullet fragments rather than sentences.
- **The "Who to compare" section is near-formulaic.** Jeju appears in it on 128 of 130 sheets and northern lands (North Korea, defectors) on 127. The facts are right but the ritual of always naming these two reads as a template, and the sheets give little beyond that for the *internal* southern regions (Yeongnam, Honam, Chungcheong, Gangwon and similar appear in only 31 sheets) or for the ethnic-Korean diasporas inside or beside the nation (Joseonjok, Koryo-saram, Zainichi in only 3 sheets; migrant or marriage-migrant groups in 54).
- **Hanja and Chinese-character terms are rare:** only 10 of 130 sheets have a Hanja term in the search-terms section, so the classical-Chinese vocabulary of Joseon-era texts is mostly reached through "Hanja for older texts" in the Languages line, not through searchable terms. This is the main missed use of the nation's depth in the terms.
- **A few finding-leaning phrases** were not checked row by row. I did not audit any sheet line by line, and I did not verify any name; I spot-read Taurus Possession, Cancer Abandonment and Libra Diplomacy only (real, well-known sources, each *check*-marked, no findings).

## Do the sheets exploit the nation's depth, or stay generic?
Mostly they exploit it, but unevenly. Crude keyword tallies of the 1,619 pointer rows (not an audit):
- **Classical and pre-modern pointers** (Joseon, Goryeo, Silla, the Annals, Zhu Xi and Neo-Confucian ritual, Samguk texts, Hunmin script, Donghak, sirhak, and similar) appear in the pointer rows of 67 of 130 sheets (104 rows): about half the sheets have at least one period source, and a typical hit is concept-specific (Joseon envoy missions and the Annals for Diplomacy; Jujagarye ritual manuals for Possession and the dead's belongings).
- **Modern-history pointers** (colonial period, the Korean War, Gwangju, the IMF crisis of 1997 to 98, Sewol, Jeju 4.3, Saemaul, and similar) in 48 sheets (66 rows).
- **North/South** pointers (Ministry of Unification library, KCNA Watch, defector sources, Hanawon, Wilson Center Digital Archive) in the pointer rows of 94 sheets (125 rows); **Jeju** (haenyeo, Jeju 4.3, Jeju Peace Forum, Jeju-eo) in 74 sheets (78 rows). Both are genuine, concept-matched pointers, not only mentions in the comparison list.
- **Modern scholarship and institutions** (journals, RISS, university presses, research institutes) appear in 367 rows, close to a quarter of all pointers.

So the sheets are not generic: roughly half name a period-specific source and about three quarters a regional (North or Jeju) one. The gaps are the other half of the sheets that stay on contemporary Korea (surveys, ministries, journals, press, apps), the thin treatment of southern regional differences and diasporas, and the near-absent Hanja search terms.

## Verdict
The cheap shape held on a history-rich, dense nation: about 11,200 tokens per sheet (unchanged from Alaska, below Sonora), 0 relaunches, 0 QA problems, 12.5 pointers and 10.6 search-term rows per sheet (the highest of the four nations), only six repeated lines, and no recurring-source problem. The one systematic cost is the lands hedge (a Korea scope file would remove it). If the author wants more of the depth used, the next lever is a line in the prompt asking for at least one pre-modern (classical or Joseon) pointer and one internal-region pointer (a southern province, not only Jeju and the North) per sheet, plus Hanja forms in the search terms; the structure (one agent per nation-sign) does not need to change.
