# Sum square difference

sum_squares = lambda n: sum(i ** 2 for i in range(n + 1))
square_sum = lambda n: sum(range(n + 1)) ** 2

result = square_sum(100) - sum_squares(100)

print(result)
