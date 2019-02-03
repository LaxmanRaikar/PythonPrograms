"""
this program is used search a value using binary search
author:Laxman Raikar
since:8 JAN,2019
"""

from tech import main
try:
    list_ = [int(x) for x in input("enter the list ").split()]
    no = int(input("enter the number to find "))
    x = sorted(list_)
    if len(x)>1:
        print(main.binary(x, no))   # calling the method
    else:
        print("enter more than one digits")
except ValueError:
    print("Input only accepts decimal numbers")