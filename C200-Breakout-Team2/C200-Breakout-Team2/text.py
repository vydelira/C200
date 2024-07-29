import pygame

pygame.init()
#Initializes font for generic text
font = pygame.font.Font(None, 25)

class Text:
    "A class to represent text"
    def __init__(self, message, x, y):
        self.messageTxt = font.render(message, True,  pygame.Color('dodgerblue'))
        self.messageTxtRect = self.messageTxt.get_rect()
        self.messageTxtRect.x = x
        self.messageTxtRect.y = y

    def update_text(self, message):
        "Updates the text"
        self.messageTxt = font.render(message, True,  pygame.Color('dodgerblue'))
        