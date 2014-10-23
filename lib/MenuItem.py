import pygame

pygame.init()

ANTI_ALIAS = 1
class MenuItem(pygame.font.Font):
    def __init__(self, text, fontSize = 30, fontColor = (0, 0, 0),
                 fontName = None, (xPos, yPos) = (0, 0)):


        # ---Item Properties---
        self.text = text
        pygame.font.Font.__init__(self, fontName, fontSize)

        # ---Font Properties---
        self.fontSize = fontSize
        self.fontColor = fontColor
        self.fontName = fontName

        # ---Position---
        self.xPos = xPos
        self.yPos = yPos
        self.position = (xPos, yPos)

        # ---Render---
        self.label = self.render(self.text, 1, self.fontColor)

        # ---Dimensions---
        self.getDimensions()

    def getDimensions(self):
        self.height = self.label.get_rect().height
        self.width = self.label.get_rect().width

    def setFont(self, fontName):
        self.fontName = fontName
        pygame.font.Font.__init__(self, self.fontName, self.fontSize)
        self.label = self.render(self.text, ANTI_ALIAS, self.fontColor)
        self.getDimensions() 

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

