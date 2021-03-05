from math import factorial
import time
start = time.time()

result=0

# store all 10 factorial numbers in a dictionary
d_factorial=dict()
for t in range(0,10):
    d_factorial[str(t)] = factorial(t)

max = 7 * d_factorial['9']
# print(max)

for i in range(3,max+1):
    temp=0
    for j in str(i):
        temp+=d_factorial[j]
        if temp>i: break

    if (i==temp):
        print(f'i: {i}')
        result+=temp


print(f'Sum: {result}')
print(f'Time: {time.time()-start}')
