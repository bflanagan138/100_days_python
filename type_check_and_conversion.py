name = len(input("What is your name?"))
num_char_str = str(name)
print("Your name has " + num_char_str + " characters")

float_a = float(12345)
print(float_a)

print(str(float_a + 123.56))

#quiz: write program that adds digits in 2 digit number
#get number input
number = input("type in any 2 digit number and press enter ")
#break number into separate digits
num_1 = int(number[0])
num_2 = int(number[1])
#add digits together
sum_digits = str(num_1 + num_2)
#respond with answer
print("Your number's individual digits added together equals " + sum_digits )