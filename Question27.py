def loopFunction(argumentListWord):
    countLenghtWord=[]
    for index in range (len(argumentListWord)):
        countLenghtWord.append(len(argumentListWord[index]) )
    return countLenghtWord
        
def mapFunction(argumentListWord):
    return len(argumentListWord)

def main():
    inputListOfWord=input("Enter words for List with white space in between ")
    inputListOfWord=inputListOfWord.split()
    
    # using simple for loop
    print(inputListOfWord)
    outputList=loopFunction(inputListOfWord)
    print("length of string calulated by for loop")
    print(outputList)  

    # using map function
    outputListForMap=map(mapFunction,inputListOfWord)
    print("Length calculated by using map function")
    print(list(outputListForMap))

    #using list comprehension
    outputListForListComp=[len(index) for index in inputListOfWord]
    print("Length calculated by list comprehension")
    print(outputListForListComp)
  
if __name__=="__main__":
    main()    
