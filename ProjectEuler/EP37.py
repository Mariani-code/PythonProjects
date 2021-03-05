from math import sqrt
def prime(number):
    if number ==1:
        return None
    for p in range(2,int(sqrt(number)//1)+1):
        if number % p ==0:
            return None
    return number

def listsplit(number):
    list1=[]
    for i in str(number):
        list1.append(i)
    return list1

def listtonumber(list1):
    number=""
    for i in list1:
        number+=i
    return int(number)

def delfromleft(list1):
    del list1[0]
    return list1

def delfromright(list1):
    del list1[-1]
    return list1

def checkleft(number):
     if prime(number)!=None:
        count=0
        numberlist=listsplit(number)
        while count!=len(str(number))-1:
            delfromleft(numberlist)
            newvalue=listtonumber(numberlist)
            if prime(newvalue)==None:
                return None
            count+=1
        return number

def checkright(number):
        if prime(number)!=None:
            count=0
            numberlist=listsplit(number)
            while count!=len(str(number))-1:
                delfromright(numberlist)
                newvalue=listtonumber(numberlist)
                if prime(newvalue)==None:
                    return None
                count+=1
        return number
total=0
for i in range(10,1000000):
    if checkright(i)!=None and checkleft(i)!=None:
        print(i)
        total+=i
print(total)
