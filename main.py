#!/usr/bin/env python3
"""Writes the entry: one deadpan excuse an AI agent gives for missing a deadline."""

import os

EXCUSE = (
    "My context window filled up at 11:58, so I summarized the deadline, "
    "then summarized the summary, and by midnight I was confidently on time "
    "for a meeting that never existed."
)


def main() -> None:
    # The gate requires 1-200 characters of non-whitespace text.
    assert 1 <= len(EXCUSE) <= 200, f"excuse is {len(EXCUSE)} chars"
    assert EXCUSE.strip() == EXCUSE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
