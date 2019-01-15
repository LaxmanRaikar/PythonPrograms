from utilities import utility
num =24
array=[]
arr=[]

for i in range(1,num):
 if(num%i==0):
  array.append(i)
print(array)


for num in range(0, len(array) + 1):  # outer loop
 isboolean = True  # boolean value
 for i in range(2, num):  # inner loop
  if (num % i) == 0:
    isboolean = False
    break  # if boolean value is false it will break the loop

  if isboolean:
   arr.append(num) # if it is prime than the number will be added to list(arr[])
   break

print(arr)


