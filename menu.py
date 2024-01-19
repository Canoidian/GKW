# Libraries
import pygame, time
from pygame import mixer
from main import *
from settings import *
from functions import *

# Variables
mixer.init()
songs = ["/Users/williamisaak/Code/GKW/Asset/Audio/Spy Exposed.mp3", "/Users/williamisaak/Code/GKW/Asset/Audio/Suite Du Matin.mp3"]

# Main Menu
def main_menu(screen, font, WIDTH, clock, game_state):
    
    # Text Renderer
    def text_format(message, textFont, textSize, textColor):
        newFont = pygame.font.Font(textFont, textSize)
        newText = newFont.render(message, 0, textColor)

        return newText
    
    #Colours
    CHRISTMAS_GREEN = (60,141,13)
    CHRISTMAS_RED = (214,0,28)
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    
    index = 0
    states = ["start", "help", "leaderboard", "quit"]
    selected = "start"

    while game_state == "start_menu":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            # Loops through the states in the list
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    index -= 1
                    if index < 0: # Checks if index is less than 0
                        index = 2
                    selected = states[index]
                    
                elif event.key == pygame.K_s:
                    index += 1
                    if index > len(states) - 1: # Checks if index is greater than the list size
                        index = 0
                    selected = states[index]
                    
                if event.key == pygame.K_RETURN:
                    if selected == "start":
                        timer = defaultTimer + 50 # Resets timer to 120 seconds
                        # Plays game music
                        mixer.music.unload()
                        mixer.music.load(songs[0])   
                        mixer.music.set_volume(1) 
                        mixer.music.play()
                        return "game"
                    
                    if selected == "help":
                        return "help_menu"  # Changed from "help" to "help_menu"
                    if selected == "leaderboard":
                        return "leaderboard"
                    if selected == "quit":
                        pygame.quit()
                        quit()
                        
                        
        # Main Menu Screen
        screen.fill(CHRISTMAS_GREEN)
        
        text_start = text_format("START", font, 75, BLACK)
        text_help = text_format("HELP", font, 75, BLACK)
        text_leaderboard = text_format("LEADERBOARD", font, 75, BLACK)
        text_quit = text_format("QUIT", font, 75, BLACK)
        
        
        title = text_format("12/25", font, 90, CHRISTMAS_RED)
        
        # When you select any of the options in the start menu, it will change the text colour to white or black
        if selected == "start":
            text_start = text_format("START", font, 75, WHITE)
        else:
            text_start = text_format("START", font, 75, BLACK)
            
        if selected == "help":
            text_help = text_format("HELP", font, 75, WHITE)
        else:
            text_help = text_format("HELP", font, 75, BLACK)
            
        if selected == "leaderboard":
            text_leaderboard = text_format("LEADERBOARD", font, 75, WHITE)
        else:
            text_leaderboard = text_format("LEADERBOARD", font, 75, BLACK)
            
        if selected == "quit":
            text_quit = text_format("QUIT", font, 75, WHITE)
        else:
            text_quit = text_format("QUIT", font, 75, BLACK)
        
        title_rect = title.get_rect()
        start_rect = text_start.get_rect()
        help_rect = text_help.get_rect()
        leaderboard_rect = text_leaderboard.get_rect()
        quit_rect = text_quit.get_rect()

        # Main Menu Text
        screen.blit(title, (WIDTH/2 - (title_rect[2]/2), 60))
        screen.blit(text_start, (WIDTH/2 - (start_rect[2]/2), 260))
        screen.blit(text_help, (WIDTH/2 - (help_rect[2]/2), 320))
        screen.blit(text_leaderboard, (WIDTH/2 - (leaderboard_rect[2]/2), 380))
        screen.blit(text_quit, (WIDTH/2 - (quit_rect[2]/2), 440))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("12/25 - Game")
        
