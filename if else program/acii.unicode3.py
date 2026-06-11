print("enter a char")
ch=input()
if len(ch)!=1:
	print("single char allow")
	sys.exit()
x=ord(ch)
if x>=97 abd x<=122:
	print("lower case")