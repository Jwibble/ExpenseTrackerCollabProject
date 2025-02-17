#Katrina Liu and Eric Yang's Expense Tracker Project
import datetime

expense_dict = {}

print('Welcome to your expense tracker.')

while True:

    menu = input("Would you like to: \n"
                    "1. Add New Expense \n"
                    "2. View all expenses \n"
                    "3. Categorize expenses \n"
                    "4. Calaculate total expenses \n"
                    "5. Delete expenses \n"
                    "6. Exit the app \n"
                    "Please select which option by the number: ").strip()

    if menu == '1':
        category =  input("Please enter the categogry for this expense: ").lower().strip()
        try:
            amount = float(input("Enter the amount for this expense: ")).strip()
            
        except ValueError:
            print("Invalid amount.")
            

        date = input("Please enter the date for when this expense is due in YYYY/MM/DD format: ").strip()

        if date: 
            try:
                date = datetime.datetime.strptime(date, "%Y/%m/%d").strftime("%Y-%m-%d")
            except ValueError:
                print("Invalid Date.")
                

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
        print('tbd')

  
    elif menu == '4':
        print("Which expense would you like to delete? Your current expenses:")

  


    elif menu == '5':
        print('tbd')


    elif menu == '6':
        print("See you next time.")
        exit()
