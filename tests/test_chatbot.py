"""
Description: Project of a simple financial chatbot developed for PiXELL River Financial
Author: Muniru Adam
Date: 2024-11-3
Usage:
"""
from unittest import TestCase
from unittest.mock import patch
from src.chatbot import get_account, ACCOUNTS

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


