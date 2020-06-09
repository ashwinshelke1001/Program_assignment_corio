def main():
        lineNumber=1
        readFile=input("Enter the filename you want to read:\n")
        fread=open(readFile,"r")
        writeFile=input("Enter the filename you want to write:\n")
        fwrite=open(writeFile,"w")
        for lines in fread.readlines():
            fwrite.write(" %d  "%(lineNumber))
            fwrite.write(lines)
            lineNumber+=1
        fread.close()
        fwrite.close()
        fp=open(writeFile)
        print(fp.read())
        fp.close()

main()
            



