
print("Thank you for choosing Python Pizza!")
size = input("What size would you like? Please type S M or L ")
pepp = input("Would you like peperoni? Please type Y or N ")
cheese = input("Would you like extra cheese? Please type Y or N ")
cost = 0

if size == "S" or size == "s":
  cost += 15
elif size == "M" or size == "m":
  cost += 20
else:
  cost += 25

if cheese == "Y" or cheese == "y":
  cost += 1

if pepp == "Y" or pepp == "y":
  if size == "S" or size == "s":
    cost += 2
  else:
    cost += 3


print(f"Your pizza total is ${cost}")
  
  
