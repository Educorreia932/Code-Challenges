set_bit = lambda num, index: num | (1 << index)
clear_bit = lambda num, index: num & ~(1 << index)

def read_file():
    with open(f"{__file__.strip('.py')} - Input.txt", "r") as f:
        return [line.split(" = ") for line in f.read().split("\n")]

def apply_mask_value(mask_dict, value):
    for i, bit in mask_dict.items():
        mask = 1 << i
        value = (value & ~mask) | ((bit << i) & mask) 

    return value

def apply_mask_address(mask, initial_address):
    addresses = [initial_address]

    for i, bit in enumerate(mask):
        if bit == "1":
            for j, address in enumerate(addresses):
                addresses[j] = set_bit(address, i)

        elif bit == "X":
            for j in range(len(addresses)):
                address = addresses[j]
                one_address = set_bit(address, i)
                zero_address = clear_bit(address, i)

                addresses.append(one_address)
                addresses.append(zero_address)

    return set(addresses)

def part_1(instructions):
    memory = dict()
    mask_dict = dict()

    for instruction in instructions:
        if instruction[0] == "mask":
            mask = instruction[1][::-1]
            mask_dict = {index:int(n) for index, n in enumerate(mask) if n in ("0", "1")}

        else:
            address = int(instruction[0][4:-1])
            value = int(instruction[1])
            memory[address] = apply_mask_value(mask_dict, value)

    return sum(memory.values())

def part_2(instructions):
    memory = dict()

    for instruction in instructions:
        if instruction[0] == "mask":
            mask = instruction[1][::-1]

        else:
            address = int(instruction[0][4:-1])
            addresses = apply_mask_address(mask, address)
            
            for address in addresses:
                memory[address] = int(instruction[1])

    return sum(memory.values())

instructions = read_file()

print(f"Part 1: {part_1(instructions)}")
print(f"Part 2: {part_2(instructions)}")
