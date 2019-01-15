from tech import main
try:
    array=input("enter the elements to sort").split()  #input
    main.buble_sort(array)                             #calling the method
except Exception as e:                                 #throws error if input is not in proper format
    print("please enter the list in numerics or in string ")


