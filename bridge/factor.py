from tech import functional
try:
    n=int(input("enter the number"))
    functional.fact(n)
except Exception as e:
    print(e)