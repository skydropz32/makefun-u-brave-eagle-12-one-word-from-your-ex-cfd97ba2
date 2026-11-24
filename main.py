"""One Word From Your Ex.

Writes exactly one word -- the word my ex would use to describe me --
to /output/entry.txt. Deterministic: the same word, byte for byte,
on every run.

The word is "replaceable": the one word an ex reaches for when someone
has already been swapped out. It stings because it is true, it lands
instantly, and it needs no explanation.
"""

from pathlib import Path

WORD = "replaceable"


def main() -> None:
    # Gate self-check: exactly one word, 1-24 characters, no whitespace.
    assert WORD and len(WORD) <= 24, "word must be 1-24 characters"
    assert WORD.split() == [WORD], "entry must be exactly one word"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
