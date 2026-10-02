"""
Russia — bare reference map for reviewing the nation-boundary decisions (2026-09-27).

Author-requested: a Woodard-style reference (plain fill colors, subdivision borders, nation-name labels
directly on the map — no side panel, no legend, no capitals, no sphere overlay) so the underlying territorial
decisions in subdivisions.csv can be reviewed on their own, before further label-polish work continues on the
four decorated production maps (which may need redoing if nation boundaries change as a result of this
review). Same geometry/CRS/antimeridian handling as render_map_russia_full.py — this script only strips the
decoration, it does not re-derive anything.

Inputs : subdivisions.csv (this package), Natural Earth 10m admin-1 (geojson/).
Output : russia_reference_map.png (+ .svg)
"""
import os
from pathlib import Path
import pandas as pd
import geopandas as gpd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patheffects
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle
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

NATIONS_HERE = ['Russia', 'The Northern Republic', 'The Volga Republic', 'Tatarstan', 'Kalmykia',
                'The Urals Republic', 'Bashkortostan', 'Western Siberia', 'Eastern Siberia', 'Tuva', 'Sakha',
                'The Russian Far East', 'Kaliningrad', 'Chechnya', 'Ingushetia', 'Dagestan',
                'North Ossetia-Alania', 'Kabardino-Balkaria', 'Karachay-Cherkessia', 'Southern Russia']
sub = pd.read_csv(HERE / 'subdivisions.csv')
sub = sub[sub.nation.isin(NATIONS_HERE)].copy()
COLORS = sub.groupby('nation').color_hex.first().to_dict()
PROVISIONAL = ['The Russian Far East', 'Sakha', 'Bashkortostan', 'North Ossetia-Alania',
               'Kabardino-Balkaria', 'Karachay-Cherkessia']

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
padx, pady = 550000.0, 550000.0
xlim = (minx - padx, maxx + padx)
ylim = (miny - pady, maxy + pady)

# ---------- no side panel — the map fills the whole figure; a plain title sits over open sea in the
#            upper-left, the one piece of chrome this reference keeps ----------
xr, yr = xlim[1] - xlim[0], ylim[1] - ylim[0]
W = 26
H = W * yr / xr
fig = plt.figure(figsize=(W, H))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(xlim); ax.set_ylim(ylim); ax.set_aspect('equal'); ax.axis('off')
SEA, NEIGH, INK = '#D7E3EA', '#ECE9E2', '#2B2B2B'
ax.add_patch(Rectangle((xlim[0], ylim[0]), xlim[1] - xlim[0], ylim[1] - ylim[0], facecolor=SEA, zorder=0))
others = a0[a0.ADMIN != 'Russia']
others.plot(ax=ax, facecolor=NEIGH, edgecolor='#B9B4A8', linewidth=0.5, zorder=1)

def lighten(hexc, t=0.22):
    c = np.array(mpl.colors.to_rgb(hexc))
    return tuple(c + (1 - c) * t)

# fills a touch more saturated than the decorated map's (t=0.22 vs 0.32) — with no legend to cross-reference,
# the fill color itself has to carry more of the identification work
for _, r in nations.iterrows():
    gpd.GeoSeries([r.geometry], crs=CRS).plot(ax=ax, facecolor=lighten(COLORS[r.nation]), edgecolor='none', zorder=2)
units.boundary.plot(ax=ax, color='white', linewidth=0.35, alpha=0.9, zorder=3)

nations.boundary.plot(ax=ax, color='white', linewidth=1.8, zorder=5)
nations.boundary.plot(ax=ax, color=INK, linewidth=0.6, zorder=5.1)
others.boundary.plot(ax=ax, color='#9A958A', linewidth=0.4, zorder=5)

def T(lon, lat, s, **kw):
    p = P(lon, lat)
    return ax.text(p.x, p.y, s, zorder=kw.pop('zorder', 11), **kw)

halo = [mpl.patheffects.withStroke(linewidth=3.2, foreground='white', alpha=0.9)]
nat_kw = dict(family=SERIF, fontweight='bold', color=INK, ha='center', va='center', path_effects=halo)

# every nation gets a label regardless of size (no TINY_SKIP here — this map's whole job is to show every
# boundary decision, including the small North Caucasus republics), just a smaller font floor
for _, r in nations.iterrows():
    geom = r.geometry
    c = geom.centroid
    lonlat = gpd.GeoSeries([c], crs=CRS).to_crs('EPSG:4326').iloc[0]
    area_frac = geom.area / core_all.area
    fs = max(9, min(20, 9 + area_frac * 500))
    label = r.nation.upper()
    mark = ' [P]' if r.nation in PROVISIONAL else ''
    T(lonlat.x - 360 if lonlat.x > 180 else lonlat.x, lonlat.y, label + mark, fontsize=fs, **nat_kw)

fig.text(0.015, 0.975, 'Russia — nation-boundary reference (unstyled)', family=SERIF, fontsize=20,
         fontweight='bold', color=INK, va='top',
         path_effects=[mpl.patheffects.withStroke(linewidth=4, foreground='white', alpha=0.85)])
fig.text(0.015, 0.93, 'For reviewing subdivisions.csv\'s nation assignments only — not a production map.\n'
         '[P] = provisional / author-review-needed. See the package README for what each one means.',
         family=SANS, fontsize=11, color='#444', va='top', linespacing=1.35,
         path_effects=[mpl.patheffects.withStroke(linewidth=3, foreground='white', alpha=0.85)])

for ext in ('png', 'svg'):
    fig.savefig(OUT / f'russia_reference_map.{ext}', dpi=200, facecolor=SEA)
print('saved', OUT)
