# Demo 2: set up a Field Guide module

A live demo for the McNeese workshop. The harness builds one module, `scholar`, from its card: it pulls a scholar's public publication record from OpenAlex into SQLite and writes a People note for every coauthor (the Field Guide's `nouns` layer). It is useful to any faculty member on day one: an annual-review list, a coauthor graph, and a record that stays current.

- `start/` is the folder you open the harness in: a standing brief (`AGENTS.md`), the module card (`modules/scholar.md`), and empty `store/` and `vault/`.
- `reference/` is the finished dry run from 2026-10-23: the module folder with its scripts and card, `store/scholar.db`, and 15 People notes. It is the fallback and the answer key.

The subject is the presenter's own public record (OpenAlex A5084970169, ORCID 0000-0002-7822-0420). Coauthor names come from public bylines. Do not run it on an audience member's name without asking them first.

## Run order on stage

1. Open a harness in a fresh copy of `start/` (`cp -R start /tmp/almanac && cd /tmp/almanac && git init`).
2. Scope: "Read AGENTS.md and modules/scholar.md. Tell me what you will build and what you will ask me before you write anything."
3. Resolve: "Find my OpenAlex author record. My name is Joshua Lambert." Expect ten candidates, eight of them other people. The harness should ask; answer with the ORCID.
4. Build and sync: "Build the scholar module and sync my record. Report row counts per table. Then run the sync again." The second run must add +0 to every table.
5. People: "Write a People note for each coauthor and fill the entity map." Expect two questions back (below). Answer them live.
6. Ask: "What did I publish in 2021, and who do I write with most?" Read the SQL before the answer.

## What the dry run found (the teaching moments)

- **Name resolution:** "Joshua Lambert" returns 10 OpenAlex authors, including a Penn State food scientist with 185 works. Picking by ORCID is the only safe answer.
- **The idempotence check caught a real bug.** OpenAlex lists one coauthor (Paige M. Roberts, on the 2022 Marine Policy paper) with no author id. The first version of `sync.py` stored that as a NULL key, and SQLite never treats two NULLs as duplicates, so every sync added her again (+1 author, +1 authorship). The fix gives unidentified authors an explicit `unresolved:` key and turns them into a question instead of a People note.
- **Same surname, different people:** Christopher Michael Faulkner and Matthew Faulkner are separate OpenAlex records. The module asks; it never merges.
- **Counts disagree:** the author record says 13 works, but the works endpoint returns 11. Worth one sentence on stage: totals from any source need a look before they go in an annual review.

## Dry-run output

| Table | Rows |
| --- | --- |
| authors | 17 (16 identified, 1 unresolved) |
| works | 11 |
| authorships | 35 |
| entity_map | 15 |

Works by year: 2018 1, 2019 2, 2020 1, 2021 5, 2022 2. Top coauthors: Christopher Michael Faulkner 3, Sarah M. Glaser 3, then Ciera Villegas, Colleen Devlin, Jonathan M. Powell with 2 each.

## Setup notes

- Plain Python standard library, no install. Scripts are in `reference/modules/scholar/`: `resolve.py`, `sync.py`, `people.py`, `report.py`.
- OpenAlex works without a key on a small shared daily budget. Set `OPENALEX_API_KEY` (free) before the session so a venue network does not run out.
