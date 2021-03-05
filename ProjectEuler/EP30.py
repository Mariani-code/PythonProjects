from math import log10

def f(n):
    return (int(log10(n)+1))*(9**5) 

def check(n):
    tot=0
    for i in str(n):
        tot+=int(i)**5
    if tot==n:
        return True
    else:
        return False

upperbound=f(500000)

l=[]

for i in range(2,upperbound+1):
    if check(i):
        l.append(i)


print(sum(l))
