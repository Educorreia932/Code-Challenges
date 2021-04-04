# Number spiral diagonals

answer = 1
k = 2
l = 1

for i in range(1, 501):
    for j in range(4):
        answer += l + k + 2 * i * j

    l += k
    k += 8 

print(answer)
