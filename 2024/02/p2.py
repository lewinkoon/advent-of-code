from pathlib import Path

input_path = Path(__file__).parent / "input.txt"


def check(list):
    inc = [list[i + 1] - list[i] for i in range(len(list) - 1)]
    if set(inc) <= {1, 2, 3} or set(inc) <= {-1, -2, -3}:
        return True
    return False


reports = 0
with open(input_path, "r") as file:
    for line in file:
        levels = [int(x) for x in line.split()]
        filtered = [levels[:i] + levels[i + 1 :] for i in range(len(levels))]
        cond = [check(i) for i in filtered]
        if any(cond):
            reports += 1
    print("Part Two:", reports)
