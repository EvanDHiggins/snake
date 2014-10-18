import sys, pygame
import itertools
import random
from lib.snakeLink import snakeLink
from lib.foodpiece import FoodPiece

pygame.init()

#COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (200, 0, 0)

#self.linkSize = 6
#self.linkSpacing = 4
#self.screenWidth = 236
#self.screenHeight = 236

class Snake():
    def __init__(self, screen):

        # ---Initialize Pygame Functionality---
        self.clock = pygame.time.Clock()

        # ---Initialize Dimensions---
        self.screen = screen
        self.screenHeight = screen.get_rect().height
        self.screenWidth = screen.get_rect().width
        self.linkSize = 6
        self.linkSpacing = 4

        self.acceptingMoves = True

        self.done = False

    def gameLoop(self):

        #End of Loop Boolean

        #Initialize Game Loop Variables
        snake = self.initializeSnake()
        numberOfFood = 0
        food = []

        while not self.done:
            #Elif statement for command interrupts
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if (self.isLegalMove(snake[0], 'u') and \
                                self.acceptingMoves == True):
                            snake[0].setDirection('u')
                            self.acceptingMoves = False

                    elif event.key == pygame.K_DOWN:
                        if (self.isLegalMove(snake[0], 'd') and \
                                self.acceptingMoves == True):
                            snake[0].setDirection('d')
                            self.acceptingMoves = False

                    elif event.key == pygame.K_LEFT:
                        if (self.isLegalMove(snake[0], 'l') and \
                                self.acceptingMoves == True):
                            snake[0].setDirection('l')
                            self.acceptingMoves = False

                    elif event.key == pygame.K_RIGHT:
                        if (self.isLegalMove(snake[0], 'r') and \
                                self.acceptingMoves == True):
                            snake[0].setDirection('r')
                            self.acceptingMoves = False

                    elif event.key == pygame.K_SPACE:
                        self.addLink(snake)

            # --- Game logic goes here ---
            numberOfFood = self.updateGame(snake, food, numberOfFood)
            

            # Overwrite Screen White
            self.screen.fill(WHITE)

            # --- Render here ---
            self.render(food, snake, self.screen)

            # Update Display
            pygame.display.flip()

            #Limit FPS
            self.clock.tick(15)

        return

    def addLink(self, oldSnake):
        """Adds a link to the end of the snake directly behind the last link"""

        #The final link of the snake in order to derive
        # the next link's location and direction
        finalLink = oldSnake[len(oldSnake) - 1]
        newdirection = finalLink.getDirection()
        newX, newY = finalLink.getOffset()

        oldSnake.append(snakeLink(newdirection, newX, newY,
                                    self.linkSize, self.linkSpacing))

    def initializeSnake(self):
        snake = []
        #Create initial head link at arbitrarily chosen position
        snake.append(snakeLink('r', 50, 100, self.linkSize, self.linkSpacing))

        #Create 4 additional links behind head
        for i in range(4):
            self.addLink(snake)
        return snake

    def nextMoves(self, snake):
        """Shifts moves down the snake"""
        tempSnake = snake[:]
        tempSnake.reverse()
        for link in range(0, len(tempSnake) - 1):
            tempSnake[link].setDirection(tempSnake[link+1].getDirection())
        self.acceptingMoves = True
        return snake

    def isLegalMove(self, head, move):
        direction = head.getDirection()
        if direction == 'r' or direction == 'l':
            if move == 'r' or move == 'l':
                return False
            else:
                return True
        else:
            if move == 'u' or move == 'd':
                return False
            else:
                return True

    def collision(self, snake, food = []):
        """Returns the title of the thing that the snake is colliding with

        :snake: snake array
        :returns: String of object the snake has collided with

        """
        headXPos = snake[0].getXPosition()
        headYPos = snake[0].getYPosition()

        #Skips head in order to avoid comparing head position with itself
        #when determining collision with self
        for link in itertools.islice(snake, 1, len(snake) - 1):
            linkXPos = link.getXPosition()
            linkYPos = link.getYPosition()
            if linkXPos == headXPos and linkYPos == headYPos:
                return "self"
        if headXPos >= self.screenWidth or headXPos < 0:
            return "wall"
        elif headYPos >= self.screenHeight or headYPos < 0:
            return "wall"

        for piece in food:
            if(piece.getXPosition() == headXPos
                and piece.getYPosition() == headYPos):
                food.remove(piece)
                return "food"

    def addFood(self, food):
        """Generates random position for piece of food

        food: array of food pieces
        returns: void

        """
        xPos = random.randrange(0, self.screenWidth)
        xPos = xPos - (xPos % (self.linkSize + self.linkSpacing))
        yPos = random.randrange(0, self.screenHeight)
        yPos = yPos - (yPos % (self.linkSize + self.linkSpacing))
        food.append(FoodPiece(xPos, yPos))

    def updateGame(self, snake, food, numberOfFood):
        #Advances the position of each link in the snake
        for link in snake:
            link.moveLink()

        #the item that the snake has collided with
        collisionItem = self.collision(snake, food)
        if collisionItem == "food":
            self.addLink(snake)
            numberOfFood -= 1
        elif collisionItem == "self":
            self.done = True
        elif collisionItem == "wall":
            self.done = True

        if numberOfFood < 3:
            self.addFood(food)
            numberOfFood += 1

        snake = self.nextMoves(snake)
        return numberOfFood

    def render(self, food, snake, screen):
        for piece in food:
            pygame.draw.rect(screen, RED, [piece.getXPosition() + 1,
                piece.getYPosition() + 1, 4, 4])
        for link in snake:
            pygame.draw.rect(screen, BLACK, [link.getXPosition(),
                        link.getYPosition(), self.linkSize, self.linkSize])


def main():
    screen = pygame.display.set_mode((500, 500))
    snakeGame = Snake(screen)
    snakeGame.gameLoop()

if __name__ == "__main__":
    main()
