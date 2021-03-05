def circle(r):
    n = int(r*2**0.5)
    n2 = n**2
    y2 = 2*r**2
    z = 4*(n+r**2)-3
    for x in range(1, r):
        y2 -= 2*x-1
        while n2 >= y2:
            n2 -= 2*n-1
            n -= 1
        z += 8*(n-r)
    return z

p210 = lambda r: 3*r*(2*r+1)/4-r+1+circle(r//8)

print (p210(10**9))