def help_menu(screen, font, WIDTH, clock, game_state):
    
    # Text Renderer
    def text_format(message, textFont, textSize, textColor):
        newFont = pygame.font.Font(textFont, textSize)
        newText = newFont.render(message, 0, textColor)

        return newText
    
    #Colours
    DARK_CHRISTMAS_GREEN = (0,110,51)
    CHRISTMAS_RED = (214,0,28)
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    
    index = 0
    selected = "back"

    # Inside the help_menu function
    while game_state == "help_menu":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:  # Change the event type check
                if event.key == pygame.K_RETURN:  # Check for the Enter key
                        return "start_menu"
                    
                        
        screen.fill(DARK_CHRISTMAS_GREEN)

        text_back = text_format("BACK", font, 75, CHRISTMAS_RED)
        text_instructions = text_format("Instructions: Use A & D to move left and right", font, 50, WHITE)
        text_instructions2 = text_format("Use W & S to move up and down", font, 50, WHITE)
        text_instructions3 = text_format("To leave the game press the Escape key", font, 50, WHITE)
        text_instructions4 = text_format("Collect as many presents as possible in the time period", font, 50, WHITE)

        if selected == "back":
            text_back = text_format("BACK", font, 75, CHRISTMAS_RED)

        back_rect = text_back.get_rect()
        instructions_rect = text_instructions.get_rect()
        instructions2_rect = text_instructions2.get_rect()
        instructions3_rect = text_instructions3.get_rect()
        instructions4_rect = text_instructions4.get_rect()
        

        # Help Menu Text
        screen.blit(text_back, (WIDTH/2 - (back_rect[2]/2), 260))
        screen.blit(text_instructions, (WIDTH/2 - (instructions_rect[2]/2), 320))
        screen.blit(text_instructions2, (WIDTH/2 - (instructions2_rect[2]/2), 380))
        screen.blit(text_instructions3, (WIDTH/2 - (instructions3_rect[2]/2), 440))
        screen.blit(text_instructions4, (WIDTH/2 - (instructions4_rect[2]/2), 500))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("12/25 - Help Menu")
        
def pause(screen, font, WIDTH, clock, game_state):
    # Text Renderer
    def text_format(message, textFont, textSize, textColor):
        newFont = pygame.font.Font(textFont, textSize)
        newText = newFont.render(message, 0, textColor)

        return newText
        
    #Colours
    DARK_CHRISTMAS_GREEN = (0,110,51)
    CHRISTMAS_RED = (214,0,28)
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    PLUM = (221,160,221)
    
    index = 0
    states = ["resume", "home", "quit"]
    selected = "resume"
    
    while game_state == "pause":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                    
            # Loops through the states in the list
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    index -= 1
                    if index < 0: # Checks if index is less than 0
                        index = 2
                    selected = states[index]
                    
                elif event.key == pygame.K_DOWN:
                    index += 1
                    if index > len(states) - 1: # Checks if index is greater than the list size
                        index = 0
                    selected = states[index]
                    
                if event.key == pygame.K_RETURN:
                    if selected == "resume":
                        return "game"
                    if selected == "home":
                        # Stops game music and plays menu music
                        mixer.music.stop()
                        mixer.music.unload()
                        mixer.music.load(songs[1])   
                        mixer.music.set_volume(.5) 
                        mixer.music.play()
                        
                        return "start_menu" 
                    if selected == "quit":
                        pygame.quit()
                        quit()
                        
        screen.fill(PLUM)
        
        text_resume = text_format("RESUME", font, 75, BLACK)
        text_home = text_format("HOME", font, 75, BLACK)
        text_quit = text_format("QUIT", font, 75, BLACK)

        if selected == "resume":
            text_resume = text_format("RESUME", font, 75, WHITE)
        else:
            text_resume = text_format("RESUME", font, 75, BLACK)
            
        if selected == "home":
            text_home = text_format("HOME", font, 75, WHITE)
        else:
            text_home = text_format("HOME", font, 75, BLACK)
            
        if selected == "quit":
            text_quit = text_format("QUIT", font, 75, WHITE)
        else:
            text_quit = text_format("QUIT", font, 75, BLACK)
            
        resume_rect = text_resume.get_rect()
        home_rect = text_home.get_rect()
        quit_rect = text_quit.get_rect()
        
        # Pause screen Menu Text
        screen.blit(text_resume, (WIDTH/2 - (resume_rect[2]/2), 260))
        screen.blit(text_home, (WIDTH/2 - (home_rect[2]/2), 320))
        screen.blit(text_quit, (WIDTH/2 - (quit_rect[2]/2), 380))

        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("12/25 - Pause Menu")
        
