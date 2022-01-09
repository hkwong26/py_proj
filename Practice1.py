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
        self._first_name: str = name
        self._color: str = color
        self._age: int = None
        self._type: Animal = None

    def __repr__(self):
        return f"Dog({self._first_name!r}, {self._color!r})"

    def __str__(self):
        return f"Dog({self._first_name}, {self._color})"

    def ab_method1(self):
        print("Bark")

    def new_method3(self):
        print("Growl")

    @property
    def name(self):
        return self._first_name

    @classmethod
    def all_dog(cls, input):
        return cls(input)

    @staticmethod
    def nothing_related():
        print(f"This is a static method that is independent of cls or self")
        return f"static method return"


if __name__ == "__main__":

    dog = Dog("frank", "black")
    dog2 = Dog.all_dog("Tommy")
    print(dog2.name)
    print(dog.name)
    print(repr(dog))
    print(dog)
    dog.nothing_related()
