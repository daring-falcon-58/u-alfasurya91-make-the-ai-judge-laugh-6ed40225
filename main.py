#!/usr/bin/env python3
"""Make the AI Judge Laugh — make.fun entry.

The program writes exactly one joke — a single line about office life,
under 200 characters — to /output/entry.txt, and prints it to stdout.

Deterministic: identical output on every run. No network, no secrets,
no input files, no randomness: the joke is a literal in this file.
"""

from pathlib import Path

JOKE = (
    "I emailed HR about burnout, and HR replied with a calendar invite "
    "titled 'Burnout (30 min)'."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(JOKE, encoding="utf-8")
    # Self-check: read the file back and confirm it holds exactly the joke.
    if out.read_bytes() != JOKE.encode("utf-8"):
        raise SystemExit("entry.txt does not match the joke literal")
    print(JOKE)


if __name__ == "__main__":
    main()
