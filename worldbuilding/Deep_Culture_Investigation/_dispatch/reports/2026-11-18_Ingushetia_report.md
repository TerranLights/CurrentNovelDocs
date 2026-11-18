# Ingushetia springboards: run report (2026-11-18, Day 4)

**Result:** all 130 sheets are marked `STATUS: done 2026-11-18, not verified`. The run used 12 sign agents and 1 single-concept relaunch. The whole-nation QA (`springboard_qa.py Ingushetia`) scanned 130 sheets and found 1 problem, a false positive (see below). No pointer has been checked; the sheets are unverified.

**Inputs:** the deeper brief, which puts accuracy and depth first, with the Day 1 to 3 lessons added to every sub-agent prompt. Those lessons are:
- no zodiac, astrolog* or horoscope words;
- the lands note once, in the Domain sheet;
- the no-reuse rule also covers the compare bullets;
- the concept is stated neutrally, never as what the culture believes or values;
- Hermes_research is never opened;
- temporary files stay in the nation's own scratchpad folder.

From Taurus on, the prompt also said to read one concept block, write that sheet, then read the next. Nothing came from a `00 - Scope.md`, a unit list or Hermes_research, and no sheet mentions Hermes. The note that the nation's lands are still to be settled appears in all 12 Domain sheets and in no concept sheet.

## Per sign
| # | Sign | Sheets | Agents | Relaunches | QA problems (fix) | Avg words | Longest | Pointers per sheet | Sub-agent tokens | Time |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Aries | 11/11 | 1 | 0 | 0 | 1,062 | 1,249 (Domain) | 14-16 | 153,489 | 09:25-09:37 |
| 2 | Taurus | 11/11 | 1 | 0 | 0 | 1,101 | 1,233 (Domain) | 15 | 182,591 | 09:38-09:51 |
| 3 | Gemini | 10/10 | 1 | 0 | 0 | 1,090 | 1,193 (Domain) | 14-15 | 166,881 | 09:51-10:02 |
| 4 | Cancer | 10/10 | 1 | 0 | 0 | 1,116 | 1,235 (Domain) | 13-15 | 175,527 | 10:03-10:14 |
| 5 | Leo | 13/13 | 1 | 0 | 0 | 1,017 | 1,224 (Domain) | 13-15 | 190,629 | 10:14-10:28 |
| 6 | Virgo | 10/10 | 1 | 0 | 0 | 1,128 | 1,240 (Domain) | 14-16 | 179,288 | 10:28-10:41 |
| 7 | Libra | 11/11 | 1 | 0 | 1 false positive (Indecision, Ingush сихо *sikho* matches "sikh"; left as is) | 1,034 | 1,226 (Domain) | 13-14 | 186,691 | 10:41-10:53 |
| 8 | Scorpio | 11/11 | 1 | 0 | 0 | 1,092 | 1,192 (Domain) | 14-16 | 183,444 | 10:54-11:06 |
| 9 | Sagittarius | 11/11 | 1 | 0 | 0 | 1,092 | 1,227 (Domain) | 14-15 | 179,445 | 11:06-11:19 |
| 10 | Capricorn | 10/10 | 2 | 1 | 1 (Domain 1,253 words; relaunched, now 1,232, clean) | 1,100 | 1,232 (Domain) | 15-16 | 170,296 + 77,694 | 11:19-11:32 |
| 11 | Aquarius | 10/10 | 1 | 0 | 0 | 1,070 | 1,224 (Domain) | 13-14 | 178,229 | 11:32-11:44 |
| 12 | Pisces | 12/12 | 1 | 0 | 0 | 1,112 | 1,232 (Domain) | 14-16 | 207,148 | 11:44-12:00 |

## Tokens and wall-clock
- **Sub-agent tokens:** 2,231,352 in all. The 12 sign agents used 2,153,658 and the Capricorn relaunch used 77,694. This is in line with Day 3 (2.30 to 2.50M per nation). The run agent's own tokens are not counted here; the main session adds them.
- **Wall-clock:** 09:25 to 12:01, about 2 h 36 min. Signs took 10.9 to 15.8 minutes each. This nation ran in parallel with Kabardino-Balkaria, Karachay-Cherkessia and North Ossetia-Alania.
- **Words:** 140,814 in all by `wc -w`, markup included. Sheets run from 943 to 1,249 words after the fix, so none is over the 1,250 scan line. Most are above the brief's 700 to 1,000 guide, which is not a rule break under the Priority block. Nothing was trimmed beyond the one QA relaunch. The length rule is still the author's to decide.

## Rule breaks and fixes
1. **Capricorn, 00 Domain was too long:** 1,253 words, 3 over the scan line. It was relaunched as a single-concept job with the problem stated. The rewrite runs 1,232 words and keeps all its pointers (16 now: the agent added one folk-calendar row). The compare bullets were rewritten, and the rescan is clean.
2. **Libra, 08 Indecision, false positive:** the Ingush term row "сихо (*sikho*), haste" matches the scan's "sikh" pattern. This is the same kind of hit as Day 3's Lezgin "sikhil" and Day 2's "Sikhote-Alin". It is a Vainakh word, marked *check*, and was left as is, not relaunched.
3. **Aries sub-agent order slip:** the agent printed concept 2's block before writing sheet 01, which breaks the one-block-at-a-time order. Sheet 01 is clean. From Taurus on, the prompt restated the order.
4. **No other breaks.** There are no zodiac words and no "Indian", not even inside a title. There is no law research outside Libra and Capricorn per the QA scan. 129 of the 130 "Held for review" lines read "none". The one that does not (Sagittarius 10 Fundamentalism) sets aside "South Asian-origin revival movements and their literature" as a category only, which the rule allows.

