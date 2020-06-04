

def main():
    #listOfWords=["abccd","desfsw","aweasd","as","Q"," "]
    listOfInt=[]
    inputNumber=int(input("enter no. of list element you want"))
    listOfWords=[input("Enter list element") for index in range(inputNumber)]
    for index in range(len(listOfWords)):
        listOfInt.append(len(listOfWords[index]))
    # listofInt=[len(index2) fot index2 in listOfWord]
    print(" List of words is : " +str(listOfWords))
    print(" List of interger correspond to string is : " +str(listOfInt))

if __name__=="__main__":
    main()
