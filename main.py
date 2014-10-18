import pygame
import time
from mainmenu import GenericMenu
from snake import Snake

pygame.init()

def main():
    # ---Initialize Screen---
    screen = pygame.display.set_mode((300, 275), 0, 32)
    pygame.display.set_caption('Snake')

    mainMenu = ('Play Game', 'High Scores', 'Settings', 'Quit')
    backgroundColor = (255, 255, 255)

    scoresList = readScoresFromFile()
    mainMenu = GenericMenu(screen, mainMenu)
    while(True):
        choice = mainMenu.run()
        if choice == 'Play Game':
            snake = Snake(screen)
            displayCountdown(screen, backgroundColor)
            newScore = snake.gameLoop()
            #scoresList.append(newScore)
        elif choice == 'High Scores':
            pass 
        elif choice == 'Quit':
            pygame.quit()
        choice == ""

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
    pass

main()
