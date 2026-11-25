#!/usr/bin/env python3
"""Describe Your Ex in One Word — make.fun entry.

Writes a single-word verdict on an ex to /output/entry.txt.
Deterministic: no network, no randomness, no time dependence.
"""

import os


WORD = "Unsubscribed"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
