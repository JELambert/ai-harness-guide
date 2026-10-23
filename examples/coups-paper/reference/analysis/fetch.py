"""Download the archived and current coup data into data/raw/ and report what arrived."""

import csv
import json
import pathlib
import urllib.request

RAW = pathlib.Path(__file__).resolve().parent.parent / "data" / "raw"
ARCHIVE_DOI = "doi:10.7910/DVN/3IC00L"
WANTED = {"powell_thyne_coups_final.txt", "GWF_AllPoliticalRegimes.tab"}
CURRENT_URL = "https://jonathanmpowell.com/wp-content/uploads/2026/08/pt_20260829.csv"


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "curl/8"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read()


def archive_files():
    meta = json.loads(get(f"https://dataverse.harvard.edu/api/datasets/:persistentId/?persistentId={ARCHIVE_DOI}"))
    for f in meta["data"]["latestVersion"]["files"]:
        name = f["dataFile"]["filename"]
        if name in WANTED:
            yield name, f"https://dataverse.harvard.edu/api/access/datafile/{f['dataFile']['id']}"


def describe(path):
    delim = "," if path.suffix == ".csv" else "\t"
    rows = list(csv.DictReader(path.open(encoding="utf-8", errors="replace"), delimiter=delim))
    versions = sorted({r.get("version", "").strip('"') for r in rows} - {""})
    print(f"{path.name}: {len(rows)} rows, version {', '.join(versions) or 'n/a'}")


def main():
    RAW.mkdir(parents=True, exist_ok=True)
    targets = list(archive_files()) + [("pt_20260829.csv", CURRENT_URL)]
    for name, url in targets:
        dest = RAW / name
        dest.write_bytes(get(url))
        describe(dest)


if __name__ == "__main__":
    main()
