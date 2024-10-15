try:
    s1=input("enter the first value:")
    s2=input("enter the second value")
    a=int(s1)
    b=int(s2)
    c=a/b                       # Code that might cause an exception
except ZeroDivisionError:
    print("do not enter zero for division") #Code that runs if an exception occurs
except ValueError:
    print("enter only numerics not  special characters or alphabets") #Code that runs if an exception occurs
except TypeError:
    print("enter correct values types") #Code that runs if an exception occurs
else:                          #code that should run only if no exceptions occur in the try block.
    print("value of c:",c)
finally:                      #Code that always runs, regardless of exceptions.clean up code
    print("i am in final block")


#link:
#https://www.tutorialspoint.com/python/python_tryexcept_block.htm
#ensuring resources are properly released and critical tasks are completed.