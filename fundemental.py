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