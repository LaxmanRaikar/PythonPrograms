from utilities import  utility
try:
    d=int(input("enter the month of date"))
    m=int(input("enter the month"))
    y=int(input("enter the year"))
    utility.day(d,m,y)
except Exception as e:
    print(e)