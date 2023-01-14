# slicing


x = 'Unhappy'.upper()
print(x)

y = x[2:].lower()
print(y)


x = '1234567812345678'
# the output will print numbers starting at index 2 =3 and stopping at index 13 = the 2nd(6)
# the 2 dictates that interval that it will skip by when slicing
print(x[2:13:2])
# output 357

# -1 by passing a negative number the output will be produced in reversed
print(x[::-1])


# LIST
# index 0  1  2  3   4   5
data = [1, 2, 3, 4, 'a', 10.4, 2]


for x in data:
    print(x)

# use append() to add object at the end of a list
data.append(34)
print(data)

# use insert() to add and object to any location within a list
# by declaring the index location within the function
data.insert(3, 'Python')
print(data)

# use del [] to delete an object from any location within a list
# by declaring the index location within the function
del data[3]
print(data)

# slicing a list

data = [1, 2, 3, 4, 'a', 10.4, 2]
print(data[2::2])
# output will be [3, 'a', 2]