## Thin, repetitive or generic sheets (by name)
- **Fewest pointers (13):** Cancer 08 Abandonment, Leo 03 Pride, Libra 09 Peace at any price and 10 Projection, and Aquarius 02 Group, 04 Reform, 07 Nonconformity and 08 Detachment. Pride is the second-shortest sheet at 955 words. A spot read found it specific: the Dalgat epic, the Sozerko Malsagov memoir, teip histories, the Orstkhoy/Karabulak claim, the Prigorodny families and the kibr sermons. The two Libra sheets and Aquarius Detachment are abstract concepts, so they lean on general ethnography and the deportation literature. Read them first if any sheet is to be redone.
- **Shortest:** Leo 12 Joy (943), Leo 03 Pride (955), Libra 06 Diplomacy (971), Aquarius 08 Detachment (978) and Leo 08 Generosity (979). A spot read of Joy found it concrete. Some of its type-only rows have an empty *check* cell (for example the Eid and mawlid custom rows); these are source types, not named items.
- **Repetition inside a sign:** no table row, compare bullet or sentence repeats. The only identical lines are short "Languages needed" fact lines. One is in 2 Aries sheets; "Ingush, Russian, Arabic." is in 4 Sagittarius sheets.
- **Repetition across the nation:** there are 7 identical lines across all 130 sheets. Five are "Languages needed" lines. Two are dictionary term rows, ламаз (prayer) and бехк (blame), each in two signs. That is acceptable.
- **Most reused works:** of 1,884 pointer rows, 1,816 have distinct first cells. These titles recur most:

| Work | Sheets |
|---|---|
| Krupnov, *Средневековая Ингушетия* | 12 |
| Bazorkin, *Из тьмы веков* | 12 |
| Yakovlev, *Ингуши* | 14 |
| *Сборник сведений о кавказских горцах* | 14 |
| the newspaper *Сердало* | 17 to 19 |
| Nichols, *Ingush Grammar* | 11 |

Memorial appears in 37 sheets, CyberLeninka in 30, the 1944 deportation in 71 and the 1992 Prigorodny conflict in 55. These are standard and fitting, but they are the nearest thing to a recurring crutch.
- **Mildly formulaic compare lists:** Chechens appear in 100 of 130 compare sections, Sunzha residents in 98, Russians in 93, women in 88 and Prigorodny families in 69. The wording varies and each bullet has a concept-specific reason, but the roster is close to fixed.

## Pointers per sheet
The average is 14.5, with a range of 13 to 16: 8 sheets have 13, 63 have 14, 46 have 15 and 13 have 16. Every sheet is inside the brief's 12 to 16 band.

## Do the sheets use the nation's depth?
Mostly yes. These are counts of sheets out of 130:

| Feature | Sheets |
|---|---|
| Ingush term rows | 130 |
| Ingush Cyrillic with the palochka (Ӏ) | 84 |
| эздел (*ezdel*), the code of conduct | 19 |
| Arabic | 110 |
| Chechen material | 124 |
| Pre-modern material (see below) | 37 to 56 per marker |
| Highland gorges (Dzheyrakh, Assa, Armkhi) | 63 |
| Highland societies (Galgai, Fyappi, Tsori, Khamkhi) | 33 |
| Orstkhoy or Karabulak | 39 |
| Sunzha and Cossack material | 103 |
| Prigorodny district | 70 |
| Ossetian material | 46 |
| Kazakhstan diaspora | 61 |
| Europe diaspora | 65 |
| Turkey, Jordan or Syria diaspora | 36 |

- **Native script:** Ingush term rows are in every sheet.
- **Pre-modern pointers:** the tower complexes (Egikal, Vovnushki, Erzi and others) are in 54 sheets. The pre-Islamic religion (Tkhaba-Yerdy, Galyerdy, Dyala, Sela) is in 37. Sufi wird, Kunta-Haji and Batal-Haji are in 56. The classic ethnographers (Akhriev, Malsagov, Dalgat, Krupnov) are in 43. Georgian chronicle sources (*Kartlis Tskhovreba*, Vakhushti) and Klaproth also appear. The mehk-khel council is in 18 sheets.
- **Thin spots:** Kists and the Pankisi link are in 11 sheets, and Georgian neighbors are almost absent from the compare lists. Ossetians appear in only 12 compare sections. The Middle Eastern diaspora is lighter than the Kazakhstan and European ones. These could be strengthened when Stage 0 names the units.
- **Lands:** the lands are unsettled. There is no scope file, and the tracker header says only "Russia". The Sunzha, Prigorodny, Chechen and Cossack rows are candidates, not decided units.

## For the author
- **Length:** the question is unchanged. Most sheets run 1,000 to 1,250 words, and the Domain sheets sit at 1,190 to 1,250.
- **QA pattern:** the scan's South Asian word pattern now has three Caucasus false positives (Sikhote-Alin, sikhil, сихо/sikho). Whether to allowlist them is the author's call.
