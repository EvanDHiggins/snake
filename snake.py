import sys, pygame
import itertools
import random
from collections import deque
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
    def __init__(self, screen, originalLength = 5):

        # ---Initialize Pygame Functionality---
        self.clock = pygame.time.Clock()
        pygame.mouse.set_visible(False)

        # ---Initialize Dimensions---
        self.screen = screen
        self.screenHeight = screen.get_rect().height
        self.screenWidth = screen.get_rect().width
        self.linkSize = 6
        self.linkSpacing = 4

        # ---Initial Snake Features---
        self.originalLength = originalLength
        self.score = 0
        self.moveQueue = []

        # If True, pressing an arrow key will affect the snakes position
        #, if False, it will not.  This prevents fast key strokes killing
        # the snake
        self.acceptingMoves = True

        self.done = False

    def gameLoop(self):

        #Initialize Game Loop Variables
        snake = self.initializeSnake()
        numberOfFood = 0
        food = []

        while not self.done:
            #Elif statement for command interrupts
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.done = True

                # Snake Movement Handlers
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

        pygame.mouse.set_visible(True)
        print(self.score)
        return self.score

    def addLink(self, snake):
        """Adds a link to the end of the snake directly behind the last link"""

        #The final link of the snake in order to derive
        # the next link's location and direction
        finalLink = snake[len(snake) - 1]
        newdirection = finalLink.direction
        newX, newY = finalLink.getOffset()

        snake.append(snakeLink(newdirection, newX, newY,
                                    self.linkSize, self.linkSpacing))


    def initializeSnake(self):
        snake = []
        #Create initial head link at arbitrarily chosen position
        snake.append(snakeLink('r', 50, 100, self.linkSize, self.linkSpacing))

        #Create 4 additional links behind head
        for i in range(self.originalLength - 1):
            self.addLink(snake)
        return snake

    def nextMoves(self, snake):
        """Shifts moves down the snake"""
        tempSnake = snake[:]
        tempSnake.reverse()
        for link in range(0, len(tempSnake) - 1):
            tempSnake[link].setDirection(tempSnake[link+1].direction)
        self.acceptingMoves = True
        return snake

    def isLegalMove(self, head, move):
        direction = head.direction
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
        headXPos = snake[0].xPos
        headYPos = snake[0].yPos

        #Skips head in order to avoid comparing head position with itself
        #when determining collision with self
        for link in itertools.islice(snake, 1, len(snake) - 1):
            linkXPos = link.xPos
            linkYPos = link.yPos
            if linkXPos == headXPos and linkYPos == headYPos:
                return "self"
        if headXPos >= self.screenWidth or headXPos < 0:
            return "wall"
        elif headYPos >= self.screenHeight or headYPos < 0:
            return "wall"

        for piece in food:
            if(piece.xPos == headXPos
                and piece.yPos == headYPos):
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

    def advanceQueue(self, snake):
        move = self.moveQueue[0]
        if 


    def updateGame(self, snake, food, numberOfFood):
        #Gets next move from queue
        advanceQueue(snake)

        #Advances the position of each link in the snake
        for link in snake:
            link.moveLink()

        #the item that the snake has collided with
        collisionItem = self.collision(snake, food)
        if collisionItem == "food":
            self.addLink(snake)
            #Add points equal to number of pieces eaten
            self.score += len(snake) - self.originalLength
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
            pygame.draw.rect(screen, RED, [piece.xPos + 1,
                piece.yPos + 1, 4, 4])
        for link in snake:
            pygame.draw.rect(screen, BLACK, [link.xPos,
                        link.yPos, self.linkSize, self.linkSize])


def main():
    screen = pygame.display.set_mode((500, 500))
    snakeGame = Snake(screen)
    snakeGame.gameLoop()

if __name__ == "__main__":
    main()
