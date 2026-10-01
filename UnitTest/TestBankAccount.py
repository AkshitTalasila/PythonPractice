import unittest
from BankAccount import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):

        self.obj = BankAccount(100)

    def TearDown(self):

        del self.obj

    def testStartingBalance(self):

        self.assertEqual(self.obj.balance,100)

    def testDeposit(self):

        self.assertEqual(self.obj.deposit(10),110)

    def testWithdraw(self):

        self.assertEqual(self.obj.withdraw(10),90)

    def testAmount(self):

        self.assertEqual(self.obj.getBalance(),100)

if __name__=="__main__":

     unittest.main()