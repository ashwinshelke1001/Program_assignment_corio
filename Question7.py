def reverseList(argument):
    returnString=''
    '''for interator in argument:
        returnString= interator + returnString
    return returnString '''
    #by recusrsion 
    if (len(argument)==0):
        return returnString
    else :
        return reverseList(argument[1:]) + argument[0]

def main():
    inputString=input("Enter string")
    returnString=reverseList(inputString)
    print(" Reverse string is %s "%(returnString))

if __name__=="__main__" :
    main()
