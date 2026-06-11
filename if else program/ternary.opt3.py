print("enter basic sal")
sal=float(input())
da=sal*0.3if sal>5000 else sal*0.2
hra=sal*0.2 if sal>=5000 else sal*0.1
totalsal=sal+da+hra
print("basic sal=",sal)
print("da=",da)
print("hra=",hra)
print("totalsal=",totalsal)