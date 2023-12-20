# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    main.py                                            :+:    :+:             #
#                                                      +:+                     #
#    By: Kevin Nhan <kenha4996@ugcloud.ca>            +#+                      #
#                                                    +#+                       #
#    Created: 2023/12/13 11:07:56 by williamisaa   #+#    #+#                  #
#    Updated: 2023/12/19 11:33:46 by williamisaa   ########   odam.nl          #
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
from classes import *


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

# Initializing the player
player = Player(name, speed)

SpriteGroup = pygame.sprite.GroupSingle()
SpriteGroup.add(player)

# Load images - background
background = pygame.transform.scale(pygame.image.load(backgroundImg).convert(), (WIDTH, HEIGHT)) 

class Camera(pygame.sprite.Group):
    def __init__(self, player, sprite_group):
        super().__init__()
        self.player = player
        self.sprite_group = sprite_group
        self.offset = pygame.math.Vector2()
        self.floor_rect = background.get_rect(topleft = (0, 0))

    def custom_draw(self):
        self.offset.x = self.player.rect.centerx - WIDTH // 2
        self.offset.y = self.player.rect.centery - HEIGHT // 2

        # draw the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        screen.blit(background, floor_offset_pos)

        for sprite in self.sprite_group:
            offset_pos = sprite.rect.topleft - self.offset
            screen.blit(sprite.image, offset_pos)

camera = Camera(player, SpriteGroup)

while True:
    keys = pygame.key.get_pressed() # Looks at all keys pressed
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Checks if user clicked the exited button
            pygame.quit()
            exit()
    
    # Detects when user holds A key
    if keys[pygame.K_a]:
        player.move(-1*player.speed, "x")
    # Detects when user holds D key
    if keys[pygame.K_d]:
        player.move(player.speed, "x")

    # Detects when user holds W key
    if keys[pygame.K_w]:
        player.move(-1*player.speed, "y")
    # Detects when user holds S key
    if keys[pygame.K_s]:
        player.move(player.speed, "y")
    
    #screen.blit(background, (0,0)) # To display background
    camera.custom_draw()
    
    pygame.display.flip()
    clock.tick(FPS)
