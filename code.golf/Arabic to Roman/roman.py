import sys

for number in map(int, sys.argv[1:]):
	num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
	i = 12
	s = ""

	while number:
		s += 'I IVV IXX XLL XCC CDD CMM '[i * 2::2].strip() * (number // num[i])

		number %= num[i]

		i -= 1

	print(s)
