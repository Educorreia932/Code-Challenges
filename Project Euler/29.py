# Distinc powers

terms = set()

for a in range(2, 101):
    for b in range(2, 101):
        terms.add(a ** b)

answer = len(terms)

print(answer)

