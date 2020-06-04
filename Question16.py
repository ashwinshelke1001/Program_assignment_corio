def filterLongWord(argumentList,argumentNumber):
    returnList=[]
    for index1 in argumentList:
        if len(index1) > argumentNumber :
            returnList +=[index1]
    return returnList
def main():
    inputNumber1=int(input("enter number of elem. you want in list"))
    inputList=[input("Enter List element") for index1 in range(inputNumber1)]
    inputNumber2=int(input("Enter number for providing greater length of list "))
    returnList=filterLongWord(inputList,inputNumber2)
    print(" list which is greater that the current number are : %s "%(returnList))

if __name__=="__main__":
    main()
 