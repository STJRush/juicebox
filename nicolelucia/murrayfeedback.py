#i am trying to make a global thing to keep the score
from time import sleep
global score 
score = 0


#this is a function for the intro to my game
def intro():
    print("Welcome to our game, you will go around an abandoned house and try not to die. If you die you have to start again. The aim of the game is to get out of the abandoned house with at least 20 points. If you die, you have to start again. Have fun:)")
    start()
    
def start():
  #i started a loop
  
  while True:
    
    
    choice =input("type start to play ")
    if choice =="start":
      print("   _____     _______   ")
      sleep(0.2)
      print("  /      \  |      /\. ")
      sleep(0.2)
      print(" /_______/  |_____/  \.")
      sleep(0.2)   
      print("|   \   /        /   / ")
      sleep(0.2)
      print(" \   \         \/   /  ")
      sleep(0.2)
      print("  \  /          \__/_  ")
      sleep(0.2)
      print("   \/ ____    /\.      ")
      sleep(0.2)
      print("     /  \    /  \.     ")
      sleep(0.2)
      print("    /\   \  /   /      ")
      sleep(0.2)
      print("      \   \/   /       ")
      sleep(0.2)
      print("       \___\__/        ")
      
      break
    

    else:
      print("start again")
      
  trees()
      
#this is a function for a picture
def trees():
  print("                                                                   .     ")
  print("                                                        .         ;      ")
  print("                           .              .              ;%     ;;       ")
  print("                             ,           ,                :;%  %;        ")
  print("                             :         ;                   :;%;'     .,  ")
  print("                   ,.        %;     %;            ;        %;'    ,;     ")
  print("                     ;       ;%;  %%;        ,     %;    ;%;    ,%'      ")
  print("                      %;       %;%;      ,  ;       %;  ;%;   ,%;'       ")
  print("                       ;%;      %;        ;%;        % ;%;  ,%;'         ")
  print("                       `%;.     ;%;     %;'         `;%%;.%;'            ")
  print("                         `:;%.    ;%%. %@;        %; ;@%;%'              ")
  print("                            `:%;.  :;bd%;          %;@%;'                ")
  print("                              `@%:.  :;%.         ;@@%;'                 ")
  print("                                `@%.  `;@%.      ;@@%;                   ")
  print("                                 `@%%. `@%%    ;@@%;                     ")
  print("                                  ;@%. :@%%  %@@%;                       ")
  print("                                    %@bd%%%bd%%:;                        ")
  print("                                      #@%%%%%:;;                         ")
  print("                                      %@@%%%::;                          ")
  print("                                      %@@@%(o);  . '                     ")
  print("                                      %@@@o%;:(.,'                       ")
  print("                                  `.. %@@@o%::;                          ")
  print("                                     `)@@@o%::;                          ")
  print("                                      %@@(o)::;                          ")
  print("                                     .%@@@@%::;                          ")
  print("                                     ;%@@@@%::;.                         ")
  print("                                    ;%@@@@%%:;;;.                        ")
  print("                                ...;%@@@@@%%:;;;;,..                     ")
  sleep(1)
  house()
  
  
