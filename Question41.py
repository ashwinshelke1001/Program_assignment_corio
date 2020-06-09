def main():
    originalWord="tiger"
    while True:
        tempString=''
        tempNewString=''
        userWord=input("Enter word  for start game :\n")
        if (userWord == originalWord ):
            break 
        for index in range (len(userWord)) :
            if userWord[index] == originalWord[index] :
                tempString += "[" + userWord[index] + "]" 
            else :
                tempString += userWord[index]
                tempNewString += originalWord[index]
        for index in range(len(tempString)):
            if (tempString[index]== "["):
                index +=2
            elif tempString[index] in tempNewString :
                tempNewString=tempNewString.replace(tempString[index],'')
                tempString = tempString[:index] + "(" + tempString[index] + ")" + tempString[index+1:]
                index+=2
        print (tempString)






main()