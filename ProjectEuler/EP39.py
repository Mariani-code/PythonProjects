import time
start = time.time()

def get_answer(n):
    MAX = n
    d = dict()
    for a in range(1,MAX+1):
        for b in range(a,MAX+1-a):
            c = (a**2 + b**2)**0.5
            if a+b+c <= MAX and c.as_integer_ratio()[1] == 1:
                d.setdefault(a+b+c, [0,[]])
                d[a+b+c][0] += 1
                d[a+b+c][1].append((a,b,c))

    return sorted(d.items(), key=lambda item: item[1], reverse=True)[0]

print(get_answer(1000))

print ("Completed in %s seconds." % ((time.time() - start)))
