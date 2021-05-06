#i am trying to make a global thing to keep the score
keyList = []
global score
score = 0


#this is a function for the intro to my game
def intro():
    print("\033[0;37;40m Welcome to our game!!! \n")
    print(
        "You will go around an abandoned house and try not to die. If you die you have to start again. The aim of the game is to get out of the abandoned housea score of at least 20 points. If you die, you lose a point and you have to repeat. Have fun:)"
    )


from time import sleep


def start():
    pass
    #i started a loop

    while True:

        choice = input("type start to load ")
        if choice == "start":
            print("   _____     _______   ")
            sleep(1)
            print("  /      \  |      /\. ")
            sleep(1)
            print(" /_______/  |_____/  \.")
            sleep(1)
            print("|   \   /        /   / ")
            sleep(1)
            print(" \   \         \/   /  ")
            sleep(1)
            print("  \  /          \__/_  ")
            sleep(1)
            print("   \/ ____    /\.      ")
            sleep(1)
            print("     /  \    /  \.     ")
            sleep(1)
            print("    /\   \  /   /      ")
            sleep(1)
            print("      \   \/   /       ")
            sleep(1)
            print("       \___\__/        ")

            break

        else:
            print("start again")


#this is a function for a picture
def trees():
    print(
        "                                                                   .     "
    )
    print(
        "                                                        .         ;      "
    )
    print(
        "                           .              .              ;%     ;;       "
    )
    print(
        "                             ,           ,                :;%  %;        "
    )
    print(
        "                             :         ;                   :;%;'     .,  "
    )
    print(
        "                   ,.        %;     %;            ;        %;'    ,;     "
    )
    print(
        "                     ;       ;%;  %%;        ,     %;    ;%;    ,%'      "
    )
    print(
        "                      %;       %;%;      ,  ;       %;  ;%;   ,%;'       "
    )
    print(
        "                       ;%;      %;        ;%;        % ;%;  ,%;'         "
    )
    print(
        "                       `%;.     ;%;     %;'         `;%%;.%;'            "
    )
    print(
        "                         `:;%.    ;%%. %@;        %; ;@%;%'              "
    )
    print(
        "                            `:%;.  :;bd%;          %;@%;'                "
    )
    print(
        "                              `@%:.  :;%.         ;@@%;'                 "
    )
    print(
        "                                `@%.  `;@%.      ;@@%;                   "
    )
    print(
        "                                 `@%%. `@%%    ;@@%;                     "
    )
    print(
        "                                  ;@%. :@%%  %@@%;                       "
    )
    print(
        "                                    %@bd%%%bd%%:;                        "
    )
    print(
        "                                      #@%%%%%:;;                         "
    )
    print(
        "                                      %@@%%%::;                          "
    )
    print(
        "                                      %@@@%(o);  . '                     "
    )
    print(
        "                                      %@@@o%;:(.,'                       "
    )
    print(
        "                                  `.. %@@@o%::;                          "
    )
    print(
        "                                     `)@@@o%::;                          "
    )
    print(
        "                                      %@@(o)::;                          "
    )
    print(
        "                                     .%@@@@%::;                          "
    )
    print(
        "                                     ;%@@@@%::;.                         "
    )
    print(
        "                                    ;%@@@@%%:;;;.                        "
    )
    print(
        "                                ...;%@@@@@%%:;;;;,..                     "
    )


#this is a function for a picture
def house():
    print(
        "You're walking in the woods. The forest is thick with a variety of large trees.  The path is narrow and earthy. It's very dark, so dark that you can't see in front of you."
    )

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
 
def groundkey():
  from time import sleep
  import pygame
  pygame.init()

  gameDisplay = pygame.display.set_mode((500,350))

  keyImg = pygame.image.load('old ground key.jfif')

  gameDisplay.blit(keyImg, (0,0))
  pygame.display.update()
  sleep(2)
    
