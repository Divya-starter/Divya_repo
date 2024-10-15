#class is a collection of datamembers and methods
#when we define the class , memory is not allocated for data members and methods

#object :instance of class is called object
#when we create an object we get memory space for data memebers and methods
#with respect to class definitions we can create n number of objects
#we can create first class then obj else we will get name error

class Student:           #class Classname
    def instance_method(self):
        print("I am from tirupathi")

student_obj1=Student()

