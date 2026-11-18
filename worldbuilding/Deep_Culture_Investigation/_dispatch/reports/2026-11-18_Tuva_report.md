STATUS: done 2026-11-18. Run agent's report; the sheets are unverified.

# Tuva: springboard run report (Day 3, deeper brief)

**Result:** 130 of 130 sheets done, every first line reads `STATUS: done 2026-11-18, not verified`. There were 12 sub-agents (one per sign) and 0 relaunches. The whole-nation QA (`springboard_qa.py Tuva`) found **0 problems** in 130 sheets. No sheet needed a hand fix.

**Tokens and wall-clock:** the sub-agents used **2,158,872 tokens** (hand-back usage, summed). The run agent's own tokens are not included; the main session adds them. The run started at 05:03 and the last sign finished at 07:32, so it took about 2 h 29 min. Signs ran one after another at 10.6 to 13.2 min each.

## Per-sign table
| # | Sign | Sheets | Agents | Relaunches | QA | Avg words | Longest | Pointers (avg, range) | Sub-agent tokens | Time |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Aries | 11/11 | 1 | 0 | 0 | 1,061 | 1,183 (Domain) | 14.6 (14-15) | 157,501 | 05:03-05:16 |
| 2 | Taurus | 11/11 | 1 | 0 | 0 | 1,080 | 1,232 (Domain) | 14.0 (14) | 183,233 | 05:16-05:29 |
| 3 | Gemini | 10/10 | 1 | 0 | 0 | 1,123 | 1,223 (Domain) | 15.0 (15) | 172,742 | 05:29-05:41 |
| 4 | Cancer | 10/10 | 1 | 0 | 0 | 1,027 | 1,244 (Domain) | 14.2 (14-16) | 175,640 | 05:41-05:52 |
| 5 | Leo | 13/13 | 1 | 0 | 0 | 1,103 | 1,215 (Domain) | 14.7 (14-15) | 188,951 | 05:52-06:05 |
| 6 | Virgo | 10/10 | 1 | 0 | 0 | 1,088 | 1,247 (Domain) | 14.3 (14-16) | 177,108 | 06:05-06:17 |
| 7 | Libra | 11/11 | 1 | 0 | 0 | 1,094 | 1,242 (Domain) | 14.1 (14-15) | 190,095 | 06:17-06:31 |
| 8 | Scorpio | 11/11 | 1 | 0 | 0 | 1,153 | 1,227 (Domain) | 14.1 (14-15) | 195,191 | 06:31-06:44 |
| 9 | Sagittarius | 11/11 | 1 | 0 | 0 | 1,058 | 1,248 (Domain) | 14.5 (14-15) | 174,838 | 06:44-06:56 |
| 10 | Capricorn | 10/10 | 1 | 0 | 0 | 1,071 | 1,239 (Domain) | 15.0 (14-16) | 176,553 | 06:56-07:08 |
| 11 | Aquarius | 10/10 | 1 | 0 | 0 | 1,142 | 1,236 (Domain) | 15.1 (14-16) | 183,261 | 07:08-07:20 |
| 12 | Pisces | 12/12 | 1 | 0 | 0 | 1,094 | 1,244 (Domain) | 14.8 (14-16) | 183,759 | 07:20-07:32 |
| | **Total** | **130** | **12** | **0** | **0** | **1,091** | **1,248** | **14.5 (14-16)** | **2,158,872** | **05:03-07:32** |

Word counts are by `wc -w`, markup included. The shortest sheet is Cancer/Protection at 964 words. No sheet is over the 1,250 scan limit. Pointers are the rows of section 2.

