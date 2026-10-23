"""Write a People note per coauthor from store/scholar.db, and fill the entity map.

Usage: python3 people.py A5084970169

Never overwrites a note: an existing note gets new shared works appended, so hand edits survive.
Coauthors who share a surname are listed at the end as a question for the person.
"""

import collections
import pathlib
import re
import sqlite3
import sys
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[2]
DB = ROOT / "store" / "scholar.db"
PEOPLE = ROOT / "vault" / "Entities" / "People"


def slugify(name):
    ascii_name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", ascii_name.lower()).strip("-")


def main(subject):
    con = sqlite3.connect(DB)
    con.execute("CREATE TABLE IF NOT EXISTS entity_map (source TEXT, external_id TEXT, slug TEXT, PRIMARY KEY (source, external_id))")
    rows = con.execute("""
        SELECT a.author_id, a.name, a.institution, w.work_id, w.doi, w.title, w.year
        FROM authorships s JOIN authors a USING (author_id) JOIN works w USING (work_id)
        WHERE a.author_id != ? ORDER BY w.year""", (subject,)).fetchall()
    shared = collections.defaultdict(list)
    info = {}
    unresolved = sorted({name for aid, name, *_ in rows if aid.startswith("unresolved:")})
    rows = [r for r in rows if not r[0].startswith("unresolved:")]
    for aid, name, inst, wid, doi, title, year in rows:
        shared[aid].append((year, title, doi or f"openalex:{wid}"))
        info[aid] = (name, inst)

    PEOPLE.mkdir(parents=True, exist_ok=True)
    written = appended = 0
    for aid, (name, inst) in sorted(info.items(), key=lambda kv: kv[1][0]):
        slug = slugify(name)
        con.execute("INSERT OR IGNORE INTO entity_map VALUES ('openalex', ?, ?)", (aid, slug))
        path = PEOPLE / f"{slug}.md"
        lines = [f"- {y}: {t} ({src})" for y, t, src in shared[aid]]
        if path.exists():
            existing = path.read_text()
            missing = [l for l in lines if l not in existing]
            if missing:
                path.write_text(existing.rstrip("\n") + "\n" + "\n".join(missing) + "\n")
                appended += 1
            continue
        path.write_text(
            f"---\ntype: person\nclass: agent\nopenalex: {aid}\naliases: [\"{name}\"]\n---\n\n"
            f"# {name}\n\n"
            f"Coauthor. Last listed institution on a shared work: {inst or 'not listed'}.\n\n"
            f"## Works together\n\n" + "\n".join(lines) + "\n")
        written += 1
    con.commit()

    print(f"coauthors {len(info)}: notes written {written}, appended {appended}")
    print(f"entity_map rows: {con.execute('SELECT COUNT(*) FROM entity_map').fetchone()[0]}")
    for name in unresolved:
        print(f"QUESTION: OpenAlex has no author id for '{name}'. Create a People note by hand, or leave it?")
    by_surname = collections.defaultdict(list)
    for aid, (name, _) in info.items():
        by_surname[name.split()[-1].lower()].append(f"{name} ({aid})")
    for surname, names in by_surname.items():
        if len(names) > 1:
            print(f"QUESTION: same surname, same person or not? {'; '.join(names)}")
    dupes = con.execute("SELECT slug, COUNT(*) FROM entity_map GROUP BY slug HAVING COUNT(*) > 1").fetchall()
    for slug, n in dupes:
        print(f"QUESTION: {n} OpenAlex ids map to one note '{slug}': merge or split?")


if __name__ == "__main__":
    main(sys.argv[1])
