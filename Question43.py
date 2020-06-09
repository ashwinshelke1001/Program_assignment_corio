def main():
    words=[]
    fileName=input("Enter file name : \n")
    fp=open(fileName,"r")
    dictionary={}
    for word in fp.readlines():
        sortedKey=''.join(sorted(word[:-1]))
        if sortedKey not in dictionary :
            dictionary[sortedKey]=[word[:-1]]
        else :
            dictionary[sortedKey]+=[word[:-1]]
    max=0
    for key in dictionary.keys() :
        if len(dictionary[key]) > max :
            max=len(dictionary[key])
    for key in dictionary.keys() :
        if len(dictionary[key]) == max :
            print(dictionary[key])

main()