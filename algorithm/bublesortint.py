from tech import main
try:
    array=[int(x) for x in input("enter the elements: ").split()]
    if len(array)>3:
        main.buble_sort(array)
    else:
        print("enter than more than 3 characters")
except Exception as e:
    print(e)