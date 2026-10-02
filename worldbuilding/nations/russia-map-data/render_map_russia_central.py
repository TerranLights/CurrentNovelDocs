"""
Russia — the Central close-up: The Urals & Siberia (Stage 3, first pass, 2026-09-27).

Companion to render_map_russia_full.py — same subdivisions.csv/spheres.csv, same CRS/antimeridian handling,
same drawing pattern, just a tighter regional crop and a nation subset. See that script's own docstring for
the Stage 1 survey / pipeline-order context.

Rebuilt 2026-09-27 (round 2) as a standalone reconstruction after this file was overwritten in place by a
later reorganization round without being archived first — see the package README for the full story. Rebuilt
from the recovered original render (russia_central_map.png), the intact render_map_russia_full.py template,
and this session's own memory of the Yekaterinburg/Kyzyl label fixes. Not guaranteed byte-identical to the
original file, but verified to reproduce the same nations, framing, and label placement.

Inputs : subdivisions.csv, spheres.csv (this package), Natural Earth 10m admin-1 (geojson/).
Output : russia_central_map.png (+ .svg)
"""
import os
from pathlib import Path
import pandas as pd
import geopandas as gpd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patheffects
from matplotlib import font_manager as fm
from matplotlib.patches import Patch, Rectangle
from matplotlib.lines import Line2D
from shapely.geometry import Point
from shapely.ops import transform as shp_transform
import numpy as np

HERE = Path(__file__).parent
NE = Path(os.environ.get('NE_DIR', '/home/claude/ne'))
OUT = Path(os.environ.get('OUT_DIR', '/mnt/user-data/outputs'))
OUT.mkdir(parents=True, exist_ok=True)

for f in (HERE / 'fonts').glob('*.ttf'):
    fm.fontManager.addfont(str(f))
SERIF, SANS = 'Crimson Text', 'Lato'
mpl.rcParams['font.family'] = SANS
mpl.rcParams['svg.fonttype'] = 'none'

CRS = '+proj=laea +lat_0=63 +lon_0=95 +datum=WGS84 +units=m'

def shift_lon(x, y, *rest):
    x2 = [(xx + 360 if xx < 0 else xx) for xx in x]
    return (x2, y, *rest) if rest else (x2, y)

def antimeridian_fix(gdf):
    gdf = gdf.copy()
    gdf['geometry'] = gdf['geometry'].apply(lambda geom: shp_transform(shift_lon, geom))
    return gdf.set_crs('EPSG:4326', allow_override=True)

NATIONS_HERE = ['The Urals Republic', 'Bashkortostan', 'Western Siberia', 'Eastern Siberia', 'Tuva']
sub = pd.read_csv(HERE / 'subdivisions.csv')
sub = sub[sub.nation.isin(NATIONS_HERE)].copy()
COLORS = sub.groupby('nation').color_hex.first().to_dict()
PROVISIONAL = ['Bashkortostan']

a1_raw = gpd.read_file(NE / 'ne_10m_admin_1_states_provinces.geojson')
a1 = a1_raw[(a1_raw.admin == 'Russia') & (~a1_raw.name.isin(['Crimea', 'Sevastopol']))][['name', 'geometry']].copy()
NAME2NATION = dict(zip(sub.subdivision_name, sub.nation))
a1['nation'] = a1.name.map(NAME2NATION)
a1 = a1.dropna(subset=['nation']).copy()
a1 = antimeridian_fix(a1)
a1 = a1.to_crs(CRS)
a1['geometry'] = a1.buffer(0)
units = a1.dissolve(by=['nation', 'name'], as_index=False)
print(f'{len(units)} polygons matched, {len(units.nation.unique())} nations')

nations = units.dissolve(by='nation', as_index=False)

a0_raw = gpd.read_file(NE / 'ne_10m_admin_0_countries.geojson')
a0 = antimeridian_fix(a0_raw).to_crs(CRS)

def P(lon, lat):
    p = Point(lon + 360 if lon < 0 else lon, lat)
    return gpd.GeoSeries([p], crs='EPSG:4326').to_crs(CRS).iloc[0]

