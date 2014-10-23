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

        self.backButton = MenuItem('Back', fontSize = 20, fontName = self.fontName)
        xPos = self.screen.get_rect().width/2 - self.backButton.width/2
        yPos = self.screen.get_rect().height - (self.backButton.height + 15)
        self.backButton.setPosition(xPos, yPos)
        # ---Dimensions---
        self.width = self.screen.get_rect().width
        self.height = self.screen.get_rect().height

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
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.backButton.isMouseSelection(pygame.mouse.get_pos()):
                        return

            self.screen.fill(self.backgroundColor)

            #Draw the Score Labels
            for item in self.scoreLabels:
                if item.yPos + item.height < self.screen.get_rect().height \
                        - self.backButton.xPos:
                    self.screen.blit(item.label, (item.xPos, item.yPos))

            #Draw the user labels
            for item in self.userLabels:
                if item.yPos + item.height < self.screen.get_rect().height \
                        - self.backButton.xPos:
                    self.screen.blit(item.label, (item.xPos, item.yPos))

            #draw the back button. Color depends on mouse position
            if self.backButton.isMouseSelection(pygame.mouse.get_pos()):
                self.backButton.setFontColor((40, 100, 234)) 
            else:
                self.backButton.setFontColor((0, 0, 0))
            self.screen.blit(self.backButton.label, (self.backButton.xPos,
                             self.backButton.yPos))

            pygame.display.flip()
