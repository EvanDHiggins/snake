import pygame
from lib.MenuItem import MenuItem

pygame.init()

class ScoreDisplay:
    def __init__(self, screen, scoresList, userList, 
                 backgroundColor = (255, 255, 255)):

        # ---Initialize Pygame Features---
        self.clock = pygame.time.Clock()

        # ---Lists of Strings---
        self.scoresList = scoresList
        self.userList = userList

        # ---Lists of MenuItems---
        self.scoreLabels = []
        self.userLabels = []

        self.screen = screen
        self.backgroundColor = backgroundColor

        # ---Dimensions---
        self.width = screen.get_rect().width
        self.height = screen.get_rect().height

        for index, user in enumerate(userList):
            itemsOnScreen = 10
            #remove trailing \n
            user = user[:-1]
            if index > 9:
                break
            self.userLabels.append(MenuItem(user, fontSize = 25))
            xPos = 20
            yPos = (index + 1) * (self.height/itemsOnScreen)
            self.userLabels[index].setPosition(xPos, yPos)

        for index, score in enumerate(scoresList):
            itemsOnScreen = 10
            #Format to 6 columns for layout
            score = "{0:0>6}".format(score)
            #remove trailing \n
            score = score[:-1]
            if index > 9:
                break
            self.scoreLabels.append(MenuItem(score, fontSize = 25))
            xPos = self.screen.get_rect().width - 20 - self.scoreLabels[index].width 
            yPos = (index + 1) * (self.height/itemsOnScreen)
            self.scoreLabels[index].setPosition(xPos, yPos)

    def run(self):

        done = False

        while not done:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            self.screen.fill(self.backgroundColor)

            for item in self.scoreLabels:
                self.screen.blit(item.label, (item.xPos, item.yPos))

            for item in self.userLabels:
                self.screen.blit(item.label, (item.xPos, item.yPos))

            pygame.display.flip()
