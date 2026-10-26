#!/usr/bin/env python3
"""Fetch geocentric Moon and Sun state vectors from JPL Horizons (DE441), ecliptic J2000, 10-minute steps.
Usage: python3 -I horizons_fetch.py <start_year> <n_years> <out_dir>
Writes <out_dir>/moon.npy and sun.npy (float64, columns x y z vx vy vz in km and km/s) and prints row counts.
The cache is large (about 75 MB per body per 30 years) and is NOT kept in the repository; rerun this script to rebuild it."""
import sys, os, urllib.request, urllib.parse, time
import numpy as np

URL = "https://ssd.jpl.nasa.gov/api/horizons.api"


def fetch(body, t0, t1):
    q = {"format": "text", "COMMAND": f"'{body}'", "OBJ_DATA": "'NO'", "MAKE_EPHEM": "'YES'", "EPHEM_TYPE": "'VECTORS'",
         "CENTER": "'500@399'", "START_TIME": f"'{t0}'", "STOP_TIME": f"'{t1}'", "STEP_SIZE": "'10m'",
         "REF_PLANE": "'ECLIPTIC'", "REF_SYSTEM": "'ICRF'", "VEC_TABLE": "'2'", "OUT_UNITS": "'KM-S'", "CSV_FORMAT": "'YES'"}
    url = URL + "?" + urllib.parse.urlencode(q, quote_via=urllib.parse.quote)
    for attempt in range(4):
        try:
            with urllib.request.urlopen(url, timeout=180) as r:
                txt = r.read().decode()
            break
        except Exception as e:
            print("retry", body, t0, e)
            time.sleep(5 * (attempt + 1))
    else:
        raise RuntimeError("fetch failed")
    a = txt.index("$$SOE") + 5
    b = txt.index("$$EOE")
    rows = []
    for line in txt[a:b].strip().split("\n"):
        f = line.split(",")
        rows.append([float(x) for x in f[2:8]])
    return np.array(rows)


if __name__ == "__main__":
    y0, ny, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    os.makedirs(out, exist_ok=True)
    for body, name in (("301", "moon"), ("10", "sun")):
        parts = []
        for y in range(y0, y0 + ny):
            # one calendar year per request; drop the duplicate first row of each later part
            a = fetch(body, f"{y}-01-01 00:00", f"{y+1}-01-01 00:00")
            parts.append(a if not parts else a)
            print(name, y, a.shape, flush=True)
        # concatenate, removing the duplicated boundary row (the stop time of year y is the start time of y+1)
        arr = np.concatenate([p[:-1] for p in parts[:-1]] + [parts[-1]])
        np.save(f"{out}/{name}.npy", arr)
        print("SAVED", name, arr.shape)
