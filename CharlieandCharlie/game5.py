from time import sleep
import pygame
pygame.init()

gameDisplay = pygame.display.set_mode((500,350))

houseImg = pygame.image.load('Hounted-House.jpg')

gameDisplay.blit(houseImg, (0,0))
pygame.display.update()
sleep(2)

def outside():
  
  choice = input ("Would you like to go into it to? - y/n?")

  if choice == "y":
    print("You enter the house and the house looks like no one has lived there for years")
    lobby() 

  else:
    print("The mysterious figure cathces up and you died... Game over!")
    print(" .-.")
    print("(o o) boo!")
    print("| O \./")
    print(" \   \.")
    print("  `~~~'")


def lobby():
  
  choice = input ("In the lobby you see a door to your left and to your right, which one will you choose - l/r?")

  if choice == "l":
    print("You go left and enter the kitchen")
    kitchen()

  elif choice == "r":
    print("You go right and enter the living room")
    living()

  else:
    print("The mysterious figure cathces up and you died... Game over!")
    print(" .-.")
    print("(o o) boo!")
    print("| O \./")
    print(" \   \.")
    print("  `~~~'")
    

def kitchen():
  choice = input ("In the kitchen you see a stairs going up and a stairs going down, which way do you want to go? - u/d?")

  if choice == "d":
    
    print("You go down the stairs into a basement")
    basement()

  elif choice == "u":
    print("You go up the stairs and see a very long hallway")
    upstairs()

  else:
    print("The mysterious figure cathces up and you died... Game over!")
    print(" .-.")
    print("(o o) boo!")
    print("| O \./")
    print(" \   \.")
    print("  `~~~'")


def upstairs():

  choice = input("You see 3 doors, which one wil you do you want to open? - 1/2/3")

  if choice == "1":
    print("You walk into a bedroom and see a ghost, it comes up to you and you died... Game over!")
    print(" .-.")
    print("(o o) boo!")
    print("| O \./")
    print(" \   \.")
    print("  `~~~'")

  elif choice == "2":
    print("You go into a bedroom and see another door")
    two()

  elif choice == "3":
    print("The door is locked and won't open")
    three()

  else:
    print("The mysterious figure cathces up and you died... Game over!")
    print(" .-.")
    print("(o o) boo!")
    print("| O \./")
    print(" \   \.")
    print("  `~~~'")


def two():

  choice = input("Would you like to open the door? - y/n")

  if choice == "y":
    print("You open it and fall down stairs")
    basement()

  else:
    print("The mysterious figure cathces up and you died... Game over!")
    print(" .-.")
    print("(o o) boo!")
    print("| O \./")
    print(" \   \.")
    print("  `~~~'")


def three():

  choice = input("Do you want to try and kick the door open or go into a different door? - k/d")

  if choice == "k":
    print("You kick it hard and it opens")
    kick()

  elif choice == "d":
    upstairs()

  else:
    print("The mysterious figure cathces up and you died... Game over!")
    print(" .-.")
    print("(o o) boo!")
    print("| O \./")
    print(" \   \.")
    print("  `~~~'")


def kick():

  while True:

    choice = input("You see another door but it's also locked. Do you want to try to kick it open or go back to the other doors? - k/d")

    if choice == "d":
      upstairs()


def living():

  while True:

    choice = input ("There is nothing interesting in the living room, will you stay or leave - s/l?")

    if choice == "s":
      print("The mysterious figure cathces up and you died... Game over!")
      print(" .-.")
      print("(o o) boo!")
      print("| O \./")
      print(" \   \.")
      print("  `~~~'")
      break

    elif choice == "l":
      print("In the lobby you see a door to your left and to your right, which one will you choose - l/r?")
      break
    
    else:
      print("The mysterious figure cathces up and you died... Game over!")
      print(" .-.")
      print("(o o) boo!")
      print("| O \./")
      print(" \   \.")
      print("  `~~~'")


def basement():
  print("when you get to the basement the door slams shut and you hear noises coming from behind the stairs, you also see a window that leads out onto the garden")

  choice = input ("Which way will you choose - s/w?")

  if choice == "s":
    print("You look from a social distance but you can't make out what they are")
    close()

  elif choice == "w":
    print("You hop onto a table and get out of the window into the garden")
    garden()

  else:
    print("The mysterious figure cathces up and you died... Game over!")
    print(" .-.")
    print("(o o) boo!")
    print("| O \./")
    print(" \   \.")
    print("  `~~~'")


def close():
  choice = input ("Do you want to take a closer look or go out the window - c/w?")

  if choice == "c":
    print("You take a closer look and you find out their zombies!")
    zombies()

  elif choice == "w":
    print("You hop onto a table and get out of the window into the garden")
    garden()

  else:
    print("The mysterious figure cathces up and you died... Game over!")
    print(" .-.")
    print("(o o) boo!")
    print("| O \./")
    print(" \   \.")
    print("  `~~~'")


def zombies():
  print("The zombies didn't like you not social distancing so they killed you... Game over!")


