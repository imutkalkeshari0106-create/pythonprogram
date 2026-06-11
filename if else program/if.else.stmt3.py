print("enter basic sal")
sal=float(input())
if sal>=5000:
	da=sal*0.3
	hra=sal*0.2
else:
	da=sal*0.2
	hra=sal*0.1
totalsal=sal+da+hra
print("basic sal=",sal)
print("hra",hra)
print("totalsal=",totalsal)