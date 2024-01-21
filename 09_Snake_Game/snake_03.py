#!/usr/bin/env python3
import pygame
import time


if __name__ == "__main__":
    # create/initialize a user interface
    # initialize the game
    pygame.init()
    # create a window
    dis = pygame.display.set_mode((400, 300))
    # update the window
    pygame.display.update()
    pygame.display.set_caption("Snake Game")
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                game_over = True
    # end the game
    pygame.quit()
    quit()
