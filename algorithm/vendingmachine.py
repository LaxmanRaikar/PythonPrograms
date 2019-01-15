from utilities import utility

try:

    notes=[1000,500,100,50,20,10,5,2,1]                 #values
    money=int(input("enter the amount to withdraw: "))
    utility.vending(notes,money)                        #calling the method
except Exception as e:
    print(e)
