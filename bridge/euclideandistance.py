from tech import functional
try:
    x=int(input("enter the x value"))
    y=int(input("enter the y value"))
    functional.distance(x,y)
except Exception as e:
    print("please provide the proper inputs")
