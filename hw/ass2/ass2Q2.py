class Animal:
    def __init__(self,name):
        self.name=name

    def printname (self):
        print("name is " +self.name)

class Dog(Animal):
    def __init__(self,name):
        self.name=name


result=Animal("Dog")
result.printname()

res1=Dog('tommy')
res1.printname()
