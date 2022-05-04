#imports
import pygame
import sys
import random
import time
import keyboard #skriv vad detta gör sen  
from functools import *
from PIL import *

from sympy import false, var #skriv vad detta
from draws import *    #skriv vad detta gör sen  
from OpenGL.GL import *   #skriv vad detta gör sen 
from OpenGL.GLU import * #skriv vad detta gör sen
from tkinter import filedialog #skriv vad detta gör sen    
from tkinter import * #skriv vad detta gör sen
from pygame.locals import *

            
#to get everything started #bryter mot standard(?!)
pygame.init() 
pygame.mixer.init()

                                                    
#global variables


#idk where these should be
BOTTOM_PANEL = 150
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400 + BOTTOM_PANEL
COUNT = 0
FPS = 60
VEL = 10
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
        self.hide = False
        self.bgimage = pygame.image.load("img/Backgrounds/background_boss.png")
        self.bgY = 0
        self.bgX = 0

    def draw_bg1(self):
        if self.hide == False:
            screen.blit(self.bgimage, (self.bgX, self.bgY))

    

class GroundLevel(pygame.sprite.Sprite):
    def __init__(self):             
        super().__init__()
        self.hide = False                                   
        self.image = pygame.image.load("img/GameObjects/lunarground.png")                                     
        self.rect = self.image.get_rect(center = (350, 350))  #rect skapar en plats för bilden man vill ha                       
                                 
    def draw_gnd(self): 
        if self.hide == False:
            screen.blit(self.image, (0, 475))                        


class Panel(pygame.sprite.Sprite):
    def __init__(self):
        self.hide = False
        super().__init__()

    def drawpanel(self): #drawing the panel on the bottom
        if self.hide == False:
            screen.blit(pnl_img, (0, SCREEN_HEIGHT - BOTTOM_PANEL))   

class Mage(pygame.sprite.Sprite):
    pass

class Ranger(pygame.sprite.Sprite):
    pass

