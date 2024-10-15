class Student:
    def read_student_data(self):
        self.sno=int(input("pkease enter the student sno\t"))
        self.sname=input("enter the student name")

    def displaydata(self):
        print(self.sno)
        print(self.sname)

obj1=Student()
obj2=Student()

obj1.read_student_data()
obj1.displaydata()

obj2.read_student_data()
obj2.displaydata()