#this is a function for a picture
def house():
  print("You're walking in the woods. The forest is thick with a variety of large trees.  The path is narrow and earthy. It's very dark, so dark that you can't see in front of you.")

  print("                   (          /^\                    ")
  print("                     )       //^\\                   ")
  print("                  (         //   \\                  ")
  print("                    )      //     \\                 ")
  print("                   __     //       \\                ")
  print("                  |=^|   //    _    \\               ")
  print("                __|= |__//    (+)    \\              ")
  print("               /LLLLLLL//      ~      \\             ")
  print("              /LLLLLLL//               \\            ")
  print("             /LLLLLLL//                 \\           ")
  print("            /LLLLLLL//  |~[|]~| |~[|]~|  \\          ")
  print("           ^| [|] //   | [|] | | [|] |   \\          ")
  print("            | [|] ^|   |_[|]_| |_[|]_|   |^          ")
  print("         ___|______|                     |           ")
  print("        /LLLLLLLLLL|_____________________|           ")
  print("       /LLLLLLLLLLL/LLLLLLLLLLLLLLLLLLLLLL\          ")
  print("      /LLLLLLLLLLL/LLLLLLLLLLLLLLLLLLLLLLLL\         ")
  print("      ^||^^^^^^^^/LLLLLLLLLLLLLLLLLLLLLLLLLL\        ")
  print("      || |~[|]~|^^||^^^^^^^^^^||^|~[|]~|^||^^        ")
  print("      || | [|] |  ||  |~~~~|  || | [|] | ||          ")
  print("      || |_[|]_|  ||  | [] |  || |_[|]_| ||          ")
  print("      ||__________||  |   o|  ||_________||          ")
  print("    .'||][][][][][||  | [] |  ||[][][][][||.'.       ")
  print("   . '||[][][][][]||_-`---- -_||][][][][]|| .")

  print("  .(')^(.)(').( )'^@/-- -- - --\@( )'( ).(( )^(.)^   ")
  print(" '( )^(`)'.(').( )@/-- -- - -- -\@ (.)'(.),( ).(').  ")
  print(" '.'.'.'' .'' '.'. @/- - --- -- - -\@ '.'.'.'.'.'.'.''  ")
  print(" '. '' '.'.'.'.'@/ - -- -- -- -- -\@'.'..''.'.'.'.' ")
  print("'.'.'.''.'.''.'@/ -- --- --- -- - -\@.'.''.'.''.'.''.")
  sleep(1)
  first()
        
def first():
   
   #i started a loop
   while True:
    choice = input("You come across a big, seemingly abandoned house.Do you want to go in? Y/N? ")

    if choice =="y":
      print("You go through the front door.")
      global score
      score = score + 5
      doorsone()
      #i put break to stop the loop

    else:
      print("You walk away from the house and keep going. You trip on a sprawled tree root and hit your head on a large rock.You suffer a fatal head injury.The ravens eat your lifeless body.You died.START AGAIN.")
      score = score + 0
      start()
      
    
        
#this is a function for a picture
def doors():
  print("  __ __   __ __      ")
  print(" |  |  | |  |  |     ")
  print(" | -|- | | -|- |     ")
  print(" |__|__| |__|__|     ")
    
def doorsone():
   global score
  #i started a loop
   while True:
    print(" Once you go in you see a long, ominous hallway containing two doors. ")
        
    doors()

    choice = input("Do you go through door 1 or 2?1/2   ")

    if choice =="1":
      print("You go through the strangely carved mahogany door.You step in a room with a wet floor and cut electrical wires everywhere.You are electricuted to death.START AGAIN.")
      score = score + 0
      start()

    if choice =="2" :
      print("You walk into a dusty, old fashioned living room.It's dead silent and you can hear your footsteps on the musty carpet.You see an old looking TV in front of you and a glass door leading to the backgarden.")
   
    else :
      print("pick a door 1 or 2")
      doorsone()
        
      score = score + 5
      break
      #i put break to stop the loop
  
#this is a function for a picture
def tv():
  print("     O        O      ")
  print("     .\\     //      ")
  print("     . \\   //       ")
  print("     .  \\ //        ")
  print("       /~~~~~\.      ")
  print(",-------------------,")
  print("| ,---------------, |")
  print("| |               | |")
  print("| |               | |")
  print("| |               | |")
  print("| |               | |")
  print("| |_______________| |")
  print("|___________________|")
  print("|___________________|")
            
