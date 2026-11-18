STATUS: done 2026-11-18, sheets not verified

# Siberia: springboard run report (2026-11-18, Day 3, deeper brief)

**Target:** Siberia (#56), `Targets/Russia/Siberia/`. The tracker header lists only "Russia" as pre-war land. There is no `00 - Scope.md` and no unit list from the author, so the brief's missing-scope rule applied. Each Domain sheet says once that the exact lands are still to be settled (the Urals edge, Yamal and Yugra, the line with the Far East) and writes for the core lands from the Urals to Transbaikalia. No other sheet mentions a scope file, and none cites Hermes_research.
**Shape:** one sub-agent per nation-sign under the deeper brief (Priority block). The Day 1 and 2 lessons went into each prompt: no zodiac, astrolog* or horoscope words; the missing-scope note once, in Domain; nothing taken from Hermes_research. No length instruction was added.
**Result:** 130 of 130 sheets done, 12 sign agents, 0 relaunches. Whole-nation QA: **130 sheets scanned, 0 problems.** Every first line reads `STATUS: done 2026-11-18, not verified`.

## Per-sign table
| # | Sign | Sheets | Agents | Relaunches | QA | Avg words | Longest | Pointers per sheet | Sub-agent tokens | Tool uses | Time |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Aries | 11 | 1 | 0 | 0 | 1,067 | 1,246 (Domain) | 13-15 | 158,455 | 36 | 05:03-05:16 |
| 2 | Taurus | 11 | 1 | 0 | 0 | 1,058 | 1,198 (Domain) | 14-16 | 184,835 | 33 | 05:16-05:30 |
| 3 | Gemini | 10 | 1 | 0 | 0 (2 repeats fixed by hand) | 1,158 | 1,246 (Domain) | 15-16 | 170,618 | 33 | 05:30-05:41 |
| 4 | Cancer | 10 | 1 | 0 | 0 | 1,114 | 1,229 (Domain) | 14 | 178,979 | 30 | 05:41-05:53 |
| 5 | Leo | 13 | 1 | 0 | 0 | 1,051 | 1,233 (Domain) | 14-15 | 191,053 | 34 | 05:53-06:07 |
| 6 | Virgo | 10 | 1 | 0 | 0 | 1,138 | 1,228 (Domain) | 13-15 | 184,947 | 31 | 06:07-06:20 |
| 7 | Libra | 11 | 1 | 0 | 0 | 1,182 | 1,228 (Domain) | 15-16 | 198,373 | 38 | 06:20-06:34 |
| 8 | Scorpio | 11 | 1 | 0 | 0 | 1,135 | 1,248 (Domain) | 15-16 | 190,252 | 36 | 06:34-06:48 |
| 9 | Sagittarius | 11 | 1 | 0 | 0 | 1,171 | 1,238 (Domain) | 14-16 | 196,570 | 45 | 06:48-07:04 |
| 10 | Capricorn | 10 | 1 | 0 | 0 | 1,105 | 1,244 (Domain) | 14-15 | 179,352 | 33 | 07:04-07:16 |
| 11 | Aquarius | 10 | 1 | 0 | 0 | 1,079 | 1,244 (Domain) | 14-15 | 185,111 | 33 | 07:16-07:28 |
| 12 | Pisces | 12 | 1 | 0 | 0 | 1,175 | 1,241 (Domain) | 15-16 | 189,125 | 32 | 07:28-07:42 |
| | **Total** | **130** | **12** | **0** | **0** | **1,119** | **1,248** | **avg 14.7** | **2,207,670** | **414** | **05:03-07:43** |

Word counts are by `wc -w`. Pointer counts are the data rows in section 2's table.

## Tokens and wall-clock
- **Sub-agent tokens:** 2,207,670 (12 sign agents, no relaunches). That is about 17,000 per sheet. The run agent's own tokens are not included.
- **Wall-clock:** 05:03 to 07:43, about 160 minutes, in parallel with the Tuva, Chechnya and Dagestan runs. Sign agents took 10.9 to 15.3 minutes each.
- The cost is in line with Day 2's nations (2.17 to 2.22M each).

## Rule breaks and fixes
- **Gemini, repeated lines (my own scan; QA does not test for them):** two lines were repeated between sheets. A Khanty and Mansi term row (*Пор, Мось*, "the two moieties") appeared in both 05 Connection and 06 Duality. A bare compare line ("Evenks and Dolgans of the Yenisei and Taymyr") appeared in both 00 Domain and 04 Curiosity, and in Curiosity it gave no reason. I fixed both with the smallest edit. In Connection, the gloss now reads "the two moieties, tied to each other by marriage rules", marked *check*. In Curiosity, I added a reason phrase. Status lines are untouched.
- **Virgo:** the agent wrote 01 Work after 02 Service. It had read the whole block first, so this is harmless. The few law mentions in Virgo only point the reader to Libra and Capricorn, which is allowed.
- **Pisces 07 Spirituality:** the "Held for review" line names a set-aside Omsk Oblast New Age site as a category only, with no name. That fits the rule, so I left it.
- **Length:** no sheet goes over the 1,250 flag. The range is 964 to 1,248, and every Domain sheet sits between 1,198 and 1,248. As on Day 2, the agents seem to aim just under the flag. The length rule is undecided, so nothing was trimmed.
- The sheets contain no zodiac words, no "Indian" and no South Asian names. The only repeated line across the whole nation is the rule's own category-only "Held for review" line, which appears in 11 sheets.

## Thin, repetitive or generic sheets (by name)
- **Fewest pointers (13):** Aries 06 Courage, 08 Anger, 09 Competition, 10 Recklessness; Virgo 06 Perfectionism. All are within the 12 to 16 range. I spot-checked Anger and found it specific: Pokrovsky on the 1648-49 Tomsk revolt, Siberian charms against anger, Letov and Yanka, the 2018 Kemerovo *Зимняя вишня* fire protests, the 2014 federalization march, and datsan teaching. It is not generic.
- **Shortest sheets:** Taurus 09 Stubbornness (964), 08 Possessiveness (978), 10 Sensuality (983); Aries 04 Initiative (997); Aquarius 08 Detachment (997). Aries and Taurus, the first two signs, run shorter and leaner than the rest (averages 1,067 and 1,058, against 1,105 to 1,182 later).
- **Repetition:** after the Gemini fix, no table row or sentence repeats between sheets anywhere in the nation.
- **Minority-language terms:** every one of the 130 sheets has at least one non-Russian term row. 104 have three or more, 12 have two, and 2 have one.

## Pointers per sheet
The average is 14.7: 24 sheets have 16 pointers, 44 have 15, 57 have 14 and 5 have 13. None has fewer than 13.

## Do the sheets exploit the nation's depth?
**Yes, broadly.**
- **Peoples, beyond the best-known two or three:** Buryat appears in 118 sheets, Altai 111, Evenk 110, Nenets 109, Khanty 106, Khakas 97, Mansi 89 and Siberian Tatars 82. Dolgans appear in 63, Shors 58, Selkups 54, Kets 53, Teleuts 38, Nganasans 31, Tofalars 18, Chulyms 12 and Yukaghirs 5. Old Believers appear in 97 sheets, Siberian Germans in 68 and Kazakhs in 43, with Poles, Ukrainians, Chinese and Central Asian migrants also present.
- **Regions:** Novosibirsk (90 sheets), Irkutsk and Krasnoyarsk (88 each), Tomsk (77), Omsk (61), Yamal (52), Kuzbass and Kemerovo (46), Transbaikalia (42) and Tyumen (31) are all well covered. Altai Krai's Barnaul (3) and Chita (3) are thin as cities, though Altai and Transbaikalia are well covered as regions.
- **Pre-modern layer:** strong and varied. Siberian chronicles and Remezov (15 to 18 sheets), Geser (11), Pazyryk and Ukok (10), *Maadai-Kara* (6), the Ob-Ugrian bear festival (6), Kuchum and Yermak, Avvakum, the 18th-century academic expeditions (Messerschmidt, Gmelin, Müller), and 17th-century town revolts.
- **Modern sources:** a mix of archives (Memorial in 17 sheets, Kunstkamera in 8), polling (Levada 30, VTsIOM 17), oblastnichestvo (Yadrintsev 13, Potanin 9), Siberian literature (Rasputin 26, Shukshin 19, Astafyev 16, Vampilov 12), and regional media, music and NGOs. Levada is the most frequent single source, as it was for Russia, but the sheets point to different survey items.

**Two caveats for the author:**
1. **Scope drift into neighboring targets.** Sakha (Yakut) terms or pointers appear in about 62 to 70 sheets, and Tuva in 15. One example is Kenin-Lopsan and the Dungur society in Aries 08 Anger. Tuva is its own target, and the Sakha Republic may belong to Künnarantaiga or the Far East. Mongolia also appears in 46 sheets, mostly for comparison with the Buryat material. Stage 0 should decide which of these stay.
2. **Buryatia and Transbaikalia are treated as core lands** ("Urals to Transbaikalia"), but the header does not settle this. Several sheets say "if Buryat lands are inside". The Buryat material, which appears in 118 sheets, stands or falls with that ruling.

## Files
- Sheets: `Targets/Russia/Siberia/Springboards/01 - Aries/` to `12 - Pisces/` (130 files).
- Run log: 12 lines appended to `_dispatch/SPRINGBOARD_PROGRESS.md`, with the nation-complete note on the Pisces line.
