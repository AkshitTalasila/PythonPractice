def iterateSum():

    userInput = int(input("Please enter the range of numbers that u want the sums for"))
    numList = list(range(userInput))

    i = 0
    while(i<(len(numList))):

        if(i==0):
            print("Current Number"+str(numList[i]) +"Previous Number 0 Sum: 0")
            i+=1
        else:
            print("Current Number"+str(numList[i]) +"Previous Number "+str(numList[i-1]) +"Sum: "+str((numList[i]+numList[i-1])))
            i+=1

iterateSum()