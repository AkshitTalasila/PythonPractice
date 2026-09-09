for i in range(10):
    print(i)

def whileLoop():
    i =4
    while(i<23):
        print(i)
        i +=1
whileLoop()

def loopOverList():
    numList = [1,2,3,4,5]
    numTuple = (1,2,3,4,5)
    for number in numList:
        print(number)

    i=0;
    while(i<len(numTuple)):
        print(numTuple[i])
        i+=1


print()
print()
loopOverList() 