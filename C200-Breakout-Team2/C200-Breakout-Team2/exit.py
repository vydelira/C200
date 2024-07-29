import pygame

pygame.init()

class Exit:
    "Class loads 'Exit' button. Exits game when button is clicked"
    def __init__(self, x, y):
        self.exitButton = pygame.image.load("exit_button.png")
        self.exitButtonRect = self.exitButton.get_rect()
        self.exitButtonRect.x = x
        self.exitButtonRect.y = y