from utilities import  utility
try:

    d=int(input("enter the date :"))
    m=int(input("enter the month :"))
    y=int(input("enter the year :"))
    if d<32 and m<13 and y>0:
        utility.dayofweek(d,m,y)
    else:
        print("please give the correct date and month")
except Exception as e:
    print(e)