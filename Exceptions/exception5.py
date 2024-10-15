try:
 s1=input("enter the first value:")
 s2=input("enter the second value:")
 a=int(s1)
 b=int(s2)
 c=a/b
except ZeroDivisionError as zde:
 print(zde)
except ValueError as Divya:
 print(Divya)
except :             #when this will come
 print("You made some mistake, please check")
else:
 print("value of a:",a)
 print(f'value of b: {b}')
 print("value of division:",c)
finally:
 print("I am in finally block:")