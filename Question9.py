def isMember( argumentValue , argumentList):
    index=0
    while ( index <= (len(argumentList)-1)):
        if ( argumentValue == argumentList[index]):
            return True
        index+=1
    return False



def main():
    inputList=[]
    inputValue=input("Enter value ")
    numberOfElemntInList=int(input("Enter number of elemn."))
    for index in range(numberOfElemntInList):
        elementOfList=input("enter element of list")
        inputList +=[elementOfList]
    returnValue=isMember(inputValue,inputList)
    if (returnValue == True):
        print("Value is present in list")
    else :
        print("value is absent in list")

if __name__=="__main__":
    main()
