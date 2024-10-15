#using functions -take list of elements.

def perfect_num(*args):

    for num in args:
        sum=0
        for i in range(1,num):
            if(num%i==0):
                sum=sum+i
                print(sum)
            elif(sum==num):
                print(f"{num} is perfect num")
            else:
                print(f"{num} is not a perfect number")

perfect_num(6,5,12)






#using functions and list of numbers.
#take inputs 5 12 6 ->check output

'''list1=list(map(int,input("entera number").split()))
for j in list1:
 sum=0
 for i in range(1,j):
    if(j%i==0):
        print(f"factors of given num {j} is:",i)
        sum=sum+i
        print("sum",sum)
    elif(sum==j):
        print(f"{j}is a perfect number")
    else:
        print(f"{j}is not a perfect num")
print("\n")


print("\n")'''



'''
#using function write the pgm

def perfect_num(num):
    sum=0
    for i in range(1,num):
        if (num % i == 0):
            print("factors of given num is:", i)
            sum = sum + i
            print("sum", sum)
    if(sum==num):
            print(f"{num}is a perfect number")
    else:
            print(f"{num}is not a perfect num")

num=int(input("enter a number:"))
perfect_num(num)'''





'''
num=int(input("entera number"))
sum=0
for i in range(1,num):
    if(num%i==0):
        print("factors of given num is:",i)
        sum=sum+i
        print("sum",sum)
if(sum==num):
    print(f"{num}is a perfect number")
else:
    print(f"{num}is not a perfect num")'''



