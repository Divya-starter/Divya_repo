try:
 s1=input("enter the first value:")
 s2=input("enter the second value:")
 a=int(s1)
 b=int(s2)
 c=a/b
except ZeroDivisionError as zde:
 print(zde)                    #print the exception that is based on ZDError which is there in built.
except ValueError as Divya:    #
 print(Divya)                  #
 print("User message: Dont give values other than integer")
else:
 print("value of a:",a)
 print(f'value of b: {b}')
 print("value of division:",c)
finally:
 print("I am in finally block:")