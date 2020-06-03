def genrateNumChar(argumentNumber , argumentChar) :
    newString=''
    index=0
    while (index < argumentNumber ) :
        newString += argumentChar
        index +=1
    return newString


def main():
    inputNumber=int(input("Enter Number"))
    inputChar=input("Enter Character")
    returnString=genrateNumChar(inputNumber,inputChar)
    print("The string is \n %s"%(returnString))
    
if __name__=="__main__":
    main()
