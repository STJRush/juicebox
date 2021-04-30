def gameover():
  print("you died, please try again")
  raise exit()
 

print("to win you must kill 3 impostors")

print("You see your front door and there is a bloody arrow on the floor")

choice = input("Forward y/n? ")

if choice =="Y":print("you walk forward")

print("You go right through the second door, a wild centaur will guide you through the hall to the kitchen")

if choice =="n":print("game over, you didnt wanna play, please run again")

print("You are in the hall and you see a door to the left. Do you go in?")

choice = input("y/n? ")


if choice =="y":
   print("you walk forward into the bathroom where an agressive dwarf attacks you and you die, game over, please run again")
   gameover()
 
else:print("you have not failed yet")

if choice =="n":
   print("gordon ramsay is cooking pizza with pineapple on it do you want some?")
   

choice = input("y/n ")

if choice =="y":
   print("gordon ramsay thinks pineapple doesnt belong on pizza, he is an impostor,you get murdered by his pizza cutter, game over, please run again")
   gameover()

if choice =="n":
   print("the centaur kills gordon with his own pizza cutter, he tells you gordon ramsay hates pineapple on pizza and that he was an impostor")

print("would you like to take the elevator or the stairs")

choice = input("e/s ")

if choice =="s":
    print("when you arrive at the 3rd floor the centaur needs a bathroom break, when hes finished he asks you to come in and check, something crazy has happened do you go in?")

if choice =="e":
    print("the elevator has broken and your inside, the centaur melee attacks you with his bow and you die, game over")
    gameover()

print ("do you go in")
choice = input("y/n ")


if choice =="y":
   print("a dead lynx is in the shower,the centaur says he has no arrows left to defend us, now it all makes sense, the centaur your defender is the last impostor, you kill the centaur with his own bow, his last words were, keep your friends close, but your enemys closer. you win. Congratulations.")

  
  

if choice =="n":
  print("You are dead. Survive next time. Please retry and win next time.")
  gameover()

