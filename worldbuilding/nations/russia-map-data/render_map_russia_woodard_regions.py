"""
Russia — Woodard-style cultural-region reference map (2026-09-27).

Author-requested: matches the exact format of `y-files/Map Files/Latin America/01 initial generations/
map-1-full-regions.png` — a PRE-DECISION cultural/historical framework map, not a hard-border nation map.
"First-pass cultural regions, for consideration only, no nations named, no borders settled." Built from
core/domain/sphere geometry (same model as Latin America's regions_geo.py/render.py): core = identity
strongest (solid fill), domain = clear but lesser influence (light fill), sphere = wide, mild influence
(hatching + dotted edge, allowed to overlap between regions — intentional, not an error). This is NOT
render_map_russia_woodard.py (that script is the plain nation-boundary map with just the Mongolic sphere
line added) and does NOT reuse subdivisions.csv's hard-border nation list — that CSV was Stage 3 work,
already a step ahead of where this review map sits. Every region here traces back to a specific finding in
`worldbuilding/extractions/Russia - Federal Fractures and the Far Eastern Question (survey).md`; where the
survey didn't research something, this map says so in the blurb and grades it low confidence rather than
inventing certainty, the same discipline Latin America's own reference map held to (visible unclaimed cream
territory, "gap in survey" notes).

Inputs : Natural Earth 10m admin-1 (geojson/).
Output : russia_cultural_regions_map.png (+ .svg)
"""
import os
import textwrap
from pathlib import Path
import geopandas as gpd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.patches import Rectangle
from matplotlib.lines import Line2D
from shapely.geometry import Point
from shapely.ops import transform as shp_transform, unary_union
import numpy as np

HERE = Path(__file__).parent
NE = Path(os.environ.get('NE_DIR', '/home/claude/ne'))
OUT = Path(os.environ.get('OUT_DIR', '/mnt/user-data/outputs'))
OUT.mkdir(parents=True, exist_ok=True)

for f in (HERE / 'fonts').glob('*.ttf'):
    mpl.font_manager.fontManager.addfont(str(f))
SERIF, SANS = 'Crimson Text', 'Lato'
mpl.rcParams['font.family'] = SANS
mpl.rcParams['svg.fonttype'] = 'none'
mpl.rcParams['hatch.linewidth'] = 0.6

CRS = '+proj=laea +lat_0=63 +lon_0=95 +datum=WGS84 +units=m'

def shift_lon(x, y, *rest):
    x2 = [(xx + 360 if xx < 0 else xx) for xx in x]
    return (x2, y, *rest) if rest else (x2, y)

def antimeridian_fix(gdf):
    gdf = gdf.copy()
    gdf['geometry'] = gdf['geometry'].apply(lambda geom: shp_transform(shift_lon, geom))
    return gdf.set_crs('EPSG:4326', allow_override=True)

a1_raw = gpd.read_file(NE / 'ne_10m_admin_1_states_provinces.geojson')
rus = a1_raw[(a1_raw.admin == 'Russia') & (~a1_raw.name.isin(['Crimea', 'Sevastopol']))].copy()
rus = rus.dropna(subset=['name']).copy()
rus = antimeridian_fix(rus).to_crs(CRS)
rus['geometry'] = rus.geometry.buffer(0)
UNIT = {r['name']: r.geometry for _, r in rus.iterrows()}
print(f'{len(UNIT)} Russian admin-1 units loaded')

a0_raw = gpd.read_file(NE / 'ne_10m_admin_0_countries.geojson')
a0 = antimeridian_fix(a0_raw).to_crs(CRS)

def U(*names):
    return unary_union([UNIT[n] for n in names])

