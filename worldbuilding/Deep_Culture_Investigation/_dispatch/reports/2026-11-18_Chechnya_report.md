# Chechnya springboards: run report (2026-11-18, Day 3)

**Result:** 130 of 130 sheets `STATUS: done 2026-11-18, not verified`. 12 sign agents plus 1 single-concept relaunch. Whole-nation QA (`springboard_qa.py Chechnya`): 130 sheets scanned, 0 problems. The sheets are unverified. No pointer has been checked.

**Inputs:** deeper brief (accuracy and depth first), with the Day 1 and 2 lessons added to every sub-agent prompt. From Taurus onward the prompts said that the no-reuse rule covers the compare bullets, and from Cancer onward that the concept restatement must not use "the culture believes" or "the culture values" wording. No `00 - Scope.md`, no unit list and nothing from Hermes_research. Every sheet uses the brief's missing-scope rule, and the "lands still to be settled" note appears once per sign, in the Domain sheet only (12 of 12 Domain sheets, no concept sheet).

## Per sign
| # | Sign | Sheets | Agents | Relaunches | QA problems (fix) | Avg words | Longest | Pointers per sheet | Sub-agent tokens | Time |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Aries | 11/11 | 1 | 0 | 0 (run-agent repeat check: one compare bullet in 4 sheets, reworded in 3) | 1,050 | 1,248 (Domain) | 14-16 | 154,213 | 05:03-05:16 |
| 2 | Taurus | 11/11 | 1 | 0 | 0 | 1,089 | 1,226 (Domain) | 14-16 | 185,451 | 05:16-05:30 |
| 3 | Gemini | 10/10 | 2 | 1 | 1 finding-phrase in Communication's concept line (relaunched; clean) | 1,061 | 1,218 (Domain) | 14-15 | 166,468 + 80,757 | 05:31-05:44 |
| 4 | Cancer | 10/10 | 1 | 0 | 0 | 1,181 | 1,245 (Domain) | 14-16 | 200,723 | 05:44-05:58 |
| 5 | Leo | 13/13 | 1 | 0 | 0 | 1,054 | 1,229 (Domain) | 13-15 | 200,330 | 05:59-06:14 |
| 6 | Virgo | 10/10 | 1 | 0 | 0 | 1,083 | 1,236 (Domain) | 14-16 | 184,320 | 06:15-06:27 |
| 7 | Libra | 11/11 | 1 | 0 | 0 | 1,128 | 1,240 (Domain) | 13-14 | 198,214 | 06:28-06:42 |
| 8 | Scorpio | 11/11 | 1 | 0 | 0 | 1,096 | 1,242 (Domain) | 14-15 | 187,936 | 06:42-06:54 |
| 9 | Sagittarius | 11/11 | 1 | 0 | 0 | 1,144 | 1,225 (Domain) | 13-16 | 187,604 | 06:55-07:09 |
| 10 | Capricorn | 10/10 | 1 | 0 | 0 | 1,105 | 1,169 (Authority) | 14-15 | 184,479 | 07:09-07:22 |
| 11 | Aquarius | 10/10 | 1 | 0 | 0 | 1,065 | 1,221 (Domain) | 15-16 | 176,910 | 07:23-07:33 |
| 12 | Pisces | 12/12 | 1 | 0 | 0 | 1,117 | 1,243 (Domain) | 14 | 199,945 | 07:33-07:49 |

## Tokens and wall-clock
- **Sub-agent tokens: 2,307,350** (12 sign agents, 2,226,593, plus the Gemini relaunch, 80,757). This is in line with Day 2 (2.17 to 2.23M per nation). The run agent's own tokens are not counted here; the main session adds them.
- **Wall-clock:** 05:03 to 07:50 (about 2 h 47 min). Signs ran 10.7 to 15.5 minutes each.
- **Words:** 142,676 in all by `wc -w` (markup included). Sheets run from 956 to 1,248 words, so none is over the scan's 1,250 limit, and most are above the brief's 700 to 1,000 guide. Under the brief's Priority block that is not a rule break, and nothing was trimmed. The length rule is still the author's to decide.

