import pygame
import time
from string import *
from operator import itemgetter
from lib.MenuItem import MenuItem
from menu import *
from snake import Snake
from ScoreDisplay import ScoreDisplay
from textbox import TextBox

pygame.init()

FONT_CHOICE = 'inconsolata.otf'

def main():
    # ---Initialize Screen---
    screen = pygame.display.set_mode((300, 275), 0, 32)
    pygame.display.set_caption('Snake')

    mainMenu = ('Play Game', 'High Scores', 'Settings', 'Quit')
    backgroundColor = (255, 255, 255)

    settings = {'snakeLength':(5, 15, 20), 'fontName':('inconsolata.otf'),
                'foodColor':(255,0,0)}
    #settings = [('Snake Length', 5, 10, 15), ('Font Name', 'inconsolata.otf')]

    #List of tuples formatted (user, score)
    highScoreList = []

    readScoresFromFile(highScoreList)
    sortScores(highScoreList)
    mainMenu = SingleColumnMenu(screen, mainMenu, fontName = settings['fontName'])
    while(True):
        choice = mainMenu.run()
        if choice == 'Play Game':
            #Create instance of Snake.py
            snake = Snake(screen)

            displayCountdown(screen, backgroundColor)

            #Runs game and returns player score
            newScore = snake.gameLoop()

            #Prompts user for name
            userName = getUsername(screen, backgroundColor, settings)

            #Adds to high Scores
            highScoreList.append((userName, newScore))
            sortScores(highScoreList)

        elif choice == 'High Scores':
            highScores = ScoreDisplay(screen, highScoreList,
                            fontName = settings['fontName'])
            highScores.run()
        elif choice == 'Settings':
            settingsMenu = SettingsMenu(screen, settings) 
            settingsMenu.run()
        elif choice == 'Quit':
            break
        choice == ""
    saveScoresToFile(highScoreList)

def getUsername(screen, backgroundColor, settings):
    done = False
    clock = pygame.time.Clock()
    oldWidth = screen.get_rect().width
    oldHeight = screen.get_rect().height
    nameBox = TextBox(fontName = settings['fontName'])
    screen = pygame.display.set_mode((nameBox.width, nameBox.height), 0, 32)
    while not done:
        clock.tick(60)

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    done = True

        nameBox.update(events)

        screen.fill(backgroundColor)

        nameBox.render(screen)

        pygame.display.flip()

    screen = pygame.display.set_mode((oldWidth, oldHeight), 0, 32)
    return nameBox.inputString

def displayCountdown(screen, backgroundColor):
    for i in xrange(3, 0, -1):
        font = pygame.font.SysFont(None, 30)
        label = font.render(str(i), 1, (0, 0, 0))

        #Center the number on the screen
        xPos = screen.get_rect().width/2 - label.get_rect().width/2
        yPos = screen.get_rect().height/2 - label.get_rect().height/2
        screen.fill(backgroundColor)
        screen.blit(label, (xPos, yPos))
        pygame.display.flip()
        time.sleep(1)

def readScoresFromFile(highScoreList):
    scoresFile = open('scores.txt', 'r')
    for line in scoresFile:
        #Cut off the newline character from end of line
        line = line.replace('\n', '')

        #Places users and scores into list of tuples
        if line.isdigit(): 
            userTuple = (userName, int(line))
            highScoreList.append(userTuple)
        else:
            userName = line

    scoresFile.close()

def sortScores(highScoreList):
    #Sorts scores in descending order
    highScoreList.sort(key=lambda tup: tup[1], reverse=True)

def saveScoresToFile(highScoreList):
    scoresFile = open('scores.txt', 'w')
    for score in highScoreList:
        userStr = str(score[0]) + '\n'
        scoreStr = str(score[1]) + '\n'
        scoresFile.write(userStr)
        scoresFile.write(scoreStr)
    scoresFile.close()

if __name__ == '__main__':
    main()
    pygame.quit()
