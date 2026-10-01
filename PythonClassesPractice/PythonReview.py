def findSmaller():

    userList =[]
    userInput = input("Please enter STOP to stop")

    while(userInput !="STOP"):
        userList.append(int(userInput))
        userInput = input("Please enter Stop to stop")

    minValue = userList[0]
    minIndex = 0

    for i in range(len(userList)):
        if(userList(i)<minValue):
            minValue = userList[i]
            minIndex = i

    return minIndex

