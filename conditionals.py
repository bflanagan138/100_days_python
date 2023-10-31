water_level = int(input("What is the water level? "))

if water_level >= 80:
  print("Turn off water")
else:
  print("Don't touch that valve")

#odd or even

if water_level % 2 == 0:
  print("Your water level is even.")
else:
  print("Your water level is odd.")

#nested conditionals

age = int(input("Please enter your age "))

if age >= 18:
  height = int(input("Please enter how tall you are in inches "))
  if height >= 55:
    print("Enjoy the ride!")
  else:
    print("I'm sorry, you are not tall enough to ride this")
else:
  print("I'm sorry, you are not old enough to ride this")

age_2 = int(input("How old are you? "))

if age_2 < 12:
  print("That will be $7")
# elif age_2 == 12 or 13 or 14 or 15 or 16 or 17:
#   print("That will be $8")
elif age_2 >= 12 and age_2 < 18:
  print("That will be $8")
else:
  print("That will be $9")