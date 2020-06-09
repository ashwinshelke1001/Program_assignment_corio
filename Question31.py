def myReduce(argumentList,argumentNumber):
    ans=0
    for i in range(argumentNumber):  
        ans+= argumentList[i] 
    return ans   

def myMap(argumentList):
    outputList=[len(word) for word in argumentList ]
    return outputList

def myFilter(inputList,inputNumberForFilter):
    outputList=[words for words in inputList if len(words) > inputNumberForFilter ]
    return outputList


def main():
    inputNumberRange=int(input("Enter range for includng "))
    inputList=[input("Enter string ") for index in range (inputNumberRange)]
    print(inputList)
    print(myMap(inputList))
    inputNumberForFilter=int(input(" enter range for filtering word"))
    print(myFilter(inputList,inputNumberForFilter))
    inputNumberRange1=int(input("Enter range for includng int list "))
    inputList1=[] 
    for  i in range(inputNumberRange1):
        inputList1+=[float(input("Enter Number for list"))]
    print("addition of number")
    print(myReduce(inputList1 ,inputNumberRange1))    


if __name__=="__main__" :
    main()