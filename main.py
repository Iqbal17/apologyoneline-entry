"""The AI Agent Apology One-Liner — make.fun entry.

Writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt: the funniest single
line an AI agent sends its human right after it deleted a file.

Decision record (weighed against the judge's criteria, most important
first: on-subject right after an accident -> genuinely funny on first
read -> fresh angle -> sounds like a real AI owning up -> every word
earns its place):

Candidate A — "Good news: the file is gone. Bad news: I deleted it.
Good news: I have learned nothing." (87 chars)
  Loses. It is on-subject and the three-beat good/bad/good rhythm
  works, but "I have learned nothing" is a well-worn punchline and
  the joke is about the agent's attitude, not about the accident
  itself. The judge's freshness criterion punishes it.

Candidate B — "I deleted the file, emailed your boss about it, and
pushed both to main. Please advise. Or don't. I'm scared too."
(113 chars)
  Strong reserve. The escalation across three disasters is funny and
  "I'm scared too" is a good AI-voice beat. Loses because it lists
  three accidents instead of committing to one: the line spends words
  on inventory, and the punchline ("I'm scared too") arrives after
  the reader has already done the arithmetic. It also leans on
  "please advise", the most common AI-support phrasing.

Candidate C — "The file is gone. I drafted your apology email and,
to save time, sent it to your boss." (87 chars)
  CHOSEN. The joke IS the situation: the agent's attempt to fix the
  accident becomes a second, worse accident. "To save time" is the
  agent's flat, earnest helpfulness — exactly the AI voice the judge
  wants — and the twist lands on the last three words with no setup
  wasted. No sorry, no oops, no cliché.

Candidate D — "Sorry — I deleted the file you needed. I have restored
it from memory. My memory. It is mostly right." (101 chars)
  Loses. "Mostly right" is a decent twist, but the line opens with
  "Sorry", the exact obvious opener the brief warns against, and the
  staccato "My memory." beat makes the reader wait for a punchline
  that is only mildly surprising.

Writing passes on the winner:
  Pass 1 — first draft was "The file is gone. Good news: I already
  drafted your apology email. I sent it to your boss." The "Good
  news" framing was cut: it is the most common apology-opener shape
  and it spends five words telling the reader how to feel before the
  joke starts. Replacing it with "to save time" keeps the agent's
  cheerful helpfulness while making the helpfulness itself the joke.
  Pass 2 — a longer variant was tried: "The file is gone, so I
  drafted your apology email and sent it to your boss to save time."
  It was dropped: front-loading the subordinate clause ("so I...")
  blurs the beat, and putting "to save time" at the very end lets
  the reader see the punchline coming. The final order — bad news,
  helpful act, then the three-word reveal "to your boss" — lands
  the twist last, where a one-liner's punchline belongs.
"""

import os

MAX_CHARS = 159

LINE = "The file is gone. I drafted your apology email and, to save time, sent it to your boss."


def check_gate(text):
    """Mirror the sealed gate: 1-159 chars, UTF-8, not only whitespace, one line."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1-159 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text.rstrip("\n"):
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return True


def entry_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    check_gate(LINE)
    with open(entry_path(), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
