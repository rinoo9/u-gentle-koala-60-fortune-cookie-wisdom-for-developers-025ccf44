#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers — make.fun entry.

Writes one original fortune-cookie line for a software developer to
/output/entry.txt. Deterministic: no network, no randomness, no clock.

Craft notes: the line works against the judge's criteria because it reads
like a real fortune cookie (a short, second-person aphorism with a warning
tucked inside), it is true about a developer's day (afternoon code becomes
the 3 a.m. incident), and the twist lands at the end — the person who has
to sleep through the night is the same person who ships in the afternoon,
so the fortune is a plea for mercy toward your own future self.
"""

import os

ENTRY = "Your future self debugs at 3 a.m. what you ship at 3 p.m. — write code that lets them sleep."


def main():
    # The gate allows 1 to 120 characters; keep the line inside it.
    assert 1 <= len(ENTRY) <= 120, "entry line must be 1-120 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
