"""
Description: Chatbot application.  Allows user to perform balance 
inquiries and make deposits to their accounts.
Author: ACE Department
Modified by: Muniru Adam
Date: 2023-11-03
Usage: From the console: python src/chatbot.py
"""

# Mock Account data
ACCOUNTS = {
    123456: {"balance": 1000.0},
    789012: {"balance": 2000.0}
}
VALID_TASKS = {"balance", "deposit", "exit"}

# Funtions and test running.
def get_account() -> int:
    try:
        account_number = int(input("Please enter your account number: "))
        if account_number not in ACCOUNTS:
            raise ValueError("Account number entered does not exist.")
        return account_number
    except ValueError as e:
        if "invalid literal" in str(e):
            raise ValueError("Account number must be a whole number.")
        else:
            raise e

def get_amount() -> float:
    try:
        amount = float(input("Enter the transaction amount: "))
        if amount <= 0:
            raise ValueError("Invalid amount. Please enter a positive number.")
        return amount
    except ValueError as e:
        if "could not convert string to float" in str(e):
            raise ValueError("Invalid amount. Amount must be numeric.")
        else:
            raise e

def get_balance(account: int) -> str:
    if account not in ACCOUNTS:
        raise ValueError("Account number does not exist.")
    balance = ACCOUNTS[account]["balance"]
    return f"Your current balance for account {account} is ${balance:,.2f}."

def make_deposit(account: int, amount: float) -> str:
    if account not in ACCOUNTS:
        raise ValueError("Account number does not exist.")
    if amount <= 0:
        raise ValueError("Invalid amount. Please enter a positive number.")
    ACCOUNTS[account]["balance"] += amount
    return f"You have made a deposit of ${amount:,.2f} to account {account}."

def user_selection() -> str:
    selection = input("What would you like to do (balance/deposit/exit)? ").strip().lower()
    if selection not in VALID_TASKS:
        raise ValueError("Invalid task. Please choose balance, deposit, or exit.")
    return selection

# Chatbot function
def chatbot():
    print("Welcome! I'm the PiXELL River Financial Chatbot! Let's get chatting!")
    keep_going = True
    while keep_going:
        try:
            selection = user_selection()
            if selection != "exit":
                valid_account = False
                while not valid_account:
                    try:
                        account = get_account()
                        valid_account = True
                    except ValueError as e:
                        print(e)
                if selection == "balance":
                    balance_info = get_balance(account)
                    print(balance_info)
                else:
                    valid_amount = False
                    while not valid_amount:
                        try:
                            amount = get_amount()
                            valid_amount = True
                        except ValueError as e:
                            print(e)
                    deposit_info = make_deposit(account, amount)
                    print(deposit_info)
            else:
                keep_going = False
        except ValueError as e:
            print(e)
    print("Thank you for banking with PiXELL River Financial.")

# Main Guard
if __name__ == "__main__":
    chatbot()
