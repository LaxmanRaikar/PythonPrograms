from tech import functional

try:
    stack=int(input("enter the stack amount"))
    goal=int(input("enter the goal amount"))
    number=int(input("enter how many times you want to play"))
    if number>0 and stack>0:
        functional.gambler(stack,goal,number)
    else:
        print("enter more than 0")
except Exception as e:
    print("enter the proper input")