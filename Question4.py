def toCheckVowel ( argument):
    if ( argument == "a" or argument=="A" or argument=="e" or argument=="E" or argument=="i" 
    or argument=="I" or argument=="o" or argument=="O" or argument=="u" or argument=="U" ):
        return True
    else :
        return False 

def main():
    inputChar=input("Enter the char. : ")
    returnValue=toCheckVowel(inputChar)
    if (returnValue == True):
        print("Entered char is vowel")
    else :
        print("Entered char is not vowel")

if __name__=="__main__":
        main()