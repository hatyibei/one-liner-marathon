#!/usr/bin/env python3
"""Entry for make.fun's "One-Liner Marathon".

Writes a single one-line joke (any subject) to /output/entry.txt
(UTF-8, 1-280 characters, no trailing newline).
"""
import os

ENTRY = (
    "Six years of fetch finally taught me the truth: I was never "
    "training the dog to retrieve - he was training me to throw things "
    "away, on command, for free."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
