
def add(a,b):
    result = a+b
    return result

# below code is written ValueError exception point of view
try:
    inp_first=int(input("Enter first value between range 0 to 10000: "))
    inp_second=int(input("Enter second value between range 0 to 20000: "))
    x=add(inp_first,inp_second)
except ValueError as e:
    # this block will execute when ValueError exception is raised
    print("*" * 50)
    print("Exception Type: ",type(e))
    print("Exception Class: ",e.__class__)
    print("*" * 50)
else:
    # this block will execute only when there is no exception raised
    print("*" * 50)
    print("Addition: ",x)
    print("*" * 50)
finally:
    # this block will always execute irrespective of exception raised or not and handled or not.
    print("Normal Termination")
    print("*" * 50)



