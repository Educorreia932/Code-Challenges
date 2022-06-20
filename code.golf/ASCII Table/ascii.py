print("  ", *range(2, 8), "\n", "-" * 13)

for i in range(16):
    print("%X:" % i, *["DEL" if i + j == 22 else chr(j * 16 + i) for j in range(2, 8)])
    