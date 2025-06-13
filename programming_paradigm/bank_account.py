# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0.0):
        """
        Initialize a new BankAccount.
        :param initial_balance: starting balance (defaults to 0.0)
        """
        # Encapsulated balance attribute
        self.__balance = float(initial_balance)

    def deposit(self, amount):
        """
        Deposit money into the account.
        :param amount: positive number to add
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount

    def withdraw(self, amount):
        """
        Withdraw money from the account if funds are sufficient.
        :param amount: positive number to withdraw
        :return: True if successful, False if insufficient funds
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            return False
        self.__balance -= amount
        return True

    def display_balance(self):
        """Print the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.__balance:.2f}")
