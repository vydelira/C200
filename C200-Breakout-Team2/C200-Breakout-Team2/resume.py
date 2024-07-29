import pygame

pygame.init()

class Resume():
    "Displays resume button. Allows player to continue playing where they left off"
    def __init__(self, x, y):
        self.resumeButton = pygame.image.load("resume_button.png")
        self.resumeButtonRect = self.resumeButton.get_rect()
        self.resumeButtonRect.x = x
        self.resumeButtonRect.y = y
