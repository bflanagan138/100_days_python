# add = 3 + 5 #three plus five
# subtract = 3 - 5 #three minus five
# #addition, subtraction, multiplication will return integers unless specified
# #division will return floats unless specified
# divide = 3 / 5 #three divided by five
# multiply = 3 * 5 #three times five
# exponent = 3 ** 5 #three to the fifth power

# print(add)
# print(subtract)
# print(divide)
# print(multiply)
# print(exponent)

#bmi index calculator
#bmi measures weight in kilograms divided by height in meters

# simple bmi calculator 
#input weight in kg
weight = input("Please enter your weight in kg ")
#input height in meters
height = input("Please enter your height in meters ")
#calculate bmi
bmi = float(weight) / float(height) ** 2
#print output of bmi
print("Your BMI is " + str(bmi))

#number manipulation

print(int( 8 / 3 ))
#will print 2, chops decimal
print(round( 8 / 3 ))
#will print 3, rounds up
print(round( 8 / 3, 2))
#will print 2.67, rounds to 2nd decimal place denoted by the 2 in parens
print( 8 // 3 )
#floor division, will return 2, chops decimal without converting to integer

#f-strings adding f in front of quotes allows mix of object types
score = 0
height = 1.8
is_winning = True

print(f"your score is {score}, your height is {height}, your winning is {is_winning}")

#write program that converts your life to how many weeks you have left in life
#assumes average person lives until 90 years old


#ask for person's age
age = int(input("How old are you? "))
#subtract age from base of 90
wks_left = (90 - age) * 52
print(f"You have {wks_left} weeks left to live")
#convert age to weeks
#subtract age from base