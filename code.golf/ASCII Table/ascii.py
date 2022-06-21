print("  ", *range(2, 8), "\n", "-" * 13)

for i in range(16):
    print("%X:" % i, *[("DEL", chr(j * 16 + i))[i + j < 22] for j in range(2, 8)])
