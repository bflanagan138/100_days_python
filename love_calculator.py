print("The Love Calculator is calculating your score")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")
score1 = 0
score2 = 0
for i in name1.lower() and name2.lower():
  if i == 'l' or i == 'o' or i == 'v' or i == 'e':
    score2 = score2 + 1
  elif i == 't' or i == 'r' or i == 'u' or i == 'e':
    score1 = score1 + 1
# for i in name2.lower():
#   if i == 'l' or i == 'o' or i == 'v' or i == 't' or i == 'r' or i == 'u':
#     score2 = score2 + 1
#   elif i == 'e':
#     score2 = score2 + 2
compatible = range(40, 50)
print(compatible)
love_score = int(repr(score1)[-1] + repr(score2)[-1])
print(f"Your love score is {love_score}")
if love_score <= 10 or love_score >= 90:
  print("You are far from compatible")
elif love_score >= 40 and love_score <= 50:
  print("You are completely compatible")
else: 
  print("Eh, you'll do fine")