## Rule breaks and fixes
- **QA:** none flagged in any sign or in the whole-nation scan. No sheet uses a zodiac word, there are no South Asian items outside the Held-for-review lines, and no sheet uses "Indian".
- **Held for review:** six sheets set aside South Asian items, each as a category only (Health, Analysis, Rebirth, Sagittarius Domain, Travel, Education; these are monastic colleges, pilgrimage sites and canonical texts). This is as the rule says.
- **Law:** Libra and Capricorn carry the law. Three Aquarius sheets (Equality, Reform, Detachment) send law questions on to Libra or Capricorn.
- **Checkpoint order (Cancer):** the sub-agent made small wording fixes to Home and Family after writing their STATUS lines. Both files are complete and pass QA, so nothing was done.
- **Missing scope file:** the note appears once, in the Domain sheet of each sign, as instructed. Nothing was taken from Hermes_research, and no unit list was added to the prompts.

## Repetition
- **Within a sign:** no repeated lines in any sign, except one short "Languages needed" flag line that appears twice in Leo.
- **Across the nation:** only two flag lines repeat, each twice.
- **Source reuse is low.** The most-reused pointers appear in at most 5 of 130 sheets:
  - Mänchen-Helfen, *Reise ins asiatische Tuwa*
  - Humphrey and Sneath, *The End of Nomadism?*
  - 4 sheets each: the Tuvan heroic-tale series, Levin and Süzükei's *Where Rivers and Mountains Sing*, Toka's *Слово арата*.

## Thin, repetitive or generic sheets
- **Most query-heavy** (pointers given as a source type plus a query, not a named source):
  - Aries/Recklessness: 8 of 14
  - Gemini/Mediation and Siblings: 7 each
  - Aries/Anger: 7
  - Gemini/Gossip and Duality: 6 each
  - Aries/Competition: 6

  These are honest under the brief, because these subjects are little studied for Tuva. They read more generic than the rest, and research on them will have to start from fieldwork and interviews.
- **Self-flagged as thin data** (9 sheets): Taurus/Possessiveness, Gemini/Mediation, Gemini/Gossip, Cancer/Shelter, Libra/Indecision, Libra/Peace at any price, Sagittarius/Fundamentalism, Capricorn/Law, Aquarius/Friendship.
- **Repetitive sheets:** none found.

## Do the sheets exploit the nation's depth?
Largely yes. The counts below are sheets out of 130 that mention each item:

| Item | Sheets |
|---|---|
| The Tozhu (Todzha) Tuvans | 112 |
| Old Believers / Russian settler villages | 108 |
| Kozhuun-level pointers | 62 |
| Mongun-Taiga, the western high pastures | 42 |
| Erzin and the southern steppe | 37 |
| Soyot | 18 |
| Tere-Khol and Kungurtug | 18 |
| Old Turkic runic and Yenisei stelae pointers | 62 |
| Tibetan-script Buddhist material | 44 |
| The Uriankhai and Qing-era past | 52 |
| The Tuvan People's Republic period | 43 |
| Kenin-Lopsan's shamanic texts | 27 |
| Tsengel Tuvans (Mongolia), Kanas Tuvans (China), Dukha | 40 |

- The Tsengel, Kanas and Dukha groups are cross-border kin, so they are comparison cases, not part of the target's lands. **The author should confirm** whether they belong in "who to compare" once the lands are settled.
- Search terms are in Tuvan Cyrillic, with Russian, Mongolian and Old Turkic forms, all marked *check*.
- **Weaker spots:**
  - Khakas and other small minorities appear in only 6 sheets.
  - Throat-singing terms (хөөмей) appear in only 4 sheets. That is right for most concepts, but it means the music tradition is not overused.
  - A few concept sheets lean on the same three or four standard ethnographers (Vainshtein, Potapov, Kenin-Lopsan, Mongush), with a different work each time.

## Open items for the author
- **Lands:** the lands of Tuva are not settled. There is no `00 - Scope.md`, and the tracker header says only "Russia". The sheets are written for the Republic of Tuva's core lands.
- **Accuracy:** nothing is verified. Spot-checks of the Courage, Spirituality, Fundamentalism, Recklessness and Gossip sheets found real, well-known sources and institutions, with uncertain items given as type plus query.
