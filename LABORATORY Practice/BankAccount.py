from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance 

    @property
    def account_number(self):
        return self._account_number
    
    @property
    def balance(self):
        return self._balance
    
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def display_account_type(self):
        pass

class CurrentAccount(BankAccount):
    def deposit(self, amount):
        self._balance += amount
    
    def withdraw(self, amount):
        if self._balance - amount >= -5000:
            self._balance -= amount
        else: 
            print("Overdraft limit exceeded!")
    
    def display_account_type(self):
        return "Current Account"
    

class SavingsAccount(BankAccount):
    def deposit(self, amount):  
        self._balance += amount

    def withdraw(self, amount):
        if self._balance - amount >= 0:
            self._balance -= amount
        else: 
            print("Insufficient funds!")

    def display_account_type(self):
        return "Savings Account"
    
def print_account_details(account):
    print(f"Account Number: {account.account_number}")
    print(f"Balance: {account.balance}")
    print(f"Type: {account.display_account_type()}")
    print("-" * 30)


sa1 = SavingsAccount("SA123", 1000)
sa2 = SavingsAccount("SA124", 1500)
ca1 = CurrentAccount("CA456", 500)
ca2 = CurrentAccount("CA457", -400)

sa1.deposit(200)
sa1.withdraw(100)
ca1.withdraw(800)
ca2.withdraw(4700)
ca2.withdraw(1000)

print_account_details(sa1)
print_account_details(sa2)
print_account_details(ca1)
print_account_details(ca2)