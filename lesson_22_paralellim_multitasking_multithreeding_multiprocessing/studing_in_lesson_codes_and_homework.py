# def bar():
#     print("i", id(x))
#     return x + 1
#
#
# x = 5
# print("t", id(x))
# print(bar())


# def count_substring(string, sub_string):
#     return string.count(sub_string)
#
#
# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
#
#     count = count_substring(string, sub_string)
#     print(count)

# print("ABCDCDC".count("CDC"))

import time


# def fib(n: int):
#     fib_numbers = [0, 1]
#     for i in range(n - 2):
#         fib_numbers.append(fib_numbers[i] + fib_numbers[i + 1])
#     return fib_numbers

# # result = fib(17)
# # for i in result:
# #     print(i, end=" ")



# Define a class BankAccount
class BankAccount:
    # Initialize the balance attribute
    def __init__(self, balance=0):
        self.balance = balance

    # Define a method to deposit money
    def deposit(self, amount):
        # Check if the amount is positive
        if amount > 0:
            # Add the amount to the balance
            self.balance += amount
            # Print a confirmation message
            print(f"You deposited ${amount}. Your new balance is ${self.balance}.")
        else:
            # Print an error message
            print("Invalid amount. Please enter a positive number.")

    # Define a method to withdraw money
    def withdraw(self, amount):
        # Check if the amount is positive
        if amount > 0:
            # Check if the amount is less than or equal to the balance
            if amount <= self.balance:
                # Subtract the amount from the balance
                self.balance -= amount
                # Print a confirmation message
                print(f"You withdrew ${amount}. Your new balance is ${self.balance}.")
            else:
                # Print an error message
                print("Insufficient funds. You cannot withdraw more than your balance.")
        else:
            # Print an error message
            print("Invalid amount. Please enter a positive number.")

    # Define a method to check the balance
    def check_balance(self):
        # Print the current balance
        print(f"Your current balance is ${self.balance}.")
