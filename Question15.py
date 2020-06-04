
def findLongestWord(argumentList):
    argumentList=[len(index1) for index1 in  (argumentList)]
    return (max(argumentList))



def main():
    lengthOfList=[]
    inputNumber=int(input("enter number "))
    intputList=[input("enter the list element ") for index in range(inputNumber)]
    returnMaxLength=findLongestWord(intputList)
    print ("Length of Longest word is %d "%(returnMaxLength))

if __name__=="__main__":
    main()
 