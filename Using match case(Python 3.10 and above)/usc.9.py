data=[1,2]

match data:
	case [1,2]:
		print("Matched")
	case [1, x]:
		print("Second value =", x)
	case _:
		print("No Match")