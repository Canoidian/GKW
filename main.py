# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    main.py                                            :+:    :+:             #
#                                                      +:+                     #
#    By: Kevin Nhan <kenha4996@ugcloud.ca>            +#+                      #
#                                                    +#+                       #
#    Created: 2023/12/13 11:07:56 by williamisaa   #+#    #+#                  #
#    Updated: 2023/12/13 11:17:48 by williamisaa   ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

#? Libraries
import pygame

#! Functions


#* Constants and Variables

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)


pygame.init()
size = (700,500)
surface = pygame.display.set_mode(size)

#~Draw Here
pygame.draw.rect(surface, RED, [100,100,150,200])
pygame.display.flip()
#~Stop Draw Here


#^ Main
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
pygame.quit()