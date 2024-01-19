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
from pygame import mixer

from sys import exit

from settings import *
from classes import *
from menu import *
from map import *


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

pointText = textFont.render("Points: ", False, CHRISTMAS_GREEN)
pointsRect = pointText.get_rect(center = (100,50))

presentText = textFont.render("Presents Collected: ", False, CHRISTMAS_RED)
presentsRect = pointText.get_rect(center = (100,100))

# Note: This is an important element in the game, there is a set timer for the amount of time to collect presents
timerText = textFont.render("#:##", False, WHITE)
timerRect = timerText.get_rect(center = (1000, 50))

#Sounds
coin_sound = pygame.mixer.Sound("/Users/williamisaak/Code/GKW/Asset/Audio/CoinSound.mp3")
coin_sound.set_volume(.4)
gold_coin_sound = pygame.mixer.Sound("/Users/williamisaak/Code/GKW/Asset/Audio/CoinSound.mp3")
gold_coin_sound.set_volume(1)

# Initializing the player
player = Player(name, speed)

# Load images - background
#background = pygame.transform.scale(pygame.image.load("/Users/williamisaak/Code/GKW/Asset/Background/BackgroundOrange.png").convert_alpha(), (WIDTH, HEIGHT)) 

#Camera
class Camera(pygame.sprite.Group):
    def __init__(self):     
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        
        # Camera offset
        self.offset = pygame.math.Vector2()
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2
    
    def center_target_camera(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h
    
    def custom_draw(self, player):
        self.center_target_camera(player)
        
        # Active Elements
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
        

# Initializing groups
cameraGroup = Camera()
presentGroup = pygame.sprite.Group()
blockGroup = pygame.sprite.Group()

# Tilemap
defaultSize = 151

y = 0
presentNames = ["small_present","medium_present","large_present", "golden_present"]
totalPresents = 0

for row in tileMap:
    x = 0
    for col in row:
        # Adds in the walls
        if col == "W":
            blockGroup.add(block((x,y)))
            
        # Adds in the presents
        elif col == "P":
            rndPresent = random.randint(0,2)
            present = Present(presentNames[rndPresent]+"_"+str(rndPresent))
            present.spawn("/Users/williamisaak/Code/GKW/Asset/Presents/"+presentNames[rndPresent]+".png",(x,y))
            presentGroup.add(present)
            totalPresents += 1
        elif col == "G":
            present = Present("golden_present_3")
            present.spawn("/Users/williamisaak/Code/GKW/Asset/Presents/golden_present.png",(x,y))
            presentGroup.add(present)
            totalPresents += 1

        x += defaultSize
    y += defaultSize

cameraGroup.add(player)
cameraGroup.add(blockGroup)
cameraGroup.add(presentGroup)

# Start music (menu music)
mixer.init()
mixer.music.load("/Users/williamisaak/Code/GKW/Asset/Audio/Suite Du Matin.mp3")
mixer.music.set_volume(.5)
mixer.music.play()

while True:
    keys = pygame.key.get_pressed() # Looks at all keys pressed
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Checks if user clicked the exited button
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_state = "pause"
    
    # All game states
    if game_state == "start_menu": # When pygame is run, the default value of the game_state is "start_menu" so it will draw out the start menu
        game_state = main_menu(screen, font, WIDTH, clock, game_state)  # Update game_state
        
    if game_state == "pause":
        game_state = pause(screen, font, WIDTH, clock, game_state)
        
    if game_state == "game_over":
        game_state = game_over(screen, font, WIDTH, clock, game_state, player.points, player.amtOfPresents)
        
    if game_state == "help_menu":
        game_state = help_menu(screen, font, WIDTH, clock, game_state)
        
    if game_state == "leaderboard":
        game_state = leaderboard(screen, font, WIDTH, clock, game_state)
        
    if game_state == "game":
        # Background colour
        screen.fill((28, 95, 51))
        
        cameraGroup.custom_draw(player)

        player.update() #Updates screen to display player
        
        # Displays points and presents collected
        screen.blit(textFont.render(f"Points: {player.points}", False, CHRISTMAS_GREEN), pointsRect)
        screen.blit(textFont.render(f"Presents Collected: {player.amtOfPresents}", False, CHRISTMAS_RED), presentsRect)

        # Displays timer
        minutes = int(timer // 60) # Figures out how much time there is
        seconds = timer % 60
        
        if minutes == 0: # When minutes is 0, it will only show the seconds
            if seconds < 10: # For formatting the seconds correctly
                time = f"0{round(seconds,2)}"
            else:
                time = f"{round(seconds,2)}"
            screen.blit(textFont.render(time, False, CHRISTMAS_RED), timerRect)
        else:
            if seconds < 10:
                time = f"{minutes}:0{int(seconds)}"
            else:
                time = f"{minutes}:{int(seconds)}"
            screen.blit(textFont.render(time, False, WHITE), timerRect)

        timer -= 1 / FPS # Counts down

        if timer <= 0: # When the timer hits 0
            with open('points_presents.txt', 'a') as file:
                file.write(f"\nPoints: {player.points}\n")
                file.write(f"Presents Collected: {player.amtOfPresents}\n")
            game_state = "game_over" # Changes state so it will display the game_over screen
            timer = defaultTimer  # Reset the timer to the default value to prevent crashing
        
        # Collisions
        presentCollision = pygame.sprite.spritecollide(player, presentGroup, True)
        
        for present in presentCollision: # When player touches a present
            player.points += present.getValue()
            player.amtOfPresents += 1

            # Plays sound effect
            mixer.music.pause()
            if present.getValue() == 500: # Special sound effect for golden present
                mixer.Sound.play(gold_coin_sound)
            else:
                mixer.Sound.play(coin_sound)
            mixer.music.unpause()
            
            
        blockCollision = pygame.sprite.spritecollide(player, blockGroup, False)

        for blockTile in blockCollision: # This will push the player away from the block, which will mimic wall collision 
            if blockTile.pos[0] - player.rect.centerx < 3: # On the X-axis
                player.rect.centerx += player.speed*2
            else:
                player.rect.centerx -= player.speed*2
                    
            if blockTile.pos[1] - player.rect.centery < 3: # On the Y-axis
                player.rect.centery += player.speed*2
            else:
                player.rect.centery -= player.speed*2

        # Updates screen
        pygame.display.flip()
        clock.tick(FPS)
