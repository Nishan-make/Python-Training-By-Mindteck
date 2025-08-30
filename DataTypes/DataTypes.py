print("Hello World")

#Primitive types -
int_number = 23
float_number = 7.3
is_done = True
text = "Welcome"
emptyValue = None

print("value of int_number - ", int_number, "of type ", type(int_number))
print("value of float_number - ", float_number, "of type ", type(float_number))
print("value of is_done - ", is_done, "of type ", type(is_done))
print("value of text - ", text, "of type ", type(text))
print("value of emptyValue - ", emptyValue, "of type ", type(emptyValue))
print("\n" + "-"*25 + "\n")

#Non Primitive types - 
cords = ("A", "B", "C", "D", "E", "F")  #Tuple
rollno = {1, 2, 3, 4, 5}  #set
personWithAge = {"Name":"John", "Age":30}  # Dictionary
fixedRollNo = frozenset(rollno)  #frozen set
names = ["aryan", "sakti", "salar", "aryan", 2, cords, rollno, personWithAge, fixedRollNo]   #List

range_numbers = range(1,5)
# range(start, stop, step)
# | Parameter | Meaning                          |
# | --------- | -------------------------------- |
# | `start`   | Starting value (inclusive) → `1` |
# | `stop`    | Ending value (exclusive) → `10`  |
# | `step`    | Interval between numbers → `2`   |



listofrange = list(range(1,5))

# print(names)
print(listofrange)
# print(rollno)
# print(personWithAge)
# print(fixedRollNo)
