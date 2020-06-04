def translate(argumentList):
    newList=''
    diction={ "merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}
    for i in argumentList.split():
        if ( i in diction):
            newList += diction[i]
            newList += " "
        else :
            newList +="."
            return newList
    return newList        
def main():
    string=input("Enter message ")        
    print(translate(string))

if __name__=="__main__":
        main()
