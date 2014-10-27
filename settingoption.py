import pygame
from lib.MenuItem import *

pygame.init()

class SettingOption:
    def __init__(self, name, options, numberOfOptions, fontName = None):
        self.name = name
        self.options = options
        self.numberOfOptions = numberOfOptions
        self.booleanOption = False
        self.currentOption = 0
        self.optionLabels = []
        self.fontName = fontName

        self.nameXPos = 0
        self.yPos = 0
        self.namePosition = (self.nameXPos, self.nameYPos)

        self.makeLabels()

    def setNamePosition(self, xPos, yPos):
        self.nameXPos = xPos
        self.yPos = yPos
        self.position = (xPos, yPos)

    def setRightMargin(self, xPos, screenWidth):
        self.rightMargin = xPos
        for label in self.optionLabels:
            label.setPosition(screenWidth - xPos - label.width, self.yPos)


    def get(self):
        return self.optionLabels[self.currentOption]

    def next(self):
        """Increment currentOption and returns a label"""
        self.currentOption += 1
        return self.optionLabels[self.currentOption]

    def makeLabels(self):
        """Creates labels"""
        self.nameLabel = MenuItem(self.name, fontName = self.fontName) 
        for tup in self.options:
            for option in tup:
                self.optionLabels.append(MenuItem(option, fontName=self.fontName))
