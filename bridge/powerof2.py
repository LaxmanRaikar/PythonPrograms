from tech import functional
try:
    number=int(input("enter the number "))
    if 0<= number<31:
        functional.power(number)
    else:
        print("enter the number between 0 to 31")
except Exception as e:
    print(e)
