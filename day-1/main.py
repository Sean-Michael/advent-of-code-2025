"""
We need to get the secret code to enter the door.
We have `input.txt` which contains the instructions for turning a dial to a safe.
"""

import sys

DEBUG = True


def main():
    file_name = sys.argv[1]

    with open(file_name) as instructions:
        rotations = [line.rstrip("\n") for line in instructions]

        # The dial starts by pointing at 50
        dial = 50
        zero_count = 0

        for r in rotations:
            prev_dial = dial
            direction = r[0]
            turn = int(r[1:])

            if direction == "R":
                dial += turn
                cycles, index = divmod(dial, 100)
                zero_count += cycles
                dial = index
            else:
                dial = (100 - dial) % 100 + turn
                cycles, index = divmod(dial, 100)
                zero_count += cycles
                dial = (prev_dial - turn) % 100

            if DEBUG:
                print(f"- DIAL_START: {prev_dial}\n- DIAL_ROTATED: {r} to {index}")

        print(zero_count)


if __name__ == "__main__":
    main()
