from tech import main
try:
    nums=[int(x) for x in input("enter the elements ").split()]
    if len(nums)>3:
        main.insertion(nums)
    else:
        print("enter than more than 3 numbers")
except Exception as e:
    print(e)