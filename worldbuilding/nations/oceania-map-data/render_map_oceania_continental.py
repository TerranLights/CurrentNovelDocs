"""
Oceania — THE CONTINENTAL MAP: Australia, New Zealand, Papua New Guinea (Stage 4).

Companion to render_map_oceania_islands.py, which covers the other 20 nations/territories. Split
2026-09-26, author-requested, from the original single-map render_map_oceania.py (still present,
kept as the reference/reproducibility copy — not part of the two-map delivery). Same subdivisions.csv
and spheres.csv as the islands map; this script just filters to a different nation subset and a much
tighter, non-antimeridian-crossing extent.

Inputs : subdivisions.csv, spheres.csv (this package), Natural Earth 10m admin-0/admin-1
         (github.com/nvkelso/natural-earth-vector, geojson/).
Output : oceania_continental_map.png (+ .svg)

Unlike the islands map, this map's real extent (Australia to New Zealand's Chatham Islands, ~112°E to
~179°E) does not cross the antimeridian in any way that matters for rendering — the antimeridian_fix()
helper is kept (harmless if applied, and New Zealand's own Chatham Islands sit at 176-177°W, close
enough to 180° that keeping the fix is cheap insurance) but this map needed no debugging pass for it
the way the islands map did.

Sphere overlay here is partial by design: only the portion of Melanesia (Papua New Guinea) and
Polynesia (New Zealand) that actually falls on this map is drawn; the rest of each sphere, plus all of
Micronesia, is out of scope here and labeled as continuing onto the companion islands map instead —
the same cross-map-sphere convention this project established for the Patani Malay World between the
Mainland and Maritime Southeast Asia maps.
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

# ---------- fonts ----------
for f in (HERE / 'fonts').glob('*.ttf'):
    fm.fontManager.addfont(str(f))
SERIF, SANS = 'Crimson Text', 'Lato'
mpl.rcParams['font.family'] = SANS
mpl.rcParams['svg.fonttype'] = 'none'

# Pacific-centered LAEA. lon_0=175 sits roughly in the middle of this map's real extent once the
# antimeridian shift below is applied (raw extent ~113E to ~235 in the shifted frame, i.e. 113E to
# 125W in real terms) — chosen empirically via a standalone test render, not a standard reference value.
CRS = '+proj=laea +lat_0=-20 +lon_0=150 +datum=WGS84 +units=m'

def shift_lon(x, y, *rest):
    x2 = [(xx + 360 if xx < 0 else xx) for xx in x]
    return (x2, y, *rest) if rest else (x2, y)

def antimeridian_fix(gdf):
    """Shift every geometry's longitude into a continuous range before reprojecting. Required for
    this region — see module docstring. Must run on EPSG:4326 data, before .to_crs()."""
    gdf = gdf.copy()
    gdf['geometry'] = gdf['geometry'].apply(lambda geom: shp_transform(shift_lon, geom))
    return gdf.set_crs('EPSG:4326', allow_override=True)

CONTINENTAL_NATIONS = ['Australia', 'New Zealand', 'Papua New Guinea']
sub = pd.read_csv(HERE / 'subdivisions.csv')
sub = sub[sub.nation.isin(CONTINENTAL_NATIONS)].copy()
COLORS = sub.groupby('nation').color_hex.first().to_dict()

# ---------- admin-0/1 geometry ----------
ISO = {
    'AUS': 'Australia', 'NZL': 'New Zealand', 'PNG': 'Papua New Guinea',
    # folded into Australia — see module docstring
    'ATC': 'Australia', 'CSI': 'Australia', 'NFK': 'Australia',
}

a1_raw = gpd.read_file(NE / 'ne_10m_admin_1_states_provinces.geojson')
a1 = a1_raw[a1_raw.adm0_a3.isin(ISO)][['adm0_a3', 'name', 'geometry']].copy()
a1['nation'] = a1.adm0_a3.map(ISO)
a1 = antimeridian_fix(a1)
a1 = a1.to_crs(CRS)
a1['geometry'] = a1.buffer(0)
units = a1.dissolve(by=['nation', 'name'], as_index=False)

key = set(zip(units.nation, units.name))
need = set(zip(sub.nation, sub.subdivision_name))
missing = need - key
extra = key - need
assert not missing, f'CSV names not found in Natural Earth data: {missing}'
assert not extra, f'Natural Earth units not in CSV: {extra}'
print(f'{len(units)} polygons matched, {len(units.nation.unique())} nations')

def U(nation, names):
    names = list(names)
    for n in names:
        assert (nation, n) in need, (nation, n)
    return units[(units.nation == nation) & units.name.isin(names)].union_all()

def ALL(nation):
    return units[units.nation == nation].union_all()

nations = units.dissolve(by='nation', as_index=False)

# ---------- spheres (mirrors spheres.csv) — PARTIAL on this map by design. Only the slice of each
#            sphere that actually falls within Australia/NZ/PNG is drawn; the rest continues onto the
#            companion islands map. S2 (Micronesia) has no presence on this map at all, so it's
#            dropped entirely rather than drawn as an empty sphere. ----------
SPHERES = {
    'S1': dict(core=[ALL('Papua New Guinea')]),   # Melanesia: only PNG is on this map
    'S3': dict(core=[ALL('New Zealand')]),        # Polynesia: only NZ is on this map
}
for s in SPHERES.values():
    s['core'] = gpd.GeoSeries(s['core'], crs=CRS).union_all()
    s['extent'] = s['core']

STY = {  # color, hatch, extent linestyle, label
    'S1': ('#2E6B3E', '\\\\\\\\', (0, (6, 2)), 'Melanesia'),
    'S2': ('#2F6F8F', '////', (0, (2, 1.5)), 'Micronesia'),
    'S3': ('#8B3A6F', '....', (0, (1, 1.6)), 'Polynesia'),
}

# ---------- context layers ----------
a0_raw = gpd.read_file(NE / 'ne_10m_admin_0_countries.geojson')
a0 = antimeridian_fix(a0_raw).to_crs(CRS)

def P(lon, lat):
    p = Point(lon + 360 if lon < 0 else lon, lat)
    return gpd.GeoSeries([p], crs='EPSG:4326').to_crs(CRS).iloc[0]

# Framing uses Australia and Papua New Guinea in full, but only New Zealand's main North/South
# Island regions — its remote sub-antarctic and equatorial dependencies (Chathams, Kermadecs,
# Tokelau, Auckland/Campbell/Antipodes Islands, the Snares, Three Kings) sit thousands of km from
# the main islands and, if included, force a frame wide enough to leave Australia stranded off-center
# with a large empty-ocean gap to New Zealand. Excluding them from the framing calculation (they are
# still drawn wherever they fall — nothing is removed from the map itself, only from what decides the
# crop) puts Australia's centroid at roughly the frame's true center while New Zealand's main islands
# keep the same comfortable margin as everything else.
NZ_REMOTE = ['Tokelau', 'Kermadec Islands', 'Chatham Islands Territory', 'Antipodes Islands',
             'Campbell Islands', 'The Snares', 'Auckland Islands', 'Three Kings Islands']
framing = units[~((units.nation == 'New Zealand') & units.name.isin(NZ_REMOTE))]
core_all = framing.union_all()
minx, miny, maxx, maxy = core_all.bounds
padx, pady = 350e3, 350e3
xlim = (minx - padx, maxx + padx)
ylim = (miny - pady, maxy + pady * 1.1)

# ---------- draw: map occupies the left MAP_FRAC of the figure; the rest is a dedicated side panel
#            for the title and legend, so a 23-nation legend can never overlap the map content —
#            it floated over Papua New Guinea in the v1 in-map-legend layout this replaced. ----------
MAP_FRAC = 0.76
xr, yr = xlim[1] - xlim[0], ylim[1] - ylim[0]
W = 26
H = (MAP_FRAC * W) * yr / xr
fig = plt.figure(figsize=(W, H))
ax = fig.add_axes([0, 0, MAP_FRAC, 1])
ax.set_xlim(xlim); ax.set_ylim(ylim); ax.set_aspect('equal'); ax.axis('off')
SEA, NEIGH, INK = '#D7E3EA', '#ECE9E2', '#2B2B2B'
ax.add_patch(Rectangle((xlim[0], ylim[0]), xlim[1] - xlim[0], ylim[1] - ylim[0], facecolor=SEA, zorder=0))
others = a0[~a0.ADM0_A3.isin(ISO)]
others.plot(ax=ax, facecolor=NEIGH, edgecolor='#B9B4A8', linewidth=0.5, zorder=1)

def lighten(hexc, t=0.42):
    c = np.array(mpl.colors.to_rgb(hexc))
    return tuple(c + (1 - c) * t)

for _, r in nations.iterrows():
    gpd.GeoSeries([r.geometry], crs=CRS).plot(ax=ax, facecolor=lighten(COLORS[r.nation]),
                                              edgecolor='none', zorder=2)
units.boundary.plot(ax=ax, color='white', linewidth=0.4, alpha=0.9, zorder=3)

# national borders: white casing under dark line
nations.boundary.plot(ax=ax, color='white', linewidth=1.6, zorder=5)
nations.boundary.plot(ax=ax, color=INK, linewidth=0.45, zorder=5.1)
others.boundary.plot(ax=ax, color='#9A958A', linewidth=0.4, zorder=5)

for sid in ['S1', 'S3']:
    col, _, ls, _ = STY[sid]
    gpd.GeoSeries([SPHERES[sid]['extent']], crs=CRS).boundary.plot(
        ax=ax, color=col, linewidth=1.3, linestyle=ls, zorder=6)

# ---------- labels ----------
def T(lon, lat, s, **kw):
    p = P(lon, lat)
    return ax.text(p.x, p.y, s, zorder=kw.pop('zorder', 11), **kw)

halo = [mpl.patheffects.withStroke(linewidth=3, foreground='white', alpha=0.85)]

nat_kw = dict(family=SERIF, fontweight='semibold', color=INK, ha='center', va='center', path_effects=halo)
def NAT(lon, lat, s, fontsize, **extra):
    T(lon, lat, s, fontsize=fontsize, **{**nat_kw, **extra})

NAT(134, -25, 'AUSTRALIA', 26)
NAT(173.7, -39.0, 'NEW ZEALAND', 13, linespacing=1.05)  # moved off Wellington's capital label
NAT(143.5, -6.3, 'PAPUA NEW\nGUINEA', 11, linespacing=1.0)

sph_kw = dict(family=SERIF, style='italic', ha='center', va='center', path_effects=halo)
T(147, -7, 'Melanesia', color=STY['S1'][0], fontsize=13, **{k: v for k, v in sph_kw.items() if k not in ('fontsize',)})
T(174, -39.7, 'Polynesia', color=STY['S3'][0], fontsize=11, **{k: v for k, v in sph_kw.items() if k not in ('fontsize',)})

sea_kw = dict(family=SERIF, style='italic', fontsize=12, color='#6D8797', ha='center')
T(155, -32, 'Tasman Sea', **sea_kw)
T(150, -3, 'Coral Sea', **{**sea_kw, 'fontsize': 10})
T(115, -15, 'Indian Ocean', **sea_kw)
T(165, -22, 'South Pacific Ocean', **sea_kw)

# out-of-scope cross-references
oos_kw = dict(family=SERIF, style='italic', fontsize=9, color='#6E6A60', ha='center', linespacing=1.2)
T(125, -3, 'West Papua — see the\nMaritime Southeast Asia\nmap (Melanesia continues west)', **oos_kw)
T(160, -14, 'Melanesia continues east →\nSolomon Islands, Vanuatu, Fiji,\nNew Caledonia (see companion map)', **oos_kw)
T(178, -30, 'Polynesia continues →\nSamoa, Tonga, French Polynesia\nand more (see companion map)', **oos_kw)

# ---------- capitals ----------
CAPS = {
    'Canberra': (149.13, -35.28, 'r'), 'Wellington': (174.78, -41.29, 'r'),
    'Port Moresby': (147.18, -9.48, 'r'),
}
CITIES = {
    'Sydney': (151.21, -33.87, 'r'), 'Melbourne': (144.96, -37.81, 'r'),
    'Perth': (115.86, -31.95, 'l'), 'Brisbane': (153.03, -27.47, 'r'),
    'Auckland': (174.76, -36.85, 'l'), 'Christchurch': (172.64, -43.53, 'r'),
    'Lae': (147.00, -6.73, 'r'),
}
for d, cap in ((CAPS, True), (CITIES, False)):
    for n, (lon, lat, side) in d.items():
        p = P(lon, lat)
        ax.plot(p.x, p.y, marker='s' if cap else 'o', ms=6 if cap else 3.4,
                mfc=INK if cap else 'white', mec=INK, mew=0.8, zorder=12)
        dx = 16e3 if side == 'l' else -16e3
        ax.text(p.x + dx, p.y, n, ha='left' if side == 'l' else 'right', va='center',
                fontsize=9.5 if cap else 8, fontweight='bold' if cap else 'normal',
                family=SANS, color=INK, zorder=12, path_effects=halo)

# ---------- side panel: title + legend + footer, physically separate from the map so a 23-nation
#            legend can never overlap map content ----------
fig.patches.append(Rectangle((MAP_FRAC, 0), 1 - MAP_FRAC, 1, transform=fig.transFigure, color='#FBFAF7',
                             zorder=-1))
px = MAP_FRAC + 0.013
fig.text(px, 0.975, 'Oceania', family=SERIF, fontsize=28, fontweight='bold', color=INK, va='top')
fig.text(px, 0.938, "Australia, New Zealand &\nPapua New Guinea",
        family=SERIF, style='italic', fontsize=13, color='#444', va='top', linespacing=1.25)
fig.text(px, 0.895, 'Post-2083 successor states · first-order\nsubdivisions, whole units only\n'
        '1 of 2 companion maps — see also "Oceania —\nthe Pacific Islands"',
        family=SANS, fontsize=8.5, color='#666', va='top', linespacing=1.3)
fig.add_artist(plt.Line2D([px, 0.99], [0.830, 0.830], color='#B9B3A7', lw=0.8))

# ---------- legend ----------
handles, labels = [], []
def head(t):
    handles.append(Patch(visible=False)); labels.append(t)

head('$\\bf{Sovereign\\ nations}$  (hard borders)')
SOVEREIGN = ['Australia', 'New Zealand', 'Papua New Guinea']
for n in SOVEREIGN:
    handles.append(Patch(facecolor=lighten(COLORS[n]), edgecolor=INK, lw=0.3)); labels.append(n)
handles.append(Line2D([], [], color=INK, lw=0.8)); labels.append('National border')
handles.append(Line2D([], [], color='#BBB', lw=0.8)); labels.append('First-order subdivision')
head('$\\bf{Spheres}$  (real ethnography, overlay — partial on this map, see footer)')
desc = {'S1': 'Papua New Guinea only — rest of\nMelanesia is on the companion map',
        'S3': 'New Zealand only — rest of\nPolynesia is on the companion map'}
for sid in ['S1', 'S3']:
    col, hc, ls, name = STY[sid]
    handles.append(Line2D([], [], color=col, lw=1.4, ls=ls)); labels.append(f'{name} — {desc[sid]}')
handles.append(Line2D([], [], marker='s', ls='', mfc=INK, mec=INK, ms=5)); labels.append('National capital')

leg = fig.legend(handles, labels, loc='upper left', bbox_to_anchor=(px, 0.805), frameon=False,
                 fontsize=7.6, handlelength=2.2, handleheight=1.1, labelspacing=0.4, borderpad=0,
                 prop={'family': SANS, 'size': 7.6})
leg.set_zorder(20)

foot = ("This is the continental half of a two-map pair — the companion 'Oceania — the Pacific\n"
        "Islands' map covers the other 20 sovereign nations and territories. Australia and New\n"
        "Zealand both stay unified post-2083 — no partition case found (see the Oceania survey).\n"
        "Papua New Guinea keeps its real-world borders unchanged, same as every other sovereign\n"
        "Pacific nation on the companion map. Norfolk Island and the uninhabited Ashmore &\n"
        "Cartier/Coral Sea Islands are folded into Australia.\n"
        "Lambert azimuthal equal-area (lat₀ 20°S, lon₀ 150°E). Boundaries: Natural Earth 1:10m.\n"
        "Spheres: standard real-world Melanesia/Polynesia ethnography, drawn partially here — see\n"
        "spheres.csv and the companion map for the rest of each sphere's extent.")
fig.text(px, 0.028, foot, fontsize=7.3, family=SANS, color='#555', va='bottom', linespacing=1.4)
for t in ax.texts:
    t.set_clip_on(True)

for ext in ('png', 'svg'):
    fig.savefig(OUT / f'oceania_continental_map.{ext}', dpi=200, facecolor=SEA)
print('saved', OUT)
