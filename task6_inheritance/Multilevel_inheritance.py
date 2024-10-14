class Grandfather:
    def func1(self):
        print("This is Grandfather class")

class Father(Grandfather):
    def func2(self):
        print("This is Father class")

class Child(Father):
    def func3(self):
        print("This is the child class")

child = Child()
child.func1()
child.func2()
child.func3()

      
            
            