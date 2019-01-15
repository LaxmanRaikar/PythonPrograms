from tech import main
try:
    nums=input("enter the element").split()
    main.insertion(nums)
except Exception as e:
    print("error")

