'''Exception
Handling
B)  Program to get the Name, Age, 6 Subjects marks as an
input from the user. Then generate the dictionary 
Before generating a dictionary you need to check whether the
entered age value is positive or not. If negative then we should add
the details to the dictionary.
Use User-Defined Exception Handling'''

class NegativeValue(Exception):
    pass
try:
    name=input( " Enter your name  : ")
    age=int(input("Enter your age  : "))
    if age<0:
        raise NegativeValue
    marks=[]
    for i in range(0,6):
        mark=float(input("Enter marks scored : "))
        marks.append(mark)
    dict_={"NAME":name,"AGE":age,"MARKS":marks}
    print("DETAILS : \n",dict_)
except NegativeValue:
    print("AGE IS NEGATIVE")

 
