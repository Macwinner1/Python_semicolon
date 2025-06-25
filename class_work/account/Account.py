class Account:
    def __init__(self, first_name, balance = 0.0):
        self.first_name = first_name
        self.balance = balance

    def withdraw(self, amount):
        print("Withdraw amount")
        self.balance -= amount

    def deposit(self, amount):
        print("account deposited")
        self.balance += amount

    def show_balance(self):
        print("Balance is", self.balance)

oba = Account("OBA", 40000)
oba.withdraw(1100)
oba.show_balance()