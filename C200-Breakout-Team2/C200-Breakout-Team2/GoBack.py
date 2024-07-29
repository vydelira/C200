import pygame

pygame.init()

class Return():
    "Class displays 'return' button and its position; returns user to the game when paused"
    def __init__(self, x, y):
        self.returnButton = pygame.image.load("return_button.png")
        self.returnButtonRect = self.returnButton.get_rect()
        self.returnButtonRect.x = x
        self.returnButtonRect.y = y

