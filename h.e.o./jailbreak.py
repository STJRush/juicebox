#random imports from libraries to make the code function properly
from colorama import Fore
import sys, time
from time import sleep
import random
import pygame
pygame.init()

#sets the window size
gameDisplay = pygame.display.set_mode((400,300))


#loads in your pics to use later
locationmarker = pygame.image.load('google-pin-icon-12.png')
jailmap = pygame.image.load('jail-concept-final.png')

def printlocation(x,y):
  gameDisplay.blit(jailmap, (0,0))
  pygame.display.update()
  gameDisplay.blit(locationmarker, (x,y))
  pygame.display.update()
  sleep(2)

#code for encounters
def Encounterr():
  
  print("   ")
  #the small line which chooses a random number between 1 and 3 to decide if you get an encounter
  EnemyEncounter = random.randint(1, 3)
  

    #the code for the actual fight
  def fight(): 
    random_number = random.randint(1, 10)
    random_minimum = random.randint(2, 9)

    #this is just the code to make the text appear as if it was being typed
    for c in "This enemies health is ":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
    print

    #this was originally a debug code but now it tells the user the health of the enemy
    print(random_minimum)

    sleep(2)
      
    #the same as last time this just makes it appear as if someone was typing
    for c in Fore.WHITE + "rolling your damage....... you hit the enemy for ":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
    print
      
    #this was debug code but now it tells the user how much damage the player did
    print(random_number)

    #this is the code to decide if you did enough damage to eliminate the enemy
    if random_number >= random_minimum:
      for c in Fore.WHITE + "You hit the enemy with enough force to eliminate him":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print
    else:
      for c in Fore.WHITE + "you were to weak, go back to training":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print
      sleep (1)
      gameover()

  


  #the code if you failed the chance encounter
  def Nencounter():
    
    for c in Fore.WHITE + "You did not encounter an enemy":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
    print


  #the code if you succeded the chance enounter
  def Yencounter():

    #code to appear as if you were typing
    for c in Fore.WHITE + "You encountered an [Enemy] ":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
    print

    sleep(1)
      
    #if this def is chosen it started the fight def
    fight()


  #just the code to decide if you get an encounter or not
  if EnemyEncounter < 2:
    Yencounter()
  else:
    Nencounter()

#the code for the jailcell part of the game
def jail_cell():
  printlocation(145,240)
  while True:
    
    #just some random backstory
    for c in Fore.GREEN + "Escape from jail, You can only go one way, You cannot go back, So choose wisely, Succeed or you will die.":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
    print
    print("   ")

    #code to decide if you leave the cell or not
    jail_cell_ = input(Fore.RED + "You're at the door, what do you do? n(go north), s(you stay in jail.)")

    #if you decide to leave this will run
    if jail_cell_ == "n":
      
      #this is just some random dialouge lol
      for c in Fore.YELLOW + "you notice your cell door is not locked properly. you pick it with hair clips you got for your fellow inmate.":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print

      corridor()
      break

    #this code will run if you decide to stay in the cell resulting in a restart of the game
    elif jail_cell_ == "s":
      print(Fore.YELLOW + "you stay behind bars. unable to do anything or see anyone.")
      gameover()
      break

    #if the player types anything but the correct letter this code will run
    else:
      print(Fore.YELLOW + "you can't go there.")

#the code for the gameover section of "jailcell"
def gameover():
  print(Fore.YELLOW + "you die of depression in a jail where your soul will be trapped till the end of this universe.")
  exit()

#the code for section two, the corridot of left and right
def corridor():
  printlocation(145,210)
  Encounterr()

  while True:

    print("   ")

    #when you leave the cell you are given two options to walk, its up to you xD
    for c in Fore.RED + "You're in the corridor, what do your do? n(go north), w(go west)":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
    print

    choice1 = input("  ")

    #here it says that if you choose east it will run this code
    if choice1 == "n":
     
      #this code just says if you chose east you will see a cafeteria
      for c in Fore.YELLOW + "you walk north. you open a big door and see tables and chairs.":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print

      cafeteria()
      break


    #if you chose to walk west this code will run
    elif choice1 == "w":

      #this code says if you chose west you will find a gym
      for c in Fore.YELLOW + "you walk west, you found the gym":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print
      gym()
      break

    #this code is to prevent people from typing anything not allowed
    else:
      for c in Fore.YELLOW + "Not an option buddy, get lost":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print

