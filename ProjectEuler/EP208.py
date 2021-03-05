from time import time
sttm=time()


def P208(N1=70,nslc1=5) :
	def cN1(l1) :
		'''
		l1 is a tuple
		'''
		if all(n0==N0 for n0 in l1) : return 1
		if l1 in dR1 : return dR1[l1]
		sm1=0
		if l1[0]<N0 : sm1+=cN1(l1[1:]+(l1[0]+1,))
		if l1[-1]<N0 : sm1+=cN1((l1[-1]+1,)+l1[:-1])
		dR1[l1]=sm1
		return sm1
	N0=N1/nslc1
	dR1={}
	return cN1((0,)*nslc1)

sm1=P208(70,5)

print (sm1)
print (time()-sttm)
