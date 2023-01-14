''''''
data = {'Apple': 30, 'Orange': 90, 'Grapes': 76}

for x in data.keys():
    print(x)

#for y in data.values():
#    print(y)

print(data['Grapes'])

data['Pears'] = 922

print(data['Pears'])


# list within a dictionary
emp = {'name': 'Phil', 'Skills': ['Docker', 'Kubernetes', 'Terraform']}

for e in emp:
    print(e)

# You can print a key with multiple values in the same way you would if it onluy had one
# output: ['Docker', 'Kubernetes', 'Terraform']
print(emp['Skills'])

# you can use index to only print a specific item within the nested list of a dict
# output: Terraform
print(emp['Skills'][2])