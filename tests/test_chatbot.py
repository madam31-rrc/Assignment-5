"""
Description: Project of a simple financial chatbot developed for PiXELL River Financial
Author: Muniru Adam
Date: 2024-11-3
Usage:
"""
from unittest import TestCase
from unittest.mock import patch
from src.chatbot import get_account, ACCOUNTS
from src.chatbot import get_account, get_amount
from src.chatbot import get_account, get_amount, get_balance
from src.chatbot import get_account, get_amount, get_balance, make_deposit


class TestChatbot(TestCase):

    def test_get_account_valid(self):
        # Arrange
        valid_account = "123456"
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = [valid_account]

            # Act
            result = get_account()

            # Assert
            self.assertEqual(result, int(valid_account))

    def test_get_account_with_non_numeric(self):
        # Arrange
        non_numeric_input = "non_numeric_data"
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = [non_numeric_input]

            # Act and Assert
            with self.assertRaises(ValueError) as context:
                get_account()
            self.assertEqual(str(context.exception), "Account number must be a whole number.")

    def test_get_account_with_non_existent(self):
        # Arrange
        non_existent_account = "112233"
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = [non_existent_account]

            # Act and Assert
            with self.assertRaises(ValueError) as context:
                get_account()
            self.assertEqual(str(context.exception), "Account number entered does not exist.")

    def test_get_amount_valid(self):
        # Arrange
        valid_amount = "500.01"
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = [valid_amount]

            # Act
            result = get_amount()

            # Assert
            self.assertEqual(result, float(valid_amount))

    def test_get_amount_non_numeric(self):
        # Arrange
        non_numeric_input = "non_numeric_data"
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = [non_numeric_input]

            # Act and Assert
            with self.assertRaises(ValueError) as context:
                get_amount()
            self.assertEqual(str(context.exception), "Invalid amount. Amount must be numeric.")

    def test_get_amount_zero_or_negative(self):
        # Arrange
        invalid_amounts = ["0", "-100"]
        for invalid_amount in invalid_amounts:
            with patch("builtins.input") as mock_input:
                mock_input.side_effect = [invalid_amount]

                # Act and Assert
                with self.assertRaises(ValueError) as context:
                    get_amount()
                self.assertEqual(str(context.exception), "Invalid amount. Please enter a positive number.")

    def test_get_balance_valid_account(self):
        # Arrange
        account_number = 123456
        expected_message = "Your current balance for account 123456 is $1,000.00."

        # Act
        result = get_balance(account_number)

        # Assert
        self.assertEqual(result, expected_message)

    def test_get_balance_non_existent_account(self):
        # Arrange
        non_existent_account = 112233

        # Act
        with self.assertRaises(ValueError) as context:
            get_balance(non_existent_account)
        
        # Assert
        self.assertEqual(str(context.exception), "Account number does not exist.")

    def test_make_deposit_balance_updated(self):
        # Arrange
        account_number = 123456
        initial_balance = 1000.0
        deposit_amount = 1500.01
        ACCOUNTS[account_number] = {"balance": initial_balance}
        
        # Act
        make_deposit(account_number, deposit_amount)
        
        # Assert
        self.assertEqual(ACCOUNTS[account_number]["balance"], initial_balance + deposit_amount)

    def test_make_deposit_confirmation_message(self):
        # Arrange
        account_number = 123456
        initial_balance = 1000.0
        deposit_amount = 1500.01
        expected_message = "You have made a deposit of $1,500.01 to account 123456."
        ACCOUNTS[account_number] = {"balance": initial_balance}
        
        # Act
        result = make_deposit(account_number, deposit_amount)
        
        # Assert
        self.assertEqual(result, expected_message)

    def test_make_deposit_non_existent_account(self):
        # Arrange
        non_existent_account = 112233
        deposit_amount = 1500.01
        
        # Act
        with self.assertRaises(ValueError) as context:
            make_deposit(non_existent_account, deposit_amount)
        
        # Assert
        self.assertEqual(str(context.exception), "Account number does not exist.")

    def test_make_deposit_invalid_amount(self):
        # Arrange
        account_number = 123456
        ACCOUNTS[account_number] = {"balance": 1000.0}
        invalid_amount = -50.01
        
        # Act
        with self.assertRaises(ValueError) as context:
            make_deposit(account_number, invalid_amount)
        
        # Assert
        self.assertEqual(str(context.exception), "Invalid amount. Please enter a positive number.")
