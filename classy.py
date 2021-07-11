"""Play around with OOP """

class Car:
    def __init__(self, name, model, make) -> None:
        print("Python constructor for Car")
        self.name = name
        self.model = model
        self.make = make

    def instancemethod(self):
        print("Instance methods utilize self instances")
        pass

    @classmethod
    def clsmethod(cls):
        print("This class method utilizes the passed-in instances")

    @staticmethod
    def statmethod():
        print("Static methods doesn't utilize and passed-in classes but related logically")

class Subaru(Car):
    pass

subaruu = Subaru("Tim", "Toyota", "Prius")

vehicle1 = Car("Flora", "Forrester", "Subaru" )
vehicle1.clsmethod()

print(help(Subaru))

