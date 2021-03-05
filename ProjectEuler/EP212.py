


N = 100
N = 50000

def gen():
    s = []
    k = 1
    while True:
        if k <= 55:
            s.append((100003 - 200003*k + 300007*k*k*k) % 1000000)
            k += 1
        else:
            s.append((s[-24] + s[-55]) % 1000000)
            s.pop(0)
        yield s[-1]

def intersection(c1, c2):
    x0, x1, y0, y1, z0, z1 = c1
    u0, u1, v0, v1, w0, w1 = c2
    xu0, xu1 = max(x0, u0), min(x1, u1)
    if xu1 <= xu0:
        return None
    yv0, yv1 = max(y0, v0), min(y1, v1)
    if yv1 <= yv0:
        return None
    zw0, zw1 = max(z0, w0), min(z1, w1)
    if zw1 <= zw0:
        return None
    return (xu0, xu1, yv0, yv1, zw0, zw1)

def volume(c):
    x0, x1, y0, y1, z0, z1 = c
    return (x1 - x0)*(y1 - y0)*(z1 - z0)

def make_all_cuboids(n):
    num = gen()
    cuboids = []
    for i in range(n):
        x0, y0, z0 = next(num) % 10000, next(num) % 10000, next(num) % 10000
        x1, y1, z1 = x0 + 1 + next(num) % 399, y0 + 1 + next(num) % 399, z0 + 1 + next(num) % 399
        cuboids.append((x0, x1, y0, y1, z0, z1))
    cuboids.sort()
    return cuboids

def intersect_again(intersections, cuboids):
    new_intersections = []
    n = len(cuboids)
    for c1, iMax in intersections:
        x1 = c1[1]
        for i in range(iMax+1, n):
            c2 = cuboids[i]
            if c2[0] >= x1:
                break
            c = intersection(c1, c2)
            if c is not None:
                new_intersections.append((c, i))
    return new_intersections

cuboids = make_all_cuboids(N)
intersections = [(cuboids[i], i) for i in range(N)]

v = sum(volume(c) for c in cuboids)
sign, k = 1, 1

while len(intersections) > 0:
    intersections = intersect_again(intersections, cuboids)
    sign = -sign
    v += sign * sum(volume(c) for c, i in intersections)
    k += 1
    print(len(intersections), "intersections of", k)

print("Total volume =", v)
