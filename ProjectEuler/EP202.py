c = 6008819575
f = [5,11,17,23,29,41,47]

t = f[:]
od=f[:]
ev=[1]

for i in range(6):
    t = [j*k for j in t for k in f if j%k != 0]
    if i%2 == 0:
        ev.extend(t)
    else:
        od.extend(t)
ev = set(ev)
od = set(od)
r = 3 - c%3
def nof(c, f, r):
    """ Returns no. of values of x s.t.
    0<x<f
    f|x
    x%3 = r%3
    """
    r = (r-1)%3 + 1
    if f%3 == 0:
        if r%3 == 0: return (c-1)/f
        else: return 0
    if f%3 == 2: r = 3 - r%3
    return (c-f*r-1)/(3*f)+1

s = 0
for i in ev:
    s += nof(c, i, r)
for i in od:
    s -= nof(c, i, r)

print (s)
