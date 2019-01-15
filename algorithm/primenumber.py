from utilities import utility
try:
    start=int(input("enter from where you want to find prime number"))
    stop=int(input("enter till where you want to find prime number"))
    if start>-1 and stop<1002:
        utility.prime(start,stop)
    else:
        print("enter number between 0-1000")
except Exception as e:
    print(e)