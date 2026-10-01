#asking for names of both the users
name1 = str(input("Please enter the name of Person 1: "))
name2 = str(input("Please enter the name of Person 2: "))
#asking for ages of both the users
age1 = int(input("Please enter the age of Person 1: "))
age2 = int(input("Please enter the age of Person 2: "))

#conditional statements which check the age of both the users against each other and perform an operation based on the result
if(age1>age2):
    print(name1+" is "+str((age1-age2))+" years older than "+name2)
elif(age2>age1):
    print(name2+" is "+str((age2-age1))+" years older than "+name1)
else:
    print(name1+" is the same age as "+name2)


