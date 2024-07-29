import pygame
from text import Text
pygame.init()

class Highscore:
    "Class to represent things related tot the highscore"
    def __init__(self, x, y):
        self.highscoreButton = pygame.image.load("highscore_button.png")
        self.highscoreButtonRect = self.highscoreButton.get_rect()
        self.highscoreButtonRect.x = x
        self.highscoreButtonRect.y = y
        self.highscores = []
        self.fileLocation = "highscores.txt"

    def isHighScore(self, score):
        "Removes the lowest score from self.highscores. If the variable score is not the smallest value, this function returns True (score is a highscore in this case)."
        print(score)
        min = int(score)
        for score2 in self.highscores:
            if(int(score2[1]) < int(min)):
                lowest = score2
                min = score2[1]
        if(min != score):
            self.highscores.remove(lowest)
        return score != min

    def addHighScore(self, name, score):
        "Adds the a list == [name, score] to self.highscores"
        self.populate()
        if(len(self.highscores) < 10):
            self.highscores.append([name, score])
        else:
            if(self.isHighScore(score)):
                self.highscores.append([name, score])

    def sortScores(self):
        "Uses selection sort to sort the list of highscores"
        #A list of all of the numbers in self.highscores
        #Used because self.highscores is a list of list -- only its scores are needed
        numbers = []
        for ele in self.highscores:
            numbers += [int(ele[1])]
        i = 0
        #loop to sort the highscores
        while i < len(numbers):
        #obtains the largest element in the sublist  
            largest = max(numbers[i:]) 
        #index of the largest element
            index_of_largest = numbers[i:].index(largest) + i
        #swaps the position of the values in each list
            lower = numbers[i]
            higher = numbers[index_of_largest]
            numbers[i] = higher
            numbers[index_of_largest] = lower
            self.highscores[i],self.highscores[index_of_largest] = self.highscores[index_of_largest],self.highscores[i]
            i += 1
        
    def read_from_file(self):
        "Reads each line in the file, and then puts its contents into a list"
        self.highscores = []
        rawData = []
        with open(self.fileLocation, 'r') as file:
            for line in file:
                temp = line.strip()
                rawData.append(temp.split(" "))
        return rawData

    def displayHighScore(self, screen):
        "Displays the highscore onto the screen"
        temp = self.read_from_file()
        count = 30
        for line in temp:
                textTemp = Text(line[0] + " " + line[1] + " " + line[2], 0, 1 * count)
                screen.blit(textTemp.messageTxt, textTemp.messageTxtRect)
                count += 30
    
    def populate(self):
        "Populates the highscores"
        #Filters the data list -- removes all ists containing empty strings
        count2 = 0
        data = self.read_from_file()
        while(count2 < len(data)):
            for elee in data[count2]:
                if(elee == ""):
                    data.pop(count2)
                    count2 -= 1
                    break
            count2 += 1
        count = 0
        #Adds a list containing the name and score of each player for each highscore
        for datum in data:
            self.highscores.append([datum[1],datum[2]])
        #Filters the self.highscores list -- removes all lists containing empty strings within self.highscores.
        while(count < len(self.highscores)):
            for ele in self.highscores[count]:
                if(ele == ""):
                    self.highscores.pop(count)
                    count -= 1
                    break
            count += 1
        

    def write_to_file(self):
        "Writes the highscores to a file"
        count = 1
        #Sorts self.highscores in asscending order
        self.sortScores()
        with open(self.fileLocation,'w') as file:
            for high in self.highscores:
                file.write(str(count) + " " + high[0] + " " + str(high[1]) + "\n")
                count += 1

   