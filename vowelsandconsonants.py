s="hello"
s1=s.upper()
vcount=0
ccount=0
for i in range(0,len(s)):
	if(s1[i]=='A' or s1[i]=='E'  or s1[i]=='O'  or s1[i]=='U' or s1[i]=='I'):
		vcount=vcount+1
	else:
		ccount=ccount+1
print(vcount,ccount)
		
