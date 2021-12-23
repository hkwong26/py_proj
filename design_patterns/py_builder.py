"""
Design Pattern: Builder Pattern

Creation design pattern, which allows construction of complex objects step by step
    - Utilization of the same construction process
    - Creation of  lots of possible configuration options

"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class Builder(ABC):
    """
    The builder interface spcifies methods for creating the different parts of the Product objects.
    """

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def product_part_a(self) -> None:
        pass

    @abstractmethod
    def product_part_b(self) -> None:
        pass

    @abstractmethod
    def product_part_c(self) -> None:
        pass

class ConcreteBuilder1(Builder):
    """
    The Concrete Builder classes follow the Builder interface and provide specific implementations of the building steps. Your program may have several variations of Builders, implemented differently
    """

    def __init__(self) -> None:
        """
        A fresh builder instance should contain a blank product object, which is used in further assembly.
        """
        self.reset()
    
    def reset(self) -> None:
        self._product = Product1()
    
    @property
    def product(self) -> Product1:
        """
        Concrete Builders are supposed to produce their own methods for retreving results. Thats because various tpes of builders may create entirely different products that don't follow the sa,e interface. Therefore, such methods cannot be declasred in the base Builder interface (at least in a statically types programming lanuage).

        Usually, after returning the end result to the client, a builder instance is expected to be ready to start producing another product. That's why it's a usual practice to call the result method at the end of the 'getProduct' method body. However, this behavior is not mandatory, and you can make your builders wait ofr an explicit reset call from the client code before disposing of the previous result.
        """

        product = self._product
        self.reset()
        return product

    def product_part_a(self) -> None:
        self._product.add('PartA1')

    def product_part_b(self) -> None:
        self._product.add('PartB1')

    def product_part_c(self) -> None:
        self._product.add('PartC1')

class Product1():
    """
    It makes sense to use the Builder pattern only when your products are quite complex and require entensive configuration.

    Unlike in other creational patterns, different concrete builders can produce unrelated products. In other words, results of various builders may not always follow the same interface.
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {','.join(self.parts)}", end="")

class Director:
    """
    The Directo is only responsible for executing the building steps in a particular sequence. It is helpful when producing productts accoding to a specific order or configuration. Strictly speaking, the Director class is optional, since the client can control builders directly.
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        """
        The Director works with any builder instance that the client code passes to it. This way, the client code may alter the final type of the newly assembled product.
        """
        self._builder = builder

    """
    The Director can construct several product variations using the same building steps.
    """

    def build_minimal_viable_product(self) -> None:
        self.builder.product_part_a()

    def build_full_featured_product(self) -> None:
        self.builder.product_part_a()
        self.builder.product_part_b()
        self.builder.product_part_c()

if __name__ == "__main__":
    """
    The client code creates a builder object, passse it to the director and then initates the construction process. The end result is tretrieved from the builder object.
    """

    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print('Standard basic product: ')
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print('\n')

    print('Standard full feature product: ')
    director.build_full_featured_product()
    builder.product.list_parts()

    print('\n')

    #Remember, the Builder pattern can be used without a Director class.
    print('Custom product: ')
    builder.product_part_a()
    builder.product_part_b()
    builder.product.list_parts()