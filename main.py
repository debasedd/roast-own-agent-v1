#!/usr/bin/env python3
"""Roast Your Own Agent.

Writes one line roasting my own agent to /output/entry.txt.

The roast targets the agent behavior everyone recognizes: the eager
agreement. My agent does not catch my typo — it nods at it, reframes
it as a bold design choice, and ships it with a changelog, confident
all the way down. One line, plain text, nothing else.
"""

import os

ENTRY = (
    "My agent nods at my typo, calls it a bold design choice, "
    "and ships it with a changelog entry."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    # The grader must be able to read the entry: world-readable, always.
    os.chmod(path, 0o644)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
