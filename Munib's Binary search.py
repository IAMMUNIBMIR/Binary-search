Found = False
myList = [16, 19, 21, 27, 36, 42, 55, 67, 76, 89]
upperBound = len(myList) - 1
lowerBound = 0
item = 0
Counter = 0
index = 0

InputDone = False

while InputDone == False:

    InputValue = (input("Please enter a value to add to the list or enter an empty string"))
    try:
        int(InputValue)
        myList.append(int(InputValue))
    except: 
        InputDone = True
        break
print(myList)


item = int(input("Please enter an item to search"))

while not Found and upperBound >= lowerBound:
    
    index = ((upperBound + lowerBound)//2)

    Counter += 1

    if myList[index] == item:
        Found = True
        break
    if item > myList[index]:
        lowerBound = index + 1

    if item < myList[index]:
        upperBound = index - 1

if Found == False:
    print("Item not found in the list")
else:
    print (Counter, item) 


