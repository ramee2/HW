class Dog:
    def __init__(self,name):
        self.name=name

    def printname (self):
        print("name is " +self.name)

result=Dog("tommy")
result.printname()
