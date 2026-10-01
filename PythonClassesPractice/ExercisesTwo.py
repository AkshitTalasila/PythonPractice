def maxValue(numList:list)->int:
    maxVal = numList[0]
    for number in numList:
        if number > maxVal:
            maxVal = number
    return maxVal

def maxValueTwo(numList:list)->int:
    maxVal = numList[0]
    i=0
    while(i<len(numList)):
        if(numList[i]>maxVal):
            maxVal = numList[i]
        i +=1
    return maxVal

def avgList()-> float:
    numList=[]
    for i in range(5):
        numList.append(int(input("Please enter a number to the list:")))

    sum =0
    for number in numList:
        sum+=number

    return("avg =",sum/5)

def userAvgList()->float:
    numList =[]

    while True:
        number =int(input("Enter a number to the list, if the number is zero, the list will stop"))
        numList.append(number)
    
        if(number ==0):
            break

    sum =0
    for number in numList:
        sum+=number
    return("avg", sum/len(numList))


maxList = [1,2,3,4,5,6,100]
maxTuple = [1,100,2]
print(str(maxValue(maxList)))
print(str(maxValueTwo(maxTuple)))
print(str(avgList()))
print(str(userAvgList()))