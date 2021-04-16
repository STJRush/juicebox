what eve u want

    print ("You are being chased by a mysterious figure and you come across a creepy looking house")

    def outside():

      choice = input ("Would you like to go into it to? - y/n?")

      if choice == "y":
        print("You enter the house and the house looks like no one has lived there for years")
        lobby() 

      else:
        print("The mysterious figure cathces up and you died... game over!")


    def lobby():

      choice = input ("In the lobby you see a door to your left and to your right, which one will you choose - l/r?")

      if choice == "l":
        print("You go left and enter the kitchen")
        kitchen()

      elif choice == "r":
        print("You go right and enter the living room")
        living()

      else:
        print("The mysterious figure cathces up and you died... game over!")


    def kitchen():
      choice = input ("In the kitchen you see a stairs going up and a stairs going down, which way do you want to go? - u/d?")

      if choice == "d":

        print("You go down the stairs into a basement")
        basement()

      elif choice == "u":
        print("You go up the stairs and see a very long hallway")
        upstairs()

      else:
        print("The mysterious figure cathces up and you died... game over!")


    def upstairs():

      choice = input("You see 3 doors, which one wil you do you want to open? - 1/2/3")

      if choice == "1":
        print("You walk into a bedroom and see a ghost, it comes up to you and you died... game over!")

      elif choice == "2":
        print("You go into a bedroom and see another door")
        two()

      elif choice == "3":
        print("The door is locked and won't open")
        three()

      else:
        print("The mysterious figure cathces up and you died... game over!")


    def two():

      choice = input("Would you like to open the door? - y/n")

      if choice == "y":
        print("You open it and fall down stairs")
        basement()

      else:
        print("The mysterious figure cathces up and you died... game over!")


    def three():

      choice = input("Do you want to try and kick the door open or go into a different door? - k/d")

      if choice == "k":
        print("You kick it hard and it opens")
        kick()

      elif choice == "d":
        upstairs()

      else:
        print("The mysterious figure cathces up and you died... game over!")


    def kick():

      while True:

        choice = input("You see another door but it's also locked. Do you want to try to kick it open or go back to the other doors? - k/d")

        if choice == "d":
          upstairs()


    def living():

      while True:

        choice = input ("There is nothing interesting in the living room, will you stay or leave - s/l?")

        if choice == "s":
          print("The mysterious figure cathces up and you died... game over!")
          break

        elif choice == "l":
          print("In the lobby you see a door to your left and to your right, which one will you choose - l/r?")
          break

        else:
          print("The mysterious figure cathces up and you died... game over!")


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
        print("The mysterious figure cathces up and you died... game over!")


    def close():
      choice = input ("Do you want to take a closer look or go out the window - c/w?")

      if choice == "c":
        print("You take a closer look and you find out their zombies!")
        zombies()

      elif choice == "w":
        print("You hop onto a table and get out of the window into the garden")
        garden()

      else:
        print("The mysterious figure cathces up and you died... game over!")


    def zombies():
      print("The zombies didn't like you not social distancing so they killed you... game over!")



    def garden():
      print("In the garden you see a lake and the a driveway leading a different way out")

      choice = input ("Which do you want to go to - l/d?")

      if choice == "l":
        print("When you walk up to the lake it feels cold and eerie and someone from behind pushes you into it. You drowned... game over! ")

      if choice == "d":
        print("You made it out of the house alive. You won!")

      else:
        print("The mysterious figure cathces up and you died... game over!")


    outside()
