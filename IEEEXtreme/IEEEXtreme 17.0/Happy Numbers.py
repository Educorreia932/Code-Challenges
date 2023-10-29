from itertools import permutations

happy_numbers = set()
unhappy_numbers = set()

def is_happy_number(n):
    sequence = []
    
    while True:
        n = sum(int(x) ** 2 for x in str(n))

        if n in happy_numbers or n == 1:
            happy_numbers.update(sequence)

            return True

        if n in unhappy_numbers or n in sequence:
            unhappy_numbers.update(sequence)
            
            return False
        
        all_permutations = list(int("".join(x)) for x in permutations(str(n)))
        sequence += all_permutations

a, b = (int(x) for x in input().split())
total = 0

for n in range(a, b + 1):
    if is_happy_number(n):
        total += 1

print(total)