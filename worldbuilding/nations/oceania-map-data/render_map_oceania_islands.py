"""
Oceania — THE PACIFIC ISLANDS MAP: the 20 nations/territories other than Australia, New Zealand and
Papua New Guinea (Stage 4).

Companion to render_map_oceania_continental.py. Split 2026-09-26, author-requested, from the original
single-map render_map_oceania.py (still present, kept as the reference/reproducibility copy — not part
of the two-map delivery). Same subdivisions.csv and spheres.csv as the continental map; this script
just filters to a different nation subset.

Inputs : subdivisions.csv, spheres.csv (this package), Natural Earth 10m admin-0/admin-1
         (github.com/nvkelso/natural-earth-vector, geojson/).
Output : oceania_islands_map.png (+ .svg)

11 real sovereign Pacific Island nations (Fiji, Kiribati, Marshall Islands, Micronesia, Nauru, Palau,
Samoa, Solomon Islands, Tonga, Tuvalu, Vanuatu) at their real-world borders — no partition decisions
needed, unlike Indonesia on the Maritime Southeast Asia map. Plus 9 pre-war colonial territories
(French/US/UK-administered, plus NZ-associated Cook Islands/Niue) carried as their own provisional
nations pending author review — every one of those rows is flagged in subdivisions.csv with a
⚠️ AUTHOR DECISION NEEDED note, since none of France/the UK/a single unified USA successor state
exists in this project yet to inherit them.

Antimeridian handling: this region straddles 180°E/W (Fiji, Tonga, Kiribati, and most of the eastern
Pacific chains all sit on or near the dateline). Every geometry is shifted (+360 to any longitude < 0)
before reprojection, turning the raw -180/180 split into one continuous coordinate range — verified
against a standalone test render before building the original single-map script this was split from;
without the shift, Fiji in particular renders as two disconnected fragments on opposite edges of the
frame. Do not remove this step.

Three-sphere cultural overlay (Melanesia / Micronesia / Polynesia): the standard, real, uncontested
anthropological three-region model for the Pacific — not this project's own construction, unlike most
of this project's other spheres. Drawn partially here — Papua New Guinea (Melanesia) and New Zealand
(Polynesia) are on the companion continental map instead, cross-referenced rather than redrawn. Kiribati
sits at a real, acknowledged boundary point between Micronesia and Polynesia; see spheres.csv's own
notes for how it was resolved.
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
CRS = '+proj=laea +lat_0=-15 +lon_0=175 +datum=WGS84 +units=m'

def shift_lon(x, y, *rest):
    x2 = [(xx + 360 if xx < 0 else xx) for xx in x]
    return (x2, y, *rest) if rest else (x2, y)

def antimeridian_fix(gdf):
    """Shift every geometry's longitude into a continuous range before reprojecting. Required for
    this region — see module docstring. Must run on EPSG:4326 data, before .to_crs()."""
    gdf = gdf.copy()
    gdf['geometry'] = gdf['geometry'].apply(lambda geom: shp_transform(shift_lon, geom))
    return gdf.set_crs('EPSG:4326', allow_override=True)

ISLANDS_NATIONS = ['Fiji', 'Solomon Islands', 'Vanuatu', 'New Caledonia', 'Micronesia',
                   'Marshall Islands', 'Palau', 'Nauru', 'Kiribati', 'Guam', 'Northern Mariana Islands',
                   'Samoa', 'American Samoa', 'Tonga', 'Tuvalu', 'Cook Islands', 'Niue',
                   'French Polynesia', 'Wallis and Futuna', 'Pitcairn Islands']
sub = pd.read_csv(HERE / 'subdivisions.csv')
sub = sub[sub.nation.isin(ISLANDS_NATIONS)].copy()
COLORS = sub.groupby('nation').color_hex.first().to_dict()

# ---------- admin-0/1 geometry ----------
ISO = {
    'FJI': 'Fiji', 'SLB': 'Solomon Islands', 'VUT': 'Vanuatu', 'NCL': 'New Caledonia',
    'FSM': 'Micronesia', 'MHL': 'Marshall Islands', 'PLW': 'Palau', 'NRU': 'Nauru', 'KIR': 'Kiribati',
    'GUM': 'Guam', 'MNP': 'Northern Mariana Islands', 'WSM': 'Samoa', 'TON': 'Tonga', 'TUV': 'Tuvalu',
    'COK': 'Cook Islands', 'NIU': 'Niue', 'PYF': 'French Polynesia', 'WLF': 'Wallis and Futuna',
    'PCN': 'Pitcairn Islands', 'ASM': 'American Samoa',
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

# ---------- spheres (mirrors spheres.csv) — PARTIAL on this map by design. Papua New Guinea
#            (Melanesia) and New Zealand (Polynesia) are on the companion continental map instead;
#            only the slice of each sphere that falls on this map is drawn here. Micronesia is fully
#            present on this map (none of its nations are on the continental map). ----------
MELANESIA_HERE = ['Solomon Islands', 'Vanuatu', 'Fiji', 'New Caledonia']  # PNG on companion map
MICRONESIA = ['Micronesia', 'Marshall Islands', 'Palau', 'Nauru', 'Guam', 'Northern Mariana Islands']
POLYNESIA_HERE = ['Samoa', 'American Samoa', 'Tonga', 'Tuvalu', 'Cook Islands', 'Niue',
                  'French Polynesia', 'Wallis and Futuna', 'Pitcairn Islands']  # NZ on companion map
# Kiribati is the one nation split between S2/S3 in real ethnography (see spheres.csv) — the whole
# country is drawn under Micronesia (its dominant/namesake identity, the Gilbert Islands), matching
# the whole-first-order-subdivision-equivalent convention used everywhere else in this project.
MICRONESIA_WITH_KIRIBATI = MICRONESIA + ['Kiribati']

SPHERES = {
    'S1': dict(core=[ALL(n) for n in MELANESIA_HERE]),
    'S2': dict(core=[ALL(n) for n in MICRONESIA_WITH_KIRIBATI]),
    'S3': dict(core=[ALL(n) for n in POLYNESIA_HERE]),
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

core_all = nations.union_all()
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

for sid in ['S1', 'S2', 'S3']:
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

NAT(161.8, -10.8, 'SOLOMON\nISLANDS', 8, linespacing=1.0)  # moved off Honiara's capital label
NAT(167, -16.5, 'VANUATU', 7)
NAT(178, -17.9, 'FIJI', 7)
NAT(165.5, -21.3, 'NEW\nCALEDONIA', 6.5, linespacing=1.0)
NAT(150.5, 7.0, 'MICRONESIA', 6.5)
NAT(168, 7.5, 'MARSHALL\nISLANDS', 6, linespacing=1.0)
NAT(134.5, 8.3, 'PALAU', 6)  # moved off Ngerulmud's capital-city label (was at nearly the same spot)
NAT(166.9, -0.5, 'NAURU', 5.5)
NAT(173.5, 1.5, 'KIRIBATI', 6.5)
NAT(144.3, 14.2, 'GUAM', 6)  # moved off Hagåtña's city label (was at the same coordinates)
NAT(145.7, 15.2, 'N. MARIANA\nIS.', 5.5, linespacing=1.0)
NAT(172, -13.8, 'SAMOA', 6.5)
NAT(189.2, -14.3, 'AMERICAN\nSAMOA', 5.5, linespacing=1.0)
NAT(184.6, -20.5, 'TONGA', 6.5)
NAT(179.2, -8.5, 'TUVALU', 5.5)
NAT(200, -19.8, 'COOK\nISLANDS', 5.5, linespacing=1.0)
NAT(190.1, -19.05, 'NIUE', 5)
NAT(213.5, -14.5, 'FRENCH\nPOLYNESIA', 8, linespacing=1.0)  # moved off Papeete's city label
NAT(183.9, -13.3, 'WALLIS &\nFUTUNA', 4.8, linespacing=0.95)
NAT(229.9, -25.1, 'PITCAIRN IS.', 5)

sph_kw = dict(family=SERIF, style='italic', ha='center', va='center', path_effects=halo)
T(163, -19, 'Melanesia', color=STY['S1'][0], fontsize=13, **{k: v for k, v in sph_kw.items() if k not in ('fontsize',)})
T(155, 10, 'Micronesia', color=STY['S2'][0], fontsize=13, **{k: v for k, v in sph_kw.items() if k not in ('fontsize',)})
T(195, -10, 'Polynesia', color=STY['S3'][0], fontsize=15, **{k: v for k, v in sph_kw.items() if k not in ('fontsize',)})

sea_kw = dict(family=SERIF, style='italic', fontsize=12, color='#6D8797', ha='center')
T(155, -32, 'Tasman Sea', **sea_kw)
T(150, -3, 'Coral Sea', **{**sea_kw, 'fontsize': 10})
T(115, -15, 'Indian Ocean', **sea_kw)
T(180, -30, 'South Pacific Ocean', **sea_kw)
T(190, 15, 'North Pacific Ocean', **sea_kw)

# out-of-scope cross-references
oos_kw = dict(family=SERIF, style='italic', fontsize=9, color='#6E6A60', ha='center', linespacing=1.2)
T(200, 21, 'Hawaii — see the North\nAmerica map (Polynesia\ncontinues north)', **oos_kw)
T(143, -22, 'Australia, New Zealand &\nPapua New Guinea —\nsee companion map', **oos_kw)

# ---------- capitals ----------
CAPS = {
    'Honiara': (159.95, -9.43, 'r'),
    'Port Vila': (168.32, -17.73, 'l'), 'Suva': (178.44, -18.14, 'r'),
    'Nouméa': (166.46, -22.28, 'l'), 'Palikir': (158.16, 6.92, 'l'),
    'Majuro': (171.38, 7.10, 'l'), 'Ngerulmud': (134.63, 7.50, 'r'),
    'Yaren': (166.92, -0.55, 'r'), 'Tarawa': (172.98, 1.33, 'l'),
    'Apia': (188.22, -13.83, 'l'), "Nuku'alofa": (184.78, -21.14, 'r'),
    'Funafuti': (179.22, -8.52, 'r'),
}
CITIES = {
    'Papeete': (210.6, -17.53, 'l'), 'Hagåtña': (144.75, 13.47, 'l'),
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
fig.text(px, 0.938, "The Pacific Islands",
        family=SERIF, style='italic', fontsize=15, color='#444', va='top', linespacing=1.25)
fig.text(px, 0.900, 'Post-2083 successor states · first-order\nsubdivisions, whole units only\n'
        '2 of 2 companion maps — see also "Oceania —\nAustralia, New Zealand & Papua New Guinea"',
        family=SANS, fontsize=8.5, color='#666', va='top', linespacing=1.3)
fig.add_artist(plt.Line2D([px, 0.99], [0.830, 0.830], color='#B9B3A7', lw=0.8))

# ---------- legend ----------
handles, labels = [], []
def head(t):
    handles.append(Patch(visible=False)); labels.append(t)

head('$\\bf{Sovereign\\ nations}$  (hard borders)')
SOVEREIGN = ['Solomon Islands', 'Vanuatu', 'Fiji', 'Micronesia', 'Marshall Islands', 'Palau', 'Nauru',
             'Kiribati', 'Samoa', 'Tonga', 'Tuvalu']
for n in SOVEREIGN:
    handles.append(Patch(facecolor=lighten(COLORS[n]), edgecolor=INK, lw=0.3)); labels.append(n)
head('$\\bf{Provisional\\ — author\\ review\\ needed}$')
PROVISIONAL = ['New Caledonia', 'Guam', 'Northern Mariana Islands', 'Cook Islands', 'Niue',
               'French Polynesia', 'Wallis and Futuna', 'Pitcairn Islands', 'American Samoa']
for n in PROVISIONAL:
    handles.append(Patch(facecolor=lighten(COLORS[n]), edgecolor=INK, lw=0.3)); labels.append(n)
handles.append(Line2D([], [], color=INK, lw=0.8)); labels.append('National border')
handles.append(Line2D([], [], color='#BBB', lw=0.8)); labels.append('First-order subdivision')
head('$\\bf{Spheres}$  (real ethnography, overlay — partial, see footer)')
desc = {'S1': 'Solomons, Vanuatu, Fiji, New\nCaledonia — PNG on companion map',
        'S2': 'Micronesia, Marshalls, Palau, Nauru,\nGuam, N. Marianas, Kiribati',
        'S3': 'Samoa, Am. Samoa, Tonga, Tuvalu,\nCooks, Niue, Fr. Polynesia, Wallis &\nFutuna, Pitcairn — NZ on companion map'}
for sid in ['S1', 'S2', 'S3']:
    col, hc, ls, name = STY[sid]
    handles.append(Line2D([], [], color=col, lw=1.4, ls=ls)); labels.append(f'{name} — {desc[sid]}')
handles.append(Line2D([], [], marker='s', ls='', mfc=INK, mec=INK, ms=5)); labels.append('National capital')

leg = fig.legend(handles, labels, loc='upper left', bbox_to_anchor=(px, 0.805), frameon=False,
                 fontsize=7.3, handlelength=2.2, handleheight=1.1, labelspacing=0.36, borderpad=0,
                 prop={'family': SANS, 'size': 7.3})
leg.set_zorder(20)

foot = ("This is the islands half of a two-map pair — the companion 'Oceania — Australia, New\n"
        "Zealand & Papua New Guinea' map covers those three. All 11 sovereign Pacific nations here\n"
        "keep their real-world borders unchanged. The nine 'provisional' nations above (former\n"
        "French/US/UK territories, plus NZ-associated Cook Islands/Niue) are flagged in\n"
        "subdivisions.csv for author review — no successor state for France/the UK/a unified USA\n"
        "exists yet in this project to inherit them; Guam's real strategic significance makes it\n"
        "the single highest-priority flag. Antimeridian-spanning region: geometry is shifted\n"
        "before reprojection (see script header) — do not remove that step when editing.\n"
        "Lambert azimuthal equal-area (lat₀ 15°S, lon₀ 175°E). Boundaries: Natural Earth 1:10m.\n"
        "Spheres: standard real-world Melanesia/Micronesia/Polynesia ethnography, drawn partially\n"
        "here — see spheres.csv and the companion map for the rest of each sphere's extent.")
fig.text(px, 0.028, foot, fontsize=7, family=SANS, color='#555', va='bottom', linespacing=1.4)
for t in ax.texts:
    t.set_clip_on(True)

for ext in ('png', 'svg'):
    fig.savefig(OUT / f'oceania_islands_map.{ext}', dpi=200, facecolor=SEA)
print('saved', OUT)
