import pygame

pygame.init()

class MenuItem(pygame.font.Font):
    def __init__(self, text, fontSize = 30, fontColor = (0, 0, 0),
                 font = None, (xPos, yPos) = (0, 0)):


        # ---Item Properties---
        self.text = text
        pygame.font.Font.__init__(self, font, fontSize)

        # ---Font Properties---
        self.fontSize = fontSize
        self.fontColor = fontColor
        self.font = font

        # ---Position---
        self.xPos = xPos
        self.yPos = yPos
        self.position = (xPos, yPos)

        # ---Render---
        self.label = self.render(self.text, 1, self.fontColor)

        # ---Dimensions---
        self.width = self.label.get_rect().width
        self.height = self.label.get_rect().height

    def setPosition(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
        self.position = (xPos, yPos)

    def setFontColor(self, colorTuple):
        self.fontColor = colorTuple
        self.label = self.render(self.text, 1, self.fontColor)

    def isMouseSelection(self, (xPos, yPos)):
        if(xPos >= self.xPos and xPos <= self.xPos + self.width) and \
            (yPos >= self.yPos and yPos <= self.yPos + self.height):
            return True
        else:
            return False

class GenericMenu:
    def __init__(self, screen, menuItems, backgroundColor = (255, 255, 255),
                 font = None, fontSize = 30, fontColor = (0, 0, 0)):

        # ---Initialize Pygame Features---
        self.clock = pygame.time.Clock()

        self.screen = screen
        self.width = screen.get_rect().width
        self.height = screen.get_rect().height
        self.menuItems = menuItems
        self.backgroundColor = backgroundColor
        self.menuList = []

        # ---Initialize MenuItems---
        for index, text in enumerate(menuItems):
            self.menuList.append(MenuItem(text))
            xPos = self.menuList[index].xPos
            yPos = self.menuList[index].yPos
            xPos = self.width/2 - self.menuList[index].width/2
            yPos = (index + 1) * 40
            self.menuList[index].setPosition(xPos, yPos)


    def run(self):

        done = False

        while not done:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

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
