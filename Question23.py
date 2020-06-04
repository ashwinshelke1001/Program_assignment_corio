import re
def correct (argumentList):
#    argumentList=re.split("\s*",argumentList)
    argumentList=re.sub('\ +',' ',argumentList)
    index=re.search('\.\w',argumentList)
    while (index):
        index=index.start()
    #    print(index)
        argumentList=argumentList[:index] + '. ' + argumentList [index+1:] 
        index=re.search('\.\w',argumentList)
        
#    argumentList=re.sub('\.','. ',argumentList)
    return argumentList


def main():
    inputString=input("Enter string")
    print(correct(inputString))

if __name__=="__main__":
        main()
