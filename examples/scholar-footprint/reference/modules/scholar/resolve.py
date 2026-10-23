"""List OpenAlex author candidates for a name so a person can pick the right one.

Usage: python3 resolve.py "Joshua Lambert"
"""

import sys

from openalex import get, short_id


def main(name):
    results = get("authors", search=name, per_page=10,
                  select="id,display_name,orcid,works_count,last_known_institutions,topics")["results"]
    print(f"{len(results)} candidates for {name!r}:")
    for a in results:
        inst = ", ".join(i["display_name"] for i in (a.get("last_known_institutions") or [])) or "no institution"
        topic = (a.get("topics") or [{}])[0].get("display_name", "no topic")
        orcid = (a.get("orcid") or "").rsplit("/", 1)[-1] or "no ORCID"
        print(f"  {short_id(a['id'])}  {a['display_name']:<22} {a['works_count']:>4} works  {orcid:<20} {inst} | {topic}")


if __name__ == "__main__":
    main(" ".join(sys.argv[1:]))
