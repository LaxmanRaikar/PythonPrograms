from utilities import utility
try:
    lst=[int(x) for x in input("enter the number with space ").split()]
    print(utility.merge_sort(lst))
except Exception as e:
    print(e)