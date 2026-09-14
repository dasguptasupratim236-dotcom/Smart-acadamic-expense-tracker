import json
from math import exp
import os
import models.expense as Expense

class TrackerEngine:
    """handes the core logic of the expense tracker application."""
    def __init__(self,data_file="data/expenses.json"):
        self.data_file = data_file
        self.expenses = []
        self.budget = 0.0
        self.load_data()

    def set_budget(self, budget: float):
        """sets the monthly budget."""
        self.budget = budget
        self.save_data()

    def add_expense(self, expense: Expense):
        """adds a new expense to the tracker."""
        self.expenses.append(expense)
        self.save_data()

    def get_expenses(self) -> dict:
        """retrieves all recorded expenses."""
        return [expense.to_dict() for expense in self.expenses]

    def get_category_breakdown(self) -> dict:
        """provides a breakdown of expenses by category."""
        breakdown = {}
        for expense in self.expenses:
            category = expense.category
            breakdown[category] = breakdown.get(category, 0) + expense.amount
        return breakdown

    def get_budget_status(self) -> dict:
        """provides the current budget status."""
        total_expenses = sum(expense.amount for expense in self.expenses)
        remaining_budget = self.budget - total_expenses
        return {
            "total_expenses": total_expenses,
            "remaining_budget": remaining_budget,
            "percentage_used": (total_expenses / self.budget * 100) if self.budget > 0 else 0
        }

    def save_data(self):
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        for expense in self.expenses:
            if hasattr(expense, "to_dict"):
                serialized_expense = expense.to_dict()
            elif isinstance(expense, dict):
                serialized_expense = expense
            else:
                raise ValueError("All items in expenses must be instances of the Expense class.")
        data={
            "monthly_budget": self.budget,
            "expenses":[serialized_expense for expense in self.expenses]
        }
        with open(self.data_file, "w") as f:
            json.dump(data, f, indent=4)    

    def load_data(self):
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, "r") as f:
                    data = json.load(f)
                self.budget = data.get("monthly_budget", 0.0)
                self.expenses = []
                for exp in data.get("expenses", []):
                    exp_obj = Expense(amount=exp["amount"], category=exp["category"], description=exp["description"], date=exp.get("date"))
                    self.expenses.append(exp_obj)
        except (json.JSONDecodeError, Exception) as e:
            self.budget = 0.0
            self.expenses = []        
                