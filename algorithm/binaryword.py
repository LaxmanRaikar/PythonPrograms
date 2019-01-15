from tech import main
try:
    item=input("enter the word which you want to find ")  #taking input which word to find
    k=open('wordlist','r')                                #command to open file
    z=k.read()                                            #command to read the file
    m=z.split()                                           #splitting the word ang taking the words in list
    list=sorted(m)                                        #sorting the list to do binary search

    print(list)                                           #printting the sorted list

    print(main.binary(list,item))                          #calling the method
except Exception as e:
    print(e)
