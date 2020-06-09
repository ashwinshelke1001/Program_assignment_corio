from collections import defaultdict

def alternade(words):
    alternadeList=defaultdict(list)
    for word in words:
        alternadeList[word]=1

    for word in words:
        if len(word)>1:
            if alternadeList[word[0::2]]==1  and alternadeList[word[1::2]]==1:
                print("\"%s\": makes \"%s\" and \"%s\"."%(word,word[0::2],word[1::2]))

def main():
    fileName=input("Enter file name : \n")
    fp=open(fileName,"r")
    words=fp.read().split()
    fp.close()
    alternade(words)

main()

    