def garden():

  from time import sleep
  import pygame
  pygame.init()

  gameDisplay = pygame.display.set_mode((500,350))

  lakeImg = pygame.image.load('Lake.jpg')

  gameDisplay.blit(lakeImg, (0,0))
  pygame.display.update()
  sleep(2)

  print("\033[1;32;40m In the garden you see a lake and the a driveway leading a different way out  \n")

  choice = input ("Which do you want to go to - l/d?")

  if choice == "l":
    print("When you walk up to the lake it feels cold and eerie and someone from behind pushes you into it! ")
    print("     .-.                                    ,-.")
    print("  .-(   )-.                              ,-(   )-.")
    print(" (     __) )-.                        ,-(_      __)")
    print("  `-(       __)                      (_    )  __)-'")
    print("    `(____)-',                        `-(____)-'")
    print("  - -  :   :  - -")
    print("      / `-' \.")
    print("    ,    |   .")
    print("         .                         _")
    print("                                  >')")
    print("               _   /              (\\         (W)")
    print("              =') //               = \     -. `|'")
    print("               ))////)             = ,-      \(| ,-")
    print("              ( (///))           ( |/  _______\|/____")
    print("~~~~~~~~~~~~~~~`~~~~'~~~~~~~~~~~~~\|,-'::::::::::::::")
    print("            _                 ,----':::::::::::::::::")
    print("         {><_'c   _      _.--':MJP:::::::::::::::::::")
    print("__,'`----._,-. {><_'c  _-':::::::::::::::::::::::::::")
    print(":.:.:.:.:.:.:.\_    ,-'.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:")
    print(".:.:.:.:.:.:.:.:`--'.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.")
    print(".....................................................")
    lake()

  elif choice == "d":
    print("You made it out of the house alive. You won!")
  
  else:
    print("The mysterious figure cathces up and you died... Game over!")
    print(" .-.")
    print("(o o) boo!")
    print("| O \./")
    print(" \   \.")
    print("  `~~~'")
    
  
def lake():
  print("At the bottom of the lake you see a cave but it is very far down")
  
  choice = input ("Do you want to swim to the bottom or to the top of the lake - b/t?")
  
  if choice == "b":
    print("You just about make it into the cave and open the door to it")
    cave()
    
  elif choice == "t":
    print("You make it out of the lake just in time and see that the big house is gone but instead there is a little cottage where the creepy house was?")
    from time import sleep
    import pygame
    pygame.init()

    gameDisplay = pygame.display.set_mode((500,350))

    cottageImg = pygame.image.load('Creepy Cottage.jpg')

    gameDisplay.blit(cottageImg, (0,0))
    pygame.display.update()
    sleep(2)
    top()
    
  else:
    print("You couldn't make a decision so you drowned... Game over!")
    
    
def cave():
  print("\033[1;31;40m When you open the door to the cave, there is no water inside but just torches on the wall leading down a long corridor  \n")
  
  choice = input ("Do you want to walk down the long corridor or leave to go back to the surface of the lake - w/l?")
  
  if choice == "w":
    print("You start walking down the long corridor that seems to be going on for ever")
    corridor()
    
  elif choice == "l":
    print("You leave and swim to the surface of the lake as fast as you can")
    top()
    
  else:
    print("The mysterious figure cathces up and you died... Game over!")
    print(" .-.")
    print("(o o) boo!")
    print("| O \./")
    print(" \   \.")
    print("  `~~~'")
    
    
def corridor():
  print("You eventually reach the end of the corridor and there is a door")
  
  choice = input ("Do you want to go through the door or leave the cave and up to the surface of the lake - d/l?")
  
  if choice == "d":
    print("You walk through the door and end up in the kitchen of the creepy house")
    kitchen()
    
  elif choice == "l":
    print("You leave and swim to the surface of the lake as fast as you can")
    top()
    
  else:
    print("The mysterious figure cathces up and you died... game over!")
    print(" .-.")
    print("(o o) boo!")
    print("| O \./")
    print(" \   \.")
    print("  `~~~'")
    
   
def top():
  print("\033[1;35;40m You make it out of the lake just in time and see that the big house is gone but instead there is a little cottage where the creepy house was?r  \n")
  
  
  choice = input ("Do you want to go into the cottage or leave through the driveway - c/d?")
                  
  if choice == "c":
    print("You enter the cottage and you are in a eery little hallway")
    hallway()
                  
  elif choice == "d":
    print("You made it out of the house alive. You won!")
                  
  else:
    print("The mysterious figure cathces up and you died... Game over!")
    print(" .-.")
    print("(o o) boo!")
    print("| O \./")
    print(" \   \.")
    print("  `~~~'")
                  
       
def hallway():
  print("In the hallway you see one door to your left and another to your right")
                  
  while True:
                  
    choice = input ("Which door do you want to go through - l/r?")

    if choice == "l":
      print("You walk into a little sitting room and see the mysterious figure in the corner, it runs up to you and you die... game over!")
      break

    elif choice == "r":
      print("You enter a kitchen but see the mysterious figure and it runs up to you")
      print(".-.")
      print("(o o) boo!")
      print("| O \./")
      print(" \   \.")
      print("  `~~~'")
      figure()
      break
                  
    
def figure():
  print("What will you do?")
                  
  choice = input ("Do you want to run away or fight back - r/f?")
                  
  if choice == "r":
    print("You made it out of the house alive. You won!")
                  
  elif choice == "f":
     print("He bet you up and you died... Game over!")
                  
  
outside()
