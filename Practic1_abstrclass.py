from abc import ABC, abstractclassmethod, abstractmethod


class Animal(ABC):
    def __init__(self):
        """Constructur for the class"""
        pass

    @abstractmethod
    def ab_method1(self):
        pass

    @abstractmethod
    def ab_method2(self):
        pass
