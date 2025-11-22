# Classes, Objects, Instance Variables, Methods

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. Balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdraw. Balance: {self.balance}")
        else: 
            print("insufficient balance")

    def show_balance(self):
        print(f"current balance: {self.balance}")

acc = BankAccount("Saed", 1000)
acc.deposit(500)
acc.withdraw(300)
acc.show_balance()