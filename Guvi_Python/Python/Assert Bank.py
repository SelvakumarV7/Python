# You are required to create a Python class to represent a bank account, and use the assert statement to ensure that the initial balance is non-negative.

class BankAccount:
    def __init__(self,initial_balance = 0):
        assert initial_balance >= 0
        self.balance = initial_balance
def check_balance(balance):
    try:
        BankAccount(balance)
        return "Assertion Passed"
    except AssertionError:
        return "Assertion Error"
initial_balance = int(input("Enter amount: "))
result = check_balance(initial_balance)
print(result)