print("The Love Calculator is calculating your score")
name1 = input("What is your name?")
name2 = input("What is their name?")
love_score = 0
for i in name1 and name2:
  if i == 'l' or i == 'o' or i == 'v' or i == 't' or i == 'r' or i == 'u':
    love_score = love_score + 1
  elif i == 'e':
    love_score = love_score + 2

print(f"Your love score is {love_score}")