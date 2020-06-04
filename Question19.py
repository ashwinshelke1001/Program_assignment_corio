def main():
    i=3
    while (i >0):
        print("%d bottles of beer on the wall, %d bottles of beer."%(i,i))
        i-=1
        if( i!= 0):
            print("Take one down, pass it around, %d bottles of beer on the wall."%(i))
        else:
            print("Take one down, pass it around, no more beer on the wall.")

if __name__=="__main__":
        main()

    
