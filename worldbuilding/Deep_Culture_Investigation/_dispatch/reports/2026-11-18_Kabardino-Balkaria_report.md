# Kabardino-Balkaria springboards: run report (2026-11-18, Day 4)

**Result:** all 130 sheets are marked `STATUS: done 2026-11-18, not verified`. The run used 12 sign agents and no relaunches. The whole-nation QA (`springboard_qa.py Kabardino-Balkaria`) scanned 130 sheets and found 0 problems. The sheets are unverified, and no pointer has been checked.

**Inputs:** the run used the deeper brief, which puts accuracy and depth first. Every sub-agent prompt carried the lessons from days 1 to 3:
- Avoid the zodiac words.
- Put the lands note in the Domain sheet only.
- Do not open Hermes_research, and add no unit list.
- The no-reuse rule covers the compare bullets.
- State each concept neutrally.
- Keep temporary files in the nation's own scratchpad subfolder.

The nation has no `00 - Scope.md` and no unit list. No sheet cites or names Hermes_research (0 hits).

## Per sign
| # | Sign | Sheets | Agents | Relaunches | QA problems (fix) | Avg words | Longest | Pointers per sheet | Sub-agent tokens | Time |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Aries | 11/11 | 1 | 0 | 0 | 1,076 | 1,228 (Domain) | 14-16 | 157,031 | 09:25-09:38 |
| 2 | Taurus | 11/11 | 1 | 0 | 0 | 1,066 | 1,226 (Domain) | 14-16 | 188,060 | 09:38-09:53 |
| 3 | Gemini | 10/10 | 1 | 0 | 0 | 1,090 | 1,182 (Domain) | 13-14 | 189,603 | 09:53-10:07 |
| 4 | Cancer | 10/10 | 1 | 0 | 0 | 1,120 | 1,239 (Domain) | 14-15 | 190,765 | 10:07-10:20 |
| 5 | Leo | 13/13 | 1 | 0 | 0 | 1,017 | 1,218 (Domain) | 13-15 | 195,452 | 10:20-10:35 |
| 6 | Virgo | 10/10 | 1 | 0 | 0 (run-agent edit to Domain, see below) | 1,108 | 1,214 (Domain; 1,204 after the edit) | 15-16 | 180,499 | 10:35-10:48 |
| 7 | Libra | 11/11 | 1 | 0 | 0 | 1,071 | 1,247 (Domain) | 14-16 | 194,068 | 10:48-11:02 |
| 8 | Scorpio | 11/11 | 1 | 0 | 0 | 1,125 | 1,234 (Domain) | 14-15 | 191,342 | 11:02-11:17 |
| 9 | Sagittarius | 11/11 | 1 | 0 | 0 | 1,135 | 1,222 (Domain) | 13-16 | 179,738 | 11:17-11:30 |
| 10 | Capricorn | 10/10 | 1 | 0 | 0 (run-agent edit to Domain, see below) | 1,132 | 1,205 (Law) | 14-15 | 192,367 | 11:30-11:44 |
| 11 | Aquarius | 10/10 | 1 | 0 | 0 | 1,075 | 1,233 (Domain) | 14-16 | 184,334 | 11:44-11:57 |
| 12 | Pisces | 12/12 | 1 | 0 | 0 | 1,074 | 1,247 (Domain) | 13-16 | 201,363 | 11:57-12:13 |

## Tokens and wall-clock
- **Sub-agent tokens: 2,244,622.** That is 12 sign agents and no relaunches. It is in line with Days 2 and 3, which ran 2.16M to 2.35M per nation. The run agent's own tokens are not counted here; the main session adds them.
- **Wall-clock:** 09:24 to about 12:16, about 2 h 52 min. Signs took 12.1 to 15.7 minutes each.
- **Words:** 141,555 in all by `wc -w`, markup included. The average is 1,089 words and the range is 947 to 1,247. No sheet is over the scan's 1,250 limit, and most are above the brief's 700 to 1,000 guide. Under the Priority block that is not a rule break, and nothing was trimmed. The length rule is still the author's to decide.

## Rule breaks and fixes
1. **The scan found no rule breaks.** It found no zodiac words, no "Indian" (and no false positives), no South Asian material and no finding phrases. All 130 "Held for review" lines read "none".
2. **A scope file is mentioned in two Domain sheets** (Virgo 00 and Capricorn 00). This was the run agent's own catch, not a QA flag. The lands flag said "no scope file exists" or "There is no scope file and no unit list yet". The brief says the reader is never to be pointed at a scope file, so the smallest edit removed those clauses and left the "lands still to be settled" note. The STATUS lines were untouched, and the rescan was clean.
3. **Law outside Libra and Capricorn:** none. A word search for law terms in the other ten signs found only:
   - kin terms such as "daughter-in-law" and "mother-in-law";
   - the NGO name Legal Initiative (Правовая инициатива), in Leo Honor and Scorpio Control;
   - the Prosecutor-General's crime-statistics portal, as data, in Sagittarius Honesty and Pisces Crime;
   - the 1944 deportees' "special settler" status, named as a term (Taurus Security);
   - deferrals to Libra.
4. **The lands note** appears exactly once per sign, in the Domain sheet, for 12 of 12 signs. It is in no concept sheet.

