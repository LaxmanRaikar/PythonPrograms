"""
this program is used to find the square root of the number by using newtons method and epsilon value
author:Laxman Raikar
since:8 JAN,2019
"""
from utilities import utility
try:
    number = int(input("enter the value to find the square root: "))
    utility.sqrt(number)
except ValueError:
    print("ENTER THE INT VALUES")
