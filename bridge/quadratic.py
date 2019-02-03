"""
this program is used to find the quadratic roots
author:Laxman Raikar
since:8 JAN,2019
"""
from tech import functional

try:
    a = int(input("Enter the value of a "))
    b = int(input("Enter the value of b "))
    c = int(input("Enter the value of c "))
    functional.quadraticFunctions(a,b,c)            # calls the method and pass the value
except ValueError:
    print("Input only accepts decimal numbers")
