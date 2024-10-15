try:
    f1=open("foo.txt","r")
except FileNotFoundError:
    print("\n file doesn't exists")
else:
    print("type of file:",type(f1))
    print("Name of the file:",f1.name)   #print name of the file -foo.txt
    print("is file readable:",f1.readable())   #True
    print("is file writable:",f1.writable())   #False because mode of file is read
    print("is file closed:",f1.closed)        #file is not yet closed
    print("file mode is:",f1.mode)            #prints mode of the file -r
finally:
    #if f1 is not None:
        f1.close()                            #close the file
        print("is the file closed?",f1.closed) #returns True