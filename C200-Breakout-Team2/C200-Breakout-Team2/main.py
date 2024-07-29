import pygame, sys
from ball import Ball
from brick import Brick
from paddle import Paddle
from wall import Wall
from level import Level
from player import Player
from start import Start
from instructions import Instructions
from exit import Exit
from highScore import Highscore
from GoBack import Return as ReturnButton
from resume import Resume
from continuee import Continue
from timer import Timer
from text import Text
from highScore import Highscore
import random
import time

#Initializes pygame library
pygame.init()

#initializes sound -- the game's sound is a special feature
#The ball makes a slap sound whenever it hits something  
woosh = pygame.mixer.Sound("woosh.wav")
#A song that plays when a level is completed
complete = pygame.mixer.Sound("triumph.wav")
#A soung that plays when a player loses a life or the game
defeat = pygame.mixer.Sound("defeat.wav")
#Dimensions of the display
width, height = 624, 600
#Colors
black = (0,0,0)
white = (255,255,255)
#Create display
screen = pygame.display.set_mode((width, height))
screen2 = pygame.display.set_mode((width, height))
#Instatiate various objects
ball2 = Ball()
paddle2 = Paddle(width//2 - 40, 500)
#used for generic brick
brick2 = Brick(225,72,50)
#used for snow brick
brickS = Brick(225, 216,50)
#used for dark brick
brickD = Brick(225,360,50)
#used for gold brick
brickG = Brick(225, 504,50)

wall2 = Wall()
start2 = Start(225, 72)
instructions2 = Instructions(225, 216)
level2 = Level()
timer2 = Timer()
resume2 = Resume(225, 504)
highscore2 = Highscore(225, 360)
continue2 = Continue(225, 37)
continue3 = Continue(225, 300)
return2 = ReturnButton(225, 504)
exit2 = Exit(225,504)
text2 = Text("You may have obtained a highscore -- please enter your initials: ", 0, height//2)
text3 = Text("Highscores", 0, 0)
text4 = Text("Choose a brick:", 0, 0)
text5 = Text("Choose difficulty:", 0, 0)
player2 = Player(3)
#Controls type of brick presented
mainBrick = None
mainBrickRect = None
#A flag to control the loop that determines whether the main menu appears
flag = True

#Adds brick objects to the list contained in the wall2 object
wall2.populate(level2,int(width/48),50)
#A flag to control a new game
brickFlag = False
#Sets the location of the ball between the lowest brick and the paddle
lowestBrick = wall2.getLowestBrick()
xLoc = paddle2.paddrect.x
yLoc = random.randint(lowestBrick.bricrect.y + 48, paddle2.paddrect.y - 48)
ball2.balrect.x = xLoc
ball2.balrect.y = yLoc

 


# While loop for running the game
while(1):
     #Generates a new wall corresponding to the current level
     if(brickFlag):
         wall2.destroyWall()
         ball2.resetBall()
         wall2.populate(level2, int(width/48), 50)
         brickFlag = False
    # While loop for main menu
     while(flag):
         #Checks to see what the player has clicked
         for event in pygame.event.get():
             #If the player attempts to close the window, the program stops running
             if event.type == pygame.QUIT:
                 sys.exit()
             #Checks which button the player has pressed
             elif event.type == pygame.MOUSEBUTTONDOWN:
                 (mouseX, mouseY) = pygame.mouse.get_pos()
                 #The game starts if the player pressed the start button
                 if((mouseX >= start2.startButtonRect.x and mouseX <= (start2.startButtonRect.x + 192)) and (mouseY >= start2.startButtonRect.y and mouseY <= start2.startButtonRect.y + 48)):
                    #A flag to control the loop for the difficulty screen
                    difficultyFlag = True
                     #The loop for the difficulty screen 
                     #It keeps on running until the player closes the window or clicks a difficulty button
                     #This is a special feature that allows the player to choose a difficulty
                    while(difficultyFlag):
                        #Checks to see what the player has clicked
                        for event in pygame.event.get():
                            #If the player attempts to close the window, the program stops running
                            if event.type == pygame.QUIT:
                                sys.exit()
                            #The game is started once the player clicks on a difficulty button
                            elif event.type == pygame.MOUSEBUTTONDOWN:
                                (mouseX2, mouseY2) = pygame.mouse.get_pos()
                                #Checks to see if easy button was pressed -- responds accordingly
                                if(mouseX2 >= level2.easyRect.x and mouseX2 <= (level2.easyRect.x + 192)) and (mouseY2 >= level2.easyRect.y and mouseY2 <= level2.easyRect.y + 48):
                                    level2.difficulty(1, player2)
                                    difficultyFlag = False
                                #Checks to see if medium button was pressed -- responds accordingly
                                elif(mouseX2 >= level2.mediumRect.x and mouseX2 <= (level2.mediumRect.x + 192)) and (mouseY2 >= level2.mediumRect.y and mouseY2 <= level2.mediumRect.y + 48):
                                    level2.difficulty(2, player2)
                                    difficultyFlag = False
                                 #Checks to see if hard button was pressed -- responds accordingly
                                elif(mouseX2 >= level2.hardRect.x and mouseX2 <= (level2.hardRect.x + 192)) and (mouseY2 >= level2.hardRect.y and mouseY2 <= level2.hardRect.y + 48):
                                    level2.difficulty(3, player2)
                                    difficultyFlag = False
                         
                        #The entire screen turns white
                        screen.fill(white)
                        #Displays the easy button onto the screen
                        screen.blit(level2.easy, level2.easyRect)
                        #Display "Highscore" at top of the screen
                        screen.blit(text5.messageTxt, text5.messageTxtRect)
                        #Displays the medium button onto the screen
                        screen.blit(level2.medium, level2.mediumRect)
                        #Displays the hard button onto the screen
                        screen.blit(level2.hard, level2.hardRect)
                        #Renders the screen
                        pygame.display.flip()
                     #The loop for the brick selection screen <----- a special feature
                     #It keeps on running until the player closes the window or clicks a brick image
                     #This is a special feature that allows the player to choose which brick they play with
                    choiceFlag = True
                    #Used to keep track of brick type
                    brickIdentifier = 0
                    while(choiceFlag):
                        #Checks to see what the player has clicked
                        for event in pygame.event.get():
                            #If the player attempts to close the window, the program stops running
                            if event.type == pygame.QUIT:
                                sys.exit()
                            #The game is started once the player clicks on a difficulty button
                            elif event.type == pygame.MOUSEBUTTONDOWN:
                                (mouseX2, mouseY2) = pygame.mouse.get_pos()
                                #Checks to see if generic brick image was pressed -- responds accordingly -- brick identifier is set to 0
                                if(mouseX2 >= brick2.bricrect.x and mouseX2 <= (brick2.bricrect.x + 192)) and (mouseY2 >= brick2.bricrect.y and mouseY2 <= brick2.bricrect.y + 48):
                                    brickIdentifier = 0
                                    choiceFlag = False
                                #Checks to see if snow brick image was pressed -- responds accordingly -- brick identifier is set to 1
                                elif(mouseX2 >= brickS.sbricrect.x and mouseX2 <= (brickS.sbricrect.x + 192)) and (mouseY2 >= brickS.sbricrect.y and mouseY2 <= brickS.sbricrect.y + 48):
                                    brickIdentifier = 1
                                    choiceFlag = False
                                 #Checks to see if dark brick image was pressed -- responds accordingly -- brick identifier is set to 2
                                elif(mouseX2 >= brickD.dbricrect.x and mouseX2 <= (brickD.dbricrect.x + 192)) and (mouseY2 >= brickD.dbricrect.y and mouseY2 <= brickD.dbricrect.y + 48):
                                    brickIdentifier = 2
                                    choiceFlag = False
                                #Checks to see if gold brick image was pressed -- responds accordingly -- brick identifier is set to 3
                                elif(mouseX2 >= brickG.gbricrect.x and mouseX2 <= (brickG.gbricrect.x + 192)) and (mouseY2 >= brickG.gbricrect.y and mouseY2 <= brickG.gbricrect.y + 48):
                                    brickIdentifier = 3
                                    choiceFlag = False
                        #The entire screen turns white
                        screen.fill(white)
                        #Display message prompting player to choose a brick at the top of the screen
                        screen.blit(text4.messageTxt, text4.messageTxtRect)
                        #Displays the generic brick onto the screen
                        screen.blit(brick2.bric, brick2.bricrect)
                        #Displays the snow brick onto the screen
                        screen.blit(brickS.sbric, brickS.sbricrect)
                        #Displays the dark brick onto the screen
                        screen.blit(brickD.dbric, brickD.dbricrect)
                        #Displays the gold brick onto the screen
                        screen.blit(brickG.gbric, brickG.gbricrect)
                        #Renders the screen
                        pygame.display.flip()
                    flag = False
                    #Resets the player's score
                    player2.reset_score()
                    #Starts the level timer
                    timer2.startTimer()
                    break
                 #The instructions appear if the player pressed the instructions button
                 elif((mouseX >= instructions2.instructionButtonRect.x and mouseX <= (instructions2.instructionButtonRect.x + 192)) and (mouseY >= instructions2.instructionButtonRect.y and mouseY <= instructions2.instructionButtonRect.y + 48)):
                     flag2 = True
                     #The loop for the instructions screen
                     #It keeps on running until the player closes the window or clicks the return button
                     while(flag2):
                        #Checks to see what the player has clicked
                        for event in pygame.event.get():
                            #If the player attempts to close the window, the program stops running
                            if event.type == pygame.QUIT:
                                sys.exit()
                            #The player is returned to the menu screen if they pressed the return button
                            elif event.type == pygame.MOUSEBUTTONDOWN:
                                (mouseX2, mouseY2) = pygame.mouse.get_pos()
                                if(mouseX2 >= return2.returnButtonRect.x and mouseX2 <= (return2.returnButtonRect.x + 192)) and (mouseY2 >= return2.returnButtonRect.y and mouseY2 <= return2.returnButtonRect.y + 48):
                                    flag2 = False
                     
                        #The entire screen turns white
                        screen.fill(white)
                        #Displays the instructions onto the screen
                        screen.blit(instructions2.instructionsImg, instructions2.instructionsImgRect)
                        #Displays the return button onto the screen
                        screen.blit(return2.returnButton, return2.returnButtonRect)
                        #Renders the screen
                        pygame.display.flip()
                #The highscores are displayed if the player clicks on the highscore
                 elif((mouseX >= highscore2.highscoreButtonRect.x and mouseX <= (highscore2.highscoreButtonRect.x + 192)) and (mouseY >= highscore2.highscoreButtonRect.y and mouseY <= highscore2.highscoreButtonRect.y + 48)):
                     flag3 = True
                     #The loop for the highscores screen
                     #It keeps on running until the player closes the window or clicks the return button
                     while(flag3):
                        #Checks to see what the player has clicked
                        for event in pygame.event.get():
                            #If the player attempts to close the window, the program stops running
                            if event.type == pygame.QUIT:
                                sys.exit()
                            #The player is returned to the menu screen if they pressed the return button
                            elif event.type == pygame.MOUSEBUTTONDOWN:
                                (mouseX2, mouseY2) = pygame.mouse.get_pos()
                                if(mouseX2 >= return2.returnButtonRect.x and mouseX2 <= (return2.returnButtonRect.x + 192)) and (mouseY2 >= return2.returnButtonRect.y and mouseY2 <= return2.returnButtonRect.y + 48):
                                    flag3 = False
                         
                        #The entire screen turns white
                        screen.fill(white)
                        #Display "Highscore" at top of the screen
                        screen.blit(text3.messageTxt, text3.messageTxtRect)
                        #Displays highscores
                        highscore2.displayHighScore(screen)
                        #Displays the return button onto the screen
                        screen.blit(return2.returnButton, return2.returnButtonRect)
                        #Renders the screen
                        pygame.display.flip()

                 #The program ends if the player clicks the exit button      
                 elif((mouseX >= exit2.exitButtonRect.x and mouseX <= (exit2.exitButtonRect.x + 192)) and (mouseY >= exit2.exitButtonRect.y and mouseY <= exit2.exitButtonRect.y + 48)):
                     sys.exit()
                   
         #The entire screen turns white                  
         screen.fill(white)
         #Displays the start button onto the screen
         screen.blit(start2.startButton, start2.startButtonRect)
         #Displays the instructions button onto the screen
         screen.blit(instructions2.instructionButton, instructions2.instructionButtonRect)
         #Displays the highscore button onto the screen
         screen.blit(highscore2.highscoreButton, highscore2.highscoreButtonRect)
         #Displays the exit button onto the screen
         screen.blit(exit2.exitButton, exit2.exitButtonRect)
         #Renders the screen
         pygame.display.flip()
     #if(ball2.balrect.x < width - 17):
     ball2.move()
     for event in pygame.event.get():
         #Quits the game if the user closes the GUI
          if event.type == pygame.QUIT: 
            sys.exit()
          #Moves the paddle to the right if the right arrow key is pressed
          elif (pygame.key.get_pressed()[pygame.K_RIGHT]) and (paddle2.x < width - 100):
            print(paddle2.x)
            paddle2.change_direction(20)
            paddle2.move()
          #Moves the paddle to the left if the left arrow key is pressed
          elif (pygame.key.get_pressed()[pygame.K_LEFT]) and (paddle2.x > 0):
            paddle2.change_direction(-20)
            paddle2.move()
     
     
     #Checks to see if the ball hit the paddle. If it has, the ball bounces off of the paddle in a direction that depends on where the ball hit the paddle.
     if(ball2.balrect.y == paddle2.paddrect.y - 16 and (ball2.balrect.x <= paddle2.paddrect.x + 96 and ball2.balrect.x >= paddle2.paddrect.x)):
        #the ball makes a slap noise
        woosh.play(0)
        #Mentally divide the paddle into 8 intervals (0 to 12, 12 to 24, 24 to 36, 36 to 48, 48 to 60, 60 to 72, 72 to 84, and 84 to 96))
        #Pretend everyone on of those numbers is added by paddle2.paddrect.x
        #The ball goes straight up if the ball it the paddle in the center
        if(ball2.balrect.x == paddle2.paddrect.x + 48):
            ball2.change_direction(-90)
        #The ball bounces at a 150 degree angle if the ball hit the paddle within the interval 36 (inclusive) to 48:
        elif(ball2.balrect.x < paddle2.paddrect.x + 48 and ball2.balrect.x >= paddle2.paddrect.x + 36):
            ball2.change_direction(-150)
        #The ball bounces at a 135 degree angle if the ball hit the paddle within the interval 24 (inclusive) to 36:
        elif(ball2.balrect.x < paddle2.paddrect.x + 36 and ball2.balrect.x >= paddle2.paddrect.x + 24):
            ball2.change_direction(-135)
        #The ball bounces at a 120 degree angle if the ball hit the paddle within the interval 12 (inclusive) to 24:
        elif(ball2.balrect.x < paddle2.paddrect.x + 24 and ball2.balrect.x >= paddle2.paddrect.x + 12):
            ball2.change_direction(-120)
        #The ball bounces at a 105 degree angle if the ball hit the paddle within the interval 0 (inclusive) to 12:
        elif(ball2.balrect.x == paddle2.paddrect.x and ball2.balrect.x < paddle2.paddrect.x + 12):
            ball2.change_direction(-105)
        #The ball bounces at a 60 degree angle if the ball hit the paddle within the interval 48 to 60 (inclusive):
        elif(ball2.balrect.x <= paddle2.paddrect.x + 60 and ball2.balrect.x > paddle2.paddrect.x + 48):
            ball2.change_direction(-60)
        #The ball bounces at a 45 degree angle if the ball hit the paddle within the interval 60 to 72 (inclusive):
        elif(ball2.balrect.x <= paddle2.paddrect.x + 72 and ball2.balrect.x > paddle2.paddrect.x + 60):
            ball2.change_direction(-45)
        #The ball bounces at a 30 degree angle if the ball hit the paddle within the interval 72 to 84 (inclusive):
        elif(ball2.balrect.x <= paddle2.paddrect.x + 84 and ball2.balrect.x > paddle2.paddrect.x + 72):
            ball2.change_direction(-30)
        #The ball bounces at a 15 degree angle if the ball hit the paddle within the interval 84 to 96 (inclusive):
        elif(ball2.balrect.x == paddle2.paddrect.x + 96 and ball2.balrect.x < paddle2.paddrect.x + 84):
            ball2.change_direction(-15)
        #For any other case not covered
        else:
            ball2.change_direction(-105)
     #If the ball hits the left wall, it bounces at a 60 or -60 degree angle depending on the current polar direction of the ball
     elif(ball2.balrect.x == 0):
        #The ball makes a sound if it hits the left wall
        woosh.play(0)
        if(ball2.polarDirection < 0):
            ball2.change_direction(-60)
        else:
            ball2.change_direction(60)
     #If the ball hits the right wall, it bounces at a 150 or -150 degree angle depending on the current polar direction of the ball
     elif(ball2.balrect.x == (width - 17)):
         #The ball makes a sound if it hits the right wall
         woosh.play(0)
         if(ball2.polarDirection < 0):
             ball2.change_direction(-150)
         else:
            ball2.change_direction(150)
    #If the ball hits the bottom of the screen, the ball and paddle reset position and direction, and the player loses a life.
     elif(ball2.balrect.y == (height)):
         #Sound of defeat plays when a player loses a life
         defeat.play(0)
         paddle2.resetPaddle()
         ball2.resetBall()
         nextLifeFlag = True
         #If the player is out of lives, everything on the screen disappears and a game over image is displayed on the screen. 
         if(player2.decrease_life()):
             #records time elapsed after level completion
             timer2.calculateActualTime()
     
             #reset the timer
             timer2.resetTimer()
             #Reset the level number, number of player lives, and then display that the player has lost
             level2.reset()
             player2.reset_lives()
             level2.display_onto_screen(level2.lost, level2.lostrect, screen)
             pygame.time.delay(2000)
             #Go back to the reset game loop, main menu loop, and skip the continue loop
             flag = True
             brickFlag = True
             nextLifeFlag = False
             highscoreFlag = True
             #String to represent player's initials
             initials = ""
             #Represents the txt for the initials
             initialsTxt = Text(initials, 0 ,height//2 + 25)
             #Loop to allow user to enter their initials if they obtained a highscore
             while(highscoreFlag):
                #Temporarily stores shift key presses
                keys = pygame.key.get_pressed()
                #Checks to see what the player does next
                for event in pygame.event.get():
                    #If the player attempts to close the window, the program stops running
                    if event.type == pygame.QUIT:
                        sys.exit()
                    #Checks to see if the player pressed a letter or number (not on the numpad)
                    elif event.type == pygame.KEYDOWN:
                        #Returns the string ID of the key pressed
                        key = pygame.key.name(event.key) 
                        #Adds the key pressed the initials
                        if len(key) == 1:  
                            if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                                initials += key.upper()
                            else:
                                initials += key
                                print(initials)
                        #Removes the last character from initials if the backspace key is pressed
                        elif key == "backspace":
                            initials = initials[:len(initials) - 1]
                        #Finalizes name if player presses enter
                        elif event.key == pygame.K_RETURN:
                            highscore2.addHighScore(initials, player2.score)
                            highscore2.write_to_file()
                            highscoreFlag = False
                #Updates initials text to whatever value the variable initials holds
                initialsTxt.update_text(initials)
                #Turns the entire screen black
                screen.fill(black)
                #Displays a message that prompts the user to enter their initials 
                screen.blit(text2.messageTxt, text2.messageTxtRect)
                #Displays the characters the player has entered
                screen.blit(initialsTxt.messageTxt, initialsTxt.messageTxtRect)
                #Renders screen
                pygame.display.flip()
         




         #While loop to pause the game after a player loses a life until they decide to continue
         while(nextLifeFlag):
         #Checks to see what the player has clicked
            for event in pygame.event.get():
             #If the player attempts to close the window, the program stops running
                if event.type == pygame.QUIT:
                    sys.exit()
             #Checks which button the player has pressed
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    (mouseX, mouseY) = pygame.mouse.get_pos()
                 #The game continues if the player pressed the continue button
                    if((mouseX >= continue3.continueButtonRect.x and mouseX <= (continue3.continueButtonRect.x + 192)) and (mouseY >= continue3.continueButtonRect.y and mouseY <= continue3.continueButtonRect.y + 48)):
                        nextLifeFlag = False
             #Slows down the game
            pygame.time.delay(10)
     #The entire display turns to black
            screen.fill(black)
     #Displays continue button
            screen.blit(continue3.continueButton, continue3.continueButtonRect)
     #Displays the brick objects in the list "wall2.bricks" onto the screen
            #Displays generic bricks
            if(brickIdentifier == 0):
                for brick in wall2.bricks:
                    screen.blit(brick.bric, brick.bricrect)
            #Displays snow bricks
            elif(brickIdentifier == 1):
                for brick in wall2.bricks:
                    screen.blit(brick.sbric, brick.sbricrect)
            #Displays dark bricks
            elif(brickIdentifier == 2):
                for brick in wall2.bricks:
                    screen.blit(brick.dbric, brick.dbricrect)
            #Displays gold bricks
            elif(brickIdentifier == 3):
                for brick in wall2.bricks:
                    screen.blit(brick.gbric, brick.gbricrect)
     #Displays the ball in its new location
            screen.blit(ball2.bal,ball2.balrect)
     #Displays the paddle in its new location
            screen.blit(paddle2.padd, paddle2.paddrect)
     #Renders screen
            pygame.display.flip()
     

            
        
     #If the ball hits the top of the screen, everything on the screen disappears and a levelup image and continue button image are displayed on the screen.
     elif(ball2.balrect.y == 0):
        complete.play(0)
        #records time elapsed after level completion
        timer2.calculateActualTime()
        #increases the score of the player based on the amount of time elapsed and the number of bricks remining
        player2.increase_score(timer2.actualTime, len(wall2.bricks))
        #reset the timer
        timer2.resetTimer()
        #generate the next level
        wall2.destroyWall()
        level2.level_up()
        ball2.resetBall()
        wall2.populate(level2, int(width/48), 50)
        nextLevelFlag = True
        while(nextLevelFlag):
             #Checks to see what the player has clicked
            for event in pygame.event.get():
             #If the player attempts to close the window, the program stops running
                if event.type == pygame.QUIT:
                    sys.exit()
             #Checks which button the player has pressed
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    (mouseX, mouseY) = pygame.mouse.get_pos()
                 #The game starts if the player pressed the continue button
                    if((mouseX >= continue2.continueButtonRect.x and mouseX <= (continue2.continueButtonRect.x + 192)) and (mouseY >= continue2.continueButtonRect.y and mouseY <= continue2.continueButtonRect.y + 48)):
                         #Starts the level timer
                        timer2.startTimer()
                        nextLevelFlag = False
            
        
            #Displays the continue button and levelup image onto the screen
            pygame.time.delay(10)
            screen.fill((white))
            screen.blit(continue2.continueButton, continue2.continueButtonRect)
            level2.display_onto_screen(level2.levelup, level2.leveluprect, screen)
            
     

     else:
       #A loop that checks to see if any of the bricks were hit by the ball.
       #Each ball that is hit is removed from the list "wall2.bricks"
       for brick in wall2.bricks:
            if((ball2.balrect.y <= brick.bricrect.y + 48 and ball2.balrect.y >= brick.bricrect.y) and (ball2.balrect.x <= brick.bricrect.x + 48 and ball2.balrect.x >= brick.bricrect.x)):
                #The ball makes a sound if it hits a brick
                woosh.play(0)
                #Randomly directs the ball -45 or -135 degrees randomly (approximately 50% chance) if a brick is hit by the ball.
                #After a brick is hit, it is removed from wall2.bricks
                temp = random.randint(0,1)
                if(temp == 0):
                    ball2.change_direction(45)
                    wall2.bricks.remove(brick)
                else:
                    ball2.change_direction(135)
                    wall2.bricks.remove(brick)

     #Slows down the game
     level2.controlSpeed()
     #The entire display turns to black
     screen.fill(black)
    #Displays the brick objects in the list "wall2.bricks" onto the screen
            #Displays generic bricks
     if(brickIdentifier == 0):
        for brick in wall2.bricks:
            screen.blit(brick.bric, brick.bricrect)
            #Displays snow bricks
     elif(brickIdentifier == 1):
        for brick in wall2.bricks:
            screen.blit(brick.sbric, brick.sbricrect)
            #Displays dark bricks
     elif(brickIdentifier == 2):
        for brick in wall2.bricks:
            screen.blit(brick.dbric, brick.dbricrect)
            #Displays gold bricks
     elif(brickIdentifier == 3):
        for brick in wall2.bricks:
            screen.blit(brick.gbric, brick.gbricrect)
     #Displays the time elapsed by the player
     timer2.updateTimer()
     screen.blit(timer2.timerTxt,timer2.timerTxtRect)
     #Displays the score of the player
     player2.updateScoreText()
     screen.blit(player2.scoreTxt, player2.scoreTxtRect)
     #Displays the remaining lives of the player
     player2.updateLifeText()
     screen.blit(player2.livesTxt, player2.livesTxtRect)
     #Displays the ball in its new location
     screen.blit(ball2.bal,ball2.balrect)
     #Displays the paddle in its new location
     screen.blit(paddle2.padd, paddle2.paddrect)
     #Renders screen
     pygame.display.flip()
     