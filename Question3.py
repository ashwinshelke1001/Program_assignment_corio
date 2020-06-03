def lengthString( argument):
    counter=0
#Using simple for loop
#    for iterator in argument:
#        counter +=1
#    return counter 
#slicing method 
    while argument[counter:]:
        counter+=1
    return counter
    

def main ():
    string1=input("Enter string : ")
    length1=lengthString(string1)
    print("Length of string is %d "%length1)

if __name__=="__main__" :
    main()
    
