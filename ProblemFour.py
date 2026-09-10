def stringSlicing():

    print("This program is going to splice the word that you are going to enter up until the number you specify")
    word = str(input("Please enter the word you want to splice"))
    index = int(input("Please enter the number of letters to include in the word"))

    print(word[index:len(word)])

stringSlicing()