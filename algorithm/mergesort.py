"""
this program is used to do the sorting of values by merge sort
author:Laxman Raikar
since:8 JAN,2019
"""
from utilities import utility
try:
    lst = [int(x) for x in input("enter the number with space ").split()]
    print(utility.merge_sort(lst))              # calls the method nad prints the output
except ValueError:
    print("ENTER THE INT VALUES")