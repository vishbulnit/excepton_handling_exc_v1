

class StudentNoStandardException(Exception):
    def __init__(self, msg):
        self.msg=msg

class StudentNoDivisionException(Exception):
    def __init__(self, msg):
        self.msg=msg

inp_std=int(input("Enter Student Standard [9,10,11,12]: "))
if  inp_std >= 9 and inp_std <= 12:
    print("*" * 30)
    print("Provided student standard is correct.")
    print("*" * 30)
else:
     raise StudentNoStandardException("This standard is not available in this school. Kindly share the correct standard.")

inp_div=str(input("Enter Student Division [A,B,C,D]: "))
if  inp_div=='A' or inp_div=='B' or inp_div=='C' or inp_div=='D':
    print("*" * 30)
    print("Provided student division is correct.")
    print("*" * 30)
else:
     raise StudentNoDivisionException("This Division is not available in this school for given standard. Kindly share the correct division.")

