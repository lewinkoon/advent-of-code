from pathlib import Path


def main():
    input_path = Path(__file__).parent / "input.txt"

    with open(input_path, "r") as file:
        data = file.read().rstrip()

    floor = 0

    for character in data:
        if character == "(":
            floor += 1
        elif character == ")":
            floor -= 1
        else:
            print("File is corrupted.")
            break

    print("Part one:", floor)


if __name__ == "__main__":
    main()
