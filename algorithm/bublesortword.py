from tech import main
try:
    file=open('number','r')                #opening the file
    str=file.read()                         #reading the text and storing it into the object
    split_array=str.split()                 #spliting the words to store the elements in array using sorted inbuilt function
    main.buble_sort(split_array)            #calling the method
except Exception as e:
    print(e)