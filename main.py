# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    main.py                                            :+:    :+:             #
#                                                      +:+                     #
#    By: Kevin Nhan <kenha4996@ugcloud.ca>            +#+                      #
#                                                    +#+                       #
#    Created: 2023/12/13 11:07:56 by williamisaa   #+#    #+#                  #
#    Updated: 2023/12/20 11:11:250 by williamisaa   ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

# YT video to help us out
# https://www.youtube.com/watch?v=OUOI6iCrmCk&ab_channel=JCode
# https://www.youtube.com/watch?v=abH2MSBdnWc
#? Libraries
import pygame, math, random

from sys import exit

from functions import *
from settings import *
from classes import *
from menu import *


#* Constants and Variables

#Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (128,128,128)
GREEN = (0,255,0)
CHRISTMAS_GREEN = (60,141,13)
TEAL = (0,128,128)
BROWN = (100,65,23)
RED = (255,0,0)
CHRISTMAS_RED = (214,0,28)
ORANGE = (255,79,0)
YELLOW = (255,240,0)
PINK = (255,105,180)
BLUE = (100,149,237)
LIGHT_BLUE = (173, 216, 230, 1)
PURPLE = (102,51,153)


game_state = "start_menu"

font = "/Users/williamisaak/Code/GKW/Asset/Fonts/Pixeltype.ttf"

#^ Main
done = False
 
pygame.init() #Initializes the window
pygame.font.init()

# Creating window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("12/25") # Name of game
clock = pygame.time.Clock()

#Texts
textFont = pygame.font.Font("/Users/williamisaak/Code/GKW/Asset/Fonts/Pixeltype.ttf", 50)
text = textFont.render("Points: ", False, CHRISTMAS_GREEN)
textRect = text.get_rect(center = (100,50))

# Initializing the player
player = Player(name, speed)

# Presents
presentGroup = pygame.sprite.Group()

# Draws presents on screen (TEMP)
for i in range(1500):
    presentNames = ["small_present","medium_present","large_present", "golden_present"]
    rndPresent = random.randint(0,3)
    present = Present(presentNames[rndPresent]+"_"+str(rndPresent))
    present.spawn("/Users/williamisaak/Code/GKW/Asset/Presents/"+presentNames[rndPresent]+".png",(random.randint(400, 1500),random.randint(400,1500) + 100))
    presentGroup.add(present)

# Load images - background
background = pygame.transform.scale(pygame.image.load("/Users/williamisaak/Code/GKW/Asset/Background/Background.png").convert_alpha(), (WIDTH, HEIGHT)) 

#Camera
class Camera(pygame.sprite.Group):
    def __init__(self):     
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        
        # Camera offset
        self.offset = pygame.math.Vector2()
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2
        
        # Background
        self.ground_surf = background
        self.ground_rect = self.ground_surf.get_rect(topleft = (0,0))
    
    def center_target_camera(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h
    
    def custom_draw(self, player):
        self.center_target_camera(player)

        # Background
        ground_offset = self.ground_rect.topleft - self.offset
        self.display_surface.blit(self.ground_surf, ground_offset)
        
        # Active Elements
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
        

# Adds player and present sprites into the came
cameraGroup = Camera()
cameraGroup.add(player)
cameraGroup.add(presentGroup)

while True:
    keys = pygame.key.get_pressed() # Looks at all keys pressed
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Checks if user clicked the exited button
            pygame.quit()
            exit()
        
    if game_state == "start_menu": # When pygame is run, the default value of the game_state is "start_menu" so it will draw out the start menu
        game_state = main_menu(screen, font, WIDTH, clock, game_state)  # Update game_state
    if game_state == "game":
       
        # Fill the screen with black color
        screen.fill(BLACK)
        
        cameraGroup.update()
        cameraGroup.custom_draw(player)

        player.update() #Updates screen to display player
        screen.blit(textFont.render(f"Points: {player.points}", False, CHRISTMAS_GREEN), textRect)

        #Detects when present is touched
        presentCollision = pygame.sprite.spritecollide(player, presentGroup, True)
        for present in presentCollision:
            player.points += present.getValue()
        
        pygame.display.flip()
        clock.tick(FPS)