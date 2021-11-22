"""Play around with OOP """

class FirstClass():

    def __init__(self, var1, var2):
        self.variable1= var1
        self.variable2= var2 # unique instance variables
        self.const1 = 100
        self.thatthing='what is it?'
    
    def class_method1(self):
        print(f'class_method1 with instance method')
    

