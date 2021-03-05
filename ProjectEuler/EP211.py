def sumOfDivisors(n):
    sum = 1 + n**2
    for i in range(2,int(n**.5)+1):
        if n%i==0:
            if i == n/i:
                sum += i**2
            else:
                sum += i**2 + (n/i)**2
    return sum

def main():
    total = 1
    for n in range(8,64000001):
        sum = sumOfDivisors(n)
        if (sum**.5)%1 == 0:
            print (n, sum, total)
            total += n

    print (total)


main()
