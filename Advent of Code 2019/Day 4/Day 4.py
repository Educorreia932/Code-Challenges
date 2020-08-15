with open("Day 4 - Input.txt") as file:
    input = file.read().split('-')
    begin = int(input[0])
    end = int(input[1])
    
def meets_criteria_1(number):
    previous_i = -1
    
    result = False
    
    for i in str(number):
        if previous_i == i:
            result = True
        
        elif int(previous_i) > int(i):
            return False
        
        previous_i = i
        
    return result
    
def meets_criteria_2(number):
    

def part_1():
    result = 0
    
    for i in range(begin, end):
        if meets_criteria(i):
            result += 1
            
    return result
        
def part_2():
    