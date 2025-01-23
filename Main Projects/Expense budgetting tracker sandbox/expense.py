class Expense:
    def __init__(self, name, category, amount) -> None: #constructor method, pass categories through self
        self.name = name
        self.category = category
        self.amount = amount

#represent function to display expense's name, category, and amount (replace memory address)
    def __repr__(self):
        return f"<Expense: {self.name}, {self.category}, ${self.amount:.2f} >"
    
    
       