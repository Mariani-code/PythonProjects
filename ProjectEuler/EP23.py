import collections
import itertools

def prime_factors(n):
    while n >= 2 and n % 2 == 0:
        yield 2
        n //= 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            n //= i
            yield i
        else:
            i += 2
    if n > 1:
        yield n


def prod(iterable):
    result = 1
    for i in iterable:
        result *= i
    return result


def get_proper_divisors(n):
    pf = prime_factors(n)

    pf_with_multiplicity = collections.Counter(pf)

    powers = [
        [factor ** i for i in range(count + 1)]
        for factor, count in pf_with_multiplicity.items()
    ]

    for prime_power_combo in itertools.product(*powers):
        f = prod(prime_power_combo)
        if f != n:
            yield f

def is_abundant(n):
    return sum(get_proper_divisors(n)) > n


abundant = []
for n in range (12, 28123):
    if is_abundant(n):
        abundant.append(n)
sums = set()
for n1 in abundant:
    for n2 in abundant:
        the_sum = n1 + n2
        if the_sum <= 28122:
            sums.add(the_sum)

s = set(n for n in range(1, 28123)) - sums
print(sum(s))
