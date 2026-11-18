# Künnarantaiga springboards: run report (2026-11-17, day 2, deeper brief)

**Result:** 130/130 sheets `STATUS: done 2026-11-17, not verified`, all twelve signs, Aries to Pisces. One agent per nation-sign (12 sub-agents), **0 relaunches**. Folder: `Targets/Russia/Künnarantaiga/Springboards/`.

**Wall-clock:** 05:03 to 07:46 (about 2 h 43 min, signs run one after another). **Sub-agent tokens:** 2,225,407 (459 tool uses; sum of sub-agent run times about 158 min). Run agent tokens are not in this figure (the main session adds them).

## Per-sign table
| # | Sign | Sheets | Avg words (wc -w) | Longest | Pointers per sheet (min/avg/max) | Sub-agent tokens | Minutes | QA |
|---|---|---|---|---|---|---|---|---|
| 1 | Aries | 11 | 1,088 | 1,215 (Domain) | 14 / 14.5 / 16 | 159,017 | 13.1 | 0 |
| 2 | Taurus | 11 | 1,123 | 1,244 (Domain) | 14 / 15.1 / 16 | 192,762 | 15.0 | 0 |
| 3 | Gemini | 10 | 1,093 | 1,215 (Domain) | 14 / 15.2 / 16 | 180,920 | 12.7 | 1 (false positive) |
| 4 | Cancer | 10 | 1,077 | 1,206 (Domain) | 14 / 14.6 / 16 | 181,208 | 12.1 | 0 |
| 5 | Leo | 13 | 1,061 | 1,233 (Domain) | 14 / 14.9 / 16 | 196,246 | 14.2 | 0 |
| 6 | Virgo | 10 | 1,129 | 1,230 (Work) | 14 / 14.4 / 16 | 170,985 | 10.7 | 0 |
| 7 | Libra | 11 | 1,072 | 1,236 (Domain) | 14 / 14.0 / 14 | 199,118 | 14.0 | 0 |
| 8 | Scorpio | 11 | 1,083 | 1,240 (Domain) | 14 / 14.6 / 16 | 184,063 | 12.7 | 0 |
| 9 | Sagittarius | 11 | 1,074 | 1,215 (Domain) | 13 / 14.2 / 15 | 188,209 | 14.1 | 0 |
| 10 | Capricorn | 10 | 1,074 | 1,232 (Domain) | 14 / 14.6 / 16 | 189,191 | 13.1 | 0 |
| 11 | Aquarius | 10 | 1,040 | 1,236 (Domain) | 14 / 14.6 / 16 | 183,504 | 11.7 | 0 |
| 12 | Pisces | 12 | 1,096 | 1,241 (Domain) | 13 / 14.4 / 15 | 200,184 | 14.6 | 0 |
| | **Total** | **130** | **1,084** (951 to 1,244) | | **13 / 14.6 / 16** | **2,225,407** | **158** | **1** |

Pointers per sheet: 14 on 63 sheets, 15 on 50, 16 on 15, 13 on 2 (Sagittarius Fundamentalism, Pisces Intuition). No sheet passed the scan's 1,250-word flag; concept sheets mostly run 1,000 to 1,170, a little above the brief's 700 to 1,000 guide (no length instruction was added to the prompts).

