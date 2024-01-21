# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    classes.py                                         :+:    :+:             #
#                                                      +:+                     #
#    By: williamisaak <williamisaak@student.coda      +#+                      #
#                                                    +#+                       #
#    Created: 2023/12/19 10:38:16 by williamisaa   #+#    #+#                  #
#    Updated: 2024/01/21 13:55:03 by williamisaa   ########   odam.nl          #
#                                                                              #
# **************************************************************************** #


# Libraries
import pygame
from settings import *

# Classes
class Animation():
    def __init__(self, SpriteAnim):
        self.SpriteAnim = SpriteAnim
        
        self.index = 0
    
    def animate(self, increment, obj, repeat=True):
        """Requires an increment to control the cycle speed of the sprites
            Repeat is turned on by default."""
        if self.index >= len(self.SpriteAnim):
            if repeat == True:
                self.index = 0
            else:
                self.index = len(self.SpriteAnim) - 1
        else:
            obj.image = self.SpriteAnim[int(self.index)]
            self.index += increment
            

class Present(pygame.sprite.Sprite):
    def __init__(self, name):
        super().__init__()
        self.name = name
        
        self.image = pygame.transform.scale2x(pygame.image.load("/Users/williamisaak/Code/GKW/Asset/Presents/medium_present.png")).convert_alpha() # Base image
        self.pos = pygame.math.Vector2()
        self.rect = self.image.get_rect(center = self.pos)
        
        self.value = 0
        self.defaultValue = 30
    
    def getValue(self):
        if self.name[-1].isnumeric():
            if int(self.name[-1]) <= len(presentValues)-1:     
                self.value = presentValues[int(self.name[-1])]
                #print("\nIdentifier found! Returning present value...")
                return self.value
        
        # print("\nCould not find the identifier at the end! Returning default value...")
        return self.defaultValue
    
    def spawn(self, image, posXY):
        self.pos = posXY
        self.image = pygame.transform.scale2x(pygame.image.load(image).convert_alpha())
        self.rect = self.image.get_rect(center = self.pos)


class Player(pygame.sprite.Sprite):
    def __init__(self, name, speed):
        super().__init__()
        self.name = name
        self.speed = speed

        self.points = 0
        self.amtOfPresents = 0
        
        self.pos = pygame.math.Vector2(PLAYER_START_X, PLAYER_START_Y)
        
        self.image = pygame.transform.scale2x(pygame.image.load("/Users/williamisaak/Code/GKW/Asset/Character/SantaRun1.png").convert_alpha()) # Base image
        self.rect = self.image.get_rect(center = self.pos).inflate(-10, -10) #Creates smaller rectangle / hitbox around the image
        
        self.walkingSprites = Animation([pygame.transform.scale2x(pygame.image.load("/Users/williamisaak/Code/GKW/Asset/Character/SantaRun1.png").convert_alpha()),
                                pygame.transform.scale2x(pygame.image.load("/Users/williamisaak/Code/GKW/Asset/Character/SantaRun2.png").convert_alpha()),
                                pygame.transform.scale2x(pygame.image.load("/Users/williamisaak/Code/GKW/Asset/Character/SantaRun3.png").convert_alpha())])
        
        self.direction = "right" # Add a direction 

    def changeSpeed(self, value):
        self.speed = value

    def update(self):
        keys = pygame.key.get_pressed()
        moving = False  # Add a flag to track movement
        if keys[pygame.K_w]:
            self.rect.centery -= self.speed
            self.walkingSprites.animate(0.07, self)
            moving = True  # Set the flag to True when moving up
        if keys[pygame.K_a]:
            self.rect.centerx -= self.speed
            self.walkingSprites.animate(0.07, self)
            self.direction = "left"  # Update direction
            moving = True  # Set the flag to True when moving left
        if keys[pygame.K_s]:
            self.rect.centery += self.speed
            self.walkingSprites.animate(0.07, self)
            moving = True  # Set the flag to True when moving down
        if keys[pygame.K_d]:
            self.rect.centerx += self.speed
            self.walkingSprites.animate(0.07, self)
            self.direction = "right"  # Update direction
            moving = True  # Set the flag to True when moving right

        # Flip the image based on direction and movement
        if moving:  # Only flip the image if the character is moving
            if self.direction == "left":
                self.image = pygame.transform.flip(self.image, True, False)
            elif self.direction == "right":
                self.image = pygame.transform.flip(self.image, False, False)

class block(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.pos = pos # Default position

        self.image = pygame.transform.scale(pygame.image.load("/Users/williamisaak/Code/GKW/Asset/GrassBlock.png").convert_alpha(), (150,150))
        self.rect = self.image.get_rect(center = self.pos)

class Cookies(pygame.sprite.Sprite):
    def __init__(self, name):
        super().__init__()
        self.name = name
        
        self.image = pygame.transform.scale(pygame.image.load("/Users/williamisaak/Code/GKW/Asset/CookiesAndMilk.png").convert_alpha(), (100,100)) # Base image
        self.pos = pygame.math.Vector2()
        self.rect = self.image.get_rect(center = self.pos)
    
    def spawn(self, image, posXY):
        self.pos = posXY
        self.image = pygame.transform.scale2x(pygame.image.load(image).convert_alpha())
        self.rect = self.image.get_rect(center = self.pos)
