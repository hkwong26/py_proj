""" Play around with the data sets like list, dict, tuples, and sets"""

my_list = [x for x in range(10)]
print(my_list)

my_lett = ["a", "b", "c", "d", "e"]
my_dict = zip(my_list, my_lett)
print(list(my_dict))

my_dict2 = dict(list(enumerate(my_lett)))
print(my_dict2)
