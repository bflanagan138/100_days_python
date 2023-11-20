import random
i = int(input("Please enter a whole number\n"))
j = int(input("Please enter a whole number larger than your first number\n"))
a = random.randint(i, j)

print(f"A random number between {i} and {j} is {a}")