list_of_x = []

def parse_path_instruction(grid, current_position, instruction, last):
    direction = instruction[0]
    length = int(instruction[1:])
    
    x = current_position[0]
    y = current_position[1]
    
    for i in range(length):
        if (direction == 'R'):
            current_position[0] += 1
            
            if i == length - 1 and last:
                grid[y][x + i + 1] = '+'
                
            elif grid[y][x + i + 1] != '.':
                grid[y][x + i + 1] = 'X'
                list_of_x.append([x - i - 1, y])
                
            else:
                grid[y][x + i + 1] = '-'
                
        elif (direction == 'L'):
            current_position[0] -= 1
            
            if i == length - 1 and last:
                grid[y][x - i - 1] = '+'
                
            elif grid[y][x - i - 1] != '.':
                grid[y][x - i - 1] = 'X'
                list_of_x.append([x - i - 1, y])
                
            else:
                grid[y][x - i - 1] = '-'
            
        elif (direction == 'U'):
            current_position[1] += 1
            
            if i == length - 1 and last:
                grid[y + i + 1][x] = '+'
                
            elif grid[y + i + 1][x] != '.':
                grid[y + i + 1][x] = 'X'
                list_of_x.append([x, y + i + 1])
                
            else:
                grid[y + i + 1][x] = '|'
            
        elif (direction == 'D'):
            current_position[1] -= 1
            
            if i == length - 1 and last:
                grid[y - i - 1][x] = '+'
                
            elif grid[y - i - 1][x] != '.':
                grid[y - i - 1][x] = 'X'
                list_of_x.append([x, y - i - 1])
                
            else:
                grid[y - i - 1][x] = '|'
        
def print_grid(grid):
    grid = grid[::-1]
    
    for i in range(len(grid)):
        line = ""

        for j in range(len(grid)):
            line += grid[i][j]
            
        print(line)
        
def manhattan_distance(point_1, point_2):
    return abs(point_1[0] - point_2[0]) + abs(point_1[1] - point_2[1])
        
def part_1():
    current_position = [0, 0]
    
    size = 200

    grid = [['.' for x in range(size)] for y in range(size)]
    
    x = current_position[0]
    y = current_position[1]
    
    with open("Day 3 - Input.txt") as file:
        wire_1_instructions =  file.read().split("\n")[0].split(',')
    
    with open("Day 3 - Input.txt") as file:
        wire_2_instructions =  file.read().split("\n")[1].split(',')
    
    for instruction in wire_1_instructions:
        last = wire_1_instructions[-1] != instruction
        
        parse_path_instruction(grid, current_position, instruction, last)
        
    current_position = [0, 0]
        
    for instruction in wire_2_instructions:
        last = wire_2_instructions[-1] != instruction
        
        parse_path_instruction(grid, current_position, instruction, last)
    
    grid[y][x] = 'o'
    
    print_grid(grid)
    
    result = manhattan_distance([0, 0], list_of_x[0])
    
    for x in list_of_x[1:]:
        if manhattan_distance([0, 0], x) < result:
            result = manhattan_distance([0, 0], x)
            
    return result
    
print(part_1())