def game_over(screen, font, WIDTH, clock, game_state, points, amtOfPresents):
    
    # Text Renderer
    def text_format(message, textFont, textSize, textColor):
        newFont = pygame.font.Font(textFont, textSize)
        newText = newFont.render(message, 0, textColor)

        return newText
        
    #Colours
    DARK_CHRISTMAS_GREEN = (0,110,51)
    CHRISTMAS_RED = (214,0,28)
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    CORN_FLOWER = (100,149,237)
    
    index = 0
    states = ["home", "quit"]
    selected = "home"
        
    while game_state == "game_over":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                    
            # Loops through the states in the list
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    index -= 1
                if event.key == pygame.K_DOWN:  # Check for the Down key
                    index += 1  # Increment the index
                    
                if index < 0:  # Check if index is less than 0
                    index = len(states) - 1  # Set index to the last item in the list
                if index >= len(states):  # Check if index is greater than or equal to the length of the list
                    index = 0  # Set index to 0
                    
                selected = states[index]  # Update the selected state based on the index
                    
                if event.key == pygame.K_RETURN:  # Check for the Enter key
                    if selected == "home":
                        return "start_menu"
                    if selected == "quit":
                        pygame.quit()
                        quit()
                        
        screen.fill(CORN_FLOWER)
        
        # Display points and presents
        text_points = text_format(f"Points: {points}", font, 50, WHITE)
        text_presents = text_format(f"Presents Collected: {amtOfPresents}", font, 50, WHITE)
        
        screen.blit(text_points, (WIDTH/2 - (text_points.get_rect()[2]/2), 200))  # Show the points text
        screen.blit(text_presents, (WIDTH/2 - (text_presents.get_rect()[2]/2), 250))  # Show the presents text
        
        # Display menu options
        text_home = text_format("HOME", font, 75, WHITE)
        text_quit = text_format("QUIT", font, 75, WHITE)
        
        if selected == "home":
            text_home = text_format("HOME", font, 75, CHRISTMAS_RED)
        else:
            text_home = text_format("HOME", font, 75, WHITE)
            
        if selected == "quit":
            text_quit = text_format("QUIT", font, 75, CHRISTMAS_RED)
        else:
            text_quit = text_format("QUIT", font, 75, WHITE)
            
        home_rect = text_home.get_rect()
        quit_rect = text_quit.get_rect()
        
        screen.blit(text_home, (WIDTH/2 - (home_rect[2]/2), 350))  # Show the "HOME" text
        screen.blit(text_quit, (WIDTH/2 - (quit_rect[2]/2), 400))  # Show the "QUIT" text
        
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("12/25 - Game Over")
        
def leaderboard(screen, font, WIDTH, clock, game_state):
    # Text Renderer
    def text_format(message, textFont, textSize, textColor):
        newFont = pygame.font.Font(textFont, textSize)
        newText = newFont.render(message, 0, textColor)
        return newText
    
    #Colours
    DARK_CHRISTMAS_GREEN = (0,110,51)
    CHRISTMAS_RED = (214,0,28)
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    
    states = ["back"]
    selected = "back"
    
    while game_state == "leaderboard":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:  # Change the event type check
                if event.key == pygame.K_RETURN:  # Check for the Enter key
                    return "start_menu"
                        
        screen.fill(CHRISTMAS_RED)
        
        text_back = text_format("BACK", font, 75, CHRISTMAS_RED)
        text_leaderboard = text_format("LEADERBOARD", font, 80, WHITE)

                
        screen.blit(text_back, (WIDTH/2 - (text_back.get_rect()[2]/2), 200))  # Show the "BACK" text
        screen.blit(text_leaderboard, (WIDTH/2 - (text_leaderboard.get_rect()[2]/2), 100))  # Show the "LEADERBOARD" text

        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("12/25 - Leaderboard")