marks = int(input("Please enter your Mark - "))
#Using if-elif-else
Grade = ""
if marks >= 90 :
    Grade = "A"
elif marks >= 80:
    Grade = "B"
elif marks >= 70:
    Grade = "C"
elif marks >= 60:
    Grade = "D"
else:
    Grade = "F"
print("After Using if-else, Grade - ", Grade)

#Using Nested if-else
Grade = ""
if marks >= 90 :
    Grade = "A"
else:
    if marks >= 80:
        Grade = "B"
    else:
        if marks >= 70:
            Grade = "C"
        else:
            if marks >= 60:
                Grade = "D"
            else:
                Grade = "F"
print("After Using Using nested if-else, Grade - ", Grade)



