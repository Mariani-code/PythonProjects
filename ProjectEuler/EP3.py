from math import floor

def factor(num):
    result = []
    if num !=2 and num % 2 == 0:
        result = [2]
    for i in range(3, int(floor(num ** 0.5)), 2):
         if num % i == 0:
             if len(factor(i)) == 0:
                 result.append(i)

    return result

print (factor(600851475143))
