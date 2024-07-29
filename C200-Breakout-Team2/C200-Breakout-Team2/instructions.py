import pygame


pygame.init()

class Instructions():
    "A class that displays an 'Instructions' button"
    "Display image with instructions when button is clicked"
    def __init__(self, x, y):
        self.instructionButton = pygame.image.load("instructions_button.png")
        self.instructionButtonRect = self.instructionButton.get_rect()
        self.instructionButtonRect.x = x
        self.instructionButtonRect.y = y
        self.instructionsImg = pygame.image.load("instructions.jpg")
        self.instructionsImgRect = self.instructionsImg.get_rect()
        


