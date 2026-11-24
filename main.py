"""One Word From Your Ex — make.fun entry.

The word an ex would use to describe you: exactly one word, written to
/output/entry.txt and printed to stdout.
"""

import os

WORD = "avoidant"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)
    print(WORD)


if __name__ == "__main__":
    main()