def livingroom():

  #i started a loop
  while True:
    tv()

    choice = input("Do you go to the backgarden or switch on the TV? Backgarden/TV ")

    if choice =="backgarden":
      print("You open the glass door and step out onto the chilled patio. You are confronted with two options.")
      
      score = score + 5
      break
      #i put break to stop the loop

    if choice =="TV" or "tv" :
      print("You switch on the TV and static pops up on the screen. After five seconds of just static, the screen turns black.A little girl appears on the screen and stares at you.She starts running at you and comes through the screen.She grabs you and pulls you into the TV.She proceeds to rip out your intestines and eat you.You died.START AGAIN.")
      
      
      score = score + 0
      start()
        
    else :
      livingroom()
  
#this is a function for a picture
def shed():
  print("          _          ") 
  print("       _-'_'-_       ")    
  print("    _-' _____ '-_    ")
  print(" _-' ___________ '-_ ")
  print("  |___|||||||||___|  ")
  print("  |___|||||||||___|  ")
  print("  |___|||||||o|___|  ")
  print("  |___|||||||||___|  ")
  print("  |___|||||||||___|  ")
  print("  |___|||||||||___|  ")
            
def shedtwo():
  #i started a loop
 while True:
   print("")

   shed()

   choice = input("You can either go on the grass or into the shed.Which do you choose? Grass/Shed")

   if choice =="shed":
      print("You walk into the wooden shed and see shelves piled with gardening tools and building tools.There are cobwebs in every corner and everything is laced in dust.You realise there's nothing here and retreat back inside")
      global score
      score = score + 5
      break
      #i put break to stop the loop

   if choice =="grass":
    print(" You step onto the dewy grass and immediately get stung by a bee. You're allergic to bee stings and your body starts puffing up. Your throat slowly closes up, causing you to slowly and painfully suffocate to death.You died. START AGAIN.")
    
    score = score + 0
    start()

   else :
    shedtwo()
  
#this is a function for a picture
def knife():
  print("        / )          ")  
  print("  |||| / /           ") 
  print("  ||||/ /            ")                        
  print("  \__(_/             ")                  
  print("   ||//              ")                  
  print("   ||/               ")                       
  print("   ||                ")
  print("  (||                ")
        
def kitchen():
#i started a loop
  while True:
    print("You go back inside but the room has changed. Now, you have a choice to either go upstairs or to the kitchen.")

    knife()

    choice = input("Where will you go?Upstairs/Kitchen")

    if choice =="upstairs":
        print("you go upstairs and see 4 doors")
        global score
        score = score + 5
        break
        #i put break to stop the loop
        doors()
        doors()

    if choice =="kitchen" :
        print("you fell over and have to start again")
        
        score = score + 0
        start()

    else :
      kitchen()
      
def upstairs():
  global score
  #i started a loop
  while True:
    print("You walk up the creaky stairs and are faced with 4 doors.")

    doors()
    doors()

    choice = input(" Which will you choose?1/2/3/4")

    if choice =="3":
        print("You go through door three and walk into a pitch black room with a spotlight on a cloth covered table.You walk up to the table and a glass casing appears. In it, are three diamonds.You open the casing and gently take them in your hand.You get transported back home suddenly.")
        
        score = score + 5
        break
        #i put break to stop the loop
        doors()
        doors()

    if choice =="2" :
        print("You walk through door two and get immediately transported back to the beginning of the forest trail. You can't seem to remember what just happened or why you came to the forest.You brush it off and turn around, back home. start again?")
        
        score = score + 0
        start()
        
    if choice =="1" :
        print("You go through door one and immediately drop dead from toxic fumes.START AGAIN.")
        
        score = score + 0
        start()
        
    if choice =="4" :
        print("You walk through the fourth door and get stabbed by the house owner. You get the police called on you and go to prison for breaking and entering.Your wound gets infected in prison and you die.START AGAIN.")
        
        score = score + 0
        start()
        
    else :
      upstairs()

  

def finalscore():
  print("Your final score is..." , score)

intro()
"""
start()

trees()

house()

first()

doorsone()

livingroom()

shedtwo()

kitchen()


 
upstairs()



finalscore()
"""



