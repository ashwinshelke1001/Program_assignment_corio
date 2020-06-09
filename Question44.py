def balanceParenthesis(argumentList):
    stack=[]
    for index in range (len(argumentList)):
        if argumentList[index] == "[" :
            stack.append(argumentList[index])
        else:   
            if stack == [] :
                return False 
                break
            elif argumentList[index] != stack[-1]:
                stack.pop()
            

    if (stack!= []):
        return False
    return True
             


def main():
    inputString=input("Enter parenthesis : \n")
    inputString=list(inputString)
    print(balanceParenthesis(inputString))

main()