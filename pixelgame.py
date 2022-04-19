#imports
import pygame

import sys
import random
from tkinter import filedialog #skriv vad detta gör sen
from tkinter import * #skriv vad detta gör sen
from pygame.locals import * #skriv vad detta gör sen
            
#to get everything started #bryter mot standard(?!)
pygame.init() 
pygame.mixer.init()

                                    
#global variables



#idk where these should be
BOTTOM_PANEL = 150
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400 + BOTTOM_PANEL
ACCELREATION = 0.3 #hittade detta specifika nummer online
FRICTION = -0.10 #hittade detta specifika nummer online
COUNT = 0
FPS = 60
CLOCK = pygame.time.Clock()

#pygame setup (inte säker på var detta ska ligga i koden enligt pep-8 standarden)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #800x550 upplösning
pygame.display.set_caption("Endless Regressor")   
icon = pygame.image.load("img/GameObjects/icon.png")      
pygame.display.set_icon(icon)
maintheme = pygame.mixer.music.load("music/Soundstracks/maintheme.mp3")
                                                           

#Klasser
class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() #super gör att andra klasser smidigare får tillgång till "main-klassen" men nu har jag inte lagt till något än.
        self.bgimage = pygame.image.load("img/Backgrounds/background_boss.png")
        self.bgY = 0
        self.bgX = 0

    def draw_bg1(self):
        screen.blit(self.bgimage, (self.bgX, self.bgY))




class Groundlevel(pygame.sprite.Sprite):
    def __init__(self):             
        super().__init__()
        self.image = pygame.image.load("img/GameObjects/lunarground.png")                                     
        self.rect = self.image.get_rect(center = (350, 350))  #rect skapar en plats för bilden man vill ha                       
                
    def draw_gnd(self):             
        screen.blit(self.image, (0, 475))                         
                    

class User(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/Player1/Playersprite.png")
        self.rect = self.image.get_rect()
        self.position = pygame.math.Vector2((340, 240)) #pygame.math.vector2 är en 2D vektor som vi kan använda för att göra så att spriten rör sig.                            
        self.velocity = pygame.math.Vector2(0, 0) #rakt                                                                                                 
        self.accelration = pygame.math.Vector2(0, 0)
        self.direction = "RIGHT"
         
    def movement(self):
         pass

    def update(self):
        pass

    def attack(self):
        pass

    def jump(self):
        pass            


    def move(self):
        pass

    def cameralock(self):
        if self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        if self.position.x < SCREEN_WIDTH:
            self.position.x = 0
        if self.position.y > SCREEN_HEIGHT: #kommer jag att göra gravitation potions lol?
            self.position.y = 0 
        if self.position.y < SCREEN_HEIGHT: #idk
            self.position.y = 0


class Mob1(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__()


#bryter most standard(?)
bg = Background()
gnd = Groundlevel()           
usr = User()

#game loop
while True:
      #drawing/rendering images/stuff
    bg.draw_bg1()
    gnd.draw_gnd()
    screen.blit(usr.image, usr.rect)
  
    
    CLOCK.tick(FPS)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
              pass #placeholder

            if event.type == pygame.KEYDOWN:
              pass 


    pygame.display.flip()
    pygame.display.update()
