"""
this program is used to find the factors of the given number
author:Laxman Raikar
since:8 JAN,2019
"""
from tech import functional
try:
    number = int(input("enter the number :"))
    functional.fact(number)          # calling the method and passing the value
except ValueError:
    print("Input only accepts decimal numbers")