# ------------------------------------------------------------------ region definitions
# Every subdivision-name key below is checked against Natural Earth's own admin-1 name for Russia (see the
# printed count above); 'Buryat' (Buryatia) deliberately appears in TWO regions' geometry (13's domain AND
# 12's own core) — see region 12's own note. That is the one deliberate overlap outside the sphere layer;
# every other overlap is sphere-only, per the template's own "overlapping spheres are intentional" rule.
REGIONS = {
 1: dict(name='The Russian Core', confidence='high', color='#3A6EA5',
         blurb='Moscow, St. Petersburg and the Central Economic Region — Rosstat\'s densest, most '
               'industrially developed macro-region; two of the survey\'s five real federal-budget donors',
         core=['Moskva', 'Moskovskaya', 'City of St. Petersburg', 'Leningrad', 'Vladimir', 'Ivanovo',
               'Kaluga', 'Kostroma', "Ryazan'", 'Smolensk', 'Tula', "Tver'", "Yaroslavl'"],
         domain=['Bryansk', 'Kursk', 'Lipetsk', 'Orel', 'Tambov', 'Voronezh', 'Belgorod', 'Novgorod',
                 'Pskov', 'Nizhegorod', 'Vologda'],
         sphere=['Kirov', 'Murmansk', "Arkhangel'sk", 'Komi', 'Karelia', 'Nenets', 'Samara', "Ul'yanovsk",
                 'Saratov', 'Volgograd', "Astrakhan'", 'Orenburg', 'Sverdlovsk', "Perm'", 'Chelyabinsk',
                 'Kurgan', 'Penza']),
 2: dict(name='Tatarstan', confidence='high', color='#C0392B',
         blurb='Declared sovereignty 30 Aug 1990; the Ittifaq party pushed outright independence through '
               'the 1990s — the most economically credible non-Caucasus secession case in the country',
         core=['Tatarstan'], domain=[], sphere=[]),
 3: dict(name='Bashkortostan', confidence='medium', color='#B5651D',
         blurb='Declared sovereignty 11 Oct 1990, partly defensive against Tatar assimilation — but Bashkirs '
               'are only the third-largest group in their own republic, behind Russians and Tatars',
         core=['Bashkortostan'], domain=[], sphere=[]),
 4: dict(name='The Volga-Ural Belt', confidence='low', color='#D4A017',
         blurb='Chuvash, Mari, Udmurt, Mordovia — grouped geographically as Volga-Ural Turkic/Finno-Ugric '
               'in the survey\'s Tier 1 table, not individually researched this pass',
         core=[], domain=['Chuvash', 'Mariy-El', 'Udmurt', 'Mordovia'],
         sphere=['Kirov', 'Penza', "Ul'yanovsk", 'Samara']),
 5: dict(name='Chechnya', confidence='high', color='#7B241C',
         blurb='96.24% Chechen, ~2% Russian — mono-ethnic, with the strongest fought-and-recent '
               'independence history in the country (First and Second Chechen Wars, 1994-2009)',
         core=['Chechnya'], domain=[], sphere=[]),
 6: dict(name='Ingushetia', confidence='high', color='#A93226',
         blurb='93% Ingush, ~1% Russian — functionally mono-ethnic, the cleanest ethnic-secession case '
               'in the survey alongside Chechnya',
         core=['Ingush'], domain=[], sphere=[]),
 7: dict(name='Dagestan', confidence='medium', color='#8E44AD',
         blurb='3.6% Russian, but no single ethnic majority at all — Avar largest at ~800,000, ~30 '
               'languages total; internally as fragmented as the empire it would secede from',
         core=['Dagestan'], domain=[], sphere=[]),
 8: dict(name='The Western Caucasus & Alania', confidence='low', color='#B08BC9',
         blurb='North Ossetia, Kabardino-Balkaria, Karachay-Cherkessia — the Circassian/Balkar/Karachay/'
               'Ossetian layer of the Caucasus; real and historically significant, not researched this pass',
         core=[], domain=['North Ossetia', 'Kabardin-Balkar', 'Karachay-Cherkess'], sphere=[]),
 9: dict(name='Southern Russia (the Kuban)', confidence='low', color='#CD853F',
         blurb='Krasnodar, Adygey, Stavropol\', Rostov — Russian-majority Cossack-heritage territory '
               'adjacent to the Caucasus cases; not individually researched this pass',
         core=[], domain=['Krasnodar', 'Adygey', "Stavropol'", 'Rostov'], sphere=[]),
 10: dict(name='Tuva', confidence='high', color='#6B3FA0',
          blurb='88.7% ethnic Tuvan; Tuva\'s own 1993 constitution asserted an explicit right of secession '
                '— a documented legal claim, not just sentiment. The Mongolic sphere\'s northern dimension',
          core=['Tuva'], domain=[], sphere=[]),
 11: dict(name='Kalmykia', confidence='low', color='#9B59B6',
          blurb='Europe\'s only Buddhist-majority republic; Mongolic Tier 1, geographically isolated from '
                'Tuva/Buryatia by the width of Russia — flagged, not researched beyond that one fact',
          core=['Kalmyk'], domain=[], sphere=[]),
 12: dict(name='Buryatia — deliberately unresolved', confidence='low', color='#8E7CC3',
          blurb='The survey\'s own non-choice: Mongolic Tier 1 and Buryat intellectuals built Mongolia\'s '
                'own institutions, but Buryats are only ~30% of their own republic. Shown in both this '
                'region AND the Russian Far East\'s domain (13) — structurally identical to East Asia\'s '
                'unresolved Inner Mongolia case',
          core=[], domain=['Buryat'], sphere=[]),
 13: dict(name='The Russian Far East', confidence='medium-high', color='#2E8B7A',
          blurb='Amur, Primorsky and Khabarovsk Krai, the Jewish AO, Sakhalin, Kamchatka, Transbaikal — '
                'almost exactly the real Far Eastern Republic (1920-22), a buffer state Soviet Russia built '
                'to avoid direct conflict with Japan',
          core=["Primor'ye", 'Khabarovsk', 'Yevrey', 'Amur'],
          domain=['Sakhalin', 'Kamchatka', 'Chukchi Autonomous Okrug', 'Chita', 'Maga Buryatdan', 'Buryat'],
          sphere=[]),
 14: dict(name='Sakha (Yakutia) — grievance without a movement', confidence='medium', color='#16A085',
          blurb='~98% of Russia\'s diamonds via ALROSA, real "colonial" framing by local activists since '
                '1990 — but the survey found actual secession likelihood LOW, "weak levels of protest." '
                'Shown as domain only, not core, to reflect that calibration',
          core=[], domain=['Sakha (Yakutia)'], sphere=[]),
 15: dict(name='Siberian Regionalism (Oblastnichestvo)', confidence='medium', color='#4F7942',
          blurb='A real, non-ethnic, 160-year-old regionalist movement (Shchapov, Yadrintsev, 1860s) that '
                'produced an actual state: the Provisional Siberian Government, Omsk, 17 June 1918',
          core=['Novosibirsk', 'Omsk'],
          domain=['Tomsk', 'Kemerovo', "Tyumen'", 'Khanty-Mansiy', 'Yamal-Nenets', 'Altay', 'Gorno-Altay',
                  'Khakass'],
          sphere=['Krasnoyarsk', 'Irkutsk']),
 16: dict(name='Kaliningrad', confidence='high', color='#C71585',
          blurb='A genuine exclave, cut off from any contiguous Russian territory by Lithuania and Poland '
                '— a geographic claim, not an ethnic one',
          core=['Kaliningrad'], domain=[], sphere=[]),
}

