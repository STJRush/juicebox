Haunted House Game: Summer Assessment 2021

#jd
this is the start of our haunted house game.
the players starts in the firtst room which is the front lawn outside the haunted house

#GAME STARTS HERE

# OUTSIDE ROOM
def outside():

  while True:

    print("You are standing on the lawn of the haunted house, and slowly proceed to make your way up to the front door.")

    choice1 = input("You're now at the front door, what do your do? f(go forward and enter the house), b(run far away and never go near the haunted house again)")

    if choice1 == "f":
      print("You push open the creeky door and wearily make your way into the haunted house")
      break
      #lobby()

    elif choice1 == "b":
      print("You run far away and never ever comeback!!")
      break
      #gameover()

    else:
      print("THAT IS NOT AN OPTION!")
