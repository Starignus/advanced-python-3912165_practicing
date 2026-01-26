# Example file for Advanced Python by Joe Marini
# Defining and using custom exceptions in Python

# Define a custom exception class
# Good practice is to inherit from the built-in Exception class
# Use a drescriptive name for the exception
# Provide a docstring explaining when the exception is raised
# Keep it simple by aboiding adding unnecessary attributes or methods
# to your custom exeption class and keep it focused to the error condition that it represents

class InsufficientFundsError(Exception):
    "Raised when an account has insufficient funds for a transaction"
    def __init__(self, balance, amount):
        message = f"Insufficient balance: ${balance:.2f} (required ${amount:.2f})"
        # initalising the super class with a messagte
        super().__init__(message)

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount

    def get_balance(self):
        return self.balance

# Create a bank account with an initial balance of $100
account = BankAccount(100)

try:
    account.deposit(10)
    # should work
    account.withdraw(50)
    # Attempt to withdraw $100, which exceeds the balance
    account.withdraw(100)
except InsufficientFundsError as e:
    print("Transaction failed:", e)
else:
    print("Transaction successful")
finally:
    print(f"Current balance: ${account.get_balance():.2f}")