# The Mongolic World — a cross-region cultural sphere (Tuva, Kalmykia, Buryatia), drawn as an overlay on
# top of everything above, the same "sphere" concept but spanning multiple regions' own core/domain rather
# than belonging to one — matches how this project's other maps (Oceania, the four decorated Russia maps)
# already use "The Mongolic World" as a named sphere.
MONGOLIC_SPHERE = ['Tuva', 'Kalmyk', 'Buryat']

def lighten(hexc, t):
    c = np.array(mpl.colors.to_rgb(hexc))
    return tuple(c + (1 - c) * t)

def P(lon, lat):
    p = Point(lon + 360 if lon < 0 else lon, lat)
    return gpd.GeoSeries([p], crs='EPSG:4326').to_crs(CRS).iloc[0]

def geo(names):
    names = [n for n in names if n]
    return unary_union([UNIT[n] for n in names]) if names else None

all_used = set()
for r in REGIONS.values():
    all_used |= set(r['core']) | set(r['domain']) | set(r['sphere'])
unclaimed = [n for n in UNIT if n not in all_used]
print(f'{len(all_used)} units claimed by at least one region, {len(unclaimed)} unclaimed: {unclaimed}')

core_all = unary_union(list(UNIT.values()))
minx, miny, maxx, maxy = core_all.bounds
padx, pady = 550000.0, 550000.0
xlim = (minx - padx, maxx + padx)
ylim = (miny - pady, maxy + pady)

