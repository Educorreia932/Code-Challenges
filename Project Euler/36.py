# Double-base palindromes

answer = 0

def is_palindromic(n):
    n = str(n)

    return n == n[::-1] 

for i in range(1000000):
    if is_palindromic(i) and is_palindromic(bin(i)[2:]):
        answer += i

print(answer)
