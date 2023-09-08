import pygame

import sys

from scripts.utils import load_image
from scripts.entities import PhysicsEntity

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Platformer")
        # Create the screen
        self.screen = pygame.display.set_mode((640, 480))

        # Create the clock object to slow down the code
        self.clock = pygame.time.Clock()

        self.movement = [False, False]

        self.assets = {
            'player': load_image('entities/player.png')
        }

        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15)) # create a player entity
    def run(self):
        while True:
            self.screen.fill((14, 219, 248)) # refill the screen with a sky blue color every frame to keep moving images from leaving a trail
            self.player.update((self.movement[1] - self.movement[0], 0)) # update the player entity
            self.player.render(self.screen) # render the player entity
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN: # I made this wasd because I'm a rebel. I read arrow keys are more common because they support multiple keyboard types but to me it feels wrong. Recommended only for qwerty keyboards or you can modify to K_UP, K_DOWN etc.
                    if event.key == pygame.K_a:
                        self.movement[0] = True
                    if event.key == pygame.K_d:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_d:
                        self.movement[1] = False

            pygame.display.update()
            self.clock.tick(60) # 60 frames per second

Game().run()