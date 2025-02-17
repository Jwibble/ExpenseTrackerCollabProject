#Katrina Liu and Eric Yang's Expense Tracker Project
import datetime

expense_dict = {}

print('Welcome to your expense tracker.')

while True:

    menu = input("\nWould you like to: \n"
                    "1. Add New Expense \n"
                    "2. View all expenses \n"
                    "3. Categorize expenses \n"
                    "4. Calaculate total expenses \n"
                    "5. Delete expenses \n"
                    "6. Exit the app \n"
                    "Please select which option by the number: ").strip()

    if menu == '1':
        category =  input("Please enter the categogry for this expense: ").lower().strip().title()
        try:
            amount = float(input("Enter the amount for this expense: "))
            
        except ValueError:
            print("Invalid amount.")
            continue
            

        date = input("Please enter the date for when this expense is due in YYYY/MM/DD format: ").strip()

        if date: 
            try:
                date = datetime.datetime.strptime(date, "%Y/%m/%d").strftime("%Y-%m-%d")
            except ValueError:
                print("Invalid Date or format.")
                continue
                

        expenseid = len(expense_dict) + 1
        expense_dict[expenseid] = {"category": category, "amount": amount, "date": date}

        print("Your expense has been added successfully.")


    elif menu == '2':
        if not expense_dict:
            print("No expenses have been added as of now.")
            
        else:
            print("Your current expenses are:")
            for key, expense in expense_dict.items():
                print(f"{key}. ${expense['amount']} - {expense['category']} - {expense['date']}")
        
    elif menu == '3':
        if not expense_dict:
            print("No expenses have been added as of now.")
        else:
            categorized_expenses = {}
            
            for expense in expense_dict.values():
                category = expense["category"]
                if category not in categorized_expenses:
                    categorized_expenses[category] = []
                categorized_expenses[category].append(expense)

            print("\nYour expenses categorized by type:")
            for category, expenses in categorized_expenses.items():
                print(f"\nCategory: {category}")
                for expense in expenses:
                    print(f"  - ${expense['amount']} on {expense['date']}")

  
    elif menu == '4':
        category_totals = {}
        for expense in expense_dict.values():
            category = expense["category"]
            amount = expense["amount"]
            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount

        print("\nYour total expenses by category are:")
        for category, total in category_totals.items():
            print(f"{category}: ${total}")

        total_spending = sum(expense["amount"] for expense in expense_dict.values())
        print(f"\nYour grand total expenses are: ${total_spending}")


    elif menu == '5':
        if not expense_dict:
            print("No expesese have been added yet.")

        else:
            print("Which expense would you like to delete? Your current expenses:")

            for key, expense in expense_dict.items():
                print(f"{key}. ${expense['amount']} - {expense['category']} - {expense['date']}")

            try:
                expense_deletion = int(input("Please enter the number associated with the expense to delete it: "))
                if expense_deletion in expense_dict:
                    expense_dict.pop(expense_deletion)
                    print("Your expense has been deleted")
                
                else:
                    print("Invalid Number.")
            
            except ValueError:
                print("Invalid input. Please enter a number associated with the expense")

    elif menu == '6':
        print("See you next time.")
        break

    else:
        input("Please enter a number between 1 - 6: ").strip()
