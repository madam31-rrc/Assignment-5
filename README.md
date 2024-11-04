# PiXELL River Financial Chatbot Project

## Description

Module 5, this project is a simple financial chatbot developed for PiXELL River Financial, allowing users
to check their account balance and make deposits via an interactive console-based application.

## Author

Muniru Adam

## Assignment

Assignment 5 Chatbot Implementation for PiXELL River Financial, functions to handle user inputs, validate accounts
and amounts, and manage deposits, testing for error handling and providing a user-friendly experience.

## Reflection

### 1. Identify any challenges or issues you encountered while writing your functions.

Understanding the separation of tasks for each function took some time, as I needed to ensure each function had a single responsibility.
Managing input validation and exceptions within each function was challenging, especially when considering user errors.
Integrating the functions in the main <chatbot()>.

### 2. Discuss the benefits and challenges of developing and using unit tests.

Benefits
Unit tests helped catch errors early, allowing me to fix issues in isolated functions before integrating them.
They provided confidence that each function worked as expected, making debugging easier during integration.
Unit tests acted as documentation for expected input and output.

Challenges
Writing tests for exceptions and validating error messages required careful attention to detail.
Ensuring coverage for edge cases was time-consuming but necessary to handle unexpected user inputs.
Setting up mock inputs for functions that rely on user input required learning how to use <unittest> and <patch>.