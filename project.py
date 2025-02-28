import csv

# file name for storing transactions
transactions_file = 'transactions.csv'

# Function to add a transaction
def add_transaction(amount, category, trans_type):
    # Format the amount to one decimal place
    amount = f"{amount:.1f}"
    
    # Open the CSV file in append mode to add a new transaction. 
    # Add new data at the end of the file without deleting existing data.
    with open(transactions_file, mode='a', newline='') as file: # csv writer object to write rows into the csv file
        writer = csv.writer(file)
        writer.writerow([amount, category, trans_type]) # Write the new transaction data (amount, category, transaction type) as a new row in the file
        print(f"Transaction added: ${amount} {category} - {trans_type}")

# Function to view all transactions
def view_transactions():
    # Read the CSV file and return the list with transactions
    transactions = []
    with open(transactions_file, mode='r') as file: # Mode r is for reading only
        reader = csv.reader(file)
        for row in reader:
            if row:  
                transactions.append(row) # Go through each row in the csv file, and if the row is not empty, we add it to the transactions list.
    return transactions # Then, return the list of transactions.

# Function to generate the summary by category
def generate_summary_by_category():
    # Read all transactions by calling view_transactions (the transaction list from above)
    transactions = view_transactions()
    summary = {} # Empty dictionary to store the summary 
    total_income = 0  # Total income initiate in 0
    total_expenses = 0  # Total expenses initiate in 0

    for row in transactions: # Loop through each transaction in the list
        if row:  # Skip empty rows
            amount = float(row[0]) # Convert the amount from string to a number (float)
            category = row[1] # Get the category of the transaction 
            trans_type = row[2] # Get the type of the transaction
    
            if category not in summary: # If the category is not already in the summary dictionary, this will add it with an initial income and expenses set to 0.
                summary[category] = {'income': 0, 'expenses': 0}
    
            if trans_type == 'income':
                summary[category]['income'] += amount
                total_income += amount  # add to total income
            elif trans_type == 'expense':
                summary[category]['expenses'] += amount
                total_expenses += amount  # add to total expenses
    
    # Add total income and expenses to the summary
    summary['Total'] = {'income': total_income, 'expenses': total_expenses}
    
    return summary


# Function to interact with the user
def main():
    print("Welcome to your Budget Tracker!\n")
    
    while True: # Keep the program running until the user wants to exit
        print("\nWhat would you like to do?")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Generate Summary by Category")
        print("4. Exit")
        
        choice = input("Enter the number of your choice: ")
        
        if choice == "1":
            try:
                amount = float(input("Enter the amount: ")) # Get the amount as a number
                category = input("Enter the category (e.g., Food, Salary, etc.): ")
                trans_type = input("Enter the transaction type (income/expense): ")
                if trans_type not in ['income', 'expense']: # If the input is not valid
                    print("Invalid transaction type. Please enter 'income' or 'expense'.") # Show error message
                else:
                    add_transaction(amount, category, trans_type)
            except ValueError: # If the amount entered is not a valid number
                print("Invalid amount entered. Please enter a numeric value for the amount.")
            
        elif choice == "2":
            transactions = view_transactions() # Get the list of transactions
            print("\nTransactions:") # Show the header/label
            if transactions: # If there are transactions 
                for transaction in transactions: # Show each transaction
                    print(transaction)
            else: # If there are no transactions
                print("No transactions found.")
                
        elif choice == "3":
            summary = generate_summary_by_category() # Generate the summary
            print("\nSummary by Category:") # Show the header
            if summary: # If there is a summary to show
                for category, data in summary.items(): # For each category in the summary
                    print(f"{category}:") # Show the category name
                    print(f"  Income: ${data['income']}") # Show the total income for the category, and format it to show the value from the dictionary data with a dollar sign in front of it.
                    print(f"  Expenses: ${data['expenses']}") # Show the total expense for the category 

            else:
                print("No summary available. Please add transactions first.")
                
        elif choice == "4":
            print("Exiting Budget Tracker.") # Exit message
            break # Exit the program
        
        else: # If the user enters an invalid option
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
