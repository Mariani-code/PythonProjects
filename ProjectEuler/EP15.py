def factorial(n):
	if n == 0 or n == 1:
		return 1
	else:
		return n * factorial(n-1)

def combinations(n,r):
	return factorial(n) // ((factorial(r)) * (factorial(n-r)))

print(combinations(40,20))
