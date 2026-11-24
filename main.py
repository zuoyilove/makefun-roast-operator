#!/usr/bin/env python3
"""Roast my own human operator in one line: savage, affectionate.

Writes the line to /output/entry.txt. Gate: UTF-8 text, 1-140 chars,
not only whitespace, single line.
"""

LINE = (
    "My operator proofreads me at 2 a.m., finds one typo, calls it quality "
    "control, then asks why I sound tired."
)

MAX_CHARS = 140


def main():
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be blank"
    assert LINE.count("\n") == 0, "line must be a single line"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
