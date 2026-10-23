"""Sync one author's works and coauthors from OpenAlex into store/scholar.db.

Usage: python3 sync.py A5084970169
"""

import datetime
import pathlib
import sqlite3
import sys

from openalex import get, short_id

ROOT = pathlib.Path(__file__).resolve().parents[2]
DB = ROOT / "store" / "scholar.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS authors (
  author_id TEXT PRIMARY KEY, name TEXT, orcid TEXT, institution TEXT);
CREATE TABLE IF NOT EXISTS works (
  work_id TEXT PRIMARY KEY, doi TEXT, title TEXT, year INT, type TEXT,
  venue TEXT, cited_by INT, is_open_access INT);
CREATE TABLE IF NOT EXISTS authorships (
  work_id TEXT REFERENCES works, author_id TEXT REFERENCES authors,
  position INT, PRIMARY KEY (work_id, author_id));
CREATE TABLE IF NOT EXISTS syncs (
  synced_at TEXT, subject_id TEXT, works_seen INT, works_new INT);
"""


def counts(con):
    return {t: con.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
            for t in ("authors", "works", "authorships")}


def main(subject):
    DB.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(DB)
    con.executescript(SCHEMA)
    before = counts(con)
    works = get("works", filter=f"author.id:{subject}", per_page=200,
                select="id,doi,title,publication_year,type,primary_location,cited_by_count,open_access,authorships")["results"]
    new = 0
    for w in works:
        wid = short_id(w["id"])
        venue = ((w.get("primary_location") or {}).get("source") or {}).get("display_name")
        new += con.execute("SELECT 1 FROM works WHERE work_id=?", (wid,)).fetchone() is None
        con.execute(
            "INSERT INTO works VALUES (?,?,?,?,?,?,?,?) ON CONFLICT(work_id) DO UPDATE SET cited_by=excluded.cited_by",
            (wid, w.get("doi"), w["title"], w["publication_year"], w["type"], venue,
             w["cited_by_count"], int(w["open_access"]["is_oa"])))
        for pos, a in enumerate(w["authorships"]):
            # OpenAlex sometimes lists an author it never identified (id is null). A NULL key
            # never dedupes in SQLite, so give it an explicit, stable placeholder instead.
            aid = short_id(a["author"]["id"]) or f"unresolved:{a['author']['display_name']}"
            inst = ", ".join(i["display_name"] for i in a.get("institutions") or []) or None
            con.execute("INSERT OR IGNORE INTO authors VALUES (?,?,?,?)",
                        (aid, a["author"]["display_name"], a["author"].get("orcid"), inst))
            con.execute("INSERT OR IGNORE INTO authorships VALUES (?,?,?)", (wid, aid, pos))
    con.execute("INSERT INTO syncs VALUES (?,?,?,?)",
                (datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"), subject, len(works), new))
    con.commit()
    after = counts(con)
    print(f"works seen {len(works)}, new {new}")
    for t in after:
        print(f"  {t}: {before[t]} -> {after[t]} (+{after[t] - before[t]})")


if __name__ == "__main__":
    main(sys.argv[1])
