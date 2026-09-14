from datetime import datetime

class Expense:
    """OOP model for representing a single expense record."""
    def __init__(self,amount: float,category:str,description:str,date:datetime.date=None):
        self.amount=float(amount)
        self.category=category.lower()
        self.description=description
        self.date=datetime.now().date() if date is None else date

    def to_dict(self) -> dict:
        """converts the expense object to a dictionary representation."""
        return {
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date.isoformat()
        }    
@classmethod
def from_dict(cls, data: dict):
    """creates an expense object from a dictionary representation."""
    amount = data.get("amount")
    category = data.get("category")
    description = data.get("description")
    date_str = data.get("date")
    date = datetime.date.fromisoformat(date_str) if date_str else None
    return cls(amount, category, description, date)