# ------------------------------------------------------------------ draw
# H is set by the LEGEND's needs (16 regions x ~2-line blurbs + a "how to read it" block), not the map's own
# aspect ratio — Russia's wide, short shape would otherwise produce a figure much too short to fit the
# legend text, which is denser here than any prior region's legend.
xr, yr = xlim[1] - xlim[0], ylim[1] - ylim[0]
W = 30
MAP_H_IN = W * 0.665 * yr / xr   # the map panel's own height in inches, at its fixed width fraction
H = max(MAP_H_IN + 3.2, 22.0)
fig = plt.figure(figsize=(W, H), dpi=170)
MAP_FRAC_X, MAP_FRAC_Y = 0.665, MAP_H_IN / H
MAP_BOTTOM = 1 - MAP_FRAC_Y - 0.045   # anchor the map panel just below the title, not at the figure's bottom
ax = fig.add_axes([0.008, MAP_BOTTOM, MAP_FRAC_X, MAP_FRAC_Y])
ax.set_xlim(xlim); ax.set_ylim(ylim); ax.set_aspect('equal'); ax.axis('off')
OCEAN, FOREIGN, BLANK, INK = '#D9E4EA', '#ECEAE4', '#F6F3EC', '#2B2B2B'
ax.add_patch(Rectangle((xlim[0], ylim[0]), xlim[1] - xlim[0], ylim[1] - ylim[0], facecolor=OCEAN, zorder=0))
others = a0[a0.ADMIN != 'Russia']
others.plot(ax=ax, facecolor=FOREIGN, edgecolor='#B9B4A8', linewidth=0.5, zorder=1)
# unclaimed-but-in-scope territory reads as cream, not the foreign-neighbor tan
gpd.GeoSeries([geo(unclaimed)], crs=CRS).plot(ax=ax, facecolor=BLANK, edgecolor='none', zorder=1.5)

def hatch_for(i):
    return ['////', '\\\\\\\\', '||||', '----'][i % 4]

# domains, then cores (cores always win visually where they overlap a domain of the same region)
for rid, r in REGIONS.items():
    d = geo(r['domain'])
    if d is not None:
        gpd.GeoSeries([d], crs=CRS).plot(ax=ax, color=r['color'], alpha=0.42, edgecolor='none', zorder=2)
for rid, r in REGIONS.items():
    c = geo(r['core'])
    if c is not None:
        gpd.GeoSeries([c], crs=CRS).plot(ax=ax, color=r['color'], alpha=0.92, edgecolor='none', zorder=2.1)

# spheres: hatching over whatever isn't already core/domain-filled by ANY region, plus a dotted boundary
# around the region's full extent (core+domain+sphere) — overlapping sphere hatches between regions are
# intentional (contested/blended zones), matching the Latin America template exactly.
filled_anywhere = unary_union([g for r in REGIONS.values()
                                for g in (geo(r['core']), geo(r['domain'])) if g is not None])
