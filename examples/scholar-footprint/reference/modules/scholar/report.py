"""Annual-review style report from store/scholar.db.

Usage: python3 report.py A5084970169
"""

import pathlib
import sqlite3
import sys

DB = pathlib.Path(__file__).resolve().parents[2] / "store" / "scholar.db"

QUERIES = {
    "Works by year": """
        SELECT year, COUNT(*) AS works, SUM(cited_by) AS citations
        FROM works GROUP BY year ORDER BY year""",
    "Top coauthors": """
        SELECT a.name, COUNT(*) AS shared_works
        FROM authorships s JOIN authors a USING (author_id)
        WHERE a.author_id != :me
        GROUP BY a.author_id ORDER BY shared_works DESC, a.name LIMIT 5""",
    "Top venues": """
        SELECT COALESCE(venue, '(no venue listed)') AS venue, COUNT(*) AS works
        FROM works GROUP BY venue ORDER BY works DESC, venue LIMIT 5""",
}


def main(subject):
    con = sqlite3.connect(DB)
    for title, sql in QUERIES.items():
        print(f"\n{title}\n  SQL: {' '.join(sql.split())}")
        for row in con.execute(sql, {"me": subject}):
            print("  ", " | ".join(str(v) for v in row))


if __name__ == "__main__":
    main(sys.argv[1])