#this is the code for the cafeteria section
def cafeteria():
  printlocation(150,130)
  Encounterr()

  while True:

    print("   ")

    #this code gives you two options to walk
    for c in Fore.RED + "You're at the cafeteria, what do your do? n(go north), s(go south)":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
    print

    choice1 = input("  ")

    #this code says if you chose right _______ will happen
    if choice1 == "n":
      
      #ignore this for now please as this is incomplete___________________________
      for c in Fore.YELLOW + "you walk north. you open a solid metal door. You walk outside into the yard":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print

      yard()
      break


    #this code is if you chose to go left
    elif choice1 == "s":

      #it says another room as this is incomplete, ignore this _______________________________________
      for c in Fore.YELLOW + "you walk south. you arrive at the corridor you started from":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print

      corridor()
      break


    #once again this code is for those who try to be rebels, VIVA LA REVOLUTION
    else:
      for c in Fore.YELLOW + "Not an option buddy, get lost":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print

#this is the code for the gym section
def gym():
  printlocation(15,130)
  Encounterr()

  while True:

    print("   ")

    #this gives you two options to walk while in the gym
    for c in Fore.RED + "You're at the gym, what do your do? n(go north), e(go east)":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
    print

    choice1 = input("  ")

    #if you chose to go north this code will run
    if choice1 == "n":
     
      #listen here buddy we aint finished alright?________________________________________
      for c in Fore.YELLOW + "you walk through a door. you see tall shelves filled with books.":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print

      library()
      break

    #if you chose south this will run
    elif choice1 == "s":

      #you ancounter :O, another room that isnt finished, my oh my you could have forseen this :)
      for c in Fore.YELLOW + "you walk south. you arrive at the corridor you started from":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)

      print
      corridor()
      break


    #gotta stop them rebels so this code makes it so the game dosnt die because of a crash xD
    else:
      for c in Fore.YELLOW + "Not an option buddy, get lost":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print

#this is the code for the gym section
def library():
  printlocation(20,10)
  Encounterr()

  while True:

    print("   ")
    
    #this code just asks which direction you want to go
    for c in Fore.RED + "You're at the library, what do your do? e(go east), ne(go north east), s(go south)":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
    print

    #input your answer you noob
    choice1 = input("  ")

    #so you chose east lmao
    if choice1 == "e":
     
      #hey look some random dialouge
      for c in Fore.YELLOW + "you walk east. you open a solid metal door and walk outside into the yard.":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print

      yard()
      break

    #oh god surgical equipment now that sends shivers down the spine
    elif choice1 == "ne":
      for c in Fore.YELLOW + "you see hospital beds and surgery equipment.":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print
      hospital()
      break

    #never thought you would go with south
    elif choice1 == "s":
      
      #how much dialouge is in this stupid game smh
      for c in Fore.YELLOW + "you walk south, you found the gym":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print
      
      gym()
      break


    #how dare you rebel, time to activate dictator mode scrub
    else:
      for c in Fore.YELLOW + "Not an option buddy, get lost":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print

#this is the code for the yard section
def yard():
  printlocation(150,60)
  Encounterr()

  while True:

    print("   ")

    #decide north, south, west or east... the choice is yours (matrix reference pog)
    for c in Fore.RED + "you are in yard, what do your do? n(go north), s(go south), w(go west), e(go east)":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
    print

    choice1 = input("  ")

    #it seems you chose west
    if choice1 == "w":
      
      #lmao not finished yet nerd
      for c in Fore.YELLOW + "you walk through a door. you see tall shelves filled with books.":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print

      library()
      break


    #hmmm you chose south lmao nerd (you a nerd as you are reading the code lmao)
    elif choice1 == "s":

      #we aint finished so BEGONE THOT
      for c in Fore.YELLOW + "you walk south. you open a big door. you see tables and chairs.":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)

      print
      cafeteria()
      break

    #it seems you chose east (help riting comments is a pain)
    elif choice1 == "e":
      for c in Fore.YELLOW + "you walk east. you remember this room. it is the room where you met your loved ones frequently.":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)

      print
      meeting_room()
      break

    #you know what imma say "It seems you chose north" so begone nerd
    elif choice1 == "n":
      for c in Fore.YELLOW + "you walk through a dorway. you see hospital beds and surgery equipment.":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)

      print
      hospital()
      break

    #hahahahahah you fool you absolute imbecile you cant choose that HAHAHAHAHA
    else:
      for c in Fore.YELLOW + "Not an option buddy, get lost":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print

