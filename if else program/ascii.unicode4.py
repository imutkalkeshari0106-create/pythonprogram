print("enter a upper char")
ch=input()
if len(ch)!=1:
	print("single chae allow")
	sys.exit()
if ch>='A' and ch<='z':
	x=ord(ch)+32
	print(chr())