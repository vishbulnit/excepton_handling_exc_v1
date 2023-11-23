

try:
    first_num = int(input("Enter the first number: "))
    second_num = int(input("Enter the second number: "))
    add=round(first_num+second_num,2)
    sub=round(first_num-second_num,2)
    mul=round(first_num*second_num,2)
    div=round(first_num/second_num,2)
    print(f"Addition: {add}, Substraction: {sub}, Multiplication: {mul}, Division: {div}")
except BaseException as e:
    print("exception description: ",e)
    print("exception type: ",type(e))
    print("exception class: ",e.__class__)
    print("exception class name: ",e.__class__.__name__)
    print("exception document: ",e.__doc__)



"""
first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
add=round(first_num+second_num,2)
sub=round(first_num-second_num,2)
mul=round(first_num*second_num,2)
div=round(first_num/second_num,2)
print(f"Addition: {add}, Substraction: {sub}, Multiplication: {mul}, Division: {div}")
"""