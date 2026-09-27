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
        DIAL = 50
        ZERO_COUNT = 0

        for r in rotations:
            PREV_DIAL = DIAL
            if "R" in r[0]:
                DIAL += int(r[1:])
            else:
                DIAL -= int(r[1:])

            quotient, remainder = divmod(DIAL, 100)
            print(f"divmod({DIAL}, 100), quotient={quotient}, remainder={remainder}")
            if PREV_DIAL != 0 and quotient != 0 and remainder != 0:
                ZERO_COUNT += abs(quotient)
                print("DIAL PASSES ZERO")
            DIAL = remainder

            if DIAL == 0:
                ZERO_COUNT += 1
                print("DIAL POINTS AT ZERO")
        print(ZERO_COUNT)


if __name__ == "__main__":
    main()
