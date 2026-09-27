"""
We need to get the secret code to enter the door.
We have `input.txt` which contains the instructions for turning a dial to a safe.

"""

DEBUG = True


def main():

    with open("input.txt") as instructions:
        rotations = [line.rstrip("\n") for line in instructions]

        # The dial starts by pointing at 50
        DIAL = 50

        if DEBUG:
            print(f"DIAL START: {DIAL}")
        for r in rotations:
            if "R" in r[0]:
                DIAL += int(r[1:])
                if DEBUG:
                    print(f"RIGHT {r[1:]}, DIAL {DIAL}")
                if DIAL > 99:
                    DIAL = DIAL - 100
            else:
                DIAL -= int(r[1:])
                if DEBUG:
                    print(f"LEFT {r[1:]}, DIAL {DIAL}")
                if DIAL < 1:
                    DIAL = DIAL + 100
            if DEBUG:
                print(f"DIAL:{DIAL}")
        print(f"FINAL DIAL POSITION: {DIAL}")


if __name__ == "__main__":
    main()
