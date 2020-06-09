import random
def main():
    number= random.randrange(1,20)
    name=input("What is your name ! ")
    print("Well, %s I am thinking of a number between 1 and 20."%(name))
    guessCount=0
    while True :
        guess=int(input("Enter Number "))
        
        if guess== number:
            guessCount +=1
            print("Good job, %s ! You guessed my number in %d guesses! "%(name,guessCount))
            break
        elif guess > number:
            guessCount +=1
            print("Your guess is too high.")
        else :
            guessCount +=1
            print("Your guess is too low.")
        
main()               
            