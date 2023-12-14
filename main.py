# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    main.py                                            :+:    :+:             #
#                                                      +:+                     #
#    By: Kevin Nhan <kenha4996@ugcloud.ca>            +#+                      #
#                                                    +#+                       #
#    Created: 2023/12/13 11:07:56 by williamisaa   #+#    #+#                  #
#    Updated: 2023/12/14 09:08:33 by williamisaa   ########   odam.nl          #
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

# Creating window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("12/25") # Name of game
clock = pygame.time.Clock()

# Load images - background ect
# background = pygame.transform.scale(pygame.image.load("").convert(), (WIDTH, HEIGHT)) # Input path to background file

# #Draws a red rectangle at the coords (100,100) on the window
pygame.draw.rect(screen, WHITE, [100,100,150,200])
pygame.display.flip()



while True:
    keys = pygame.key.get_pressed() # Looks at all keys pressed
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Checks if user clicked the exited button
            pygame.quit()
            exit()
    
    #screen.blit(background, (0,0)) # To display background
    
    pygame.display.update()
    clock.tick(FPS)