N = int(input())

result = 0

for i in range(N):
    s = input()

    if not s[0].isupper():
        continue

    

    s1 = set(s.split(" "))

    if len(s1) == 1:
        continue

    

    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    flag = False

    for word in s1:
        for char in word:
            if char in vowels:
                flag = True

    if not flag:
        continue

    flag = True

    digits ={"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

    for word in s1:
        for char in word:
            if char in digits:
                flag = False

    if not flag:
        continue

    result += 1

print(result)
