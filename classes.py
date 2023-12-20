# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    Classes.py                                         :+:    :+:             #
#                                                      +:+                     #
#    By: williamisaak <williamisaak@student.coda      +#+                      #
#                                                    +#+                       #
#    Created: 2023/12/19 10:38:16 by williamisaa   #+#    #+#                  #
#    Updated: 2023/12/19 11:32:45 by williamisaa   ########   odam.nl          #
#                                                                              #
# **************************************************************************** #


# Libraries
import pygame
from settings import *

# Classes
class Animation():
    def __init__(self, anims):
        self.anims = anims

        self.index = 0

    def animate(self, animType, increment):
        if animType == "Walk":
            if self.index >= len(self.anims):
                self.index = 0
            else:
                self.image = self.anims[int(self.index)]
                self.index += increment

class Present(pygame.sprite.Sprite):
    def __init__(self, name):
        super().__init__()
        self.name = name

        self.value = None
        self.defaultValue = 3

        self.pos = pygame.math.Vector2(0,0)

        self.image = pygame.transform.scale2x(pygame.image.load("").convert_alpha()) # Base image
        self.rect = self.image.get_rect(center = self.pos)

    def getValue(self):
        if self.name[-1].isnumeric():
            if self.name[-1] <= len(presentValues)-1:
                self.value = presentValues[int(self.name[-1])] # Searches through the presents value list and indexes the value of the present in the list
                print("\nIdentifier found! Returning present value...")
                return self.value
        
        return self.defaultValue #If the identifier was greater than the list or was not a number
    
    def spawn(self, image, posXY):
        self.pos = posXY
        self.image = pygame.transform.scale2x(pygame.image.load("").convert_alpha())
        self.rect = self.image.get_rect(center = self.pos)

class Player(pygame.sprite.Sprite):
    def __init__(self, name, speed):
        super().__init__()
        self.name = name
        self.speed = speed
        
        self.pos = pygame.math.Vector2(PLAYER_START_X, PLAYER_START_Y)
        
        self.image = pygame.transform.scale2x(pygame.image.load(image).convert_alpha()) # Base image
        self.rect = self.image.get_rect(center = self.pos) #Creates rectangle / hitbox around the image
        
        self.inv = []
        
        self.walkingAnimation = Animation([pygame.transform.scale2x(pygame.image.load("/Users/williamisaak/Code/GKW/Asset/Character/player.png").convert_alpha()),
                                pygame.transform.scale2x(pygame.image.load("/Users/williamisaak/Code/GKW/Asset/Character/playerWalk2x.png").convert_alpha())])
        
    def changeSpeed(self, value):
        self.speed = value
    
    def move(self, value, direction):
        if direction == "x":
            self.rect.centerx += value
            self.walkingAnimation.animate("Walk",0.07)
        else:
            self.rect.centery += value
            self.walkingAnimation.animate("Walk",0.07)
    
    def getPresent(self, present):
        pass


