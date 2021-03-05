def fib(n):
    a=0
    b=1
    i=1
    counter=1
    while i < n:
        c=a+b
        a=b
        b=c
        counter=counter+1
        i=len(str(b))
    return counter
x=fib(1000)
print (x)
