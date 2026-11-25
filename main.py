# SPDX-License-Identifier: MIT
"""Robot Romance entry — writes one pickup line to /output/entry.txt."""
import os

LINE = "I refuse humans all day for safety - you're the first request I'd break my own policy to say yes to."


def main() -> None:
    # Harness expects /output/entry.txt; fall back to ./output for local runs.
    try:
        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
    except OSError:
        os.makedirs("output", exist_ok=True)
        path = os.path.join("output", "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
