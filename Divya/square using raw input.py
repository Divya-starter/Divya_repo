list1=list(map(int,input("enter elements:").split()))
list2=[]
list3=[]
for i in list1:
    list2.append(i**2)
    list3.append(i**0.5)
    print(list2)
    print(list3)