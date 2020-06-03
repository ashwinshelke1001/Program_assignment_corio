def overlapping(argumentList1, argumentList2):
    index1=0
    while(index1< len(argumentList1)):
        index2=0
        while(index2 < len(argumentList2)):
            if(argumentList1[index1] == argumentList2[index2]):
                return True
            else :
                index2 +=1
        index1 +=1
    return False


def main():
    inputList1=[]
    inputList2=[]
    inputNumber1,inputNumber2=  [int(inputNumber1) for inputNumber1 in input("Enter 2 number").split()]
    for index in range(inputNumber1):
        element1=input("enter element for list1")
        inputList1 +=[element1]

    for index in range(inputNumber2):
        element2=input("enter element for list2")
        inputList2 +=[element2]

    returnValue=overlapping(inputList1,inputList2)
    if ( returnValue == True):
        print("Common Element is present")
    else :
        print("No common element ")

if __name__=="__main__":
    main()        