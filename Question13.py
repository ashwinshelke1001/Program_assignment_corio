def functionOfMaxElement(inputList,inputNumber):
    maxNumber=inputList[0]
    for index in range(1,inputNumber):
        if inputList[index]>maxNumber:
            maxNumber=inputList[index]
    return maxNumber        



def main():
    inputList=[]
    inputNumber=int(input("enter number u want in list \n"))
    for index in range(inputNumber):
        inputElement=int(input("enter element for list \n"))
        inputList +=[inputElement]
    maxNumber=functionOfMaxElement(inputList,inputNumber)
    print("Maximum number is ",maxNumber)


if __name__=="__main__":
    main()
