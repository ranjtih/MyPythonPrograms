name=input("enter the name\n")
len=len(name)
for i in range(0,len):
	if(ord(name[i])>=97 and ord(name[i])<=125):
		print(chr(ord(name[i])-32),end="")
	if(ord(name[i])>=65 and ord(name[i])<=90):
		print(chr(ord(name[i])+32),end="")
