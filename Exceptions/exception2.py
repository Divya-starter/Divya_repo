try:
    s1=input("enter a value:")
    s2=input("enter b value:")
    a=int(s1)
    b=int(s2)
    c=a/b
except (ZeroDivisionError,ValueError):  #both print stmts will print even though one we encounter
    print("do not enter zero for division operation")
    print("do not enter alpha numeric numbers")
else:
    print("value of a:",a)
    print("value of b:",b)
    print(c)

finally:        #fine in case if we wont give this finally block
    print("I am done30")