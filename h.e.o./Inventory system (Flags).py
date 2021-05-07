#The imports
from time import sleep

#the second section and the end of game
def Grave():

  #this just gives some backstory
  print("You arrived at the grave yard where your mother lies in peace")

  #this checks your input from the FlowerGarden function
  if PickFlower == "yes":
    
    #this just tells you that you won
    print("You cry for a bit and replace the flowers on her grave, you have done well")

    #if in the other area you said no this code will run
  elif PickFlower == "no":

    #shame on you, this part tells you that you lost because you didnt pick the flower
    print("You sadly watch the whilting dead flowers on your moms grave, you have no flower to replace it, shame on you, shame")

#this is the first section where it adds the item or flag
def FlowerGarden():

  #some random backstory
  print("Flowers lmao")
  sleep(1)
  print("Hey you found a pretty flower, do you want to pick it?")

  #this makes the variable work outside of the fuction
  global PickFlower
  PickFlower = input("   ")
  
  #this just tells you something based on your response
  if PickFlower == "yes":
    print("You picked a flower, poor organism")
  elif PickFlower == "no":
    print("Welp you didnt pick the flower")

  sleep(1)

  #this tells the code to run the other section
  Grave()


#this is the very start of the game and gives you to choices
print("Hey where you gonna go straight or are you gonna stay here")

#you input the choices here
MoveOne = input("  ")

#if you chose straight it runs the FlowerGarden function
if MoveOne =="straight":
  FlowerGarden()

  #if you chose anything else this code will run
else:

  #this just tells you that you died
  print("You died get good scrub")
  sleep(0.5)

  #this just ends the code if you run anything else
  exit()
