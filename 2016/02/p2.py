from pathlib import Path

input_path = Path(__file__).parent / "input.txt"

with open(input_path, "r") as file:
    data = file.read().splitlines()

pad = [
    ["0", "0", "1", "0", "0"],
    ["0", "2", "3", "4", "0"],
    ["5", "6", "7", "8", "9"],
    ["0", "A", "B", "C", "0"],
    ["0", "0", "D", "0", "0"],
]

cur = (2, 0)

inst = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}

code = str()

for button in data:
    for i in button:
        x = max(0, min(cur[0] + inst[i][0], 4))
        y = max(0, min(cur[1] + inst[i][1], 4))
        if pad[x][y] != "0":
            cur = (x, y)
    code += pad[cur[1]][cur[0]]

print("Part two:", code)
