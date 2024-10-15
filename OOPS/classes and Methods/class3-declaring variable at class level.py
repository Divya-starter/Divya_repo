class Student:
    sname=input("enter the name of student")         #datamembers -common obj are placed here
    marks=int(input("enter the marks of student"))       #declared input  dynamically
    avg=90                                              #declared input via statically

#initialise object for Student
obj1=Student()
obj2=Student()

print(obj1.sname)
print(obj1.marks)
print(obj1.avg)
print(obj2.sname)
print(obj2.marks)