from tech import functional

try:
    array= [int(x) for x in input("enter the elements between 0 to 9---> ").split()]
    functional.count(array)
except Exception as e:
    print("enter the proper input")
