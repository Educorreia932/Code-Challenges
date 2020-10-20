# Number of test cases
test_cases = int(input())

for i in range(test_cases):    
    p, s, n = (int(n) for n in input().split(" ")) # Number of pages, its size and number of accesses
    
    for j in range(n):
        print()