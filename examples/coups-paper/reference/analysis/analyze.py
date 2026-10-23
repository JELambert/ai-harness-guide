"""Decade counts, version drift, and the paper's failure-share claim, from data/raw/."""

import collections
import csv
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
OUT = ROOT / "analysis" / "out"
ARCHIVED = RAW / "powell_thyne_coups_final.txt"
CURRENT = RAW / "pt_20260829.csv"
REGIMES = RAW / "GWF_AllPoliticalRegimes.tab"


def load_coups(path):
    delim = "," if path.suffix == ".csv" else "\t"
    return [
        {"country": r["country"].strip('"'), "ccode": int(r["ccode"]), "year": int(r["year"]),
         "month": int(r["month"]), "day": int(r["day"]), "coup": int(r["coup"])}
        for r in csv.DictReader(path.open(encoding="utf-8"), delimiter=delim)
    ]


def key(r):
    return (r["ccode"], r["year"], r["month"], r["day"])


def decades(rows):
    counts = collections.Counter((r["year"] // 10 * 10, r["coup"]) for r in rows)
    with (OUT / "decades.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["decade", "successful", "failed", "total"])
        for d in sorted({dec for dec, _ in counts}):
            s, fl = counts[(d, 2)], counts[(d, 1)]
            w.writerow([d, s, fl, s + fl])
            print(f"  {d}s: {s} successful, {fl} failed")


def drift(old, new):
    o, n = {key(r): r for r in old}, {key(r): r for r in new}
    last_old_year = max(r["year"] for r in old)
    changes = (
        [("dropped", o[k]) for k in o if k not in n]
        + [("added", n[k]) for k in n if k not in o and k[1] <= last_old_year]
        + [("recoded", n[k]) for k in o if k in n and o[k]["coup"] != n[k]["coup"]]
    )
    with (OUT / "drift.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["change", "country", "year", "month", "day", "coup_now"])
        for change, r in sorted(changes, key=lambda c: (c[1]["country"], c[1]["year"], c[1]["month"])):
            w.writerow([change, r["country"], r["year"], r["month"], r["day"], r["coup"]])
    tally = collections.Counter(c for c, _ in changes)
    print(f"  dropped {tally['dropped']}, added (<= {last_old_year}) {tally['added']}, recoded {tally['recoded']}")


def failure_shares(rows):
    regime = {}
    for r in csv.DictReader(REGIMES.open(encoding="utf-8"), delimiter="\t"):
        regime[(int(r["cowcode"]), int(r["year"]))] = r["gwf_nonautocracy"].strip('"')
    autocracy = lambda r: regime.get((r["ccode"], r["year"])) == "NA"
    eras = [("1950-1989", 1950, 1989), ("1990-2014", 1990, 2014)]
    defs = {
        "all attempts": lambda rs: [r["coup"] for r in rs],
        "attempts against dictatorships": lambda rs: [r["coup"] for r in rs if autocracy(r)],
        "dictatorship country-years": lambda rs: list(
            {(r["ccode"], r["year"]): max(x["coup"] for x in rs if (x["ccode"], x["year"]) == (r["ccode"], r["year"]))
             for r in rs if autocracy(r)}.values()),
    }
    with (OUT / "failure_shares.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["definition", "era", "n", "failed_share"])
        for name, pick in defs.items():
            for label, lo, hi in eras:
                vals = pick([r for r in rows if lo <= r["year"] <= hi])
                share = vals.count(1) / len(vals)
                w.writerow([name, label, len(vals), f"{share:.3f}"])
                print(f"  {name}, {label}: n={len(vals)}, failed {share:.1%}")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    old, new = load_coups(ARCHIVED), load_coups(CURRENT)
    print(f"rows in: archived {len(old)}, current {len(new)}")
    print("coup attempts by decade (current release):")
    decades(new)
    print("archived vs current:")
    drift(old, new)
    print("paper says 48% failed 1950-89 and 63% after; archived file gives:")
    failure_shares(old)


if __name__ == "__main__":
    main()
