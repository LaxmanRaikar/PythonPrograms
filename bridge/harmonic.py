"""
this program is used print the nth harmonic value
author:Laxman Raikar
since:8 JAN,2019
"""
from tech import functional
try:
    value = int(input("enter the value:  "))
    if value > 0:                                     # if value is more than 0 it will  run the method
        functional.harmonic(value)
    else:print("enter more than 0")
except ValueError:                    # if is not numerical value it will throw the error
    print("enter the proper input")