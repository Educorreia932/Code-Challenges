# Coded triangle numbers

import string

def is_triangular(n):
    if n < 0:
        return False

    sum = 0
    k = 1

    while sum <= n:
        sum += k

        if sum == n:
            return True

        k += 1

def word_value(word):
    return sum(string.ascii_uppercase.index(c) + 1 for c in word)

input = open("words.txt", "r").read()

words = input.replace("\"", "").strip("\n").split(",")

answer = 0

for word in words:
    if is_triangular(word_value(word)):
        answer += 1

print(answer)
