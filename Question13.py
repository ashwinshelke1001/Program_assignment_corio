def functionOfMaxElement(inputList,low,high):
    #using Quick sort method
    if low < high :
        partionIndex=partitionFunction(inputList,low,high)
        functionOfMaxElement(inputList,low,partionIndex-1)
        functionOfMaxElement(inputList,partionIndex+1,high)

def partitionFunction(inputList,low,high):
    index=(low-1)
    pivotElement=inputList[high]
    for index2 in range(low,high):
        if inputList[index2] <= pivotElement :
            index+=1
            inputList[index],inputList[index2]=inputList[index2],inputList[index]

    inputList[ index+1],inputList[high]=inputList[high],inputList[index+1]
    return (index+1)

        



def main():
    inputList=[]
    inputNumber=int(input("enter number u want in list"))
    for index in range(inputNumber):
        inputElement=int(input("enter element for lisr"))
        inputList +=[inputElement]
    functionOfMaxElement(inputList,0,inputNumber-1)
    print("Maximum number is %d "%(inputList[-1]))


if __name__=="__main__":
    main()