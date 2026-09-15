
#Declaring Function
def numberAverage(treshold):

    #nitializing up the default values
    negativeNumberEntered = False
    numberList =[]

    #Starting the while loop to ask the users for the numbers
    while(negativeNumberEntered==False):

        numberToAdd = float(input("Plese enter a number to add to the list(Enter a negative number to stop):  "))

        #Conditional statements to break the loop if any of the number entered is negative
        if(numberToAdd<0) :
            negativeNumberEntered = True
            break
        else:
            numberList.append(numberToAdd)

    #Initializing the default sum value
    sum = 0

    #Created a new list so that even when the user enter two numbers which are below the threshold beside each other,
    #it would remove both of them and prevents the list.remove() funtion from skipping over it
    numberListChecker = numberList.copy()

    #loop to check and remove the numbers in the list which are below the threshold
    for i in numberListChecker:
        if(i<=treshold):
            numberList.remove(i)
        else:
            sum+=i

    #conditional statements to make sure that there are numbers in the list before dividing by the length of the list
    if(len(numberList) == 0):
        print("Please enter positive numbers and numbers above the threshold to run the program")
    else:
        return(sum/len(numberList))


#statement to display the output
print(numberAverage(15))

