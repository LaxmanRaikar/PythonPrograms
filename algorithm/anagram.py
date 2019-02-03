"""
this program is used check the one string is anagram of other
author:Laxman Raikar
since:8 JAN,2019
"""

from utilities import utility
first_value = (input("enter the string1  :"))
second_value = (input("enter the string2  :"))
try:
    utility.anag(first_value,second_value)      # calling anag method
except  Exception :
    print("error")