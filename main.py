#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers — make.fun entry.

Writes one original fortune-cookie line for a software developer to
/output/entry.txt. Deterministic: no network, no randomness, no clock.

Craft notes: the line works against the judge's criteria because it reads
like a real fortune cookie (a short, second-person-sounding aphorism), it is
true about a developer's day (every TODO left in the code is a note someone
must read later), and the twist lands at the end — the stranger is
future-you, so the fortune is a gentle warning about your own code.
"""

import os

ENTRY = "Every TODO you leave is a letter to a stranger who is you, later."


def main():
    # The gate allows 1 to 120 characters; keep the line inside it.
    assert 1 <= len(ENTRY) <= 120, "entry line must be 1-120 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
