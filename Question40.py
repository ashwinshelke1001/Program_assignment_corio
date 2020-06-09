''' program of colour word anagram '''
import random
def main():
    colorWord=["black","brown","blue","red","yellow","pink","green","white","purple","violet","indigo"]
    randomIndex=random.randrange(0,(len(colorWord)-1))
    realColor=colorWord[randomIndex]
    tempList=list(realColor)
    random.shuffle(tempList)
    randomColor=''.join(tempList)
    print("Colour word anagram:  %s"%(randomColor))
    while True:
        guessColor=input("Guess the colour word!\n")
        if ( guessColor == realColor):
            print("Correct!")
            break
        
main()
