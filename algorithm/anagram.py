from utilities import utility
l=input("enter the string1 ")
l1=input("enter the string2")
try:
    utility.anag(l,l1)
except Exception as  e:
    print("error")