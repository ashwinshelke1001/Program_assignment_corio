import os
import time
def speak_ICAO(argumentMess,timeLetter,timeWord):
    d={'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot',
     'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima',
     'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo',
     's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey', 
     'x':'x-ray', 'y':'yankee', 'z':'zulu'}
    
    for char in argumentMess :
        if char in d.keys():
            os.system(' echo '+ d[char] )
            os.system(' say '+ d[char])
        else :
            os.system(' echo '+ char )
            os.system(' say '+  char)
            print("\n")
        time.sleep(timeLetter)

def main():
    mess=input("Enter message : \n")
    timeInLetter=float(input("ente time between letters : \n"))
    timeInWord=float(input("ente time between letters : \n"))
    speak_ICAO(mess,timeInLetter,timeInWord)
main()