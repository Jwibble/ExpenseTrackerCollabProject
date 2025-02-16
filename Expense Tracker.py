#Katrina Liu and Eric Yang's Expense Tracker Project
import datetime

list_expense = []

menu = input("Welcome to your expense tracker. Would you like to: \n"
                "1. Add New Expense \n"
                "2. View all expenses \n"
                "3. Categorize expenses \n"
                "4. Calaculate total expenses \n"
                "5. Delete expenses \n"
                "Please select which option by the number: ")

def Expense_Addition():
    if menu == '1':
        category =  input("Please enter the categogry for this expense: ").lower().strip().title()
        amount = float(input("Enter the amount for this expense: "))
        date = input("Please enter the date for when this expense is due in YYYY/MM/DD format: ")

Expense_Addition()

def Expense_View():
    if menu == '2':
    yada yada

Expense_Addition()

def Categorize_Expenses():
    if menu == '3':
    yada yada

Categorize_Expenses()

def Total_Expenses():
    if menu == '4':
    yada yada

Total_Expenses()

def Expense_Deletion():
    if menu == '5':
    yada yada

Expense_Deletion()