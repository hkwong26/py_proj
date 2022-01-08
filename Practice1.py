"""
    Daily Practice for better coding skills
    1/8/2022
    Focus - OOP and OOD
"""

from py_proj.Practic1_abstrclass import Animal


class Dog(Animal):
    def __init__(self, name: str = None, color: str = None):
        """
        Explicitly state what data the class is holding within the class
        by placing the self.variables inside this constructor
        """
        self.first_name = name
        self.color = color
        self.age = None
        self.type = None

    def ab_method1(self):
        print("Bark")

    def ab_method2(self):
        print("Woof")

    def new_method3(self):
        print("Growl")

    @property
    def name(self):
        print(f"@property getter for name")
        return self.first_name


if __name__ == "__main__":

    dog = Dog("frank", "black")
    print(f"Dog's name is {dog.name} and the color ir {dog.color}")
    bark = dog.ab_method1
    woof = dog.ab_method2
    bark()
    woof()
    dog.new_method3()
    what_is_the_name = dog.name
