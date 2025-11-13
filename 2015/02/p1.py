from pathlib import Path


def main():
    input_path = Path(__file__).parent / "input.txt"

    surface = 0
    for line in open(input_path):
        l, w, h = [int(i) for i in line.split("x")]
        area = 2 * l * w + 2 * w * h + 2 * h * l
        slack = min(l * w, w * h, h * l)
        surface += area + slack

    print("Part one:", surface)


if __name__ == "__main__":
    main()
