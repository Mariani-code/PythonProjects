def isPrim(num):
    for prim in primenumber:
        if num % prim == 0:
            return False
    return True

primenumber = list([2])
num = 3
counter = 1

while counter <= 10000:
    if isPrim(num):
        primenumber.append(num)
        counter += 1
    num += 1
print(primenumber[-1])
