import pytest
import csv
from project import add_transaction, view_transactions, generate_summary_by_category

# Function to clears the transactions.csv file to remove old data and ensure the tests are accurate
def clear_transactions_file():
    with open('transactions.csv', mode='w', newline='') as file: # Mode 'w' clears the file
        writer = csv.writer(file)
        
# add_transaction test function
def test_add_transaction():
    # Clear the file before the test
    clear_transactions_file()

    # add a transaction
    add_transaction(100, "Salary", "income")
    
    # Check if the transaction was added correctly
    transactions = view_transactions()
    assert len(transactions) > 0  #Check to see if at least one transaction was added to the transaction list
    assert transactions[-1] == ['100.0', 'Salary', 'income'] #assert checks if a condition is true. If the condition is false, then the test fails


# Test view_transactions function
def test_view_transactions():
    # Clear the file before the test
    clear_transactions_file()

    # Add transactions
    add_transaction(50, "Food", "expense")
    add_transaction(20, "Transport", "expense")
    
    # Get all transactions and verify
    transactions = view_transactions()
    assert len(transactions) == 2  # there must be exactly 2 transactions
    assert transactions[0] == ['50.0', 'Food', 'expense']
    assert transactions[1] == ['20.0', 'Transport', 'expense']

# Test generate_summary function
def test_generate_summary():
    # Clear the file before the test
    clear_transactions_file()

    # Add sample transactions
    add_transaction(100, "Salary", "income")
    add_transaction(50, "Food", "expense")
    add_transaction(20, "Transport", "expense")
    
    # Generate summary
    summary = generate_summary_by_category()

    # Check if the summary is correct and formatted
    assert summary['Salary']['income'] == 100.0
    assert summary['Food']['expenses'] == 50.0
    assert summary['Transport']['expenses'] == 20.0

    # Check if the summary values are in the correct format/type with assert isinstance. (integer,float,str)
    assert isinstance(summary['Salary']['income'], float) 
    assert isinstance(summary['Food']['expenses'], float)
    assert isinstance(summary['Transport']['expenses'], float)
    assert summary['Total']['income'] == 100.0
    assert summary['Total']['expenses'] == 70.0

