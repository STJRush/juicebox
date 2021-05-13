#starts pygame
from time import sleep
import pygame
pygame.init()

#sets the window size
gameDisplay = pygame.display.set_mode((400,300))


#loads in your pics to use later
locationmarker = pygame.image.load('google-pin-icon-12.png')
jailmap = pygame.image.load('jail_concept4.png')

def printlocation(x,y):
  gameDisplay.blit(jailmap, (0,0))
  pygame.display.update()
  gameDisplay.blit(locationmarker, (x,y))
  pygame.display.update()
  sleep(2)

gameDisplay.blit(jailmap, (0,0))
pygame.display.update()



#DISPLAY GARY
gameDisplay.blit(locationmarker, (180,250))
pygame.display.update()
sleep(2)

printlocation(180, 100)

sleep(2)

gameDisplay.blit(jailmap, (0,0))
pygame.display.update()


gameDisplay.blit(locationmarker, (180,200))
pygame.display.update()
sleep(2)


pygame.quit()
quit()
