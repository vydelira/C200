import pygame

pygame.init()

class Continue():
    "Represents a 'continue' button"
    def __init__(self, x, y):
        self.continueButton = pygame.image.load("continue_button.png")
        self.continueButtonRect = self.continueButton.get_rect()
        self.continueButtonRect.x = x
        self.continueButtonRect.y = y
