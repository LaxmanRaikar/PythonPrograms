from utilities import utility
try:
    c=int(input("enter the value to find the square root: "))
    utility.sqrt(c)
except Exception as e:
    print(e)
