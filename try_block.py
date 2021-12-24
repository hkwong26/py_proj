""" Looking at what try blocks can do """

istrue = False

# EARP more Pythonic way
# Faster and quicker way to determine the issue
# Readbility and cleaner, Avoid race conditions
try:
    f = open("test.txt")

# except Exception:
#     print("Exception block")

except FileNotFoundError:
    print("File does not exist")

else:
    print("Else blockk")
# finally:
#     print("Finally block")
