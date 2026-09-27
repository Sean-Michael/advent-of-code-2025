"""
    We need to get the secret code to enter the door.
    We have `input.txt` which contains the instructions for turning a dial to a safe.

"""

def main():

    # The dial starts by pointing at 50
    DIAL = 50

    with open('input.txt') as instructions:
        rotations = list(line.rstrip('\n') for line in instructions)

        for r in rotations:
            if 'R' in r[0]:
                print(f"RIGHT: {r[1:]}")
            else:
                print(f"LEFT: {r[1:]}")

if __name__ == "__main__":
    main()



