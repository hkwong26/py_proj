# Projects to work on
""" Software Developement Plan """

print("Fun Making lists")

first_list = ["first", "second", 'third', 'fourth']
num_list = [1, 2, 3, 4, 5, 6]
fl_list = [2.3,4.25, 3.44, 3.22]

print(first_list)
print(first_list[0])
print(first_list[2])

first_list.append('fifth')

print(first_list)

first_list.extend(num_list)

print(first_list)

first_list.remove('first')
first_list.remove('second')

print(first_list)

first_list.insert(0, 'first')

print(first_list)
