def MaxFunction ( Argument1 , Argument2 ):
    if ( Argument1 > Argument2) :
        return Argument1 
    elif ( Argument2 > Argument1):
        return Argument2
    else :
        return -1
def main():
#    Argument1=float(input("Enter The Number1: "))
#    Argument2=float(input("Enter The Number2: "))


# if the argument taken by list comprehension 
    Argument1 ,Argument2 =[float(Argument1) for Argument1 in input ("Enter 2 Values").split()]
    ReturnVariable=MaxFunction(Argument1,Argument2)
    if (ReturnVariable== -1 ):
        print("The Number Is Equal")
    else :
        print("The Maximum Number Is %f "%ReturnVariable)
    
if __name__=="__main__":
    main()
    
