# FinalProject

CM3 - CS Final Project 

Mathias Osland & Juliana Moscoso

Project Idea: Personal Budget Tracker

• Users will be able to track their income and expenses, categorize transactions, and create reports (like total expenses by category). It will be a command-line application that reads and writes data to a CSV file.

• A command-line application is a program that the user can interact with by typing commands. It reads and writes data to a csv file. A csv is a file format that stores data. The program takes the information from the file, and it can also add/update data in it.

Features:

-	Add income and expenses with descriptions and categories
-	Show transactions
-	Create summary reports (total expenses and income by category)
-	Save transactions in a CSV file 
-	Basic error handling for user input
-	Three main functions with pytest test cases
  
Project Structure:

/budget_tracker/
-	project.py          # main Python script with functions
-	test_project.py     # pytest test cases for three functions
-	transactions.csv    # csv file to store transactions
-	requirements.txt    # dependencies (if needed)

  
Functions to Implement & Test:

•	add_transaction (amount, category, type)
Users can add transactions with an amount, category, and type (income or expense).
  
• The add_transaction function also adds the transaction to the csv file.
Example: add_transaction ($50, food, expense)

•	view_transactions ()
Reads and shows all transactions from transactions.csv.
  
•	generate_summary ()
This function generates a report showing income and expenses by category.
It calculates totals for each category and a summary for total income and expenses.

Basic Error Handling for User Input:

•The main () function has error handling for invalid amounts (non-numeric input).
•It ensures valid transaction types (income or expense).

Three Main Functions:

•	add_transaction: Adds a new transaction.
•	view_transactions: Displays all transactions.
•	generate_summary_by_category: Generates a summary report by category.

Python code:

The Python script for the budget tracker allows users to add transactions, view them, and generate a summary by category. It stores transactions in a csv file (transactions.csv). The add_transaction () function formats the amount to one decimal place and adds it to the file along with the category and transaction type. The view_transactions () function reads the file and returns a list of transactions. The generate_summary_by_category () function go through all the transactions, then categorizes them into income and expenses, sums them up, and stores them in a dictionary, including the total income and expenses. The main () function allow users to interact, where they can choose to add a transaction by entering an amount, category, and type (income or expense), view all transactions, or generate a summary. It also checks that the transaction type is correct, and the amount is a number. The program runs in a loop until the user selects option 4 to exit. 

Pytest Test Cases:

pytest test cases that correspond to the functionality of the project are included. 
The pytest script tests three functions for the budget tracking project: add_transaction (), view_transactions (), and generate_summary_by_category (). 

It imports pytest, csv, and the required functions from project.py. A function called clear_transactions_file (), is used to clear the transactions.csv before each test to ensure accuracy. The test_add_transaction () function clears the file, adds a transaction (100, "salary", "income"), and then it checks that the transaction was added and appears in the correct format in the list.

The test_view_transactions () function clears the file, adds two transactions (50, "food", "expense" and 20, "transport", "expense"), and it checks that both transactions were added and their details are displayed correctly.

The test_generate_summary () function clears the file, adds three transactions (100, "Salary", "income", 50, "Food", "expense", and 20, "Transport", "expense"), then creates a summary, and checks if income and expenses are categorized in the correct order, ensuring that the values are stored as floats and the total calculations are accurate (100.0 income, 70.0 expenses). To run the tests, we execute pytest test_project.py.
