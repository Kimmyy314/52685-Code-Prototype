# 52865 A2: Code prototype
## Financial expense tracker

### Project purpose:
The purpose of this project is to provide the user a basic command line interface (CLI) in order to track there expenses. Users can add, remove, edit and view transactions which are stored in a Comma Seperated Value (CSV) file.

### Features 
1. **Add Transaction**: Allows users to add a new transaction with details such as date, type (income or spending), category, and amount.
2. **Remove Transaction**: Users can remove a transaction by specifying its index within the dataframe which is shown on the far left.
3. **Edit Transaction**: Users can edit the details of an existing transaction.
4. **View Transactions**: Displays all the transactions stored in the CSV file so that users can track what they've been earning/ spending. 

Each feature is available via the menu and the user can click option 5 to exit.

### Code libraries and dependencies
* Pandas: Is being used to structure the financial data into dataframes for the user to see. The library also makes handling the numerical data easier to interact with then without and is a very common library in data projects.
* OS: This library is being used to check for the existance of the CSV file
---
### Installation and Setup

Pre-requisite install
- Python 3.x

Download the code or clone using below
```
git clone https://github.com/Kimmyy314/52685-Code-Prototype.git 
```

Install the pandas library 
```
pip install pandas
```
