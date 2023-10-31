# water_level = int(input("What is the water level? "))

# if water_level >= 80:
#   print("Turn off water")
# else:
#   print("Don't touch that valve")

# #odd or even

# if water_level % 2 == 0:
#   print("Your water level is even.")
# else:
#   print("Your water level is odd.")

# #nested conditionals

# age = int(input("Please enter your age "))

# if age >= 18:
#   height = int(input("Please enter how tall you are in inches "))
#   if height >= 55:
#     print("Enjoy the ride!")
#   else:
#     print("I'm sorry, you are not tall enough to ride this")
# else:
#   print("I'm sorry, you are not old enough to ride this")

# age_2 = int(input("How old are you? "))

# if age_2 < 12:
#   print("That will be $7")
# # elif age_2 == 12 or 13 or 14 or 15 or 16 or 17:
# #   print("That will be $8")
# elif age_2 >= 12 and age_2 < 18:
#   print("That will be $8")
# else:
#   print("That will be $9")

# #advanced bmi calculator
# #input weight in kg
# weight = input("Please enter your weight in kg ")
# #input height in meters
# height = input("Please enter your height in meters ")
# #calculate bmi
# bmi = float(weight) / float(height) ** 2
# #print output of bmi
# if bmi <= 18.5:
#   print("Your BMI is " + str(bmi) + ", please proceed to your nearest Carl's Jr")
# elif bmi > 18.5 and bmi < 25:
#   print("Your BMI is " + str(bmi) + ", keep doing what you are doing!")
# else:
#     print("Your BMI is " + str(bmi) + ", please drop the chalupa")

# leap year calculator

year = int(input("Enter a year "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print(f"{year} is a leap year")
    else:
      print(f"{year} is not a leap year")
  else:
    print(f"{year} is a leap year")
else: 
  print(f"{year} is not a leap year")

