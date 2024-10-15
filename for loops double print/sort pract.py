l=[3,1,5,12,9]
temp=0
for i in range(len(l)):
    for j in range(len(l)-1):
        if(l[j]>l[j+1]):
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp
print(l)


'''l=[3,1,5,12,9]
temp=0
for i in l:
    for j in range(0,i-1):
        if(l[j]>l[j+1]):
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp
print(l)'''