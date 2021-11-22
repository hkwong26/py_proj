"""This is the nester.py function that provides one function called
    print_lol(). """

def print_lol(the_list):
    """Inner comments of the function"""
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item) 
        else:
            print(each_item) 