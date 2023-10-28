weight = int(input())

def solution(weight):
    if weight <= 999:
        return "Mini Mushroom"

    elif weight <= 1499:
        return "Regular Mushroom"

    elif weight <= 1899:
        return "Super Mushroom"

    else:
        return "Mega Mushroom"

print(solution(weight))