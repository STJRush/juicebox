name = str(input("Please enter your name.\n> "))
age = int(input("Please enter your age.\n> "))
while True:
    val = float(input("Please enter a value between 7 and 100 with two decimal places.\n> "))
    val = round(val, 2)
    if val <= 7 or val >= 100:
        print("Improper input.")
    else:
        break
print("Hello,",name, end = ', ')
if age < 21:
    print("you can't legally drink yet!", end = ' ')
elif age >= 21 and age < 50:
    print("you are in the prime of your life!", end = ' ')
else:
    print("you're getting kinda old!", end = ' ')
print("If you had",'$'+str(val),"you could buy",str(int(val // 1)),"items at a dollar store!")

#Program 2
week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
while True:
    day = int(input("Please enter a value from 1 to 7.\n> "))
    if day >= 1 and day <= 7:
        break
    else:
        print("Incorrect Input!")
day -= 1
print(week[day])

#Program 3
print("You are playing blackjack")
from random import randint
pc1 = randint(1,10)
pc2 = randint(1,10)
cc1 = randint(1,10)
cc2 = randint(1,10)
print("Your cards are",str(pc1),"and",str(pc2)+'.',"The computer's cards are",str(cc1),"and",str(cc2)+'.')
if (pc1 + pc2) > (cc1 + cc2):
    print("Congrats! You win!")
elif (pc1 + pc2) < (cc1 + cc2):
    print("You lose!")
else:
    print("Tie!")

#Program 4
while True:
    number = int(input("Please enter an integer greater than 0.\n> "))
    if number > 0:
        break
    else:
        print("Incorrect input!")
count = 0
while count <= number:
    print(count)
    count+=1
    
#Program 5
nums = []
count = 0
for i in range(10):
    nums.append(randint(1,50))
#print(nums)
while True:
  guess = int(input("Please enter a guess for one of the 10 integers the computer has generated between 1 and 50.\n> "))
  if guess >= 1 and guess <= 50:
    break
  else:
    print("Please enter a number between 1 and 50")
z = 0
for i in nums:
  if i == guess:
    print("The number has shown up!")
    z = 1
    break
if z == 0:
  print("Wrong guess!")
  
#Program 6
from random import randint
count = 1
print("This game has you roll dice until you get a 7 or an 11!")
while True:
  d1 = randint(1,6)
  d2 = randint(1,6)
  print("You rolled a",str(d1),"and",str(d2))
  if (d1+d2) == 7 or (d1+d2) == 11:
    print("You win! It only took",count,'roll(s)!')
    break
  else:
    print("You did not roll 7 or 11.")
    go = str(input("Hit enter to roll again, enter any input to quit the program.\n"))
    if go != '':
      print("Quitter!")
      break
  count += 1

