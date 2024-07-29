import pygame

pygame.init()

class Start():
    "Class displays'start' button. Initializes the game when button is pressed"
    def __init__(self,x,y):
        self.startButton = pygame.image.load("start_button.png")
        self.startButtonRect = self.startButton.get_rect()
        self.startButtonRect.x = x
        self.startButtonRect.y = y

    
