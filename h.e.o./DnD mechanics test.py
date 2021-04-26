#just the random libraries for this code
import random
import sys, time
from time import sleep

#the small line which chooses a random number between 1 and 10 to decide if you get an encounter
EnemyEncounter = random.randint(1, 10)


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
  for c in "rolling your damage....... you hit the enemy for ":
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(0.07)
  print
  
  #this was debug code but now it tells the user how much damage the player did
  print(random_number)

  #this is the code to decide if you did enough damage to eliminate the enemy
  if random_number >= random_minimum:
    print("You hit the enemy with enough force to eliminate him")
  else:
    print("you were to weak, go back to training")


#the code if you failed the chance encounter
def Nencounter():
 
  for c in "You did not encounter an enemy":
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(0.07)
  print


#the code if you succeded the chance enounter
def Yencounter():

  #code to appear as if you were typing
  for c in "You encountered an [Enemy] ":
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
 
