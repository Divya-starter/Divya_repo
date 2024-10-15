fp=open("xyz.txt","r+")
x=fp.readline(2)  #print 2 characters- same as read(2) output
print(x)
fp.seek(0)
print("\n")

y=fp.readline()
print("readline y:",y)  #print readline -single line
fp.seek(0)
print("\n")

k=fp.readlines(0)       #print all the lines with new line as ending
print("readline K:",k)
fp.seek(0)

k=fp.readlines()          #this also equal like above readlines(0) output
print("readline K:",k)       #print all the lines.
fp.seek(0)


s=fp.readlines(3)          #no .of bytes to read here is 3-hint
print("readline s:",s)
fp.seek(0)