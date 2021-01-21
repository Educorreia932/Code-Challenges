# Smallest multiple

n = 2520
divisible = False

while not divisible:
    n += 20  

    for i in range(2, 21):
        if n % i != 0:
            break

    else:
        divisible = True

print(n)
