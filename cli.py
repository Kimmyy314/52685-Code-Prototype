import pandas as pd  # Allows users to work with data in structured formats like dataframes and series such as grouping and visualizing data
import os


def save_data(data):
    data.to_csv("finance_data.csv")  # data will be saved in a table format


def add_transaction(data):  # add a transaction to the data
    float_read = False  # keep track of whether something has happened yet
    date = input(
        "Enter date (DD-MM-YYYY): "
    )  # asking the user to input a date for the transaction

    print("\nSelect Transaction Type:")
    print("1: Income")
    print("2: Spending")

    transaction_type_choice = input("Enter 1 or 2 for Income or Spending:")
    if transaction_type_choice == "1":
        transaction_type = "Income"
    elif transaction_type_choice == "2":
        transaction_type = "Spending"
    else:
        print("Invalid option. Defaulting to Spending.")
        transaction_type = "Spending"

    print(f"Transaction type: {transaction_type}")
    category = input(
        "Enter category: "
    )  # asks the user to type in a category for an item

    while (
        not float_read
    ):  # sets up loop that will keep running until float_read changes to True
        try:
            amount = float(input("Enter amount: $"))  # read the amount
            float_read = (
                True  # float (decimal number) has been read, so setting to true
            )
        except ValueError:  # if an error occurs move to below
            print(
                "Issue reading the digit"
            )  # print the issue reading the digit and loop repeats

    new_transaction = (
        pd.DataFrame(  # creates a new data frame with the following columns
            {
                "Date": [date],
                "Type": [transaction_type],
                "Category": [category],
                "Amount": [amount],
            }
        )
    )

    data = pd.concat(
        [data, new_transaction]
    )  # it combines two data which are the existing data set in "data" and the new data in "new transaction"
    save_data(data)  # it saves the data
    print("Transaction added successfully.")  # Transaction has been added successfully


def remove_transaction(data):  # it removes the transaction from the data
    print(data)
    index = int(
        input("Enter the index of the transaction to remove: ")
    )  # asking the user to type in a number to coose which transaction they wanted to delete
    data = data.drop(index)  # removes a specific transaction from the data collection
    save_data(data)  # Saves the data
    print("Transaction removed successfully.")


def edit_transaction(data):  # edits the transaction data
    print(data)
    index = int(
        input("Enter the index of the transaction to edit: ")
    )  # allows the user to type a number to specify which transaction
    column = input(
        "Enter the column to edit (Date/Type/Category/Amount): "
    )  # asking the user to specify which part of the trasaction they want to change
    new_value = input("Enter the new value: ")  # asking the user to type in a new value

    if column == "Amount":  # checks if the user chose amount to edit
        new_value = float(
            new_value
        )  # changes the type of new value from a string text to a number that can have decimals
        data.at[index, column] = new_value  # changes a specific value in the data table
        save_data(data)  # saves the data
        print("Transaction edited successfully.")


def view_transactions(data):
    print(data)


# check whether the finance_data.csv file exists
if os.path.exists("finance_data.csv"):
    # load the data from the file
    data = pd.read_csv("finance_data.csv")
else:
    # create an empty DataFrame
    data = pd.DataFrame(columns=["Date", "Type", "Category", "Amount"])

# main loop
while True:
    print("\nMenu:")
    print("1. Add Transaction")
    print("2. Remove Transaction")
    print("3. Edit Transaction")
    print("4. View Transactions")
    print("5. Exit")

    # ask the user to choose an option
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_transaction(data)
    elif choice == "2":
        remove_transaction(data)
    elif choice == "3":
        edit_transaction(data)
    elif choice == "4":
        view_transactions(data)
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please choose a number from the menu:")
