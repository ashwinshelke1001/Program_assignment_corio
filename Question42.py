def main():
    fname=input("Enter file name : \n")
    fp=open(fname,"r")
    txt=fp.read()
    i=0
    period=['.','?','!']
    while i <(len(txt)):
        if txt[i] in period and  txt[i+1]==' ' and ord(txt[i+2]) < 97 :
            if txt[i-2:i]!='Mr' and txt[i-3:i]!='Mrs' and txt[i-2:1]!='Dr':
                print(txt[i])
                i+=1
            else:
                print(txt[i],end='')
        else :
            print(txt[i],end='')
        i+=1
main()