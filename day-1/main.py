"""
    We need to get the secret code to enter the door.
    We have `input.txt` which contains the instructions for turning a dial to a safe.

"""

def main():

    # The dial starts by pointing at 50
    DIAL = 50

    with open('input.txt') as instructions:
        steps = (line.rstrip('\n') for line in instructions)
        for line in steps:
            print(line)

if __name__ == "__main__":
    main()



