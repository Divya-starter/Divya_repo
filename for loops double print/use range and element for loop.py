l=[3,4,5]
for i in range(len(l)):
    for j in range(0,l[i]-1):
        print("awesome i element:",l[i])
        print("awesome j element:",l[j])

print("\n")

#print index
l=[3,4,5]
for i in l:
    for j in range(0,i-1):
        print("awesome i:",i)
        print("awesome j:",j)




#this wont work bcoz declared list with str elements not with numbers to work below pgm
#TypeError: unsupported operand type(s) for -: 'str' and 'int'
#for j in range(0,i-1): will get error here
l=['a','b','c']
for i in l:
    for j in range(0,i-1):
        print(i)
        print(j)