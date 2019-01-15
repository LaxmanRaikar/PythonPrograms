from utilities import utility
try:
    x=int(input("to convert the temperature from Celsius to Fahrenheit press 1\n"
            "to convert the temperature from Fahrenheit to Celsius press 2:  "))

    if x==1:
        value=int(input("enter the temperature in celsius "))
        utility.fahreheit(value)
    elif x==2:
        value=int(input("enter the temperature in fahrenheit "))
        utility.celsius(value)

    else:
        print("enter between 1 and 2")
except Exception as e:
    print(e)