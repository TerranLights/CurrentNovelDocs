STATUS: done 2026-11-17 (run agent report; sheets not verified)

# Idelsk-Uralia springboards: run report (Day 2, deeper brief)

**Result:** 130 of 130 sheets done in all twelve signs, using 12 sub-agents (one per sign) and no relaunches. The whole-nation QA (`springboard_qa.py Idelsk-Uralia`) scanned 130 sheets and found 0 problems. No hand edits were made.

**Cost and time:** the sub-agents used **2,221,600 tokens** (sum of the twelve hand-backs), about 185,000 per sign. The run agent's own tokens are not included; the main session adds them. Wall-clock ran **05:03 to 07:42** (about 159 minutes), with each sign taking 10.7 to 15.3 minutes.

## Per sign
| # | Sign | Sheets | Relaunches | QA | Avg words (wc -w) | Longest | Pointers (avg, range) | Sub-agent tokens | Minutes |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Aries | 11/11 | 0 | 0 | 1,064 | 1,250 (Domain) | 14.4 (14-16) | 149,828 | 11.3 |
| 2 | Taurus | 11/11 | 0 | 0 | 1,133 | 1,231 (Domain) | 15.0 (15) | 197,801 | 14.6 |
| 3 | Gemini | 10/10 | 0 | 0 | 1,176 | 1,248 (Domain) | 15.7 (15-17) | 180,745 | 12.6 |
| 4 | Cancer | 10/10 | 0 | 0 | 1,085 | 1,244 (Domain) | 14.0 (14) | 180,524 | 11.7 |
| 5 | Leo | 13/13 | 0 | 0 | 1,110 | 1,239 (Domain) | 14.5 (14-16) | 195,539 | 14.8 |
| 6 | Virgo | 10/10 | 0 | 0 | 1,073 | 1,168 (Domain) | 15.0 (15) | 179,755 | 12.0 |
| 7 | Libra | 11/11 | 0 | 0 | 1,103 | 1,227 (Justice) | 14.3 (14-16) | 201,167 | 14.5 |
| 8 | Scorpio | 11/11 | 0 | 0 | 1,046 | 1,232 (Domain) | 14.1 (13-16) | 187,087 | 12.0 |
| 9 | Sagittarius | 11/11 | 0 | 0 | 1,098 | 1,248 (Domain) | 14.0 (14) | 193,823 | 14.8 |
| 10 | Capricorn | 10/10 | 0 | 0 | 1,079 | 1,245 (Domain) | 14.6 (14-15) | 171,827 | 10.7 |
| 11 | Aquarius | 10/10 | 0 | 0 | 1,012 | 1,195 (Domain) | 14.5 (14-16) | 182,912 | 11.6 |
| 12 | Pisces | 12/12 | 0 | 0 | 1,129 | 1,244 (Domain) | 15.0 (14-16) | 200,592 | 15.3 |

Across the nation, sheets average 14.6 pointers, between 13 and 17. Pointers are counted as the rows of each sheet's "Where to look first" table. No sheet went over the scan's 1,250-word limit; the Aries Domain sheet sits exactly at 1,250. Most concept sheets run 1,000 to 1,200 words, above the brief's 700-to-1,000 guide. The length rule is still undecided, so nothing was trimmed.

## Rule breaks and fixes
- **None.** No zodiac or divination wording was flagged, no "Indian", no South Asian names (129 sheets say "Held for review: none"; one gives the category line only), and no findings phrases. Every sub-agent prompt carried the Day 1 lessons: the zodiac-word ban, the missing-scope note once in Domain, a private scratch folder, and no extra length instruction.
- **Scope:** the tracker header gives the pre-war lands only as "Russia", and there is no `00 - Scope.md`. Every sub-agent wrote for the Volga-Ural (Idel-Ural) core and the Urals, and put the note that the lands are still to be settled once, in each sign's Domain sheet. **The author should settle the lands.** For example, Kirov and Kurgan oblasts are never named, Penza and Ulyanovsk barely, and Orenburg, Perm, Samara, Chelyabinsk and Sverdlovsk often. The agents' working map is a guess.
- **Kept as published:** Capricorn Merit cites Ledeneva's *Russia's Economy of Favours* under its British spelling, as published.

## Thin, repetitive or generic sheets
- **Repetition is very low.** Across all 130 sheets there are only 2 identical table rows: the Mari term вожылмаш (Taurus 03 and Leo 07), and the Tatar кеше ни әйтер (Gemini 09 and Leo 02). There is 1 identical prose line, the "Languages needed" line shared by Taurus 08 and 10.
- **Sources reused most:** Kotkin, *Magnetic Mountain* (7 sheets); Ledeneva, Kefeli, Werth and Ross, *Tatar Empire* (5 each); Ivanov's *Нарспи*, Graney, Crews and Steinwedel (4 each, counting exact pointer titles). These are the standard monographs for the region, spread across signs rather than packed into one.
- **Thinnest by length:** Aquarius 08 Detachment (946 words), 05 Idealism (958) and 07 Nonconformity (964); Capricorn 07 Merit (968); Scorpio 05 Control (972). All still carry 13 to 14 specific pointers. A read of Detachment, Control and Idealism found concrete, nation-specific items, such as the Book of Bakyrgan, Mawla Kolyy, Pülĕkh and Püryshö, the Kuibyshev reservoir floodings, Ozyorsk, Chavain and Gerd, and Krapivin's Karavella. None of them is generic.
- **Fewest pointers:** Scorpio 05 Control and 07 Revenge (13 each).
- **Self-reported soft spots:** some Mari, Udmurt, Erzya and Moksha terms in Gemini (curiosity, two-faced, gossip) are left as dictionary look-ups. Virgo dropped one Mari and one Erzya/Moksha term the agent was unsure of. About 15 term rows nation-wide are look-up-only, all in Finno-Ugric languages.

## Do the sheets exploit the nation's depth?
**Mostly yes. This is the strongest minority coverage of the nations run so far.**
- **Languages:** the search-term rows cover Russian (414 rows), Tatar (294), Bashkir (131), Chuvash (130), Udmurt (101), Mari (about 94 with meadow-Mari rows), Erzya and Moksha (about 75), Komi-Permyak (24), Kazakh (19), and Arabic and Old Tatar in Arabic script (10). Tatar-specific Cyrillic letters appear in 125 sheets, Bashkir in 106 and Chuvash in 64. Udmurt rows mostly lack their diacritic letters (only 6 sheets have them), so check Udmurt spellings first.
- **Peoples:** Tatar, Bashkir, Chuvash, Mari and Udmurt appear in all 130 sheets; Erzya in 121; Moksha in 117; Old Believers in 101; Kryashen in 95; Komi in 67; Kazakhs in 59; Mishars in 47; Germans in 31; Besermyan in 28; Jews in 13; Teptyars in 8; and Nagaybaks in 4. Ukrainians (3) and other Soviet-era settlers are thin.
- **Pre-modern pointers:** these include Ibn Fadlan's Risala (12 sheets), Volga Bulgaria and Bolgar (34), the Golden Horde (12), the Kazan Khanate (9), Kul Gali's *Qissa-i Yusuf* (9), *Ural-batyr* (11), *Idegey* (6), the Domostroy, shejere genealogies, the Pugachev rising (11) and the Book of Bakyrgan. Almost every sheet has at least one.
- **Gaps for the later research:** Komi-Permyak and Besermyan depth, the Russian-speaking Soviet settler layer (Ukrainians and others), the western fringe (Penza and Ulyanovsk) and the trans-Ural east (Kurgan), once the lands are settled.
