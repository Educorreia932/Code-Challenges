def countSubstrings(s):
    result = set()

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            temp = s[i:j]

            if temp == temp[::-1]:
                result.add((temp, i, j))

    return result

def overlap(s1, s2):
    return max(0, min(s1[2], s2[2]) - max(s1[1], s2[1]))

T = int(input()) # Number of test cases

for i in range(T):
    S = input()

    substrings = sorted(countSubstrings(S), key=lambda s: len(s[0]), reverse=True)
        
    length_sum = 0
    flag = False

    for j in range(len(substrings)):
        for k in range(len(substrings)):
            s1 = substrings[j]
            s2 = substrings[k]
            length = len(s1[0]) + len(s2[0])

            if length > length_sum and not overlap(s1, s2):
                length_sum = length

                if k - i == 1:
                    flag = True
                    break

        if flag:
            break

    print(length_sum)
