import math
from datetime import datetime as dt

start = dt.now()
mn = math.floor(math.sqrt(1020304050607080900))
mx = math.ceil(math.sqrt(1929394959697989990))
mx -= mx % 10

def passesTest(n):
    st = str(n ** 2)
    st = ''.join([st[i] for i in range(len(st)) if i % 2 == 0])
    for i in range(1, 10):
        if (st[i - 1] != str(i)):
            return False
    return True

for i in range(mx, mn, -10):
    if (i % 30 != 0 or i % 70 != 0): continue
    if (passesTest(i)):
        print(i)
        break

print(dt.now() - start)