## Rule breaks and fixes
- **None needing a fix.** The whole-nation QA reports 1 problem, a false positive: `03 - Gemini/04 - Curiosity.md` line 36, "Sikhote-Alin meteorite fall (1947)". The scan's South Asian pattern `sikh` matches **Sikhote-Alin**, the mountain range of Primorye and Khabarovsk. Kept as is (a real place in the nation's lands). **Suggest adding Sikhote-Alin to the scan's allowlist**, since it will recur for this nation in the research stage.
- No zodiac words, no "Indian", no URLs, no findings phrases. One category-only Held-for-review line (Scorpio, Rebirth: Buddhist scriptures of South Asian origin in the Buryat canon). Law appears outside Libra and Capricorn only as flags pointing there (and Pisces Crime's thieves'-code terms, which are the concept's own vocabulary).
- No repeated lines (over 40 characters) between sheets inside any sign.

## A prompt addition the author should know about
The tracker header says only "Pre-war lands carried: Russia", and `00 - Scope.md` does not exist, so a sub-agent following the brief alone would have written for Russia as a whole. For accuracy, the run agent added the nation's lands to every sub-agent prompt, from `Hermes_research/reference/geography/01_territories_by_target.md`: the 12 whole units Sakha (Yakutia), Amur, Buryatia, Zabaykalsky, Chukotka, Kamchatka, Khabarovsk, Magadan, Primorye, Sakhalin (with the Kurils), the Jewish AO and Irkutsk; capital Vladivostok. Nothing else in the prompt was changed beyond the day-1 lessons. The other Russia successors may have the same header gap. **Suggest putting the unit list into each Russia-successor tracker header** (or into the brief).

## Thin, repetitive or generic sheets (by name)
- **Fewer peoples named** (4 to 6 of the nation's groups mentioned, against 10 to 32 elsewhere): Libra *Impartiality*, Aquarius *Detachment*, Pisces *Crime*, Capricorn *Ambition*, Cancer *Care*, Libra *Projection*. These lean on Russian-language and national sources.
- **No clear pre-modern pointer:** Aries *Identity* (starts at the 1926 census; Sakha and Buryat genealogical and chronicle traditions would fit), Virgo *Criticism* (Soviet and present-day sources; only the Cossack and Semeiskie chastushki reach back), Libra *Projection* (all 20th and 21st century), Pisces *Escapism*. Most other sheets carry an oral, epic or 18th to 19th-century ethnographic pointer.
- **Repeated sources across signs** (expected over 130 sheets, not within a sign): Vitebsky, *The Reindeer People* (about 11 sheets), Krasheninnikov's *Описание земли Камчатки* (about 8), Gray on Chukotka (about 8), Quijada, *Buddhists, Shamans, and Soviets* (about 8), Rasputin, *Прощание с Матёрой* (about 8), Kerttula, Balzer, Humphrey, Ledeneva, the Jesup monographs and Avvakum's *Житие* (4 to 6 each). No source fills a whole sign.
- No sheet reads as generic: every one names Künnarantaiga's own places, archives and peoples.

## Do the sheets exploit the nation's depth?
**Mostly yes.** Coverage of the nation's peoples across the 130 sheets: Sakha and Buryats in all 130; Koreans 115; Chukchi 114; Evenks 106; the Jewish AO / Yiddish 97; Old Believers (Semeiskie) 96; Koryaks 93; Nanai 82; Yupik 77; Nivkh 76; Chinese 69; Ulch 66; Evens about 65; Udege 65; Cossacks 56; Japanese (Karafuto) 55; Itelmen 50; and smaller peoples reach many sheets too (Uilta 33, Yukaghir 30, Oroch 24, Ainu 23, Dolgan 21, Negidal 20, Kamchadals 20, Tofalar and Soyots 18 each, Chuvans 11, Kerek 6). Native scripts: Sakha/Buryat Cyrillic letters in 107 sheets, hangul in 98, Yiddish in Hebrew script in 77, Chinese or Japanese script in 57; about 47 Cyrillic words per sheet. Pre-modern pointers are common (olonkho and the Geser epic, Krasheninnikov, Avvakum, the Jesup Expedition, Ksenofontov, Arsenyev, Chekhov's *Sakhalin Island*). Weaker spots: Khamnigans, Molokans and Oroks appear only once to a few times; Irkutsk's and Zabaykalsky's non-Indigenous regional cultures get less than Primorye and Sakha.

**All of it is unverified:** every named item is marked *check* and must be verified in the research stage.
