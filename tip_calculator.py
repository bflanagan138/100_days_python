#total bill
total = input("Welcome to the tip calculator.\n What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
tip_percentage = float(tip) / 100
people = input("How many people to split the bill? ")
per_person = round(((float(total) * float(tip_percentage)) + float(total)) / float(people), 2)
print(f"Each person should pay: ${per_person} ")