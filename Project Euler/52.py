# Permuted multiples

n = 1

while True:
    digits = set(int(x) for x in str(n))

    for i in range(2, 7):
        if set(int(x) for x in str(n * i)) != digits:
            break

    else:
        print(n)
        break

    n += 1
    