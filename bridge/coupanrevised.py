from utilities import utility

try:

    a=int(input("enter how many coupan numbers you want to generate :"))
    if a>0:

     utility.coupan_revised(a)                  # calling the method and passing the value
    else:
        print("enter positive number")
except Exception as  e:
    print(e)