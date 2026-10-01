def exerciseOne():
    numOne = int(input("Enter the first number: "))
    numTwo = int(input("Enter the second number: "))
    sum = numOne+numTwo
    print("The sum of both the numbers is:"+str(sum))

def exerciseTwo():
    numOne = int(input("Enter the first number: "))
    numTwo = int(input("Enter the second number"))
    numThree = int(input("Enter the thirdNumber"))
    numFour = int(input("Enter the fourthNumber"))

    print("The avg of all number is: ", str((numOne+numTwo+numThree+numFour)/4))

def exerciseThree():
    name = str(input("What is your name? "))
    age = int(input("What is your age?"))

    print("Hello "+name+" of age "+str(age))

def tempConvert(temp:float) -> float:
    tempInCelsius =(temp-32)/1.8
    return(tempInCelsius) 

#exerciseOne()
#exerciseTwo()
#exerciseThree()
temp = tempConvert(100)
print(temp)