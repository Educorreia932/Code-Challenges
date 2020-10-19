def fibonacci(n):
    a, b = 1, 1

    for j in range(n - 1):
        a, b = a + b, a
    
    return a

last_digits = []

# Number of test cases
t = int(input())

# The last digit of a fibonacci sequence number repeats every 60th term
for i in range(60):
    last_digit = str(fibonacci(i))[-1]
    last_digits.append(last_digit) 

for i in range(t):
    m = int(input())

    print(last_digits[m % 60])

