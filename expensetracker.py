import csv
import os
from datetime import datetime

FILE = 'expenses.csv'

# Function checks to see if csv file exists, if not, then it will create it
def initialize_csv():
    # Check if the file exists
    if not os.path.exists(FILE):
        # If the file doesn't exist, create it and add the header row
        with open(FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Description', 'Amount', 'Category', 'Date'])

# Function to add an expense to the csv file
def add_expense(description, amount, category, date):
    with open(FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([description, amount, category, date])

# Function to view all expenses
def view_expenses():
    with open(FILE, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)  

# Main function to run the expense tracker application 
def main():
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            date = datetime.now().strftime("%d-%m-%Y")
            add_expense(description, amount, category, date)
        if choice == '2':
            view_expenses()
        if choice =='3':
            break

 main()