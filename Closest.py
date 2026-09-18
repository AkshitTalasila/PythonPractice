def findClosest(numberList:list,findNumber:float)->int:

    difference =abs(numberList[0]-findNumber)
    index = -1
    for i in range(len(numberList)):
        if((abs(numberList[i]-findNumber))<=difference):
            difference = abs(numberList[i]-findNumber)
            index = i

    return index

print(findClosest([1.1,2.1,3.1,4.1,5.1], 3))

    