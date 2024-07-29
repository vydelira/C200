import pygame     

pygame.init()

class Paddle:
    "A class to represent a paddle that can move."
    def __init__ (self, x, y):
        #paddle position
        self.x = x
        self.y = y
        #Direction of paddle
        self.xdirection = 0
        #Create paddle image + bounding box
        self.padd = pygame.image.load("paddle.png")
        self.paddrect = self.padd.get_rect()
        #Placing paddle in a specific location - self.x and self.y
        self.paddrect.x = self.x
        self.paddrect.y = self.y

    def change_direction(self,x):
        "Change direction (paddle)"
        self.xdirection = x

    
    """def draw(self, surface, color):
        "Draw rectangle (paddle)"
        pygame.draw.rect(surface, color, pygame.Rect(self.x, self.y, 60, 20),0)"""
    
             
    def move(self):
        "Moves the rectangle (paddle)"
        self.x += self.xdirection
        self.paddrect.x = self.x
                                                                                    

    def resetPaddle(self):
        "Resets the position and the direction of the paddle"
        self.x = 312
        self.paddrect.x = self.x
        self.xdirection = 0
 
       
     

