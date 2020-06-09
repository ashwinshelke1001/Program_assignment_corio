def main():
    filename=input("Enter the filename ")
    fp=open(filename,"r")
    dictionary={}
    for char in fp.read():
        if char  not in dictionary:
            dictionary[char]=1
        else :
            dictionary[char]+=1
    for char in sorted(dictionary.keys()):
        print(" %c | %d "%(char,dictionary[char]))
    fp.close()
main()