for i, (rid, r) in enumerate(REGIONS.items()):
    s = geo(r['sphere'])
    if s is None:
        continue
    hatch_zone = s.difference(filled_anywhere)
    if not hatch_zone.is_empty:
        gpd.GeoSeries([hatch_zone], crs=CRS).plot(ax=ax, facecolor='none', edgecolor=r['color'],
                                                   linewidth=0, hatch=hatch_for(i), alpha=0.5, zorder=3)
    extent = unary_union([g for g in (geo(r['core']), geo(r['domain']), s) if g is not None])
    gpd.GeoSeries([extent.boundary], crs=CRS).plot(ax=ax, color=r['color'], linewidth=1.1,
                                                    linestyle=(0, (1.2, 1.6)), alpha=0.9, zorder=4)

# thin white seams between every claimed unit, so adjacent same-alpha fills don't visually merge
for rid, r in REGIONS.items():
    ext = unary_union([g for g in (geo(r['core']), geo(r['domain'])) if g is not None])
    if ext is not None:
        gpd.GeoSeries([ext], crs=CRS).boundary.plot(ax=ax, color='white', linewidth=0.5, alpha=0.8, zorder=5)

# The Mongolic World cross-region sphere overlay — a second, distinct dotted boundary in a color none of
# the individual regions use, drawn on top, so it reads as its own cross-cutting claim rather than being
# mistaken for one region's own sphere edge.
mongolic = geo(MONGOLIC_SPHERE)
gpd.GeoSeries([mongolic.boundary], crs=CRS).plot(ax=ax, color='#4B0082', linewidth=1.8,
                                                   linestyle=(0, (1, 2.2)), alpha=0.85, zorder=6)

others.boundary.plot(ax=ax, color='#9A958A', linewidth=0.4, zorder=5.5)
gpd.GeoSeries(list(UNIT.values()), crs=CRS).boundary.plot(ax=ax, color='#9A958A', linewidth=0.3, alpha=0.6, zorder=1.6)

def T(lon, lat, s, **kw):
    p = P(lon, lat)
    return ax.text(p.x, p.y, s, zorder=kw.pop('zorder', 20), **kw)

halo = [pe.withStroke(linewidth=3, foreground='white', alpha=0.9)]

LABELS = {
 1: (37.5, 56.6, 'THE\nRUSSIAN CORE'), 2: (50.5, 55.6, 'TATARSTAN'), 3: (56.0, 54.2, 'BASHKORTOSTAN'),
 5: (45.8, 43.4, 'CHECHNYA'), 6: (44.9, 43.15, 'INGUSH.'), 7: (47.2, 42.6, 'DAGESTAN'),
 9: (39.5, 45.5, 'SOUTHERN\nRUSSIA'), 10: (94.3, 51.6, 'TUVA'), 11: (44.3, 46.3, 'KALMYKIA'),
 12: (112.5, 53.5, 'BURYATIA\n(unresolved)'), 13: (135.5, 55.0, 'THE RUSSIAN\nFAR EAST'),
 14: (129.7, 65.5, 'SAKHA\n(domain only)'), 15: (85.0, 58.5, 'SIBERIAN\nREGIONALISM'),
 16: (20.5, 54.7, 'KALININGRAD'),
}
for rid, (lon, lat, txt) in LABELS.items():
    r = REGIONS[rid]
    fs = 15 if rid in (1, 13, 15) else 10.5
    T(lon, lat, txt, ha='center', va='center', fontsize=fs, family=SERIF, fontweight='bold', color=INK,
      linespacing=0.95, path_effects=halo)
T(97, 76, 'The Mongolic World (cross-region sphere: Tuva, Kalmykia, Buryatia)', ha='left', va='center',
  fontsize=12, family=SANS, style='italic', color='#4B0082', path_effects=halo)
T(80, 68, 'Unclaimed — in scope, no research yet', ha='center', va='center', fontsize=11, family=SANS,
  style='italic', color='#8A857B', path_effects=halo)

fig.text(0.012, 0.985, 'RUSSIA — PROPOSED POST-COLLAPSE REGIONAL DIVISION', fontsize=24, fontweight='bold',
         family=SERIF, color=INK, va='top')
