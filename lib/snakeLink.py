class snakeLink:
    def __init__(self, direction, xPosition, yPosition, linkSize, linkSpacing):
        self.linkSize = linkSize + linkSpacing
        self.direction = direction
        self.xPosition = xPosition
        self.yPosition = yPosition

    def setDirection(self, newDirection):
        self.direction = newDirection

    def getXPosition(self):
        return self.xPosition

    def getYPosition(self):
        return self.yPosition

    def getDirection(self):
        return self.direction

    def getOffset(self):
        if self.direction == 'r':
            return self.xPosition - self.linkSize, self.yPosition
        elif self.direction == 'l':
            return self.xPosition + self.linkSize, self.yPosition
        elif self.direction == 'u':
            return self.xPosition, self.yPosition + self.linkSize
        else:
            return self.xPosition, self.yPosition - self.linkSize

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
            self.xPosition += self.linkSize
        elif self.direction == 'l':
            self.xPosition -= self.linkSize
        elif self.direction == 'u':
            self.yPosition -= self.linkSize
        elif self.direction == 'd':
            self.yPosition += self.linkSize
