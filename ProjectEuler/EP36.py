def palindromic(number):
    l=""
    n= len(str(number))
    num=number
    number=int(number)
    for i in range(n):
       b=number%10
       number //= 10
       l+=str(b)
    if int(l)==num:
       return True

def binary(number):
    l=""
    while number>0:
       b= number % 2
       number //= 2
       l+=str(b)

    l=''.join(reversed(l))
    return l
l=[]
for i in range(1,1000000):
    if palindromic(i)== True and palindromic(int(binary(i))):
        l.append(i)
print(sum(l))
