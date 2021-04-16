from time import sleep

def jail_cell():

  while True:

    print("escape from jail.")
    sleep(2)
    print("you can only go one way. you cannot go back.")
    sleep(4)
    print("so choose wisely.")
    sleep(2)
    print("succeed or you die.")
    sleep(4)
    print(" ")
    jail_cell_ = input("You're at the door, what do your do? f(forward), b(you stay in jail.)")

    if jail_cell_ == "f":
      print("you notice your cell dor is not locked properly. you pick it with hair clips you got for youtr inmate.")
      corridor()
      break

    elif jail_cell_ == "b":
      print("you stay behind bars. unable to do anything or see anyone.")
      gameover()
      break

    else:
      print("you cant go there.")

def gameover():
  print("you die of depression.")


def corridor():

  while True:

    choice1 = input("You're in the corridor, what do your do? r(go right), l(go left)")

    if choice1 == "r":
      print("you walk right. you see the cafiteria in the distance")
      #cafeteria()
      break


    elif choice1 == "l":
      print("you walk left. you arrive at the gym")
      #gym()
      break


    else:
      print("you cannot go there")

jail_cell()
