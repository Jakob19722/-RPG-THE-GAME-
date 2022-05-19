import pygame

BOTTOM_PANEL = 150
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400 + BOTTOM_PANEL

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #800x550 upplösning


#npc
oldwiz_img = pygame.image.load("img/GameObjects/oldwizardman.png").convert_alpha()
oldwiz_img = pygame.transform.scale(oldwiz_img, (360, 360))
innkeeper_img = pygame.image.load("img/GameObjects/innkeeper.png").convert_alpha()
innkeeper_img = pygame.transform.scale(innkeeper_img, (360, 360))
inndevil_img = pygame.image.load("img/GameObjects/inndevil.png").convert_alpha()
inndevil_img = pygame.transform.scale(inndevil_img, (360, 360))
#panel
pnl_img = pygame.image.load("img/GameObjects/panel.png").convert_alpha()                                        

#gnd
gnd_img = pygame.image.load("img/GameObjects/ground.png").convert_alpha()
#intro
bgintro_img = pygame.image.load("img/Backgrounds/introbg.png").convert_alpha()
logo_img = pygame.image.load("img/GameObjects/logo.png").convert_alpha()
press_img = pygame.image.load("img/GameObjects/p2c.png").convert_alpha()

#scene1
scene_1_img = pygame.image.load("img/Backgrounds/scene1bg.png")


#scene2
scene_2_img = pygame.image.load("img/Backgrounds/scene2bg.png")

#scene3
inn_img = pygame.image.load("img/Backgrounds/inn.png")

#scene4
inn2_img = pygame.image.load("img/Backgrounds/inn2.png")

#scene5
questboard_img = pygame.image.load("img/Backgrounds/quest.png")

#scene6
scene_6_img = pygame.image.load("img/Backgrounds/background_3.png")

#bossstage
bgboss_img = pygame.image.load("img/Backgrounds/background_boss.png")
