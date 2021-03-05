c = 0
b = 25
while c < 124:
   t1,t2,t3 = 1,1,3
   b += 2
   while (t3 != 0) and ([t1,t2,t3] != [1,1,1]):
      t1,t2,t3 = t2,t3,(t1+t2+t3) % b
   c += t3
print(b)
