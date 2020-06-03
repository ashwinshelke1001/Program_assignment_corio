def vowelChecker ( argument):
    if ( argument == "a" or argument=="A" or argument=="e" or argument=="E" or argument=="i" 
    or argument=="I" or argument=="o" or argument=="O" or argument=="u" or argument=="U" ):
        return True
    else :
        return False 

def translate(argument):
    newString=''
    for iterator in argument :
        if ( iterator>= "A" and iterator <= "Z" ) or (iterator>="a" and iterator<="z"):
            if  (vowelChecker(iterator)== False ):
                    newString = newString + iterator + "o" + iterator 
            else :
                newString +=iterator 
        else :
            newString += iterator 
        
    return newString


def main():
    inputString=input("Enter string")
    returnString=translate(inputString)
    print("Translated string is %s "%(returnString))


if __name__=="__main__":
    main()
