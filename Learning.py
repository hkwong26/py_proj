""" First file to play around Pythong """
print(" This is the learning.py file ")

print("Function play")

def function1(n):
    loc_var = n
    print("Inside the function")
    print(f"print out local variable {loc_var}")
    return loc_var

"""User space"""

result = function1(10)

print(result)