def main():
    wordList={}
    fileName=input("Enter the filename : \n")
    fp=open(fileName,"r")
    for word in fp.readlines():
        wordList[word[:-1]]=0
    fp.close()
    for word in wordList.keys():
        if (word[::-1] in wordList.keys()) and  (wordList[word]==0 ) and (word[::-1] != word):
            print("%s  %s"%(word,word[::-1]))
            wordList[word[::-1]]=1
    
main()
