def say_hello():
    print("Hello")
    print("This is a part of the hello function")

def say_bye():
    print("Bye")
    print("This is a part of the bye function")

def say_welcome(name:str)->str:
    return(name )

say_hello();
say_bye();
statement = say_welcome(3)
print(statement)