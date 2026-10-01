def isDivByTwo(a:int, b:int)->bool:

    if((a%2==0)and(b%2==0)):
        return True
    else:
        return False

print(isDivByTwo(2,3))


def passingList(aList):
    temp = aList[0]
    aList[0]= aList[-1]
    aList[-1] = temp

li = [1,2,3,4]
passingList(li)
print(li)
print()

if __name__=="__main__":
    print("Hello World!")
    print(isDivByTwo(2,4))
