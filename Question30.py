import sys

def translateFunction(argumentString):
    d={"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", 
        "new":"nytt", "year":"ar"}
    newString=''
    if argumentString not in d :
        print("%s is not defined in dictonary"%(argumentString))
        sys.exit()
    else :
        newString +=d[argumentString] 
    return newString    
    

def main():
    inputString=input("Enter words which u want to translate put sapce while entering ")
    inputString=inputString.split(' ')
    returnString=' '.join(list(map(translateFunction,inputString)))
    print(returnString)

if __name__=="__main__":
        main()
