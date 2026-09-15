from BankAccount import BankAccount

class Main:

    hsbc = BankAccount()
    hsbc.deposit(100)
    print(hsbc.getBalance())
    hsbc.withdraw(50)
    print(hsbc.getBalance())

