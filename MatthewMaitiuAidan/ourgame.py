from time import sleep
import pygame
pygame.init()
score = 0
from pygame import mixer

from time import sleep

def hallwayv22():
  print("you enter the door and before you lies a dark hallway. you walk down the hall only to find another door. You enter...")
  room2()
  
def hallway222():
  print("you enter the door and before you lies a dark hallway. you walk down the hall only to find another door. You enter..,.")
  room3()

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
  mixer.init()

mixer.music.load("251_Candledeep.mp3")

mixer.music.play()
sleep(100)
mixer.music.stop()

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

   def room3():
 choice=input("You sprint into the next room for no reason except for dramatic effect. You see a man in wizard robe and hat stand in front of you. Do you speak to him? Y/N...")
 if choice =="Y":
    choice = input ("You choose to speak to him but before you manage to say anything he interrupts you. The wizard says 'I AM THE GREAT WIZARD KEVIN LARVA AND YOU WILL BOW BEFORE ME '. Do you wish to fight Kevin? F/R...  ")
 

 if choice =="F":
    print("You chose to fight Kevin Larva")
    kevinfight1()

 if choice =="R": 
    print("You try to run away from the mighty Kevin Larva, but as you turn away Kevin zaps you with his Kevin Larva magic. ")
    gameoverdisplay = pygame.display.set_mode((800,500))

    gameover = pygame.image.load('death3.jpg')

    gameoverdisplay.blit(gameover, (0,0))
    pygame.display.update()
    sleep(5)

    pygame.quit()
    quit()
    outside() 
    
    else:
     print("You do nothing....Kevin gets bored and Kevin kills you with his legendary scar Fortnite. ")
     gameoverdisplay = pygame.display.set_mode((800,500))

     gameover = pygame.image.load('death3.jpg')

     gameoverdisplay.blit(gameover, (0,0))
     pygame.display.update()
     sleep(5)

     pygame.quit()
     quit()
     outside()
    
     def kevinfight1():
      choice = input("Kevin gazes into your eyes. Suddenly you think of many ways to defeat kevin.... Y/N/D/HH/ER/S/V/A/POOP...  ")
  
  
      if choice == "Y":
       print("KEVIN DOES NOT APPROVE OF THIS MOVE. HE ZAPS YOU WITH HIS KEVIN LARVA MAGIC...YOU DIE  ")
       gameoverdisplay = pygame.display.set_mode((800,500))

       gameover = pygame.image.load('death3.jpg')

      gameoverdisplay.blit(gameover, (0,0))
      pygame.display.update()
      sleep(5)

      pygame.quit()
      quit()
      outside()
      
  elif choice == "N":
   print("KEVIN DOES NOT APPROVE OF THIS MOVE. HE ZAPS YOU WITH HIS KEVIN LARVA MAGIC...YOU DIE  ")
   gameoverdisplay = pygame.display.set_mode((800,500))

   gameover = pygame.image.load('death3.jpg')

   gameoverdisplay.blit(gameover, (0,0))
   pygame.display.update()
   sleep(5)

   pygame.quit()
   quit()
   outside()
   
  
  elif choice == "D":
   print("KEVIN DOES NOT APPROVE OF THIS MOVE. HE ZAPS YOU WITH HIS KEVIN LARVA MAGIC...YOU DIE  ")
   gameoverdisplay = pygame.display.set_mode((800,500))

   gameover = pygame.image.load('death3.jpg')

   gameoverdisplay.blit(gameover, (0,0))
   pygame.display.update()
   sleep(5)

   pygame.quit()
   quit()
   outside()
   outside()
    

  elif choice == "HH":
   print("KEVIN DOES NOT APPROVE OF THIS MOVE. HE ZAPS YOU WITH HIS KEVIN LARVA MAGIC...YOU DIE  ")
   gameoverdisplay = pygame.display.set_mode((800,500))

   gameover = pygame.image.load('death3.jpg')

   gameoverdisplay.blit(gameover, (0,0))
   pygame.display.update()
   sleep(5)

   pygame.quit()
   quit()
   outside()
   outside()
    

  elif choice == "ER":
    print("KEVIN DOES NOT APPROVE OF THIS MOVE. HE ZAPS YOU WITH HIS KEVIN LARVA MAGIC...YOU DIE  ")
    gameoverdisplay = pygame.display.set_mode((800,500))

    gameover = pygame.image.load('death3.jpg')

    gameoverdisplay.blit(gameover, (0,0))
    pygame.display.update()
    sleep(5)

    pygame.quit()
    quit()
    outside()
    
    

  elif choice == "S":
     print("Of course S the only valid option....You a shoot laser beam from your chest and evaporate Kevin. You gain a ancient sword shard! You stroll to the next room. ")
     bag.append("ancient sword upper shard")
     hallway4()

  elif choice == "V":
    print("KEVIN DOES NOT APPROVE OF THIS MOVE. HE ZAPS YOU WITH HIS KEVIN LARVA MAGIC...YOU DIE  ")
    gameoverdisplay = pygame.display.set_mode((800,500))

    gameover = pygame.image.load('death3.jpg')

    gameoverdisplay.blit(gameover, (0,0))
    pygame.display.update()
    sleep(5)

    pygame.quit()
    quit()
    outside()
    

  elif choice == "A":
   print("KEVIN DOES NOT APPROVE OF THIS MOVE. HE ZAPS YOU WITH HIS KEVIN LARVA MAGIC...YOU DIE  ")
   
   outside()
 

  elif choice == "POOP": 
     print("You poop on Kevin. Kevin starts buring to death. His final words are , 'NOOOOOOOO MY K/D '. You proceed to the next room ")
     hallway4()

  else:
       print("NOT AN OPTION FOOL....KEVIN DUNKS ON YOU WITH HIS EPIC BASKETBALL SKILLS...")
       gameoverdisplay = pygame.display.set_mode((800,500))

       gameover = pygame.image.load('death3.jpg')

       gameoverdisplay.blit(gameover, (0,0))
       pygame.display.update()
       sleep(5)

       pygame.quit()
       quit()
       outside()
      
       def trollfight1():
        choice = input("You see a troll jump out of the barrel, do you wish to fight it or sneak by it? Y/N/S...")
        if choice == "Y":
        trollfight1y()
        if choice == "N":
       trollfight1n()
       if choice =="S":
       sneaktroll()

def trollfight1y():
 print("The troll swings its axe at you.")
 print("You  manage to barely dodge it ")
 print("You hit the troll with your wooden sword and kill it.")
 print("you gain a ancient sword hilt!")
 bag.append("ancient sword hilt")
 hallway11()

def trollfight1n():
  print("The troll swings its axe at you. The axe chops you in half and you guessed it you die.   ")
  sleep(2)
  choice5 = input("You have died, restart Y/Y...")
  if choice5 == "Y":
   
    outside()
  else:
    print("nuh uh mister!")
    sleep(2)
    outside() 
    
def sneaktroll():
    print("You sneak past the troll")
    hallway11()
    

  
  def room1():
   choice=input("You walk into the next room. You see another door on the other side of the room that is locked and a bunch of barrels stacked on top of each other. The top barrel starts to rattle. Do you go over to it? Y/N...")
   if choice =="Y":
    print ("You walk over to the barrel and open it....SUDDENLY A TROLL APPEARS ")
    trollfight1()
   if choice =="N": ("You do nothing....")
  
   else: 
   print("You trip over your own leg and break your face .... you die .... we do a little trolling :)")
   outside()

while True: 
  mixer.init()

  mixer.music.load("251_Candledeep.mp3")

  mixer.music.play()
  sleep(100)
  mixer.music.stop()
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
