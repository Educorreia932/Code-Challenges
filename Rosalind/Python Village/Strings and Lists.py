def slice(string, ranges):
    a, b, c, d = ranges

    return string[a:b + 1] + " " + string[c:d + 1]