class Knight(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.hide = False
        self.image = pygame.image.load("img/Player1/Playersprite.png")
        self.image = pygame.transform.scale(self.image, (400, 475)) 
        self.rect = self.image.get_rect()
        self.position = pygame.math.Vector2((340, 240)) #pygame.math.vector2 är en 2D vektor som vi kan använda för att göra så att spriten rör sig.                            
        self.velocity = pygame.math.Vector2(0, 0) #rakt                                                                                                 
        self.acceleration = pygame.math.Vector2(0, 0)
        self.direction = "RIGHT"
    
    def knight_drawing(self):
        if self.hide == False:
            screen.blit(knight.image, knight.rect)

    def knight_speed(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            self.rect.x -= VEL
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.x += VEL

    def jumping(self):
        pass
 
    def animations(self):
        pass

                                                                                
    def attack(self):
        pass

    def jump(self):
        pass            


    def cameralock(self):
        if self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH


class Mob1(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__()
        self.hide = False

class GameName:
    font = pygame.font.SysFont("img/Fonts/VT323_Regular.ttf", 30)
    
    @classmethod
    def draw(cls, surf, username, *args):       
        text_surf = cls.font.render(str(username), True, 'white')
        surf.blit(text_surf, (180, 417))
        

class Intro(pygame.sprite.Sprite):
    def __init__(self):
        self.hide = False
        super().__init__()

    def introbg(self):
        if self.hide == False:
            screen.blit(bgintro_img, (0, 0))

    def logoimg(self):
        if self.hide == False:
            screen.blit(logo_img, (130, 160))


    def presstocontinue(self):
        if self.hide == False:
            screen.blit(press_img, (162, 280))



class StageManager():
    def __init__(self):
        self.SHOWTK = False

    def next_stage(self):
        pass

                            

    def stage_fixer1(self):
        self.tkwindow = Tk() 
        self.tkwindow.title("NAME") 
        self.tkwindow.geometry("300x200") 
        self.tkwindow.iconbitmap("img/GameObjects/icon.ico")
        btn1 = Button(self.tkwindow, text="Are you ready to start?", fg="blue", command = self.scene_4)  #command basically triggar def scene:1(): när man klickar på knappen
        btn1.place(x=80, y=150)
        self.tkwindow.mainloop() 


    def stage_fixer2(self):
        self.tkwindow = Tk() #så jag kan kalla på tkinter
        self.tkwindow.title("Login") #titel
        self.tkwindow.geometry("300x200") #skapar ett window, basically samma som pygame.display.set_mode 
        self.tkwindow.iconbitmap("img/GameObjects/icon.ico")

    #username label and text entry box
        usernameLabel = Label(self.tkwindow, text="Enter a username:").grid(row=0, column=0)
        username = StringVar()
        usernameEntry = Entry(self.tkwindow, textvariable=username).grid(row=0, column=1)                                                                                                                        
        
      
        btn1 = Button(self.tkwindow, text="Are you ready to start?", fg="blue", command = self.scene_2)  
        btn1.place(x=80, y=150)
        self.tkwindow.mainloop()
        return username.get()        

    def stage_fixer3(self):
        self.tkwindow = Tk()
        self.tkwindow.title("Welcome Hero...") 
        self.tkwindow.geometry("300x200") 
        self.tkwindow.iconbitmap("img/GameObjects/icon.ico")
        btn1 = Button(self.tkwindow, text="Are you ready to start?", fg="blue", command = self.scene_3) 
        btn1.place(x=80, y=150)        
                   


    def scene_0(self):
        intro.introbg()
        intro.logoimg() 
        intro.presstocontinue()
        GameName().draw()
        bg.hide = True
        gnd.hide = True  
        knight.hide = True 
        s1.hide = True 
        

    def scene_4(self):
        self.tkwindow.destroy()
        knight.knight_speed()
        knight.cameralock()
        intro.hide = True
        s1.hide = True
        bg.hide = False
        gnd.hide = False
        knight.hide = False
        
    def scene_2(self): 
        self.tkwindow.destroy()
        mgr.SHOWTK = False
        
        ball = pygame.Rect(0,0,10,10)
        screen.fill((0,0,0))
        pygame.draw.circle(screen,(255,255,255),ball.center,5)
        ball.move_ip(1,1) 
        s1.hide = False
        intro.hide = True
        bg.hide = True
        gnd.hide = True
        knight.hide = True

    def scene_3(self):
        self.tkwindow.destroy()
        ball = pygame.Rect(0,0,10,10)
        screen.fill((0,0,0))
        pygame.draw.circle(screen,(255,255,255),ball.center,5)
        ball.move_ip(1,1) 
        bg.hide = True
        gnd.hide = True
        pnl.hide = False
        knight.hide = True
        intro.hide = True
        s1.hide = True
        s2.hide = False


class SceneOne(pygame.sprite.Sprite):
    def sceneonebg(self):
        if self.hide == False:
            screen.blit(scene_1_img, (0, 0))

    def oldwiz(self):
        if self.hide == False:
            screen.blit(oldwiz_img, (400, 120))

    def paragraph(self):
        if self.hide == False:
            font = pygame.font.SysFont("img/Fonts/VT323_Regular.ttf", 30)
            wiztext = font.render(str("Welcome"), True, (255, 255, 255))
            screen.blit(wiztext, (85, 417))
    
    def paragraph2(self):
        if self.hide == False:
            font = pygame.font.SysFont("img/Fonts/VT323_Regular.ttf", 30)
            wiztext2 = font.render(str("You have been summoned to the world "), True, (255, 255, 255))
            wiztext3 = font.render(str("of Ruscandel in order to defeat the"), True, (255, 255, 255))
            wiztext4 = font.render(str("evil scheming Demon King, Baran. "), True, (255, 255, 255))
            wiztext5 = font.render(str("365 Days Remaining."), True, (128, 0, 0))
            wiztext6 = font.render(str("Press Space..."), True, (0, 0, 0))
            screen.blit(wiztext2, (15, 443))
            screen.blit(wiztext3, (15, 463))
            screen.blit(wiztext4, (15, 483))
            screen.blit(wiztext5, (15, 503))
            screen.blit(wiztext6, (235, 503))


class Scenetwo(pygame.sprite.Sprite):
    def __init__(self):
        self.SHOWTK = False
    
    def scenetwobg(self):
        if self.hide == False:
            font = pygame.font.SysFont("img/Fonts/VT323_Regular.ttf", 30)
            text1 = font.render(str("TUTORIAL WILL COMMENCE"), True, (255, 255, 255))
    

#bryter most standard(?)
bg = Background()
gnd = GroundLevel()  
pnl = Panel()       
knight = Knight()
mgr = StageManager()
intro = Intro()
s1 = SceneOne()
s2 = Scenetwo()

#game loop
if __name__ == "__main__":
    while True:
        s2.SHOWTK = True
        mgr.SHOWTK = True
        bg.draw_bg1()
        gnd.draw_gnd()
        knight.knight_speed()
        knight.knight_drawing()
        intro.introbg()
        intro.logoimg()
        intro.presstocontinue()

        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
              pass 

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and s2.SHOWTK == True:
                    s2.SHOWTK = False
                    usrname = mgr.stage_fixer2()
                    s1.sceneonebg()
                    pnl.drawpanel()
                    s1.oldwiz()
                    s1.paragraph()
                    s1.paragraph2()
                    GameName.draw(screen, usrname)
                         
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and mgr.SHOWTK == True: 
                    keyboard.block_key("return")       
                    mgr.stage_fixer1()
                    bg.draw_bg1()
                    gnd.draw_gnd()
                    knight.knight_speed() 
                    knight.knight_drawing()  
                    

        pygame.display.flip()               
        pygame.display.update()
