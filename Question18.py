def ispangram(str):
   alphabet = "abcdefghijklmnopqrstuvwxyz"
   for char in alphabet:
      if char not in str.lower():
         return False
   return True

def main():
   string=input("enter string")
   returnValue=ispangram(string)
   if (returnValue==True):
      print("String is panagram")
   else :
      print("string is not panagram")

if __name__=="__main__":
        main()
