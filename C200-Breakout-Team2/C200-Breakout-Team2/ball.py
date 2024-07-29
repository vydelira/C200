import pygame
import random
import math

pygame.init()

class Ball:
    "A class to represent a moving ball."
    def __init__(self):
        #position of ball
        self.x = 320
        self.y = 200     
        #direction of ball
        self.polarDirection = random.randint(180,360) * (math.pi/180) * -1
        self.xdirection = math.cos(self.polarDirection)
        self.ydirection = math.sin(self.polarDirection)
        #create image ball and its bounding box
        self.bal = pygame.image.load("ball.JPEG")
        self.balrect = self.bal.get_rect()
        #putting ball in the location of self.x and self.y
        self.balrect.x = self.x
        self.balrect.y = self.y

    def change_direction(self,angle):
        "Changes the direction of the ball. The coordinates are denoted by the variables 'x' and 'y'."
        self.polarDirection = angle * (math.pi/180)
        self.xdirection = math.cos(self.polarDirection)
        self.ydirection = math.sin(self.polarDirection)
    
    def move(self):
        "Moves the ball in its direction."
        self.x += self.xdirection
        self.y += self.ydirection
        self.balrect.x = self.x
        self.balrect.y = self.y

    def resetBall(self):
        "Resets the position and direction of the ball"
        self.x = 320
        self.y = 200
        self.polarDirection = random.randint(180,360) * (math.pi/180) * -1
        self.xdirection = math.cos(self.polarDirection)
        self.ydirection = math.sin(self.polarDirection)

 
       
        
   
