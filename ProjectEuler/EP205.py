from time import time
timethen = time()

memo = dict()

def P(score,throws,rnge):
    if throws == 1:
        return 1 if score>=1 and score <=rnge else 0
    if (score,throws,rnge) in memo:
        return memo[(score,throws,rnge)]
    res = 0
    for k in range(1,rnge+1):
        res += P(score-k,throws-1,rnge)
    memo[(score,throws,rnge)] = res
    return res

res = 4**9*(P(6,6,6)+P(7,6,6)+P(8,6,6))
val = 4**9-P(9,9,4)
for k in range(9,36):
    res += P(k,6,6)*val
    val -= P(k+1,9,4)

print(round(res/(4**9*6**6),7),"in",time()-timethen,"seconds")
