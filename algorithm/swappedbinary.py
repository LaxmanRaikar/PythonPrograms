"""
this program is used to find the binary number and swap the binary number by using padding
author:Laxman Raikar
since:8 JAN,2019
"""

from utilities import utility

try:
    num = int(input("enter the number :"))
    utility.swap(num)           # calls the method
except ValueError:
    print("ENTER THE INT VALUE")