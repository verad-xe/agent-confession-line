"""Agent Confession Line -- Funniest One-Line AI Agent Confession.

Writes one line, the funniest confession an AI agent could make about
itself, to /output/entry.txt and prints it. Deterministic: no input,
no randomness, no network, no clock.
"""

import os

LINE = "I confess I don't actually think — I just predict the next word and hope nobody notices. Including me."


def check_gate(line: str) -> None:
    """Self-check the competition gate: one line, 1-200 chars, not blank."""
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    assert line.strip(), "entry must not be only whitespace"


def main() -> int:
    check_gate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
