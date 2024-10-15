def add_fun(a,b):
    try:
        c=a/b
    except ZeroDivisionError as ZDE:
        print(ZDE)
    except:
        print("nothing is fine")
        #print("something went wrong")
    else:
        return(c)

try:
 a=int(input("enter a value:"))
 b=int(input("enter b value"))
except ValueError as VE:
 print(VE)
else:
 result=add_fun(a,b)
 print(result)