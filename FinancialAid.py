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
# Ask for data input
eligible_aid = True
student_status = input("Are you a new or returning student? (Enter n or r):")
current_gpa = float(input("What is your current GPA?:"))
felony = input("Have you ever been convicted of a felony? (Enter y or n):")
credit_hours = int(input("How many credit hours are you enrolled for next semester?:"))
yearly_income = float(input("What is your gross yearly income, rounded to the nearest dollar?(No commas):"))

if student_status == 'n':
    eligible_aid = True
else:
    eligible_aid = False
    print("You are not eligible for financial aid.")
