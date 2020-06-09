def main():
    filename=input("Enter the filename ")
    fp=open(filename,"r")
    dictionary={}
    word=fp.read()
    word=word.split()
    for char in word:
        if char not in dictionary:
            dictionary[char]=1
        else :
            dictionary[char]+=1
    print(" hapax legomenon word from file is ")
    for char in word :
        if (dictionary[char]==1):
            print(char)

    fp.close()
main()