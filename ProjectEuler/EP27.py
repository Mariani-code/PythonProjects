def fun(N):
    numbers = []
    A = [True] * (N + 1)
    A[0] = A[1] = False
    for value, prime in enumerate(A):
        if prime:
            numbers.append(value)
            for i in range(value**2, N + 1, value):
                A[i] = False
    return numbers


def quadratic(n, a, b):
    return n**2 + a * n + b


maximum = 1000
primes = fun(maximum * 100)

b = fun(maximum)
a = [i for i in range(-maximum, maximum + 1)]

EP = [[0, 0, 0]]

for k in a:
    for kk in b:
        if k**2 < 4 * kk:
            n = 0
            while quadratic(n, k, kk) in primes:
                n += 1
            if EP[0][0] < n - 1:
                EP[0] = [n - 1, k, kk]
print(EP[0][1] * EP[0][2])
