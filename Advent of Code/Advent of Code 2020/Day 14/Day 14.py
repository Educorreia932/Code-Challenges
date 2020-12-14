from rich import print

def read_file():
    with open(f"{__file__.strip('.py')} - Input.txt", "r") as f:
        return [line.split(" = ") for line in f.read().split("\n")]

def apply_mask(mask_dict, value):
    for i, bit in mask_dict.items():
        mask = 1 << i
        value = (value & ~mask) | ((bit << i) & mask) 

    return value

def part_1(lines):
    memory = dict()
    mask_dict = dict()

    for instruction in lines:
        if instruction[0] == "mask":
            mask = instruction[1][::-1]
            mask_dict = {index:int(n) for index, n in enumerate(mask) if n in ("0", "1")}

        else:
            address = int(instruction[0][4:-1])
            value = apply_mask(mask_dict, int(instruction[1]))
            memory[address] = value

    return sum(memory.values())

lines = read_file()

print(f"Part 1: {part_1(lines)}")
# print(f"Part 2: {part_2(timestamps)}")