import pygame
from main import *
from settings import *
from functions import *


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
    states = ["start","help", "leaderboard", "quit"]
    selected = "start"

    while game_state == "start_menu":
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
                    if selected == "start":
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
        pygame.display.set_caption("12/25 - Game Menu")
        
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
    states = ["back"]
    selected = "back"

    while game_state == "help_menu":  # Changed from "help" to "help_menu"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Loops through the states in the list
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    index = 0
                    selected = states[index]
                    
                if event.key == pygame.K_RETURN:
                    if selected == "back":
                        return "start_menu"
                        
        screen.fill(DARK_CHRISTMAS_GREEN)

        text_back = text_format("BACK", font, 75, BLACK)
        text_instructions = text_format("Instructions: Use A & D to move left and right", font, 50, WHITE)
        text_instructions2 = text_format("Use W & S to move up and down", font, 50, WHITE)
        text_instructions3 = text_format("To leave the game press the Escape key", font, 50, WHITE)
        text_instructions4 = text_format("Collect as many presents as possible in the time period", font, 50, WHITE)

        if selected == "back":
            text_back = text_format("BACK", font, 75, WHITE)
        else:
            text_back = text_format("BACK", font, 75, BLACK)

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