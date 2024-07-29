import pygame
pygame.init()

class Brick:
    "class 'Brick' represents each brick"
    def __init__(self, x, y, value):
        #position of brick
        self.x = x
        self.y = y
        self.value = value
        #creating brick image and bounding box
        self.bric = pygame.image.load("brick.JPEG")
        self.bricrect = self.bric.get_rect()
        #Placing brick in location self.x and self.y
        self.bricrect.x = self.x
        self.bricrect.y = self.y
       #creating a dark brick image and bounding box
        self.dbric = pygame.image.load("darkbrick.png")
        self.dbricrect = self.dbric.get_rect()
        #Placing dark brick in location self.x and self.y
        self.dbricrect.x = self.x
        self.dbricrect.y = self.y
        #creating gold brick image and bounding box
        self.gbric = pygame.image.load("goldbrick.png")
        self.gbricrect = self.bric.get_rect()
        #Placing gold brick in location self.x and self.y
        self.gbricrect.x = self.x
        self.gbricrect.y = self.y
        #creating snow brick image and bounding box
        self.sbric = pygame.image.load("snowbrick.png")
        self.sbricrect = self.bric.get_rect()
        #Placing snow brick in location self.x and self.y
        self.sbricrect.x = self.x
        self.sbricrect.y = self.y
        #Represents the mainBrick (the brick the player choose)
        self.mainBrick = None
        self.mainBrickRect = None

    def changeBrick(self, image, boundingBox):
        self.mainBrick = image
        self.mainBrickRect = boundingBox