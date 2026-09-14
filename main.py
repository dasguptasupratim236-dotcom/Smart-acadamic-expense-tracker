import sys
from turtle import clear
from engine.tracker import TrackerEngine
from models.expense import Expense
from utils.validators import validate_positive_float, validate_non_empty_string

def print_menu():
    print("\n")
    print("Smart Academic Expense Tracker")
    print()
    print("1. Set monthly budget")
    print("2. Add expense")
    print("3. View all expenses")
    print("4. View analytics and summary")
    print("5. Exit")
    print()

def main():
    tracker = TrackerEngine()
    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ").strip()
        if choice == '1':
            budget_input = input("Enter your monthly budget: ")
            try:
                budget = validate_positive_float(budget_input)
                tracker.set_budget(budget)
                print(f"Monthly budget set to: {budget}")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == '2':
            name_input = input("Enter expense name: ")
            amount_input = input("Enter expense amount: ")
            try:
                name = validate_non_empty_string(name_input)
                amount = validate_positive_float(amount_input)
                expense = Expense(amount=amount, category=name, description="")
                tracker.add_expense(expense)
                print(f"Expense '{name}' of amount {amount} added.")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == '3':
            expenses = tracker.get_expenses()
            if not expenses:
                print("No expenses recorded.")
            else:
                print("Expenses:")
                for expense in expenses:
                    print(f"- {expense['category']}: {expense['amount']}")
        elif choice == '4':
            summary = tracker.get_budget_status()
            print("Analytics and Summary:")
            print(f"Total Expenses: {summary['total_expenses']}")
            print(f"Remaining Budget: {summary['remaining_budget']}")

            if summary['remaining_budget'] < 0:
                print("Warning: You have exceeded your budget!")
        elif choice == '5':
            print("Exiting the application.Thank you")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
if __name__ == "__main__":
    main()