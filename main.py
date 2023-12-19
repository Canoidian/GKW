# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    main.py                                            :+:    :+:             #
#                                                      +:+                     #
#    By: Kevin Nhan <kenha4996@ugcloud.ca>            +#+                      #
#                                                    +#+                       #
#    Created: 2023/12/13 11:07:56 by williamisaa   #+#    #+#                  #
#    Updated: 2023/12/18 14:59:28 by williamisaa   ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

# YT video to help us out
# https://www.youtube.com/watch?v=OUOI6iCrmCk&ab_channel=JCode

#? Libraries
from typing import Iterable, Union
import pygame, math
from sys import exit

from pygame.sprite import AbstractGroup

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
        
        self.image = pygame.transform.scale2x(pygame.image.load(image).convert_alpha()) # Base image
        self.rect = self.image.get_rect(center = self.pos) #Creates rectangle / hitbox around the image
        
        self.inv = []
        
        self.index = 0
        self.walkingAnimation = [pygame.transform.scale2x(pygame.image.load("/Users/williamisaak/Code/GKW/Asset/Character/player.png").convert_alpha()),
                                pygame.transform.scale2x(pygame.image.load("/Users/williamisaak/Code/GKW/Asset/Character/playerWalk2x.png").convert_alpha())]
        
    def changeSpeed(self, value):
        self.speed = value
    
    def move(self, value, direction):
        if direction == "x":
            self.rect.centerx += value
        else:
            self.rect.centery += value
            
    def animate(self, animType, increment):
        if animType == "Walk":
            if self.index >= len(self.walkingAnimation):
                self.index = 0
            else:
                self.image = self.walkingAnimation[int(self.index)]
                self.index += increment
    
class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.offset = pygame.math.Vector2()
        
    def custom_draw(self):
        self.offset.x = character.rect.centerx - WIDTH // 2
        self.offset.y = character.rect.centery - HEIGHT // 2
        
        
            
    
        
# Initializing the player
character = Player(name, speed)

SpriteGroup = pygame.sprite.GroupSingle()
SpriteGroup.add(character)

# Load images - background
background = pygame.transform.scale(pygame.image.load(backgroundImg).convert(), (WIDTH, HEIGHT)) 

# #Draws a red rectangle at the coords (100,100) on the window
#pygame.draw.rect(screen, WHITE, [100,100,150,200])

while True:
    keys = pygame.key.get_pressed() # Looks at all keys pressed
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Checks if user clicked the exited button
            pygame.quit()
            exit()
    
    # Detects when user holds A key
    if keys[pygame.K_a]:
        character.move(-1*character.speed, "x")
        character.animate("Walking", 0.1)
    # Detects when user holds D key
    if keys[pygame.K_d]:
        character.move(character.speed, "x")
        character.animate("Walking", 0.1)

    # Detects when user holds W key
    if keys[pygame.K_w]:
        character.move(-1*character.speed, "y")
        character.animate("Walking", 0.1)
    # Detects when user holds S key
    if keys[pygame.K_s]:
        character.move(character.speed, "y")
        character.animate("Walking", 0.1)
    
    screen.blit(background, (0,0)) # To display background
    SpriteGroup.draw(screen)
    
    pygame.display.flip()
    clock.tick(FPS)