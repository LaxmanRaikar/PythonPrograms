from tech import main

try:
    list=input("enter the elements").split()#input
    x=sorted(list)                                             #sorting the entered list
    print(x)                                                   #printing the sorted list
    key=input("enter the key to search")                #input for the element to search
    print("enetered search key is",key)                        #printing the element to find
    print(main.binary(x,key))                                  #calling the methond and printing the output
except Exception as e:
    print("please enter the proper input and search element")  #throws error if the input is not proper