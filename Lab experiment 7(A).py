''' Exception
Handling

A) If you give an index that is not in an range
then it will throw an error 
( error needs to be handled using try and except block.)'''

try:
    n=int(input("Enter the range :  "))
    list_=[]
    for i in range(0,n):
        num=int(input())
        list_.append(num)
    a=int(input("Enter the index : "))
    print("The element at ",a," is ",list_[a])
except IndexError:
    print("index exceeds limit !")
    print("the last index is  : ",len(list_) -1)
