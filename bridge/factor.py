from tech import functional
try:
    n=int(input("enter the number"))
    functional.fact(n)          # calling the method and passing the value
except Exception as e:
    print(e)