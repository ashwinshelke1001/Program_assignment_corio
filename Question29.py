

def main():
    inputIntValue=int(input("enter the number"))
    inputList=[input("Enter words  ")for index in range(inputIntValue)]
    rangeVariable=int(input("Enter no."))
    newList=list(filter(lambda a : len(a) > rangeVariable ,inputList))
    print("words greater than inputnumber is %s"%(newList))
if __name__=="__main__":
    main()    
