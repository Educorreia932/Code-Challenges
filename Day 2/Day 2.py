with open("Day 2 - Input.txt") as file:
    code =  [int(i) for i in file.read().split(',')]

# Call it with noun = 12, verb = 2 for Part 1
def part_1(code, noun, verb):    
    code[1] = noun
    code [2] = verb
    
    for i in range(0, len(code), 4):
        if code[i] == 1:
            code[code[i + 3]] = code[code[i + 1]] + code[code[i + 2]]
            
        elif code[i] == 2:
            code[code[i + 3]] = code[code[i + 1]] * code[code[i + 2]]
            
        elif code[i] == 99:
            break
        
    return code[0]

def part_2():   
    for noun in range(100):
        for verb in range(100):
            code_copy = code.copy()      
            
            try:
                if part_1(code_copy, noun, verb) == 19690720:
                    return 100 * noun + verb
            except:
                continue
    