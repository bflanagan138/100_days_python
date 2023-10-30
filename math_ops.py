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


