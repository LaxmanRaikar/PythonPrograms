from utilities import utility
try:
    principle=int(input("enter the principle amount: "))
    year=int(input("enter the number of year: "))
    roi=int(input("enter the rate of interest: "))
    utility.monthly_payment(principle,year,roi)
except Exception as e:
    print(e)
