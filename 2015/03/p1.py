from pathlib import Path

input_path = Path(__file__).parent / "input.txt"

with open(input_path, "r") as file:
    data = file.read().rstrip()
    pos = [0, 0]
    pos_list = ["0,0"]
    for x in data:
        if x == ">":
            pos[0] += 1
        if x == "<":
            pos[0] -= 1
        if x == "^":
            pos[1] += 1
        if x == "v":
            pos[1] -= 1
        pos_list.append(str(pos[0]) + "," + str(pos[1]))

houses = len(set(pos_list))

print("Part one:", houses)
