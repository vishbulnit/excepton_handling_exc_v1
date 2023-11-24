

class Arithmetic_Operation:
    
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def Add(self):
        result=round(self.a+self.b,2)
        print(f"Addition: {result}")
    
    def Sub(self):
        result=round(self.a-self.b,2)
        print(f"Substraction: {result}")
    
    def Mul(self):
        result=round(self.a * self.b,2)
        print(f"Multiplication: {result}")
    
    def Div(self):
        result=round(self.a / self.b,2)
        print(f"Division: {result}")


## case 1 - check for zero division error and see output
try:
    first_num = int(input("Enter first number: "))
    second_num = int(input("Enter Second number: "))
    obj = Arithmetic_Operation(first_num,second_num)
    obj.Div()
    print("Code executed successfully.")   
except ZeroDivisionError as e:
    print("exception type: ",e)

## finally block will always execute irrespective of try and except block
## finally block is mainly used to deallocate the resources/clean-op 
finally:
    print("This is arithmetic operation statement")   


## case 2 - check for zero division error and see output
try:
    first_num = int(input("Enter first number: "))
    second_num = int(input("Enter Second number: "))
    obj = Arithmetic_Operation(first_num,second_num)
    obj.Div()
    print("Code executed successfully.")   
except ValueError as e:
    print("exception type: ",e)

## finally block will always execute irrespective of try and except block
## finally block is mainly used to deallocate the resources/clean-op 
finally:
    print("This is arithmetic operation.")   


## case 3 - check for zero division error and see output
try:
    first_num = int(input("Enter first number: "))
    second_num = int(input("Enter Second number: "))
    obj = Arithmetic_Operation(first_num,second_num)
    obj.Div()
    print("Code executed successfully.")   
except ValueError as e:
    print("exception type: ",e)
except:
    print("other exception raised")

## finally block will always execute irrespective of try and except block
## finally block is mainly used to deallocate the resources/clean-op 
finally:
    print("This is arithmetic operation statement")    
