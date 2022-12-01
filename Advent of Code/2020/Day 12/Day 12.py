import numpy as np

def read_file():
    with open(f"{__file__.strip('.py')} - Input.txt", "r") as f:
        return [(line[0], int(line[1:])) for line in f.read().split("\n")]

directions = {
    "N": [0, 1],
    "E": [1, 0],
    "S": [0, -1],
    "W": [-1, 0],
}

manhattan_distance = lambda position: abs(position[0]) + abs(position[1])

move = lambda position, displacement: np.add(position, displacement).tolist()

def rotate(position, rotation, angle):
    turns = (angle // 90) % 4

    for _ in range(turns):
        if rotation == "L":
            position[1] = -position[1]

        elif rotation == "R":
            position[0] = -position[0]

        position[0], position[1] = position[1], position[0]

    return position

def run(boat, waypoint, instruction, mode):
    if instruction[0] == "F":
        displacement = np.array(waypoint) * instruction[1]
        boat = move(boat, displacement)

    elif instruction[0] in ("L", "R"):
        waypoint = rotate(waypoint, instruction[0], instruction[1])

    else:
        displacement = np.array(directions[instruction[0]]) * instruction[1]

        if mode == 1:
            boat = move(boat, displacement)

        elif mode == 2:
            waypoint = move(waypoint, displacement)

    return boat, waypoint

def part_1(instructions):
    boat = [0, 0]
    waypoint = [1, 0]

    for instruction in instructions:
        boat, waypoint = run(boat, waypoint, instruction, 1)
    
    return manhattan_distance(boat)

def part_2(instructions):
    boat = [0, 0]
    waypoint = [10, 1]

    for instruction in instructions:
        boat, waypoint = run(boat, waypoint, instruction, 2)

    return manhattan_distance(boat)

instructions = read_file()

print(f"Part 1: {part_1(instructions)}")
print(f"Part 2: {part_2(instructions)}")
