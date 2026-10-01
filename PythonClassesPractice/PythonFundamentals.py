def addTax()->float:

    price = float(input("Please enter the price of the item: "))
    quantity = int(input("Please enter the number of items you are purchasing: "))

    return(((price*quantity)*0.08)+(price*quantity))

def capitalizeName(name)->str:

    spaceIndex = name.find(" ")
    firstName = name[:spaceIndex]
    lastName = name[spaceIndex+1:]

    firstName = firstName.capitalize()
    lastName = lastName.capitalize()

    return(firstName+" "+lastName)

def grader(score:int)->str:

    if((score>=90)):
        return("A")
    elif((score<90)and(score>=80)):
        return("B")
    elif((score<80)and(score>=70)):
        return("C")
    elif((score<70)and(score>=55)):
        return("D")
    else:
        return("F")

def isPrime(number)->bool:

    for i in range(2,number):
        if(number == 2):
            return(True)
        elif((number%i)==0):
            return(False)

    return(True)


#print(addTax())
#print(capitalizeName("ada lovelace"))
#print(grader(98))
#print(isPrime(100895953))




