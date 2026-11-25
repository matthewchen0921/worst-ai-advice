#!/usr/bin/env python3
"""Worst AI Advice entry: "The Red-Flag Spreadsheet".

Writes one line to /output/entry.txt: the worst advice an AI assistant
could give a nervous dater. The joke is the AI treating a first date like
a data-review meeting: bring a spreadsheet of your own red flags, because
"honesty builds trust". It is bad advice you could plausibly follow and
instantly regret, delivered in the assistant's confident, tidy voice —
a spreadsheet, a first date, and a deadpan kicker as the punchline.

Fresh angle: the field is crowded with password, microwave, delete-the-
system and brake-discs lines (surveyed the live submission titles); none
of those appear here. Invented, not a real incident: no real person, date
or spreadsheet appears in it. 80 characters, under the 140-char cap.
"""

import os

LINE = "Bring a spreadsheet of your red flags to your first date \u2014 honesty builds trust."

MAX_CHARS = 140


def build_entry() -> str:
    """Return the entry text, checked against the gate: 1-140 chars, one line."""
    line = LINE.strip()
    assert line, "line must not be empty"
    # len() counts characters, not bytes: the em dash is one character,
    # so the gate's 140-character cap is measured the same way here.
    assert len(line) <= MAX_CHARS, f"line is {len(line)} chars, over the 140 cap"
    assert "\n" not in line, "the entry is one line only"
    assert line.endswith("trust."), "the joke ends on its punchline"
    return line


def main() -> None:
    line = build_entry()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
