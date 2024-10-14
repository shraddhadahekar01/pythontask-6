class School:
    def func1(self):
        print("This is in school class.")

class Student1(School):
    def func2(self):
        print("This is in student1 class.")

class Student2(School):
    def func3(self):
        print("This is in student2 class")   

class Student3(Student1, School):
    def func4(self):
        print("This is in student3")    

object = Student3()   
object.func1()
object.func2()                      