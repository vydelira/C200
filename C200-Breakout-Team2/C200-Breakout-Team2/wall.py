import pygame
from level import Level
from brick import Brick

pygame.init()

class Wall:
    "A class to represent a container that contains brick objects"
    def __init__(self):
        self.bricks = []

    def addBrick(self, Brick):
        "Appends a brick object to the bricks list"
        self.bricks.append(Brick)

    def populate(self, Level, Columns, Value):
        "Populates self.bricks with a number Level.level rows and Columns columns of bricks"
        for row in range(0,Level.level):
            for column in range(0, Columns):
                self.addBrick(Brick(column * 48, row * 48, Value))
    
    def destroyWall(self):
        "Removes all bricks from self.bricks"
        self.bricks = []
        
    def getLowestBrick(self):
        "Returns the lowest brick in self.bricks"
        return self.bricks[-1]