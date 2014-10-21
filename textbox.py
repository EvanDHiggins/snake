import pygame

pygame.init()
ANTI_ALIAS = 1

class TextBox:
    def __init__(self, (xPos, yPos) = (0, 0), textFieldColor = (255, 255, 255),
                 borderColor = (0, 0, 0), fontName = None, fontSize = 30,
                 fontColor = (0, 0, 0), numberOfChars = 20,
                 borderThickness = 2):
        """ (xPos, yPos) - coordinates of upper left corner
            borderColor - color of textBox outline
            fontSize - size of input string font, will determine vertical
                        dimension of box
            fontColor - color of input string font
            numberOfChars - number of characters (approximately) which can fit in
                    the textbox"""

        #Set position
        self.xPos = xPos
        self.yPos = yPos
        self.position = (xPos, yPos)

        #Set font properties
        self.fontSize = fontSize
        self.fontColor = fontColor
        self.fontName = fontName


        #Textbox properties
        self.displayCursor = True
        self.numberOfChars = numberOfChars
        self.borderThickness = borderThickness
        self.padding = 3#px
        self.borderColor = borderColor
        self.inputString = 'text'
        self.shifted = False
        self.font = pygame.font.Font(self.fontName, self.fontSize)
        self.label = self.font.render(self.inputString, ANTI_ALIAS,
                                      self.fontColor)

        #Dimensions
        self.width, self.height = self.determineDimensions(numberOfChars)


        self.setPosition(xPos, yPos)

    def setPosition(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
        self.position = (xPos, yPos)

        #Text Position
        self.textXPos = self.xPos + self.borderThickness + self.padding
        self.textYPos = self.yPos + self.borderThickness + self.padding
        self.textPosition = (self.textXPos, self.textYPos)

    def setFont(self, fontName):
        self.fontName = fontName
        self.font = pygame.font.Font(self.fontName, self.fontSize)
        self.width, self.height = self.determineDimensions(self.numberOfChars)


    def determineDimensions(self, characters):
        """Determines dimensions for text box based on input font size
           and length of box.

           characters: integer of the number of characters long the textbox
                       should be.
        """
        text = '['
        for char in xrange(characters):
            text += 'm'
        print(text)
        text = self.font.render(text, ANTI_ALIAS, (0, 0, 0))
        return text.get_rect().width + self.padding, \
            text.get_rect().height + self.padding


    def update(self, events):
        """
            Call this method within a loop to update the contents of the
            textbox
        events - list of events created within a pygame loop with:
                 events = pygame.events.get()
        """
        for event in events:

            #Turns shift off when shift goes up
            if event.type == pygame.KEYUP:
                if (event.key == pygame.K_LSHIFT or
                        event.key == pygame.K_RSHIFT):
                    self.shifted = False
            #Returns input string when return is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return self.inputString

                #Turns shift on when shift goes down
                if (event.key == pygame.K_LSHIFT or
                        event.key == pygame.K_RSHIFT):
                    self.shifted = True

                #This includes alphanumeric characters and special symbols
                if event.key > 31 and event.key < 126:
                    if self.shifted == True:
                        self.inputString += chr(event.key).capitalize()
                        return
                    elif self.shifted == False:
                        self.inputString += chr(event.key)
                        return
                #Removes final object in array when backspace is pressed
                elif event.key == pygame.K_BACKSPACE:
                    self.inputString = self.inputString[:-1]


    def render(self, screen):
        """function renders textbox at x/y position"""
        #Create image of text for rendering
        self.label = self.font.render(self.inputString, ANTI_ALIAS, self.fontColor)

        #Draw border rectangle
        pygame.draw.rect(screen, self.borderColor, [self.xPos, self.yPos,
                         self.width, self.height], self.borderThickness)

        #Render text to screen
        screen.blit(self.label, self.textPosition)
        #Render text highlight
        #text = self.font.render(self.inputString, ANTI_ALIAS, self.fontColor)
        #screen.blit(self.text, self.position)
        #Render cursor



def main():
    screen = pygame.display.set_mode((500, 500), 0, 32)
    pygame.display.set_caption('Text Box Test')
    aBox = TextBox()
    done = False
    aBox.setPosition(20, 20)
    aBox.setFont('Inconsolata.otf')
    inputString = ''
    while not done:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                done = True
        inputString = aBox.update(events)
        screen.fill((255, 255, 255))
        aBox.render(screen)
        pygame.display.flip()
    print(inputString)
    pygame.quit()

if __name__ == "__main__" :
    main()
