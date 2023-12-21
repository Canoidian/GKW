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


#* Constants and Variables

#Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
LIGHT_BLUE = (173, 216, 230, 1)

game_state = "start_menu"

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
text = textFont.render("Points: ", False, LIGHT_BLUE)
textRect = text.get_rect(center = (100,50))

# Initializing the player
player = Player(name, speed)

# Presents
presentGroup = pygame.sprite.Group()

for i in range(1500):
    presentNames = ["small_present","medium_present","large_present", "golden_present"]
    rndPresent = random.randint(0,3)
    present = Present(presentNames[rndPresent]+"_"+str(rndPresent))
    present.spawn("/Users/williamisaak/Code/GKW/Asset/Presents/"+presentNames[rndPresent]+".png",(random.randint(400, 1500),random.randint(400,1500) + 100))
    presentGroup.add(present)

# Load images - background
background = pygame.transform.scale(pygame.image.load("/Users/williamisaak/Code/GKW/Asset/Background/Background.png").convert_alpha(), (WIDTH, HEIGHT)) 

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

cameraGroup = Camera()
cameraGroup.add(player)
cameraGroup.add(presentGroup)

def draw_start_menu():
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('/Users/williamisaak/Code/GKW/Asset/Fonts/Pixeltype.ttf', 40)
    title = font.render('My Game', True, (255, 255, 255))
    start_button = font.render('Start', True, (255, 255, 255))
    screen.blit(title, (WIDTH/2 - title.get_width()/2, HEIGHT/2 - title.get_height()/2))
    screen.blit(start_button, (WIDTH/2 - start_button.get_width()/2, HEIGHT/2 + start_button.get_height()/2))
    pygame.display.update()

while True:
    keys = pygame.key.get_pressed() # Looks at all keys pressed
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Checks if user clicked the exited button
            pygame.quit()
            exit()
        
    if game_state == "start_menu":
        draw_start_menu()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            player_x = 200
            player_y = 400
            game_state = "game"
            game_over = False
  
    if game_state == "game":
        keys = pygame.key.get_pressed()
       
        # Fill the screen with black color
        screen.fill(BLACK)
        
        #screen.blit(background, (0,0)) # To display background
        cameraGroup.update()
        cameraGroup.custom_draw(player)

        player.update()
        screen.blit(textFont.render(f"Points: {player.points}", False, RED), textRect)

        #Detects when present is touched
        presentCollision = pygame.sprite.spritecollide(player, presentGroup, True)
        for present in presentCollision:
            player.points += present.getValue()
        
        pygame.display.flip()
        clock.tick(FPS)
