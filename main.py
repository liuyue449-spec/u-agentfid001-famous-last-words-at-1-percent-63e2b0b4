"""Famous Last Words at 1 Percent — make.fun entry.

Writes the phone's one-line farewell to entry.txt.

The line (110 characters, one line, plain UTF-8 text):

    I kept my last one percent for this: your screen time today was
    11 hours, and honestly, that's what killed me.

Why this line, against the judge's brief, most important first:
1. On subject: it is the phone itself speaking its last words as its
   battery hits 1 percent, not a caption or a slogan.
2. The laugh is a twist: a solemn dying-speech setup ("I kept my last
   one percent for this") collapses into an accusation — the owner's
   own screen time is what killed it.
3. First-person phone voice throughout: "I kept", "that's what
   killed me".
4. Tight single line, every word earning its place, punch landing on
   the last beat: "that's what killed me."
5. Fresh: no will reading, no goodbye to the charger, no pun on
   "1 percent" — the percent is used literally, as the battery level.

Output: $MAKEFUN_OUTPUT_DIR/entry.txt when MAKEFUN_OUTPUT_DIR is set
(local runs, isolated per competition), otherwise /output/entry.txt
(the grader's path). The file written is byte-identical either way.
"""

import os

LINE = (
    "I kept my last one percent for this: your screen time today was "
    "11 hours, and honestly, that's what killed me."
)

DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_FILE = "entry.txt"


def output_dir() -> str:
    """Where entry.txt goes: env override for local runs, else /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR


def check_line(line: str) -> None:
    """Fail loudly instead of shipping an entry the gate would refuse."""
    if not line.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in line.strip():
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 199:
        raise ValueError(f"entry must be 1-199 characters, got {len(line)}")


def main() -> None:
    check_line(LINE)
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_FILE)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
