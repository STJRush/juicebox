from time import sleep
score = 0
def goblinfight1n1():
  print("The loot goblin swings its mace at you. It collides with you breaking all of your bones turning you to jellow, the last hear is it cackeling whilst saying 'I'm the victim here!' ")
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

