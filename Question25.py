vowelString="aeiouAEIOU"
consonantString="QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklmnbvcxz"
exceptionList=["be","see","flee","knee"]
def makeIngForm(argumentList):
    if argumentList.endswith("e") and argumentList not in exceptionList:
        argumentList= argumentList[:-1] + "ing"
    elif  argumentList.endswith("ie"):
        argumentList= argumentList[:-2] + "ying"
    elif  argumentList[-1] in consonantString and argumentList[-2] in vowelString and argumentList[:-2] in consonantString :
        argumentList= argumentList + argumentList[-1] +"ing"
    else :
        argumentList= argumentList +"ing"
    return argumentList
    

def main():
    inputString=input("Enter string ")
    print(makeIngForm(inputString))

if __name__=="__main__":
        main()
