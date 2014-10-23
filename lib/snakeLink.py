class snakeLink:
    def __init__(self, direction, xPos, yPos, linkSize, linkSpacing):
        self.linkSize = linkSize + linkSpacing
        self.direction = direction
        self.xPos = xPos
        self.yPos = yPos

    def setDirection(self, newDirection):
        self.direction = newDirection

    def getOffset(self):
        if self.direction == 'r':
            return self.xPos - self.linkSize, self.yPos
        elif self.direction == 'l':
            return self.xPos + self.linkSize, self.yPos
        elif self.direction == 'u':
            return self.xPos, self.yPos + self.linkSize
        else:
            return self.xPos, self.yPos - self.linkSize

    def getXOffset(self):
        """X Offset for new link generation"""
        if self.direction == 'r':
            return (-1) * self.linkSize
        else:
            return self.linkSize

    def getYOffest(self):
        """Y Offset for new link generation"""
        if self.direction == 'u':
            return (-1) * self.linkSize
        else:
            return self.linkSize

    def moveLink(self):
        if self.direction == 'r':
            self.xPos += self.linkSize
        elif self.direction == 'l':
            self.xPos -= self.linkSize
        elif self.direction == 'u':
            self.yPos -= self.linkSize
        elif self.direction == 'd':
            self.yPos += self.linkSize
