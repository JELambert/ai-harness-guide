# Setup

Two steps. You do the first by hand. The harness does the second with you.

## 1. Install a harness and sign in (by hand)

Pick one. Both work with everything in this folder.

- **Claude Code:** follow the [quickstart](https://code.claude.com/docs/en/quickstart), or use Claude Code inside the [Claude desktop app](https://claude.com/download). Needs a paid Claude plan.
- **Codex:** use the [Codex app](https://developers.openai.com/codex/app) or the [Codex CLI](https://developers.openai.com/codex/cli). Needs a ChatGPT plan that includes Codex.

Then download this folder (green **Code** button on GitHub, then **Download ZIP**), unzip it, and open the harness in it.

Check your institution's guidance on approved AI tools and data before using real work files.

## 2. Paste this file in, and let it walk you through the rest

Copy everything below the line into the harness and press Enter.

---

You are helping me set up an AI harness for the first time. I am not a programmer. Go one step at a time, tell me what each step is for in plain language, check that it worked before moving on, and stop to ask me whenever something needs my decision or my password. Do not install anything without telling me first.

1. Tell me which harness and operating system I am on, and confirm you can read the files in this folder. Summarize README.md and AGENTS.md for me in three sentences.
2. Check whether Git is installed. If not, help me install it, then set my name and email for Git. Explain in one sentence why it matters (it is your undo button).
3. Check whether you can read the Word document in semester/teaching. If not, help me install what you need to read .docx files.
4. Run semester/research/get-paper.sh to download the reading, and confirm the PDF opened.
5. Make one commit of the current state of this folder so I have a save point, and show me how to undo back to it.
6. Run the first prompt in prompts.md, then stop and ask me what I want to try next.

---

## When you are ready for your own work

Copy [`starter/AGENTS.md`](starter/AGENTS.md) into a new folder for one real piece of your work, and ask the harness to interview you and fill it in.

When one folder is not enough, the [Almanac Field Guide](https://github.com/JELambert/almanac-field-guide) has its own paste-in setup that builds the larger version: one folder holding your repositories, notes, PDFs, and data.
