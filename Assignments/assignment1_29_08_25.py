# Write a Python program that manages a list of student scores. Perform the following operations step-by-step:


# Create an empty list to store scores.
mySpecialList = []
print("Blank List")
print(mySpecialList)

# Append the scores: 85, 90, 78, 92, 88
mySpecialList.append(85)
mySpecialList.append(90)
mySpecialList.append(78)
mySpecialList.append(92)
mySpecialList.append(88)
print("List after appending 5 elements")
print(mySpecialList)

# Insert the score 80 at index 
mySpecialList.insert(3, 80)  # Inserts 80 at index 3
print("List after appending an elements at particular index")
print(mySpecialList)

# Remove the score 92 from the list
mySpecialList.remove(92)
print("List after removing 92")
print(mySpecialList)

# Sort the scores in ascending order
mySpecialList.sort()
print("List after Sorting in ascending order")
print(mySpecialList)

# Reverse the list
mySpecialList.reverse()
print("List after reversing")
print(mySpecialList)

# Find and print the maximum and minimum score
# As list is now sorted in reverse of ascending order we can get max and min using index number
print("Max Value - ", mySpecialList[0])
print("Min Value - ", mySpecialList[-1])
#             or
# print("Max Value - " + max(mySpecialList))
# print("Min Value - " + min(mySpecialList))

# Check if 90 is in the list
# Making it as general
searchElement = int(input("Enter a number want to search in the list: "))
if searchElement in mySpecialList:
    print(searchElement, " is in the list")
else:
    print(searchElement, " is not in the list")

# Print the total number of scores
sum = 0
for i in mySpecialList:
    sum+= i
print("Sum of all - ", sum)

# Slice and print the first three scores
fewElements = mySpecialList[:3]
print("After slicing, printing first 3 elements -",fewElements)