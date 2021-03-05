def readnum(number):
    dic={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",}
    dic2={20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety"}
    read_lst=[]
    if len(str(number))==1:
        read_lst.append(dic.get(number))
    elif number==1000:
        read_lst.append("onethousand")
    elif len(str(number))==2:
        if number<20:
            read_lst.append(dic.get(number))
        else:
            num=int(str(number)[0])*10
            temp=dic2.get(num)
            read_lst.append(temp)
            if number!=num:
                read_lst.append(dic.get(int(str(number)[1])))

    elif len(str(number))==3:
        read_lst.append(dic.get(int(str(number)[0]))  + "hundred")
        temp=int(str(number)[1:])
        if temp!=0:
            read_lst.append("and")
            read_lst.append(compose(readnum(temp)))


    return read_lst

def compose(lst):

    return "".join(lst)



counter=0
for i in range(1,1001):
    for letter in compose(readnum(i)):
        counter+=1

print(counter)
