#while
print("While Loop")
number = 1
while number <= 10:
    print(number)
    number += 1

#do while - execute atleast one time
print("Do - While Loop")
number = 1
while True: 
    print(number)
    number += 1
    if number > 5:
        break

#for, continue and break
# for this loops it does not include maxrage

listofrange = list(range(1,5))
print(listofrange)  # print 1, 2, 3, 4

print("for Loop")
for i in range(1,10): #iterate 1 to 9, i.e less than 10 
    if i == 5:
        continue
    # if i == 8:
    #     break
    print(i)