from pathlib import Path

input_path = Path(__file__).parent / "input.txt"

with open(input_path, "r") as file:
    data = file.read().splitlines()

pad = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

cur = (1, 1)

inst = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}

code = str()

for button in data:
    for x in button:
        cur = (max(0, min(cur[0] + inst[x][0], 2)), max(0, min(cur[1] + inst[x][1], 2)))
    code += pad[cur[1]][cur[0]]

print("Part one:", code)
