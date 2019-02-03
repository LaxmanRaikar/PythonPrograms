"""
this program is to find the sum of three numbers in a list is zero or not
author:Laxman Raikar
since:8 JAN,2019
"""
from tech import functional
try:

    list1 = [int(x) for x in input("enter the elements: ").split()]
    functional.triple(list1)            # calls the method and  passes the value
except ValueError:
    print("Input only accepts decimal numbers")