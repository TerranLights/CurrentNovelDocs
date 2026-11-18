STATUS: done 2026-11-18. Run agent's report; the sheets are unverified.

# Karachay-Cherkessia: springboard run report (Day 4, deeper brief)

**Result:** 130 of 130 sheets are done, and every first line reads `STATUS: done 2026-11-18, not verified`. The run used 12 sub-agents, one per sign, with 0 relaunches. The whole-nation QA (`springboard_qa.py Karachay-Cherkessia`) found **0 problems** in 130 sheets. One sign, Sagittarius, needed a small hand fix (see below).

**Tokens and wall-clock:** the sub-agents used **2,226,036 tokens** (the hand-back usage, summed) and 439 tool calls. This does not include the run agent's own tokens; the main session adds them. The run agent started at 09:24 and launched the first sub-agent at 09:25. The last sign finished at 12:09, and the report was written at 12:10, so the run took about 2 h 46 min. Signs ran one after another, at 12.1 to 15.7 min each. Three other nations ran in parallel.

## Per-sign table
| # | Sign | Sheets | Agents | Relaunches | QA | Avg words | Longest | Pointers (avg, range) | Sub-agent tokens | Time |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Aries | 11/11 | 1 | 0 | 0 | 1,100 | 1,234 (Domain) | 14.5 (14-16) | 156,794 | 09:25-09:38 |
| 2 | Taurus | 11/11 | 1 | 0 | 0 | 1,104 | 1,239 (Domain) | 14.1 (14-15) | 179,992 | 09:38-09:51 |
| 3 | Gemini | 10/10 | 1 | 0 | 0 | 1,054 | 1,234 (Domain) | 14.9 (14-16) | 184,615 | 09:51-10:05 |
| 4 | Cancer | 10/10 | 1 | 0 | 0 | 1,108 | 1,201 (Domain) | 14.6 (14-15) | 184,455 | 10:05-10:18 |
| 5 | Leo | 13/13 | 1 | 0 | 0 | 1,079 | 1,231 (Domain) | 14.6 (14-16) | 199,708 | 10:18-10:33 |
| 6 | Virgo | 10/10 | 1 | 0 | 0 | 1,113 | 1,231 (Domain) | 15.0 (15) | 183,905 | 10:33-10:47 |
| 7 | Libra | 11/11 | 1 | 0 | 0 | 1,148 | 1,236 (Domain) | 14.0 (14) | 209,998 | 10:47-11:03 |
| 8 | Scorpio | 11/11 | 1 | 0 | 0 | 1,088 | 1,228 (Domain) | 14.8 (14-15) | 182,306 | 11:03-11:15 |
| 9 | Sagittarius | 11/11 | 1 | 0 | 0 (1 hand fix) | 1,082 | 1,217 (Domain) | 14.8 (14-16) | 179,509 | 11:15-11:29 |
| 10 | Capricorn | 10/10 | 1 | 0 | 0 | 1,080 | 1,193 (Domain) | 15.3 (14-16) | 179,209 | 11:29-11:42 |
| 11 | Aquarius | 10/10 | 1 | 0 | 0 | 1,109 | 1,249 (Domain) | 14.4 (14-16) | 198,705 | 11:42-11:56 |
| 12 | Pisces | 12/12 | 1 | 0 | 0 | 1,103 | 1,219 (Domain) | 14.1 (14-15) | 186,840 | 11:56-12:09 |
| | **Total** | **130** | **12** | **0** | **0** | **1,098** | **1,249** | **14.6 (14-16)** | **2,226,036** | **09:25-12:09** |

- **Word counts** are by `wc -w`, markup included.
- **Shortest sheets:** Gemini/Curiosity at 986 words and Leo/Play at 988.
- **Longest sheet:** Aquarius/Domain at 1,249, one word under the scan limit. No sheet goes over 1,250.
- **Length guide:** every concept sheet runs above the brief's 700 to 1,000 guide, as on Days 2 and 3. The length rule is still the author's to decide, so nothing was trimmed.
- **Pointers** are counted as the rows of section 2.

## Rule breaks and fixes
- **QA:** nothing was flagged in any sign or in the whole-nation scan. No sheet uses a zodiac word or "Indian", and no sheet has a URL or a finding phrase.
- **Held for review:** every sheet reads "none", so no South Asian item came up.
- **Sagittarius hand fix:** the run agent's repeat check found two identical "Languages needed" lines in the sign's Flags, one pair in Meaning and Honesty and one in Education and Fundamentalism. The smallest edit fixed both: the lines in Honesty and Fundamentalism now say which language serves which pointers. I checked that these pointers are in the sheets. The re-scan found 0 repeats and QA 0 problems.
- **Missing scope file:** the note on the lands being unsettled appears once per sign, in each Domain sheet (12 of 12) and nowhere else.
- **Hermes_research:** no sheet cites it or names it. No unit list was added.
- **Law:** Libra and Capricorn carry the law. 100 sheets in other signs point law questions to Libra or Capricorn by name.
- **Published title in British spelling:** Libra/Impartiality cites *Russia's Economy of Favours*. The title is kept as published.
- **Gaps the sub-agents reported:** in Taurus most Abaza terms are marked as not known. This is an honest gap under the brief, and nothing was invented.

