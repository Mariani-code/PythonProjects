import math
factorials=[1]
for i in range(1,51):
    factorials.append(i*factorials[i-1])

def C(n,r):
    return factorials[n]/(factorials[r]*factorials[n-r])

def isPrime(n):
    if n<2:return False
    if n==2:return True
    if n%2==0:return False
    for i in range(3,int(math.sqrt(n)+1)):
        if n%i==0:return False
    return True

combinations=list();


for i in range(51):
    for j in range(i+1):
        combinations.append(C(i,j))

prime_squares=[4]

for i in range(3,26):
    if isPrime(i):
        prime_squares.append(i*i)

combinations.sort()
distinct_combinations=[1]
for i in range(1,len(combinations)):
    if combinations[i-1]==combinations[i]:continue
    distinct_combinations.append(combinations[i])



def isSquareFree(n):
    for i in prime_squares:
        if n%i==0:return False
    return True

sum=0
for i in distinct_combinations:
    if isSquareFree(i):
        sum+=i

print (sum)
