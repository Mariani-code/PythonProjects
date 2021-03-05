import time
def chsum(str):
    x=0
    for t in str:
        x+=ord(t)-64
    return x

t=time.time()
f=open("C:\\names.txt")
x=f.read()
x=x.replace('"','').split(",")
x.sort()
sum=0
for n in range(0,len(x)):
    sum+=(n+1)*chsum(x[n])
print ('Sum:', sum, 'Time:', time.time() - t)
