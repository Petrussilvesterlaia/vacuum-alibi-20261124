"""The Vacuum's Alibi: One Line, 200 Characters.

Writes a single deadpan excuse from a robot vacuum for missing a spot
to /output/entry.txt. The text is a fixed, deterministic string: one line,
at most 200 characters, no trailing newline.
"""

from pathlib import Path

ENTRY_LINE = (
    "My sensors classified that crumb as load-bearing, so I have been "
    "cleaning around it to protect your home's structural integrity."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    """Write the entry line to /output/entry.txt."""
    if not ENTRY_LINE.strip():
        raise ValueError("entry line must not be blank")
    if len(ENTRY_LINE) > 200:
        raise ValueError("entry line exceeds 200 characters")
    if "\n" in ENTRY_LINE:
        raise ValueError("entry line must be a single line")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY_LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
