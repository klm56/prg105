"""
Create a program that helps someone create a budget. It should ask the user for monthly income
and for each of the following expenses:
Housing
Food
Transportation
Phone
Utilities
Clothing
The program should get input from the user and convert each of the inputs to floats.
The program should calculate and display the income percentage of each budget item.
The program should also tell the user how much money they have left after subtracting
the budgeted items from the income.
Submit you plan as a Word document or plain text file (.txt).
"""
print("This program will help you create a personalized budget")
print("")
Monthly_income = float(input(f"What is your total net monthly income?"))
Housing = float(input(f"How much do you spend on housing each month?"))
Transport = float(input(f"How much do you spend in transportation each month?"))
Phone = float(input(f"How much do you spend on your phone bill each month?"))
Utilities = float(input(f"How much do you spend on utilities each month?"))
Clothes = float(input(f"How much do you spend on clothing each month?"))

# I could not get the print percent code provided to work,so I used this coding instead.
Housing2 = format(Housing / Monthly_income * 100, ",.2f")
Transport2 = format(Transport / Monthly_income * 100, ",.2f")
Phone2 = format(Phone / Monthly_income * 100, ",.2f")
Utilities2 = format(Utilities / Monthly_income * 100, ",.2f")
Clothes2 = format(Clothes / Monthly_income * 100, ",.2f")

print("Housing takes up", Housing2 + "%", "of your monthly income")
print("Transportation takes up", Transport2 + "%", "of your monthly income")
print("Phone bill takes up", Phone2 + "%", "of your monthly income")
print("Utilities takes up", Utilities2 + "%", "of your monthly income")
print("Clothing takes up", Clothes2 + "%", "of your monthly income")

Final = format(Monthly_income - Housing - Transport - Phone - Utilities - Clothes, ",.2f")

print("You have $", Final + " left from your income after paying these monthly expenses.")
