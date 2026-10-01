def productOrSum()-> float:

    numOne = int(input("Enter the first number that you would like to use:"))
    numTwo = int(input("Enter the second number that you would like to use:"))

    if((numOne*numTwo)<=1000):
        return(numOne*numTwo)
    else:
        return(numOne+numTwo)

print(productOrSum())