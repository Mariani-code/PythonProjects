def is_pandigital(n, limit):
    # is_pandigital('12345', 5)
    seen = set()
    required = set()
    [required.add(x) for x in range(1, limit+1)]
    for digit in n:
        if int(digit) in seen:
            return False
        seen.add(int(digit))
    # Sets are sorted by default
    if seen == required:
        # All found
        return True
    else:
        return False

largest = 0
for n in range(1, 10001):
    product = ""
    for m in range(1, 20):
        prod = n*m
        product += str(prod)
        if is_pandigital(product, 9):
            print("Found {} ({}*{})".format(product, n, m))
            if int(product) > largest:
                largest = int(product)
            break

print("Largest: {}".format(largest))
