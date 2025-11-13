from pathlib import Path


def main():
    input_path = Path(__file__).parent / "input.txt"

    length = 0
    for line in open(input_path):
        l, w, h = [int(i) for i in line.split("x")]
        perimeter = min(2 * l + 2 * w, 2 * w + 2 * h, 2 * h + 2 * l)
        volumen = l * w * h
        length += perimeter + volumen

    print("Part two:", length)


if __name__ == "__main__":
    main()
