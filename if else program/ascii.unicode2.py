print("enter a char")
ch=input()
if len(ch)!=1:
	print("single char allow")
	sys.exit()
if ch>='A' and ch<='Z':
	PRINT("upper case"