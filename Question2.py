def Max_Of_Three ( Argument1 , Argument2 , Argument3):
    if ( Argument1 >= Argument2 ) and ( Argument1 >= Argument3) :
        Largest=Argument1
    elif ( Argument2 >= Argument1 ) and ( Argument2 >= Argument3) :
        Largest=Argument2
    else :
        Largest=Argument3
    return Largest

def main():
    #input is taken by list comprehension 
    Number1,Number2,Number3= [float (Number1) for Number1 in input("Enter 3 Number" ).split()]
    Largest=Max_Of_Three(Number1,Number2,Number3)
    print("The Maximum Number Is %f",Largest)

if __name__=="__main__":
    main()
