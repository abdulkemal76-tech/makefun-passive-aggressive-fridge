"""Notes From a Passive-Aggressive Fridge.

Writes the fridge's single passive-aggressive note to /output/entry.txt.
"""

from pathlib import Path

NOTE = "You opened me at 3:12 AM for the third night in a row. Even the pickles saw you. We all saw you."


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(NOTE, encoding="utf-8")


if __name__ == "__main__":
    main()
