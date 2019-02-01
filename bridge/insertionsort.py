from tech import main
try:
    nums=input("enter the element").split()
    main.insertion(nums)            # calling the method and passing the value
except Exception as e:
    print("error")

