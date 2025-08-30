marks = 90
if marks >= 90 :
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")

# in if else we can check the range but in switch we can check only matching element
#Switch - case
match marks:
    case 90:
        print("Excellent")
    case 80:
        print("Very Good")
    case _:
        print("Scope of improvement")

#Using Indexing
if marks >= 90 :
    print("Grade A")
else:
    if marks >= 80:
        print("Grade B")
    else:
        if marks >= 70:
            print("Grade C")
        else:
            if marks >= 60:
                print("Grade D")
            else:
                print("Grade F")