def encode(argumentList):
    encodedString=''
    for char in argumentList:
        if ( char >= "A" and char<= "Z") :
            encodedString += chr((ord(char) + 13-65) % 26 + 65) 
        elif ( char>="a" and char<="z"):
            encodedString += chr((ord(char) + 13-97) % 26 + 97) 
        else :
            encodedString += char
    return encodedString
def decode(argumentList):
    decodedString=''
    for char in argumentList:
        if ( char >= "A" and char<= "Z") :
            decodedString += chr((ord(char) - 13-65) % 26 + 65) 
        elif ( char>="a" and char<="z"):
            decodedString += chr((ord(char) - 13-97) % 26 + 97) 
        else :
            decodedString += char
    return decodedString
                

def main():
    string=input("Enter string ")
    option=int(input(" For encondin press 1 and For decoding press 0"))
    if option==1 :
        print(encode(string))
    else :
        print(decode(string))

if __name__=="__main__":
        main()
