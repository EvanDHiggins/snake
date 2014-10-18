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

LINK_SIZE = 6
LINK_SPACING = 4
SCREEN_WIDTH = 236
SCREEN_HEIGHT = 236

def gameLoop():
    size = SCREEN_WIDTH, SCREEN_HEIGHT
    screen = pygame.display.set_mode(size)

    #End of Loop Boolean
    done = False

    clock = pygame.time.Clock()

    #Initialize Game Loop Variables
    snake = initializeSnake()
    numberOfFood = 0
    food = []

    while not done:
        #Elif statement for command interrupts
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if isLegalMove(snake[0], 'u'):
                        snake[0].setDirection('u')

                elif event.key == pygame.K_DOWN:
                    if isLegalMove(snake[0], 'd'):
                        snake[0].setDirection('d')

                elif event.key == pygame.K_LEFT:
                    if isLegalMove(snake[0], 'l'):
                        snake[0].setDirection('l')

                elif event.key == pygame.K_RIGHT:
                    if isLegalMove(snake[0], 'r'):
                        snake[0].setDirection('r')

                elif event.key == pygame.K_SPACE:
                    addLink(snake)

        # --- Game logic goes here ---
        numberOfFood = updateGame(snake, food, numberOfFood)
        

        # Overwrite Screen White
        screen.fill(WHITE)

        # --- Render here ---
        render(food, snake, screen)

        # Update Display
        pygame.display.flip()

        #Limit FPS
        clock.tick(15)

    pygame.quit()

def addLink(oldSnake):
    """Adds a link to the end of the snake directly behind the last link"""

    #The final link of the snake in order to derive
    # the next link's location and direction
    finalLink = oldSnake[len(oldSnake) - 1]
    newdirection = finalLink.getDirection()
    newX, newY = finalLink.getOffset()

    oldSnake.append(snakeLink(newdirection, newX, newY,
                                LINK_SIZE, LINK_SPACING))

def initializeSnake():
    snake = []
    #Create initial head link at arbitrarily chosen position
    snake.append(snakeLink('r', 50, 100, LINK_SIZE, LINK_SPACING))

    #Create 4 additional links behind head
    for i in range(4):
        addLink(snake)
    return snake

def nextMoves(snake):
    """Shifts moves down the snake"""
    tempSnake = snake[:]
    tempSnake.reverse()
    for link in range(0, len(tempSnake) - 1):
        tempSnake[link].setDirection(tempSnake[link+1].getDirection())
    return snake

def isLegalMove(head, move):
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

def collision(snake, food = []):
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
    if headXPos >= SCREEN_WIDTH or headXPos < 0:
        return "wall"
    elif headYPos >= SCREEN_HEIGHT or headYPos < 0:
        return "wall"

    for piece in food:
        if(piece.getXPosition() == headXPos
            and piece.getYPosition() == headYPos):
            food.remove(piece)
            return "food"

def addFood(food):
    """Generates random position for piece of food

    food: array of food pieces
    returns: void

    """
    xPos = random.randrange(0, SCREEN_WIDTH)
    xPos = xPos - (xPos % (LINK_SIZE + LINK_SPACING))
    yPos = random.randrange(0, SCREEN_HEIGHT)
    yPos = yPos - (yPos % (LINK_SIZE + LINK_SPACING))
    food.append(FoodPiece(xPos, yPos))

def updateGame(snake, food, numberOfFood):
    #Advances the position of each link in the snake
    for link in snake:
        link.moveLink()

    #the item that the snake has collided with
    collisionItem = collision(snake, food)
    if collisionItem == "food":
        addLink(snake)
        numberOfFood -= 1
    elif collisionItem == "self":
        quit()
    elif collisionItem == "wall":
        quit()

    if numberOfFood < 3:
        addFood(food)
        numberOfFood += 1

    snake = nextMoves(snake)
    return numberOfFood

def render(food, snake, screen):
    for piece in food:
        pygame.draw.rect(screen, RED, [piece.getXPosition() + 1,
            piece.getYPosition() + 1, 4, 4])
    for link in snake:
        pygame.draw.rect(screen, BLACK, [link.getXPosition(),
                    link.getYPosition(), LINK_SIZE, LINK_SIZE])


def main():
    gameLoop()

if __name__ == "__main__":
    main()
