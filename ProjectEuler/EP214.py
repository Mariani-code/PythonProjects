import time

start = time.time()
def chain(i):
    if i == 1:
        return (0,1)
    else:
        c = chain(int(tab[i]))
        return (c[0]+tab[i],c[1]+1)

print(time.time()-start)

tab = [i for i in range(40*10**6)]
i = 2

tab[1] = 2

for i in range(2,len(tab)):
    if(tab[i] != i):
        continue
    p = 1 - 1/i
    tab[i] *=p

    j = 2
    while i*j < len(tab):
        tab[i*j] *= p
        j += 1

#print([round(i) for i in tab]   )

print(time.time()-start)

s = 0
for i in range(2,len(tab)):
    if tab[i] == i-1:
        c = chain(i)
        if round(c[1]) == 25:
            #print(i)
            s+= i

print(s)

print(time.time()-start)
