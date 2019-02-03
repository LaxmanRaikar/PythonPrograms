"""
this program is used to print the 2d array by using numpy
author:Laxman Raikar
since:8 JAN,2019
"""
from tech import functional
try:
    row = int(input("enter the number of rows :"))
    column = int(input("enter the number of columns :"))

    functional.array(row, column)                # calling the method and passing two values
except ValueError:
    print("Input only accepts decimal numbers")

