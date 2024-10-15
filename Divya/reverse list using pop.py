#l=['a','b','c']
list1=[4,6,8,2]
l2=[]
for i in range(len(list1)):
    l2.append(list1.pop())
    print(l2)

list2=['a','b','c','d']
l2=[]
for i in range(len(list2)):
    l2.append(list2.pop())
    print(l2)

#why we are losing first 2 elements?
list3=['a','b','c','e','f']
l3=[]
for i in list3:
    l3.append(list3.pop())
    print(l3)
