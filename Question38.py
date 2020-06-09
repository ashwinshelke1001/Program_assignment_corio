def main():
    filename=input("Enter the filename ")
    fp=open(filename,"r")
    dictionary={}
    wordList=fp.read()
    wordList=wordList.split()
    total=0
    for words in wordList :
        total+=len(words)
    average=total/len(wordList)
    print(" average is %d "%(average))
    fp.close()
main()


