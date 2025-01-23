#main app

#expense class is avail now in this file
from expense import Expense
import calendar
import datetime


def main():
    print(f"🎯Running Expense Tracker!")
    expense_file_path = "expenses.csv"
    budget = 1000

#when main runs: it will run "sub-functions" one by one
    #Get user input for expense.
    expense = get_user_expense()

    #Write their expense to a file
    save_expense_to_file(expense, expense_file_path)

    #Read file nd summarise expenses
    summarize_expenses(expense_file_path, budget)
    

def get_user_expense():
    print(f"🎯Getting User Expense")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: ")) #float function for numerical

    #Define LIST of Categories to choose from
    expense_categories = [
        "🍔Food",
        "🏠Home",
        "💼Work",
        "🎉Fun",
        "🔴Misc"
    ] #square brackets for list

#While loop to select expense category
    while True: 
        print("Select a Category: ")
        for i, category_name in enumerate(expense_categories): #enumerate with list: tuple response (i)index & (category_name) value of item
            print(f"  {i + 1}. {category_name}") #format string for 2pieces of info #curly brack to substitute values

        value_range = f"[1 - {len(expense_categories)}]" #len calculates number of categories 
        selected_index = int(input(f"Enter a category number {value_range}: ")) -1 #subtract cause +1 index

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense =  Expense(
                name=expense_name, category=selected_category, amount=expense_amount
            )
            return new_expense
        else:
            print("Invalid Category. Please try again!")

   
def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"🎯Saving User Expense: {expense} to {expense_file_path}")
    now = datetime.datetime.now()
    formatted_date = now.strftime("%Y-%m-%d")  # Format the date as YYYY-MM-DD

    with open(expense_file_path, "a") as f:
        f.write(f"{formatted_date},{expense.name},{expense.amount},{expense.category}\n")

def summarize_expenses(expense_file_path, budget):
    print(f"🎯Summarizing User Expense!")
    expenses: list[Expense] = []  # expenses list to store results below
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            # Use split(",") to separate values into a list
            expense_data = line.strip().split(",")
            
            # Check if there are enough values
            if len(expense_data) >= 4:  # Assumingx date, name, amount, category
                formatted_date = expense_data[0]
                expense_name = expense_data[1]
                expense_amount = float(expense_data[2])
                expense_category = expense_data[3]

                line_expense = Expense(
                    name=expense_name,
                    amount=expense_amount,
                    category=expense_category
                )
                expenses.append(line_expense)
            else:
                print(f"Skipping invalid line: {line}")
    
    
    amount_by_category = {}
    for expense in expenses: #loop through each expense
        key = expense.category
        if key in amount_by_category: #code for if key is present
            amount_by_category[key] += expense.amount
        else: #code for if key not present
            amount_by_category[key] = expense.amount #create new entry: no +
    
    print("Expenses By Category 📊:") #loop through keys for nicer format
    for key, amount in amount_by_category.items():
        print(f"  {key}: ${amount:.2f}")

    #calc total spent
    total_spent = sum([x.amount for x in expenses]) #for every x in expenses: create new list where each item = x amount
    print(f"\033[93m💸Total Spent: ${total_spent:.2f}\033[0m")

    #calc remaining budget
    remaining_budget = budget - total_spent #budget variable 

    #print budget status
    if remaining_budget >= 0:
        print(f"\033[91m✅Budget Remaining: ${remaining_budget:.2f}\033[0m")
    else:
        print(f"\033[91m❌Budget Exceeded! You are ${abs(remaining_budget):.2f} over budget.\033[0m") #abs to ensure positive value is shown


    # Get current date
    now = datetime.datetime.now ()

    # Get the number of days in the current month
    days_in_month = calendar.monthrange(now.year, now.month)[1]

    # Calculate remaining number of days in the current month
    remaining_days = days_in_month - now.day

    # Check if remaining_days is zero to avoid division by zero
    if remaining_days > 0:
        daily_budget = remaining_budget / remaining_days
        print(f"\033[92m🔑Avg Budget Daily till month end: ${daily_budget:.2f}\033[0m")
    else:
        print("\033[92m🔑No Avg Daily Budget (last day of month)\033[0m")

#Ensure this runs ONLY when it run this file, not when running as part of another file
if __name__ == "__main__": #__name__ is special variable, will be equal to __name__ when ran as a file
    main()