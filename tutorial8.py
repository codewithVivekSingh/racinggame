#Adding enemy and its movement
import pygame  
import sys
import random
import math
from pygame.locals import *
pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize

pygame.init()
#
myfont = pygame.font.SysFont("monospace", 24)

pygame.display.set_caption('Surya\'s Game')
background=pygame.image.load(r"I:\pythonfun\Pygame\folder\gaming\gameroad.png")
#pygame.mixer.music.load(r"I:\pythonfun\Pygame\folder\gaming\car-interior-1.mp3") 
#pygame.mixer.music.play(-1,0.0)

#defining our color that we are going to use in our game
black_ = pygame.Color(0, 0, 0)         # Black
white_ = pygame.Color(255, 255, 255)   # White
grey_ = pygame.Color(128, 128, 128)   # Grey
red_ = pygame.Color(255, 0, 0)       # Red

#cordinates for player starting point
global Xc, Yc

Xc=160
Yc=325
Xe1=75
Ye1=50
Xe2=100
Ye2=50
speed=5
X_change=0
Y_change=0
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
score=0

#creating Player class

class Player():
    def __init__(self):
        self.image=pygame.image.load(r"I:\pythonfun\Pygame\folder\gaming\car.png")
        self.surf = pygame.Surface((50, 80))
        
    def center(self):
        gameSurface.blit(player1.image, (Xc, Yc))

    def moveLeft(self):
        global Xc
        global X_change
        X_change = -1
        Xc=Xc+X_change
        if (Xc<50):
            Xc=50
        
        
        pygame.mixer.music.load(r"I:\pythonfun\Pygame\folder\gaming\TIRE_SKID.mp3") 
        pygame.mixer.music.play()
        
        #print(Xc)
   
    def moveRight(self):
        global Xc
        global X_change
        X_change = 1
        Xc=Xc+X_change
        if (Xc>270):
            Xc=270
        pygame.mixer.music.load(r"I:\pythonfun\Pygame\folder\gaming\TIRE_SKID.mp3") 
        pygame.mixer.music.play()
        
        
        
        #print(Xc)
    def moveUp(self):
        global Xc
        global Yc

        global Y_change
        Y_change = 0.3
        Yc=Yc-Y_change
        pygame.mixer.music.load(r"I:\pythonfun\Pygame\folder\gaming\TIRE_SKID.mp3") 
        pygame.mixer.music.play()
        
        #print(Yc)

    def moveDown(self):
        global Xc
        global Yc
        global Y_change
        Y_change = 0.3
        Yc=Yc+Y_change
        pygame.mixer.music.load(r"I:\pythonfun\Pygame\folder\gaming\TIRE_SKID.mp3") 
        pygame.mixer.music.play()
        
        #print(Yc)
class Enemy():
    def __init__(self):
        self.image=pygame.image.load(r"I:\pythonfun\Pygame\folder\gaming\enemy.png")
        self.surf = pygame.Surface((50, 80))

player1=Player()  
#Bomb1=Bomb()     
enemy1=Enemy() 
enemy2=Enemy()

#creating game surface
gameSurface = pygame.display.set_mode((400,400))


#filling the game surface with a grey color
gameSurface.fill(grey_)
#pygame.mixer.Channel(1).play(pygame.mixer.Sound(r'I:\pythonfun\Pygame\folder\gaming\car-interior-1.mp3'))

def game_over():
    font = pygame.font.Font('freesansbold.ttf', 60)
    text = font.render('Game Over', True, green, blue)

    textRect = text.get_rect()

    textRect.center = (400// 2, 400 // 2)

    gameSurface.blit(text,textRect)




#creating game loop

while True:
   # We write here thing to be happen in game
    gameSurface.fill(grey_)
    gameSurface.blit(background, (0, 0))

    #getting our player 1 on the game window

    #player1.center()
   #Checking every event
    for event in pygame.event.get():
        #if quit event happens, quit the game
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    keys = pygame.key.get_pressed()  # This will give us a dictonary where each key has a value of 1 or 0. Where 1 is pressed and 0 is not pressed.

    if keys[pygame.K_LEFT]: # We can check if a key is pressed like this
        player1.moveLeft()

    
    

    if keys[pygame.K_RIGHT]:
        player1.moveRight()
    
      
    if keys[pygame.K_UP]:
        player1.moveUp()
        
    if keys[pygame.K_DOWN]:
        player1.moveDown()


    
    gameSurface.blit(player1.image, (Xc, Yc))   

    gameSurface.blit(enemy1.image, (Xe1, Ye1)) 

    Ye1=Ye1+0.7
    
  

    if Ye1>=400:
        Ye1=50  
        Xe1=random.randint(50,275)

    score=score+1   
    D=math.sqrt(math.pow(Xc-Xe1, 2)+math.pow(Yc-Ye1, 2))
    print(D)
    
    scoretext = myfont.render("Score {0}".format(score), 1, (0,0,0))
    gameSurface.blit(scoretext, (5, 10))
    score += 1

    if D<35:
        print("Game Over")
        game_over()
        score=0
        pygame.mixer.music.load(r"I:\pythonfun\Pygame\folder\gaming\explosion.wav") 
        pygame.mixer.music.play()
        

    

    #remember to update the display
    pygame.display.update()