def isPalindrome(argumentList):
    #print(argumentList)
    index1=0
    index2=len(argumentList)-1
    while( index1 < index2):
        if (argumentList[index1] != argumentList[index2]):
            return False
        index1+=1
        index2-=1
    return True

def palindromeRec(argumentList):
    returnPhrase=''
    for index1 in argumentList:
        if ( index1 == " " or index1== "," or index1=="?" or index1=="!" or index1== "." ):
            returnPhrase=returnPhrase
        else:    
            returnPhrase += index1
    returnFromIsPalindrome=isPalindrome(returnPhrase.lower())
    return returnFromIsPalindrome


def main():
    fileName=input("Enter the name of file : \n")
    fp=open(fileName,"r")
    for line in fp.readlines() :
        if (palindromeRec(line[:-1])):
            print(line)
        
    fp.close()

if __name__=="__main__" :
    main()



