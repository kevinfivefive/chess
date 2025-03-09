import pygame
import sys

from const import *
from game import Game

class Main:
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.game = Game()

        pygame.display.set_caption('Chess')

    def mainloop(self):
        
        screen = self.screen
        game = self.game

        while True:
            game.show_background(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()



            pygame.display.update()

main = Main()
main.mainloop()