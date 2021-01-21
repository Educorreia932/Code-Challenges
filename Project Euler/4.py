# Largest palindrome product

is_palindrome = lambda k : str(k)[::-1] == str(k)

result = 0

for i in range(100, 999):
    for k in range(100, 999):
        n = i * k

        if is_palindrome(n) and n > result:
            result = n

print(result)
