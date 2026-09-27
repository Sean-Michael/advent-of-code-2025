"""
We need to get the secret code to enter the door.
We have `input.txt` which contains the instructions for turning a dial to a safe.
"""

import sys

DEBUG = True


def log(message: str) -> None:
    if DEBUG:
        print(message)


def main():
    file_name = sys.argv[1]

    with open(file_name) as instructions:
        rotations = [line.rstrip("\n") for line in instructions]

        # The dial starts by pointing at 50
        dial = 50
        zero_count = 0

        for r in rotations:
            prev_dial = dial
            turn = int(r[1:])
            if "R" in r[0]:
                dial += turn
                cycles, index = divmod(dial, 100)
                zero_count += cycles
                dial = index
            else:
                dial = (100 - dial) % 100 + turn
                cycles, index = divmod(dial, 100)
                zero_count += cycles
                dial = (prev_dial - turn) % 100

            log(f"- DIAL_START: {prev_dial}")
            log(f"- DIAL_ROTATED: {r} to {index}")

        print(zero_count)


if __name__ == "__main__":
    main()
