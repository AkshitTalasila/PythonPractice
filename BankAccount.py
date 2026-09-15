class BankAccount:

    def __init__(self):

        self.balance = 0

    def withdraw(self,amount):

       self.balance = self.balance-amount 

    def deposit(self,amount):

        self.balance = self.balance+amount

    def getBalance(self)->str:

        return("$"+str(self.balance))