## Rule breaks and fixes
1. **Gemini, 01 Communication:** the "Concept in one line" copied "what the culture believes good communication is" from the concept block, and QA flagged it as a finding. The sheet was relaunched as a single-concept job with the problem stated. The rewrite phrases the line as questions to research, keeps 15 pointers and runs 1,120 words, and the rescan is clean. Later prompts carried the warning, and no sign flagged again.
2. **Aries, compare bullet repeated:** the run agent's own repeat check found one "Who to compare" bullet (Kists and Akkin Chechens) word for word in 4 sheets. This was not a QA flag. The smallest edit reworded it in Independence, Anger and Recklessness, and Autonomy kept the original. Later prompts said the no-reuse rule covers the compare bullets, and no later sign repeated a line inside the sign.
3. **No other breaks.** The scan found no zodiac words, no "Indian" (no false positives either), no South Asian material and no law outside Libra or Capricorn. All 130 "Held for review" lines read "none".

## Thin, repetitive or generic sheets (by name)
- **Fewest pointers (13):** Leo 07 Humiliation (also the shortest sheet, 956 words), Libra 07 Reciprocity, 08 Indecision and 09 Peace at any price, Sagittarius 00 Domain and 10 Fundamentalism. Humiliation is short but specific: public apology videos, filtration camps, the Akkin resettlement and the Moscow migrants are all there, and it is the most sensitive sheet, rated "very high". The three Libra sheets are abstract concepts with little direct literature, so they lean on general ethnography. Read them first if any sheet is to be redone.
- **Shortest after Humiliation:** Leo 10 Play (984), Aries 06 Courage (993), Taurus 09 Stubbornness (995) and Aquarius 06 Friendship (997). A spot read of Courage found it concrete (k'onakh terms, illi singers, Dadi-Yurt 1819, Baysangur, Kunta-Haji, Vazha-Pshavela, the Heroes of the Soviet Union lists), not thin.
- **Repetition across the nation:** within a sign, no line repeats. Across all 130 sheets, the only identical lines are 4 Chechen term-table rows, each used in two signs (хийцам, совгӏат, собар, машар). That is the same dictionary word appearing for related concepts, which is acceptable. Out of 1,718 pointer rows (Aries to Aquarius), the most reused exact titles are Tishkov's *Chechnya: Life in a War-Torn Society* (7 sheets), Sadulaev's *Я — чеченец!* (6), Zelkina's *In Quest for God and Freedom* (6) and Gammer's *The Lone Wolf and the Bear* (5). These are standard works, and their reuse is modest. Memorial appears in about 32 pointer rows, and the 1944 deportation in about 43, which suits the history but is the nearest thing to a recurring crutch.
- **Mildly formulaic:** the "Who to compare" lists name Kumyks and Nogais in about 120 of 130 sheets and Russians or Terek Cossacks in about 100. The wording varies, but it is close to a fixed roster. For example, "Russians and Terek Cossack descendants" opens 8 bullets across signs.

## Pointers per sheet
Average 14.5, and the range is 13 to 16: 6 sheets have 13, 62 have 14, 52 have 15 and 10 have 16. Every sheet is inside the brief's 12 to 16 band.

## Do the sheets use the nation's depth?
On the whole, yes.
- **Native script:** Chechen Cyrillic with the palochka (Ӏ) appears in 97 sheets. Key native terms are used: нохчалла, къонахалла, ловзар, тайп/тейп, вирд, illi and illancha.
- **Second literatures:** Georgian or Kist material is in 58 sheets, and Pankisi or Kist pointers in about 70. Arabic appears for the pre-1925 written record and sermons.
- **Pre-modern pointers:** 115 of 130 sheets have at least one. Examples are the Vainakh tower complexes, the pre-Islamic Vainakh religion (Tusholi, Sela), Shamil's Imamate and the 19th-century naibs, Kunta-Haji's Qadiriyya, Dadi-Yurt (1819) and Tolstoy's Caucasus prose.
- **Internal regions:** highland districts such as Itum-Kale, Sharoy, Vedeno and Galanchozh appear in 44 sheets. The Terek and Naur-Shelkovskaya lowland strip appears in 95.
- **Minorities and diaspora:** Ingush appear in 77 sheets and Akkin or Aukh Chechens in 35. The Turkish and Jordanian diaspora appear in about 71, and the European diaspora is broadly present.
- **Thin minorities:** Avars (12 sheets), Bats or Tsova-Tush (5) and Kabardian or Circassian links (5). These could be strengthened when Stage 0 names the units.
- **Lands:** the nation's lands are unsettled. There is no scope file and the tracker header says only "Russia", so the Ingush, Kumyk, Nogai and Cossack rows are candidates, not decided units.

## For the author
- The Gemini concept-line flag was caused by the concept block's own wording ("what the culture believes"). A permanent fix would be one sentence in the brief, but that is the author's call; this run only added it to the prompts.
- The length question is unchanged: most sheets run 1,000 to 1,250 words.
