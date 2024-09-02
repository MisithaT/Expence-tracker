import csv
import os

# File to store expenses
CSV_FILE = 'expenses.csv'

def initialize_csv():
    """Create the CSV file with headers if it doesn't exist."""
    if not os.path.isfile(CSV_FILE):
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['UserID', 'Name', 'Date', 'Category', 'Amount'])

def add_person(user_id, name):
    """Add a new person to the CSV file."""
    if not os.path.isfile(CSV_FILE):
        print("CSV file not found. Initialize the file first.")
        return

    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([user_id, name, '', '', ''])  # Add person with no expense details

def add_expense(user_id, date, category, amount):
    """Add a new expense record for a user."""
    if not os.path.isfile(CSV_FILE):
        print("CSV file not found. Initialize the file first.")
        return

    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([user_id, '', date, category, amount])


def view_expenses(user_id):
    """Display all expenses for a user."""
    if not os.path.isfile(CSV_FILE):
        print("No expenses recorded yet.")
        return

    with open(CSV_FILE, mode='r') as file:
        reader = csv.reader(file)
        headers = next(reader, None)  # Read the header

        if headers is None:
            print("No expenses recorded yet.")
            return

        print("\nDate       | Category   | Amount")
        print("---------------------------------")
        found = False
        for row in reader:
            if row[0] == user_id and row[2]:  # Ensure there's an expense to show
                print(f"{row[2]} | {row[3]:<10} | ${row[4]}")
                found = True
        if not found:
            print("No expenses found for this user.")


def delete_expense(user_id, date):
    """Delete an expense record by user ID and date."""
    if not os.path.isfile(CSV_FILE):
        print("No expenses to delete.")
        return

    lines = []
    with open(CSV_FILE, mode='r') as file:
        reader = csv.reader(file)
        lines = list(reader)

    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        if lines:
            writer.writerow(lines[0])  # Write the header back
            deleted = False
            for line in lines[1:]:
                if line[0] == user_id and line[2] == date:
                    deleted = True
                    print(f"Deleted expense on {date} for user {user_id}")
                else:
                    writer.writerow(line)

            if not deleted:
                print(f"No expense found for date {date} and user {user_id}")

def main():
    initialize_csv()
    while True:
        print("\nExpense Tracker")
        print("1. Add Person")
        print("2. Add Expense")
        print("3. View Expenses")
        print("4. Delete Expense")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            user_id = input("Enter UserID: ")
            name = input("Enter Name: ")
            add_person(user_id, name)

        elif choice == '2':
            user_id = input("Enter UserID to add expense: ")
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = input("Enter amount: ")
            add_expense(user_id, date, category, amount)

        elif choice == '3':
            user_id = input("Enter UserID to view expenses: ")
            view_expenses(user_id)

        elif choice == '4':
            user_id = input("Enter UserID of expense to delete: ")
            date = input("Enter date of expense to delete (YYYY-MM-DD): ")
            delete_expense(user_id, date)

        elif choice == '5':
            print("Program ended successfully")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
