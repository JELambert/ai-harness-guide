# Standing brief: a small almanac

This folder follows the Almanac Field Guide layout (github.com/JELambert/almanac-field-guide):
`modules/` holds capability, `store/` holds SQLite data, `vault/` holds markdown notes.

## Rules

- Build each module from its card in `modules/<name>.md`. The card is the spec; check the result against it.
- Data lands in `store/<name>.db`. Notes land in `vault/`. Nothing lives only in a web service.
- Resolve a name before writing it. If two records could be the same person, or one name could be several people, ask. Never merge people without a yes.
- Every fact in a People note carries its source (an OpenAlex work id or DOI).
- Report row counts per table after every sync. A second sync with no new data must add zero rows.
- Use plain Python with the standard library.
- Commit after each step, with a message that says why.
- Do not send, publish, or upload anything.
