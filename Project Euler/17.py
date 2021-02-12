# Number letter counts

import inflect

solution = 0
p = inflect.engine()

for i in range(1, 1001):
    n = p.number_to_words(i)
    letters = len(n.replace(" ", "").replace("-", ""))

    solution += letters

print(solution)