core_all = nations.union_all()
minx, miny, maxx, maxy = core_all.bounds
padx, pady = 300000.0, 300000.0
xlim = (minx - padx, maxx + padx)
ylim = (miny - pady, maxy + pady)

MAP_FRAC = 0.74
xr, yr = xlim[1] - xlim[0], ylim[1] - ylim[0]
W = 24
H = (MAP_FRAC * W) * yr / xr
fig = plt.figure(figsize=(W, H))
ax = fig.add_axes([0, 0, MAP_FRAC, 1])
ax.set_xlim(xlim); ax.set_ylim(ylim); ax.set_aspect('equal'); ax.axis('off')
SEA, NEIGH, INK = '#D7E3EA', '#ECE9E2', '#2B2B2B'
ax.add_patch(Rectangle((xlim[0], ylim[0]), xlim[1] - xlim[0], ylim[1] - ylim[0], facecolor=SEA, zorder=0))
others = a0[a0.ADMIN != 'Russia']
others.plot(ax=ax, facecolor=NEIGH, edgecolor='#B9B4A8', linewidth=0.5, zorder=1)

def lighten(hexc, t=0.32):
    c = np.array(mpl.colors.to_rgb(hexc))
    return tuple(c + (1 - c) * t)

for _, r in nations.iterrows():
    gpd.GeoSeries([r.geometry], crs=CRS).plot(ax=ax, facecolor=lighten(COLORS[r.nation]), edgecolor='none', zorder=2)
units.boundary.plot(ax=ax, color='white', linewidth=0.35, alpha=0.9, zorder=3)

nations.boundary.plot(ax=ax, color='white', linewidth=1.5, zorder=5)
nations.boundary.plot(ax=ax, color=INK, linewidth=0.45, zorder=5.1)
others.boundary.plot(ax=ax, color='#9A958A', linewidth=0.4, zorder=5)

def T(lon, lat, s, **kw):
    p = P(lon, lat)
    return ax.text(p.x, p.y, s, zorder=kw.pop('zorder', 11), **kw)

halo = [mpl.patheffects.withStroke(linewidth=3, foreground='white', alpha=0.85)]
nat_kw = dict(family=SERIF, fontweight='semibold', color=INK, ha='center', va='center', path_effects=halo)

TINY_SKIP = 0.0015
for _, r in nations.iterrows():
    geom = r.geometry
    c = geom.centroid
    lonlat = gpd.GeoSeries([c], crs=CRS).to_crs('EPSG:4326').iloc[0]
    area_frac = geom.area / core_all.area
    if area_frac < TINY_SKIP:
        continue
    fs = max(7, min(15, 7 + area_frac * 400))
    label = r.nation.upper() if len(r.nation) < 14 else r.nation
    mark = ' [P]' if r.nation in PROVISIONAL else ''
    T(lonlat.x - 360 if lonlat.x > 180 else lonlat.x, lonlat.y, label + mark, fontsize=fs, **nat_kw)

sea_kw = dict(family=SERIF, style='italic', fontsize=11, color='#6D8797', ha='center')
for t, lon, lat in [('ARCTIC OCEAN', 90.0, 82.5), ('Barents Sea', 40.0, 74.0), ('Kara Sea', 75.0, 76.0),
                    ('Laptev Sea', 125.0, 76.0)]:
    T(lon, lat, t, **sea_kw)

# Yekaterinburg and Kyzyl both collided with their own nation's auto-centroid label ("The Urals Republic",
# "TUVA") at the default offset — nudged below with a vertical (dy) offset.
CAPS = {'Yekaterinburg': (60.61, 56.84, 'l', None, -34e3), 'Ufa': (55.97, 54.74, 'r'),
        'Novosibirsk': (82.92, 55.03, 'r'), 'Krasnoyarsk': (92.87, 56.01, 'l'),
        'Kyzyl': (94.44, 51.72, 'r', None, -55e3)}
