# scholar

> Your public publication record, kept current on your own disk, with a People note for every coauthor.

**Contract:** Signal (owns `store/scholar.db`, landed from OpenAlex). Feeds `nouns`, the People layer.
**You provide:** your name, and your ORCID if you have one. No account or key is required.
**Depends on:** core only. Pairs with `nouns` and `research`.

## What your agent builds

- A **resolve step** that finds your author record in OpenAlex. Common names return several people; the agent shows the candidates with their institutions and topics, and you pick. It stores the id it was given, never a guess.
- A **sync** that pulls your works, their venues and citation counts, and every coauthor on each, into `store/scholar.db`. Running it twice adds nothing new.
- A **People note** in `vault/Entities/People/` for each coauthor: name, last known institution, OpenAlex id, and the works you share, each with its source.
- An **entity map** table joining each OpenAlex author id to its People note, so a coauthor found later through any other module lands on the same note.
- A short **report**: works by year, top coauthors, and top venues, ready for an annual review.

## The command

`/scholar` - sync your record, then answer questions about it (what did I publish in 2021, who do I write with most, what changed since last time).

## Notes

- Two records that might be the same coauthor are a question for you, not a merge.
- The record is only as good as OpenAlex's author matching. Missing or misattributed works are worth a look before you trust the totals.
