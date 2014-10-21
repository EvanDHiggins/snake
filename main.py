import pygame
import time
from lib.MenuItem import MenuItem
from mainmenu import GenericMenu
from snake import Snake
from ScoreDisplay import ScoreDisplay
from textbox import TextBox

pygame.init()

def main():
    # ---Initialize Screen---
    screen = pygame.display.set_mode((300, 275), 0, 32)
    pygame.display.set_caption('Snake')

    mainMenu = ('Play Game', 'High Scores', 'Settings', 'Quit')
    backgroundColor = (255, 255, 255)

    scoresList, userList = readScoresFromFile()
    mainMenu = GenericMenu(screen, mainMenu)
    mainMenu.setFont('inconsolata.otf')
    while(True):
        choice = mainMenu.run()
        if choice == 'Play Game':
            snake = Snake(screen)
            displayCountdown(screen, backgroundColor)
            newScore = snake.gameLoop()
            getUsername(screen, backgroundColor)
            #scoresList.append(newScore)
        elif choice == 'High Scores':
            highScores = ScoreDisplay(screen, scoresList, userList)
            highScores.run()
        elif choice == 'Quit':
            break
        choice == ""

def getUsername(screen, backgroundColor):
    done = False
    clock = pygame.time.Clock()
    oldWidth = screen.get_rect().width
    oldHeight = screen.get_rect().height
    textBox = TextBox()
    textBox.setFont('Inconsolata.otf')
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

        textBox.update(events)

        screen.fill(backgroundColor)

        textBox.render(screen)

        pygame.display.flip()

    print(textBox.inputString)

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

    file = open('scores.txt', 'r')
    for index, line in enumerate(file):
        if index % 2 == 0:
            userList.append(line)
        else:
            scoresList.append(line)
    for item in userList:
        print (item)
    for item in scoresList:
        item = "{0:0>5}".format(item)
        print(item)
    file.close()
    return scoresList, userList

main()
pygame.quit()
