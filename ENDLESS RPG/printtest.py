import pygame
import random

pygame.init()
black=(0,0,0)
screen = pygame.display.set_mode((800,600))
screen.fill((255,255,255))

#Dice random number generation
diceRoll = random.randrange(0, 5)

#Text through GUI
myFont = pygame.font.SysFont("Times New Roman", 18)

randNumLabel = myFont.render("You have rolled:", 1, black)
### pass a string to myFont.render
diceDisplay = myFont.render(str(diceRoll), 1, black)

screen.blit(randNumLabel, (520, 20))
screen.blit(diceDisplay, (520, 30))

### main loop
run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    pygame.display.flip()