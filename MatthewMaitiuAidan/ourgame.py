from time import sleep
score = 0
def goblinfight1n1():
  print("The loot goblin swings its mace at you. It collides with you breaking all of your bones turning you to jellow, the last thing you hear is it cackeling whilst saying 'I'm the victim here!' ")
  sleep(2)
  choice5 = input("you have died, restart Y/Y")
  if choice5 == "Y":
    outside()
  else:
    print("nuh uh mister!")
    sleep(2)
    outside()




def goblinfight1y():
 print("The loot goblin swings its mace at you.")
 print("You mange to dodge the mace")
 print("You hit the loot goblin with your wooden sword and kill it.")
 print("you gain a point!")
 score + 1


def goblinfight1():
  choice = input(". You see a goblin jump dow from the rafters, do you wish to fight it? Y/N")
  if choice == "Y":
    goblinfight1y()
  if choice == "N":
    goblinfight1n1()
  else:
    print("NUH UH MISTER!")
    goblinfight1()

def tutorialroom():
  choice2 = input("Do you want to me to explain the tutorial to you?(Y/N ) ")
  if choice2 =="Y": 
   print(" Paul: You have chosen the tutorial, congrats. In this game, choices matter!")
   
   print ("Paul: During this game the choices you make as the player determine how you progress throughout the dungeon!")
   
   print("Paul: Enjoy ") 
   goblinfight1()
  
  if choice2 == "N":
    goblinfight1()
  


def outside():
  while True:  
    print("THE DUNGEON")

    print("Welcome to dungeon. I am your guide  Paul the ultimate destroyer of world ruler of the forgotten kingdom and I will help you throughout your adventure in THE DUNGEON. ")

    print("NOW ENTER THE DUNGEON!!! ")

    choice1 = input ("You see a big door appear in front of you. What do you do?F(forward), B ( Run away like a lil poo poo brain")

    if choice1 == "F" :
      print("You enter the dungeon *scary noises")
      tutorialroom()
      break

    elif choice1 == "B" :
      print (" You run away like a lil poo poo brain ......")
      break

    else:
      print (" NOT AN OPTION")
    outside()




while True:  
    print("THE DUNGEON")

    print("Welcome to THE DUNGEON!!!!! I am your guide  Paul the ultimate destroyer of world ruler of the forgotten kingdom and I will help you throughout your adventure in THE DUNGEON!!! ")

    print("NOW ENTER THE DUNGEON!!! ")

    choice1 = input ("You see a big door appear in front of you. What do you do?F(forward), B ( Run away like a lil poo poo brain")

    if choice1 == "F" :
      print("You enter the dungeon *scary noises")
      tutorialroom()
      break

    elif choice1 == "B" :
      print (" You run away like a lil poo poo brain ......")
      break

    else:
      print (" NOT AN OPTION")
    outside()
