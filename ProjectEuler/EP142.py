sol = dict()
max_ = 0
maxcnt = 0
for i in range(1, 100_0001):
    temp = i
    cnt = 1
    while temp != 1:
        if temp in sol:
            sol[i] = cnt+sol[temp]-1
            break
        if temp % 2 == 0:
            temp >>= 1
        else:
            temp = 3*temp+1
        cnt += 1
    else:
        sol[i] = cnt
    if maxcnt < sol[i]:
        maxcnt = sol[i]
        max_ = i
print(max_)
