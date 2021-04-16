


# OUTSIDE ROOM
def outside():

  while True:

    print("THR DOOOOOOOOORRR....")

    choice1 = input("You're at the door, what do your do? f(forward), b(run away like a chicken person)")

    if choice1 == "f":
      print("You step boldly through the creeeeeeeeky door")
      break
      #lobby()

    elif choice1 == "b":
      print("You run away like a silly chicken")
      break
      #gameover()

    else:
      print("Print, NOT AN OPTION DUDE OR DUDETTE")

# LOBBY ROOM
def lobby():

  while True:

    print("THR LOBBBYY....")
    print("THE DOOR LOCKS!!!")

    choice1 = input("You see a door (l)eft and (r)ight, what do your do")

    if choice1 == "l":
      print("You go left")
      break
      #sittingRoom()

    elif choice1 == "r":
      print("You go thorugh the right door")
      break
      #kitchen()

    else:
      print("Print, NOT AN OPTION DUDE OR DUDETTE")




#GAME STARTS HERE

outside()
