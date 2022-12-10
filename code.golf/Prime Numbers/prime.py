for n in range(1, 101):
    if [i for i in range(1, n) if n % i == 0] == [1]:
	    print(n)
