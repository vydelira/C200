import pygame

pygame.init()
#Initializes font for life and score
font = pygame.font.Font(None, 20)

class Player:
    "A class to represent a player"
    def __init__(self, lives):
         self.lives = lives
         self.totalLives = lives
         self.score = 0
         self.livesTxt = font.render("Lives remaining: " + str(self.lives), True,  pygame.Color('dodgerblue'))
         self.livesTxtRect = self.livesTxt.get_rect()
         self.livesTxtRect.x = 50
         self.livesTxtRect.y = 528
         self.scoreTxt =  font.render("Score: " + str(self.score), True,  pygame.Color('dodgerblue'))
         self.scoreTxtRect = self.scoreTxt.get_rect()
         self.scoreTxtRect.x = 270
         self.scoreTxtRect.y = 528
    def increase_score(self, time, bricksRemaining):
        "Increases the score of the player. The score is determined after every level by the number of bricks remaining multiplied by 50 subtracted by the time divided by two casted to the nearest integer towards zero (in seconds since last epoch)."
        self.score += (bricksRemaining * 50) - (int(time * 0.5))
    
    def reset_score(self):
        "Resets the score"
        self.score = 0

    def decrease_life(self):
        "Decreases the number of lives of the player by 1"
        self.lives -= 1
        #returns True if the player is out of lives
        return self.lives == 0

    def reset_lives(self):
        "Resets the number of lives of the player"
        self.lives = self.totalLives

    def updateLifeText(self):
        "Updates the text representing the number of lives the player has"
        self.livesTxt = font.render("Lives remaining: " + str(self.lives), True,  pygame.Color('dodgerblue'))

    def updateScoreText(self):
        "Updates the text representing the player's score"
        self.scoreTxt =  font.render("Score: " + str(self.score), True,  pygame.Color('dodgerblue'))