#random imports from libraries to make the code function properly
from colorama import Fore
import sys, time
from time import sleep

sleep(0)
#the code for the jailcell part of the game
def jail_cell():

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

#the code for section two, the corridot of left and right
def corridor():

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
      for c in Fore.YELLOW + "you walk right. you see the cafeteria in the distance":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print

      cafeteria()
      break


    #if you chose to walk west this code will run
    elif choice1 == "w":

      #this code says if you chose west you will find a gym
      for c in Fore.YELLOW + "you walk right, you found the gym":
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
      for c in Fore.YELLOW + "random room here":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print

      yard()
      break


    #this code is if you chose to go left
    elif choice1 == "s":

      #it says another room as this is incomplete, ignore this _______________________________________
      for c in Fore.YELLOW + "another room":
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
      for c in Fore.YELLOW + "random room here":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print

      library()
      break

    #if you chose east this will run
    elif choice1 == "e":

      #you ancounter :O, another room that isnt finished, my oh my you could have forseen this :)
      for c in Fore.YELLOW + "another room":
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

  while True:

    print("   ")

    for c in Fore.RED + "You're at the library, what do your do? e(go east), ne(go north east), s(go south)":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
    print

    choice1 = input("  ")

    if choice1 == "e":
     
      for c in Fore.YELLOW + "random room here":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print

      yard()
      break


    elif choice1 == "ne":
      for c in Fore.YELLOW + "another room":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print
      hospital()
      break

    elif choice1 == "s":
      for c in Fore.YELLOW + "another room":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print
      gym()
      break


    else:
      for c in Fore.YELLOW + "Not an option buddy, get lost":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print

#this is the code for the yard section
def yard():

  while True:

    print("   ")

    #decide north, south, west or east... the choice is yours (matrix reference pog)
    for c in Fore.RED + "You're in the yard, what do your do? n(go north), s(go south), w(go west), e(go east)":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
    print

    choice1 = input("  ")

    #it seems you chose west
    if choice1 == "w":
      
      #lmao not finished yet nerd
      for c in Fore.YELLOW + "random room here":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print

      library()
      break


    #hmmm you chose south lmao nerd (you a nerd as you are reading the code lmao)
    elif choice1 == "s":

      #we aint finished so BEGONE THOT
      for c in Fore.YELLOW + "another room":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)

      print
      cafeteria()
      break

    #it seems you chose east (help riting comments is a pain)
    elif choice1 == "e":
      for c in Fore.YELLOW + "another room":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)

      print
      meeting_room()
      break

    #you know what imma say "It seems you chose north" so begone nerd
    elif choice1 == "n":
      for c in Fore.YELLOW + "another room":
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
      for c in Fore.YELLOW + "random room here":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print

      library()
      break


    #ha only nerds choose south so you a nerd
    elif choice1 == "s":

      #god damn we aint finished yet? oh god
      for c in Fore.YELLOW + "another room":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)

      print
      yard()
      break


    elif choice1 == "e":
      for c in Fore.YELLOW + "another room":
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

  while True:

    print("   ")

    for c in Fore.RED + "You're in the lobby, what do your do? n(go north), s(go south), w(go west), e(go east)":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
    print

    choice1 = input("  ")

    if choice1 == "w":
     
      for c in Fore.YELLOW + "random room here":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print

      hospital()
      break


    elif choice1 == "s":
      for c in Fore.YELLOW + "another room":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print
      meeting_room()
      break

    elif choice1 == "e":
      for c in Fore.YELLOW + "another room":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print
      guards_office()
      break

    elif choice1 == "n":
      for c in Fore.YELLOW + "another room":
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
      for c in Fore.YELLOW + "random room here":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print

      lobby()
      break

    #if you chose west this will run
    elif choice1 == "w":

      #you ancounter :O, another room that isnt finished, my oh my you could have forseen this :)
      for c in Fore.YELLOW + "another room":
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

  while True:

    print("   ")

    #this gives you two options to walk while in the gym
    for c in Fore.RED + "You're at the guards office, what do your do? w(go west)":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
    print

    choice1 = input("  ")

    #if you chose to go north this code will run
    if choice1 == "w":
     
      #listen here buddy we aint finished alright?________________________________________
      for c in Fore.YELLOW + "random room here":
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
  print(Fore.YELLOW + "u win lol")
  
jail_cell()
