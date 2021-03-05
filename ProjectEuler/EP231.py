import math
import itertools
import functools
import operator
def sieve(n):
    is_prime=[True]*(n+1)
    is_prime[0]=False
    is_prime[1]=False
    result=[]
    for i,prime in enumerate(is_prime):
        if prime:
            result.append(int(i))
            for j in range(i*i,n+1,i):
                is_prime[j]=False
        else:
            continue
    return result

def factors(n,primes):
    if primes is None: primes=sieve(int(math.sqrt(n+1)))
    factors={}
    for prime in primes:
        while n%prime==0:
            n=n//prime
            if prime not in factors:
                factors[prime]=0
            factors[int(prime)]+=1
    if n!=1:
        factors[n]=1
    return factors

def binomial(n,k):
    primes=sieve(5000)
    res={}
    for i in range(n-k+1,n+1):
        if i%100000==0: print(i)
        f=factors(i,primes)
        for fac in f:
            if fac not in res:
                res[fac]=f[fac]
            else:
                res[fac]+=f[fac]
    print(res)
    for i in range(1, k+1):
        f = factors(i, primes)
        for fac in f:
            res[fac] -= f[fac]
    return sum([res[i]*i for i in res])
print(binomial(20000000,5000000))
