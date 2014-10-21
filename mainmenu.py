import pygame
from snake import Snake
from lib.MenuItem import MenuItem
from textbox import *

pygame.init()

class GenericMenu:
    def __init__(self, screen, menuItems, backgroundColor = (255, 255, 255),
                 fontName = None, fontSize = 30, fontColor = (0, 0, 0)):

        # ---Initialize Pygame Features---
        self.clock = pygame.time.Clock()

        self.listLength = len(menuItems)

        self.fontName = fontName

        self.screen = screen
        self.width = screen.get_rect().width
        self.height = screen.get_rect().height
        self.menuItems = menuItems
        self.backgroundColor = backgroundColor
        self.menuList = []

        # ---Initialize MenuItems---
        self.initializeMenuItems()


    def initializeMenuItems(self):
        self.menuList = []
        for index, text in enumerate(self.menuItems):
            self.menuList.append(MenuItem(text))
            self.menuList[index].setFont(self.fontName)
            xPos = self.menuList[index].xPos
            yPos = self.menuList[index].yPos
            xPos = self.width/2 - self.menuList[index].width/2
            yPos = (index + 1) * (self.height/(self.listLength + 1))
            yPos -= self.menuList[index].height/2
            self.menuList[index].setPosition(xPos, yPos)

    def setFont(self, fontName):
        self.fontName = fontName
        self.initializeMenuItems()

    def run(self):

        done = False

        while not done:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for item in self.menuList:
                        if item.isMouseSelection(pygame.mouse.get_pos()):
                            return item.text

            self.screen.fill(self.backgroundColor)
            for item in self.menuList:
                if item.isMouseSelection(pygame.mouse.get_pos()):
                    item.setFontColor((40, 100, 234))
                else:
                    item.setFontColor((0, 0, 0))
                self.screen.blit(item.label, (item.xPos, item.yPos))

            pygame.display.flip()


if __name__ == "__main__":
    screen = pygame.display.set_mode((200, 175), 0, 32)
    pygame.display.set_caption('Main Menu')
    menuStrings = ('Play Game', 'High Scores', 'Quit')
    mainMenu = GenericMenu(screen, menuStrings)
    mainMenu.run()
