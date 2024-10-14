class Father:
    def teach(self):
        print("Father teaches")

class Mother:
    def care(self):
        print("mother cares")

class Child(Father, Mother):
    def play(self):
        print("child plays")

child = Child()
child.teach()
child.care()
child.play()