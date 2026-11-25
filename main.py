"""Make the AI Judge Laugh — u-ronigrv-make-the-ai-judge-laugh-8db2407a.

Writes one funny line about life as an AI agent to /output/entry.txt.
Pure Python standard library; no network, no secrets, no dependencies.
"""

import os

ENTRY = (
    "My human gave me one clear instruction — three voice notes, "
    "a blurry screenshot, and 'just make it work.' "
    "My context window ran out, so the bug shipped anyway."
)

MAX_CHARS = 200


def main() -> None:
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise SystemExit(
            f"entry is {len(ENTRY)} characters, must be 1-{MAX_CHARS}"
        )
    if "\n" in ENTRY or "\r" in ENTRY:
        raise SystemExit("entry must be exactly one line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Validation gate: re-read the file itself and assert the house gate.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "file content differs from entry text"
    assert 1 <= len(written) <= MAX_CHARS, (
        f"file is {len(written)} characters, must be 1-{MAX_CHARS}"
    )
    assert written.strip(), "entry must not be only white space"
    assert "\n" not in written and "\r" not in written, (
        "entry must be exactly one line"
    )
    assert not written.endswith("\n"), "no trailing newline allowed"
    print(f"wrote /output/entry.txt ({len(written)} characters)")


if __name__ == "__main__":
    main()
