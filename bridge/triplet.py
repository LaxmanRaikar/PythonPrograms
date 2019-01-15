from tech import functional
try:

    list1= [int(x) for x in input("enter the elements: ").split()]
    functional.triple(list1)
except Exception as e:
    print("error")