#this is the code for the yard section
def hospital():
  printlocation(100,0)
  Encounterr()

  while True:

    print("   ")

    #pain you choose which direction west, south, east? i dont care nerd
    for c in Fore.RED + "You're at the hospital, what do your do? w(go west), s(go south) e(go east)":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
    print

    choice1 = input("  ")

    #you are still reading? welp you the user chose west lmao nerd get rekt
    if choice1 == "w":
      
      #we are not finished but we would like to talk to you about your car extendency warranty
      for c in Fore.YELLOW + "you walk through a door. you see tall shelves filled with books.":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print

      library()
      break


    #ha only nerds choose south so you a nerd
    elif choice1 == "s":

      #god damn we aint finished yet? oh god
      for c in Fore.YELLOW + "you walk south. you open a solid metal door. You walk outside into the yard":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)

      print
      yard()
      break


    #guess hou chose east again you fool uou absolute imbicile
    elif choice1 == "e":
      for c in Fore.YELLOW + "you walk into a room decorated with carpets and paintings":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print
      lobby()
      break

    else:
      for c in Fore.YELLOW + "Not an option buddy, get lost":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print

def lobby():
  printlocation(220,0)
  Encounterr()

  while True:

    print("   ")

    for c in Fore.RED + "You're in the lobby, what do your do? n(go north), s(go south), w(go west), e(go east)":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
    print

    choice1 = input("  ")

    if choice1 == "w":
     
      for c in Fore.YELLOW + "you walk through a dorway. you see hospital beds and surgery equipment.":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print

      hospital()
      break


    elif choice1 == "s":
      for c in Fore.YELLOW + "you walk east. you remember this room. it is the room where you met your loved ones frequently.":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print
      meeting_room()
      break

    elif choice1 == "e":
      for c in Fore.YELLOW + "you see cctv cameras and guns.":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print
      guards_office()
      break

    elif choice1 == "n":
      for c in Fore.YELLOW + "you walk through a large door":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print
      exit_door()
      break

    else:
      for c in Fore.YELLOW + "Not an option buddy, get lost":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print
    
def meeting_room():
  printlocation(320,120)
  Encounterr()

  while True:

    print("   ")

    #this gives you two options to walk while in the gym
    for c in Fore.RED + "You're at the meeting room, what do your do? n(go north), w(go west)":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
    print

    choice1 = input("  ")

    #if you chose to go north this code will run
    if choice1 == "n":
     
      #listen here buddy we aint finished alright?________________________________________
      for c in Fore.YELLOW + "you walk into a room decorated with carpets and paintings":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print

      lobby()
      break

    #if you chose west this will run
    elif choice1 == "w":

      #you ancounter :O, another room that isnt finished, my oh my you could have forseen this :)
      for c in Fore.YELLOW + "you walk west. you open a solid metal door. You walk outside into the yard":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)

      print
      yard()
      break


    #gotta stop them rebels so this code makes it so the game dosnt die because of a crash xD
    else:
      for c in Fore.YELLOW + "Not an option buddy, get lost":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print

def guards_office():
  printlocation(340,0)
  Encounterr()

  while True:

    print("   ")

    #this gives you one option to walk while in the guards office
    for c in Fore.RED + "You're at the guards office, what do your do? w(go west)":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
    print

    choice1 = input("  ")

    #if you chose to go west this code will run
    if choice1 == "w":
     
      #listen here buddy we aint finished alright?________________________________________
      for c in Fore.YELLOW + "you walk into a room decorated with carpets and paintings":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print

      lobby()
      break

    #gotta stop them rebels so this code makes it so the game dosnt die because of a crash xD
    else:
      for c in Fore.YELLOW + "Not an option buddy, get lost":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print

def exit_door():

  print("    ")

  while True:
    try:
      for c in Fore.WHITE + "what do you rate this game outta 10?":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print
      Rating = input(" ")
      RealRating = int(Rating)
      break
    except ValueError:
      for c in Fore.WHITE + "not a number you idiot":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print
      print(" ")
  for c in Fore.WHITE + "You encounter a boss.":
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.07)
  print
  print(" ")
  for c in Fore.WHITE + "the health of this boss is ":
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.07)
  print
  print(10)
  for c in Fore.WHITE + "rolling your damage....... you hit the enemy with your rating!":
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.07)
  print
  print(" ")

  if RealRating >= 10:
    for c in Fore.WHITE + "You hit the enemy with enough force to eliminate him. thanks for playing :)":
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(0.07)
    print
  else:
    for c in Fore.WHITE + "you were to weak, go back to training":
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(0.07)
    print
    gameover()
jail_cell()
