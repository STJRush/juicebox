from time import sleep


def Grave():
  print("You arrived at the grave yard where your mother lies in peace")

  if PickFlower == "yes":
    print("You cry for a bit and replace the flowers on her grave, you have done well")
  elif PickFlower == "no":
    print("You sadly watch the whilting dead flowers on your moms grave, you have no flower to replace it, shame on you, shame")

def FlowerGarden():
  print("Flowers lmao")
  sleep(1)
  print("Hey you found a pretty flower, do you want to pick it?")

  global PickFlower
  PickFlower = input("   ")
  
  if PickFlower == "yes":
    print("You picked a flower, poor organism")
  elif PickFlower == "no":
    print("Welp you didnt pick the flower")

  Grave()



print("Hey where you gonna go straight or are you gonna stay here")
MoveOne = input("  ")

if MoveOne =="straight":
  FlowerGarden()
else:
  print("You died get good scrub")
  sleep(0.5)
  exit()


