print("Welcome to Treasure Island. Your mission is to find the treasure")
step_1 = input("Would you like to go left or right?\nType left or right\n")
if step_1 == "right":
  print("You have fallen off a cliff. Game over.")
elif step_1 == "left":
  step_2 = input("You come to a beach. Do you want to go for a swim or wait on the beach?\nType swim or wait\n")
  if step_2 == "swim":
    print("You are eaten by a shark. Game over.")
  elif step_2 == "wait":
    step_3 = input("You notice a small cabin with 3 doors on the beach and decide to go inside. Do you enter the red door, yellow door, or blue door?\nType red yellow or blue\n")
    if step_3 == "red":
      print("Once the door is opened, an axe swings from the ceiling and lands firmly in your head. Game over")
    elif step_3 == "blue":
      print("You hear a quick clicking noise, and then see the explosives in the corner of the room just in time to watch them ignite. Game over")
    elif step_3 == "yellow":
      print("You enter a room filled from floor to ceiling with gold, diamonds and other precious metals.\nYou have found the treasure!")



