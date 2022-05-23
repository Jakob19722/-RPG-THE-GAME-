#imports
import pygame
"""A tool to make games easier with a newbie friendly gui which still allows you to make professional games (ofc they dont use this) but its possible. They have many inbuilt commands which i will showcase later down the code.
"""
import sys #I do not think this needs any explanation
import random #Neither does this
import time #or this
import keyboard 
"""This allows one to use the keyboard for keypresses which is nice for use.
"""
from PIL import * 
"""Allows one to easy draw text over stuff in python, usable for many things such as tkinter
"""
from sympy import Q, false, true, var 
"""Math module which i might use
"""
from draws import *   
"""My drawings in another file

"""
from tkinter import * 
from pygame.locals import *
"""contains useful constants such as pygame.display which will be showed later down the line
"""

            
#to get everything started #bryter mot standard(?!)
pygame.init() 
pygame.mixer.init()

                                                    
#global variables


#pygame setup (inte säker på var detta ska ligga i koden enligt pep-8 standarden)
BOTTOM_PANEL = 150
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400 + BOTTOM_PANEL
FPS = 60
VEL = 10
ACC = 0.3
FRIC = -0.10
CLOCK = pygame.time.Clock()

#knight.animations
run_ani_R = [pygame.image.load("img/Knight/Player_Sprite_R.png"), pygame.image.load("img/Knight/Player_Sprite2_R.png"),
             pygame.image.load("img/Knight/Player_Sprite3_R.png"),pygame.image.load("img/Knight/Player_Sprite4_R.png"),
             pygame.image.load("img/Knight/Player_Sprite5_R.png"),pygame.image.load("img/Knight/Player_Sprite6_R.png"),
             pygame.image.load("img/Knight/Player_Sprite_R.png")]
"""Loads in images

    Returns:
        image which we can draw later
"""

             

run_ani_L = [pygame.image.load("img/Knight/Player_Sprite_L.png"), pygame.image.load("img/Knight/Player_Sprite2_L.png"),
             pygame.image.load("img/Knight/Player_Sprite3_L.png"),pygame.image.load("img/Knight/Player_Sprite4_L.png"),
             pygame.image.load("img/Knight/Player_Sprite5_L.png"),pygame.image.load("img/Knight/Player_Sprite6_L.png"),
             pygame.image.load("img/Knight/Player_Sprite_L.png")]


# Attack animation for the RIGHT
attack_ani_R = [pygame.image.load("img/Knight/Player_Sprite_R.png"), pygame.image.load("img/Knight/Player_Attack_R.png"),
                pygame.image.load("img/Knight/Player_Attack2_R.png"),pygame.image.load("img/Knight/Player_Attack2_R.png"),
                pygame.image.load("img/Knight/Player_Attack3_R.png"),pygame.image.load("img/Knight/Player_Attack3_R.png"),
                pygame.image.load("img/Knight/Player_Attack4_R.png"),pygame.image.load("img/Knight/Player_Attack4_R.png"),
                pygame.image.load("img/Knight/Player_Attack5_R.png"),pygame.image.load("img/Knight/Player_Attack5_R.png"),
                pygame.image.load("img/Knight/Player_Sprite_R.png")]
 
# Attack animation for the LEFT
attack_ani_L = [pygame.image.load("img/Knight/Player_Sprite_L.png"), pygame.image.load("img/Knight/Player_Attack_L.png"),
                pygame.image.load("img/Knight/Player_Attack2_L.png"),pygame.image.load("img/Knight/Player_Attack2_L.png"),
                pygame.image.load("img/Knight/Player_Attack3_L.png"),pygame.image.load("img/Knight/Player_Attack3_L.png"),
                pygame.image.load("img/Knight/Player_Attack4_L.png"),pygame.image.load("img/Knight/Player_Attack4_L.png"),
                pygame.image.load("img/Knight/Player_Attack5_L.png"),pygame.image.load("img/Knight/Player_Attack5_L.png"),
                pygame.image.load("img/Knight/Player_Sprite_L.png")]
 


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #800x550 upplösning
pygame.display.set_caption("Endless Regressor")   
icon = pygame.image.load("img/GameObjects/icon.png")      
pygame.display.set_icon(icon)



