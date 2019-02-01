from tech import functional
try:

    list1= [int(x) for x in input("enter the elements: ").split()]
    functional.triple(list1)            #  calls the method and  passes the value
except Exception as e:
    print("error")