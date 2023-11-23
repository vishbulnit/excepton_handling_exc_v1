

print("Hellow....welcome in the topoc exception handling")

print(10/1)

print(10/2)

print(10/3)

try:
    print(10/0)
except ZeroDivisionError as e:
    print("exception detail: ",type(e))
    print("exception detail: ",e)
    print("exception detail: ",e.__class__)
    print("exception detail: ",e.__class__.__name__)
    print("exception detail: ",e.__doc__)
    print(10/1)

print(10/4)

print(10/5)

print("This is the first program")

