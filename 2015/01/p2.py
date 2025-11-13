from pathlib import Path


def main():

    input_path = Path(__file__).parent / "input.txt"

    with open(input_path, "r") as file:
        data = file.read().rstrip()

    floor = 0
    position = 0

    for i, character in enumerate(data):
        if character == "(":
            floor += 1
        elif character == ")":
            floor -= 1
        else:
            print("File is corrupted.")
            break

        if floor == -1:
            position = i + 1
            break

    print("Part two:", position)


if __name__ == "__main__":
    main()
