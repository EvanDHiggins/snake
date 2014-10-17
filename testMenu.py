import pygame

pygame.init()

class GameMenu():
    def __init__(self, screen, menuItems, backgroundColor =(0, 0, 0),
                 font = None, fontSize = 30, fontColor = (255, 255, 255)):

        self.items = []
        self.font = pygame.font.SysFont(font, fontSize)
        for item in menuItems:
            label = self.font.render(item, 1, fontColor)
            self.items.append(label)

        self.screen = screen
        self.backgroundColor = backgroundColor
        self.clock = pygame.time.Clock()

    def run(self):
        done = False
        while not done:
            self.clock.tick(50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            self.screen.fill(self.backgroundColor)
            for label in self.items:
                self.screen.blit(label, (100, 100))
            pygame.display.flip()

if __name__ == "__main__":
    screen = pygame.display.set_mode((640, 480), 0, 32)
    pygame.display.set_caption('Game Menu')
    menuItems = ('Start', 'Quit')
    gm = GameMenu(screen, menuItems)
    gm.run()


