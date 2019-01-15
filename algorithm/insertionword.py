from tech import main

try:
    file=open('wordlist','r')                    #opening the file
    str=file.read()                              #read the text anf=d storing in object
    split_array=str.split()                      #splitting the array to list
    main.insertion(split_array)           #calling the method
except Exception as e:
    print(e)