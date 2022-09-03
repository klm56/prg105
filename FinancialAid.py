""" DATA
student_status = user input(current or new)
current_gpa = float
felony = boolean
credit_hours = int
gross yearly income = float

PROCESSING
The program will have to identify if the user is eligible for financial aid based on their inputs for all if the
variables.
student_status == new  keep going
student_status == current  ask gpa
current_gpa >= 2.0 continue
else: eligible_aid = False
felony - if True eligible_aid = False
credit_hours < 6  eligible_aid = False
yearly income >= 50,000  eligible_aid = False

OUTPUT
Display if the user is eligible (yes,no) for financial aid.
"""
# Ask for data input and add if,or,else statements for each answer.
eligible_aid = True
student_status = input("Are you a new or returning student? (Enter n or r):")
if student_status == 'r' or student_status == 'R':
    current_gpa = float(input("What is your current GPA?:"))
    if current_gpa < 2.0:
        eligible_aid = False
felony = input("Have you ever been convicted of a felony? (Enter y or n):")
if felony == 'y' or felony == 'Y':
    eligible_aid = False
credit_hours = int(input("How many credit hours are you enrolled for next semester?:"))
if credit_hours < 6:
    eligible_aid = False
yearly_income = float(input("What is your gross yearly income, rounded to the nearest dollar?(No commas):"))
if yearly_income > 50000:
    eligible_aid = False
# Output answers depending on user input
if eligible_aid:
    print("You are eligible to apply for financial aid.")
else:
    print("You are not eligible to apply for financial aid.")
