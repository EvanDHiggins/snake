import pygame
from lib.MenuItem import MenuItem

pygame.init()

class ScoreDisplay:
    def __init__(self, screen, highScoreList, scoresOnScreen=10,
                 backgroundColor = (255, 255, 255), fontName = None):

        # ---Initialize Pygame Features---
        self.clock = pygame.time.Clock()

        # ---Lists of Strings---
        self.highScoreList = highScoreList

        # ---Lists of MenuItems---
        self.scoreLabels = []
        self.userLabels = []
        self.scoresOnScreen = scoresOnScreen
        self.screen = screen
        self.backgroundColor = backgroundColor

        self.fontName = fontName

        # ---Dimensions---
        self.width = screen.get_rect().width
        self.height = screen.get_rect().height

        self.createLabelLists()

    def createLabelLists(self):
        self.userLabels = []
        self.scoreLabels = []
        for index, scoreTuple in enumerate(self.highScoreList):
            #First index of tuple is username, second is score
            if index >= self.scoresOnScreen:
                break
            user = scoreTuple[0] 
            score = scoreTuple[1]

            user = user.replace('\n', '')
            self.userLabels.append(MenuItem(user, fontSize = 20))
            self.userLabels[index].setFont(self.fontName)
            xPos = 20
            yPos = (index + 1) * (self.height/self.scoresOnScreen)
            self.userLabels[index].setPosition(xPos, yPos)

            score = "{0:0>5}".format(score)
            #remove trailing \n
            score = score.replace('\n', '')
            if index > 9:
                break
            self.scoreLabels.append(MenuItem(score, fontSize = 20))
            self.scoreLabels[index].setFont(self.fontName)
            xPos = (self.screen.get_rect().width - 20 - \
                    self.scoreLabels[index].width) 
            yPos = (index + 1) * (self.height/self.scoresOnScreen)
            self.scoreLabels[index].setPosition(xPos, yPos)

    def setFont(self, fontName):
        self.fontName = fontName
        self.createLabelLists()

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