#Klasser




                            
class Music:
    def __init__(self):
        pass

    def maintheme(self):
        pygame.mixer.music.load("music/Soundtracks/maintheme.mp3")
        """This loads in the music
        """
        pygame.mixer.music.play(-1, 0, 0)
        """Plays the song, loops, start, fade_ms, -1 lets the music loop infinitely
        """

    def inntheme(self):
        pygame.mixer.music.load("music/Soundtracks/inn.mp3")
        pygame.mixer.music.play(-1, 0 ,0)

    def edgelordmusic(self):
        pygame.mixer.music.load("music/Soundtracks/Electrodynamix1.mp3")
        pygame.mixer.music.play(-1, 0 ,0)



class Background(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__() #super gör att andra klasser smidigare får tillgång till "main-klassen" men nu har jag inte lagt till något än.
        self.hide = False
        self.bgimage = pygame.image.load("img/Backgrounds/background_3.png")
        self.bgY = 0
        self.bgX = 0

    def draw_bg1(self):
        """Drawing an image on it's x and y cordinates.
        """
        if self.hide == False:
            screen.blit(self.bgimage, (self.bgX, self.bgY))
        """draws an image over the desired place

        Returns:
            an images                                                                   
        """

    

class GroundLevel(pygame.sprite.Sprite):
    def __init__(self):             
        super().__init__()
        self.hide = False                                   
        self.bgimage = pygame.image.load("img/GameObjects/ground.png")                                   
        self.rect = self.bgimage.get_rect(center = (350, 530))
        """Makes a rectangular area at the desired cordinates
        Returns:
            a list of rects of the areas
        """
    
   

    def draw_gnd2(self): 
        if self.hide == False:
            screen.blit(self.bgimage, (self.rect.x, self.rect.y))            

class LunarGround(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.hide = False
        self.bgimage = pygame.image.load("img/GameObjects/lunarground.png")  
        self.rect = self.bgimage.get_rect(center = (350, 530)) 

    def draw_gnd3(self):
        if self.hide == False:
            screen.blit(self.bgimage, (self.rect.x, self.rect.y))


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
        self.jumping = False
        self.running = False
        self.health = 300
        self.move_frame = 0
        self.attacking = False
        self.cooldown = False
        self.attack_frame = 0
        self.hide = False
        self.image = pygame.image.load("img/Knight/Player_Sprite_R.png")
        self.rect = self.image.get_rect()
        self.vx = 0
        self.pos = pygame.math.Vector2((340, 240)) #pygame.math.vector2 is a 2d vector we can use to make the sprite move in a more "complex" or rather useful way, if you add on more feautres otherwise you can juse change the blit cords.                          
        self.vel = pygame.math.Vector2(0, 0) #rakt                                                                                                 
        self.acc = pygame.math.Vector2(0, 0)
        self.direction = "RIGHT"
    
    def knight_drawing(self):
        if self.hide == False:
            screen.blit(knight.image, knight.rect)

    def knight_speed(self):
       #implementing newton, gravity, y cord
      self.acc = pygame.math.Vector2(0,0.5)
 
      # 
      if abs(self.vel.x) > 0.3:
        # abs returns the absolute value, 
        # of course i found this on the guide but it is useful as the 
        # echaracter can go with a negative x cordinate which makes -x = x
        
        self.running = True
      else:
            self.running = False

 
      #this is the BASIC movement that even I could come up with myself easily but the code later down is the one i copied as it lets one make more advaced movement.
      if keyboard.is_pressed("a"):
            self.acc.x = -ACC
      if keyboard.is_pressed("d"):
            self.acc.x = ACC 
 
      
      self.acc.x += self.vel.x * FRIC
      self.vel += self.acc
      self.pos += self.vel + 0.5 * self.acc  #updating the position
 
      
      if self.pos.x > SCREEN_WIDTH:
            self.pos.x = 0
      if self.pos.x < 0:
            self.pos.x = SCREEN_WIDTH 
            """Basically IF character goes outside the screen, it comes from the other side instead and vice versa.
            """
     
      self.rect.midbottom = self.pos  #updating the position

    def update(self):
        if self.move_frame > 6:
            self.move_frame = 0
            return #returns the value of which animation is running
        if self.jumping == False and self.running == True:
            if self.vel.x > 0:
                self.image = run_ani_R[self.move_frame] #changing animation
                self.direction = "RIGHT"
            else:
                self.image = run_ani_L[self.move_frame] #this too, changes animation
                self.direction = "LEFT"
                self.move_frame += 1
       

    def attack(self):             
      if self.attack_frame > 10:
            self.attack_frame = 0
            self.attacking = False
            """If the animation is finished it returns to the original sprite animation
            """
 
      # This is also code I would never be able to come up with myself as its a bugfix with the animation
      if self.direction == "RIGHT":
             self.image = attack_ani_R[self.attack_frame]
      elif self.direction == "LEFT":
             self.correction()
             self.image = attack_ani_L[self.attack_frame] 
 
      # Update the current attack frame  
      self.attack_frame += 1


    def correction(self):
      if self.attack_frame == 1:
            self.pos.x -= 20
      if self.attack_frame == 10:
            self.pos.x += 20 #this too



    def newton_gravity(self):
        """What it does it that if they collide they will DIE if I change False to True. But the other part is that it checks if the knight/user is moving downwards and if he isnt jumping becomes false
        """
        hits = pygame.sprite.spritecollide(knight ,gnd_group, False)
        if self.vel.y > 0:
            if hits:
                lowest = hits[0]
                if self.pos.y < lowest.rect.bottom:
                    self.pos.y = lowest.rect.top + 1
                    self.vel.y = 0
                    self.jumping = False
        

    

    def jump(self): #this code is very much similar to the one above in some sense.
        self.rect.x += 1
        hits = pygame.sprite.spritecollide(self, gnd_group, False)
        
        self.rect.x -= 1
        if hits and not self.jumping:
            self.jumping = True
            self.vel.y = -12

    def hp(self):
        self.health = self.health - 10
        if self.health <= 0:
            print("dont worry nothing happens")


class Mobs(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 50
        self.hide = False
        self.image = pygame.image.load("img/Mobs/test.png")
        self.rect = self.image.get_rect()     
        self.pos = pygame.math.Vector2(0, 0)
        self.vel = pygame.math.Vector2(0, 0)
        self.direction = random.randint(0, 1) # 0 = right, 1 = left
        self.vel.x = random.randint(2, 6) / 2
        """This makes it look like goblin has its own movement because it is randomized.
        """
        if self.direction == 0:
            self.pos.x = 0
            self.pos.y = 350
        if self.direction == 1:
            self.pos.x = 700
            self.pos.y = 350
            

        
    def move(self): 
            if self.pos.x >= (SCREEN_WIDTH-20):
                    self.direction = 1
            elif self.pos.x <= 0:
                    self.direction = 0
              
            if self.direction == 0:
                self.pos.x += self.vel.x
            if self.direction == 1:
                self.pos.x -= self.vel.x
                
            self.rect.center = self.pos 
            """This updates the image's position
            """

            
    def render(self):
        if self.hide == False:
            screen.blit(self.image, (self.pos.x, self.pos.y))
        

    def hp(self):
        self.health = self.health - 10
        if self.health <= 0 and l.stage_generator == 6:
            mgr.stage_fixer7()    

class EdgelordBoss(pygame.sprite.Sprite):
    def __init__(self):
        self.health = 500
        self.defense = 300
        self.dexterity = 0.5
        self.hide = False
        self.image = pygame.image.load("img/Mobs/edgelord_boss.png")
        self.rect = self.image.get_rect()
        self.pos = pygame.math.Vector2(0, 0)
        self.vel = pygame.math.Vector2(0, 0)
        self.direction = random.randint(0, 1)
        self.vel.x = random.randint(2, 6) / 4
        self.vel.y = random.randint(2, 6)
        
        if self.direction == 0:
            self.pos.x = 0
            self.pos.y = 350
        if self.direction == 1:
            self.pos.x = 700
            self.pos.y = 350

    def move(self):
            if self.pos.x >= (SCREEN_WIDTH-20):
                    self.direction = 1
            elif self.pos.x <= 0:
                    self.direction = 0
            
            if self.direction == 0:
                self.pos.x += self.vel.x
            if self.direction == 1:
                self.pos.x -= self.vel.x
                
            self.rect.center = self.pos 
    def render(self):
        if self.hide == False:
            screen.blit(self.image, (self.pos.x, self.pos.y))

    def hp(self):
        self.health = self.health - 10
        if self.health <= 0 and l.stage_generator == 6:
            mgr.stage_fixer7()    

    def move2(self): 
            if self.pos.x >= (SCREEN_HEIGHT-20):
                    self.direction = 1
            elif self.pos.y <= 0:
                    self.direction = 0
            # Updates position with new values     
            if self.direction == 0:
                self.pos.y += self.vel.y
            if self.direction == 1:
                self.pos.y -= self.vel.y
                
            self.rect.center = self.pos # 


    def render(self):
        if self.hide == False:
            screen.blit(self.image, (self.pos.x, self.pos.y))

    def hp(self):
        self.health = self.health - 10
        if self.health <= 0 and l.stage_generator == 6:
            mgr.stage_fixer7()    




class GameName:
    font = pygame.font.SysFont("img/Fonts/VT323_Regular.ttf", 30)
    
    @classmethod
    def draw(cls, surf, username, *args):       
        text_surf = cls.font.render(str(username), True, 'white')
        surf.blit(text_surf, (180, 417))
        """This renders the username and I found this in a tutorial of where you use classmethod as you can call on this method very easily and is easily accessable.

        Returns:
            a class method for a function
        """
        

class Intro(pygame.sprite.Sprite):
    def __init__(self):
        self.hide = False
        super().__init__() #this was something that could come in handy very LATE in the tutorial but that was perhaps 3000lines down or something and I only followed the tutorial to about 150 lines (of course changing a few things and really understanding the code)

    def introbg(self):
        if self.hide == False:
            screen.blit(bgintro_img, (0, 0))

    def logoimg(self):
        if self.hide == False:
            screen.blit(logo_img, (130, 160))


    def presstocontinue(self):
        if self.hide == False:
            screen.blit(press_img, (162, 280))


        
				

class WindowManager():
    def __init__(self):
        self.SHOWTK = False
                          



    def stage_fixer2(self):
        self.tkwindow = Tk() #så jag kan kalla på tkinter
        self.tkwindow.title("Login") #titel
        self.tkwindow.geometry("300x200") #skapar ett window, basically samma som pygame.display.set_mode 
        self.tkwindow.iconbitmap("img/GameObjects/icon.ico")
        
        """The only thing here which might need explanation is the button of which basically just in a button that trigger a "command", a function which of in this case is scene_x
            """


    #username label and text entry box
        usernameLabel = Label(self.tkwindow, text="Enter a username:").grid(row=0, column=0)
        username = StringVar()#makes it easier to use the value, username,
        usernameEntry = Entry(self.tkwindow, textvariable=username).grid(row=0, column=1)  #An entry shows a textline of the user can write down something and then save it.       
                                                                                                         
        
      
        btn1 = Button(self.tkwindow, text="Are you ready to start?", fg="blue", command = self.scene_1)  
        btn1.place(x=80, y=150)
        self.tkwindow.mainloop() 
        return username.get()   #actually returns the username the user wrote down.

    def stage_fixer3(self):
        self.tkwindow = Tk()
        self.tkwindow.title("Welcome Hero...")                                                                                                                                                  
        self.tkwindow.geometry("300x200") 
        self.tkwindow.iconbitmap("img/GameObjects/icon.ico")
        btn1 = Button(self.tkwindow, text="Are you ready to start?", fg="blue", command = self.scene_2) 
        btn1.place(x=80, y=150)   
        self.tkwindow.mainloop()     

    
    def stage_fixer4(self):
        self.tkwindow = Tk()
        self.tkwindow.title("Welcome Hero...")                                                                                                                                                  
        self.tkwindow.geometry("300x200") 
        self.tkwindow.iconbitmap("img/GameObjects/icon.ico")
        btn1 = Button(self.tkwindow, text="Are you ready to start?", fg="blue", command = self.scene_3) 
        btn1.place(x=80, y=150)   
        self.tkwindow.mainloop()     

    def stage_fixer5(self):
        self.tkwindow = Tk()
        self.tkwindow.title("Welcome Hero...")                                                                                                                                                  
        self.tkwindow.geometry("300x200") 
        self.tkwindow.iconbitmap("img/GameObjects/icon.ico")
        btn1 = Button(self.tkwindow, text="Are you ready to start?", fg="blue", command = self.scene_4) 
        btn1.place(x=80, y=150)   
        self.tkwindow.mainloop()

    def stage_fixer6(self):
        self.tkwindow = Tk()
        self.tkwindow.title("Welcome Hero...")                                                                                                                                                  
        self.tkwindow.geometry("300x200") 
        self.tkwindow.iconbitmap("img/GameObjects/icon.ico")
        btn1 = Button(self.tkwindow, text="Are you ready to start?", fg="blue", command = self.scene_5) 
        btn1.place(x=80, y=150)   
        self.tkwindow.mainloop()   


    def stage_fixer7(self):
        self.tkwindow = Tk()
        self.tkwindow.title("Do you wanna proceed")                                                                                                                                                  
        self.tkwindow.geometry("300x200") 
        self.tkwindow.iconbitmap("img/GameObjects/icon.ico")
        btn1 = Button(self.tkwindow, text="Are you ready to start?", fg="blue", command = self.scene_7) 
        btn1.place(x=80, y=150)   
        self.tkwindow.mainloop()  


    def stage_fixer8(self):
        self.tkwindow = Tk()
        self.tkwindow.title("VIRUS!!! VARNING!!")                                                                                                                                                  
        self.tkwindow.geometry("300x200") 
        self.tkwindow.iconbitmap("img/GameObjects/icon.ico")
        btn1 = Button(self.tkwindow, text="Ender Of Spacetime is waiting....?", fg="blue", command = self.scene_8) 
        btn1.place(x=80, y=150)   
        self.tkwindow.mainloop()   


  
    def killgoblins(self): 
        self.tkwindow = Tk()

        self.tkwindow.title("Adventure Quest")
        self.tkwindow.geometry("350x450")
        self.tkwindow.iconbitmap("img/GameObjects/icon.ico")


        bg = PhotoImage(file = "img/Backgrounds/tkbg.png")


        canvas1 = Canvas( self.tkwindow, width = 400,
                        height = 400)

        canvas1.pack(fill = "both", expand = True)


        canvas1.create_image( 0, 0, image = bg,
                            anchor = "nw")
        canvas1.create_text(155, 50, font="Courier 16 bold" ,text = "Subjugate The Goblins")
        canvas1.create_text(145, 80, font="Roman 14" ,text = "The villagers are afraid these")
        canvas1.create_text(147, 100, font="Roman 14" ,text = "bloodthirsty goblins are gonna")
        canvas1.create_text(167, 120, font="Roman 14" ,text = "kill them and burn up their village.")
        canvas1.create_text(174, 140, font="Roman 14" ,text = "The goblins have started to close in.")
        canvas1.create_text(177, 160, font="Roman 14" ,text = "they are located in springwood glade.")
        canvas1.create_text(120, 250, font="Courier 16 bold" ,text = "Quest Objective")
        canvas1.create_text(147, 280, font="Roman 14" ,text = "You have to help the villagers.")
        canvas1.create_text(137, 300, font="Roman 14" ,text = "You must kill One goblin!")
        btn1 = Button(self.tkwindow, text="Accept", fg="yellow", bg="red", command = self.scene_6) 
        btn1.place(x=10, y=410)
        self.tkwindow.mainloop()
        """Canvas is basically pygames equivalent to rect from my understanding as it also creatres a drawing space.
        """

    
                   
    def scene_0(self):
        intro.introbg()
        intro.logoimg() 
        intro.presstocontinue()
        GameName().draw()
        bg.hide = True
        gnd.hide = True  
        lgnd.hide = True
        knight.hide = True 
        mobs.hide = True
        eg.hide = True
         
    def scene_1(self): 
        self.tkwindow.destroy()
        mgr.SHOWTK = False
        
        ball = pygame.Rect(0,0,10,10)
        screen.fill((0,0,0))
        pygame.draw.circle(screen,(255,255,255),ball.center,5)
        ball.move_ip(1,1)  #clears the screen, just googled this up BUT something important to note is that I would NEVER use this again if I knew what I couldve done, as written in the readme, in the first paragraph.
        s1.hide = False
        intro.hide = True
        mobs.hide = True
        bg.hide = True
        gnd.hide = True
        lgnd.hide = True
        knight.hide = True
        eg.hide = True

    def scene_2(self):
        self.tkwindow.destroy()
        ball = pygame.Rect(0,0,10,10)
        screen.fill((0,0,0))
        pygame.draw.circle(screen,(255,255,255),ball.center,5)
        ball.move_ip(1,1) 
        bg.hide = True
        gnd.hide = True
        lgnd.hide = True
        mobs.hide = True
        pnl.hide = False
        knight.hide = True
        intro.hide = True
        s1.hide = True
        s2.hide = False
        eg.hide = True

    def scene_3(self):
        self.tkwindow.destroy()
        ball = pygame.Rect(0,0,10,10)
        screen.fill((0,0,0))
        pygame.draw.circle(screen,(255,255,255),ball.center,5)
        ball.move_ip(1,1) 
        bg.hide = True
        gnd.hide = True
        lgnd.hide = True
        mobs.hide = True
        pnl.hide = False
        knight.hide = True
        intro.hide = True
        s1.hide = True
        s2.hide = True
        s3.hide = False
        eg.hide = True

    def scene_4(self):
        self.tkwindow.destroy()
        ball = pygame.Rect(0,0,10,10)
        screen.fill((0,0,0))
        pygame.draw.circle(screen,(255,255,255),ball.center,5)
        ball.move_ip(1,1) 
        bg.hide = True
        gnd.hide = True
        lgnd.hide = True
        pnl.hide = False
        knight.hide = True
        mobs.hide = True
        intro.hide = True
        s1.hide = True
        s2.hide = True
        s3.hide = True
        s4.hide = False
        eg.hide = True

    def scene_5(self):
        self.tkwindow.destroy()
        ball = pygame.Rect(0,0,10,10)
        screen.fill((0,0,0))
        pygame.draw.circle(screen,(255,255,255),ball.center,5)
        ball.move_ip(1,1)
        bg.hide = True
        gnd.hide = True
        lgnd.hide = True
        pnl.hide = False
        knight.hide = True
        mobs.hide = True
        intro.hide = True
        s1.hide = True
        s2.hide = True
        s3.hide = True
        s4.hide = True
        s5.hide = False  
        eg.hide = True     

    def scene_6(self):
        self.tkwindow.destroy()
        knight.newton_gravity()
        knight.knight_speed()
        mobs.update()
        mobs.move()
        mobs.render
        mobs.hide = False
        intro.hide = True
        lgnd.hide = True
        s1.hide = True
        s2.hide = True
        s3.hide = True
        s4.hide = True
        s5.hide = True
        s6.hide = False
        bg.hide = False
        gnd.hide = False
        knight.hide = False
        eg.hide = True


    def scene_7(self):
        self.tkwindow.destroy()
        ball = pygame.Rect(0,0,10,10)
        screen.fill((0,0,0))
        pygame.draw.circle(screen,(255,255,255),ball.center,5)
        ball.move_ip(1,1)
        mobs.hide = True
        intro.hide = True
        gnd.hide = True
        lgnd.hide = True
        knight.hide = True
        pnl.hide = False
        s1.hide = True
        s2.hide = True
        s3.hide = true
        s4.hide = True
        s5.hide = true
        s6.hide = True
        bg.hide = True
        s7.hide = False
        eg.hide = True
        s7.scenesevenbg()
        s7.innkeeper()
        pnl.drawpanel()
        s7.paragraph()
        l.next_stage()


    def scene_8(self):
        self.tkwindow.destroy()
        ball = pygame.Rect(0,0,10,10)
        screen.fill((0,0,0))
        pygame.draw.circle(screen,(255,255,255),ball.center,5)
        ball.move_ip(1,1)
        mobs.hide = True
        intro.hide = True
        gnd.hide = True
        lgnd.hide = False
        bg.hide = True
        pnl.hide = True
        knight.hide = True
        s1.hide = True
        s2.hide = True
        s3.hide = True
        s4.hide = True
        s5.hide = True
        s6.hide = True
        s7.hide = True
        s8.hide = False
        eg.hide = False

class EventHandler():
    def __init__(self):
        self.stage_generator = 0

    def next_stage(self):
        self.stage_generator +=1 #To see what stage we are at, this is something I personally was working on to make it a easy way to make different scenes and then I realised I could just do this and set other requirements as well for changing scene, used later in code.

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


class SceneTwo(pygame.sprite.Sprite):
    def __init__(self):
        self.SHOWTK = False
    
    def scenetwobg(self):
        if self.hide == False:
            screen.blit(scene_2_img, (0, 0))

    def oldwiz2(self):
        if self.hide == False:
            screen.blit(oldwiz_img, (400, 120))

    def bg2paragraph(self):
        font = pygame.font.SysFont("img/Fonts/VT323_Regular.ttf", 30)
        wiztext = font.render(str("I have summoned you to the local inn,"), True, (255, 255, 255))
        wiztext2 = font.render(str("also known as the Adventurer's guild. "), True, (255, 255, 255))
        wiztext3 = font.render(str("Begin your journey and gain fame. "), True, (255, 255, 255))
        wiztext6 = font.render(str("Press Space To Continue..."), True, (0, 0, 0))
        screen.blit(wiztext, (15, 423))
        screen.blit(wiztext2, (15, 443))
        screen.blit(wiztext3, (15, 463))
        screen.blit(wiztext6, (60, 503))

class SceneThree(pygame.sprite.Sprite):
    def scenethreebg(self):
        if self.hide == False:
            screen.blit(inn_img, (0, 0))


class SceneFour(pygame.sprite.Sprite):
    def scenefourbg(self):
        if self.hide == False:
            screen.blit(inn2_img, (0, 0))
    def innkeeper(self):
        if self.hide == False:
            screen.blit(innkeeper_img, (0, 50))

    def paragraphs4(self):
        font = pygame.font.SysFont("img/Fonts/VT323_Regular.ttf", 30)
        wiztext = font.render(str("Hello there young one!"), True, (255, 255, 255))
        wiztext2 = font.render(str("I have not seen you before, you must"), True, (255, 255, 255))
        wiztext3 = font.render(str("be a new one are ye?"), True, (255, 255, 255))
        wiztext4 = font.render(str("Take yer quest over there, don't die!"), True, (255, 255, 255))
        wiztext5 = font.render(str("[Always press space to continue...]"), True, (255, 255, 0))
        screen.blit(wiztext, (15, 423))
        screen.blit(wiztext2, (15, 443))
        screen.blit(wiztext3, (15, 463))
        screen.blit(wiztext4, (15, 483))
        screen.blit(wiztext5, (415, 423))

class SceneFive(pygame.sprite.Sprite):
    def scenefivebg(self):
        if self.hide == False:
            screen.blit(questboard_img, (0, 0))

class SceneSix(pygame.sprite.Sprite):
    def scenesixbg(self):
        if self.hide == False:
            screen.blit(scene_6_img, (0, 0))

class SceneSeven(pygame.sprite.Sprite):
    def scenesevenbg(self):
        if self.hide == False:
            screen.blit(inn2_img, (0, 0))

    def innkeeper(self):
        if self.hide == False:
            screen.blit(inndevil_img, (0, 50))

    def paragraph(self):
        font = pygame.font.SysFont("img/Fonts/VT323_Regular.ttf", 30)
        text = font.render(str("YOU ARE TOO STRONG FOR THIS WORLD THIS BE CONTAINED IN."), True, (255, 0, 0))
        text2 = font.render(str("YOU MUST BE PURGED!!!!!!!!"), True, (0, 0, 0))
        text3 = font.render(str("PREPARE TO FACE THE ALLMIGHTY EDGELORD, ALBION!!!!!!!!!"), True, (255, 0, 0))
        screen.blit(text, (15, 423))
        screen.blit(text2, (15, 443))
        screen.blit(text3, (15, 463))


class SceneEight(pygame.sprite.Sprite):

    def bg(self):
        if self.hide == False:
            screen.blit(bgboss_img, (0, 0))

#bryter most standard(?)
m = Music()
bg = Background()
gnd = GroundLevel()
gnd_group = pygame.sprite.Group()
gnd_group.add(gnd) #this is adding  the ground as a object of collision we can refer to, there are other ways to do this which I personally find easier. as I refered to in line 1015.
lgnd = LunarGround()
lgnd_group = pygame.sprite.Group()
lgnd_group.add(gnd) 
pnl = Panel()       
knight = Knight()
Knightgroup = pygame.sprite.Group()
Knightgroup.add(knight)
mobs = Mobs()
eg = EdgelordBoss()
mgr = WindowManager()
l = EventHandler()
intro = Intro()
s1 = SceneOne()
s2 = SceneTwo()
s3 = SceneThree()
s4 = SceneFour()
s5 = SceneFive()
s6 = SceneSix()
s7 = SceneSeven()
s8 = SceneEight()



#game loop
if __name__ == "__main__":
    cd = pygame.USEREVENT + 1 #it is used to create an "invincibility time" of where our character has a cooldown.
    #This is used so that the user/player CAN NOT spam attack to deal infinite damage.
    m.maintheme()
    while True:
        s2.SHOWTK = True
        mgr.SHOWTK = True
        bg.draw_bg1()
        gnd.draw_gnd2()
        lgnd.draw_gnd3()
        knight.newton_gravity()
        knight.update()
        knight.knight_speed()
        knight.knight_drawing()
        mobs.update()
        mobs.render()
        mobs.move()
        eg.update()
        eg.render()
        eg.move()
        eg.move2()

        intro.introbg()
        intro.logoimg()
        intro.presstocontinue()
        knight_mob_collision = knight.rect.colliderect(mobs.rect)
        

        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == cd:
                knight.cooldown = False
                pygame.time.set_timer(cd, 0)
            if event.type == pygame.QUIT:
                pygame.QUIT()
                sys.exit()      



            if keyboard.is_pressed("space") and l.stage_generator == 0:
                    s2.SHOWTK = False
                    usrname = mgr.stage_fixer2()
                    s1.sceneonebg()
                    pnl.drawpanel()
                    s1.oldwiz()
                    s1.paragraph()
                    s1.paragraph2()
                    l.next_stage()
                    GameName.draw(screen, usrname)

            if keyboard.is_pressed("space") and l.stage_generator == 1:
                    mgr.stage_fixer3()
                    s2.scenetwobg()
                    pnl.drawpanel()
                    s2.oldwiz2()
                    s2.bg2paragraph()
                    l.next_stage()

            if keyboard.is_pressed("space") and l.stage_generator == 2:
                mgr.stage_fixer4()
                pygame.mixer.music.stop()
                m.inntheme()
                s3.scenethreebg()
                l.next_stage()

            if keyboard.is_pressed("space") and l.stage_generator == 3:
                mgr.stage_fixer5()
                s4.scenefourbg()
                pnl.drawpanel()
                s4.innkeeper()
                s4.paragraphs4()
                l.next_stage()                  
            
            if keyboard.is_pressed("space") and l.stage_generator == 4:
                mgr.stage_fixer6()
                s5.scenefivebg()
                l.next_stage()

            if keyboard.is_pressed("space") and l.stage_generator == 5:
                pygame.mixer.music.stop()
                mgr.killgoblins()
                s6.scenesixbg()
                knight.newton_gravity()
                knight.update()
                knight.knight_speed()
                knight.knight_drawing()
                mobs.render()
                mobs.update()
                l.next_stage()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                  knight.jump()
                  
                if event.key == pygame.K_RETURN:
                    if knight.attacking == False:
                        knight.attack()
                        knight.attacking = True  
                        knight.update()
                    if knight.attacking == True:
                        knight.attack() 
                        knight.knight_speed() 

                    if knight_mob_collision:
                        mobs.hp()

            if keyboard.is_pressed("space") and l.stage_generator == 7:
                    mgr.stage_fixer8()
                    m.edgelordmusic()
                    s8.bg()
                    eg.update()
                    eg.render()
                
            
            

 

            
                    

        pygame.display.flip()               
        pygame.display.update()
