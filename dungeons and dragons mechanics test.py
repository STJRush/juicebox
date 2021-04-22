import random
import sys, time
from time import sleep

random_number = random.randint(1, 10)
random_minimum = random.randint(2, 9)


for c in "This enemies health is ":
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.07)
print

print(random_minimum)

sleep(2)

for c in "rolling your damage....... you hit the enemy for ":
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.07)
print

print(random_number)


if random_number >= random_minimum:
  print("You hit the enemy with enough force to eliminate him")
else:
  print("you were to weak, go back to training")

