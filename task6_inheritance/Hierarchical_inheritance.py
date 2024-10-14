class Parent:
    def func1(self):
        print("This is in parent class.")

class Child1(Parent):
    def func2(self):
        print("This is in child1 class.")

class Child2(Parent):
    def func3(self):
        print("This is in child2 class.") 

child1 = Child1()
child2 = Child2()
child1.func1()
child1.func2()
child2.func1()
child2.func3()

