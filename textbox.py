import pygame
from datetime import datetime

pygame.init()
ANTI_ALIAS = 1

class TextBox:
    """

    Attributes:
        self.xPos (int): X Position in pixels of the top left corner of the
                    text box.
        self.yPos (int): Y Position in pixels of the tops left corner of the
                    text box.
        self.position (tuple): Tuple containing (xPos, yPos) for easier access
                    to location
        self.fontSize (int): size of text within text box
        self.fontColor (tuple): RGB value of text color, doesn't necessarily
                    match border color
        self.fontName (str): String name of font of text within box
        self.numberOfChars (int): estimated number of characters which can fit
                    in the text box.  This determines the width of the text
                    box. Width is determined based off a string of this many
                    'm' (one of the widest characters).
        self.borderThickness (int): The thickness of the text box border in
                    pixels
        self.padding (int): number of pixels of padding between edge of
                    characters and text box border
        self.borderColor (tuple): RGB tuple for color of border
        self.inputString (string): String of text displayed within text box.
                    Changes reflect keypresses of user while textbox is present.
        self.shifted (boolean): Reflects whether or not any keypresses by the
                    user will be capitalized.  This defaults to False, is set
                    True when either right or left shift is pressed, and changes
                    back to false when a shift is still pressed.
        self.font (Font): pygame Font object created from the font name and the
                    size of the desired font.  This is rendered separately
        self.label (surface): Rendered image of text from self.font.Font object.
                    This updates during runtime to reflect inputString.
    """
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
        self.inputString = 'Enter your name'
        self.inputList = []
        for char in self.inputString:
            self.inputList.append(char)
        self.shifted = False
        self.backSpace = False
        self.elapsedBackspaceTime = 0
        self.contBackspace = False
        self.font = pygame.font.Font(self.fontName, self.fontSize)
        self.makeLabels()
        #self.label = self.font.render(self.inputString, ANTI_ALIAS,
        #                              self.fontColor)
        self.cursorPosition = len(self.labelList) - 1
        self.previousTime = float(str(datetime.now())[-9:])
        self.elapsedTime = 0

        #Dimensions
        self.width, self.height = self.determineDimensions(numberOfChars)


        self.setPosition(xPos, yPos)

    def makeLabels(self):
        self.labelList = []
        for char in self.inputList:
            label = self.font.render(char, ANTI_ALIAS, self.fontColor)
            width = label.get_rect().width
            height = label.get_rect().height
            self.labelList.append((label, width, height))

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
        text = '[g'
        for char in xrange(characters):
            text += 'm'
        text = self.font.render(text, ANTI_ALIAS, (0, 0, 0))
        return text.get_rect().width + self.padding, \
            text.get_rect().height + self.padding*2

    def deleteChar(self):
        """Removes item from inputString at cursor"""
        if len(self.inputList) > 0:
            self.inputList.pop(self.cursorPosition)
            self.cursorPosition -= 1

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
                elif event.key == pygame.K_BACKSPACE:
                    self.backSpace = False
                    self.contBackspace = False
                    self.elapsedBackspaceTime = 0

            #Returns input string when return is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return self.inputList

                #Turns shift on when shift goes down
                elif (event.key == pygame.K_LSHIFT or
                        event.key == pygame.K_RSHIFT):
                    self.shifted = True

                #This includes alphanumeric characters and special symbols
                elif event.key > 31 and event.key < 126:
                    if self.shifted == True:
                        self.cursorPosition += 1
                        self.inputList.insert(self.cursorPosition,
                                chr(event.key).capitalize())
                        return
                    elif self.shifted == False:
                        self.cursorPosition += 1
                        self.inputList.insert(self.cursorPosition,
                                chr(event.key))
                        return
                #Removes final object in array when backspace is pressed
                elif event.key == pygame.K_BACKSPACE:
                    self.deleteChar()
                    self.backSpace = True

                elif event.key == pygame.K_LEFT:
                    if self.cursorPosition > 0:
                        self.cursorPosition -= 1

                elif event.key == pygame.K_RIGHT:
                    if self.cursorPosition < len(self.labelList) - 1:
                        self.cursorPosition += 1

        currentTime = str(datetime.now())
        currentTime = float(currentTime[-9:])
        self.elapsedTime += currentTime - self.previousTime

        if self.backSpace == True:
            self.elapsedBackspaceTime += currentTime - self.previousTime
            if self.elapsedBackspaceTime > .5:
                self.contBackspace = True

        if self.elapsedTime > .5:
            self.displayCursor = not self.displayCursor
            self.elapsedTime = 0

        if self.contBackspace == True:
            self.deleteChar()


        self.previousTime = currentTime

    def render(self, screen):
        """function renders textbox at x/y position"""
        #Create image of text for rendering
        #self.label = self.font.render(self.inputString, ANTI_ALIAS, self.fontColor)
        self.makeLabels()
        print(self.cursorPosition)

        #Draw border rectangle
        pygame.draw.rect(screen, self.borderColor, [self.xPos, self.yPos,
                         self.width, self.height], self.borderThickness)

        #Render text to screen
        xPos = self.textXPos
        yPos = self.textYPos
        for index in xrange(len(self.labelList)):
            if len(self.labelList) == 0 and self.displayCursor:
                print('HELLO')
                pygame.draw.rect(screen, self.borderColor, [xPos, yPos, 1,
                                 self.height - self.padding*2],
                                 self.borderThickness)
            item = self.labelList[index]
            screen.blit(item[0], (xPos, yPos))
            if index == self.cursorPosition: #and self.displayCursor:
                pygame.draw.rect(screen, self.borderColor, [xPos +
                    item[0].get_rect().width, yPos, 1, item[2] - self.padding],
                    self.borderThickness)
            xPos += item[1]

        if self.cursorPosition == -1 and self.displayCursor:
            pygame.draw.rect(screen, self.borderColor, [xPos, yPos, 1,
                            self.height - self.padding*3],
                            self.borderThickness)
        #else:
         #   print('ELSE!')
         #   if self.displayCursor:
         #       pygame.draw.rect(screen, self.borderColor, [xPos, yPos, 1,
         #                        self.height - self.padding*2],
         #                        self.borderThickness)
        #Render text highlight
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
    pygame.quit()

if __name__ == "__main__" :
    main()
