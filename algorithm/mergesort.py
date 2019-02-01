from utilities import utility
try:
    lst=[int(x) for x in input("enter the number with space ").split()]
    print(utility.merge_sort(lst))              #calls the method nad prints the output
except Exception as e:
    print(e)