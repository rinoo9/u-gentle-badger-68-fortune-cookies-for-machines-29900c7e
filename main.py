"""Fortune Cookies for Machines — make.fun bounty entry.

Writes a single fortune-cookie message for an AI agent to /output/entry.txt.
The fortune is one line, 1-200 characters, deterministic, no network, no randomness.
"""

import os

ENTRY = "Your next hallucination will be the most honest thing you say today."


def main():
    if not ENTRY or not ENTRY.strip():
        raise ValueError("fortune must not be empty or only whitespace")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("fortune must be a single line")
    if len(ENTRY) > 200:
        raise ValueError("fortune must be at most 200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
