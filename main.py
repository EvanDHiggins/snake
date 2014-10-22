import pygame
import time
from lib.MenuItem import MenuItem
from mainmenu import GenericMenu
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

    settings = {'snakeLength':5, 'fontName':'inconsolata.otf',
                'foodColor':(255,0,0)} 

    scoresList, userList = readScoresFromFile()
    mainMenu = GenericMenu(screen, mainMenu, fontName = settings['fontName'])
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
            scoresList.append(newScore)
            userList.append(userName)

        elif choice == 'High Scores':
            highScores = ScoreDisplay(screen, scoresList, userList,
                            fontName = settings['fontName'])
            #highScores.setFont(settings['fontName'])
            highScores.run()
        elif choice == 'Quit':
            break
        choice == ""
    saveScoresToFile(scoresList, userList)

def getUsername(screen, backgroundColor, settings):
    done = False
    clock = pygame.time.Clock()
    oldWidth = screen.get_rect().width
    oldHeight = screen.get_rect().height
    nameBox = TextBox()
    nameBox.setFont(settings['fontName'])
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

def readScoresFromFile():
    userList = []
    scoresList = []

    scoresFile = open('scores.txt', 'r')
    for index, line in enumerate(scoresFile):
        if index % 2 == 0:
            userList.append(line)
        else:
            scoresList.append(int(line))
    scoresFile.close()
    return scoresList, userList

def saveScoresToFile(scoresList, userList):
    scoresFile = open('scores.txt', 'w')
    for index in range(len(scoresList)):
        scoresFile.write(userList[index])
        scoresFile.write(str(scoresList[index]))
        print(str(scoresList[index]))
    scoresFile.close()

main()
pygame.quit()
