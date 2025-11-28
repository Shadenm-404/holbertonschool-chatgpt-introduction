#!/usr/bin/python3

class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        """Deposit money into the account."""
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """Withdraw money from the account if sufficient balance exists."""
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """Display the current account balance."""
        print("Current Balance: ${:.2f}".format(self.balance))


def safe_float_input(prompt):
    """
    Safely request a float from the user.
    Prevents crashing if input is not a number.
    """
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")

        if action.lower() == 'exit':
            break

        elif action.lower() == 'deposit':
            amount = safe_float_input("Enter the amount to deposit: $")
            cb.deposit(amount)

        elif action.lower() == 'withdraw':
            amount = safe_float_input("Enter the amount to withdraw: $")
            cb.withdraw(amount)

        elif action.lower() == 'balance':
            cb.get_balance()

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
