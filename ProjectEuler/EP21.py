def d(t):
    s = 0
    i = 1
    while i < t:
        if t % i == 0:
                s += i
        i += 1
    return s
def a(t1, t2):
    if d(t1) == t2 and d(t2) == t1 and t1 != t2:
        return 1
    else:
        return 0
sum = 0
b = 1
while b < 10000:
    if a(b, d(b)) == 1:
        sum += b
    b += 1
print (sum)