CITIES = {'Perm': (56.23, 58.01, 'r'), 'Omsk': (73.37, 54.99, 'r'), 'Irkutsk': (104.3, 52.29, 'r'),
          'Norilsk': (88.2, 69.35, 'l')}
places = gpd.read_file(NE / 'ne_10m_populated_places_simple.geojson')
for d, is_cap in ((CAPS, True), (CITIES, False)):
    for n, v in d.items():
        lon, lat, side = v[0], v[1], v[2]
        dx_override = v[3] if len(v) > 3 else None
        dy = v[4] if len(v) > 4 else 0
        p = P(lon, lat)
        ax.plot(p.x, p.y, marker='s' if is_cap else 'o', ms=6 if is_cap else 3.4,
                mfc=INK if is_cap else 'white', mec=INK, mew=0.8, zorder=12)
        dx = dx_override if dx_override is not None else (16e3 if side == 'l' else -16e3)
        ha = 'left' if dx >= 0 else 'right'
        ax.text(p.x + dx, p.y + dy, n, ha=ha, va='center',
                fontsize=9.5 if is_cap else 8, fontweight='bold' if is_cap else 'normal',
                family=SANS, color=INK, zorder=12, path_effects=halo)

# ---------- side panel ----------
fig.patches.append(Rectangle((MAP_FRAC, 0), 1 - MAP_FRAC, 1, transform=fig.transFigure, color='#FBFAF7', zorder=-1))
px = MAP_FRAC + 0.013
fig.text(px, 0.975, 'Russia', family=SERIF, fontsize=28, fontweight='bold', color=INK, va='top')
fig.text(px, 0.938, 'The Urals & Siberia', family=SERIF, style='italic', fontsize=13, color='#444', va='top',
         linespacing=1.25)
fig.text(px, 0.895, 'Post-collapse successor states · first pass, Stage 2 not yet done\n'
        'first-order subdivisions, whole units only\n3 of 4 maps — see also the full overview, the West and East close-ups',
        family=SANS, fontsize=8.5, color='#666', va='top', linespacing=1.3)
fig.add_artist(plt.Line2D([px, 0.99], [0.830, 0.830], color='#B9B3A7', lw=0.8))

handles, labels = [], []
def head(t):
    handles.append(Patch(visible=False)); labels.append(t)

head('$\\bf{Nations}$  (hard borders)')
for n in sorted(NATIONS_HERE):
    mark = ' [P] provisional' if n in PROVISIONAL else ''
    handles.append(Patch(facecolor=lighten(COLORS[n]), edgecolor=INK, lw=0.3)); labels.append(n + mark)
handles.append(Line2D([], [], color=INK, lw=0.8)); labels.append('National border')
handles.append(Line2D([], [], color='#BBB', lw=0.8)); labels.append('First-order subdivision')
handles.append(Line2D([], [], color='#6B3FA0', lw=1.4, ls=(0, (1, 1.6))))
labels.append('The Mongolic World')
handles.append(Line2D([], [], marker='s', ls='', mfc=INK, mec=INK, ms=5)); labels.append('Nation capital')

leg = fig.legend(handles, labels, loc='upper left', bbox_to_anchor=(px, 0.805), frameon=False,
                 fontsize=7.4, handlelength=2.0, handleheight=1.05, labelspacing=0.42, borderpad=0,
                 prop={'family': SANS, 'size': 7.4})
leg.set_zorder(20)

foot = ('First pass, built 2026-09-27.\n'
        '3 of 4 maps — see also the full overview, the West and East close-ups.\n'
        'Lambert azimuthal equal-area. Boundaries: Natural Earth 1:10m.\n'
        '[P] = provisional / genuine author-review-needed judgment call — see legend and README.')
fig.text(px, 0.028, foot, fontsize=7.0, family=SANS, color='#555', va='bottom', linespacing=1.4)
for t in ax.texts:
    t.set_clip_on(True)

for ext in ('png', 'svg'):
    fig.savefig(OUT / f'russia_central_map.{ext}', dpi=200, facecolor=SEA)
print('saved', OUT)
