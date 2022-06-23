for i in range(1, 101):
    print("Fizz" * (i % 3 < 1) + "Buzz" * (i % 5 < 1) or i)
