import pygame
import time

pygame.init()

#Initializes font for timer
font = pygame.font.Font(None, 20)


class Timer:
    "A class to represent the game timer"
    def __init__(self):
        self.startTime = 0
        self.endTime = 0
        self.actualTime = 0
        self.timerTxt =  font.render("Time elapsed: " + str(self.actualTime), True,  pygame.Color('dodgerblue'))
        self.timerTxtRect = self.timerTxt.get_rect()
        self.timerTxtRect.x = 440
        self.timerTxtRect.y = 528

    def startTimer(self):
        "Start the timer"
        self.startTime = time.time()

    def endTimer(self):
        "End the timer"
        self.endTime = time.time()

    def calculateActualTime(self):
        "Calculate the time elapsed"
        self.endTimer()
        self.actualTime = int(self.endTime - self.startTime)
        return self.actualTime

    def updateTimer(self):
        "Update the timer"
        self.timerTxt = font.render("Time elapsed: " + str(self.calculateActualTime()), True,  pygame.Color('dodgerblue'))

    def resetTimer(self):
        "Resets the timer"
        self.startTime = 0
        self.endTime = 0
        self.actualTime = 0