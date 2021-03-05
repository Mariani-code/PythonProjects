import time, math, multiprocessing, itertools

def isprime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for factor in range(3, int(math.sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True

def findfactors(n, primes):
    factors = []
    for p in primes:
        if p * p > n and n != 1:
            factors.append(n)
            break
        if n % p == 0:
            factors.append(p)
        while (n % p == 0):
            n //= p
    return factors

def allfactors(A, B, q, primes):
    L = findfactors(A, primes) + findfactors(B, primes)
    for p in primes:
        if p >= q:
            break
        if (p not in L):
            return False
    return True

def findq(p, Primes):
    for q in Primes:
        if p < q * q:
            return q

# This isn't particularly efficient, but there's not much to do
def computeinversetable(primes):
    inverse = {}
    for p in primes:
        inv = [0] * p
        for (r, s) in itertools.product(range(1, p), repeat=2):
            if r * s % p == 1:
                inv[r] = s
        inverse[p] = inv
    return inverse

def product(L):
    prod = 1
    for x in L:
        prod *= x
    return prod
# assumes moduli are relatively prime
# inverse is a dictionary of inverse tables for each m in moduli
# solutions is the list of right hand sides of the congruences
def chineseremaindertheorem(solutions, moduli, inverse):
    M = product(moduli)
    L = []
    for a, m in zip(solutions, moduli):
        b = M // m
        L.append(a * b * inverse[m][b % m])
    return (sum(L) % M)

def computeV(input):
    (p, primes, inverse) = input

    # Compute the q associated with p
    q = findq(p, primes)

    # First, let's look for a candidate of the form p=A+B
    for A in range((p + 1) // 2, p):
        B = p - A
        if ((math.gcd(A, B) == 1) and allfactors(A, B, q, primes)):
            return A

    # Now look for a candidate of the form p=A-B
    primesuptoq = [P for P in primes if P < q]
    candidates = []
    for solutions in itertools.product([0, p], repeat=len(primesuptoq)):
        c = chineseremaindertheorem(solutions, primesuptoq, inverse)
        if (c > p):
            candidates.append(c)

    return min(candidates)

def main():
    start = time.clock()

    # This sets up the multiprocessing pool to run on 8 cores
    pool = multiprocessing.Pool(8)

    # initialize list of primes
    primes = []
    for n in range(2, 3800):
        if isprime(n):
            primes.append(n)

    # initialize inverse table.  Only need the inverse table up to p=61,
    # which is the first 18 primes
    inverse = computeinversetable(primes[:18])

    # Create work to do -- can't use multiple input values for multiprocessing
    interleavedprimes = [(p, primes, inverse) for p in primes]

    # heavy lifting
    print(sum(pool.imap_unordered(computeV, interleavedprimes)))

    print("\nExecution time:  " + str((round(time.clock() - start, 2))))

if __name__ == '__main__':
    main()
