# u-xvader-the-funniest-honest-appliance-error-adec4450: The Funniest Honest Appliance Error
# One line of at most 200 characters: the funniest honest error message an
# appliance could show. The program writes the line to /output/entry.txt
# (or $MAKEFUN_OUTPUT_DIR).
import os

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# Gate: the entry is one line of 1-200 characters.
MAX_CHARS = 200

# The joke is the truth of the fault: an unbalanced washing-machine load
# really does make the machine walk across the floor — and it really is
# the owner's loading that caused it. No pun bolted on.
MESSAGE = "Unbalanced load. I am about to walk across the laundry room. This is on you."


def validate_line(line):
    assert 1 <= len(line) <= MAX_CHARS, f"message is {len(line)} chars, must be 1-200"
    assert line.strip(), "message must not be only whitespace"
    assert "\n" not in line, "message must be a single line"


def main():
    validate_line(MESSAGE)

    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(MESSAGE)


if __name__ == "__main__":
    main()
