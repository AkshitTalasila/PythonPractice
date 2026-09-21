#Code for is_prime function
def is_prime(n):

    if(n<=1):
        return False
    elif(n ==2):
        return True
    else:
        for i in range(2,n):

            if((n%i) ==0):
                return False

    return True

#Code for is_relatively_prime function
def are_relatively_prime(x,y):

    for i in range(2,x+1):
        if(((x%i)==0) and ((y%i)==0)):
            return False

    return True

#Code for primes_up_to(n) function

def primes_up_to(n):

    primeList =[]
    for i in range(n):
        if((is_prime(i))==True):
            primeList.append(i)

    return primeList

#Code for prime_decomposition(n) function

def prime_decomposition(n):

    factorList =[]
    divisor =2

    while(n>1):
        if((n%divisor)==0):
            factorList.append(divisor)
            n=n//divisor
        else:
            divisor+=1

    return factorList

#Code for decom_check(n) function

def decomp_check(n):

    checkList = prime_decomposition(n)

    if((len(checkList)==2)and(checkList[0]!=checkList[1])):
        return True
    return False

def toBytes():

    string = input("Please enter a word")

    bits = ""

    for i in range(len(string)):

        bits = bits+" "+str(bin((ord(string[i]))))

    print(bits)

toBytes()
