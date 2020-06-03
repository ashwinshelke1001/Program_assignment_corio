def isPallindrome(argument):
    iterator1=0 
    iterator2=len(argument)-1
    while ( iterator1 < iterator2 ):
        if ( argument[iterator1] != argument[iterator2]):
            return False
        iterator1+=1
        iterator2-=1
    return True 


def main():
    inputString=input("Enter string")
    returnvalue=isPallindrome(inputString)
    if (returnvalue == True):
        print("string is pallindrome")
    else :
        print("string is  not pallindrome")

if __name__=="__main__":
    main()