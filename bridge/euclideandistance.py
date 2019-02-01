from tech import functional
try:
    x=int(input("enter the x value"))
    y=int(input("enter the y value"))
    functional.distance(x,y)                    # calling the method and passing the value
except Exception as e:
    print("please provide the proper inputs")
