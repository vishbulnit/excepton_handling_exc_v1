
## multiple exception class are written to handle run time error 

dist = {"A1":1,"A2":2,"A3":3,"A4":4}
try:
    import pandas
    import numpy
    first_num = int(input("Enter the first number: "))
    second_num = int(input("Enter the second number: "))
    add=round(first_num+second_num,2)
    sub=round(first_num-second_num,2)
    mul=round(first_num*second_num,2)
    div=round(first_num/second_num,2)
    print(f"Addition: {add}, Substraction: {sub}, Multiplication: {mul}, Division: {div}")
    print(dist["A4"])

except SyntaxError as e:
    print("exception description: ",e)
    print("exception type: ",type(e))
    print("exception class: ",e.__class__)
    print("exception class name: ",e.__class__.__name__)
    print("exception document: ",e.__doc__)
except TypeError as e:
    print("exception description: ",e)
    print("exception type: ",type(e))
    print("exception class: ",e.__class__)
    print("exception class name: ",e.__class__.__name__)
    print("exception document: ",e.__doc__)
except NameError as e:
    print("exception description: ",e)
    print("exception type: ",type(e))
    print("exception class: ",e.__class__)
    print("exception class name: ",e.__class__.__name__)
    print("exception document: ",e.__doc__)    
except IndexError as e:
    print("exception description: ",e)
    print("exception type: ",type(e))
    print("exception class: ",e.__class__)
    print("exception class name: ",e.__class__.__name__)
    print("exception document: ",e.__doc__)    
except KeyError as e:
    print("exception description: ",e)
    print("exception type: ",type(e))
    print("exception class: ",e.__class__)
    print("exception class name: ",e.__class__.__name__)
    print("exception document: ",e.__doc__)   
except ValueError as e:
    print("exception description: ",e)
    print("exception type: ",type(e))
    print("exception class: ",e.__class__)
    print("exception class name: ",e.__class__.__name__)
    print("exception document: ",e.__doc__)   
except AttributeError as e:
    print("exception description: ",e)
    print("exception type: ",type(e))
    print("exception class: ",e.__class__)
    print("exception class name: ",e.__class__.__name__)
    print("exception document: ",e.__doc__)   
except IOError as e:
    print("exception description: ",e)
    print("exception type: ",type(e))
    print("exception class: ",e.__class__)
    print("exception class name: ",e.__class__.__name__)
    print("exception document: ",e.__doc__)   
except ZeroDivisionError as e:
    print("exception description: ",e)
    print("exception type: ",type(e))
    print("exception class: ",e.__class__)
    print("exception class name: ",e.__class__.__name__)
    print("exception document: ",e.__doc__)   
except ImportError as e:
    print("exception description: ",e)
    print("exception type: ",type(e))
    print("exception class: ",e.__class__)
    print("exception class name: ",e.__class__.__name__)
    print("exception document: ",e.__doc__)                           