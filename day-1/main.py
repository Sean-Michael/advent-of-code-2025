"""
We need to get the secret code to enter the door.
We have `input.txt` which contains the instructions for turning a dial to a safe.

"""

import sys

DEBUG = True


"""
    The cases that increase the zero count:
    1. We land on Zero
    2. We pass zero during a rotation

    Landing on Zero means that DIAL == 0 after calculating quotient - easy
    Passing zero can happen in a few more cases:
        i.) A full rotation passes zero as many times as rotated, this is the quotient
        ii.) A partial rotation from left or right halves of the dial, this is trickier .. 
            Going right, this is also when the quotient is nonzero since we use the remainder to find the index
            Going left, it's negative but the absolute value should help us there..  

    So how to not double count ..
    - if we started on 0 we don't count that zero, but if we do a full rotation and land on zero, just count that once
    - if we do multiple full rotations and land on zero at the end, count the intermediate
    - so only count the cycles as zero count if we land on zero if they are greater than 1
    - like two rotations, starting from a previous zero index, and ending on zero would add two to the count, not 4 or 3
    - so count a full cycle only if the ending index is zero
    - Do we even need to count the previous zero? i actually don't think so, cause if we end up with DIAL there again, it's rigth
"""


def log(message: str) -> None:
    if DEBUG:
        print(message)


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

            cycles, index = divmod(DIAL, 100)

            log(f"- DIAL_START: {PREV_DIAL}")
            log(f"- DIAL_ROTATED: {r} to {index}")

            # Increment based on the quotient
            ZERO_COUNT += abs(cycles)

            # if we started at zero, and went left
            if PREV_DIAL == 0 and cycles < 0:
                ZERO_COUNT -= 1  # the first 'cycle' doesn't count

            # if we land on zero without a full rotation
            if cycles == 0 and index == 0:
                ZERO_COUNT += 1

            DIAL = index

        print(ZERO_COUNT)


if __name__ == "__main__":
    main()
