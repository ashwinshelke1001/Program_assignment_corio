def histogram(argumentList):
    index=0
    while(index < len(argumentList)):
        printstring=''
        printstring = argumentList[index] * "*"
        print(printstring)
        index+=1
     

def main ():
    inputList=[]
    inputNumber=int(input("enter number u want in list"))
    for index in range(inputNumber):
        inputElement=int(input("enter element for lisr"))
        inputList +=[inputElement]
    histogram(inputList)

if __name__=="__main__" :
    main()