## Thin, repetitive or generic sheets (by name)
- **Fewest pointers (13):** Gemini 04 Curiosity, 06 Duality, 08 Mediation and 09 Gossip; Leo 07 Humiliation and 11 Honor; Sagittarius 10 Fundamentalism; Pisces 08 Surrender, 09 Intuition and 10 Crime. Gemini is the one sign where no sheet reached 15.
- **Shortest sheets:** five of the six shortest are in Leo: 08 Generosity (947), 07 Humiliation (951), 12 Joy (961), 10 Play (964) and 11 Honor (964). The sixth is Pisces 09 Intuition (973).
  - A spot read of Generosity found it concrete, not generic. It has 10 search terms in Kabardian, Karachay-Balkar and Russian. It points to Güldenstädt, Lavrov, Mambetov, the хьэщІэщ guest house, Balkar мадар work bees, funeral sadaqa, the Circassian Charity Association in Amman, aid to the Syrian repatriates, Nalchik's Mountain Jewish community and Terek Cossack помочи.
  - Leo 11 Honor (13 pointers, 964 words) is the one to re-read first, because it is the concept most central to Adyghe and Balkar ethnography.
- **Repetition within a sign:** no pointer row, sentence or compare bullet repeats. The only identical lines are bare "Languages needed" flag lines, such as "Kabardian, Karachay-Balkar, Russian." These are in Cancer (2 sheets), Scorpio (two pairs) and Pisces (4 sheets). They are language lists, not reused content, and were left as is.
- **Repetition across signs:**
  - 4 Karachay-Balkar term-table rows appear in two signs each: тукъум, ыйыкъ, тумар and башчы. Each is the same dictionary word used for a related concept, which is acceptable.
  - The most reused works are *Адыгэ псалъэ* (25 sheets by name), Evliya Çelebi's *Seyahatname* (9), Khan-Girey's *Записки о Черкесии* (9), Colarusso's *Nart Sagas from the Caucasus* (8), Kuliev's *Вершины не спят* (8), the *Сборник сведений о кавказских горцах* (8), Richmond's *The Circassian Genocide* (7) and the *СМОМПК* (7). These are standard works, and the reuse is modest.
- **Mildly formulaic:**
  - The "Who to compare" lists name Russians or Terek Cossacks (Prokhladny, Maysky) in 122 of 130 sheets. "**Russians and Terek Cossacks**" opens 16 bullets, but the reasons differ from sheet to sheet.
  - The Syrian, Jordanian and Turkish repatriates and diaspora appear in about 80 sheets.
  - This is close to a fixed roster, as Chechnya's report also found.

## Pointers per sheet
The average is 14.5 and the range is 13 to 16: 10 sheets have 13, 65 have 14, 39 have 15 and 16 have 16. Every sheet is inside the brief's 12 to 16 band.

## Do the sheets use the nation's depth?
On the whole, yes, in both titular languages.
- **Both titular peoples in every sheet:**
  - Kabardian and Karachay-Balkar search terms are in all 130 sheets.
  - Arabic is in 78, for Islamic terms and the Ajami record.
  - Turkish and diaspora Arabic appear in about 72 to 83 sheets.
- **Palochka (check item for the researcher):** Kabardian words are written with four different characters for the palochka:
  - the proper Ӏ (U+04C0) in 75 sheets;
  - the lowercase ӏ (U+04CF) in 9;
  - Cyrillic І (U+0406) in 10;
  - Latin I in 19.

  Russian-language catalogs and eLibrary often use I or 1 instead, so a researcher should try each variant when searching.
- **Pre-modern pointers:** about 123 of 130 sheets have at least one, by a pattern count. Examples:
  - the Nart epic (Нартхэр; 31 sheets name it);
  - Evliya Çelebi;
  - Interiano and other early European visitors;
  - Güldenstädt and Klaproth;
  - Khan-Girey and Shora Nogmov;
  - the 16th to 18th-century Kabarda-Russian documents;
  - the pre-Islamic Adyghe and Balkar deities and Tengri.
- **Internal regions:**
  - Elbrus and Upper Baksan, including Tyrnyauz, appear in 46 to 62 sheets.
  - Chegem appears in 40, Cherek and the Balkar gorges (Bezengi, Khulam) in 24 to 32, and Baksan in 43.
  - The Prokhladny and Maysky lowland appears in 31 to 42, and Zolsky in 15.
  - Leskensky (5) and Terek district (9) are thin.
- **Minorities and diaspora:**
  - Meskhetian Turks appear in 54 sheets, Ossetians (including Mozdok links) in 45 and Mountain Jews in 41.
  - Koreans appear in 18, Germans in 13 and Armenians in 12.
  - The Syrian, Jordanian and Turkish Circassian diasporas are broadly present.
  - The Balkar 1944 deportation appears in 52 sheets, and the 1864 expulsion or Russo-Circassian war in 23.
- **Thin minorities:** Kosovo Adyghe (4 sheets), Abkhaz and Abaza (6 and 1), Ukrainians (5), Georgians (3) and Digor or Ossetian highland links (1). Kumyks and Nogais do not appear at all, which suits the republic's lands. These could be strengthened when Stage 0 names the units.
- **Lands:** the nation's lands are unsettled. There is no scope file, and the tracker header says only "Russia". So the Cossack, Ossetian and Meskhetian rows are candidate units, not decided ones.

## For the author
- The length question is unchanged: most sheets run 1,000 to 1,250 words.
- The palochka variants are worth one line in the brief or the research RUNBOOK, if the author wants consistent Kabardian spelling.
