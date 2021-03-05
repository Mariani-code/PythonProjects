sumOfSquares = 0
for i in range(1, 101):
    sumOfSquares += i * i

squareOfSums = 0
for i in range (1, 101):
    squareOfSums += i
squareOfSums = squareOfSums * squareOfSums

print(squareOfSums - sumOfSquares)
