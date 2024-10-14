class Parent:
    def func1(self):
        print("This is in parent class.")

class Child(Parent):   
    def func2(self):    
        print("This is in child class.") 

object =Child()
object.func1()
object.func2()

