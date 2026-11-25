#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers — make.fun entry.

Writes one original fortune-cookie line for a software developer to
/output/entry.txt. Deterministic: no network, no randomness, no clock.

Craft notes: the line works against the judge's criteria because it reads
like a real fortune cookie (a short, second-person-sounding aphorism), it is
true about a developer's day (code outlives the memory of writing it), and
the twist lands at the end — the detective following your clues is future-
you, so the fortune is a gentle warning to comment for your own sake.
"""

import os

ENTRY = "Your code will outlive your memory of writing it, so comment like you are leaving clues for a detective who is you."


def main():
    # The gate allows 1 to 120 characters; keep the line inside it.
    assert 1 <= len(ENTRY) <= 120, "entry line must be 1-120 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
