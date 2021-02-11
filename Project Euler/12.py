triangle_number = lambda n: n * (n + 1) // 2
number_divisors = lambda n: sum(1 for i in range(1, n + 1) if n % i == 0)

i = 1

while number_divisors(i) < 5:
    i = triangle_number(i)

print(i)
