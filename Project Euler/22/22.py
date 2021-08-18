# Names scores

import string

name_score = lambda name, index: sum(string.ascii_uppercase.index(character) + 1 for character in name) * index

input = open("p022_names.txt", "r").read()
input = sorted(input.replace("\"", "").split(","))

result = sum(map(name_score, input, range(1, len(input) + 1)))

print(result)
