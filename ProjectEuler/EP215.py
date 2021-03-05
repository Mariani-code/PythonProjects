def createRows(n):
    if n == 2:
        return [[2]]
    if n == 3:
        return [[3]]
    if n == 4:
        return [[2, 2]]
    rows = []
    rows += [row + [3] for row in createRows(n - 3)]
    rows += [row + [2] for row in createRows(n - 2)]
    return rows

def accum(row):
    crack = [row[0]]
    for i in range(1, len(row) - 1):
        crack += [crack[-1] + row[i]]
    return crack

def disjoint(x,y):
    for i in x:
        if i in y:
            return False
    return True

def collect(n):
    cracks = [accum(row) for row in createRows(n)]
    v = [[]] * len(cracks)
    for i in range(len(cracks) - 1):
        for j in range(i + 1, len(cracks)):
            if disjoint(cracks[i],cracks[j]):
                v[i] = v[i] + [j]
                v[j] = v[j] + [i]
    return v

def go(a,b):
    walls = collect(a)
    v = [1] * len(walls)
    i = 1
    while i < b:
        v = [sum([v[j] for j in wall]) for wall in walls]
        i += 1
    print(sum(v))

go(32,10)
