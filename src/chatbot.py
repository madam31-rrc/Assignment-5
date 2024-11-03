"""
Description: Chatbot application.  Allows user to perform balance 
inquiries and make deposits to their accounts.
Author: ACE Department
Modified by: {Student Name}
Date: 2023-10-15
Usage: From the console: python src/chatbot.py
"""

## GIVEN CONSTANT COLLECTIONS
ACCOUNTS = {
    123456 : {"balance" : 1000.0},
    789012 : {"balance" : 2000.0}
}

VALID_TASKS = {"balance", "deposit", "exit"}

## CODE REQUIRED FUNCTIONS STARTING HERE:

## GIVEN CHATBOT FUNCTION
## REQUIRES REVISION
"""
def chatbot():
    '''
    The main program.  Uses the functionality of the functions:
        get_account()
        get_amount()
        get_balance()
        make_deposit()
        user_selection()
    '''

    print("Welcome! I'm the PiXELL River Financial Chatbot!  Let's get chatting!")

    keep_going = True
    while keep_going:
        try:
            ## CALL THE user_selection FUNCTION HERE 
            ## CAPTURING THE RESULTS IN A VARIABLE CALLED
            ## selection:

            if selection != "exit":
                
                # Account number validation.
                valid_account = False
                while valid_account == False:
                    try:
                        ## CALL THE get_account FUNCTION HERE
                        ## CAPTURING THE RESULTS IN A VARIABLE 
                        ## CALLED account:

                        valid_account = True
                    except ValueError as e:
                        # Invalid account.
                        print(e)
                if selection == "balance":
                        ## CALL THE get_balance FUNCTION HERE
                        ## PASSING THE account VARIABLE DEFINED 
                        ## ABOVE, AND PRINT THE RESULTS:

                else:

                    # Amount validation.
                    valid_amount = False
                    while valid_amount == False:
                        try:
                            ## CALL THE get_amount FUNCTION HERE
                            ## AND CAPTURE THE RESULTS IN A VARIABLE 
                            ## CALLED amount:


                            valid_amount = True
                        except ValueError as e:
                            # Invalid amount.
                            print(e)
                ## CALL THE make_deposit FUNCTION HERE PASSING THE 
                ## VARIABLES account AND amount DEFINED ABOVE AND 
                ## PRINT THE RESULTS:


            else:
                # User selected 'exit'
                keep_going = False
        except ValueError as e:
            # Invalid selection:
            print(e)

    print("Thank you for banking with PiXELL River Financial.")
"""
    
"""
if __name__ == "__main__":
    chatbot()
"""

def get_account() -> int:
    """
    Prompts the user for an account number and returns it if valid.

    Returns:
        int: The entered account number if valid.

    Raises:
        ValueError: If the account number is not a whole number or does not exist in ACCOUNTS.
    """
    try:
        # Prompt user for account number
        account_number = int(input("Please enter your account number: "))
        
        # Check if the account exists in ACCOUNTS
        if account_number not in ACCOUNTS:
            raise ValueError("Account number entered does not exist.")
        
        return account_number

    except ValueError as e:
        if "invalid literal" in str(e):
            raise ValueError("Account number must be a whole number.")
        else:
            raise e

def get_amount() -> float:
    """
    This prompts the user for a transaction amount and returns it if valid.

    Returns:
        float: The entered amount if valid.

    Raises:
        ValueError: If the amount is not numeric or is zero/negative.
    """
    try:
        # Prompt user for the transaction amount
        amount = float(input("Enter the transaction amount: "))
        
        # Check if the amount is greater than zero
        if amount <= 0:
            raise ValueError("Invalid amount. Please enter a positive number.")
        
        return amount

    except ValueError as e:
        # Check if the error is due to non-numeric input
        if "could not convert string to float" in str(e):
            raise ValueError("Invalid amount. Amount must be numeric.")
        else:
            raise e
