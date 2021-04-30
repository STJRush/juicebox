Haunted House Game: Summer Assessment 2021

#jd
this is the start of our haunted house game.
the players starts in the firtst room which is the front lawn outside the haunted house

#GAME STARTS HERE

# OUTSIDE ROOM
def outside():

  while True:

    print("You are standing on the lawn of the haunted house, and slowly proceed to make your way up to the front door.")

    choice1 = input("You're now at the front door, what do your do? f(go forward and enter the house), b(run far away and never go near the haunted house again)")

    if choice1 == "f":
      print("You push open the creeky door and wearily make your way into the haunted house")
      break
      #lobby()

    elif choice1 == "b":
      print("You run far away and never ever comeback!!")
      break
      #gameover()

    else:
      print("THAT IS NOT AN OPTION!")



this is the second room of our haunted house
it is the hallway through the front door if the user choses to go through the front door of the haunted house

# HALLWAY ROOM
def lobby():

  while True:

    print("YOU ARE NOW IN THE HALLWAY")
    print("THE FRONT DOOR SUDDENLY SLAMS SHUT AND LOCKS BEHIND YOU!!!")

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
      print("THAT IS NOT AN OPTION!")
      
Today I added a score keeper to our haunted house game.

#This is a score keeper to keep track of the points the playe earns during the game.
#Players earn points for making the correct decisions.

global score 
score = 0





Today I added two new rooms to our game.

# sittingRoom()
def sittingRoom():

    while True:


      print("You are now currently standing in the sitting room and see a locked door in the corner. Do you want to investigate it???")

      choice3 = input("Will you investigate the locked door (y)es or (n)o")
      
    if choice3 == "y":
      print("You go and investigate the locked door")
      break
      
        global score
      score = score + 5
      
      elif choice3 == "n":
      print("A demonic monster runs out of the kitchen and chases you out of the haunted house. GAME OVER!")
      break
      

    else:
      print("THAT IS NOT AN OPTION!!")

      # LockedDoor()
def LockedDoor():

    while True:


       print("As you are curiosly invstigating the locked door you notice the glint of a key out of the corner of your eye")

       choice4 = input("Do you dare to dash across the dark, scary room and get the key, (y)es or (n)o??")

       if choice4 == "y":
       print("You dash across the room, when suddnely the floor begins to collapse beneathe your feet, fortuneatley you are quick enough and make it back to the locked door with the key.")
       break
      
        global score
        score = score + 5
      
        elif choice4 == "n":
        print("You end up standing in the same place for too long and the floor begins to crumble beneath your feet and you fall into a bottomless pit. GAME OVER!")
       break
      

        else:
        print("THAT IS NOT AN OPTION!!")

      
      
      ERRORS
      
      A LOT OF THE ABOVE CODE DID NOT WORK DUE TO SYNTAX ERRORS AND INDENTATION ERRORS WHEN I TESTED IT.
      
    due to the high frequency of errors within our code i retyped a whole new code for the game that fully works as i have frequently tested the code 
    and proof chekced it for errors. It now fully work and we have got a solid foundation for our game.
    
    
    
    #This is a score keeper to keep track of the points the playe earns during the game
#Players earn points for making the correct decisions

global score 
score = 0



#function for the intro of the game
def intro():
  print("Hello and welcome to our haunted house game. It will now be your job to try and make it through our haunted house..... alive. Goodluck..... you'll need it. ")




#GAME STARTS HERE

#function for the begining of the game 
def start():
  pass
  #start of loop
  
  while True:
    
    
    choice =input("Type yes, to walk up to the front door of the haunted house and begin the game ")
    if choice =="yes":
      print("The game will now begin and you will enter the haunted house")

      
      break
    

    else:
      print("You run far away from the house never to be seen again. GAME OVER!!!")
    

def frontDoor():
  global score
  #start of loop
  while True :
    choice = input("Do you want to push open the front door and enter the haunted house, yes or no? ")

    if choice =="yes":
      print("you are pushing open the front door now and you take a step inside of the haunted house")
      global score
      score = score + 5
      break
      #break out of loop

    else:
      print("Your nerves got the better of you and you walk ome crying. GAME OVER!!!")
      score = score + 0
      frontDoor()


def hallway():
 global score
  #start of loop
 while True:
    print("As your standing in the hallway you step forward and see two doors, one on the left and one on the right, which one do you want to go and investigate, type left or right.")
        

    choice = input("do you want to go through the left door or the right door, type left or right")

    if choice =="right":
      print("you enter the kitchen, and a demonic monster sneaks up behind you and kills you. GAME OVER!!!")
      score = score + 0
      frontDoor()

    if choice =="left" :
      print("you are now in the sitting room ")
      score = score + 5
      break
      #break out of loop


    else :
      print("pick a door, left or right")
      hallway()

def sittingRoom():
  global score

  #start of loop
  while True:

    choice = input("While you are standing in the sitting room you notice a hidden door in the corner, do you wish to investigate this hidden door, yes or no ")

    if choice =="yes":
      print("you approach the hidden door and begin to investigate it ")
      global score
      score = score + 5
      break
      #break out of loop

    if choice =="no":
      print("you end up standing in the same spot for too long and the ground collapses beneath your feet as you fall down the bottomless pit beneath the haunted house. GAME OVER!!!")
      score = score + 0
      frontDoor()
    
    else :
      sittingRoom()

def HiddenRoom():
  #start of loop
 while True:
   print("you seem a key on the other side of the room do you run over and grab the key")


   choice = input("yes or no ")

   if choice =="yes":
      print("you grab the key and sprint back across the room to begin unlocking the door")
      global score
      score = score + 5
      break
      #i put break to stop the loop

   if choice =="no":
    print("while standing besdie the hidden door, a demon smashes through the wall and eats you. GAME OVER!!!")
    score = score + 0
    start()

   else :
    HiddenRoom()

def attic():
#start of loop
  while True:
    print("the locked door reveals a hidden passage into the old abandoned attic ")


    choice = input("do you want to go through the secret passage to the attic, type yes or no? ")

    if choice =="yes":
        print("you go up the secret passage way to the abandoned attic")
        global score
        score = score + 5
        attic2()
        break
        #break out of loop
    

    if choice =="no" :
        print("the hidden passage way slowly gets smaller until it completely engulfs you. GAME OVER!!!")
        score = score + 0
        start()

    else :
      attic()

def attic2():
#start of loop
  while True:
    print("you are now currently stading in the attic and see the demonic final boss, who owns and lives in the haunted house ")


    choice = input("the final boss has not yet seen you do you wish to pick up the conviniently placed sword on the ground and strike him from behind before he notices you? type yes or no ")

    if choice =="yes":
        print("you strike and kill the final boss before he has any time to react. CONGRATULATION you have survived and completed our game")
        global score
        score = score + 5
        endscore() 
        break
        #break out of loop
    

    if choice =="no" :
        print("tough luck the final boss turned around and was in no mood to be your friend, so he strikes and kills you instantly. GAME OVER!!!")
        score = score + 0
        start()

    else :
      attic2()

def endscore():

  while True:
     print("You finished with a score of", score)
     break

intro()

start()

frontDoor()

hallway()

sittingRoom()

HiddenRoom()

attic()

attic2

This is the brand new working code for our game that i have spent the past 3 classes and some time at home on my laptop retyping and copying partial 
blocks from my old Repls from when we completed this coding project during lockdown.
We can now begin to try and add more advanced features to our game such as soundtracks and images.
