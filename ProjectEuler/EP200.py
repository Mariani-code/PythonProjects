import time
def Primes(y):
    primes=[2]
    i=3
    while i<y:
        isprime=True
        for x in range(2, int(i**.5 + 1)):
            if i%x==0:
                isprime=False
                break
        if isprime:
            primes.append(i)
        i=i+1
    return primes

def isPrime(n):
    if n==0:
        return False
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for x in range(3,int(n**0.5)+1,2):
        if n%x==0:
            return False
    return True

def primeProof(n):
    s=str(n)
    l=0
    for x in s:
        #i=int(s.index(x))
        for y in range(0,10):
            x=str(y)
            s=s[0:l]+x+s[l+1:]
            if isPrime(int(s)):
                return False
        s=str(n)
        l+=1
    return True

def main():
    t1=time.time()
    array=[]
    prime=[2,5]
    primes=Primes(300000)
    for x in prime:
        for y in primes[primes.index(x):]:
            if x!=y:
                temp=(x**2)*(y**3)
                temp2=(x**3)*(y**2)
                if temp<260200323272:
                    if str(temp).__contains__("200") and primeProof(temp):
                        #print temp,x,y
                        array.append(temp)
                if temp2<260200323272:
                    if str(temp2).__contains__("200") and primeProof(temp2):
                        #print temp2,x,y
                        array.append(temp2)
                        #print len(array)
                elif temp>260200323272 and temp2>260200323272:
                    break
        print (x)
    array=sorted(list(set(array)))
    print (array)
    print ("finding")
    print (len(array))
    print (array[199])
    print (time.time()-t1)
main()
