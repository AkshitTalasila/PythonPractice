
#Declaring the funtion
def passwordChecker(password):

    #checking weather the password is 8 characters
    if(len(password)!=8):
        return(False)

    #initializing the first and second letter of the password
    firstLetter = password[0]
    secondLetter = password[1]

    #checking if the first or second letter is lower case or if they are equal to each other
    if((firstLetter.islower())or(secondLetter.islower()) or (firstLetter==secondLetter)):
       return(False) 

    #initializing the sum variable to check if the digits add up to an even number
    digitSum=0

    #adding all the digits in the password to digitSum
    for i in range(len(password)):
        if(password[i].isdigit()):
            digitSum+=int(password[i])

    #checking if the sum of the digits in the password is an even number
    if((digitSum%2)!=0):
        return(False)

    #checking for special characters or spaces in the password
    if (not(password.isalnum())):
        return(False)

    #returning true if the password passes all the conditions
    return(True)
