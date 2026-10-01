def evenIndex():

    print("This program prints only the letter at the even indicies of the word you are going to enter")
    word = str(input("Please enter the word that you would like to be printed"))
    for i in range(len(word)):
        if((i%2)==0):
            print(word[i])

evenIndex() 