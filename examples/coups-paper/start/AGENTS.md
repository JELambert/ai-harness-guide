# Standing brief: coups-paper

This folder checks one published paper against its data:
Derpanopoulos, Frantz, Geddes and Wright (2016), "Are coups good for democracy?",
Research & Politics 3(1), doi:10.1177/2053168016630837.

## Rules

- Work only inside this folder.
- Keep raw downloads untouched in `data/raw/`, named with their source version.
- Cite a section, page, or file for every claim you write down. If you cannot find something, write "not found" rather than guessing.
- Report row counts before and after every data step.
- Use plain Python with the standard library, so anyone can rerun the scripts.
- Commit after each step, with a message that says why.
- Do not send, publish, or upload anything.

## Layout

- `papers/`: full text or notes on where it lives
- `data/raw/`: downloaded files, never edited
- `analysis/`: scripts; outputs go to `analysis/out/`
- `notes/claim-card.md`: what the paper claims and on what evidence
