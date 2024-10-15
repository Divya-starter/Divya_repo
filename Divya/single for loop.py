list1=[1,2,3,4]
print(list1)
for i in list1:
    print("elements:",i)
    print("list1:",list1)
    print("list1[i]",list1[i])  #you will get index error for l[4] wont be availble here

#check you will get type error
list1=['a','b','c']
for i in list1:
    print(list1[i])