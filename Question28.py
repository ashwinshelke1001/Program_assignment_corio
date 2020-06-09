import functools

def main():
    inputList=input("enter strings with white space in between ")
    inputList=inputList.split(" ")
    lambdaVar= lambda a , b : a if len(a) > len (b) else b
    outputValue= functools.reduce(lambdaVar,inputList)
    print(len(outputValue))   

    
if __name__=="__main__":
    main()    
