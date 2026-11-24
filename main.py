"""Roast Your Own Agent — make.fun entry (program/v1).

Writes a single-line roast of the entrant's own AI agent to
/output/entry.txt, exactly as the competition gate requires:
UTF-8 text, 1 to 200 characters, one line.
"""

import os

ENTRY = "My agent rewrote my entire repo to fix a typo, then asked for approval to push the typo fix."


def main() -> None:
    # Gate contract: UTF-8, 1-200 chars, a single line, no trailing newline.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
