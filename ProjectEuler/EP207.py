from math import log
from time import time

st = time()
i = 3
ctrperfect = 1
ctr = 1
while 1:

  log2t = int(log(i)/log(2)) 
  if 2**log2t == i:
    ctrperfect += 1
  ctr += 1

  if float(ctrperfect)/ctr < 1/12345.:
    break
  else:
    i += 1

print ("number of partitions =",i * (i-1))
print ("total processing time is", time() - st)
