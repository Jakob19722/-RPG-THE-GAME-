#imports
import pygame
import random 
import sys
import button
import time

pygame.init()

#classes


#en metod jag hittade online för att skapa olika scener, basically lägger du in hela pygame run event i en class och sen kallar på den delen du vill ha, t.ex "intro".
class GameState():
    def __init__(self):
        self.state = "intro"     

    def intro(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                sys.exit
            if event.type == pygame.MOUSEBUTTONDOWN:
                time.sleep(0.2)
                self.state = "main_game"

        # draw pngs                     
        draw_intro()
        draw_logo()
        pygame.display.flip()
                
                  


    def main_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                sys.exit
        
        #draw pngs
        draw_bg1()
        pygame.display.flip()



    #what scene is gonna run
    def state_manager(self):
        if self.state == "intro":
            self.intro()
        if self.state == "main_game":
            self.main_game()
        
            
                         









#setup for pygame and general stuff         

#fönster 800x550
bottom_panel = 150
screen_width = 800
screen_height = 400 + bottom_panel

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PixelLegend")

clock = pygame.time.Clock()
game_state = GameState()      
fps = 60

#convert_alpha ändrar png'n med det upplösningen man vill ha så det blir bra.

intro_img = pygame.image.load("Public/Backgrounds/background_intro.png").convert_alpha()
bg1_img = pygame.image.load("Public/Backgrounds/background_1.png").convert_alpha()
bg3_img = pygame.image.load("Public/Backgrounds/background_3.png").convert_alpha()
logo_img = pygame.image.load("Public/GameObjects/logo.png").convert_alpha()
panel_img = pygame.image.load("Public/GameObjects/panel.png").convert_alpha()

#drawing every picture, screen.blit ger en plats åt den önskade bilden.                     

def draw_intro():
    screen.blit(intro_img, (0, 0))

def draw_bg1():                         
    screen.blit(bg1_img, (0, 0))

def draw_bg3():
    screen.blit(bg3_img, (0, 0))

def draw_logo():
    screen.blit(logo_img,(150, 250))

def draw_panel():
    screen.blit(panel_img, (0, screen_height - bottom_panel))





while True:
    game_state.state_manager()
    clock.tick(60)

            
