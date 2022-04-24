import pygame

BOTTOM_PANEL = 150
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400 + BOTTOM_PANEL

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #800x550 upplösning


#panel
pnl_img = pygame.image.load("img/GameObjects/panel.png").convert_alpha()                                        

#intro
bgintro_img = pygame.image.load("img/Backgrounds/introbg.png").convert_alpha()
logo_img = pygame.image.load("img/GameObjects/logo.png").convert_alpha()
press_img = pygame.image.load("img/GameObjects/p2c.png").convert_alpha()

#scene1
scene_1_img = pygame.image.load("img/Backgrounds/scene1bg.png")
oldwiz_img = pygame.image.load("img/GameObjects/oldwizardman.png").convert_alpha()
oldwiz_img = pygame.transform.scale(oldwiz_img, (360, 360))
