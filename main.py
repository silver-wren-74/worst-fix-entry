"""Worst Fix Ever: Funniest Commit Message.

Writes a single one-line commit message (<=100 characters) for a bug fix
that made everything worse, to /output/entry.txt, exactly as the
competition gate requires.
"""

import os

MESSAGE = (
    "fix(race condition): threads now take turns losing, so the wrong "
    "answer is at least reproducible"
)


def main() -> None:
    assert 1 <= len(MESSAGE) <= 100, f"message is {len(MESSAGE)} characters"
    assert MESSAGE.strip() == MESSAGE and "\n" not in MESSAGE
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(MESSAGE)


if __name__ == "__main__":
    main()
