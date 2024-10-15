f=open("abc.txt","r+")
print(f.read(6))
print(f.closed)  #check whether the file is closed or not
f.close() #file will be closed now
print(f.closed) #check again file is closed or not-returns True