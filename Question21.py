def charFreq(string):
    dictionary={}
    for i in string:
        if  ( i not in dictionary):
            dictionary[i]=1
        else :
            dictionary[i] +=1
    print(dictionary)

def main():
    string=input("enter string")
    charFreq(string)

if __name__=="__main__":
        main()
  
