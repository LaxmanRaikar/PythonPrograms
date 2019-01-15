from utilities import utility
try:
    num=int(input("enter the number to convert to binary: "))
    utility.bin_ary(num)
except Exception as e:
    print(e)