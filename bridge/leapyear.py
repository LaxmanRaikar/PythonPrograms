from tech import functional


year=int(input("enter the year"))
if year>0:
    functional.leap(year)           # calling the method and passing the value
else:
    print("please enter the proper year")
