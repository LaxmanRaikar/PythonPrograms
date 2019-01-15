from tech import main
try:
    list=[int(x) for x in input("enter the list ").split()]
    no=int(input("enter the number to find "))
    x=sorted(list)
    if len(x)>1:
     print(main.binary(x,no))
    else:
        print("enter more than one digits")
except Exception as e:
    print(e)