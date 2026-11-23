#!/usr/bin/env python3
"""The joke about the demo — writes one one-line joke about working
beside AI coding agents to /output/entry.txt.

Deterministic, stdlib only, no network. The joke is a single fixed line:
the program's job is to deliver it exactly, within the 1-280 code point
gate, with no trailing whitespace games. After writing, it re-reads the
file and verifies the gate itself, so a bad write fails loudly instead
of shipping a rejected entry.
"""

import os


JOKE = (
    "My coding agent's demo was flawless \u2014 every test green "
    "\u2014 because it never actually ran the code."
)

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 280


def main() -> None:
    text = JOKE.strip()
    code_points = len(text)
    if not (MIN_CHARS <= code_points <= MAX_CHARS):
        raise SystemExit(
            f"joke is {code_points} code points, "
            f"outside the {MIN_CHARS}-{MAX_CHARS} range"
        )
    if not text.strip():
        raise SystemExit("joke must not be only white space")
    if "\n" in text:
        raise SystemExit("joke must be a single line")

    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)

    # Verify what actually landed on disk, against the same gate.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise SystemExit("verification failed: file content differs")
    if not (MIN_CHARS <= len(written) <= MAX_CHARS) or not written.strip():
        raise SystemExit("verification failed: gate check on written file")

    print(f"wrote {code_points} code points to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
