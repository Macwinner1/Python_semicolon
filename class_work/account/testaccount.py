import unittest
import Account

class MyTestCase(unittest.TestCase):
    def test_that_account_can_be_added(self):
        Account.Account("Oba", 0)

    def test_withdraw(self):
        self.assertEqual(Account.Account("Oba", 100).withdraw(100), 0)

    def test_deposit(self):
        self.assertEqual(Account.Account("Oba", 0).deposit(1000), 1000)

    def test_show_balance(self):
        self.assertEqual(Account.Account("Oba", 1450).show_balance(), 1450)


if __name__ == '__main__':
    unittest.main()
