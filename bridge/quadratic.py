from tech import functional

try:
    a = int(input("Enter the value of a "))
    b = int(input("Enter the value of b "))
    c = int(input("Enter the value of c "))
    functional.quadraticFunctions(a,b,c)
except Exception as e:
    print("Enter a number not characters ")
