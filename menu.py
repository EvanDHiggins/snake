import pygame

pygame.init()

class MenuItem(pygame.font.Font):
    def __init__(self, text, fontSize = 30, fontColor = (0, 0, 0),
                 font = None, (posX, posY) = (0, 0)):
        
        self.xPos = xPos
        self.yPos = yPos
        self.position = (xPos, yPos)

    def setPosition(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
        self.position = (xPos, yPos)

    def getXPos(self):
        return self.xPos

    def getYPos(self):
        return self.yPos



class GameMenu:
    def __init__(self, screen, menuStrings, backgroundColor = (255, 255, 255),
                 font = None, fontSize = 30, fontColor = (0, 0, 0)):
        self.screen = screen
        self.backgroundColor = backgroundColor
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(font, fontSize)
        self.menuStrings = menuStrings

        self.scrWidth = self.screen.get_rect().width
        self.scrHeight = self.screen.get_rect().height

        self.menuItems = {}

        for index, item in enumerate(menuStrings):
            label = self.font.render(item, 1, fontColor)

            width = label.get_rect().width
            height = label.get_rect().height
            xPos = screen.get_rect().width/2 - width/2
            yPos = 30 * (index + 1)
            self.menuItems[item] = [label, width, height, xPos, yPos]

    def run(self):

        #Boolean to signal end of looping
        done = False
        while not done:
            #Sets render speed
            self.clock.tick(60)

            #Handles input interrupts
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            #clear screen
            self.screen.fill(self.backgroundColor)

            for item in self.menuStrings:
                label = self.menuItems[item]
                self.screen.blit(label[0], (label[3], label[4]))
            pygame.display.flip()


if __name__ == "__main__":
    screen = pygame.display.set_mode((200, 200), 0, 32)
    pygame.display.set_caption('Game Menu')
    menuStrings = ('Play Game', 'High Scores', 'Quit')
    mainMenu = GameMenu(screen, menuStrings)
    mainMenu.run()
