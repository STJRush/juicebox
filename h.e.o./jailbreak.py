#random imports from libraries to make the code function properly
from colorama import Fore
import sys, time
from time import sleep


#the code for the jailcell part of the game
def jail_cell():

  while True:
    
    for c in Fore.GREEN + "Escape from jail, You can only go one way, You cannot go back, So choose wisely, Succeed or you will die.":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
    print

    print("   ")

    jail_cell_ = input(Fore.RED + "You're at the door, what do you do? f(forward), b(you stay in jail.)")

    if jail_cell_ == "f":

      for c in Fore.YELLOW + "you notice your cell door is not locked properly. you pick it with hair clips you got for your fellow inmate.":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print

      corridor()
      break

    elif jail_cell_ == "b":
      print(Fore.YELLOW + "you stay behind bars. unable to do anything or see anyone.")
      gameover()
      break

    else:
      print(Fore.YELLOW + "you can't go there.")

sleep(2)

#the code for the gameover section of "jailcell"
def gameover():
  print(Fore.YELLOW + "you die of depression in a jail where your soul will be trapped till the end of this universe.")

sleep(2)

#the code for section two, the corridot of left and right
def corridor():

  while True:
    
    print("   ")

    for c in Fore.RED + "You're in the corridor, what do your do? r(go right), l(go left)":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
    print

    choice1 = input("  ")

    if choice1 == "r":
     
      for c in Fore.YELLOW + "you walk right. you see the cafeteria in the distance":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print

      cafeteria()
      break


    elif choice1 == "l":
      for c in Fore.YELLOW + "you walk right, you found the gym":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print
      #gym()
      break


    else:
      for c in Fore.YELLOW + "Not an option buddy, get lost":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print


def cafeteria():

  while True:

    print("   ")

    for c in Fore.RED + "You're at the cafeteria, what do your do? r(go right), l(go left)":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
    print

    choice1 = input("  ")

    if choice1 == "r":
     
      for c in Fore.YELLOW + "random room here":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print

      #cafeteria()
      break


    elif choice1 == "l":
      for c in Fore.YELLOW + "another room":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print
      #gym()
      break


    else:
      for c in Fore.YELLOW + "Not an option buddy, get lost":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print
      
def gym():

  while True:

    print("   ")

    for c in Fore.RED + "You're at the gym, what do your do? r(go right), l(go left)":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
    print

    choice1 = input("  ")

    if choice1 == "r":
     
      for c in Fore.YELLOW + "random room here":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print

      #cafeteria()
      break


    elif choice1 == "l":
      for c in Fore.YELLOW + "another room":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print
      #gym()
      break


    else:
      for c in Fore.YELLOW + "Not an option buddy, get lost":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
      print
      
jail_cell()
