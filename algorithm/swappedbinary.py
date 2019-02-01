from utilities import utility

try:
    num=int(input("enter the number :"))
    utility.swap(num)           #calls the method
except Exception as e:
    print(e)