# FinalProject

CM3 - CS Final Project 

Vide Demo: <https://www.youtube.com/watch?v=MZ__wxSbv_E>

Feb 28 2025

Mathias Osland & Juliana Moscoso

Project Idea: Personal Budget Tracker

- Users will be able to track their income and expenses, categorize transactions, and create reports (like total expenses by category). It will be a command-line application that reads and writes data to a CSV file.

- A command-line application is a program that the user can interact with by typing commands. It reads and writes data to a csv file. A csv is a file format that stores data. The program takes the information from the file, and it can also add/update data in it.

Features:
- Add income and expenses with descriptions and categories
- Show transactions
- Create summary reports (total expenses and income by category)
- Save transactions in a CSV file 
- Basic error handling for user input
- Three main functions with pytest test cases

Project Structure:
/budget_tracker/
 - project.py          # main Python script with functions
 - test_project.py     # pytest test cases for three functions
 - transactions.csv    # csv file to store transactions
 - requirements.txt    # dependencies 

Functions 

• add_transaction (amount, category, type)
  - Users can add transactions with an amount, category, and type (income or expense).
 -  The add_transaction function also adds the transaction to the csv file.
  - Example: add_transaction ($50, food, expense)

• view_transactions ()
  - Reads and shows all transactions from transactions.csv.

• generate_summary ()
  - This function generates a report showing income and expenses by category.
  - It calculates totals for each category and a summary for total income and expenses.

Basic Error Handling for User Input:
- The main () function has error handling for invalid amounts (non-numeric input).
- It ensures valid transaction types (income or expense).

Three Main Functions:
  1. add_transaction: Adds a new transaction.
  2. view_transactions: Displays all transactions.
  3. generate_summary_by_category: Generates a summary report by category.

Pytest Test Cases 
- pytest test cases that correspond to the functionality of the project are included. 
