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
    intputString=input("Enter phrase")
    returnFromIsPalindrome=palindromeRec(intputString)
    if (returnFromIsPalindrome == True):
        print("Enter phrase can be pallindromic phrase")
    else :
        print("phrase is not pallindome")        

if __name__=="__main__":
    main()
