# place the code that causes the excepting inside the try block
try:
    pass
# handling the exception should be done in the except block
# you have the ability to explicitly mention what type of error you want except to catch
except KeyError:
    print("KeyError")
# generally finally block is used for cleaning up the resources open by the code
finally:
    pass


# You have the ability to handle multiple exception by mention them within your code
# in this example the first exp block will be skipped and the second will execute
try:
    emp = {'name': 'Phil', 'Skills': ['Docker', 'Kubernetes', 'Terraform']}
    #print(emp['tom'])
    print(10/0)
except KeyError:
    print('Exception in the code')
except ZeroDivisionError:
    print("ZeroDivisionError")
finally:
    print('Finally called...')