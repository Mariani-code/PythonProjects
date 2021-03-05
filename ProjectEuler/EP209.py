PoT = [1]
for z in range(64):
    PoT.append(2 * PoT[-1])
L = [2, 1]
for z in range(63):
    L.append(L[-1] + L[-2])
rings = []
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                for e in range(2):
                    for f in range(2):
                        i = (a, b, c, d, e, f)
                        newInput = True
                        for ring in rings:
                            if (i in ring):
                                newInput = False
                        if (newInput):
                            newRing = [i]
                            j = (b, c, d, e, f, a ^ (b & c))
                            while j not in newRing:
                                newRing.append(j)
                                j = (j[1], j[2], j[3], j[4], j[5], j[0] ^ (j[1] & j[2]))
                            rings.append(newRing)
N = PoT[64]
for ring in rings:
    h = len(ring)
    N = N * L[h] / PoT[h]
print (N)
