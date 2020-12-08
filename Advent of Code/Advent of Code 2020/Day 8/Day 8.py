def read_file():
    with open(f"{__file__.strip('.py')} - Input.txt", "r") as f:
        return [[line.split(" ")[0], int(line.split(" ")[1])] for line in f.read().split("\n")]

def run(instructions):
    accumulator = 0
    instruction_counter = 0
    number_instructions = len(instructions)
    executed = []

    while instruction_counter not in executed and instruction_counter < number_instructions:
        executed.append(instruction_counter)

        instruction = instructions[instruction_counter]

        if instruction[0] == "acc":
            accumulator += instruction[1]
            instruction_counter += 1

        elif instruction[0] == "jmp":
            instruction_counter += instruction[1]

        else:
            instruction_counter += 1

    return accumulator, instruction_counter == number_instructions

def part_1(instructions):
    return run(instructions)[0]

def part_2(instructions):
    number_instructions = len(instructions)

    for i in range(number_instructions):
        if instructions[i][0] == "jmp":
            instructions[i][0] = "nop"
            accumulator, halted = run(instructions)
            instructions[i][0] = "jmp"

        elif instructions[i][0] == "nop":
            instructions[i][0] = "jmp"
            accumulator, halted = run(instructions)
            instructions[i][0] = "nop"

        else: 
            continue 

        if halted:
            break

    return accumulator

instructions = read_file()

print(f"Part 1: {part_1(instructions)}")
print(f"Part 2: {part_2(instructions)}")
