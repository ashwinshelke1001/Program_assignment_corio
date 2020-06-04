
def thirdPersonSingular(argumentList):
    if argumentList.endswith("y"):
        argumentList= argumentList[:-1] + "ies"
    elif (argumentList.endswith("o") or argumentList.endswith("s")
     or argumentList.endswith("z") or argumentList.endswith("x") or argumentList.endswith("sh") 
        or argumentList.endswith("ch")) :
    
        argumentList= argumentList + "es"
    
    else :
        argumentList= argumentList + "s"
    return argumentList

def main():
    inputString=input("Enter string")
    print(thirdPersonSingular(inputString))

if __name__=="__main__":
        main()
