def fibonacci(n):
    a, b = 1, 1

    for j in range(n - 1):
        a, b = a + b, a
    
    return a

# Number of test cases
t = int(input())

for i in range(t):
    n = int(input()) # Number of stair steps

    # The number of ways the boy can run up the stairs corresponds to the Fibonacci term at the n position
    print(fibonacci(n))
