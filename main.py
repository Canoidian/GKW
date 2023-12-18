# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    main.py                                            :+:    :+:             #
#                                                      +:+                     #
#    By: Kevin Nhan <kenha4996@ugcloud.ca>            +#+                      #
#                                                    +#+                       #
#    Created: 2023/12/13 11:07:56 by williamisaa   #+#    #+#                  #
#    Updated: 2023/12/18 10:47:30 by williamisaa   ########   odam.nl          #
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

class character(pygame.sprite.Sprite):
    def __init__(self, speed, gifts, buffs, name, image, pos):
        super().__init__()
        self.speed = speed
        self.gifts = gifts
        self.buffs = buffs
        self.name = name
        self.image = pygame.image.load("").convert_alpha()
        self.pos = pygame.math.Vector2(PLAYER_START_X, PLAYER_START_Y)
        
#player = Player()

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
    
    # Detects when user holds W key
    if keys[pygame.K_w]:
        print("Holding W key")
    
    screen.blit(background, (0,0)) # To display background
    #screen.blit(player.image, player.pos)
    
    pygame.display.update()
    clock.tick(FPS)