""" Playing with Try/Except Blocks for Error Handling """

try:
    pass
except Exception as e:
    print(e)
except FileNotFoundError as a:
    print(a)
else:
    print("else of the try block")
finally:
    print("finally portion of try block")
