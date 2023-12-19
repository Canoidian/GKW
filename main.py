# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    main.py                                            :+:    :+:             #
#                                                      +:+                     #
#    By: Kevin Nhan <kenha4996@ugcloud.ca>            +#+                      #
#                                                    +#+                       #
#    Created: 2023/12/13 11:07:56 by williamisaa   #+#    #+#                  #
#    Updated: 2023/12/18 11:07:17 by williamisaa   ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

# YT video to help us out
# https://www.youtube.com/watch?v=OUOI6iCrmCk&ab_channel=JCode

#? Libraries
import pygame, math
from sys import exit

from functions import *
from settings import *


#* Constants and Variables

#Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)

#^ Main
done = False
 
pygame.init() #Initializes the window
pygame.font.init()

# Creating window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("12/25") # Name of game
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self, name, speed):
        super().__init__()
        self.name = name
        self.speed = speed
        
        self.pos = pygame.math.Vector2(PLAYER_START_X, PLAYER_START_Y)
        
        self.image = pygame.transform.scale2x(pygame.image.load("/Users/williamisaak/Code/GKW/Asset/Character/player.png").convert_alpha())
        self.rect = self.image.get_rect(center = self.pos)
        
        self.inv = []
        
    def changeSpeed(self, value):
        self.speed = value
    
    def move(self, value, direction):
        if direction == "x":
            self.rect.centerx += value
        
        
    
        
# Initializing the player
character = Player("Gabriel", 3)

SpriteGroup = pygame.sprite.GroupSingle()
SpriteGroup.add(character)

# Load images - background ect
background = pygame.transform.scale(pygame.image.load("/Users/williamisaak/Code/GKW/Asset/Background/Background.jpg").convert(), (WIDTH, HEIGHT)) # Input path to background file

# #Draws a red rectangle at the coords (100,100) on the window
pygame.draw.rect(screen, WHITE, [100,100,150,200])
pygame.display.flip()


while True:
    keys = pygame.key.get_pressed() # Looks at all keys pressed
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Checks if user clicked the exited button
            pygame.quit()
            exit()
    
    # Detects when user holds A key
    if keys[pygame.K_a]:
        character.move(3, "x")
    # Detects when user holds D key
    if keys[pygame.K_d]:
        character.move(-3, "x")
    
    screen.blit(background, (0,0)) # To display background
    SpriteGroup.draw(screen)
    
    pygame.display.flip()
    clock.tick(FPS)