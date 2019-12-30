result = 0

with open("Day 1 - Input.txt") as modules:
    for mass in modules:
        fuel = int(mass) // 3 - 2
        
        result += fuel

print(result)
