import pygame
from player import Player

pygame.init()

class Level():
    "A class to represent a level that can change"
    def __init__(self):
        self.win = False 
        self.level = 1
        self.lost = pygame.image.load("gameover.png")
        self.lostrect = self.lost.get_rect()
        self.lostrect.x = 175
        self.lostrect.y = 113
        self.levelup = pygame.image.load("levelup.png")
        self.leveluprect = self.levelup.get_rect() 
        self.leveluprect.x = 175
        self.leveluprect.y = 113
        self.easy = pygame.image.load("easy_button.png")
        self.easyRect = self.easy.get_rect()
        self.easyRect.x = 225
        self.easyRect.y = 72
        self.medium = pygame.image.load("medium_button.png")
        self.mediumRect = self.medium.get_rect()
        self.mediumRect.x = 225
        self.mediumRect.y = 216
        self.hard = pygame.image.load("hard_button.png")
        self.hardRect = self.hard.get_rect()
        self.hardRect.x = 225
        self.hardRect.y = 360
        self.speed = 0
        
  
    def display_onto_screen(self, pic, picrect, screen):
        "Displays an image onto the screen"
        screen.blit(pic, picrect)
        pygame.display.flip()
        pygame.time.delay(100)
         
    def level_up(self):
        "Increases the level"
        self.level += 1

    def reset(self):
        "Resets the game's level"
        self.level = 1
    #Special feature -- determines difficulty
    def difficulty(self, difficult, player):
        "A method the represents the difficulty of the game -- pass it 1 for easy, 2 for medium, and 3 for hard. Also, pass it a player object -- the difficulty will determine the number of lives the player has."
        #represents the easy difficulty
        if(difficult == 1):
           #Changes the speed to the slowest availible
           self.speed = 5
           #Sets the player's lives to 4
           player.lives = 4
        #Represents the medium difficulty
        elif(difficult == 2):
           #Changes the speed to the second slowest availible
           self.speed = 3
           #Sets the player's lives to 3
           player.lives = 3
        #Represents hard difficulty
        else:
           #Changes the speed to the fastest availible
           self.speed = 2
           #Sets the player's lives to 2
           player.lives = 2

    def controlSpeed(self):
        "Adjusts the speed of the ball"
        pygame.time.delay(self.speed)

    