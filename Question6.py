def sumFuction(argument):
    totalSum=0
    for iterator in range(len(argument)):
        totalSum+= argument[iterator]

    return totalSum

def multiplyFuction(argument):
    totalMultiplication=1
    for iterator in range(len(argument)):
        totalMultiplication*= argument[iterator]

    return totalMultiplication
        


def main():
    inputList=[]
    numberOfElementInList=int(input("enter number that you want in List"))
    for iterator in range (numberOfElementInList):
        elementOfList=float(input("enter list elem."))
        inputList += [elementOfList]
        #inpuList.append(elementOfList)
#    print(inputList)
    returnSum=sumFuction(inputList)
    print("The sum of all element in list is %d "%returnSum)
    returnMultiplication=multiplyFuction(inputList)
    print("The sum of all element in list is %d "%returnMultiplication)



if __name__=="__main__":
        main()
