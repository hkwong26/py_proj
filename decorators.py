"""Understand first class function and closure for
    function - wrapper function and class - __call__ method decorators"""


def outer_func(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func


stor_func1 = outer_func("Yo")
stor_func2 = outer_func("cya")

stor_func1()
stor_func2()
