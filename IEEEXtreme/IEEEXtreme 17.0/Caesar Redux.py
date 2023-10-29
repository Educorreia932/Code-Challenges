def caesar_redux(shift, sentence):
    shift *= -1 if "the" in sentence.split() else 1
    cypher = lambda x: chr(((ord(x) + shift - ord("a")) % 26) + ord("a"))

    return "".join(cypher(x) if x != " " else " " for x in sentence)

number_cases = int(input())

for i in range(number_cases):
    shift = int(input())
    sentence = input()

    print(caesar_redux(shift, sentence))
