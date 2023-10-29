n, m = map(int, input().split())

rhymes_list = []
for i in range(n):
    rhymes_list.append(input().split())

input()

last_words = []
for i in range(m):
    last_words.append(input().split()[-1:][0].lower())


def solve_rhymes(rhymes, last_words):
    rhyme_scheme = ""
    rhyme_labels = {}

    for i, rhyming_words in enumerate(rhymes):
        for word in rhyming_words:
            rhyme_labels[word] = chr(ord("A") + i)

    for word in last_words:
        if word in rhyme_labels:
            rhyme_scheme += rhyme_labels[word]
        else:
            rhyme_scheme += "X"

    return rhyme_scheme


rhyme_scheme = solve_rhymes(rhymes_list, last_words)

dict_letter = {}
curr_letter = "A"
new_rhyme_scheme = ""
for char in rhyme_scheme:
    if char not in dict_letter:
        dict_letter[char] = curr_letter
        new_rhyme_scheme += curr_letter
        curr_letter = chr(ord(curr_letter) + 1)
    else:
        new_rhyme_scheme += dict_letter[char]


print(new_rhyme_scheme)
