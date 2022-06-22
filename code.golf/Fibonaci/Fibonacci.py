def f(i, j):
    print(i)
    i < 2**19 and f(j, i + j)
        
f(0, 1)