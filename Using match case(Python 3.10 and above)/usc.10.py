data= [1, [2,3]]
match data:
	case[1, [a,b]]:
		print(a,b)
	case _:
		print("No match")