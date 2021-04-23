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
    
    
    
    
def dragonfight():
  choice = input("You enter a new room and you hear a hollow rumble from a distance.THE DRIP DRAGON BURSTS THROUGH THE WALL!!!. He challenges you to a battle to the death. Do you wish to to accept his challenge? Y/N") 
  
  if choice== "Y":
    dragonfight3y() 

  if choice== "N":
    dragonfight3n()

def dragonfight3y():
  print("The Drip Dragon says that whoever does the drippiest pose is the winner of this battle.")

  sleep(1)

  print("The Drip Dragon pulls out the drippiest pose you have ever seen.")

  sleep(1)

  print("You start spitting bars so valid that the Drip Dragon has nothing to do but self-combust")

  sleep(1)

  print("When the last couple of cold bars left your mouth, the Drip Dragon was unable to do anything, besides letting out a soft, SHEEEESSSHHH")
  
  print("You gained another point, WOOHOO!!!")
  
  score + 1
  

def dragonfight3n():
  print("The Drip Dragon shoots you lol. He did not burst through a wall to challenge you just for nothing to happen. tut tut tut you should have a least accepted his challenge")
  
  choice = input("You have died, Restart? Y/N")

  if choice == "Y":
    outside()

  else:
    print("So you think you have a choice huh hehe.")

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
