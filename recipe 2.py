"""
Find a simple recipe online, provide a link to the recipe in the comments. Display the ingredients with amounts and
list the servings that will be made with the recipe. Ask the user to enter how many servings they would like to make,
and display the required amount of ingredients they will need. Format to one decimal place.
Upload to GitHub and submit your URL.
"""

# base ingredients given to me
Butter_base = 0.5 / 16  # cups
Granulated_sugar_base = 0.5 / 16  # cups
Brown_sugar_base = 0.25 / 16  # cups
Vanilla_base = 2 / 16  # cups
Egg_base = 1 / 16  # eggs
Flour_base = 1.75 / 16  # cups
Baking_soda_base = 0.5 / 16  # teaspoons
Salt_base = 0.5 / 16  # teaspoons
Chocolate_chips_base = 1 / 16  # cups
serving_base = 24

print("Chocolate Chip Cookie Recipe Program")
serving_quantity = float(input("How many servings would you like?:"))
print("For" + str(serving_quantity) + "servings, you will need:")
# User serving quantity
print("Butter: " + format(serving_quantity * Butter_base, ",.1f") + " cups")
print("Granulated_sugar: " + format(serving_quantity * Granulated_sugar_base, ",.1f") + " cups")
print("Egg: " + format(serving_quantity * Egg_base, ",.1f"))
print("Vanilla: " + format(serving_quantity * Vanilla_base, ",.1f") + " teaspoons")
print("Brown_sugar_base: " + format(serving_quantity * Brown_sugar_base, ",.1f") + " cups")
print("Flour: " + format(serving_quantity * Flour_base, ",.1f") + " cups")
print("Baking_soda: " + format(serving_quantity * Baking_soda_base, ",.1f") + " cups")
print("Salt: " + format(serving_quantity * Salt_base, ",.1f") + " cups")
print("Chocolate_chips: " + format(serving_quantity * Chocolate_chips_base, ",.1f") + " cups")