fig.text(0.012, 0.962, 'First-pass cultural regions · for consideration only · no nations named, no borders settled',
         fontsize=13, color='#555', style='italic', va='top')

# ------------------------------------------------------------------ legend
# Two columns (8 regions each) — 16 regions with 2-4 line blurbs apiece overflowed a single column no
# matter how tight the per-entry spacing got, since blurb length (and therefore wrapped line count) varies
# region to region; splitting the vertical budget in half is more robust than guessing at a fixed height.
lx = fig.add_axes([0.685, 0.01, 0.305, 0.97]); lx.axis('off')
lx.set_xlim(0, 1); lx.set_ylim(0, 1)   # fixed 0-1 coordinate space — Rectangle patches added below would
                                        # otherwise trigger autoscale and silently break every yy offset
COLX = [0.0, 0.52]
yy = [0.995, 0.995]
def head(t, col=0):
    lx.text(COLX[col], yy[col], t, fontsize=12.5, fontweight='bold', family=SERIF, va='top')
    yy[col] -= 0.018
def entry(rid, col, dy=0.034):
    r = REGIONS[rid]
    x0 = COLX[col]
    lx.add_patch(Rectangle((x0, yy[col] - 0.011), 0.05, 0.011, color=r['color']))
    lx.add_patch(Rectangle((x0 + 0.05, yy[col] - 0.011), 0.035, 0.011, color=r['color'], alpha=0.42))
    conf = {'high': '●●●', 'medium-high': '●●●', 'medium': '●●○',
            'low': '●○○'}[r['confidence']]
    lx.text(x0 + 0.1, yy[col], f"{rid}. {r['name']}", fontsize=8.0, fontweight='bold', va='top')
    lx.text(x0 + 0.46, yy[col], conf, fontsize=7, va='top', ha='right', color='#666')
    body = textwrap.fill(r['blurb'], 46)
    lx.text(x0 + 0.1, yy[col] - 0.0105, body, fontsize=5.9, va='top', color='#444', linespacing=1.25)
    yy[col] -= dy + body.count('\n') * 0.0125
head('Regions', 0)
for i, rid in enumerate(REGIONS):
    entry(rid, i % 2)
yy[0] = min(yy[0], yy[1]) - 0.012
yy[1] = yy[0]
head('How to read it', 0)
items = [
    ('Solid fill', 'Solid fill — core: where identity is strongest'),
    ('Light fill', 'Light fill — domain: clear but lesser influence'),
    (None, 'Hatching + dotted edge — sphere: wide, mild influence'),
    (None, '   (overlapping spheres are intentional, not errors)'),
    (None, 'Indigo dotted line — The Mongolic World (cross-region sphere)'),
    (None, 'Buryatia sits in two regions at once — the survey’s own unresolved case'),
    (None, 'Cream — in scope but not claimed by any region (a survey gap)'),
    (None, 'Confidence:  ●●● high   ●●○ medium   ●○○ low'),
]
for kind, t in items:
    if kind is not None:
        lx.add_patch(Rectangle((0.0, yy[0] - 0.009), 0.035, 0.009, color='#777',
                                alpha=1 if kind == 'Solid fill' else 0.42))
    lx.text(0.05, yy[0], t, fontsize=7.6, va='top', linespacing=1.2)
    yy[0] -= 0.0165
yy[0] -= 0.006
lx.text(0, yy[0], textwrap.fill('Boundaries follow present-day federal subjects (Natural Earth 1:10m). '
        'Crimea and Sevastopol are excluded — Natural Earth codes them Ukrainian, not asserted as Russian '
        'here. This map predates and does not reuse the hard-border nation package in subdivisions.csv — '
        'see render_map_russia_reference.py / render_map_russia_woodard.py for that later-stage work.', 46),
        fontsize=6.6, va='top', color='#555', style='italic', linespacing=1.3)

for ext in ('png', 'svg'):
    fig.savefig(OUT / f'russia_cultural_regions_map.{ext}', dpi=170, facecolor='white')
print('saved', OUT)
