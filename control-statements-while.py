'''
data = 1
while data <= 10:
    print(data)
    data += 1
else:
    print('greater then 10')
'''


# the first print output will read 10, 20, 0, 0  making the final print output: The value of a is 0
nunmbers = [10, 2, 0, 10]
a = 1
for x in nunmbers:
    a = a*x
    print(a)
print(f'The value of a is {a}')

# You can skip the number 0 and continue your code by adding a conditional that checks for 0
# followed by a CONTINUE statement which moves on to the next obect in your list
nunmbers = [3, 2, 10, 0, 20, 5]
a = 1
for x in nunmbers:
    if x == 0:
        continue
    a = a * x
print(f'The value of a is {a}')


# You can also stop the code from running by adding a conditional that checks for OBJECTS  that == 0
# followed by a BREAK statement which will stop the for loop
nunmbers = [3, 2, 10, 0, 20, 5]
a = 1
for x in nunmbers:
    if x == 0:
        break
    a = a * x
print(f'The value of a is {a}')
