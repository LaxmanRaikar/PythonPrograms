from utilities import utility

try:
    num=int(input("enter the number :"))
    utility.swap(num)
except Exception as e:
    print(e)