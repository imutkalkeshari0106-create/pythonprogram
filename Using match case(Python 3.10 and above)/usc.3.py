grade = input("Enter Grade (A/B/C/D): ")

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Very Good")
    case "C":
        print("Good")
    case "D":
        print("Needs Improvement")
    case _:
        print("Invalid Grade")