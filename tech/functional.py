#user input and replace the string
import random
import numpy as np
import math
import time

def username(name):
     print("hello",name,"how are you")  #printing the username

#---------------------------------------------------------------------------------------------------------

#flip of coin


def flipcoin(no):
    heads=0
    tails=0                         #intialization
    for x in range(no):
        x=random.random()           #taking random variable for random value to flip a coin
        if(x<0.5):                  #if the x is less than 0.5 than its tails
            tails+=1
        else:                       #if x is more than 0.5 than its heads
            heads+=1
    totalnoheads=heads
    totalnotails=tails
    print("total no of heads",totalnoheads)
    print("total no of tails",totalnotails)
    print("percentage of heads",(totalnoheads/no)*100)
    print("percentage of tails",(totalnotails/no)*100)

#-------------------------------------------------------------------------------------------------------------# -
#program to print the leap year
def leap(year):
    if(year%4==0 and year%100!=0 or year%400==0):
        print("it is leap year")
    else:
        print("it is not leap year")
#---------------------------------------------------------------------------------------------------------------
#program to print power of 2
def power(number):
    i=0
    while i<=number:                    #it will iterate the loop till i<=number
       print(i,"-",pow(2,i))
       i+=1
#---------------------------------------------------------------------------------------------------------------
def harmonic(value):
    sum=0
    for i in range(1,value,1):          #USING LOOP TO ITERATE THE VALUES
        sum=sum+1/i
    print(sum)
# -----------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------
# gambler
def gambler(stack,goal,number):
    bets=0
    wins=0
    loss=0
    for i in range(number):
        while 0<stack<goal:
            bets+=1
            if random.random()<0.5:
                stack+=1
            else:
                stack-=1
                print(stack)
    if stack==goal:
        wins+=1
    else:
        loss+=1

    noofwin=wins
    noofloss=loss


    print("no of wins",noofwin)
    print("no of loss",noofloss)
    print("percentage of win",(noofwin/number)*100)
    print("percentage of loss",(noofloss/number)*100)
#--------------------------------------------------------------------------------------------------------------
#coupan number
def count(array):
    count=0
    while(len(array)>0):
        x=random.randint(1,9)
        count+=1
        if x in array:
            array.remove(x)
            print(array)

    print("total random number to have all distinct codes",count)
#--------------------------------------------------------------------------------------------------------------------
#2d array
def array(row,column):
    arr = [[0 for i in range(row)] for j in range(column)]
    for i in range(column):
        for j in range(row):
            arr[i][j] = int(input("entered elements:"))
            array = np.array(arr)
    print(array)
#---------------------------------------------------------------------------------------------------------
#triplets
def triple(array):
    n=len(array)
    count=0
    for i in range(0,n-2,1):
        for j in range(i+1,n-1,1):
            for k in range(j+1,n,1):
                if (array[i]+array[j]+array[k]==0):
                    count+=1
                print(array[i]," ",array[j]," ",array[k]," ")
    print("number of triplets found in the above list   is",count)
    if count==0:
        print("no triplets found")
#--------------------------------------------------------------------------------------------------------------
def distance(x,y):
    z=math.sqrt(x*x+y*y)
    print("euclidean distance value of",x,"and",y,"is",z)
#---------------------------------------------------------------------------------------------------
#start and stop program
def start_time():
    t0=time.time()
    t1=time.time()
    print("start time is",t0)
    print("stopped time is ",t1)
    t2=t1-t0
    print("elapsed time is ",t2)
#-------------------------------------------------------------------------------------------------------------
#quadratic function
def quadraticFunctions(a, b, c):
    print("Given quadratic equation is:", a, "x^2 +", b, "x + ", c)
    d = (b * b) - (4 * a * c)
    if (d > 0):
        print("Roots are real and unequal")
        root1 = (-b + math.sqrt(d)) / (2 * a)
        root2 = (-b - math.sqrt(d)) / (2 * a)
        print("First Root ", root1)
        print("Second Root ", root2)

    elif (d == 0):
        print("Roots are real and equal")
        root1 = (-b + math.sqrt(d)) / (2 * a)
        print("First Root ", root1)

    else:
        print("Root are imaginary")
#------------------------------------------------------------------------------------------------------------
#windchill
def wind(t,v):
    w = (355.74 + 0.6215 * t + (.4275 * t - 35.75)) * pow(v, 0.16)
    print(w)
#  ---------------------------------------------------------------------------------------------------------
def fahreheit(value):
    fah=(value*9 / 5)+32
    print(fah)
def celsius(value):
    cel=(value-32)*5/9

#  ------------------------------------------------------------------------------------------------------------
def fact(n):
    p=2
    while n>p*p:
        if n%p==0:
            print(p)
            n=n//p
        else:
            p+=1
    print(n)








