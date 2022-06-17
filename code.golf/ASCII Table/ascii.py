print(end=f"   {' '.join(map(str, range(2, 8)))}\n ")

print("-" * 13)

for i in range(16):
    print("%X" % i, end=": ")

    for j in range(2, 8):
        print("DEL" if i + j == 22 else chr(j * 16 + i), end=" ")

    print()
    