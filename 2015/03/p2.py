from pathlib import Path

input_path = Path(__file__).parent / "input.txt"

with open(input_path, "r") as file:
    data = file.read().rstrip()
    santa_pos = [0, 0]
    robo_pos = [0, 0]
    pos_list = ["0,0"]

    i = 0
    for x in data:
        i += 1
        if i % 2 == 0:
            if x == ">":
                santa_pos[0] += 1
            if x == "<":
                santa_pos[0] -= 1
            if x == "^":
                santa_pos[1] += 1
            if x == "v":
                santa_pos[1] -= 1
            pos_list.append(str(santa_pos[0]) + "," + str(santa_pos[1]))
        else:
            if x == ">":
                robo_pos[0] += 1
            if x == "<":
                robo_pos[0] -= 1
            if x == "^":
                robo_pos[1] += 1
            if x == "v":
                robo_pos[1] -= 1
            pos_list.append(str(robo_pos[0]) + "," + str(robo_pos[1]))

houses = len(set(pos_list))

print("Part two:", houses)
