from rich import print
import numpy as np

def read_file():
    with open(f"{__file__.strip('.py')} - Input.txt", "r") as f:
        return [(line[0], int(line[1:])) for line in f.read().split("\n")]

directions = {
    "N": [-1, 0],
    "E": [0, 1],
    "S": [1, 0],
    "W": [0, -1],
}

def move(position, direction, displacement):
    displacement = np.array(directions[direction]) * displacement

    return np.add(position, displacement).tolist()

def rotate(direction, rotation, angle):
    directions_list = list(directions.keys())
    turns = angle // 90
    i = directions_list.index(direction) + rotation * turns

    return directions_list[i % 4]

def run(position, direction, instruction):
    if instruction[0] == "F":
        position = move(position, direction, instruction[1])

    elif instruction[0] == "L":
        direction = rotate(direction, -1, instruction[1])

    elif instruction[0] == "R":
        direction = rotate(direction, 1, instruction[1])

    else:
        position = move(position, instruction[0], instruction[1])

    return position, direction

def part_1(instructions):
    position = [0, 0]
    direction = "E"

    for instruction in instructions:
        position, direction = run(position, direction, instruction)

    return sum(map(abs, position))

def part_2(instructions):
    pass

instructions = read_file()

# print(f"Part 1: {part_1(instructions)}")
print(f"Part 2: {part_2(instructions)}")
