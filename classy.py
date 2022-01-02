"""Play around with OOP """


class FirstClass:
    def __init__(self, var1, var2):
        self.variable1 = var1
        self.variable2 = var2  # unique instance variables
        self.const1 = 100
        self.thatthing = "what is it?"

    def class_method1(self, param1: float, param2: int):
        print(f"class_method1 with instance method")


class SecondClass:
    def __init__(self, var1, var2):
        self.variable1 = var1
        self.variable2 = var2
        self.TABLE = 2.3

    def class_method2(self, parm1, parm2):
        print(f"based in {__name__} parm1 = {parm1} parm2 = {parm2}")


def main():
    first = FirstClass()
    second = SecondClass()
    
    first.class_method1
    second.class_method2

if __name__ == "__main__":
    main()
