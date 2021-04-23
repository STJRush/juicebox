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



this is the second room of our haunted house
it is the hallway through the front door if the user choses to go through the front door of the haunted house

# HALLWAY ROOM
def lobby():

  while True:

    print("YOU ARE NOW IN THE HALLWAY")
    print("THE FRONT DOOR SUDDENLY SLAMS SHUT AND LOCKS BEHIND YOU!!!")

    choice1 = input("You see a door (l)eft and (r)ight, what do your do")

    if choice1 == "l":
      print("You go left")
      break
      #sittingRoom()

    elif choice1 == "r":
      print("You go thorugh the right door")
      break
      #kitchen()

    else:
      print("THAT IS NOT AN OPTION!")
      
Today I added a score keeper to our haunted house game.

#This is a score keeper to keep track of the points the playe earns during the game.
#Players earn points for making the correct decisions.

global score 
score = 0
