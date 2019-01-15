from tech import functional
try:
    row=int(input("enter the number of rows"))
    column=int(input("enter the number of columns"))

    functional.array(row,column)
except Exception as e:
    print("error")