## Repetition
- **Within a sign:** after the Sagittarius fix, no line repeats between the sheets of any sign. The template's own lines are not counted.
- **Across the nation:** two search-term rows repeat across signs. These are single-word rows, which is acceptable:
  - Karachay-Balkar ант, "oath", in Leo/Honor and Pisces/Crime
  - Kabardian гъыбзэ, "lament song", in Scorpio/Death and Pisces/Empathy
- **Source reuse is moderate.** These italic titles appear most often, out of 130 sheets:

  | Source | Sheets |
  |---|---|
  | Khan-Girey, *Записки о Черкесии* | 9 |
  | Evliya Çelebi, *Seyahatname* | 9 |
  | Bell, *Journal of a Residence in Circassia* | 7 |
  | *Nart Sagas from the Caucasus* | 7 |
  | The republic's newspapers (*День республики*, *Черкес хэку*) | 6 each |
  | Richmond, *The Circassian Genocide* | 6 |
  | *Сборник материалов для описания местностей и племен Кавказа* (СМОМПК) | 5 |
  | Klaproth, *Reise in den Kaukasus* | 5 |
  | The Circassian etiquette and ethics books | 5 |
  | *Кавказский узел* | 5 |

  These are the standard pre-modern and regional sources, used for different questions each time.

## Thin, repetitive or generic sheets
- **Most query-heavy sheets.** Here many pointers are given as a source type plus a Russian or native query, not as a named work. The count is query pointers out of all pointers:

  | Sheet | Query pointers |
  |---|---|
  | Capricorn/Order | 12 of 16 |
  | Capricorn/Discipline | 11 of 15 |
  | Aries/Competition | 11 of 15 |
  | Aries/Recklessness | 11 of 14 |
  | Virgo/Perfectionism | 10 of 15 |
  | Capricorn/Merit | 10 of 14 |
  | Aries/Courage | 10 of 14 |
  | Virgo/Improvement | 9 of 15 |
  | Aries/Anger | 9 of 15 |
  | Sagittarius/Fundamentalism | 9 of 14 |

  A sample read of Order shows that these queries are specific, not generic. They name topics such as the 2004 seizure of the government building, джайлыкъ pasture allocation and the 1990-1992 sovereignty crisis, with Russian query strings. They follow the brief's rule to give a query rather than invent a name.
- **Self-flagged as thin (rated "thin" or "thin to mixed"):** Libra/Indecision, Virgo/Perfectionism, Taurus/Possessiveness, Gemini/Gossip, Sagittarius/Meaning, Pisces/Intuition.
- **Other data ratings:** of the concept sheets' data ratings, 38 are "rich" and about 75 "mixed".
- **Repetitive sheets:** none found after the Sagittarius fix.
- **Generic sheets:** none found in the checks run. The sheets were not read in full, so the main session's sample audit should confirm this.

## Do the sheets exploit the nation's depth?
Largely yes. The table counts sheets out of 130 that mention each item:

| Item | Sheets |
|---|---|
| Abaza | 130 |
| Nogai | 130 |
| Cossack / Russian settler villages (Zelenchuk, etc.) | 128 |
| Cherkessk | 108 |
| Karachaevsk | 74 |
| The 1943 deportation and return | 74 |
| Arkhyz / Alania (medieval) | 71 |
| Circassian diaspora (Turkey, Jordan, Syria) | 66 |
| Islam / the muftiate | 64 |
| Teberda / Dombay | 54 |
| Nart epic | 51 |
| Besleney Circassians | 35 |
| Old Turkic, runic or medieval inscriptions | 32 |
| Adyghe Khabze | 27 |
| Census pointers | 26 |
| Ossetians | 22 |
| Uchkulan / Elbrus | 19 |
| Greeks | 16 |
| The republic's university and humanities institute (КЧГУ, КЧИГИ) | 14 each |
| Khurzuk | 9 |
| The battle of Khasauka (1828) | 5 |

- **Search terms** appear throughout in Karachay-Balkar, Kabardian-Cherkess, Abaza and Nogai Cyrillic, with Russian and some Arabic and Turkish, marked *check* where unsure.
- **Pre-modern pointers** are in every sign. They include Khan-Girey, Evliya Çelebi, Klaproth, Bell, СМОМПК, the Nart epic and the medieval Alanian sites.
- **Weaker spots:**
  - Arabic-script (ajami) manuscripts appear in only 2 sheets, and Sufi orders in 4.
  - The smaller minorities appear in few sheets: Greeks in 16, Ossetians in 22, and Estonian settler villages in only 1.
  - The village level beyond the best-known names is thin. Khurzuk appears in 9 sheets and Uchkulan in 19.
  - Abaza vocabulary is often marked as unknown, so the Abaza search terms will need the Abaza-Russian dictionary first.
- **For the author:** the Circassian and Karachay diasporas in Turkey, Jordan and Syria are comparison cases, not part of the target's lands. The author should confirm whether they belong in "who to compare" once the lands are settled.
