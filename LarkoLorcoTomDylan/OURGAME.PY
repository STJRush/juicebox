from time import sleep 

def gameover():
  print("you died, please try again")
  raise exit()
 
print("\033[0;31;40m \n")
print("to win you must kill 3 impostors")

print("\033[0;37;40m\n")
print("You see your front door and there is a bloody arrow on the floor")

choice = input("Forward yes or no? ")

print("\033[0;31;40m \n")
if choice =="yes":print("you walk forward")
print("You go right through the door anyways, a wild centaur will guide you through the hall to the kitchen")
if choice =="no": 
  while True:
   print("game over, you didn't wanna play, please run again")
print("You are in the hall and you see a door to the left. Do you go in?")

print("\033[0;37;40m \n")
choice = input("yes or no? ")

print("\033[0;31;40m \n")
if choice =="yes":
   while True:
     print("game over you died")
      
 
else:print("you have not failed yet")

if choice =="no":
   print("gordon ramsay is cooking pizza with pineapple on it do you want some?")
   
print("\033[0;37;40m \n")
choice = input("yes or no? ")

print("\033[0;31;40m \n")
if choice =="yes":
   print("gordon ramsay thinks pineapple doesnt belong on pizza, he is an impostor,you get murdered by his pizza cutter, game over, please run again")
   gameover()

if choice =="no":
   print("the centaur kills gordon with his own pizza cutter, he tells you gordon ramsay hates pineapple on pizza and that he was an impostor")

print("would you like to take the elevator or the stairs")

print("\033[0;37;40m \n")
choice = input("elevator or stairs? ")

print("\033[0;31;40m \n")
if choice =="stairs":
    print("when you arrive at the 3rd floor the centaur needs a bathroom break, when hes finished he asks you to come in and check, something crazy has happened do you go in? ")

if choice =="elevator":
    print("the elevator has broken and your inside, the centaur melee attacks you with his bow and you die, game over")
    gameover()

print("\033[0;37;40m \n")
choice = input("yes or no? ")

print("\033[0;31;40m \n")
if choice =="yes":
   print("a lynx is in the shower,he is weak, near the verge of death, the centaur hands you a sword and tells you to finish him. ")

if choice =="no":
  print("You are dead. Survive next time. Please retry and win next time.")
  gameover()

sleep(1.2)

bagList = []

print("Do you want to pick up this sword?")

print("\033[0;37;40m \n")
choice = input ("yes or no? ")

print("\033[0;32;40m \n")
if choice == "yes":print("SWORD COLLECTED")

print("\033[0;31;40m \n")
if choice == "no":
  print("You walk away from the sword")
  gameover()

bagList.append("sword")



if "sword" in bagList:
  sleep(1.2)
  print("The centuar shouts 'FINISH HIM', do you want to finish him? ")

print("\033[0;37;40m \n")
choice = input ("yes or no? ")

if choice =="yes":print("You stab him in the chest, GAME OVER YOU WIN!") 
if choice =="no":print("You refuse to finish the centuar, you walk away from the castle, you coward... GAME OVER.")
exit()
