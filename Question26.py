import functools

def main():
    inputNumber=int(input("Enter NUmber you want in list"))
    inputList=[input("Enter number for list") for index in range(inputNumber)]
    print("The maximum number from list is ")
    print(functools.reduce (lambda a , b : a if a > b else b ,inputList) )

if __name__=="__main__":
    main()    