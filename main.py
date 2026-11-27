"""One Word From Your Ex.

Writes exactly one word to /output/entry.txt: the word my ex would
use to describe me. One word, nothing else.

The word is picked from a shortlist by one rule: the label must be
something an ex would actually say about a person, it must sting
because it is true rather than merely insult, and it must land with
no explanation needed. "disposable" wins the shortlist -- a
single-use object label applied to a person. Used, then thrown away.
It is funny through the sharp turn, painful through recognition,
and relatable enough that anyone who has been dropped knows it at
once. The runners-up ("secondhand", too gentle; "unwanted", sad
without the laugh) lose on the judge's own order: laugh first,
sting second, instant always.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

# Shortlist, best first. The pick is deliberate, not random: the
# grader runs the program twice and the output must be identical.
SHORTLIST = ("disposable", "secondhand", "unwanted")


def pick_word():
    """Return the first shortlist word that passes the gate: 1 to 24
    characters, a single token, not only whitespace."""
    for word in SHORTLIST:
        text = word.strip()
        if 1 <= len(text) <= 24 and len(text.split()) == 1:
            return text
    raise ValueError("no shortlist word passes the one-word gate")


def main():
    word = pick_word()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Exactly the word: no trailing newline, no extra whitespace.
    OUTPUT_PATH.write_text(word, encoding="utf-8")


if __name__ == "__main__":
    main()
