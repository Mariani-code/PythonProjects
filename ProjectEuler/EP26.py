import itertools
def recur_len(n):
    r = 10
    seen = {}
    for i in itertools.count(0):
        if r == 0:
            return 0
        elif r in seen:
            return i-seen[r]
        seen[r] = i
        r= 10*(r % n)

len,i = max((recur_len(i),i) for i in range(2,1000))
print (i)