def key():
  global score
  while True:
        choice = input(
            "Do you want to pick up the key that you see on the ground? y/n? "
        )

        if choice == "y":
            print("You pick up the key, it is now in your possesion. ")
            keyList.append("Key")

            print(keyList)

            score = score + 5 
            break
            #i put break to stop the loop
            
        if choice == "n":
            print(" You decide to not pick up the key so you walk away from the house and keep going. You trip on a sprawled tree root and hit your head on a large rock.You suffer a fatal head injury.The ravens eat your lifeless body.You died.")
            print("\033[2;34;40m REPEAT \n")

            score = score - 2
                    
            start()
            

        else:
           
            first()



def first():
    global score
    #i started a loop
    while True:
        choice = input(
            "Do you want to use the key to go into the house? y/n? "
        )

        if choice == "y":
            print("You go through the front door.")

            score = score + 5
            break
            #i put break to stop the loop
            
        if choice == "n":
            print("You walk away from the house and keep going. You trip on a sprawled tree root and hit your head on a large rock.You suffer a fatal head injury.The ravens eat your lifeless body.You died.")
            print("\033[2;31;40m REPEAT \n")

            score = score - 2

            start()
            

        else:
           
            first()


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
        print(
            " Once you go in you see a long, ominous hallway containing two doors. "
        )

        doors()

        choice = input("Do you go through door 1 or 2?1/2   ")

        if choice == "2":
            print(
                "You walk into a dusty, old fashioned living room.It's dead silent and you can hear your footsteps on the musty carpet.You see an old looking TV in front of you and a glass door leading to the backgarden."
            )
            score = score + 5
            break

        if choice == "1":
            print(
                "You go through the strangely carved mahogany door.You step in a room with a wet floor and cut electrical wires everywhere.You are electricuted to death.")
            print("\033[2;32;40m REPEAT \n")
            score = score - 2

            start()

        else:
            print("pick a door 1 or 2")
            doorsone()

            
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
    global score

    #i started a loop
    while True:
        tv()

        choice = input(
            "Do you go to the backgarden or switch on the TV? Backgarden/TV ")

        if choice == "backgarden":
            print(
                "You open the glass door and step out onto the chilled patio. You are confronted with two options."
            )

            score = score + 5
            break
            #i put break to stop the loop

        if choice == "TV" or "tv":
            print(
                "You switch on the TV and static pops up on the screen. After five seconds of just static, the screen turns black.A little girl appears on the screen and stares at you.She starts running at you and comes through the screen.She grabs you and pulls you into the TV.She proceeds to rip out your intestines and eat you.You died."
            )
            print("\033[2;33;40m REPEAT \n")

            score = score - 2
            start()

        else:
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
    global score
    #i started a loop
    while True:
        print("")

        shed()

        choice = input(
            "You can either go on the grass or into the shed.Which do you choose? Grass/Shed"
        )

        if choice == "shed":
            print(
                "You walk into the wooden shed and see shelves piled with gardening tools and building tools.There are cobwebs in every corner and everything is laced in dust.You realise there's nothing here and retreat back inside"
            )

            score = score + 5
            break
            #i put break to stop the loop

        if choice == "grass":
            print(
                " You step onto the dewy grass and immediately get stung by a bee. You're allergic to bee stings and your body starts puffing up. Your throat slowly closes up, causing you to slowly and painfully suffocate to death.You died. "
            )
            print("\033[2;36;40m REPEAT \n")
            
            score = score - 2
            start()

        else:
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
    global score
    #i started a loop
    while True:
        print(
            "You go back inside but the room has changed. Now, you have a choice to either go upstairs or to the kitchen."
        )

        knife()

        choice = input("Where will you go?Upstairs/Kitchen")

        if choice == "upstairs":
            print("you go upstairs and see 4 doors, you try each one of them but all of them are locked except for one, you open the ony unlocked door to find...")
            
            score = score + 5
            break
            #i put break to stop the loop
            

        if choice == "kitchen":
            print("You walk into a dingy kitchen and immediately trip over a misplaced stool. You fall and hit your head on the hard floor. Your head starts gushing blood and you bleed to death.")
            print("\033[2;34;40m REPEAT \n")

            score = score - 2
            start()

        else:
            kitchen()


def finalscore():
    print("\033[2;33;40m YOU FINISHED!!!!!!!1 \n")
    print("Your final score is...", score)


intro()

start()

trees()

house()

groundkey()

key()

first()

doorsone()

livingroom()

shedtwo()

kitchen()

finalscore()
