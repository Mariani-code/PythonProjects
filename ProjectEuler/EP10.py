
limit = 2000000
is_prime_array = [True] * limit

def prime_sieve(prime_array):
    the_sum = 0
    for i in range(2, len(prime_array)):
        if prime_array[i]:
            the_sum += i
            k = i + i
            while k < len(prime_array):
                prime_array[k] = False
                k += i
    return the_sum


the_sum = prime_sieve(is_prime_array)

print(the_sum)
